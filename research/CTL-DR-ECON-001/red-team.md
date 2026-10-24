# Red-Team Audit: CTL-DR-ECON-001 ("The Black Business Ecosystem") — Merged Corpus

**Auditor role:** red-team (adversarial review). **Date:** 2026-09-28.
**Scope:** `merge/entities.json` (65 entities, 301 claims), `merge/timeline.json` (187 events),
`merge/relationships.json` (61 relationships), `merge/sources.md`, `merge/merge-log.md`.
**Method:** full-corpus read; programmatic checks for duplicate claims, unresolvable references,
grade/source mismatches, and identifier-scheme consistency; spot web verification of four
load-bearing ambiguities (Arthur J. Wilson, Leaders Network Credit Union charter status,
Fuller→John H. Johnson "training" link, Johnson Products exchange listing).
**I did not edit any files.** Severity scale: **blocking** = must fix before any public
rendering; **should-fix** = correct before or during publication pass; **note** = confirmed
solid, minor polish, or residual risk to watch.

---

## A. Findings

### Blocking

**F-001 — Fuller/Pittsburgh Courier purchase: Verified in one entity, Disputed in another.**
Entity: ECON-025 (Fuller Products Company). Claim: *"Fuller purchased the Regal Theater, the
South Center department store, and Black newspaper properties including the Pittsburgh Courier
and the New York Age — recirculating manufacturing profits into community-facing institutions
and media."* Grade: **Verified**. But ECON-055 (Samuel B. Fuller) carries a **Disputed** claim on
the same fact: *"Fuller purchased several Black newspapers including the New York Age and the
Pittsburgh Courier. The Courier claim is contradicted: the Pittsburgh Courier was sold in 1965
to John H. Sengstacke of the Chicago Defender"* (evidence: E&P 2017; Pitt Chronicle 2010;
Wikipedia Pittsburgh Courier). The merge propagated the dispute to the person entity but left the
company entity asserting the purchase as Verified. The same ECON-025 claim asserts the South
Center purchase as Verified while ECON-055 grades South Center "acquisition year unverified"
(Provisional). **Recommendation:** downgrade the ECON-025 claim to Disputed/Provisional, attach
the Sengstacke contradiction, and split the Regal (solid, City landmark report) from the
newspaper/South Center acquisitions.

**F-002 — Poro College founding year: entity contradicts itself; timeline picks the disputed side.**
Entity: ECON-052 (Poro College). Claim A (Disputed): *"Poro College was founded in St. Louis —
1917 per Good Black News/Face2Face, 1918 per SHSMO."* Claim B (**Verified**): *"Annie Turnbo
Malone founded Poro College in 1918 in St. Louis as the first U.S. educational institution
dedicated to Black cosmetology."* Both cannot stand. Timeline compounds it: event [22] is
Disputed (1917 vs 1918) but events [23] and [24] assert "Poro College opened 1918" as
**Verified**. The merge recorded the dispute and then published the disputed side as fact.
**Recommendation:** downgrade claim B and timeline [23]/[24] to Disputed (or delete the redundant
timeline events), keeping the "first U.S. institution dedicated to Black cosmetology"
superlative only with its dispute attached.

**F-003 — Unsupported Verified relationship: Fuller "trained" John H. Johnson.**
`relationships.json` [3]: subject `ECON-W2-001` (S.B. Fuller), relation `trained`, object
"John H. Johnson (founder of ECON-W2-007)", grade **Verified**. The corpus's own entity claim
(ECON-055) says only that Fuller's company "trained and inspired a generation... including John
H. Johnson... and George E. Johnson," with the uncertainty note *"Characterization of training
relationship is broad; specifics (dates, roles) not documented."* A web spot-check confirms
George E. Johnson sold door-to-door for Fuller Products (wordinblack.com 2026; WSJ 2026), but
finds no evidence John H. Johnson (Supreme Life 1936–42, founded Negro Digest 1942) ever worked
in Fuller's sales organization — the John H. Johnson link is "mentorship/inspiration" lore at
best. **Recommendation:** change relation to `influenced/mentored` at Provisional, or drop the
edge. (The George E. Johnson edge [2] is fine.)

