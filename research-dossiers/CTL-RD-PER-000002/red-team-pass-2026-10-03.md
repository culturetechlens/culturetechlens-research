# CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# Red-Team Pass — Marcus Freeman Package (CTL-RD-PER-000002)

**Audit date:** 2026-10-03  
**Auditor role:** adversarial review only. No draft was rewritten and nothing was published.  
**Materials audited:** `dossier.md`, `evidence-file.md`, `entities.json`, `relationships.json`, `gaps.md`, `sources.md`, `visuals.md`; derivatives `freeman-essay-2026-10-03.md` and `freeman-article-2026-10-03.md`; research backbone `/home/hatch/workspace/research_notes/marcus-freeman-dossier-20261003-1810/report.md`.  
**Backbone convention used:** `(verified)` = full page opened 2026-10-03; `(index)` = snippet/search-result tier only.

## Verdict

**Publishable with fixes — not safe to publish as-is.**

The five headline corrections survive independent re-verification. The core record (draft team, Willingham/Freeman order, title-game firsts, 30th-coach count, contract caution) is not fabricated. But the package is not publishable in its current form: the dossier's narrative claim pointers repeatedly send readers to the wrong ledger claims; five VERIFIED claims contain index-tier subclaims despite the dossier's own grading rule; one direct-quote passage in the essay is presented out of sequence; the essay turns Freeman's 0–3 tenure start into a false "first team started 0–3"; the article adds an unsupported "misdemeanor" classification; and the dossier prints the single-source $70.8M buyout figure in its Myth table while elsewhere saying the figure is not printed.

**Severity counts:** BLOCKER 6 · SERIOUS 3 · MINOR 7 · CLEAN 6 checks passed.

---

## BLOCKER findings

### B-01 — Narrative claim cross-references in dossier §§03 and 09–12 point to adjacent or unrelated ledger claims

