# CULTURETECHLENS
## Culture, Clearly Seen. — Black Cultural Intelligence

# CTL-RB-CHI-000003 — Visuals Log

**Brief:** "Black Chicago's Commercial Corridors: Where They Developed, and Why"

## Archival-image sourcing status

A targeted attempt was made to source rights-cleared archival images:
- **Library of Congress item fsa2000020189/PP** (Farm Security Administration–Office of War Information photo by Russell Lee, Regal Theater, 1941, cited by CinemaTreasures user comment) — fetch of the item page returned HTTP 403 (access denied); per policy the request was not retried. Status: **unavailable-with-reason** (item identified but not verified/fetched).
- **Wikimedia Commons "Category:Regal Theater, Chicago"** — opened the live category page; it contains no media files. Status: **unavailable-with-reason** (no files uploaded).
- **CinemaTreasures Regal Theater page** — user-uploaded photo with no verifiable license statement. Status: **excluded** (unknown provenance; directive forbids).

**Decision:** all explanatory visuals are **data-driven graphics** built from research data (addresses, dates, grades from this brief's claim ledger and entities). These require no rights clearance and can be rendered at publication. The visuals/ subfolder is created with no downloaded files; the reason is documented here rather than hotlinking uncleared images.

---

## Visual 1 — Corridor map by era (data graphic)

- **Type:** data graphic — build at publish
- **Status:** build-at-publish
- **What it shows:** Base map of Chicago's South and West Sides with seven major corridors drawn as colored polylines (State St., 35th St., 47th St., Cottage Grove Ave., 63rd St., Madison St., 79th St.), each styled by peak era (1908–1945: State/35th; 1927–1960s: 47th/Cottage Grove; 1945–1975: 63rd/Madison; 1950s–present: 79th). Anchor institutions plotted as points with era-coded labels (Binga Bank 3633 S. State; Regal 4719 S. King Dr.; Sears 63rd & Halsted; South Side Trust & Savings 47th & Cottage Grove; Independence Bank 79th & Cottage Grove).
- **Why it explains:** Answers "where" in a single glance and makes the era-sequencing visible — the north-to-south, institution-to-retail drift of the Black commercial center.
- **Creator:** CTL research team (build at publish). **Date:** 2026. **Source institution:** CTL. **Rights:** CTL-owned work product, no clearance needed.
- **Caption draft:** "Seven corridors, four eras: Black Chicago's commercial center moved south — from State Street's 'Wall Street of the black community' (1908) to Chatham's 79th Street banks (1964–present)."
- **Build spec:** data source = entities.json (E-CORR-* with coordinates to be geocoded at build from addresses in brief §13); fields: corridor_id, name, peak_start, peak_end, era_color; rendering notes: lineweight by era prominence, anchor points with year labels.

## Visual 2 — Corridor comparison table/chart (data graphic)

- **Type:** data graphic — build at publish
- **Status:** build-at-publish
- **What it shows:** Rows = 7 corridors; columns = peak era, anchor institutions (2–4 each), anchor transit node, Black-ownership character (built / inherited / mixed), decline mechanism, evidence grade of the "why here" explanation.
- **Why it explains:** The comparative argument in one artifact — shows the pattern (white-built → Black succession → disinvestment) holds across corridors, and where it doesn't (35th Street's Black capital exception; 79th's survival).
- **Creator/date/institution/rights:** as Visual 1.
- **Caption draft:** "Every major corridor followed the same sequence — white-built, Black succession, disinvestment — except the 35th Street capital core, which Black bankers built themselves."
- **Build spec:** data source = brief §08 + claim-ledger CL-001–CL-030; fields: corridor, peak_era, anchors, transit_node, ownership_character, decline_mechanism, why_here_grade; render as styled HTML table (no image rights issues).

## Visual 3 — Transit-overlay map (data graphic)

- **Type:** data graphic — build at publish
- **Status:** build-at-publish
- **What it shows:** CTA 'L' infrastructure (South Side Elevated/main line, Englewood/Ashland branch, Jackson Park/East 63rd branch, Lake Street elevated) overlaid with the seven corridors, highlighting station–corridor adjacencies (47th station 1892 → 47th corridor; 35th–Bronzeville–IIT → 35th corridor; Halsted/63rd + Cottage Grove stations → 63rd corridor; Lake St. elevated → Madison corridor). Includes the caution annotation: "Rails predate the Black city; transit marks where commerce clustered, not why it was Black."
- **Why it explains:** Directly tests and illustrates the brief's causation discipline — adjacency is visible and honest, while the annotation prevents the map from implying transit *caused* Black commercial density.
- **Creator/date/institution/rights:** as Visual 1.
- **Caption draft:** "The 'L' stations mark where each corridor's commerce clustered — but every line was built for a white city first. Transit explains the 'where along,' not the 'why Black.'"
- **Build spec:** data source = CTA station data (stations + opening dates in §10/§16) + corridor polylines; fields: line, station, opened_date, corridor_id; rendering notes: muted transit lines, highlighted corridors, footnote-style caution annotation.

## Visual 4 — Rise/decline timeline per corridor (data graphic)

- **Type:** data graphic — build at publish
- **Status:** build-at-publish
- **What it shows:** Horizontal swimlane timeline, 1890–2026, one lane per corridor, with rise phase (green), peak (gold), decline (red) spans; event markers: Binga Bank 1908; Regal/Savoy 1927–28; Sears dispute 1929/34; Independence Bank 1964; 1968 uprisings; Sears closure 1976; Regal demolition 1973; el demolition 1982–97; Target at Chatham 2002.
- **Why it explains:** Makes the two-era model and the staged destruction visible — the northern institutional corridors peak before 1950, the retail corridors after, and decline clusters around dated policy events rather than smooth decay.
- **Creator/date/institution/rights:** as Visual 1.
- **Caption draft:** "Institutional corridors peaked before 1950; retail corridors after. Decline came in dated shocks — 1962, 1968, 1973, 1976, 1982, 1997 — not gradual decay."
- **Build spec:** data source = brief §10 timeline; fields: corridor, phase_start, phase_end, phase_type, event markers; rendering notes: color-coded phases, diamond event markers with year labels.

## Visual 5 — Ownership-pattern diagram (data graphic)

- **Type:** data graphic — build at publish
- **Status:** build-at-publish
- **What it shows:** For each corridor, a two-segment bar: documented Black-owned anchor capital vs. white-developed/financed capital vs. unknown (e.g., 47th: Regal–Savoy white-developed until 1961; 35th: Black-built; 63rd: largely unknown — visually shows the evidence gap; Madison: unknown).
- **Why it explains:** Makes Finding 2 (succession, not founding) and the "Black markets on white capital" structure visible, and — critically — makes the *evidence gaps* visible rather than filling them.
- **Creator/date/institution/rights:** as Visual 1.
- **Caption draft:** "Who built the corridors? Black capital built 35th Street; white capital built the rest. For 63rd and Madison, the ownership record is the gap."
- **Build spec:** data source = claim-ledger + sibling records; fields: corridor, black_built_share, white_built_share, unknown_share, evidence_note; rendering notes: stacked bar with hatched "unknown" segments.

## Visual 6 — Container → succession → disinvestment model diagram (data graphic)

- **Type:** data graphic — build at publish
- **Status:** build-at-publish
- **What it shows:** Three-panel flow diagram: (1) "The container" — HOLC D74 map shape, covenant boundary, captive dense population; (2) "Succession" — white-built strip → Black patronage → selective Black ownership; (3) "Disinvestment" — dated shocks (1968, expressway, anchor closures, transit withdrawal) → hollowed corridor. Small caution: "Correlation ≠ causation; transit's role graded PROVISIONAL."
- **Why it explains:** The brief's causal framework as a single teaching graphic; the caution box preserves the evidence discipline.
- **Creator/date/institution/rights:** as Visual 1.
- **Caption draft:** "How the corridors formed — and fell: segregation contained the market, succession filled it, disinvestment emptied it."
- **Build spec:** conceptual diagram from brief §09; fields: panel, mechanism, dated_evidence; rendering notes: three panels, arrows, small-print caution.

---

## Video

**Selected: 1 video (embeddable status to be re-checked at publication; treated as link-pending).**

- **Title:** "Bronzeville, the Black Metropolis"
- **Channel:** Language and Life Project (NC State University)
- **Video ID / URL:** u6WRG66ZwU0 — https://youtube.com/watch?v=u6WRG66ZwU0
- **Upload date:** c. 2017 (search index: ~3,336 days before 2026-09-28)
- **Uploader:** Language and Life Project at NC State (production credited in description)
- **Why selected:** Genuine oral-history interview excerpt with Harold Lucas, Bronzeville preservationist and historian, recorded for the PBS documentary *Talking Black in America*. Explains the "narrow band of land" container mechanism and the cultural fluorescence inside it — directly supports this brief's central causal finding. Not a full work, not a reupload of unknown provenance.
- **Timestamp range:** Full clip relevant (short excerpt; interview format). Segment of interest for this brief: Lucas's description of housing-covenant confinement producing the Bronzeville corridor economy (exact timestamps to be logged when embedded at publication).
- **Embed status:** not verified at research time — record as **link-only pending re-check at publication**.
- **Relevance check:** description and transcript metadata verified via page fetch (2026-09-28). Video is illustrative only; no claim in this brief rests on it.

**Excluded with reason:**
- "Bronzeville, Chicago: The Kitchenette Flats Behind the Black Metropolis" (youtube.com/watch?v=YzZLmhbeHGA) — **excluded**: the video's own description discloses that its reconstructions and narration are AI-generated. Per directive: never AI-generated content. Its *source list* (Drake & Cayton 1945; Chicago Commission on Race Relations 1922; Hirsch 1983) was noted as a reading list only.
- "Bronzeville, 1955: The REALITY of the Midwest's Wealthiest Black Neighborhood" (youtube.com/watch?v=F7Qbbi2HBHY) — **excluded**: AI-generated imagery/narration per its own disclosure.
- "Englewood, Chicago in the 1970s" (youtube.com/watch?v=wO2rNQvqPA4) — **excluded**: nostalgia-channel content with unsourced claims (e.g., specific Sears details); not institutional.
- WTTW "DuSable to Obama: Chicago's Black Metropolis" YouTube copy (youtube.com/watch?v=TWtSr8gkJGA) — **excluded**: provenance of the YouTube copy is unclear (possible unauthorized reupload of a full documentary). The PBS streaming page (video.pbsnc.org) is the authoritative link; note it in sources.md as institutional media, not embedded.

---

*CULTURETECHLENS — Culture, Clearly Seen. — Black Cultural Intelligence · CTL-RB-CHI-000003 visuals.md v0.1*
