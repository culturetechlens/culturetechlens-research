# CTL-DR-GLOBAL-001 — Red Team Report

**Date:** 2026-09-28
**Auditor:** dedicated red-team worker over the six-track merged corpus
**Scope:** all 213 merged entities, 371 claims, 163 relationships, 265 sources, 65 negative findings

## Verdict

**Not publication-ready as a research base — but honest.** The corpus has a serious negative-findings apparatus, contradictory evidence is usually recorded rather than hidden, and several tracks made genuinely adversarial moves (the Rogers/Defender dispute, the "Europeans saved the blues" debunk, track C's refusal of house-music origin claims). All findings below were resolved at merge; the resolutions are logged in the Applied-changes section. The corpus's headline structural finding — that the evidence supports Chicago-centered transnational corridors, not a "world system" — survived the audit and is adopted in the research brief.

## Findings

### Challenged claims (10: 1 high, 8 medium, 1 low)

**HIGH**
1. **Garvey's first Chicago visit — direct cross-track contradiction.** Track F asserted "by 1917" (Verified, working paper); track A documented September 1919 (Verified, UIUC scholarship). Neither noted the conflict. → **Resolved:** single canonical Garvey entity; 1919 Black Star Line trip kept Verified with the 1917 assertion recorded as contradictory evidence; the "first by 1917" claim re-graded **Disputed**.

**MEDIUM** (all re-graded Verified → Provisional unless noted)
2. Elijah Muhammad's Nov 1959–Jan 1960 world tour — single secondary source. → Provisional.
3. Haile Selassie I's June 8, 1954 Chicago visit — sole source via uncertain-provenance copy. → Provisional. (A separate Rogers/Ethiopia 1935 claim was correctly left Verified — multi-sourced.)
4. Malcolm X founding *Muhammad Speaks* — contradicted by track F's own contested-founding note. → **Disputed**, contradictory evidence added.
5. Chuck Berry's May 1955 Chicago trip / Waters referral — single hobbyist source. → Provisional (applied to both the Berry and Chess Records instances).
6. Sun Ra's first concerts outside the U.S. (1970) — label liner notes. → Provisional.
7. Frankie Knuckles at Ministry of Sound (1992) — fan catalog. → Provisional.
8. Defender "Great Northern Drive" / 250,000-circulation claims — Congressional tribute sources (honorific genre). → Provisional.
9. Pilgrim Baptist as Smithsonian-certified "birthplace of gospel music" — competing Tindley historiography unnoted. → **Disputed** with contradictory evidence added; Dorsey's appointment and 1932 NCGCC founding kept Verified.

**LOW**
10. Hughes Defender column start: 1942 vs February 1943. → Reconciled to 1942 (historically standard) with the 1943 variant noted; cross-note added to the Defender entity's copy of the claim.

### Duplicate entities (23 groups merged)

All 23 cross-track duplicate groups were merged into canonical records (IDs GBL-001…GBL-213), including 4 triple-track entities (Elijah Muhammad, Marcus Garvey, Nation of Islam, Johnson Publishing Company, Associated Negro Press). Claim-level dedup applied conservative grading where tracks disagreed. Resolved alongside: Dorsey's Pilgrim appointment year (1931/1932 → single Verified claim with year variance noted).

### Relationship issues (10 flagged → resolved)

| Edge | Resolution |
|------|-----------|
| Ida B. Wells-Barnett → Chicago Defender ("press_succession_context") | **Dropped** — researcher's synthesis, not a documented link (Wells's 1892 flight predates the Defender's 1905 founding by 13 years) |
| Defender ↔ BSCP ("shared_labor_network") | Re-graded Verified → Provisional — no dated direct institutional link cited |
| John Lee Hooker → Vee-Jay ("cross_city_session") | **Dropped** — redundant/misassigned duplicate of "recorded_for" |
| Gaddafi → Nation of Islam ($5M loan) | **Dropped from graph** — no primary document; claim kept as Unresolved with source-quality warning |
| Operation PUSH → Mandela (photo-caption edge; track described it as Tambo — the track itself was unsure who the photo shows) | **Dropped from graph** — re-graded Unresolved |
| Rogers → ANC Midwest chapter ("at the ANC's request") | Softened to "established chapter per testimony"; Provisional |
| 11 track-C "located_in/organized_in/based_in → Chicago" edges | **Reclassified** as geographic anchors (presence ≠ exchange); moved to geographic-anchors.json |
| Bo Diddley "musical-influence" | Renamed to "hypothesized-rhythmic-parallel"; Provisional |
| Big Bill Broonzy "preceded" | Softened to "toured Europe 1951–57; later cited as precedent"; Provisional |

### Source issues

- Track C's 12 negative findings had incomplete search logs (dates only, no sources searched) → flagged `search_log_complete: false`; require backfill (gaps.md).
- Track F's several negative findings have empty search logs → same flag.
- Congressional Record tributes used for Verified scale claims → capped at Provisional.
- Scribd-provenance documents (Selassie, Gaddafi) → locate published originals or archival equivalents.
- Track E discographic aggregators (Discogs, MixesDB, MusicVF, setlist.fm) underpinning Verified claims → require corroboration (Official Charts, studio logs, venue listings).
- NBC 1915 split: Wikipedia "corroborated" by a mirror → corroboration claim overstated; held at Provisional.

### Structural gaps (carried into gaps.md)

LGBTQ+ contributors absent (most distorting in track E — house's queer origins unacknowledged); working-class/non-famous actors thin; women mainly as performers rather than institution-builders; Indigenous presence only via Du Sable framing; African immigrant community voices thin beyond one figure; Caribbean track documents presence more than exchange; zero cross-track relationships by construction (schema pre-judged the world-system question).

## Applied-changes log

Full machine-readable log: `_tracks/applied-changes.json` (64 entries: 23 merges, 12 re-grades, 4 drops, 11 anchor reclassifications, 5 contradiction resolutions, renames/softens, cosmetic cleanups). Merge script: `_tracks/merge.py` — re-runnable; all outputs re-validated with `json.tool` after every change.
