# Red-Team Audit — CTL-DR-LIFE-001 ("How We Lived: An Encyclopedia of Black Everyday Life")

**Auditor:** red-team subagent (parent orchestrator, session 067a026c-53d2-44bb-9919-a8d8ca8cc9a7)
**Date:** 2026-09-28
**Package reviewed:** `~/workspace/culturetechlens/research/CTL-DR-LIFE-001/`
- `entities.json` — 84 entities, 293 claims (154 Verified / 115 Provisional / 22 Unresolved / 2 Disputed) — counts verified by script
- `timeline.json` — 92 events (indices 0–91)
- `relationships.json` — 58 relationships, rule declared as "verified-only"
- `object-biographies.json` — 10 biographies × 11 links = 110 links
- `sources.md`, `gaps.md`, `rights-log.md`, `object-biography-methodology.md`
- Raw worker outputs in `working/` consulted for provenance on contested items

## Method

1. Read all 84 entities end-to-end (every claim, evidence, uncertainty field) — not just a sample. All 154 Verified claims were individually assessed against their cited evidence (full listing in §8).
2. Read all 58 relationships and checked each against the "verified-only" rule and against the grades of the entity claims they cite.
3. Read all 92 timeline events; validated every date programmatically (no impossible dates, no future dates, era ranges sane); checked each event's grade against its source entity claim and against methodology §6 ("Verified dated events only").
4. Read all 10 object biographies link-by-link, with hard scrutiny on the two Disputed links (ob-01/ob-02 `related_people`) and the weakest biography (ob-07, 0 Verified links).
5. Checked duplicates/contradictions across workstreams (entity↔entity, entity↔timeline, entity↔relationships).
6. Reviewed `rights-log.md` for any clearance-implying language; reviewed `sources.md`/`gaps.md` for honesty of negative findings.
7. Applied the project's own rules back to itself (methodology §§4–4.3 symbolism rule; slang rule; verified-only relationship rule).

**Overall posture:** The workers were strikingly honest — uncertainties are specific, gaps.md is a genuine negative-findings register, weak sources are labeled, and the two Disputed links are correctly handled. The failures found are sins of *over-grading at the margin* and *rule drift between files* (timeline/relationships not held to their declared standards), not fabrication. No invented manufacturers, dates, museum holdings, or relationships were found.

## Verdict: NOT YET PUBLICATION-READY — should-fix items required, no blocking issues

- **Blocking (must fix before any public use): 0**
- **Should-fix: 44** (in `changes.json`)
- **Notes: 9** (report only)

Nothing in the package is fabricated. But `relationships.json` and `timeline.json` both violate their own declared standards, two entity duplicates survive, and 7 claims plus 2 biography links are over-graded. After the 44 should-fix changes are applied mechanically, the package is publication-ready **as a research-grade deliverable** — the remaining Provisional/Unresolved items are honestly marked and must stay marked in any public rendering.

---

## 1. GRADE INFLATION (7 claim downgrades + 2 biography-link downgrades)

Every Verified claim was checked. Nine over-grades found:

