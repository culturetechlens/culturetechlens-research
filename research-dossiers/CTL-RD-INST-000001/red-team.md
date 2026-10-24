# CTL-RD-INST-000001 — Red-Team Review

**CULTURETECHLENS · Culture, Clearly Seen. · Black Cultural Intelligence**

Deliverable: red-team.md · Dossier: **CTL-RD-INST-000001** · Date: 2026-09-28
Method: adversarial pass against the Appendix C checklist, item by item. Findings recorded; fixes applied to the dossier where possible.

---

## C1. Claim reconciliation (42 = 42)

- [x] **Dossier §15 ledger:** 42 claims (CLM-001–CLM-042).
- [x] **Evidence file CTL-EF-INST-000001:** 42 records (CLM-001–CLM-042), ten-part architecture each.
- [x] **Mapping check:** 16 VERIFIED / 20 SUPPORTED / 1 PROVISIONAL (CLM-020) / 2 DISPUTED (CLM-001, CLM-004) / 1 REFUTED (CLM-011 → ledger DISPUTED) / 2 UNVERIFIABLE (CLM-039, CLM-040 → ledger UNRESOLVED) = 42. Ledger equivalents: 16/20/1/3/2 = 42. ✓
- [x] **Unique claim IDs:** CLM-001–CLM-042, no duplicates, no gaps.

## C2. Circular sourcing

