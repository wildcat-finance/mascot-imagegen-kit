# mascot-imagegen-kit

A small reference kit for generating consistent Wildcat mascot imagery: canonical reference images, prompt fragments, style notes, and examples for face swaps, redraws, meme formats, and other deeply regrettable acts of brand stewardship.

This one. this is the repo we go to jail for.

## Agent access

The installable payload is only `plugins/wildcat-brand-imagegen`; it contains
instructions and a fetch helper, not the reference images or brand guide. The
private-plugin descriptor at `.wildcat-labs/private-plugin.json` lets an
eligible Fiat run discover and copy that subtree without cloning this
repository into a plugin cache.

Authorization reuses Hexaemeron Fiat's
`check_wildcat_contributor.py`. It checks an already-authenticated local GitHub
account first, so a GitHub connector is optional. Failed or inconclusive checks
are silent. Do not replace this with a second user or email allowlist.

For matching Wildcat branding or mascot image requests, the installed skill
creates a private request-scoped temporary directory, sparse-fetches the guide
and references, passes them to the image-generation tool, and deletes the
directory in a `finally` path. Installation, ordinary Fiat work, and unrelated
image generation do not fetch the references.

Operator checks:

```text
python3 -m unittest discover -s tests
python3 <plugin-creator>/scripts/validate_plugin.py plugins/wildcat-brand-imagegen
python3 <skill-creator>/scripts/quick_validate.py plugins/wildcat-brand-imagegen/skills/wildcat-brand-imagegen
```
