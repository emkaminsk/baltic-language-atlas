# Baltic Language Atlas

Interactive map of 61 languages of northern and eastern Europe: families, estimated divergence dates, word comparisons and contact (loanword) links. Focus on Baltic and Finnic languages and their relation to Polish and other Slavic languages.

- **Open locally:** `baltic-language-atlas.html` (self-contained; needs internet only for fonts)
- **Published artifact:** https://claude.ai/artifact/NQaRBVdrjoJg8Jm4UeUXz5
- **Created:** 2026-11-14

## Files

- `baltic-language-atlas.html` - the page, with map geometry and all data inlined
- `data/uralic.json` - Uralic languages and tree nodes
- `data/baltoslavic.json` - Baltic and Slavic languages, tree nodes, Polish-Lithuanian notes
- `data/others.json` - Germanic, Romance, Turkic languages, tree nodes, contact links

The page overrides some entries of `data/others.json` at build time (native spelling of words and endonyms for Swedish, Icelandic, Faroese, Romanian, Tatar, Chuvash, Crimean Tatar, Karaim), so the page is the reference for those.

## Caveats

- Dates and word forms come from model reference knowledge and were not verified against web sources.
- Several internal Finnic splits and the Samogitian and Latgalian dates are low-confidence simplifications.
- Word lists for small or extinct languages are partly empty rather than guessed.
- "Spelling resemblance" is a crude letter-by-letter comparison and understates true cognates.
