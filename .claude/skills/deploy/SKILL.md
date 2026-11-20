---
name: deploy
description: Republish the atlas page to its claude.ai artifact (URL in README.md). Use when asked to publish, deploy, ship or update the live page.
disable-model-invocation: true
---

# Publish

The page is published as a claude.ai artifact; there is no server or CI.

1. Run `/verify-app`. Stop and report if anything fails.
2. Read the artifact URL from `README.md`.
3. Publish with the Artifact tool: `action: "publish"`, `url: <that URL>`, `file_path: <absolute path to baltic-language-atlas/baltic-language-atlas.html>`. Updating in place keeps the link. The tool may require reading the artifact first.
4. Report the URL and what changed. If the URL ever changes, update `README.md`.

Only the HTML is published; the page must stay self-contained (data inlined; only Google Fonts loaded externally).
