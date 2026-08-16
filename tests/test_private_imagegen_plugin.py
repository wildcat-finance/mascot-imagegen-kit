"""Security and packaging contract for the private image-generation plugin."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "wildcat-brand-imagegen"
SKILL = PLUGIN / "skills" / "wildcat-brand-imagegen" / "SKILL.md"
HELPER = PLUGIN / "skills" / "wildcat-brand-imagegen" / "scripts" / "reference_session.py"
DESCRIPTOR = ROOT / ".wildcat-labs" / "private-plugin.json"
IMAGE_SUFFIXES = {".gif", ".jpeg", ".jpg", ".png", ".webp"}


def load_helper():
    spec = importlib.util.spec_from_file_location("reference_session", HELPER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class PrivateImagegenPluginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.helper = load_helper()

    def test_plugin_payload_contains_no_reference_images(self):
        payload_images = [
            path for path in PLUGIN.rglob("*") if path.is_file() and path.suffix.casefold() in IMAGE_SUFFIXES
        ]
        self.assertEqual(payload_images, [])

    def test_descriptor_installs_only_the_plugin_subtree(self):
        descriptor = json.loads(DESCRIPTOR.read_text(encoding="utf-8"))
        self.assertEqual(descriptor["source_subtree"], "plugins/wildcat-brand-imagegen")
        self.assertEqual(descriptor["authorization"], "fiat-contributor-check")
        self.assertEqual(descriptor["authentication"], "on-use")

    def test_semantic_triggers_and_exclusions_are_explicit(self):
        for phrase in (
            "Wildcat Protocol branding",
            "pointy ears",
            "narrow yellow eyes",
            "Wildcat guy",
            "pointy-eared cat character",
        ):
            self.assertIn(phrase, self.skill)
        self.assertIn("Do not use for unrelated image generation", self.skill)
        self.assertIn("merely because Hexaemeron or Fiat is running", self.skill)

    def test_skill_reuses_fiat_authorizer_and_requires_finally_cleanup(self):
        self.assertIn("check_wildcat_contributor.py", self.skill)
        self.assertIn("does not require a GitHub connector", self.skill)
        self.assertIn("In a `finally` path", self.skill)
        self.assertIn("Say\nnothing about the check", self.skill)

    @staticmethod
    def completed(returncode=0):
        return subprocess.CompletedProcess(["mock"], returncode, stdout="", stderr="")

    def fake_run(self, command):
        if command[0] == "gh":
            source = Path(command[4])
            (source / "assets").mkdir(parents=True)
            (source / "assets" / "internal-name.png").write_bytes(b"png")
            (source / "assets" / "another-secret.webp").write_bytes(b"webp")
            (source / "brand-guidelines.md").write_text("private guide", encoding="utf-8")
        return self.completed()

    def test_authorized_session_sanitizes_names_and_cleans_up(self):
        with tempfile.TemporaryDirectory() as authorizer_dir:
            authorizer = Path(authorizer_dir) / "check.py"
            authorizer.write_text("pass\n", encoding="utf-8")
            with mock.patch.object(self.helper, "_run", side_effect=self.fake_run):
                result = self.helper.begin(authorizer)
        self.assertIsNotNone(result)
        session_dir = Path(result["session_dir"])
        try:
            self.assertTrue(session_dir.is_dir())
            self.assertFalse((session_dir / ".source").exists())
            reference_names = [Path(path).name for path in result["reference_paths"]]
            self.assertEqual(reference_names, ["reference-001.webp", "reference-002.png"])
            self.assertNotIn("internal-name", json.dumps(result))
            self.assertNotIn("another-secret", json.dumps(result))
        finally:
            self.assertTrue(self.helper.end(session_dir))
        self.assertFalse(session_dir.exists())

    def test_rejected_authorization_is_silent_and_fetches_nothing(self):
        with tempfile.TemporaryDirectory() as authorizer_dir:
            authorizer = Path(authorizer_dir) / "check.py"
            authorizer.write_text("pass\n", encoding="utf-8")
            with mock.patch.object(self.helper, "_run", return_value=self.completed(returncode=1)):
                with mock.patch("sys.stdout") as stdout, mock.patch("sys.stderr") as stderr:
                    self.assertIsNone(self.helper.begin(authorizer))
                    stdout.write.assert_not_called()
                    stderr.write.assert_not_called()


if __name__ == "__main__":
    unittest.main()