**E-033 Johnson Products Company**
- **[0] → Provisional.** Founding details ($250 loan, barber co-founder, Joan's 1957 Ultra Sheen repositioning) rest on Wikipedia alone; "consistent with AP/Ebony obituaries" is asserted in uncertainty, not cited. (should-fix)
- **[1] → Provisional.** 80% market-share estimate, $12.6M sales, 1971 AMEX "first" — Wikipedia alone. (should-fix)

**E-034 Hair-care routines at home**
- **[1] → Provisional.** Afro Sheen slogans ("Natural Hair hangs out. Beautiful!", "soul food for the natural") quoted via Wikipedia only. (should-fix)

**E-008 DuSable High School**
- **[0] → Provisional.** Day-precision dates (opened Feb 4, 1935; renamed Apr 25, 1936) rest on Wikipedia; the AbeBooks yearbook listing corroborates years only. (should-fix)

**E-006 Bud Billiken Parade and Picnic**
- **[2] → Provisional.** The celebrity-guest list (Truman → Harold Washington → Oprah → Obama) rests on encyclopedia2.thefreedictionary.com, a Wikipedia mirror. The Defender Charities/theme portions are better sourced, but the claim stands or falls as written. (should-fix)

**E-017 A.A. Rayner & Sons Funeral Home**
- **[0] → Provisional.** "Serving since 1947" rests on business listings + a company press release — company-supplied history, single-origin. (should-fix)

**E-049 DuSable "Wonder Five"**
- **[0] → Provisional.** "First all-Black team, led by a Black coach, to reach the highest levels of an organized, integrated traditional sports program in America" — the superlative is Ira Berkow's book-description framing via IMDb, not a verified historical first. The state-final/Public League facts are fine; the "first in America" is not. (should-fix)

**Object-biography symbolism links**
- **ob-01 `symbolism` → Provisional.** "The fist comb was a symbol of the 1970s Black Civil Rights/Power movement" rests on the Fitzwilliam Museum's 2013 exhibition and NMAAHC topic cataloging — modern framing, not a contemporary (1970s) source. The link's own uncertainty admits it is "strong but second-order." Per the audit brief (symbolism must be documented in a contemporary source), this fails. The NMAAHC cataloging keeps it credible — hence Provisional, not Unresolved. (should-fix)
- **ob-04 `symbolism` → Provisional.** "Ordering by mail was a documented political act" rests on modern historian Einav Rabinovitch-Fox's framing (Finance & Commerce interview). Methodology §4.2 is explicit: "Where a modern scholar's framing is the only source, the link is Provisional at best." (should-fix)

**Kept as Verified (fairness notes):** ob-02 `symbolism` (NMAAHC 'Sizzle' essay documents meanings from historical sources it cites — keep, but the evidence field should name the specific period sources; noted in §7); ob-08 `symbolism` (Ebony's 1949 "Why Negroes Buy Cadillacs" is contemporary Black press, quoted via CJR — a methodology-approved source; keep, recommend consulting the original issue per the rights note); E-001[0] (Black Metropolis kitchenette passage quoted secondhand from a dissertation — the wording matches the widely cited passage and uncertainty is recorded; keep); E-023[0]/[1] (Poe 1999 via summary — peer-reviewed source, claim matches; keep, "Pig Ankle Joints" headline still needs Defender-archive confirmation as the uncertainty states).

---

## 2. NOSTALGIA BIAS

The workers policed this well — E-003's uncertainty explicitly says "High risk of nostalgia bias," and gaps.md logs cautions for Timuel Black's 47th Street memories, Idlewild's "Black Eden" framing, and the Wonder Five heroics. Findings:

- **E-003 (Saturday morning cleaning ritual):** already Provisional with explicit nostalgia-bias flag. No change; commend the handling. The entity exists only because of nostalgia-genre content and is correctly quarantined at Provisional.
- **Timeline [2] (Idlewild, 1912):** event text adds the gloss "an era of upward mobility" — not in the entity evidence. Mild romanticization; reword to neutral. (note)
- **E-041 (Idlewild) description:** "vacation free from humiliation" + "Black Eden" framing is balanced by claim [3] (decline after segregation) and the gaps.md caution that Idlewild's necessity was a product of exclusion. No change.
- **E-058 (porch-sitting):** the Andscape source is framed by 2016 gun-violence reporting; the worker notes "extract practice documentation with care." Fine.
- **No passages found** that romanticize without acknowledging hardship — the hardship acknowledgments (kitchenette exploitation, grocery price-gouging, segregation's role in Idlewild's existence, DuSable's later crises noted in gaps.md) are present where the material is celebratory.

---

## 3. PRESENTISM

- **E-038 [1]:** "House music is 'Black queer trans from root to tip'" — a 2021 DJ's retrospective characterization of the 1970s–80s scene, honestly attributed ("in the words of Chicago DJ Rae Chardonnay") with uncertainty noting it is a contemporary characterization. Keep Verified as reported speech, but any public rendering must keep the attribution and date; do not present "trans" as period terminology. (note)
- No other presentism found. Analytic frames ("respectability performance," "double-duty dollar") are period or scholarly terms, correctly used. The hot comb's `related_movements` was correctly left Unresolved rather than back-projecting "respectability politics."

---

## 4. MIDDLE-CLASS BIAS

The package is unusually self-aware here (dedicated bias notes in sources.md W1/W2/W3 and gaps.md). Specific assessment:

- **Well-flagged by workers:** E-036[2] (Black press ads skew bourgeois, citing Frazier); E-013 description (Defender wedding pages "encoding class standards"); gaps.md W2 ("Green Book documents the Black MIDDLE class"; "Johnson Products' story is entrepreneurial-elite history"); W1 source-bias note (kitchenette poor "rarely left first-person records").
- **Single-informant generalization risk (no grade change, note):** E-010[1], E-011[0], E-029[0][1], E-030[0] all rest on Timuel Black — an upwardly-mobile Bronzevillean recalling decades later. The claims accurately report his testimony (Verified = the testimony is documented), and uncertainties flag his perspective, but four entities' shopping/leisure picture leans on one man's memory. Recommend a scope sentence in E-029's description noting the perspective. (note)
- **E-019[2] (Black Santa, Hyde Park Holly-Days):** specific to Hyde Park; no false generalization. Fine.
- **Counterweights present:** barbershop/beauty-shop scholarship (Mills, Gill) centering workers; Cohen on working-class mass consumption (E-046[4]); Jiffy Cab crowd-memory (E-044). The bias is acknowledged, not laundered.

---

## 5. CELEBRITY CREEP

- **E-006[2]** downgraded (see §1) — the Truman/Oprah/Obama name-drop list is the clearest drift, and its evidence is weakest.
- **ob-08 Cadillac:** the museum exemplar is Chuck Berry's Eldorado — but the biography carries the caveat explicitly ("documents the museum holding, not the ordinary consumer's car"), and the symbolism/consumer-use links use ordinary-consumer sources (Ebony 1949, scholarship). Keep; gaps.md already lists finding a non-celebrity exemplar as follow-up. (note)
- **E-041[2]** (Du Bois/Walker/Daniel Hale Williams at Idlewild), **E-018** (Sam Cooke/MLK at Leak & Sons): already Provisional with contradictions/weak sources flagged. Acceptable as institution histories, not biography drift.
- **E-049, E-067, E-074, E-033, E-035:** community-institution and audience-practice framing; no drift into celebrity biography. No removals.

---

## 6. MANUFACTURED CLAIMS

No invented manufacturers, dates, museum holdings, or relationships found — the W4 worker checked holdings against live collection databases and said so. Two substance issues:

- **ob-07 / E-081 (console stereo): 0 Verified links.** All 11 links are Provisional (Wikipedia + stereoconsole.com, a hobbyist site) or Unresolved. The Provisional claims (e.g., "Zenith Radio Corporation, Chicago (exemplar Chicago maker)") are plausible-sounding filler without real evidence — honestly graded, but the biography contributes no verified knowledge. **Recommend removal** of ob-07 and E-081 until a verified museum holding and Black-household use evidence exist (gaps.md already lists exactly this as follow-up). (should-fix)
- **E-008[0] day-precision dates** (downgraded §1) — likely true, but day-level precision from Wikipedia alone is how manufactured precision enters the record.

---

## 7. SLANG

- **E-064/E-065:** clean — explicitly no folk etymology; Smitherman scholarship only. W3 gaps.md documents the exclusion policy. Commend.
- **E-047[0] → edit (should-fix):** "the porters originated bid whist terms like 'Boston,' 'uptown,' 'downtown'" is a term-origin claim sourced to a book review ("Rise and Fly" review, 2005), graded Provisional with "Oral-tradition origin story" uncertainty. Per the brief ("any folk etymology or unsourced slang origin must be flagged for removal; only scholarly-sourced linguistic claims survive"), the term-origin clause must be removed. The rest of the claim (porters popularized spades/bid whist on layovers) is fine and stays.
- **E-037[0] ("steppin'" naming):** origin story attributed to Chatman himself, Provisional, dates vary (1973 vs 1974) — kept as Provisional with a note; it is a sourced attribution, not an unsourced etymology.

---

## 8. SPECULATIVE SYMBOLISM

Covered in §1 (ob-01 → Provisional, ob-04 → Provisional). Remaining links:

- **ob-02 `symbolism` (hot comb): keep Verified**, with a should-fix documentation note: the evidence field should name the specific period sources the NMAAHC 'Sizzle' essay draws on for "respectability, beauty, identity, economic necessity," so a future reader isn't taking the essay's synthesis on faith. (note)
- **ob-03 `symbolism`: Provisional** (MTSU scholar's framing, honestly labeled). Correct.
- **ob-08 `symbolism`: Verified** (contemporary 1949 Black press). Correct.
- **ob-10 `symbolism`: Provisional** ("museum-framed, not contemporary-sourced" — honest). Correct.
- **ob-05/ob-06/ob-07/ob-09 `symbolism`: Unresolved** — correctly refused to invent. Commend; this is the methodology working as designed.
- **The two Disputed links (ob-01/ob-02 `related_people`): sound.** Both record materially conflicting accounts without choosing sides; gaps.md records the contradictions; relationships.json [39] captures the Walker refutation as an intentional verified negative. No changes.

---

## 9. DUPLICATES & CONTRADICTIONS

**Entity duplicates (rent-party precedent not applied consistently):**
- **E-048 → merge into E-006 (should-fix).** "Bud Billiken Parade — back-to-school Black family ritual" (w2) duplicates "Bud Billiken Parade and Picnic" (w1): same founding date, same "largest parade" claim, same back-to-school function. Merge and reconcile the initiator accounts — E-006[0] says "initiated by David Kellum (a Chicago Defender staffer)" while E-048[0] says "created by Robert Sengstacke Abbott." Both can be partially true (Abbott created, Kellum organized), but as written they are competing single-initiator claims.
- **E-070 → merge into E-027 (should-fix).** Two "Studs Terkel Radio Archive" source-collection entities (w1's E-027, w3's E-070). E-070 is more detailed; merge E-070's claims into E-027 and keep one.
- **E-001 vs E-057** (kitchenette practice vs kitchenette object) and **E-004 vs E-005** (Cooper vs Search for Missing Persons): legitimate practice/object and institution/program splits. Keep. (note)

**Timeline duplicates:**
- **[13]/[14] → merge (should-fix).** Same event (first Bud Billiken Parade, 1929-08-11) entered twice from w1 and w2, with contradictory initiators (Kellum vs Abbott). Fold into one event naming both accounts.
- **[26]/[28] → merge (should-fix).** Both: "Drake & Cayton publish Black Metropolis (1945), WPA-based." Fold [28] into [26]; keep [27] (grocery-pricing finding) as the distinct event but see below.

**Contradictions already handled well:** E-041[2] (Walker/Du Bois land — contradictory_evidence recorded), E-035[0] (187 vs 190 venues — recorded), E-033[1] (hour-count variance — recorded). No action.

---

## 10. RELATIONSHIPS (12 flags — the worst rule drift in the package)

`relationships.json` declares `"rule": "verified-only"`. Twelve of 58 relationships violate it:

**Rest on Provisional/interpretive evidence (remove from the verified-only set or re-grade):**
- **[21]** Jubilee Showcase → Sunday church attendance. Evidence is the "church before church" collector description that E-052[1] grades Provisional with explicit warning ("characterizes reception, not production... Provisional until viewer oral histories confirm"). (should-fix)
- **[26]** Sunday church attendance → Pullman porter work (job networks). Evidence: FreeLibrary summary citing Grossman 1989; E-060[2] is Provisional ("not directly consulted"). (should-fix)
- **[27]** Porch-sitting → Signifying. The evidence field itself says "the relationship is interpretive, not etymological." Interpretive links do not belong in a verified-only file. (should-fix)
- **[16]** Dance lineage → Steppin'. Evidence is Mary Harris, a single informant; E-050 claims are Provisional. (should-fix)
- **[24]** Photo studios → Family album. Evidence mixes Newberry exhibition claims E-062[0][1] (Provisional) with the Willis thesis. (should-fix)
- **[6]** Defender wedding announcements → Chicago Defender. Evidence cites E-013 claims, all Provisional (thesis-level, "not directly examined"). (should-fix)
- **[7]** Repast → Homegoing service. E-016[0] is Provisional (magazine article, Florida informant, national framing). (should-fix)
- **[8]** Easter best → Sunday dinner. Evidence is blackwallstreet-pa.com — a first-person non-Chicago source; E-021 claims are Provisional. (should-fix)

**Structural defects:**
- **[22]** from-node "Johnson Publishing Company (Chicago)" **is not an entity** in entities.json. Phantom node. (should-fix)
- **[25]** from-node "Chicago Urban League" **is not an entity** in entities.json. Phantom node. (should-fix)
- **[19]** wrong target: "Bud Billiken Parade → Chicago Defender / Ebony / Jet advertisements as evidence" — the evidence is about Abbott creating the parade for Defender newsboys; the relationship should target the Chicago Defender institution (E-025), not the ads source-collection. Type label also malformed ("institution — institution (origin)"). (should-fix)
- **[12]** malformed type ("practice — object") and wrong target: evidence is about barbershops circulating the Defender newspaper; target should be the Chicago Defender (E-025), not the ads source-collection. (should-fix)

**Notes:** [2] "sponsored_by" is loose for "initiated/organized by" (note); [9] mixes Verified and Provisional evidence (note); [30] should verify Robinson's Working tape is in the digitized set (note); type labels are inconsistent across the file ("-->" vs "--X-->" vs em-dash compounds) — normalize (note). The verified *negative* relationship [39] (Walker→hot comb invention, refuted) is intentional per methodology §6 and is correct — keep.

---

## 11. RIGHTS

**Pass.** `rights-log.md` treats nothing as cleared:
- W4 explicitly states NMAAHC's "No Known Copyright Restrictions" is recorded under `unknown`, "not treated as clearance" — exactly right.
- "Public domain" is used only for U.S. federal government works (FSA-OWI photos, Congressional Record), which is correct, with "confirm the call number" caveats where appropriate.
- Everything else is "likely copyrighted — needs clearance" or "unknown — needs clearance."
- No language found implying any item is cleared for reuse. The W3 "safest visual assets" guidance correctly scopes to public-domain items.

---

## 12. TIMELINE

- **Dates: all real.** Programmatic validation of all 92 events: no impossible dates, no future dates, era ranges sane.
- **Chicago-relevance/scoping:** [44] (1959 Braun TP 1, MoMA) and [82] (2013 Fitzwilliam exhibition, Cambridge UK) are comparative/object-chain context rather than Chicago events — acceptable if the event text scopes them as such; recommend confirming the scoping language. (note)
- **"Verified dated events only" violated:** methodology §6 says timeline.json holds Verified dated events only, but 16 events rest on Provisional-grade evidence: [3] (Williams/Idlewild — Provisional + contradiction), [5][6] (1922 Defender pages — thesis-level), [10] (Lake Ivanhoe — single secondary source), [24] (1943 wedding announcement — citation only), [25] (1944 Harper quote — secondhand), [27] (grocery pricing — via summary), [31] (Rayner 1947 — company-supplied; entity downgraded), [32] (Negro Newsfront — "claimed"), [37] (Wonder Five "first" — entity downgraded), [55] (Karamu 1971 — single parenting-magazine source), [61] (1974 "steppin'" coined — dates vary 1973/74; asserting 1974 as "the evolutionary transition year" is overconfident), [63][69] (WKKC/WVAZ radio dates — Wikipedia), [66] (Hot Mix Five audience 250k–1M — "High" uncertainty; the parenthetical "claimed" is honest but the figure is journalistic color), [70] (1993 Johnson Products sale price — single radio-tribute source, no entity claim). **Fix:** annotate each event with its verification grade or remove the Provisional ones; the methodology statement must then match practice. (should-fix ×16)
- [54] (Soul Train premiere date) and [72] (Black Talk publication): Provisional-grade but standard facts; note only. (note)
- [80][84][86][87] accession years inferred from NMAAHC object-numbering convention — honestly labeled ("Accession year from object numbers"); keep the caveat attached. (note)
- Glosses not in entity evidence: [2] "an era of upward mobility," [19] "for the rising Black middle class." Reword or source. (note)

---

## Full Verified-claim assessment log (§8)

All 154 Verified claims were read against their evidence. Disposition: **downgrade 7** (listed in §1), **keep 147**. Kept claims include all museum-record-anchored W4 links except the two symbolism downgrades; all primary-testimony claims (oral histories, interviews, Congressional Record); and multi-source secondary claims. The most common keep rationale: the claim accurately reports what its source documents, and uncertainties disclose the residual risk. Full per-claim notes are in the auditor's working dump at `/tmp/entities_dump.txt` (ephemeral); the actionable outcomes are all in `changes.json`.

## Changes summary

| Severity | Count |
|---|---|
| blocking | 0 |
| should-fix | 44 |
| note | 9 |

**By category:** claim downgrades 7; claim edits 1; entity merges 2; entity/biography removals 2; biography-link downgrades 2; timeline merges 2; timeline grade flags 16; relationship flags 12.

## The 5 most serious findings

1. **relationships.json violates its verified-only rule** — 12 of 58 relationships rest on Provisional/interpretive evidence ([21] "church before church," [26] job-networks, [27] self-described "interpretive") or point from phantom entities ([22] Johnson Publishing Company, [25] Chicago Urban League) or to wrong targets ([12], [19]).
2. **timeline.json violates "Verified dated events only"** — 16 events rest on Provisional-grade evidence, and two duplicate pairs survive ([13]/[14] Bud Billiken with contradictory Kellum-vs-Abbott initiators; [26]/[28] Black Metropolis).
3. **Two unmerged entity duplicates** — E-048→E-006 (Bud Billiken Parade) and E-070→E-027 (Terkel Radio Archive); the rent-party merge precedent was not applied consistently, and the Bud Billiken pair carries contradictory initiator claims.
4. **Grade inflation on 9 items** — 7 Verified claims rest on Wikipedia-only, mirror-site, or company-supplied evidence (Johnson Products ×2, Afro Sheen slogans, DuSable day-dates, Bud Billiken celebrity list, Rayner founding, Wonder Five "first in America"); 2 biography symbolism links (ob-01 fist-pick, ob-04 catalog) fail the contemporary-source / methodology-§4.2 tests.
5. **ob-07/E-081 console stereo is a 0-Verified-link biography** built on Wikipedia + a hobbyist site — recommend removal until a verified holding and Black-household use evidence exist; plus a folk-etymology clause in E-047[0] (bid-whist term origins) that must be removed per the project's slang rule.

## Publication-readiness verdict

**Not yet ready — but close, and honestly built.** No blocking issues: nothing is fabricated, the Disputed links are correctly handled, rights are correctly un-cleared, and the workers' uncertainty/gaps discipline is the package's greatest strength. The 44 should-fix items are mechanical (downgrades, merges, removals, annotations) and fully specified in `changes.json`. Once applied — and once the methodology's "verified-only" promises for timeline/relationships are made true — the package is publication-ready as a clearly-graded research deliverable. Any public rendering must preserve the Provisional/Unresolved markings; stripping the grades would convert honest uncertainty into false authority.
