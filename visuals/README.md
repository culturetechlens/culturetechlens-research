# CultureTechLens Visual Assets

CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

Shareable visual assets produced by CultureTechLens NFP for social media, classrooms,
and the global content program. All assets are original programmatic renders (Pillow/SVG) —
no AI-generated faces, no AI-generated likenesses, no stock imagery.

## License

All visual assets in this directory are released under **CC BY 4.0**, matching the
repository's open core. Attribution: `CultureTechLens. "Culture, Clearly Seen."
https://culturetechlens.com`

## Packs

| Folder | Contents |
|---|---|
| `audience-pack-2026-10-05/` | 13 social cards (1080×1080): CTL 10 Index leaderboard and data-story graphics, Clear Ear Award shortlist, quote cards, archive promos, working-paper promos. Includes `manifest.md` (per-file source data, captions, hashtags) and `build_cards.py` (re-runnable generator). |
| `templates-2026-10-05/` | 16 cards (1080×1080): reusable monthly Index announcement template set, 10-slide Black Memory Emergency carousel, Clear Ear Award countdown set. Includes `manifest.md`, `template-README.md` (monthly workflow), and the build scripts. |
| `true-size-of-africa-2026-10-05/` | "True Size of Africa" graphic (1920×1080): 11 countries drawn to true relative scale inside Africa's 30.37M km². Includes `manifest.md` with every area figure and its source. |
| `african-flags-2026-10-05/` | 55 African flags (800px wide) + `diaspora-strip.png` composite banner. Includes `manifest.md` with per-flag accuracy notes. |
| `educators-2026-10-05/` | 7 classroom visuals (1080×1080): lesson hook cards + the evidence-grades poster. Includes `visuals-manifest-2026-10-05.md`. |

## Honesty notes

- **Data graphics:** every number on the Index, paper, and archive cards is read from real
  CTL data files (Edition 2026-10 CSV, the Zenodo working papers, the knowledge graph).
  Nothing is invented; sources are listed in each pack's manifest.
- **African flags:** drawn from documented flag specifications. Complex emblems (e.g.
  Egypt's Eagle of Saladin, Eswatini's Nguni shield, Malawi's 31-ray sun) are simplified
  geometric abstractions — see the manifest's per-flag accuracy notes. Do not use these
  for vexillological reference; they are social/article illustrations.
- **True Size of Africa:** country shapes are schematic rectangles drawn to exact
  relative area; land-area figures are sourced to UN Statistics Division / FAO data
  (see manifest). Eastern Europe was omitted — no agreed definition.
- **Quote cards:** all quotes are verbatim from William Maxey's recorded statements.

## Reproducibility

Where a build script is included, the cards can be regenerated exactly by running it
(Python 3 + Pillow). Future monthly Index editions drop into `build_index.py`'s
`EDITIONS` dict to render new announcement cards.

---
Source: CultureTechLens
