# Monthly Index Announcement Template Set — README

**CULTURETECHLENS** · *"Culture, Clearly Seen."* · Black Cultural Intelligence

This folder holds a **data-driven template system** for the monthly CTL 10 Index
announcement graphics. The design is fixed; only the data changes each month.

## How it works

`build_index.py` contains an `EDITIONS` dict. Each edition is one entry:

```python
"2026-11": dict(
    topic="MOMENTS",                                        # ← monthly slot 1: edition topic
    method_url="culturetechlens.com/research/culturetechlens-index/methodology/",
    rows=[
        ("Item name", 78.8, 33922),                        # ← monthly slot 2: (name, score, pageviews)
        ...                                                #    all 10 ranked items, top first
    ],
),
```

To publish a new month: add the edition entry, run `python3 build_index.py`.
Three 1080×1080 PNGs render automatically:

| File | Purpose |
|---|---|
| `index-{YYYY-MM}-announcement.png` | The edition announcement: topic, #1 item + score, top three |
| `index-{YYYY-MM}-leaderboard.png` | Full 10-item ranking with score bars |
| `index-{YYYY-MM}-paradox.png` | The data-story card: highest-attention item vs. deepest-evidence item |

## Monthly slots (the only things that change)

1. **Edition key + topic** — e.g. `2026-11`, `MOMENTS`
2. **The 10 rows** — `(name, score, wikipedia_pageviews)`, ranked top-first, from the real edition CSV
3. **The paradox pair** — auto-selected as row 1 (top score) vs. row 9 (deepest evidence); if a future edition's deepest-evidence item isn't row 9, edit `render_paradox` to pick by the evidence column

## Design tokens (do not change without founder approval)

- Palette: black `#080808` · deep red `#A51C30` · bronze `#8A5A2B` · gold `#c99a5e` · ink `#E8E0D2` · muted `#b3a894`
- Headlines: DejaVu Serif Bold · Body: DejaVu Sans · Eyebrows: tracked DejaVu Sans Bold
- Backgrounds: `assets/texture-archival-dark.png`, `assets/texture-crimson-bronze.png` (AI-generated abstract textures, no faces, no text)
- Every card carries the brand footer: CULTURETECHLENS · "Culture, Clearly Seen." · culturetechlens.com
- Layout guard: `build_carousel.py` prints `LAYOUT WARNING` if any text block runs past y=918 — fix by trimming copy, never by shrinking the footer zone

## Source of truth

Scores and pageviews come from the edition's `index-scores.csv`
(`~/workspace/culturetechlens/programs/culturetechlens-index/editions/{YYYY-MM}/`).
Never type scores by hand — copy them from the CSV.