**F-004 — 35 of 187 timeline events have no grade and no source.**
`timeline.json`: 35 events carry neither `grade` nor `source` (e.g., [12] *"Jesse Binga opens a
private bank — the first Black-owned bank in the Northern U.S."*, [25] Liberty Life founding,
[36] Douglass Bank "1922/1923 (disputed)"). Ungraded events assert superlatives and disputed
dates as flat fact, and the merge-log's "Verified-only" policy language does not cover the
timeline. **Recommendation:** grade every event (or delete the unsourced ones); nothing ungraded
may render publicly.

**F-005 — WVON electoral causality asserted as Verified.**
Entity: ECON-064. Claim: *"In 1986 WVON adopted a Black-oriented all-talk format; the station
was instrumental in electing Harold Washington (1983), Carol Moseley Braun, and Barack
Obama."* Grade: **Verified**. The evidence is a Congressional tribute, and the corpus itself
flags *"Electoral-causality claims are the Congressional tribute's, not independently
quantified"* plus a CONTRADICTS note that Washington's 1983 election predates the 1986 format
change. A tribute's causal boast is not verification. **Recommendation:** downgrade to
Provisional; reword as attributed claim ("credited by supporters/tributes with..."); separate the
1983 Washington role (pre-talk format) from later elections.

**F-006 — "Six-hour dollar" debunk lacks an entity-level flag and could be misread as fact.**
Entity: ECON-002. The debunking is correct (Spriggs/TruthBeTold; content confirmed solid), but it
is encoded only as two Verified *claims* inside an entity of type `disputed_claim` named
"(debunked quantification)". There is no entity-level grade or `status: debunked` field anywhere
in `entities.json` (entities have no grade field at all). A downstream page builder reading
"Verified" claims could render this as a fact entity. **Recommendation:** add an explicit
entity-level `status: debunked` (and consider renaming to remove the bare statistic from the
title). Related hygiene: claim 2's evidence cites `ECON-W5-006`/`ECON-W5-007` (worker IDs);
rewrite as ECON-048 / ECON-001.

