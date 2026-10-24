# Red-Team Audit — CTL-DR-PRESERVE-001 ("The Black Memory Emergency")

> **Auditor:** red-team worker · **Date:** 2026-09-28
> **Scope:** `research-brief.md`, `entities.json`, `timeline.json`, `relationships.json`, `sources.md`, `memory-map.json`, `priority-framework.md`, `gaps.md`, `SYNTHESIS-NOTES.md`, `_tracks/*`. Checked package honesty only; no research redone.

---

## Verdicts by checklist item

### 1. PRIVACY AUDIT — **PASS (0 violations), with one policy-consistency caveat**

- Scanned every record in `memory-map.json` (84), all claims in `entities.json` (142 claims across 119 entities), `timeline.json`, and `_tracks/*` for street-address patterns, phone/DOB/medical patterns, and named private individuals.
- **Zero private street addresses. Zero private home/storage locations. Zero phone numbers, dates of birth, medical data, or financial data.** Private collectors, WVON aircheck collectors, family collections, and funeral-home records are all described at aggregate level only.
- Named living individuals (Angela Ford, Julieanna L. Richardson, Theaster Gates, John Duke Kisch, Sherry Williams, Ovie Carter, Bob Black, John Simmons, archivist Megan McShea) are public figures or public-role professionals with non-sensitive, role-related claims only. Teenie Harris (d. 1998) death detail is historical.
- **Caveat (minor):** 7 `memory-map.json` records retain full street addresses in `location` (C-005 DuSable, C-007 Stony Island Arts Bank, C-012 CBMR, C-022 Schomburg, C-028 Amistad, C-030 AUC Woodruff, C-031 Wright Museum). All are **public museums/landmarks** — not violations — but they contradict the meta `privacy_statement` ("locations recorded at city/institution granularity only") and `SYNTHESIS-NOTES.md` §4's claim that the Moorland-Spingarn address was normalized to city level. The normalization rule was applied to one record and not to seven others. Sources-track files do document a "public-landmark addresses drawn from published sources" exception, but the canonical files don't state that exception.

### 2. Savior narratives — **FLAG (moderate)**

"Rescue" is mostly accurate event-description (JPC auction, Internet Archive capturing BET articles). Specific lines that position CTL/institutions as saviors of community-held material:

- `research-brief.md`: *"the private collector's mortality is the single most time-sensitive risk class: estates disperse, garages burn, and hard drives die **before any institution intervenes**."* — Frames institutions as the default interveners in private/family custody.
- `research-brief.md`: *"The rescues prove triage works."* + *"The priority framework exists to manufacture more decision points."* — implies the external triage lens is what made rescues work, despite the rescues (DJ Screw family donation, BHS burial records, Shorefront) being community-led.
- `priority-framework.md` (EX-06): *"The framework rewards rescue; it does not permanently rank."*
- Counterweight noted: `priority-framework.md` §7 has strong consent language ("not a license to extract… Preservation without consent is not preservation; it is acquisition"). The package is *not* consistently saviorist, but the brief's executive framing is.

### 3. Community-controlled archives coverage — **FLAG (mild imbalance)**

- Of 84 memory-map collections, ~52 (≈62%) are held by universities, major museums, public libraries, or federal institutions (my classifier counts Chicago Public Library, NYPL, NARA as institutional; community-based custody like Shorefront, Bronzeville Historical Society, Black Archives of Mid-America, Obsidian, South Side Community Art Center = ~12 clearly community-controlled; ~7 private/family).
- The community track exists and the gaps honestly state *"the most important collections are the ones no search can find"* and *"privacy wins"* — so the skew is **method-induced and disclosed**, not hidden. But a project about Black memory where >60% of mapped collections sit in white-majority universities and big-city museums should name the skew explicitly in the brief, not just in gaps.md.

### 4. Digital-decay optimism — **PASS**

- The package consistently separates digitization from preservation: framework EX-05 (*"digitization must not substitute for preservation of the physical archive"*), memory-map HistoryMakers (*"Rescued, not finished"*), JPC (*"Physical rescue does not equal digital access yet"*), BMRC portal (*"discovery layer… not a preservation layer"*), chain-stage DIGITIZED rated only "Patchy." No claim found implying a digitized collection is "safe."

### 5. Rights paralysis — **FLAG (high — hidden at synthesis level)**

