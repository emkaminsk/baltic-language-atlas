# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Static, no-build project: one page, `baltic-language-atlas/baltic-language-atlas.html` (CSS, JS, map geometry and all data inlined; three.js 0.170.0 from jsdelivr via an importmap), plus reference data in `baltic-language-atlas/data/{uralic,baltoslavic,others}.json`. No package manager, tests or linter; one stdlib build script, `tools/build_data.py`. The page is published as a claude.ai artifact (URL in `README.md`); Claude regenerates/patches the HTML and republishes it. Use `/verify-app` before publishing and `/deploy` to publish.

## Data rules

- **Never guess word lists.** Leave words empty for small or extinct languages rather than inventing forms. Dates and word forms are unverified model knowledge; flag low-confidence ones in the `note` field.
- **JSON is the golden source.** Edit `data/*.json`, then run `uv run tools/build_data.py` to regenerate the inlined `const D = ...` line (derives `g` and map `x, y` from the lineage and `lat, lon`); `--check` reports drift. Never hand-edit that line.
- **Provenance:** every word needs a citation in the language's `sources` map or its concept in `low_confidence`; nodes, contacts and cards carry `sources` (list) and `low_confidence` (bool). The UI shows these as hover tooltips.
- Each tree node is defined once, in the JSON file of its family (`indo-european` lives in `others.json`).
- Language schema: `id, name, endonym, family, parent, speakers_m, status, lat, lon, where, note, words, sources, low_confidence`. Each file also has tree nodes; `others.json` has top-level `languages`, `nodes`, `contacts` (loanword links).
- Verify in a browser (light and dark mode) before republishing.

## Gotchas

- Two scripts: the classic one owns data, state `S`, the 2D SVG map, panel and tree; the `type="module"` one is the 3D view and only reads those globals and exposes `window.atlas3d` (`update`, `setActive`, `setLift`, `zoom`, `reset`). `drawMap()` routes to 3D or 2D.
- 3D encoding: height = `sqrt(NOW - year)`, the same compression as the tree; ancestors sit over their descendants' centroid (a layout choice, not a homeland).
- 3D globe: the inlined map geometry is a Lambert conformal conic (constants fitted to the graticule, in `LCC`). The 3D module keeps all logic in flat map space (x, height, z) and `bend()` / `bendGeo()` wrap it onto a sphere of true-scale radius, height along the local vertical. Anything new placed in 3D must go through `bend()`.
- Without WebGL or the CDN the module never runs and the 2D map stays (3D button disabled). Fonts and three.js need internet; the 2D page works offline.
- Dark mode uses `prefers-color-scheme` with a `data-theme="light"` override. Keep new CSS on the existing custom properties.
- `.claude/agents/` still holds agents copied from an unrelated dice-roll project (`game-builder`, `fairness-auditor`, ...). Ignore them; they don't describe this repo.
