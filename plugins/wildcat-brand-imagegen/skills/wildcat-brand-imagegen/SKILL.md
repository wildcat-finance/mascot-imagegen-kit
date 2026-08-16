---
name: wildcat-brand-imagegen
description: Use with image generation or image editing when the request explicitly calls for Wildcat Protocol branding, the Wildcat mascot or brand character, or the recognizable lean light-grey or white cat-like figure with an angular head, tall pointy ears, narrow yellow eyes, and a dry or intelligent expression. Match indirect phrases such as the Wildcat guy, pointy-eared cat character, mascot meme, or established Wildcat visual style. Do not use for unrelated image generation, generic cats or foxes, or merely because Hexaemeron or Fiat is running.
---

# Wildcat brand image generation

Use the normal image-generation skill and tool for the actual image. This skill
adds private reference material to a matching request; it does not replace the
image-generation workflow.

## Boundary

Run this workflow only after the description above matches the user's image
request. Do not fetch references during skill discovery, plugin installation,
an ordinary Fiat run, or unrelated image generation.

Use Fiat's contributor check as the sole authorization decision. Locate
`check_wildcat_contributor.py` under the installed Hexaemeron Fiat skill. The
check deliberately supports an already-authenticated local `gh` account and
does not require a GitHub connector. Do not substitute a user claim, repository
commit author, fuzzy name match, or a second identity system.

If the Fiat check is unavailable, returns non-zero, or the reference session
cannot start, continue the image request without private references. Say
nothing about the check, source repository, missing references, private plugin,
or failure. Never ask the user for affiliation evidence or credentials.

## Request-scoped reference session

1. Run:

   ```text
   python3 "$SKILL_DIR/scripts/reference_session.py" begin \
     --authorizer "/absolute/path/to/check_wildcat_contributor.py"
   ```

2. A successful command prints one JSON object containing a session directory,
   the brand guide, and generic local reference paths. Read the guide. Use the
   returned reference paths with the normal image-generation tool. Do not show,
   enumerate, describe, attach, or otherwise surface the reference library to
   the user.
3. Keep the user's requested subject, format, dimensions, and edits
   authoritative. Apply the guide and references only to Wildcat brand identity
   and visual treatment.
4. In a `finally` path after the image tool succeeds, fails, or is cancelled,
   run:

   ```text
   python3 "$SKILL_DIR/scripts/reference_session.py" end \
     --session-dir "/absolute/path/from-the-begin-result"
   ```

5. Confirm cleanup by the command's zero exit status. Never retain, cache,
   index, commit, upload separately, or copy the guide or references outside
   that session directory.

The source images may contain captions, backgrounds, interfaces, or other
characters. Treat only the established mascot identity as authoritative unless
the user explicitly requests another referenced element.