- At record level, rights are documented: **33 of 84** memory-map records say `rights: "Not documented"` (plus 1 "Unclear"); EX-07 notes "murky rights." Honest.
- But the **research brief never uses the word "rights" once**, and `gaps.md` (15 gaps) never mentions rights uncertainty as a barrier. Eyes on the Prize — a pure rights-blackout loss case — is in the corpus (event entity) yet rights get no synthesis-level finding, no "we don't know" bullet, no "next investigation." Rights uncertainty — arguably the top blocker for digitization/reuse of Black collections — is minimized by omission. The package tells readers that the *known* risks (cataloging, ownership change) are the risks; the rights barrier is documented in rows but erased in the story.

### 6. Grade inflation — **FLAG (high — specific downgrades required)**

Internal standard (`sources.md` l.261–262): Verified = *"corroborated by ≥2 independent sources or rest on institutional/primary evidence"*; Provisional = *"single-source claims."* Sampled 18 of the 58 Verified claims with `primary: false`. Four fail the standard:

| Entity | Claim | Problem | Fix |
|---|---|---|---|
| CTL-PRESERVE-E-078 | "Fire destroyed sheet music…; $2.8M had been needed for repairs" | Single source (RNS 2006), evidence = citation only. | → Provisional |
| CTL-PRESERVE-E-067 | "LoC acquired The HistoryMakers in 2014" | Single source (JBHE), primary=false. | → Provisional |
| CTL-PRESERVE-E-097 | "LoC acquired the collection in 2014" (duplicate of E-067) | Same single source; also redundant with E-067. | → Provisional (or merge into E-067's claim) |
| CTL-PRESERVE-E-044 | BPP raid seizures via Ward Churchill | Single, admitted "non-ideal" hosting source; contentious author. | → Provisional at best (consider Disputed) |

- Also: CTL-PRESERVE-E-018 (Harsh claim) cites *"Risks track, CTL-DR-PRESERVE-001"* — the project's own track file — as the sole evidence for a **Verified** grade. Self-citation cannot meet "primary or corroborated reporting"; cite the Mellon grant announcement directly or downgrade to Provisional.
- 58 of 123 Verified claims rest on `primary: false`; the sample hit rate (~22%) suggests **~10–15 more grade-inflated claims** in the full set. The 58 need a re-audit against the ≥2-sources-or-primary rule.

### 7. Manufactured relationships — **PASS (one weak edge)**

- 78/78 edges Verified; all subject/object IDs resolve to the entity registry; zero duplicate edges; zero dangling references; predicates match the brief's counts (14 held_by, 26 threatens, 28 related, 10 affected).
- Weak edge: **CTL-PRESERVE-R-006** (`held_by`, evidence: `"JBHE, 2014"`) — a citation stub with no corroboration; inherits the E-067 grade-inflation problem. Downgrade to Provisional or expand evidence.

### 8. Internal contradictions — **FLAG (medium — arithmetic/docs)**

1. **Track-count arithmetic.** Brief: *"deduplicated from 91 track-level records."* But origin counts sum to **89** in `memory-map.json` meta (32+29+19+5+4) and **87** in `SYNTHESIS-NOTES.md` §3 (32+29+17+5+4). None equals 91. (Note: 91→84 via 6 merges *is* arithmetically consistent — JPC absorbed 3 records, five others 2 each — but the two origin-count tables contradict both the brief and each other.)
2. **Digital record count:** meta says 19 `digital_collection_like_records`; notes say 17 digital-only.
3. **Address normalization:** notes claim Moorland-Spingarn was normalized to city level, while 7 other institutional addresses keep street detail (see §1 caveat).

### 9. The "Not graded" collections — **PASS (disclosed honestly)**

- Brief: *"54 Not graded at record level (the institutional and community track files grade substantive claims, not collection records; this is recorded honestly rather than backfilled)"*. Every such record carries that note in `memory-map.json`. No backfilling, no implication of stronger verification. Model behavior.

### 10. Standard red-team items — **mixed**

- **Missing women — FLAG:** only **2 of 84** memory-map collections explicitly center women's history (C-024 Terrell/Parks holdings; C-030 AUC). No collection centered on Black women's organizations (sororities, women's clubs, NCNW), church mothers, or women-led press. `gaps.md` never names the gender gap.
- **Working-class history — mild FLAG:** 4 labor mentions (mostly as subsidiary subjects); Black business records documented mainly through their *absence* (Vee-Jay, Binga/Supreme Life — which is itself a valid finding).
- **Geographic bias — PASS (disclosed):** 33/84 Chicago; corpus is Chicago-anchored *by design* and says so repeatedly.
- **Survivorship/selection bias — FLAG:** framework claims *"The framework's tiers are validated by the cases that moved"* — 8 hand-picked worked examples, two retrospective successes (DJ Screw, Mother Bethel). These rescues **predated the framework by 13–15 years**; they cannot validate a 2026 tool. The validation claim is a causal overreach. (Corpus losses are underdocumented — acknowledged via negative findings.)
- **Weak sources — mild:** sources.md is unusually honest (tertiary sources labeled, self-reported figures flagged Provisional, Wikipedia use bounded). Exceptions are the E-044 Churchill claim and the E-018 self-citation (see §6).
- **Disputed dates — PASS:** point-value conflicts preserved as ranges, MySpace causation flagged as disputed, timeline eras used where dates are approximate. (One date-sensitivity note at sources.md l.325 is explicit and sound.)
- **Misleading causality — FLAG:** *"Every rescue in this corpus happened because someone acted at the decision point, not after the loss"* is near-tautological; *"The framework's tiers are validated by the cases that moved"* implies the framework caused rescues. See selection-bias note.

---

## Prioritized fix list

| # | File | Location | What to change | Why |
|---|---|---|---|---|
| 1 | `entities.json` | E-078, E-067, E-097, E-044 claims | Downgrade `verification_status` Verified → Provisional (E-044: consider Disputed) | Single-source / weak-source claims fail the package's own Verified standard (§6) |
| 2 | `entities.json` | E-018 Harsh claim | Replace `"source": "Risks track, CTL-DR-PRESERVE-001"` with the Mellon grant announcement citation, or downgrade to Provisional | Self-citation cannot support Verified (§6) |
| 3 | `entities.json` + `relationships.json` | all 58 Verified-but-`primary:false` claims; R-006 | Re-audit each against "≥2 independent sources or primary evidence"; fix R-006 evidence or downgrade | Sample hit rate ~22% suggests 10–15 more inflated grades (§6); R-006 inherits E-067's problem |
| 4 | `research-brief.md` | Key findings / "We don't know" | Add a finding on rights uncertainty as a synthesis-level barrier (33/84 records undocumented; Eyes on the Prize) | Rights paralysis is documented at record level but erased from the brief's story (§5) |
| 5 | `research-brief.md` | Executive summary §5; "Central question" | Soften: "the rescues prove triage works" → note the rescues were community/institutional action, not framework output; remove framework-as-cause implication | Anti-savior/causal honesty (§2, §10) |
| 6 | `research-brief.md` | "before any institution intervenes" line | Reword to acknowledge family/community succession as the norm and external custody as one option | Institution-as-default-savior framing (§2) |
| 7 | `memory-map.json` meta + `SYNTHESIS-NOTES.md` §4 | `privacy_statement`; address note | Either apply city/institution normalization to all 7 records or state the public-landmark exception explicitly in the canonical files | Policy inconsistency (§1) |
| 8 | `research-brief.md` + meta + notes | "91 track-level records" / origin counts | Reconcile: make meta components (19 vs 17 digital) and notes match the brief's 91, or correct 91 | Arithmetic contradiction (§8) |
| 9 | `priority-framework.md` | "The framework's tiers are validated by the cases that moved" (brief §5 too) | Reword: the retrospective examples *illustrate* tier movement; they cannot validate the framework (predate it by 13–15 years) | Selection bias / causal overreach (§10) |
| 10 | `gaps.md` | Tier C or new Tier D item | Add acknowledged gap: Black women's organizational/community history absent from corpus | Gender gap unacknowledged (§10) |
| 11 | `research-brief.md` | Key findings | Add one-line disclosure: ~62% of mapped collections are university/major-institution held; community-controlled coverage is the known thin edge | Coverage skew disclosed only in gaps.md (§3) |
| 12 | `relationships.json` | CTL-PRESERVE-R-006 | Expand evidence (add Getty/NMAAHC corroboration) or downgrade to Provisional | Weakest edge in the graph (§7) |

---

## Overall publication-readiness verdict

**Not ready as-is — publishable after the fix list.** The package's structural integrity is good: 84/84 memory-map records, 119/119 entities, 70/70 timeline events, and 78/78 relationships check out mechanically; privacy is genuinely clean; negative findings, "Not graded" records, and contradictory evidence are handled with rare honesty. The blocking problems are (a) grade inflation in ~4 confirmed + likely ~10 more claims that violate the package's own evidence standard, (b) rights uncertainty — the single biggest practical barrier in this domain — being documented in rows but omitted from the brief's findings, and (c) a handful of arithmetic/policy contradictions that undermine the "auditable" claim. The savior-narrative and validation-overclaim issues are fixable with rewording. Fix items 1–9 and this clears to publish; items 10–12 are lower-risk improvements.

---

## Remediation log — 2026-09-28 (all 12 items addressed)

| # | Fix | Status | Detail |
|---|---|---|---|
| 1 | E-078, E-067, E-097, E-044 downgrades | ✅ Applied | All four claims Verified → Provisional in `entities.json`, each with a red-team audit note in the uncertainty field. E-044 kept at Provisional (not Disputed): no conflicting source is documented in the corpus, so Provisional + explicit source caveat is the honest grade. |
| 2 | E-018 self-citation | ✅ Applied | Replaced "Risks track" citation with the primary CPL Mellon-grant announcement (chipublib.org) + corroborating JBHE reporting, both verified via fresh web search 2026-09-28. Claim stays Verified, now `primary: true`. |
| 3 | Full re-audit of Verified-but-`primary:false` claims | ✅ Applied | 53 claims examined (worker audit, `_tracks/grade-reaudit.json`); **19 downgrades applied**: 17 → Provisional, 2 → Disputed (E-027, E-079 — UMG vault-fire claims, where UMG's public statements contradict the internal loss memo). Dominant failure mode was single-sourcing (15/19). Borderline keeps documented in the audit file (E-001, E-020, E-091, E-004/E-006). Total grade corrections across the package: 23 claims + 1 relationship. Follow-up (not done): merge candidates E-051/E-087 → E-001 and E-031/E-088 noted in the audit file. |
| 4 | Rights uncertainty in brief | ✅ Applied | New finding 7 in `research-brief.md`: 33/84 records undocumented rights; Eyes on the Prize license blackout; Duke 2013 orphan-works filing. Dedicated investigation queued in `gaps.md` (item 18). |
| 5 | Savior-leaning phrasing | ✅ Applied | Brief §5 reworded: rescues credited to communities/families/coalitions; framework "manufactures decision points" but "cannot claim credit for rescues that predate it." |
| 6 | "Before any institution intervenes" | ✅ Applied | Reworded: family/community succession is the norm; external custody is one option, never the default. |
| 7 | Seven public-institution addresses | ✅ Applied | Public-landmark exception documented in `memory-map.json` meta `privacy_statement` and `SYNTHESIS-NOTES.md` §4. Verified: exactly 7 records (C-005 DuSable, C-007 Stony Island Arts Bank, C-012 CBMR, C-022 Schomburg, C-028 Amistad, C-030 AUC Woodruff, C-031 Wright Museum) — all published public addresses, zero privacy risk. |
| 8 | Count reconciliation | ✅ Applied | 91 track-level inputs = 32 institutional + 29 community + 21 digital-origin (17 pure + 4 in merges) + 5 framework + 4 risk; 6 merges absorbed 13 records → 84 canonical. Meta counts corrected (digital 19 → 21), `SYNTHESIS-NOTES.md` §3 rewritten, brief headline numbers made explicit. |
| 9 | Validation overclaim | ✅ Applied | Brief and `priority-framework.md` reworded: retrospective examples *illustrate* tier movement; they predate the framework by 13–15 years and cannot validate it. |
| 10 | Women's-history gap | ✅ Applied | `gaps.md` item 16: ~2/84 records center Black women's organizational history; item 17 adds working-class history thinness; item 18 queues rights as a dedicated investigation. |
| 11 | Institutional-skew disclosure | ✅ Applied | Brief methodology now discloses ~62% university/major-museum/public-library/federal holdings as a method-induced skew; community-controlled holdings are the known thin edge of the corpus. |
| 12 | R-006 | ✅ Applied | Downgraded to Provisional with grade note (evidence was a citation stub; inherits E-067's single-source limitation). Brief's relationship statistics updated: 78 relationships = 77 Verified · 1 Provisional. |

**Post-remediation grade-marker adjustments in the brief** (re-audit ripple): findings 1, 3, 4 now hedge the AFRO current-state portion, the Simmons-fire claim, and the Black Archives Co follower figure as Provisional.

**Publication readiness after remediation:** all 12 red-team items addressed; all JSON files revalidated with `python3 -m json.tool`; privacy re-scan clean. Remaining known follow-ups (non-blocking): entity merge candidates from the re-audit, Obsidian current-status verification, A.A. Rayner inquiry — all recorded in `gaps.md`.
