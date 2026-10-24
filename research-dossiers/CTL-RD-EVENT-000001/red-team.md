# Red-Team Report — CTL-RD-EVENT-000001 (E2 Nightclub Tragedy)

**Date:** 2026-09-28 · **Version:** 1.0 · **Verdict key:** PASS / FLAG (with disposition) / FAIL

## Appendix C checklist

- [x] **Unsupported claims** — PASS. Every §15 claim (42) traces to a CTL-EF-EVENT-000001 record with Evidence For/Against. Ledger ↔ evidence file reconcile 1:1 (verified by claim-ID audit).
- [x] **Circular sourcing** — PASS with note. Wikipedia mirrors (Alchetron, Liquisearch) identified and excluded from corroboration counts. Wikipedia's E2 article used only as corroborating restatement, never sole support for a VERIFIED claim. The Samuel Bone identity (CLAIM-007) is single-threaded through Wikipedia's Tribune citation — graded SUPPORTED, not VERIFIED, with the chain disclosed.
- [x] **Myths repeated as facts** — PASS. §27 adjudicates five: the Feb-21 date (False), the 2009-manslaughter-acquittal conflation (False), the chained exit (Unverifiable), "code violations caused the deaths" (Exaggerated as legal claim), the promoter-ordinance-as-reform (False).
- [x] **Date conflicts** — PASS. Checked against contradictions.json: no E2-related harmonized positions exist; no conflict. The one internal date lead (Feb 21) was refuted by the full record (CLAIM-003).
- [x] **Name ambiguity** — PASS. §04 disambiguates E2/Epitome/Le Mirage(Hero's/the Clique; Calvin Hollins Jr. vs. III; Demetricta Carwell vs. "Cardwell" spelling discrepancy recorded, not adjudicated. No two entities share an ID; external stubs use RD-EVENT-000001-EXT-* (no invented canon-* IDs after red-team correction).
- [x] **Geographic errors** — PASS. 2347 S. Michigan = South Loop / Motor Row; not collapsed into Bronzeville. Community-area distinction stated in §06.
- [x] **Anachronisms** — PASS. Timeline built from contemporary reporting first (AP Feb 2003 → Time Out 2012 → retrospectives). No claim predates its evidence.
- [x] **Causation without evidence** — PASS. The dossier never says E2 "caused" the state law beyond AP's reported sequence; the promoter ordinance is explicitly marked never-adopted. CLAIM-024's "supervening act" is a quoted court finding, not CTL's causal claim. The legal-causation vs. moral-responsibility distinction is stated in §07 and §26.
- [x] **Selection bias** — FLAG (disclosed). The record is dominated by trial coverage and owner interviews (Time Out 2012); survivors' and families' voices appear mainly through anniversary journalism. Noted in §28 and here: a family-authorized oral-history layer is the top future enrichment.
- [x] **Celebrity bias** — PASS with note. Ordinary people included where documented: guards (Bone, Navarro), promoter, ten security staff, first responders, activists (Valenti), and the collective victims. Obama/R. Kelly/50 Cent appear only as documented venue history, not as the story's center.
- [x] **Survivorship bias** — PASS. The venue's closure and the building's demolition are documented; the thinness of the post-2003 business record is acknowledged (no E2 archive exists — §19).
- [x] **Missing women** — PASS. The 12-women/9-men split is recorded; no gendered erasure found in the legal record. Victim-centered reporting (Rainey, Carwell) is family-led.
- [x] **Missing institutions** — PASS. Institutional context mapped: city regulators, courts, CFD/CPD, state legislature, landmarks bodies, advocacy group, media.
- [x] **Duplicate entities** — PASS. duplicates.json checked: no E2-related canonical clusters; no contradictions with audit harmonized positions. Venue ≠ building separation observed (audit near-miss rule).
- [x] **Weak visual provenance** — PASS. Zero images cleared; none reproduced. Four candidate images listed with UNVERIFIED status and explicit do-not-publish flags. Data-driven graphics specified instead.
- [x] **Copyright/rights** — PASS. §33 log complete and empty; nothing reproduced without clearance; documents described not transcribed.
- [x] **Privacy** — PASS. No private residences published. Kyles's Hyde Park home mentioned only as "Hyde Park home" per the published interview — no address. Victim family members named only where they gave on-record interviews to reputable outlets.
- [x] **Sensitive subjects (MANDATORY)** — PASS. Dignity review: victims memorialized collectively; no graphic detail beyond the documented mechanism (inward-opening stairwell doors, compressional asphyxia — the minimum the record requires); no speculation about victims' actions; the terror-panic material is sourced to witness accounts, not embellished; the owners' racial-scapegoating allegation is recorded as allegation, not CTL adjudication; curiosity-serving details omitted (e.g., the owners' personal biographical color from Time Out is used only where it bears on ownership structure). A second reviewer should re-check tone before publication.

## Red-team findings (adversarial)

1. **Wikipedia date conflation caught and corrected** (CLAIM-037): the E2 article's "acquitted of involuntary manslaughter… November 25, 2009" is wrong — that was the contempt conviction. Any downstream CTL product must use CTL's timeline, not Wikipedia's.
2. **V103/iHeart is unreliable on details** ("124-year-old," "died… during a fire") — quarantined to venue-name history only.
3. **The AP 2024 retrospective is the sole source for the city ordinance** — VERIFIED on AP's strength, but a second source or the code citation is needed before the claim is load-bearing in a flagship product.
4. **The state-law claim (Obama-sponsored) is single-sourced** — graded SUPPORTED; the bill number is a gap. Do not cite the statute's contents beyond what AP states.
5. **Response-time dispute is genuinely unresolvable from press sources** — DISPUTED, both sides recorded; CTL must not let the city's specific timestamps (2:18/2:24/2:28) harden into "fact" in summaries without the dispute flag.
6. **ra.co's "40 minutes" appears to echo the owners' litigation claim**, not an independent finding — flagged in sources.md.

## Sign-off

Red-team complete 2026-09-28. No FAIL verdicts. Dossier remains at Research status pending: (a) primary-document verification of the ordinance and state law; (b) live-browser per-file image license checks; (c) a second dignity read.