- **Files/locations:** `dossier.md` lines 55–59 (§03); lines 151–161 (§09); lines 167–172 (§10); lines 186–191 (§12). Contrast with the ledger at `dossier.md` lines 219–273 and the matching records in `evidence-file.md` (e.g., CLAIM-008 at line 202, CLAIM-015 at line 380, CLAIM-021 at line 532, CLAIM-026 at line 660, CLAIM-042 at line 1066, CLAIM-055 at line 1399).
- **Claim under audit:** That the dossier's narrative sections trace each summarized claim to the correct CLAIM ID in the §15 ledger.
- **Problem:** The ledger, evidence file, `entities.json`, and `relationships.json` align with each other; the narrative pointers do not. Examples: §03 line 55 cites CLAIM-022 for the FBS title-game first, but the ledger assigns that claim to CLAIM-021 (CLAIM-022 is the Norm Chow / first Asian American at Notre Dame claim). Line 56 cites CLAIM-019 and CLAIM-021 for Willingham-first/Freeman-second; the football-specific claim is CLAIM-018 and the media-error claim is CLAIM-020. Line 57 cites CLAIM-049 for the coordinator/position-coach pattern; the ledger assigns that pattern to CLAIM-048 (CLAIM-049 is the Mickens/Ash transaction). Line 58 cites CLAIM-027 for the 2024 season; the ledger assigns it to CLAIM-026. The same +1 / adjacent-claim drift recurs through §09 (Willingham, Kelly/Swarbrick/Bevacqua, Locksley, Mickens, Franklin/Tucker, Edmonds, Chow), §10 (CFP, NCMFC, Catholic conversion), and §12 (Players' Tribune, Dodd dispute, 10-men finish, CFP, Orange Bowl, bowl opt-out).
- **Evidence:** Ledger text at `dossier.md` lines 236–273 defines the claims; the narrative citations at lines 55–59, 151–161, 167–172, and 186–191 do not match those definitions. This is a traceability defect, not proof that the underlying facts are false — but for a dossier whose stated method is claim-by-claim traceability, broken pointers are publication-blocking.

### B-02 — Five VERIFIED claims contain subclaims supported only by `(index)` sourcing in the backbone

- **Files/locations:** `dossier.md` ledger lines 226 (CLAIM-008), 233 (CLAIM-015), 244 (CLAIM-026), 260 (CLAIM-042), 273 (CLAIM-055); the dossier's contrary assurance at `dossier.md` line 277; the rule restated in `sources.md` line 12.
- **Claim under audit:** "No claim in this ledger grades above the backbone's sourcing flag: `(verified)` sources support VERIFIED; `(index)` sourcing caps at SUPPORTED."
- **Problem:** That assurance is false for bundled subclaims inside five VERIFIED claims:
  - CLAIM-008 (VERIFIED): practice-squad stops are `(verified)` in backbone line 46–47, but "never played a regular-season NFL game" is carried at backbone line 48 as "(Multiple sources, index)." The dossier's §16 evidence repeats the index-tier attestation without downgrading the bundled claim.
  - CLAIM-015 (VERIFIED): the December 3, 2021 announcement is `(verified)` (backbone line 74, FightingIrish.com), but the December 6, 2021 introduction date in the same backbone sentence is sourced to ESPN/Field Level Media `(index)`.
  - CLAIM-026 (VERIFIED): the 2024 record and game results are `(verified)`, but "final AP No. 2 is the highest postseason ranking since 1993" is attributed at backbone line 116 to 247Sports `(index)`. The dossier's §16 evidence itself flags that ranking framing as `(index)`.
  - CLAIM-042 (VERIFIED): the *Players' Tribune* text is `(verified)` (backbone line 223), but the December 12, 2021 clarification date is `(index)` at backbone line 170 (On3; 247Sports).
  - CLAIM-055 (VERIFIED): Freeman's NCMFC membership is in his `(verified)` *Players' Tribune* text (backbone line 224), but the coalition's 2020 founding by Mike Locksley appears at backbone line 160 as AP `(index)`.
- **Evidence:** Backbone lines 48, 74, 116, 160, 170, 223–224; dossier ledger lines 226, 233, 244, 260, 273; dossier line 277; `sources.md` line 12. Independent checking during this audit corroborated several of the underlying facts — the failure is grade discipline against CTL's own rule, not necessarily factual falsity. As written, the dossier overclaims its verification tier.

### B-03 — Essay presents the January 9, 2025 Freeman quote out of sequence

- **Files/locations:** `freeman-essay-2026-10-03.md` line 24; backbone quoted passage at `report.md` line 227.
- **Claim under audit:** That Freeman, asked about the title-game milestone afterward, first deflected with "this ain't about me. This is about us," and *then* said he hoped all coaches keep getting opportunities.
- **Problem:** The backbone gives the opposite order in one continuous postgame statement: "It is an honor, and I hope all coaches, minorities, Black, Asian, white, it doesn't matter, great people continue to get opportunities to lead young men like this. But this ain't about me. This is about us." The essay moves the "this ain't about me" fragment before the hope/opportunity fragment, lowercases the fragment's opening, and paraphrases "continue to get" as "keep getting" outside the quoted fragment while narrating the sequence with "Then he said…". The quoted words are real; the presented sequence is not the sequence in the backbone.
- **Evidence:** Essay line 24 vs. backbone line 227. Direct quotes must be verbatim *and* in order when the draft narrates order. This is a quote-integrity failure in the essay's centerpiece passage.

### B-04 — Essay converts Freeman's 0–3 tenure start into a false "first team started 0–3"

- **Files/locations:** `freeman-essay-2026-10-03.md` line 26; compare `dossier.md` line 119 and backbone `report.md` line 110.
- **Claim under audit:** "His first team started 0–3."
- **Problem:** Freeman started his head-coaching tenure 0–3 across two seasons: the January 1, 2022 Fiesta Bowl (the 2021 season's bowl, credited to Freeman) plus the first two games of the 2022 season (Ohio State and Marshall). The 2022 team itself started 0–2, not 0–3. The dossier's own §07 phrasing at line 119 ("2022 opened 0–3 (the Fiesta Bowl plus Ohio State and Marshall)") invites the same conflation, and the essay hardens it into "His first team started 0–3."
- **Evidence:** Backbone line 110 states the supported version precisely: "First head coach in Notre Dame history to start 0–3 (Fiesta loss + losses to No. 2 Ohio State … and Marshall)." Dossier §05/§25 correctly credit the Fiesta Bowl to the 2021 accounting. The essay sentence is materially false as written.

### B-05 — Article adds an unsupported "misdemeanor" classification to the January 2026 battery allegation

- **Files/locations:** `freeman-article-2026-10-03.md` line 84; dossier CLAIM-053 at `dossier.md` ledger (January 2026 allegation record) and §16 evidence; backbone `report.md` line 206.
- **Claim under audit:** That the January 2026 wrestling-meet matter was a "misdemeanor battery allegation."
- **Problem:** No audited source supports the word "misdemeanor." The supported record is narrower: a battery allegation arising from the January 3, 2026 Al Smith Invitational; Mishawaka police investigation; and the St. Joseph County Prosecutor's January 12, 2026 determination that "no criminal battery occurred" and that no criminal charges would be filed. Adding a charge-level classification ("misdemeanor") that neither the prosecutor's reported statement nor CLAIM-053 contains is an unsupported legal characterization.
- **Evidence:** Article line 84 vs. backbone line 206 (prosecutor's quoted determination) and the dossier's own CLAIM-053 wording, which says "battery allegation" without any misdemeanor classification. Legal wording must not outrun the prosecutor's record.

### B-06 — Dossier prints the UNRESOLVED $70.8M buyout figure while stating that it does not print the figure

- **Files/locations:** `dossier.md` line 121 ("A detailed buyout table circulating from a single source is graded UNRESOLVED and is not repeated here"); `dossier.md` §16 CLAIM-034 evidence ("This dossier does not print its numbers"); `dossier.md` §27 Myth table row 7 at line 429; `gaps.md` line 35 ("no edge, no numbers printed").
- **Claim under audit:** That the single-source buyout figures are graded UNRESOLVED and are not printed in the package.
- **Problem:** §27 row 7 prints the figure anyway — "Freeman's buyout is $70.8M after 2025" — inside the myth claim being rebutted, and then asserts in the same row "not printed." Presenting an UNRESOLVED single-source number in a quotable myth row still publishes the number, and it directly contradicts the dossier's §07 statement, its CLAIM-034 evidence note, and `gaps.md`.
- **Evidence:** Dossier line 121, §16 CLAIM-034 evidence, and §27 line 429; `gaps.md` line 35. The essay and article correctly omit buyout figures; the dossier does not.

---

## SERIOUS findings

### S-01 — Publication window and current contract state are not cleanly fixed in the derivatives

- **Files/locations:** `freeman-article-2026-10-03.md` lines 61 and 90; `freeman-essay-2026-10-03.md` line 30; `gaps.md` lines 42 and 51 (Open Question 10).
- **Claim under audit:** That the October 3, 2026 derivatives present a current, internally consistent record.
- **Problem:** The record core runs through the 2025 season, while the drafts are dated October 3, 2026 and include January 2026 events. More concretely, the article first reports a December 2025 restructure "above $10 million annually through 2031" (line 61), then closes by describing Freeman as "extended through 2030" (line 90) without reconciling the two contract states. The essay's closing "Four seasons in, 43–12" (line 30) omits an explicit "through the 2025 season" limit in that sentence. `gaps.md` itself leaves the cutoff unresolved: 2026-season material is "excluded until the cutoff date is fixed," and a future-research item says to "Confirm the publication cutoff … before the derivatives are revised."
- **Evidence:** Article lines 61 vs. 90; essay line 30; `gaps.md` lines 42 and 51. This is a publication-gate defect: a reader cannot tell from the closing lines whether "through 2030" is the operative term or superseded reported term, or whether 43–12 is a through-2025 accounting or a current record.

### S-02 — Dossier §35 (Cultural Lens) broadens two "first" claims beyond the ledger and backbone

- **Files/locations:** `dossier.md` line 489 (§35 Representation); ledger CLAIM-022 at `dossier.md` §15; backbone `report.md` line 89.
- **Claim under audit:** That Freeman is "the first of Korean descent anywhere in the FBS head-coaching ranks after Norm Chow," and at Notre Dame "the first Asian American head coach in any capacity the record shows."
- **Problem:** The ledger's supported claim (CLAIM-022) is narrower: second FBS head coach of Asian descent after Norm Chow, and first Asian American head coach at Notre Dame. The backbone (line 89) supports exactly that narrower wording and expressly notes that "Asian descent" is the sources' wording, with Chow of Chinese/Hawaiian descent. §35's "first of Korean descent anywhere … after Norm Chow" introduces an unledgered superlative the backbone does not state, and "in any capacity" broadens "head coach" beyond the graded claim — in a section that simultaneously argues the dossier's job is to keep representation claims exact.
- **Evidence:** Dossier line 489 vs. CLAIM-022 (ledger) and backbone line 89. The underlying narrower claims are supported; the §35 expansions are not traced to any claim ID.

### S-03 — Essay paraphrases the Pivot Podcast hiring philosophy in a way that drops its racial-opportunity clause, despite the package's own transcription warning

- **Files/locations:** `freeman-essay-2026-10-03.md` line 28; backbone `report.md` line 195 (§11 staff/hiring discussion) and line 170 (Pivot revisit, index); `gaps.md` line 48.
- **Claim under audit:** "Freeman has been blunt about the standard — qualified people who can help you win, full stop."
- **Problem:** The backbone's version of Freeman's stated philosophy is not race-neutral: "If there's a qualified Black man or minority, search and find them. But, at the end of the day, if you can't help us win, I can have every coach on my staff be Black, and if we lose, we're all gone." The essay's compressed paraphrase deletes the "search and find" qualified-Black/minority clause and presents only the win-standard half — in the very paragraph where the essay argues Freeman's standard "turns back on his program." Compounding the problem, the backbone carries the Pivot passage as an On3 `(index)` summary, the dossier gives it no ledger claim, and `gaps.md` line 48 expressly requires transcribing the Pivot segment "before any print use of its hiring-philosophy passage."
- **Evidence:** Essay line 28 vs. backbone lines 170 and 195; `gaps.md` line 48. The essay's thesis does not need this passage — the verified *Players' Tribune* text carries the opportunity argument — but as written the paraphrase both outruns its sourcing tier and changes the emphasis of the quoted philosophy.

---

## MINOR findings

### M-01 — Article overstates the Buffalo practice-squad stint as "three weeks"

- **Files/locations:** `freeman-article-2026-10-03.md` line 16; `dossier.md` §05 dates table and CLAIM-008.
- **Claim:** Freeman "spent three weeks on Buffalo's practice squad."
- **Problem/evidence:** The package's own dates are September 22–October 5, 2009 — 13 elapsed days (14 calendar days inclusive). "Three weeks" overstates the stint the dossier elsewhere dates precisely.

### M-02 — Article lists Tommy Rees among coordinators Freeman "has hired"; the record describes Rees as retained

- **Files/locations:** `freeman-article-2026-10-03.md` line 75; `dossier.md` §03/§09 and CLAIM-048 ("every coordinator he has employed").
- **Claim:** "every coordinator he has hired — Tommy Rees, Al Golden, Mike Denbrock, Chris Ash."
- **Problem/evidence:** Rees was Brian Kelly's offensive coordinator whom Freeman retained on taking the job; the dossier's own safer verb is "employed." The racial pattern claim itself is supported (CLAIM-048); the verb "hired" is wrong for Rees.

### M-03 — Article's correction bullet drops "head coach" and "FBS" from the title-game first

- **Files/locations:** `freeman-article-2026-10-03.md` line 82; dossier CLAIM-021.
- **Claim:** Freeman is "the first Black and first Asian American coach in a national title game."
- **Problem/evidence:** The graded claim is bounded: first Black and first Asian American *head coach* to lead a team into an *FBS* national championship game. The bullet's unqualified "coach in a national title game" reads broader than the evidence (assistant coaches and other divisions are different claims). The article states the bounded version correctly elsewhere (record section), so this is a precision slip, not a false first.

### M-04 — Essay inserts a comma into the "wrong decision twice" quotation

- **Files/locations:** `freeman-essay-2026-10-03.md` line 14; backbone `report.md` line 170.
- **Claim:** "And I just thank God," Freeman wrote, "that I didn't make the wrong decision twice."
- **Problem/evidence:** The backbone's verified text reads "And I just thank God that I didn't make the wrong decision twice" — no comma after "God." Splitting the quote around an attribution is conventional, but under a character-by-character quote standard the inserted comma is a punctuation alteration. The article (line 41) reproduces the sentence exactly.

### M-05 — Backbone executive summary misstates the career total as "47–12 through 2025"

- **Files/locations:** backbone `report.md` line 17 vs. line 118.
- **Claim:** "Career 47–12 through 2025 per the season table."
- **Problem/evidence:** The season table sums to 43–12 through 2025 (0–1 + 9–4 + 10–3 + 14–2 + 10–2); line 118 itself clarifies that 47–12 includes a 4–0 start in 2026 from the live table. The dossier and both derivatives correctly use 43–12 through 2025, so the defect is confined to the backbone's summary line and did not propagate.

### M-06 — Dossier §35 states the "I'm done" absence categorically; the ledger correctly scopes it as a record finding

- **Files/locations:** `dossier.md` line 493 (§35) and §27 Myth row 3; ledger CLAIM-044 at `dossier.md` §15; `gaps.md` Open Question 5.
- **Claim:** Freeman was "credited with an 'I'm done' quote that does not exist."
- **Problem/evidence:** A negative search finding supports "no such quote exists *in the record*" / "not found" — the ledger's own scoped wording ("No 2022 Ohio State 'I'm done' pregame quote by Freeman exists in the record," graded SUPPORTED) — not an unqualified metaphysical "does not exist." This audit's independent searches likewise located no 2022 quote and found only the January 2026 *College GameDay* line, so the correction is substantively right; §35's phrasing is stronger than the evidence form. §27's "Not found" framing is the correct register.

### M-07 — Three relationship edges are inferential rather than directly evidenced (structure itself is clean)

- **Files/locations:** `relationships.json` line 248 (rel-021, Notre Dame football `plays_home_games_at` Notre Dame Stadium, SUPPORTED); line 272 (rel-023, Freeman `based_in` South Bend from 2021, SUPPORTED); line 284 (rel-024, Freeman `from` Huber Heights with `date_from` 1986, SUPPORTED).
- **Claim:** That each CTL-E-1412 / Notre Dame edge is directly supported by its cited claim.
- **Problem/evidence:** The edges are plausible and honestly graded SUPPORTED, but their cited evidence does not directly prove the predicate as stated: CLAIM-026 evidences a CFP game played at Notre Dame Stadium, not a general home-stadium edge; CLAIM-015 (the December 2021 appointment) does not itself establish a South Bend professional base from January 2021; and rel-024 attaches Freeman's birth year (1986) as `date_from` to a hometown predicate whose claim (CLAIM-004) is about high-school attendance. No edge asserts a relationship the backbone contradicts, and all 28 endpoints resolve — this is graph hygiene, not a factual break.

---

## CLEAN checks

### C-01 — The five corrections independently re-verified against the live web

- **(a) Draft team — CORRECT.** Notre Dame's official Freeman bio and the Marcus Freeman reference record agree: drafted by the Chicago Bears, fifth round, 154th overall, 2009; waived September 4, 2009; Buffalo Bills practice squad September 22–October 5, 2009; Houston Texans practice squad from November 4, 2009; no regular-season NFL appearance. Buffalo was practice-squad only.
- **(b) Willingham first, Freeman second — CORRECT.** The January 20, 2025 *Beacon Journal* synthesis states Tyrone Willingham coached Notre Dame 2002–04 (21–15) as the program's first Black head coach, with Freeman second; it also supports Freeman as the second FBS head coach of Asian descent after Norm Chow. Notre Dame's official bio and the same January 2025 reporting support the bounded national first: first Black and first Asian American head coach to lead a team into an FBS national championship game.
- **(c) No 2022 Ohio State "I'm done" quote — CORRECT as a record finding.** Independent searches located no 2022 pregame "I'm done" quote. The only located line is the January 2026 *College GameDay* joke segment (On3's account quotes Freeman, after turning 40 and a Pat McAfee fight joke: "And I'm done. I retired. I'm retired."). See M-06 for the required scoped phrasing.
- **(d) 30th head coach — CORRECT.** Notre Dame's official bio states verbatim: "On December 3, 2021, Freeman was announced as the 30th head coach in school history," and gives the 43-12 (.782) record entering 2026. The 32nd count is a variant including interim/acting coaches, as the dossier says.
- **(e) Contract terms contested; buyout single-source — CORRECT.** Reporting continues to conflict on the original deal (six-year/~$42M guaranteed per FootballScoop/Irish Illustrated sourcing vs. five-year figures); Notre Dame has disclosed neither. The detailed salary/buyout table traces to a single SportsCasting page; no filing or second report behind that table was located in this audit, and independent salary coverage (USA TODAY via ND Insider) lists Freeman's buyout as unknown for a private university. The dossier's refusal to state original terms as fact is the right posture — subject to B-06, which faults §27 for printing the $70.8M figure inside a myth row.

### C-02 — Arithmetic, season records, CFP results, and key dates reconcile

Season records sum correctly: 0–1 + 9–4 + 10–3 + 14–2 + 10–2 = **43–12** through 2025 (.782 = 43/55), matching Notre Dame's official accounting. CFP results check: Indiana 27–17 (Dec 20, 2024), Georgia 23–10 (Sugar Bowl, Jan 2, 2025), Penn State 27–24 (Orange Bowl, Jan 9, 2025), Ohio State 34–23 (National Championship, Jan 20, 2025); 14 wins a program single-season record. Hiring dates check: announced December 3, 2021; introduced December 6, 2021; Fiesta Bowl January 1, 2022. Representation arithmetic checks: 13/136 = 9.56%; 7/69 ≈ 10%. (Exceptions: M-01, M-05.)

### C-03 — JSON validity and graph structure

Both JSON files parse (`python3 -m json.tool`). `entities.json` holds 30 entities (subject CTL-E-1412, Marcus Freeman; 16 further people, 9 organizations, 4 places). `relationships.json` holds 28 relationships (13 VERIFIED, 15 SUPPORTED), and every subject/object endpoint resolves to an entity ID present in `entities.json`. No relationship asserts a tie the backbone contradicts. (Hygiene exceptions: M-07.)

### C-04 — Visuals discipline

`visuals.md` contains 6 PHOTO NEEDED and 2 VIDEO NEEDED entries. No invented image URLs, file paths, embeds, video IDs, or credits were found; each entry states the rights/provenance that must be recorded at pull time, and AI-generated depictions are expressly rejected. No jersey number, photo credit, or image fact is asserted anywhere in the package.

### C-05 — Branding, voice, and 501(c)(3) neutrality

The dossier and both derivatives carry the CULTURETECHLENS header with "Culture, Clearly Seen." and the Black Cultural Intelligence descriptor, "Cite as" lines, the master citation, the nonprofit citation with EIN 39-3143901, and "Source: CultureTechLens." No AI byline or AI namecheck appears. A filler scan of the essay and article found zero instances of "delve," "moreover," "furthermore," "landscape," "tapestry," "testament," "underscores," "notably," "crucial," or "journey." Both derivatives close with the nonprofit no-endorsement statement ("does not endorse or oppose any candidate for office"), and no candidate endorsement or partisan framing appears.

### C-06 — Essay does not repeat DISPUTED or UNRESOLVED claims as fact

Checked specifically: the essay does not state Freeman's original contract terms (DISPUTED) as fact and gives no contract dollars; it does not adopt either side of the Dodd "misquoted" dispute (DISPUTED) — it does not mention it; it prints no buyout figure (UNRESOLVED); and it does not repeat the erroneous "first Black head coach" claim except to correct it. Its one PROVISIONAL item — Willingham as first Black head coach in any Notre Dame sport — is carried with the matching qualifier "by widespread account," as the dossier's grade requires. The essay's argument (demonstration/opportunity) stands on the verified *Players' Tribune* text and supported record claims. (The dossier's own Myth table is the exception to buyout discipline — see B-06; the essay itself is clean on this check.)

---

## Appendix A — VERIFIED-claim trace matrix (all 18)

Backbone flags: `(verified)` = page opened 2026-10-03; `(index)` = snippet tier. "Overgrade" = a bundled subclaim rests only on `(index)` sourcing (see B-02).

| Claim | Backbone basis | Audit result |
|---|---|---|
| CLAIM-001 Birth (Jan 10, 1986; Wright-Patterson AFB) | Report §1: Wikipedia `(verified)`; Notre Dame bio corroboration `(verified)` | Substantiated |
| CLAIM-004 Wayne HS / Parade All-American | Report §1: Wikipedia `(verified)`; FightingIrish.com `(verified)` | Substantiated |
| CLAIM-005 Ohio State B.S. 2007 / M.S. 2011 | Report §1: FightingIrish.com `(verified)` | Substantiated |
| CLAIM-006 Ohio State playing record (51 games, 268 tackles, 2× All-Big Ten) | Report §2: Wikipedia `(verified)`; FightingIrish.com `(verified)` | Substantiated |
| CLAIM-007 Chicago draft (5th/154th), waived Sep 4, 2009 | Report §2: Wikipedia/PFR `(verified)` | Substantiated |
| CLAIM-008 Practice squads; never played a regular-season NFL game | Stops `(verified)` (report §2); "never appeared" = "(Multiple sources, index)" | **Overgrade** (index subclaim) |
| CLAIM-009 Enlarged heart (Feb 2010); retired May 1, 2010 | Report §2: Wikipedia `(verified)` | Substantiated |
| CLAIM-010 Early ladder (OSU GA → Purdue co-DC) | Report §3 table: Wikipedia + Notre Dame bio, both `(verified)` | Substantiated |
| CLAIM-011 Cincinnati DC; Broyles finalist; 247Sports DC of Year | Report §3: Wikipedia + FightingIrish.com, both `(verified)` | Substantiated |
| CLAIM-012 Notre Dame DC hire Jan 8, 2021; 15th scoring defense; sack record | Report §3: FightingIrish.com `(verified)` | Substantiated |
| CLAIM-015 Announced Dec 3, 2021 (permanent); introduced Dec 6 | Dec 3 `(verified)` (FightingIrish.com); Dec 6 date `(index)` (report §4) | **Overgrade** (index subclaim) |
| CLAIM-016 Notre Dame's official "30th head coach" (32nd variant) | Report §4: FightingIrish.com `(verified)` vs. Wikipedia text `(verified)` | Substantiated |
| CLAIM-021 First Black + first Asian American head coach in an FBS title game | Report §5: Wikipedia 2024 season `(verified)`; CBS/AP framing partly via references/`(index)` | Substantiated; independently corroborated (Beacon Journal, Jan 20, 2025) |
| CLAIM-025 Season records 2021–2023 | Report §6 table: Wikipedia `(verified)`, cross-checked FightingIrish.com `(verified)` | Substantiated |
| CLAIM-026 2024 season 14–2; CFP run; AP No. 2 highest since 1993 | Record/games `(verified)`; "highest since 1993" = 247Sports `(index)` (report §6) | **Overgrade** (index subclaim) |
| CLAIM-027 2025 season 10–2; CFP No. 11 / AP No. 10; bowl withdrawal | Report §6: Wikipedia 2025 season `(verified)`; withdrawal via CBS reference | Substantiated |
| CLAIM-042 *Players' Tribune* passages; Dec 12, 2021 clarification | Letter text `(verified)` (report §13); clarification date `(index)` (report §10) | **Overgrade** (index subclaim) |
| CLAIM-055 NCMFC member; founded by Locksley in 2020 | Membership `(verified)` (Players' Tribune); "founded … in 2020" = AP `(index)` (report §9) | **Overgrade** (index subclaim) |

All other direct quotations sampled in the dossier and derivatives — the *Players' Tribune* demonstration passage (dossier §02; essay; article), the Bevacqua "top, top, top tier" / "living, breathing document" lines, the Mickens "ready to run his own defense" line, and Freeman's September 23, 2023 postgame lines — match the backbone's quoted passages verbatim. The exceptions are B-03 and M-04.

## Appendix B — Independent sources consulted for the five corrections

- Notre Dame Fighting Irish (official), "Marcus Freeman" staff bio — fightingirish.com (30th head coach; 43-12 entering 2026; draft and ladder record).
- Wikipedia, "Marcus Freeman" (Chicago Bears, 5th round, 154th overall, 2009; Buffalo practice squad Sept 22–Oct 5, 2009; Houston practice squad from Nov 4, 2009; no regular-season appearance).
- *Beacon Journal*, January 20, 2025 — Willingham (2002–04, 21–15) first Black head coach at Notre Dame; Freeman second; second FBS head coach of Asian descent after Norm Chow; first Black/Asian American head coach in an FBS title game.
- On3, January 2026 — *College GameDay* segment account quoting Freeman's "I'm done. I retired." joke line; no 2022 Ohio State "I'm done" quote located in any searched source.
- SportsCasting, "Marcus Freeman Salary, Contract, Buyout" — the single detailed buyout table; contrasted with USA TODAY/ND Insider salary coverage listing the buyout as unknown, and with conflicting six-year/~$42M vs. five-year reporting on the original deal (247Sports/FootballScoop/Irish Illustrated chain).

---

## Required before publication (fix list — findings only; drafts not rewritten here)

1. Repoint every narrative CLAIM reference in dossier §§03, 09–12 to the ledger claim that actually carries the statement (B-01).
2. Downgrade or split the five bundled VERIFIED claims so no VERIFIED grade rests on an `(index)` subclaim, or open the underlying pages to `(verified)` tier (B-02).
3. Restore the January 9, 2025 quotation to its backbone sequence in the essay (B-03).
4. Correct the 0–3 framing to Freeman's tenure start across the Fiesta Bowl and the first two 2022 games (B-04; check dossier §07 line 119 as well).
5. Remove the unsupported "misdemeanor" classification from the article's allegation sentence (B-05).
6. Remove the $70.8M figure from dossier §27 so the package's "not printed" rule holds everywhere (B-06).
7. Fix the publication cutoff framing and reconcile the article's through-2030 close with its reported through-2031 restructure (S-01); align dossier §35's firsts to CLAIM-022's wording (S-02); transcribe the Pivot passage before any print use or drop the paraphrase (S-03).
8. Sweep the MINOR items (M-01–M-07) in the same pass.

**Final verdict: publishable with fixes.** The corrections and the core record are sound; the package's failures are in traceability mechanics, quote handling, and three localized factual/legal wordings. None requires new reporting except the optional `(verified)`-tier upgrades in item 2. Until items 1–6 are fixed, the dossier should not be cited as a verified-grade authority and neither derivative should be published.

*Red-team pass prepared for CultureTechLens internal review. Source of record: CTL-RD-PER-000002 · CTL-EF-PER-000002 · backbone `report.md` (2026-10-03).*

---

## Corrections applied 2026-10-03 (red-team pass)

Correction pass executed 2026-10-03. Each finding below gives its resolution. Ledger after the pass: 61 claims — VERIFIED 18 · SUPPORTED 33 · PROVISIONAL 6 · DISPUTED 3 · UNRESOLVED 1. `entities.json` and `relationships.json` re-validated with `python3 -m json.tool`; edges unchanged at 28 (13 VERIFIED · 15 SUPPORTED).

### BLOCKER

**B-01 RESOLVED — Narrative pointers re-aligned.** Dossier §§03, 09–12 claim references were corrected across ~30 pointers (all off-by-one drift fixed, including §12's Tribune/Dodd/10-men pointers and §07's letter pointer). Verified after the pass: every CLAIM reference in the dossier resolves to an existing ledger ID.

**B-02 RESOLVED — Bundled claims split.** The five bundled claims (008, 015, 026, 042, 055) were split into a/b subclaims in the ledger, `evidence-file.md`, `entities.json`, and `relationships.json`, so no VERIFIED grade rests on `(index)` sourcing. The `(verified)` cores (practice-squad stops; Dec 3 announcement; 2024 record and game results; the *Tribune* text; NCMFC membership) retain VERIFIED as the a-claims; the `(index)` portions (no regular-season appearance; Dec 6 introduction; AP No. 2 "highest since 1993"; Dec 12 clarification; 2020 founding) now grade SUPPORTED as the b-claims. VERIFIED count unchanged at 18; SUPPORTED rose to 33. The §05 dates table was also corrected: the December 6 introduction now grades SUPPORTED.

**B-03 RESOLVED — Quote sequence restored.** The essay now quotes the January 9, 2025 statement in the backbone's order and exact words ("It is an honor, and I hope all coaches, minorities, Black, Asian, white, it doesn't matter, great people continue to get opportunities to lead young men like this. But this ain't about me. This is about us."), introduced as "he put the opportunity first and himself second."

**B-04 RESOLVED — 0–3 framing corrected.** Essay: "His first three games as a head coach were losses — the Fiesta Bowl, then Ohio State and Marshall to open the 2022 season." Dossier §07: the tenure start (Fiesta Bowl plus the first two 2022 games) is now distinguished from the 2022 team's own 0–2 start.

**B-05 RESOLVED — "Misdemeanor" removed.** Article now says "a battery allegation"; the prosecutor's declination language (no criminal battery occurred; no charges filed, January 12, 2026) stands as the only characterization, matching CLAIM-053.

**B-06 RESOLVED — Buyout figure struck.** The single-source figure was removed from dossier §27 (row 7 now reads "Single-source figure, not printed" and withholds the number) and from the figure's second appearance in `evidence-file.md` (CLAIM-034 evidence), so the dossier's "not printed" rule now holds everywhere in the package.

### SERIOUS

**S-01 RESOLVED — Cutoff fixed and applied.** Package cutoff fixed at **the close of the 2025 season, with the January 12, 2026 prosecutor's declination as the final in-scope event** (recorded in dossier §28 Open Question 10 and `gaps.md`). Derivatives aligned: essay closing reads "43–12 through the 2025 season"; the article's "Sources and grading" preamble states the cutoff, and its closing reconciles the December 2024 extension through 2030 with the later reported 2025 restructure through 2031 in reported language.

**S-02 RESOLVED — §35 firsts pulled back to CLAIM-022.** Section 35 now reads "second FBS head coach of Asian descent after Norm Chow and the first Asian American head coach at Notre Dame" — no "first of Korean descent anywhere" superlative, no "in any capacity" broadening. The §27 myth table and the title-game first (CLAIM-021) were confirmed bounded throughout.

**S-03 RESOLVED — Pivot paraphrase dropped.** The essay's compressed Pivot Podcast paraphrase was replaced with language drawn verbatim from the verified *Players' Tribune* standard (opportunity to interview; opportunity to do a job a coach can succeed in). The transcription requirement now stands recorded in `gaps.md` as un-exercised; no derivative relies on the Pivot passage.

### MINOR

**M-01 RESOLVED** — Article: Buffalo stint now "September 22 to October 5, 2009" (matching CLAIM-008a).
**M-02 RESOLVED** — Article: "every coordinator he has employed — Tommy Rees (retained from Brian Kelly's staff), …".
**M-03 RESOLVED** — Article correction bullet now uses the bounded wording: "first Black and first Asian American head coach to lead a team into an FBS national championship game."
**M-04 RESOLVED** — Essay quote punctuation restored to the verified text (the inserted comma around "thank God" removed).
**M-05 NOTED, NOT EDITED** — The backbone's executive-summary "47–12 through 2025" line sits in `report.md` outside the dossier package and was not altered here; the dossier and both derivatives already use the correct 43–12 accounting. Flagged for the backbone's owner.
**M-06 RESOLVED** — Dossier §35 now reads "an 'I'm done' quote that does not exist in the record," matching CLAIM-044's scoped wording.
**M-07 RESOLVED (hygiene)** — `relationships.json` rel-024 `date_from` (1986) removed; edge predicates otherwise unchanged. Edges still 28 (13 VERIFIED · 15 SUPPORTED); all endpoints still resolve.

### Post-pass verdict

All six BLOCKER, all three SERIOUS, and six of seven MINOR findings are resolved in text; M-05 is a backbone-summary note that does not propagate into the package. The five headline corrections remain intact, no DISPUTED or UNRESOLVED claim is presented as fact in either derivative, no single-source figure appears anywhere in the package, and both JSONs parse. **The package is now publishable on its evidence discipline; publication itself remains William's call.**
