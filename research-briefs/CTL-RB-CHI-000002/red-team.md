# Red Team — CTL-RB-CHI-000002: The Rise of Bronzeville

**Date:** 2026-09-28
**Purpose:** Deliberately attack this brief's weaknesses before any CTL artifact is built from it. Inherited sibling risks are re-checked, not re-argued; new risks from this brief's causal framing get fresh scrutiny.

## 1. The central thesis as single-cause risk
**Attack:** The confinement→concentration thesis ("segregation manufactured the critical mass") is elegant — suspiciously elegant. It risks becoming the single-cause story the sibling's house position rejects.
**Defense:** The brief names seven forces and three feedback loops, not one cause; §09 states each force alone was insufficient. The thesis is labeled *interpretive* (SUPPORTED, not VERIFIED) and §20 admits it is not quantitatively testable from this package.
**Residual:** Medium. An artifact could easily headline "segregation built Bronzeville" and drop the qualifications. The artifact layer must keep the seven-force structure visible.

## 2. Constraint-as-hero: making segregation the protagonist
**Attack:** Framing confinement as the *productive* force centers white coercion as the engine of Black achievement and sidelines Black agency.
**Defense:** §19(2) records this competing interpretation explicitly; F1's agency note (migrants chose Chicago for wages) and F7 (self-naming as Black-authored force) counterweight it.
**Residual:** Low-medium. Watch the artifact's narrative voice.

## 3. New-research sourcing: secondhand tables and snippet captures
**Attack:** The migration series rests on an NPS *table* reproduced secondhand, not a direct census pull; the chicago.gov corridor description and EoC Demography share-arc come from search-result captures, not fetched pages; the 1919 riot figures are snippet-level.
**Defense:** The brief is honest about all of this: the NPS table is labeled "reproduced secondhand," NHGIS verification is listed as the P0 upgrade, the riot is graded Provisional with an explicit "do not cite figures" note, and the EoC Bronzeville page fetch failure is disclosed in sources.md.
**Residual:** Medium. The artifact must not present the population chart as NHGIS-grade. The build spec (V-DATA-1) footnotes the 1920 variant — good — but the whole series wants the NHGIS rebuild before flagship use.

## 4. Circular sourcing risk: NPS ↔ landmarks reports
**Attack:** The NPS nomination (1986), the Chicago landmarks reports, and the chicago.gov Black Renaissance report may share authorship lineages and source pools — citing them as independent corroboration could be circular.
**Defense:** The brief does not claim multi-source independence where it isn't established; the strongest corroboration pairs are genuinely independent (NPS table vs UIC report vs Yale lecture for numbers; EoC entry vs sibling for naming).
**Residual:** Low-medium. A provenance audit of the landmarks/NPS documents is a reasonable further-research add.

## 5. The 1920 figure variant (109,458 vs 109,894)
**Attack:** Publishing a population series with an unresolved 436-person discrepancy looks sloppy — or worse, suggests the compiler didn't notice.
**Defense:** Noticed, flagged in the data table, the claim ledger (CL-001), and the visual build spec. The discrepancy is immaterial to the argument (both show ~2.5× growth 1910–20).
**Residual:** Low. Keep the footnote in the artifact.

## 6. Defender circulation series dispute
**Attack:** Two different series (50K→125K vs 33K→130K) for the same years undermines the "Defender as infrastructure" force.
**Defense:** §19(5) and CL-005 preserve both; the force claim rests on the *direction* (explosive growth) and the *mechanism* (porter network, Great Northern Drive), not the exact numbers.
**Residual:** Low.

## 7. Video provenance and the "unwatched" rule
**Attack:** Neither video was fully watched; transcripts were not reviewed; upload dates are approximate. VID-1's description contains an inflated "twenty thousand arrived each day" claim.
**Defense:** visuals.md records all of this: assessment basis (title + full description + channel authority), the inflated claim flagged, embed status checked via oEmbed with a re-check-at-publication instruction, and full identity metadata for link-rot replacement. Video is illustrative-only by policy.
**Residual:** Low-medium. Someone should watch both end-to-end before publication and log timestamp ranges precisely.

## 8. Geographic discipline
**Attack:** The forces narrative could blur the corridor with Woodlawn/Washington Park (covenant case is Woodlawn; RTR is Grand Boulevard/Washington Park).
**Defense:** §05 definitions, §13, and CL-008 keep them distinct; the brief's claims attach to Douglas/northern Grand Boulevard unless marked.
**Residual:** Low — provided V-DATA-3's map keeps the distinction.

## 9. Missing women / missing ordinary people
**Attack:** A forces brief about "capital" and "institutions" defaults to great-men history (Abbott, Binga, Overton, Fuller).
**Defense:** CL-022 and §11/§12 name the women's institutional layer (Olive Leaf Club → Liberty Baptist; Harsh; Gaines; Davis; Joyner; Burroughs); §21 admits oral histories are unconsulted and the working-class layer is thin.
**Residual:** Medium. The forces model currently explains the rise through elites and institutions; the kitchenette/rent-party/porters/domestic-worker layer is acknowledged but underbuilt — same residual as the sibling.

## 10. Anachronism check
**Attack:** "Bronzeville" (1930/32) applied to 1910s events; "Great Migration" periodization imposed on actors who said "exodus" or "Northern drive."
**Defense:** §05 defines the naming date; the brief uses "Black Belt"/"Black Metropolis" for the pre-1930 corridor and reserves "Bronzeville" for the named identity — mostly. 
**Residual:** Low-medium. One audit pass over the artifact text for pre-1930 "Bronzeville" uses is warranted.

## 11. Duplicate-entity / namespace check
**Attack:** Forces-namespace entities could collide with sibling district entities in the knowledge graph.
**Defense:** entities.json uses the `-F` namespace and a note forbidding re-ingestion of district entities; relationships.json endpoints were machine-validated (18/18 resolve).
**Residual:** Low.

## 12. Copyright
**Attack:** Three images, all cleared — but the Commons 403 means license verification was indirect for the file pages.
**Defense:** Verified via Commons API extmetadata (authoritative) + NPS.gov corroboration for the two CC BY-SA images; PD status of the 1915 newspaper photo is sound. Attribution + share-alike terms recorded; re-verification at publication is instructed.
**Residual:** Low.

## 13. What this red team cannot check
- Whether the NHGIS rebuild will confirm or revise the NPS table (structural uncertainty, not a flaw).
- Whether the Defender archival run will support the "Great Northern Drive" mechanism at the claimed scale.
- Whether oral histories will revise the forces model toward everyday-life mechanisms.

**Net assessment:** The brief's causal thesis is its biggest strength and its biggest risk. The grading discipline holds — 21 VERIFIED / 10 SUPPORTED / 3 PROVISIONAL / 1 UNRESOLVED, with the interpretive core honestly labeled. Highest residual risks: (a) the artifact flattening seven forces into one slogan; (b) the population series shipping before NHGIS verification; (c) the thin working-class/oral-history layer. None is fatal to this brief as a research product.
