# 3D atlas + modernisation (2026-11-20)

Concept: **time is height.** The map is a 3D relief table; ancestors float above it at a height set by their break-up date (same sqrt compression as the tree). Each language's dot rides up its lineage curve as the year goes back, so sister languages physically merge at their common ancestor.

## Plan
- [x] Review: data sync, layout, a11y, console (findings in review section)
- [x] three.js (pinned 0.170.0, jsdelivr ES module + importmap) as a `<script type="module">` reusing existing state `S`, `pick()`, `render()`
- [x] Land: parse the inlined SVG path (M/L/Z only) into THREE.Shape, extrude, coast + border lines
- [x] Languages: instanced beads (size = speakers, colour = family / kinship), extinct = hollow ring
- [x] Lineage canopy: bezier tubes leaf → ancestor; "Lift tree" toggle animates height 0 ↔ 1
- [x] Year slider drives bead position along lineage curves; translucent "time sheet" at the year; Play button animates 4500 BCE → today
- [x] Contact arcs: 3D arcs with particles flowing borrower-ward (from → to), clickable
- [x] Selection: raycast click/hover, highlighted path to the last common ancestor, LCA node label (dropped: auto camera move on select, felt disorienting)
- [x] HTML labels (CSS2DRenderer) themed by CSS vars, screen-space collision hiding
- [x] Theme sync (light/dark), prefers-reduced-motion, pause when offscreen, WebGL/CDN fallback to the 2D SVG map
- [x] 2D/3D segmented toggle; 2D map kept (keyboard access, fallback)
- [x] Modern touches: language search, shareable URL hash, refreshed surface styling
- [x] Fixes: tree left clipping, `<title>` into `<head>`, sync JSON to HTML (drop "override" gotcha)
- [x] Verify: Playwright screenshots light/dark/375px, no console errors, interactions
- [x] Update CLAUDE.md / README / skills (three.js CDN dependency), commit + push
- [ ] Publish with `/deploy` (user-triggered)

## Review

- Data: `others.json` had drifted from the page for 9 languages beyond spelling (Norwegian/Karaim names, Low German endonym, Chuvash *anne*/*śĕr* missing); synced JSON to the page. `indo-european` was defined twice with conflicting confidence (medium vs low); removed the stale copy in `baltoslavic.json`.
- Page: tree clipped on the left ("uropean", "4000 BCE"); `<title>` was in `<body>`; no shareable state; 2D labels collide in the Baltic.
- Verified (headless Chromium, swiftshader WebGL): no console errors; 3D flat/lifted, light/dark, 375px with reduced motion, no horizontal overflow; hover tip, click-to-compare, search, URL hash, play/pause, contact arcs, kinship colour, 2D toggle.
- Open: selected labels may overlap each other (they bypass collision by design); endonyms such as Russian are transliterated (`russkii iazyk`) rather than in native script; the 3D view needs the jsdelivr CDN.
