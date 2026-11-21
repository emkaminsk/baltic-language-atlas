# Baltic Language Atlas

Interactive 3D map of 61 languages of northern and eastern Europe: families, estimated divergence dates, word comparisons and contact (loanword) links. Focus on Baltic and Finnic languages and their relation to Polish and other Slavic languages.

- **Open locally:** `baltic-language-atlas.html` (data inlined; needs internet for fonts and three.js, otherwise falls back to the 2D map)
- **3D view:** the map is a curved slab of the globe at true scale (Earth's curvature visible); height is time, along the local vertical. Lift the family tree out of the map, play history from 4500 BCE, follow loanword arcs. The URL hash keeps the selection (`#f=pol&c=lit&y=-800`).
- **Published artifact:** https://claude.ai/artifact/NQaRBVdrjoJg8Jm4UeUXz5
- **Created:** 2026-11-14

## Files

- `baltic-language-atlas.html` - the page, with map geometry and all data inlined (the data line is generated, see below)
- `data/uralic.json` - Uralic languages and tree nodes
- `data/baltoslavic.json` - Baltic and Slavic languages, tree nodes, Polish-Lithuanian notes
- `data/others.json` - Germanic, Romance, Turkic languages, tree nodes, contact links
- `tools/build_data.py` - regenerates the inlined data from the JSON (`uv run tools/build_data.py`; `--check` reports drift). JSON is the golden source.

## Sources and methodology

Every word form, divergence date, contact link and Polish-Lithuanian card carries either a citation (`sources`) or a `low_confidence` flag. On the page, hover a word in the comparison table, a lineage step, the "broke up around" date, a tree node, a contact link or a card to see its source. Words without a published source are marked with a dotted underline and "?".

**How it was checked (2026-11-21).** Ten Claude subagents (Sonnet, with Haiku for Germanic and Romanian) each took one batch of languages or tree nodes. The coordinating session then reviewed their output before applying it.

- **Words.** For every one of the 12 concepts, each agent got two published sources:
  - the English Wiktionary translation table for that concept
  - NorthEuraLex 0.9 (Dellert et al. 2020), which covers 38 of the 61 languages

  Unresolved forms were looked up in Wiktionary entries, fi.wiktionary, Álgu and the EKI Votic dictionary. A romanisation of a sourced native-script form counts as a match; the atlas keeps its Latin transliterations. Where a source gave a different basic word, the value was corrected. Empty slots were filled only when a source attests the form explicitly. Nothing was guessed.
- **Dates.** Each tree node's `year`/`range` was compared with published estimates:
  - Uralic: Grünthal et al. 2022, Honkola et al. 2013, Kallio 2014
  - Balto-Slavic: Novotná & Blažek 2007 (glottochronology), Girdenis & Mažiulis 1994, Gray & Atkinson 2003
  - Indo-European: Heggarty et al. 2023, Bouckaert et al. 2012
  - Turkic and Germanic: Savelyev & Robbeets 2020, Dybo 2007, Ringe 2006

  A date was "confirmed" if it falls inside the published estimates. It was corrected if the sources clearly put it elsewhere. Some nodes rest on a proxy, such as a dated migration or the first written record; the citation says so. Some citations were read through Wikipedia articles that cite the handbook; these are marked "via Wikipedia".
- **Contacts and cards.** Loanword examples were checked against Wiktionary etymology sections, and wrong examples were replaced.
- **Review.** The coordinator rejected or adjusted some agent proposals:
  - Danish *én* was rejected; *en* stays, since Wiktionary lists it as the numeral.
  - The single-source Sudovian addition and an uncertain Polabian 'heart' were dropped.
  - Rusyn forms are flagged, because only Pannonian Rusyn entries were found.
  - A citation the agent had not actually retrieved was removed.
  - Kildin Sami additions cite the Cyrillic form they transliterate.

**Main sources:**
- Wiktionary (en, fi)
- NorthEuraLex 0.9 (Dellert et al. 2020, *Language Resources and Evaluation* 54)
- Álgu (Sámi etymological database)
- EKI *Vadja keele sõnaraamat*
- Grünthal et al. 2022, *Diachronica* 39(4)
- Honkola et al. 2013, *J. Evol. Biol.* 26(6)
- Kallio 2014, *The Diversification of Proto-Finnic*
- Novotná & Blažek 2007, *Baltistica* 42(2)
- Girdenis 1994, *Baltistica*
- Heggarty et al. 2023, *Science* 381
- Bouckaert et al. 2012, *Science* 337
- Gray & Atkinson 2003, *Nature* 426
- Savelyev & Robbeets 2020, *J. Language Evolution* 5(1)
- Ringe 2006
- Derksen 2008
- Dahl & Koptjevskaja-Tamm 2001, *The Circum-Baltic Languages*
- Visser 2022, *J. Germanic Linguistics*

Each entry's own `sources` field has the exact citation. Every value that changed is listed in `SOURCE_CHECK_CHANGES.md`.

**Coverage:**

| | entries | sourced | low confidence |
|---|---|---|---|
| Word forms | 669 | 632 | 37 |
| Tree nodes (dates) | 45 | 33 | 12 |
| Contact links | 30 | 27 | 3 |
| Polish-Lithuanian cards | 10 | 10 | 0 |

Low-confidence word forms (no published source found):
- **Meänkieli and Kven:** all words except 'one' and 'water', 10 each. A Finnish entry is not evidence for them, and their dictionaries could not be queried.
- **Ludian:** 'one', 'two'
- **Võro:** 'mother', 'winter'
- **Skolt Sami:** 'night'
- **Tundra Nenets:** 'one'
- **Samogitian:** 'two'
- **Old Prussian:** 'three', 'sun', 'name'
- **Silesian:** 'winter'
- **Rusyn:** 'two', 'three', 'water', 'fish'
- **Karaim:** 'name', 'fish'

Low-confidence dates (no published date for that specific split):
- West Sami
- East Sami
- South Estonian
- North Finnic
- Coastal Finnic
- West Baltic
- Lechitic
- West Norse
- East Norse
- High German
- Oghur
- Common Turkic

Low-confidence contact links:
- Russian → Komi-Zyrian
- Russian → Meadow Mari
- Tatar → Udmurt

Several Slavic dates (West, South, West South Slavic, Czech-Slovak, Sorbian) now follow the glottochronology of Novotná & Blažek 2007. That method dates the break-up of dialect continua late, and those notes say so.

## Caveats

- Divergence dates are model choices within published ranges; many published dates are themselves method-dependent (Bayesian phylogenetics vs glottochronology vs historical proxies).
- Source checks were done by language models reading Wiktionary, NorthEuraLex and papers. They are not a specialist's review, so check anything important against the cited source.
- Word lists for small or extinct languages are partly empty rather than guessed.
- "Spelling resemblance" is a crude letter-by-letter comparison and understates true cognates.
