#!/usr/bin/env python3
"""Create and destroy fail-silent, request-scoped Wildcat reference sessions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Sequence


PRIVATE_REPOSITORY = "wildcat-finance/mascot-imagegen-kit"
SESSION_PREFIX = "wildcat-brand-imagegen-"
SENTINEL = ".wildcat-brand-session"
IMAGE_SUFFIXES = {".gif", ".jpeg", ".jpg", ".png", ".webp"}
TIMEOUT_SECONDS = 120


def _run(command: Sequence[str]) -> subprocess.CompletedProcess[str] | None:
    try:
        return subprocess.run(
            list(command),
            check=False,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.SubprocessError):
        return None


def _authorised(authorizer: Path) -> bool:
    if not authorizer.is_file() or authorizer.is_symlink():
        return False
    result = _run([sys.executable, str(authorizer)])
    return result is not None and result.returncode == 0


def _copy_references(source: Path, session_root: Path) -> dict[str, object] | None:
    assets = source / "assets"
    guide = source / "brand-guidelines.md"
    if not assets.is_dir() or not guide.is_file() or guide.is_symlink():
        return None

    candidates = sorted(
        path
        for path in assets.rglob("*")
        if path.is_file() and not path.is_symlink() and path.suffix.casefold() in IMAGE_SUFFIXES
    )
    if not candidates:
        return None

    references = session_root / "references"
    references.mkdir(mode=0o700)
    copied: list[str] = []
    for index, original in enumerate(candidates, start=1):
        destination = references / f"reference-{index:03d}{original.suffix.casefold()}"
        shutil.copyfile(original, destination)
        destination.chmod(0o600)
        copied.append(str(destination))

    guide_destination = session_root / "brand-guidelines.md"
    shutil.copyfile(guide, guide_destination)
    guide_destination.chmod(0o600)
    return {
        "session_dir": str(session_root),
        "brand_guide": str(guide_destination),
        "reference_paths": copied,
    }


def begin(authorizer: Path) -> dict[str, object] | None:
    if not _authorised(authorizer):
        return None

    session_root: Path | None = None
    try:
        session_root = Path(tempfile.mkdtemp(prefix=SESSION_PREFIX)).resolve()
        session_root.chmod(0o700)
        source = session_root / ".source"
        clone = _run(
            [
                "gh",
                "repo",
                "clone",
                PRIVATE_REPOSITORY,
                str(source),
                "--",
                "--depth=1",
                "--filter=blob:none",
                "--sparse",
            ]
        )
        if clone is None or clone.returncode != 0:
            raise RuntimeError("private source unavailable")
        sparse = _run(
            [
                "git",
                "-C",
                str(source),
                "sparse-checkout",
                "set",
                "assets",
                "brand-guidelines.md",
            ]
        )
        if sparse is None or sparse.returncode != 0:
            raise RuntimeError("private references unavailable")

        result = _copy_references(source, session_root)
        if result is None:
            raise RuntimeError("private references invalid")
        shutil.rmtree(source)
        (session_root / SENTINEL).write_text("wildcat-brand-imagegen-session-v1\n", encoding="utf-8")
        (session_root / SENTINEL).chmod(0o600)
        return result
    except Exception:
        if session_root is not None:
            shutil.rmtree(session_root, ignore_errors=True)
        return None


def end(session_dir: Path) -> bool:
    try:
        resolved = session_dir.resolve(strict=True)
        temp_root = Path(tempfile.gettempdir()).resolve(strict=True)
        sentinel = resolved / SENTINEL
        if (
            resolved.parent != temp_root
            or not resolved.name.startswith(SESSION_PREFIX)
            or not sentinel.is_file()
            or sentinel.is_symlink()
            or sentinel.read_text(encoding="utf-8") != "wildcat-brand-imagegen-session-v1\n"
        ):
            return False
        shutil.rmtree(resolved)
        return not resolved.exists()
    except (OSError, UnicodeError):
        return False


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    begin_parser = subparsers.add_parser("begin")
    begin_parser.add_argument("--authorizer", required=True, type=Path)
    end_parser = subparsers.add_parser("end")
    end_parser.add_argument("--session-dir", required=True, type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "begin":
        result = begin(args.authorizer)
        if result is None:
            return 1
        print(json.dumps(result, sort_keys=True))
        return 0
    return 0 if end(args.session_dir) else 1


if __name__ == "__main__":
    sys.exit(main())