- [x] **Checked:** MEDIA-001, BCI-001, BPM-003, and brief CTL-RB-MEDIA-000001 are cited in the dossier but flagged as sibling-CTL products, never as independent verification for a VERIFIED grade.
- [x] **Specific exposure:** CLM-035 (decline analysis) leans on MEDIA-001's synthesis. The claim is graded SUPPORTED and the dossier's §27 flags the circularity. Red-team verdict: acceptable at SUPPORTED with the flag, not promotable to VERIFIED without external industry sources.
- [x] **Defender self-history:** SRC-S-26 (the Defender's own centennial history) is treated as attributed; no contested VERIFIED claim rests on it alone.

## C3. Date harmonizations

- [x] **Founding date:** "May 5, 1905 (BlackPast gives May 6)" appears in dossier §§01, 03, 05, 12, 15 (CLM-001), 17, 26, and Appendix A. No bare "May 5, 1905" occurrence found in prose.
- [x] **3435 S. Indiana:** "1920–1956 (building retained to 1960)" appears in §§01, 06, 07, 15 (CLM-026), 23, and Appendix A. No bare "1920–1960" occurrence without the composite.
- [x] **Weekly reversion:** 2008 (E&P, ndinsider) used throughout; Wikipedia's 2003 rejected and the rejection recorded (CLM-023, §27).
- [x] **Abbott birth year:** Both variants shown everywhere the date appears (§§05, 12, 15/CLM-004, 26).

## C4. Entity duplication and building separation

- [x] **entities.json:** `canon-chicago-defender` (organization) ≠ `canon-chicago-defender-building` (3435 S. Indiana) ≠ `RD-INST-000001-2400-s-michigan` (2400/2410 S. Michigan). Linked by `headquartered-at` edges, not by identity merge.
- [x] **relationships.json:** 28 edges parsed successfully; every edge carries provenance and a grade; no edge conflates organization with building.
- [x] **JSON validity:** `entities.json` and `relationships.json` both parse under `python3 -m json.tool`.
- [x] **Known blemish:** Dossier §29 says "4 reuse audit IDs" but lists five IDs (canon-chicago-defender, canon-chicago-defender-building, canon-robert-sengstacke-abbott, canon-john-h-sengstacke, canon-great-migration). **Fix applied:** count corrected to five.

## C5. Causation wording

- [x] **Great Migration:** The dossier never says the Defender "caused" the migration except inside the refuted CLM-011 formulation. Corpus language is "documented catalyst." ✓
- [x] **FEPC:** The dossier never says Sengstacke caused EO 8802; CLM-039 is UNVERIFIABLE and the advocacy-only version is attributed. ✓
- [x] **Overclaims scanned:** The Chicago Literary Hall of Fame's "initiated the Great Migration" and journal-isms.com's "triggered the Great Migration" are quoted as *their* wording and flagged, not adopted.

## C6. Porter legend quarantine

- [x] **CLM-008 (core network):** VERIFIED, documented via Congressional Record + NMAAHC.
- [x] **CLM-040 (concealment/train-tossing):** UNVERIFIABLE → ledger UNRESOLVED; quarantined as legend.
- [x] **Visuals:** GFX-001 build spec explicitly forbids depicting concealment or train-tossing.
- [x] **Payment/routes/named carriers:** recorded as gaps (§28), not smuggled into the VERIFIED narrative.

## C7. Missing women and workers

- [x] **Women present:** Ethel L. Payne, Gwendolyn Brooks, Margaret Burroughs, Daisy Bates (NNPA), Vera Pigee, Charlotta Bass, Ida B. Wells (Defender-adjacent).
- [x] **Workers present:** Pullman porters (network, not names); Ben Burns (first white editor, Jewish); Lucius Harper (children's-page editor).
- [x] **Recorded gaps:** No named porter carriers; no women in the daily-conversion or sale narratives; the NNPA founding meeting is all-male in the record as cited. These are documented as gaps, not patched with speculation.

## C8. Rights and privacy

- [x] **Cleared:** IMG-001 (Wikimedia Commons, PD statement); IMG-002 (Internet Archive, federal PD).
- [x] **Not cleared, omitted:** commercial/Getty Abbott portraits; pre-1929 front-page scans; IMG-101 (Delano newsboy, LOC record pending); Defender-archive/CPL and Park District parade photos.
- [x] **Video:** WTTW documentary is illustration-only with timestamps to check; "One Tenth of a Nation" is link-only.
- [x] **No AI-generated historical people or imagery** anywhere in the package.

## C9. Adversarial spot-checks (claims chosen to stress the dossier)

| Target | Attack attempted | Result |
|---|---|---|
| CLM-012 (500,000) | "The dossier claims 500,000 circulation." | Rejected — dossier says ~250,000 copies, ~500,000 *readers*, with the conflation named and resolved. |
| CLM-023 (2008) | "Wikipedia says weekly since 2003." | Rejected — two contemporary sources (E&P, ndinsider) beat Wikipedia; rejection recorded. |
| CLM-011 | "The Defender caused the Great Migration." | Rejected — REFUTED as stated; "documented catalyst" is the corpus position. |
| CLM-039 | "The Defender's subscription-agent contracts, commission rates, and headcount are documented." | Rejected — UNVERIFIABLE → ledger UNRESOLVED; repeatedly asserted, never sourced. |
| CLM-040 | "Porter-network mechanics (payment, routes, quantities, named agents) are documented." | Rejected — UNVERIFIABLE → ledger UNRESOLVED; core network (CLM-008) documented, mechanics not; linen/tossed-from-trains details quarantined as legend in §27. |
| CLM-020 | "The paper never used 'Negro' or 'black.'" | Held at PROVISIONAL — single source, absolute negative; not promoted. |

## C10. Grade-tally verification

Programmatic recount of §15 ledger grades completed 2026-09-28: **42 rows, unique and sequential CLM-001–CLM-042**; tally **16 VERIFIED / 20 SUPPORTED / 1 PROVISIONAL / 3 DISPUTED / 2 UNRESOLVED** — matches the dossier §15 footer exactly. Evidence file: 42 records, tally 16/20/1/2 DISPUTED/1 REFUTED (CLM-011 → ledger DISPUTED)/2 UNVERIFIABLE (CLM-039, CLM-040 → ledger UNRESOLVED); cross-check of all 42 claim/classification pairs shows no mismatches. All 42 evidence records carry the ten-part architecture. relationships.json: 28 edges (19 VERIFIED / 9 SUPPORTED), unique edge IDs, all with provenance. entities.json: 27 entities, unique IDs. During this pass the red team caught a numbering mismatch in the first evidence-file draft (records CLM-031–CLM-042 described claims that did not match the dossier ledger — a phantom "FEPC direct-cause" claim and a "train-tossing" claim were among them); the records were rewritten to the ledger's actual claims and the mismatch is closed.

## Red-team verdict

The dossier's load-bearing positions (date harmonizations, causation language, porter legend quarantine, rights rules, entity separation) hold under adversarial pressure. The weakest points are single-chain SUPPORTED claims (CLM-032 CJR circulation-collapse figures, CLM-036 publisher-reported 2019 scale, CLM-042 Harsh Collection box counts via a CTL-internal chain) and the UNVERIFIABLE distribution-mechanics claims (CLM-039, CLM-040) — all graded honestly and none load-bearing for the dossier's three strongest findings.
