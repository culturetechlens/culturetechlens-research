# Red Team — CTL-RB-BIZ-000002: Black-Owned Banks in Chicago

*Adversarial review of the brief's evidence, conducted 2026-09-28 before publication. Each risk is named, tested, and given a disposition.*

## 1. Circular sourcing

**Risk:** The Kansas City Fed book, BlackPast, and popular accounts may all draw on the same underlying secondary literature, creating an illusion of corroboration.
**Test:** The brief's strongest quantitative claims (Binga's $200K/$1.3M deposits; Douglass charter no. 12227; ISF's $7,000 founding) each rest on one or two secondary sources with no primary record behind them.
**Disposition:** Accepted as a limitation. Claims are graded PROVISIONAL or SUPPORTED (never VERIFIED) where only secondary agreement exists, and §21 states plainly that no call reports, examiner files, or charter records were consulted. The grades are the anti-circularity mechanism — do not upgrade them without new primary evidence.

## 2. Myths and heroic narratives

**Risk:** "Binga refused to foreclose on Black churches, which killed the bank" and "regulators refused Binga a rescue" circulate online without evidence.
**Test:** Neither claim was found in any source consulted this session.
**Disposition:** Both are excluded from the brief. The red-team rule stands: a good story without a source is not a finding.

## 3. Date conflicts

- **Douglass founding (1922 vs. 1923):** flagged in the timeline (§10) and claim C008; do not silently pick one.
- **Binga's arrival in Chicago (1892 vs. 1893):** immaterial to bank claims; excluded.
- **ISF's 25-year mark vs. the 1961 Jet caption:** the arithmetic (1934 + 25 = 1959 ≠ 1961) suggests the "25-year" framing is approximate; the claim is graded PROVISIONAL and the figures are not treated as balance-sheet data.

## 4. Name/geography conflicts

- **NPS calls Douglass the "first" nationally chartered Black-owned bank; LoC/Weems and the KC Fed say "second."** Disposition: the brief uses "second" per the stronger sources and footnotes the NPS discrepancy (C009). Possible explanation: the NPS page frames it as a Chicago first. Do not "correct" the NPS page in CTL's voice — report the conflict.
- **Binga Bank addresses:** NPS verifies 3633 S. State St.; other State Street addresses are reported. Disposition: only the NPS address is VERIFIED; the map (V6) visually distinguishes verified from reported locations.

## 5. Anachronism

**Risk:** Projecting modern MDI/FDIC vocabulary onto 1908–1932 institutions.
**Test:** The brief uses "Black-owned/controlled/serving" as analytic categories, not period terms, and says so in §05. The FDIC MDI designation did not exist in Binga's era; no claim implies it did.
**Disposition:** Clean, provided §05's framing survives editing.

## 6. Unsupported causation

- The brief does **not** claim discrimination caused any specific failure. It documents discrimination as the founding context and multi-causal mechanisms (concentration, undercapitalization, interest-rate risk, real-estate losses, governance) for the endings.
- It does **not** claim the OCC consent-order termination means GN Bank is "safe and sound" — the procedural wording is quoted, not paraphrased upward (C015).
- It does **not** claim lending volumes it cannot measure — §16 states the gap explicitly.

## 7. Selection and survivorship bias

**Risk:** Six banks are not the whole story; failed banks are overrepresented because failures generate regulator paper.
**Test:** The brief acknowledges (§21) that no comprehensive census of Chicago Black-controlled financial institutions was attempted, and that credit unions and insurers appear only as bounded comparison. GN Bank — the survivor — is the least documented institution in the brief, which is itself a survivorship-data gap worth naming.
**Disposition:** The scope decision (§04) is explicit; do not let the six-episode frame harden into "these were the only ones."

## 8. Celebrity bias / missing ordinary people

**Risk:** The record names founders and chairmen; depositors, tellers, and borrowers are nearly invisible.
**Test:** The 3,000+ Covenant investors, the children with tin banks, and the 800 foreclosure preventions are the brief's only windows onto ordinary participants — all thinly sourced.
**Disposition:** §20 lists the gender composition of depositor/investor bases as unknown; §22 proposes oral histories as further research. Do not invent representative depositors.

## 9. Missing women

**Risk:** A bank history told entirely through men.
**Test:** Eudora Johnson Binga's capital, Veranda Dickens's chairmanship, and Maggie Lena Walker (national comparison) appear, but women's roles are under-documented in the sources, not just the brief.
**Disposition:** Named as a gap in §20 and a research direction in §22. The brief does not inflate the three mentions into a finding of gender equity.

## 10. Duplicate entities

**Risk:** Binga Bank vs. Binga State Bank; Community Bank of Lawndale vs. Covenant Bank; Illinois Service Federal vs. GN Bank; Independence Bank vs. Indecorp — the same institution under two names could double-count in the graph.
**Test:** All four pairs are intentionally merged into single entities in `entities.json` with continuity notes, and the merge is declared in the file's entity_note.
**Disposition:** Clean. Graph ingest must respect the merged IDs.

## 11. Weak visual rights

- V1 (Overton photo): license attributed by NPS but the Commons file page could not be opened (HTTP 403). **Publication blocker unless re-verified** — the fallback is documented in visuals.md.
- V2 (Broad Ax page) and V3 (NPS photos): identified but not yet captured; URLs and credits must be captured at publish.
- No image of Jesse Binga, Douglass Bank, or any bank interior is rights-cleared in this session. Do not substitute an AI-generated portrait — the directive forbids it and the red team concurs.
- VID-2's channel authority is unverified; default to link, not embed, if verification fails.

## 12. Claim-grade integrity

**Audit:** 31 claims — 7 VERIFIED, 17 SUPPORTED, 6 PROVISIONAL, 1 UNRESOLVED, 0 DISPUTED-as-standalone (the Douglass first/second conflict is documented inside C009).
**Test:** Are any PROVISIONAL claims load-bearing for a Key Finding? Finding 3 (employment) leans on C007 (PROVISIONAL) — the finding's wording ("the direction is documented; the scale is thin") matches the grade. Finding 1's Binga deposit figures are SUPPORTED, not VERIFIED — the finding labels them "reported." No finding outruns its claims.
**Disposition:** Clean at v0.1. Any future upgrade of a grade requires new evidence cited in the ledger.

## Final verdict

- **WHAT THE EVIDENCE ESTABLISHES:** Six Black-controlled Chicago banks operated between 1908 and 2017; their founding pattern (pooled excluded savings), their five documented roles, their varied multi-causal endings, and the deposit-continuity/ownership-loss pattern at resolution.
- **WHAT THE EVIDENCE SUGGESTS:** That community concentration was both mission and vulnerability; that ownership labels in popular accounts overstate survival; that the banks' scale was real but small relative to need.
- **WHAT REMAINS DISPUTED OR UNKNOWN:** Douglass's founding year and first/second status; Binga's address chronology and the 1933 conviction's full context; GN Bank's current ownership classification; institution-level lending volumes; causal weights behind closures.
- **WHAT CTL SHOULD RESEARCH NEXT:** OCC/FDIC primary records; Cook County court records on Binga; Chronicling America capture of the 1921 Broad Ax coverage; FDIC BankFind verification of GN Bank; oral histories with former employees and depositors; the women's-capital dimension; and the correspondent-banking/regulatory-treatment question with primary evidence.
