# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Static, no-build project: one self-contained page, `baltic-language-atlas/baltic-language-atlas.html` (CSS, JS, map geometry and all data inlined), plus reference data in `baltic-language-atlas/data/{uralic,baltoslavic,others}.json`. No package manager, tests, linter or git repo. The page is published as a claude.ai artifact (URL in `README.md`); Claude regenerates/patches the HTML and republishes it. Use `/verify-app` before publishing and `/deploy` to publish.

## Data rules

- **Never guess word lists.** Leave words empty for small or extinct languages rather than inventing forms. Dates and word forms are unverified model knowledge; flag low-confidence ones in the `note` field.
- **Keep JSON and inlined HTML data in sync.** Any data change goes in both places.
- **The HTML overrides some `others.json` entries** (native spellings/endonyms for Swedish, Icelandic, Faroese, Romanian, Tatar, Chuvash, Crimean Tatar, Karaim). For those, the HTML is the reference and the JSON is stale. Check the HTML before editing them.
- Language schema: `id, name, endonym, family, parent, speakers_m, status, lat, lon, where, note, words`. Each file also has tree nodes; `others.json` has top-level `languages`, `nodes`, `contacts` (loanword links).
- Verify in a browser (light and dark mode) before republishing.

## Gotchas

- Fonts load from Google Fonts; everything else works offline.
- Dark mode uses `prefers-color-scheme` with a `data-theme="light"` override. Keep new CSS on the existing custom properties.
- `.claude/agents/` still holds agents copied from an unrelated dice-roll project (`game-builder`, `fairness-auditor`, ...). Ignore them; they don't describe this repo.
