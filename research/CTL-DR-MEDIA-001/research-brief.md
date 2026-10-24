# CTL-DR-MEDIA-001 — Research Brief
**"Who Controls the Story? The Black Media Infrastructure of America"**
Status: v0.1 research package complete | Date: 2026-09-28

## Central question
Who controls the Black media story in America, how did that control change, and what survived?

## Executive summary
Across print, radio, television, digital, and the economics underneath them, one pattern repeats: **the infrastructure that reaches Black audiences is increasingly not owned by Black institutions.** The largest Black-targeted assets — BET (Paramount Skydance), the iHeartMedia and Audacy urban radio portfolios — are non-Black-owned, while the Black-owned national core has consolidated into three operators: Urban One, Allen Media Group, and Essence Ventures. Policy is the hinge of the story: the 1978 Minority Tax Certificate built Black broadcast ownership (roughly 40 to ~323 minority-owned stations); its 1995 repeal plus the 1996 Telecommunications Act dismantled it (fewer than 180 of 11,000+ commercial stations Black-owned by 2020, ~1.6%, per NABOB). Advertising dollars structurally bypass Black media (multicultural media ~5.2% of total ad/marketing spend against ~40% of the population, per ANA/AIMM-PQ Media 2018 — industry-reported). Survival runs through four models: Black-capital buy-backs (Essence, Ebony, TheGrio, The Root), scale-and-diversification (Urban One), nonprofit/philanthropy conversion (Capital B, Word In Black), and corporate-IP consolidation (BET, Soul Train). The archival record itself is at risk: the 2022 JPC Archive rescue ($30M consortium purchase, joint NMAAHC/Getty ownership, 3–4M images plus A/V) is the century's largest Black-media archival event, and documented known loss exists (Schomburg's missing Garvey scrapbooks; Tennessee Black papers with no extant copies at all).

## Key findings
1. **Ownership ≠ targeting.** The distinction is the analytical spine: BET, iHeart/Audacy urban radio, and much Black-targeted cable are not Black-owned. (Verified)
2. **Policy built and broke Black radio ownership.** Minority Tax Certificate (1978) → growth; repeal (1995) + Telecom Act (1996) → collapse. (Verified)
3. **Family ownership is print's survival pattern.** The Murphys/AFRO (132 years), the Real Times Inc. rescue of the Sengstacke chain (2003, ~$12M), multigenerational ownership transfers. (Verified/Provisional)
4. **Ad spend bypasses Black media by industry-reported measures.** 5.2% multicultural share of spend; diverse-owned media 2.5% of largest holding companies' 2023 spend; $51M (1.02%) of $5B+ federal ad spend to Black-owned firms FY14–23 (GAO via NNPA). All labeled reported-not-independent. (Provisional)
5. **Carriage is the distribution choke point.** Allen's §1981 litigation produced Xfinity carriage (settled 2020–21); cable blackouts recur as leverage events. (Verified)
6. **Platform dependence is documented infrastructure risk.** Facebook's January 2018 feed shift hit dependent publishers industry-wide; Meta deprecated Facebook News (2024); Blavity's CEO confirms a Facebook page block forced revenue diversification. Correlational traffic-decline claims are NOT treated as proven causation. (Verified/Provisional)
7. **Digital ownership churn is extreme.** The Root cycled Washington Post Co. → Univision → G/O Media → Watering Hole Media, returning to Black ownership in October 2025. (Verified)
8. **The firsts are contested.** "First Black-owned station" (WERD 1949 vs. others), "first all-Black format" (WDIA 1948, white-owned), BET deal value ($2.3B vs ~$3B), BET full-time launch (1982 vs 1983) — all graded Disputed with both sides recorded. (Disputed)
9. **Nostalgia inflates print influence.** Historic circulation figures are self-reported/unaudited (Courier 350–400k; Muhammad Speaks 950k; Ebony 2M); readership-vs-circulation conflation is flagged throughout. (Provisional)
10. **Measurement is contested ground.** Nielsen's national accreditation was suspended by the MRC (Sept 2021–Apr 2023); Big Data + Panel accredited January 2025. Undercount critiques are documented; advocacy figures (VAB's "7B Black impressions") are labeled as advocacy. (Verified/Provisional)

## Coverage
- **140 deduplicated entities** (174 raw across 6 tracks; 34 duplicates merged via 22 merge groups, 0 merge conflicts), 482 graded claims: **297 Verified, 164 Provisional, 18 Disputed, 3 Unresolved**
- **255 timeline events**, 1827–2026 (206 Verified, 36 Provisional, 13 Disputed)
- **78 verified-only relationships** (17 single-source relationships held for corroboration in `_tracks/held-relationships.json`)
- **335 deduplicated sources: 45 primary, 290 secondary**
- Entity mix: 42 Business, 29 Person, 25 Publication, 19 Organization, 12 Institution, 6 Event, 4 Technology, 3 Policy

## Methodology
Six parallel research tracks (print beyond Chicago; Black radio; Black television; Black digital; infrastructure economics; archives/preservation/survival), each producing evidence-graded JSON against the CTL standard (claim, evidence, source, primary/secondary, publication/date, uncertainty, contradictory evidence, verification status). Tracks were merged programmatically (`_tracks/merge.py`): cross-track duplicates harmonized, relationships remapped and filtered to Verified-only, timeline normalized across three input schemas and sorted, sources deduplicated. **Red-team regrade applied** (`_tracks/regrade.py`): 38 claims marked Verified on Wikipedia-alone (or Wikipedia + Alchetron mirror) sourcing were downgraded to Provisional with audit notes. Full audit in `red-team.md`.

## Relationship to sibling projects
- **CTL-DR-BPM-003 (Chicago Black press, complete)** is the Chicago depth layer: Defender, Crusader, Johnson Publishing Chicago operations, WVON/WGCI, WJPC, Lyons, Saunders. MEDIA-001 does not redo it; Johnson Publishing appears here only via the national archive disposition and Ebony/Jet as national publications.
- **CTL-DR-MUSIC-001** will cover the music-ecosystem constellation; radio entities here (WDIA, WBLS, Urban One, AURN) are infrastructure nodes it can link to.

## Data-architecture note
Per the CTL standing principle, this package feeds the shared registries: entities carry claims → evidence → sources; timeline and relationship graph are machine-readable; all IDs are stable (`MED-001`–`MED-140`) for merging into the Black Cultural Knowledge Graph.

## What we know / think we know / remain unknown
See `gaps.md` for the full registers. In brief: the ownership arc and consolidation mechanics are well-documented; the economics of ad-spend bypass are industry-reported but not independently verified; the true scale of archival loss is unknowable from surviving records (survivorship bias is structural).

## Limitations
- 39% of originally-"Verified" claims rested on Wikipedia; 38 were downgraded to Provisional (the rest had independent corroboration). Re-sourcing is the top backlog item.
- No primary FCC Form 323 filings were reviewed; ownership counts are reported, not independently verified.
- Digital-track funding and traffic figures are largely founder-reported (primary but self-interested).
- See `red-team.md` and `gaps.md` for the complete accounting.
