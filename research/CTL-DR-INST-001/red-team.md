# CTL-DR-INST-001 — Red Team Audit

Date: 2026-09-28 · Auditor: synthesis coordinator (post-merge pass over 5 tracks)

## Applied corrections (during merge)

1. **Merged duplicate pair:** "South Side Settlement House" (track-a) + "Ada S. McKinley Community Services" (track-d) → canonical INST-003. Same 1919 Ada S. McKinley founding; rename lineage. Survival corrected track-d's "unknown" → "operating" (track-a Verified: still operates).
2. **Merged duplicate pair:** "Chicago Metropolitan Assurance Company" (track-a) + "Chicago Metropolitan Mutual Assurance Company" (track-c) → canonical INST-024. Same 1925 Chicago Black burial-insurance origins, multi-state expansion, 1990 Atlanta Life acquisition. Naming variation flagged for archival confirmation (Illinois Dept. of Insurance) — recorded as Unresolved merge note, not silently elided.
3. **Type vocabulary normalized:** settlement_house→settlement house, professional_association→professional association, insurer→insurance company.
4. **Rejected false-positive merges:** Cook County Bar Association vs Cook County Physicians Association (distinct); Supreme Life vs Victory Life (distinct companies).
5. **Verification policy enforced:** relationships.json contains ONLY Verified edges (60). Track-c's Provisional CCBA→Douglass receivership link and track-a's single-source claims (Leak's MLK limousine, Rayner Jr. as Tuskegee Airman, Black Elks at The Forum) were kept out of relationships.json per worker grading.
6. **No numeric Survival Index scores assigned** — track-e correctly used descriptive indicators only; confirmed no scores in the dataset.

## Checklist

1. **Unsupported claims:** PASS with notes. 174/329 claims Verified; 115 Provisional clearly marked. No manufactured dates/founders found in sample review.
2. **Missing communities:** CONCERN. UNIA/Chicago Garvey movement entirely absent — the most obvious missing mass-membership institution. Black Catholic institutions thin (St. Elizabeth school only). Nation of Islam/Moorish Science covered only via SCI-004 cross-ref.
3. **Geographic bias:** CONCERN. South Side dominant; West Side institutions under-covered (track-d notes KOCO, WSO; track-a notes gaps). Suburbs absent.
4. **Famous-person/institution bias:** CONCERN (mild). Flagships (Provident, DuSable Museum, Pekin, Defender-adjacent) well covered; storefront/small institutions thin — though tracks A and D deliberately covered funeral homes, block clubs, and the Forum.
5. **Institutional bias:** CONCERN. Defunct institutions' records are thinner — 31/81 entities have "unknown" survival; disappearance is under-documented (survivorship bias in the archive itself). Stated in brief.
6. **Survivorship bias:** See #5. Also: the Survival Index's 50 Provisional rows must not be presented as settled.
7. **Missing women:** PARTIAL PASS. 15/81 entities women-associated (women's clubs, Wells, McKinley, Harsh, Links, St. Elizabeth). Better than sibling packages, but women-led banks, insurers, and publishers still thin.
8. **Missing working-class/everyday-life history:** PARTIAL PASS. Funeral homes, burial societies, block clubs, credit unions covered; beauty schools/barbershops deferred to CTL-DR-LIFE-001 (correct scoping).
9. **Weak sources:** CONCERN. Ethiopian Art Theatre is Wikipedia-level; Supreme Life's 1999 takeover rests on weak secondary; several newspaper citations are secondhand via tertiary sources. All graded accordingly — no laundering found in sample.
10. **Duplicate entities:** PASS (post-correction). Fuzzy scan found no remaining duplicates above 0.5 token overlap except known-distinct pairs.
11. **Disputed dates:** PASS. Preserved as given: St. Monica 1893/1894, Pekin 1904/1905, Ethiopian Art Theatre 1922/1923, Negro Chamber 1931/1933, American Giants end date (1952/1955-56/1958) — never single-year.
12. **Misleading causality:** CONCERN (watched). Track-e's "governance transition predicts survival" is a pattern finding across cases, presented as synthesis not causal law. The "no Black-owned bank HQ in Chicago" inference is flagged must-recheck before public use.
13. **Rights/copyright:** CONCERN. No rights review done; photographs/advertisements mentioned in dossiers are not cleared. Must gate page build.
14. **Directory-without-analysis drift:** PASS. The function-question template held across tracks; spot check confirms function/problem_solved populated for all 81 entities.

## Residual risks for the page-build stage

- Do not present Provisional survival-index rows or decade cells as settled fact; grades travel with the data.
- The social-club decade column is entirely "unknown" — show the gap, don't fill it.
- Recheck the bank-headquarters inference against the current FDIC MDI list.
- Rights clearance required before any photography/advertising use.