**F-007 — relationships.json is not a traversable graph: mixed identifier scheme, duplicates.**
Endpoints mix worker IDs (`ECON-W2-001`), free-text names ("John H. Johnson", "Victory Life
Insurance Company", "Supreme Life Insurance Company"), and bracketed external refs ("Douglass
National Bank [CTL-DR-BVM-005]"). Many free-text endpoints duplicate merged entities that have
ECON-001..065 IDs: Victory Life→ECON-063, Supreme Life→ECON-061, Regal Theater→ECON-053,
Johnson Products→ECON-034, Independence Bank→ECON-031, Operation Breadbasket→ECON-048,
Poro College→ECON-052, Annie Turnbo Malone→ECON-007, Best Chicago Meat→ECON-009. Near-duplicate
edges assert the same fact repeatedly: [1]/[47]/[51] (Fuller→Regal purchase ×3), [12]/[49] and
[13]/[50] (John H. Johnson↔Supreme Life/JPC pairs). Per the project's data-architecture rule
(every project feeds a shared Relationship Graph), this file cannot be ingested as-is.
**Recommendation:** normalize all endpoints to merged ECON-IDs (or typed external refs),
dedupe, and re-verify each edge's grade after F-003 and F-025 are resolved.

### Should-fix

**F-008 — ECON-011 duplicate claims, conflicting grades.** Two near-identical claims (0.77 text
similarity): Provisional *"Jesse Binga opened a private bank in 1908; it received an Illinois
state charter in 1921... first black-owned bank in the Northern U.S."* (Kansas City Fed) and
Verified *"Binga opened a private bank in 1908; it received a state charter in 1921... closed in
1930. It was the first Black-owned bank in the Northern U.S."* (BVM-005 cross-ref). Same fact,
two grades. **Recommendation:** consolidate into one claim, one grade.

**F-009 — ECON-055 duplicate claims.** Regal purchase appears as Verified (City landmark report)
and Provisional (BVM-005 cross-ref); NAACP/Business League leadership appears twice
(Verified + Provisional, 0.55 similarity). **Recommendation:** consolidate; keep the strongest
sourcing.

**F-010 — ECON-061 duplicate claims.** Supreme Life founding appears as Provisional
(blackhistoryheroes) and Verified (BHR abstract), 0.77 similarity. **Recommendation:**
consolidate.

**F-011 — ECON-040 overlapping founding-capital claims.** Three variants of the 1933 founding
capital ($500 loan from grandmother Dottie Leak vs. $500 loan + $500 World's Fair earnings),
graded Provisional and Verified inconsistently. **Recommendation:** one claim with the variants
explicitly noted (the corpus already documents the variant honestly — just unify it).

**F-012 — ECON-045 duplicate claims.** The 1912 ordinance + "hotbed of entrepreneurial
micro-capitalism" passage appears twice, both Verified. **Recommendation:** consolidate.

**F-013 — ECON-042 picket claims, mismatched specificity/grade.** Verified: *"In 1965-66,
civil-rights organizers picketed white-owned businesses on Madison Street..."*; Provisional:
*"In 1965-1966, Martin Luther King Jr. and SCLC organizers picketed..."* (both ProPublica).
**Recommendation:** keep both but cross-note: the King-personally-picketed detail is the
Provisional one; do not let the Verified claim silently inherit it.

**F-014 — ECON-034 exchange-listing dispute is resolvable — resolve it.** Claim (Disputed): 1971
first Black-owned company on a U.S. stock exchange — AMEX per Black Enterprise, NYSE per BET.
A second claim (Verified, AP obituary July 2026 via Hamilton County Herald) confirms **American
Stock Exchange**, corroborated by v103. BET's NYSE variant looks like the error.
**Recommendation:** mark the BET NYSE variant erroneous, close the dispute as AMEX.

**F-015 — ECON-034 "first African-American company to sponsor a nationally syndicated television
program" — Verified on Wikipedia alone.** Superlative resting on a single tertiary chain
(claim: *"Beginning 1971 the company sponsored Soul Train..."*). **Recommendation:** downgrade to
Provisional pending Black Enterprise/contemporary-press corroboration.

**F-016 — ECON-012 Ida Gray Nelson Rollins — Verified on Wikipedia alone.** Claim: *"graduated
from the University of Michigan College of Dentistry in 1890 as the first African-American woman
dentist in the United States."* Single chain, and the claim carries a "grade propagated"
flag. **Recommendation:** downgrade to Provisional until U-M/dental-history source is checked
(the fact is likely correct, but the grade is unearned).

**F-017 — ECON-021 Travis claim 3 (Nixon/Ford task forces) — Verified, Wikipedia single chain.**
**Recommendation:** downgrade to Provisional.

**F-018 — ECON-033 Moutoussamy claim 3 (IIT 1948, Mies van der Rohe) — Verified, Wikipedia single
chain.** **Recommendation:** downgrade to Provisional.

**F-019 — ECON-065 Bailey claim 2 (Overton Hygienic Building office; Little Rock/Hot Springs
commissions) — Verified, Wikipedia single chain.** **Recommendation:** downgrade to Provisional.

**F-020 — ECON-019 Cosmopolitan Chamber "pioneered" mentor program — Verified, single 2026
industry source** (Powering Chicago). A superlative ("pioneered") on one trade source.
**Recommendation:** downgrade to Provisional.

**F-021 — ECON-016 Cook County 40% set-aside struck down — Verified, single Feminist Majority
Foundation news item**, no case citation. **Recommendation:** downgrade to Provisional pending
case record.

**F-022 — ECON-055 "first African American inducted into the National Association of
Manufacturers (1963)" — Verified, Wikipedia only.** **Recommendation:** downgrade to Provisional
pending NAM records.

**F-023 — ECON-023 Dickerson claim 3, partially weak.** LDF organizing + alderman role are
NPS/Stanford-backed (keep Verified); the office-sharing-with-Wendell-Green detail is
Wikipedia-only. **Recommendation:** split the claim; downgrade the office-sharing detail.

**F-024 — Timeline "deduped" claim is false: ~14 near-duplicate pairs.** Regal purchase ×3
([110]/[111]/[112]); Boyer purchase ×2 ([85]/[86]); Fuller bankruptcy ×2 ([140]/[142]); Poro
relocation ×2; Binga closure ×2 ([57]/[60]); Malone death ×2 ([102]/[103]); Supreme Life building
purchase ×3 ([38]/[39]/[40]); Liberty Life founding ×2 ([25]/[27]); Overton Hygienic commission
×2 ([32]/[35]); Seaway founding ×2 ([121]/[122], with a "Seaway Bank and Trust Company" naming
variant); Madison pickets ×2 ([125]/[127]); Leak relocation ×2 ([105]/[106]); Poro 1951 loss ×2
([94]/[95]); Douglass founding ×2 ([33]/[34]). **Recommendation:** dedupe to one event per fact;
keep dispute annotations on the survivor.

**F-025 — Relationship [59] (small-business credit gap) is Verified on an aggregator chain with
no backing entity.** Evidence: *"WBEZ via moguldom.com"* for the Woodstock Institute 'Patterns
of Disparity' finding (28,000 more loans / $350M at parity). Moguldom is a weak relay, and no
entity in `entities.json` documents this finding — the relationship is orphaned from the entity
corpus. **Recommendation:** downgrade to Provisional; cite the Woodstock Institute report
directly; add a backing entity or drop the edge.

**F-026 — ECON-039 Leaders Network Credit Union implies an operating institution on a 2023
groundbreaking.** DATES: "2023-"; claim honestly notes *"opening status and NCUA charter outcome
need verification"* (Provisional). A web check (2026-09-28) found no NCUA listing under that
name. **Recommendation:** change dates to "2023 (groundbreaking; operating status unverified)";
verify charter before any public page presents it as active.

**F-027 — ECON-061 "$1.65 trillion in insurance in force" (1960) is arithmetically implausible.**
Claim (Provisional): NIA's 46 member companies held *"a reported $1.65 trillion in insurance in
force and $300 million in assets."* A 5,500:1 in-force-to-assets ratio is impossible for
insurers, and $1.65T exceeded plausible 1960 totals — likely a transcription error for $1.65
billion. The claim already flags checking Abner (1962). **Recommendation:** check Abner before
any rendering; do not publish the figure as-is.

**F-028 — Stale worker-ID citations in merged claims.** ECON-002 evidence cites `ECON-W5-006` /
`ECON-W5-007` (resolve to ECON-048 / ECON-001 but are not rewritten). **Recommendation:**
rewrite all claim/evidence text to merged ECON-IDs.

**F-029 — Arthur J. Wilson appears in two bank entities without linkage.** ECON-044: Wilson was
Binga State Bank cashier, later VP, mentor to Mary T. Washington Wylie. ECON-022: "Cashier
Arthur J. Wilson" per officer signatures on Douglass National Bank currency. A web check
(Wikipedia, citing standard bios) confirms Wilson was Binga's cashier then VP; the Douglass
currency signature suggests a later Douglass role (plausible: Binga closed 1930, Douglass 1932).
The corpus never states whether this is one man. **Recommendation:** add an uncertainty note
linking the two (likely same person, career sequence unconfirmed) or verify via bank records.

**F-030 — Superlatives stranded in entity summaries without claims.** ECON-008 summary: *"the
largest Black-owned business conglomerate of early 20th-century Chicago"*; ECON-025 summary:
*"the largest Black-owned direct-sales company of its era."* No dedicated claim/evidence backs
either superlative (Weems 2020 would support the Overton one). **Recommendation:** promote each
to a graded claim with citation, or soften the summary language.

### Notes (confirmed solid / residual watch)

**N-001 — Six-hour dollar debunk: content is correct.** Traces to Brooke Stephens's 1996
*Talking Dollars and Making Sense* (names no study); Spriggs/TruthBeTold debunk documented;
the "leakage campaigns are real, the number is not" distinction is exactly right. Only the
encoding needs F-006.

**N-002 — Joyner patent: correct.** U.S. Patent 1,693,515 recorded as Verified (NIHF, Lemelson,
Stanford Tech. L. Rev.); the 1,683,530 variant noted as erroneous with BVM-005 flagged for
correction. Textbook handling.

**N-003 — Most disputed dates/numbers are handled honestly.** Fuller bankruptcy 1969 vs 1971
(Disputed, ECON-025/055, timeline [140]/[142]); Douglass founding 1921/1922/1923 (Disputed,
ECON-022, timeline [33]/[34]); Overton birth (1865 vs 1864) and death day (July 2 vs 3)
(Disputed, ECON-008); Jones syndicate $18M/$25M/$100M (Disputed, "Do not publish a single figure
as fact," ECON-036); Binga embezzlement narrative flagged single-sourced (ECON-011); Arthur
Wilson's CPA ordinal contradiction recorded (ECON-044). The exceptions are F-002.

**N-004 — Women and working-class gaps are acknowledged, not papered over.** ECON-014
(boarding-house keepers: named keepers "the largest named-firm gap in this track"),
ECON-032 (independent beauty shops "survive in the record mainly as a sector, not as named
firms — a documented erasure"), ECON-042 (Madison Street named firms "largest geographic gap"),
ECON-043 (Joyner's salon address unrecoverable except via Defender ads/directories), ECON-005
(87th Street earlier history "unresolved... not an absence"). Women's institutional coverage
(Malone, Washington Wylie, Joyner, Henderson, Rollins, Bettiann Gardner, Joan Johnson, AKA
credit union) is substantive. Residual: domestic/laundry/seamstress occupations are absent, but
the corpus does not claim to cover them.

**N-005 — No survivorship whitewash; failure is documented.** Binga (1930), Douglass (1932),
Chicago Metropolitan's decline, Fuller's bankruptcy, Seaway's 2017 failure ($57.2M DIF loss,
FDIC OIG), Covenant Bank's 2013 closure, JPC's 2019 Chapter 7, Independence Bank's sale to
ShoreBank. Famous-firm overclaims are the specific F-items (F-001, F-005, F-015), not a
pattern.

**N-006 — Rights/copyright: clean, with two pre-publication checks.** No long copyrighted-text
reproduction found; quotations (Pace 1934, slogans) are short and attributed. Before public
use: (a) ECON-028's "Half-Century Magazine on archive.org / 1916–1928 public domain" is
Provisional with "holdings not spot-checked" — verify holdings and PD status before linking;
(b) ECON-060's NARA street-vendor photos are cited via a BuzzFeed essay — cite NARA/DOCUMERICA
directly (federal public domain) instead of the BuzzFeed relay; (c) ECON-052's WHMC Poro photo
rights are honestly flagged unverified — keep flagged.

**N-007 — The 111 "Grade propagated from worker entity-level overall_grade... pending red-team
review" notes are honest merge hygiene.** This report's F-014–F-023 downgrades constitute that
red-team review for the weakest Verified propagations. Remaining propagated grades I spot-checked
(ECON-003, ECON-004, ECON-005, ECON-017, ECON-029, ECON-061 provisionals) look appropriate.

**N-008 — Cross-package references show no contradictions beyond F-001.** Binga June-1930
closure consistent across ECON-011/059/022; State Street Black-owned vs 47th-complex
white-financed boundary (ECON-059, from BVM-005) consistent with ECON-008/053/055; Regal
1961/1968/1973 dates consistent across ECON-025/053/055/056; Breadbasket→Seaway deposit figures
consistent between ECON-048 and ECON-056; Supreme Life building dates consistent between
ECON-035/059/061; PLACE-001's 63rd Street evidence boundary faithfully reproduced (ECON-003).

**N-009 — Merge-log accurately describes the merges/splits performed** (14 merges, 3 splits;
65 entities verified present). The log's "deduped" timeline claim (F-024) and silence on
relationship ID normalization (F-007) are its gaps.

**N-010 — ECON-036 properly hedges the policy-kings reinvestment thesis.** *"'The claim that
policy capital formed a material share of Bronzeville's legitimate business capitalization is
NOT established — separate it from the documented fact of community reinvestment/philanthropy.'"*
This is the standard the rest of the corpus should meet.

**N-011 — No missed duplicate entities found.** Checked candidate pairs: Binga Block
storefronts vs Binga State Bank (distinct subjects), Fuller person vs Fuller Products (correctly
split), Poro College vs Annie Malone, Overton vs his four companies, Johnson Products vs
Independence Bank, beauty-shops sector vs Joyner's salon. All correctly separate.

**N-012 — ECON-013's NOI-grocery causal claim** ("collapsed as Black shoppers moved to
white-owned chains after integration") rests on a single oral-history chain and is correctly
Provisional. Do not upgrade without corroboration; the causal mechanism is plausible but
single-sourced.

---

## B. Summary counts

| Severity | Count | IDs |
|---|---|---|
| **Blocking** | **7** | F-001 – F-007 |
| **Should-fix** | **23** | F-008 – F-030 |
| **Note** | **12** | N-001 – N-012 |
| **Total findings** | **42** | |

Claim-grade distribution in `entities.json`: 140 Verified / 144 Provisional / 9 Disputed /
8 Unresolved (301 claims). Timeline: 108 Verified / 34 Provisional / 10 Disputed / **35
ungraded**. Relationships: 61, all labeled Verified (several should not be: F-003, F-025).

## C. Blocking issues that must be fixed before publication

1. **Fuller/Pittsburgh Courier contradiction across entities (F-001).** ECON-025 asserts the
Courier purchase as Verified; ECON-055 records it as Disputed/contradicted (sold to Sengstacke,
1965). A public page would publish a false newspaper acquisition. Downgrade ECON-025 and attach
the contradiction.
2. **Poro College founding-year self-contradiction (F-002).** ECON-052 asserts 1918 as Verified
while grading 1917-vs-1918 Disputed; timeline events [23]/[24] publish the disputed side as
Verified. Reconcile to Disputed throughout.
3. **Relationship graph integrity (F-007), including the false Fuller→John H. Johnson "trained"
edge (F-003).** Mixed worker-ID / free-text / bracketed endpoints, duplicate edges, and one
Verified edge with no evidentiary basis. Normalize endpoints to merged ECON-IDs, dedupe, and
re-grade.
4. **35 ungraded, unsourced timeline events (F-004).** Several assert superlatives as fact.
Grade or remove; none may render publicly.
5. **WVON electoral causality as Verified (F-005).** A Congressional tribute's causal boast
("instrumental in electing...") is not verification — and the corpus itself notes the
Washington-1983/format-1986 anachronism. Downgrade to attributed Provisional.
6. **Six-hour-dollar entity needs an entity-level debunked flag (F-006).** The debunk content is
right; the encoding lets a renderer misread Verified claims as fact. Add `status: debunked`.

## D. What's solid (fairness statement)

The merge is substantially honest: disputes are usually recorded rather than smoothed over
(N-003), gaps are named as gaps (N-004), failure cases sit alongside successes (N-005),
propagated grades are explicitly marked pending review (N-007), cross-package citations are
consistent (N-008), the Joyner patent and six-hour-dollar debunk are handled correctly (N-001,
N-002), and no copyrighted text is reproduced (N-006). The blocking items are fixable
reconciliation and encoding problems, not a rotten corpus. The single most valuable
pre-publication step after the blocking fixes is the F-014–F-023 downgrade pass on
Wikipedia/single-chain claims currently sitting at Verified.
