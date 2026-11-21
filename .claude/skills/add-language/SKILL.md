---
name: add-language
description: Recipe for adding or editing a language (or tree node / contact link) in the Baltic Language Atlas, keeping the JSON files and the inlined HTML data in sync. Use whenever data entries change.
---

# Add or edit a language

1. **Pick the file** by family: `uralic.json`, `baltoslavic.json`, or `others.json` (Germanic, Romance, Turkic, tree nodes, `contacts`).
2. **Follow the schema** of neighbouring entries: `id, name, endonym, family, parent, speakers_m, status, lat, lon, where, note, words`. `parent` must reference an existing tree node id. Add a tree node first if needed.
3. **Words**: only include forms you can cite. For small or extinct languages leave `words` empty rather than guessing. Every non-empty word needs a citation in `sources` (`{"<concept>": "Wiktionary: vesi (Finnish)"}`) or its concept listed in `low_confidence` (and named in `note`). Tree nodes, contacts and Polish-Lithuanian cards take `sources` (list of citations) and `low_confidence` (true when nothing was found). See README "Sources and methodology".
4. **Regenerate the inlined data**: `uv run tools/build_data.py`. Never hand-edit the `const D = ...` line in the HTML; JSON is the golden source.
5. **Update counts** in `README.md` (currently "61 languages") and any count shown on the page.
6. Run `/verify-app`, then `/deploy` if the user wants it published.
