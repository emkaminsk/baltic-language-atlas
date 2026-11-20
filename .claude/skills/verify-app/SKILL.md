---
name: verify-app
description: Check the atlas page and data before publishing. Validates the JSON files, checks JSON/HTML sync, serves the page locally and inspects it in light and dark mode. Use before every publish and whenever asked to verify or test the page.
---

# Verify the atlas

There is no test suite. Run these checks from the project root (`baltic-language-atlas/` is the nested dir with the HTML).

1. **JSON validity**
   ```bash
   for f in baltic-language-atlas/data/*.json; do python3 -m json.tool "$f" >/dev/null && echo "ok $f"; done
   ```
2. **Sync**: for every language or node touched, confirm the inlined data in the HTML matches the JSON exactly.
3. **Serve and look**
   ```bash
   cd baltic-language-atlas && python3 -m http.server 8000
   ```
   Open http://localhost:8000/baltic-language-atlas.html (or drive it with the `webapp-testing` skill). Check:
   - no console errors
   - the map, family tree, word comparison and contact links render
   - light and dark mode (`prefers-color-scheme`, and `data-theme="light"`)
   - layout holds at ~375px width
   - 3D view: dots render, click picks, "Lift family tree" and "Play history" animate, contact arcs show; the 2D toggle still works
   - Headless Chromium needs WebGL flags: `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader` (run Playwright with `uv run --with playwright`)
4. **Data rules**: no invented word lists; low-confidence dates flagged in `note`.

Report what was checked and anything that failed. Fix the page or data, not the check.
