---
name: add-language
description: Recipe for adding or editing a language (or tree node / contact link) in the Baltic Language Atlas, keeping the JSON files and the inlined HTML data in sync. Use whenever data entries change.
---

# Add or edit a language

1. **Pick the file** by family: `uralic.json`, `baltoslavic.json`, or `others.json` (Germanic, Romance, Turkic, tree nodes, `contacts`).
2. **Follow the schema** of neighbouring entries: `id, name, endonym, family, parent, speakers_m, status, lat, lon, where, note, words`. `parent` must reference an existing tree node id. Add a tree node first if needed.
3. **Words**: only include forms you are confident of. For small or extinct languages leave `words` empty rather than guessing. Put uncertainty about dates, splits or forms in `note`.
4. **Mirror the change in the inlined data** in `baltic-language-atlas.html`. The same entry must exist in both places.
5. **Update counts** in `README.md` (currently "61 languages") and any count shown on the page.
6. Run `/verify-app`, then `/deploy` if the user wants it published.
