# CTL-DR-BPM-003 — Red-Team Review (Final)

**Research ID:** CTL-DR-BPM-003
**Status:** Final red-team report, 2026-09-28.
**Method:** Independent adversarial review of the five research tracks (A–E), with three targeted verification searches to adjudicate cross-track contradictions. Checklist: institutional bias, missing women, working-class readers/labor, date/circulation disputes, weak source chains, duplicate/inconsistent entities, famous-person bias, geographic bias, survivorship bias, decline-causation overreach, copyright/rights, unsupported "Verified" claims.

**Applied to the final data package:** the resolutions below were applied to `entities.json` and `timeline.json`:
- Defender daily→weekly **2008** (E&P contemporary report; Wikipedia's "2003" is wrong) — corrected.
- Real Times sale: **approved Nov 4, 2002; control transferred Jan 2003** — consolidated.
- Pittsburgh Courier purchase: **1965** (relaunched 1967 as New Pittsburgh Courier) — standardized; timeline event added.
- JPC HQ sale: **sold late 2010; transaction closed January 2011** — standardized.
- Jet final print issue: **June 2014** (announced May 7, 2014) — standardized.
- R.R. Donnelley printed Ebony/Jet; **~$12M mortgage against JPC HQ (2009)** over unpaid bills — added to `co-jpc` as Provisional.
- **WJPC radio** (JPC bought WGRT May 1973, $1.8M; first Black-owned Chicago radio; sold Dec 1994) — new entity + timeline event.
- **Charlotte L. Lyons** (Ebony food editor, Test Kitchen operator) — new entity; **Doris E. Saunders** (JPC books editor) — new entity (Provisional); Fay M. Jackson's **ANP Hollywood correspondent** role added (Provisional).
- Bee political orientation: sources contradict — softened to **Disputed** in `pub-bee`.
- "First Black paper over 100,000 circulation" — standardized to **Verified** (Track E sourcing) with archival-survival caveat.
- Bob Johnson death (1995 vs 1996), Alice Dunnigan death day (May 3 vs May 6), Whip 1932–39 tail, Broad Ax 1931 thinness — uncertainty notes added.
- Track D's over-graded Bee/ANP dates (Bee 1925/1947, ANP 1967) were already **Disputed** in the final entities; no downgrade needed.

---

## 1. Institutional bias: does the Defender swallow the story?

**Finding: Partially — volume is Defender-heavy, but the skew is acknowledged in some tracks and not others.**

- Track A is roughly twice the length of any other track and the Defender reappears as the gravitational center of tracks D (Abbott, Sengstacke, Payne, Brooks, Burley, Jay Jackson, Lochard, Harper, Bobby Sengstacke) and E (buildings, presses, digitization). The Whip, Bee, Conservator, and Broad Ax get genuine substantive treatment in Track B, and JPC gets its own track — so the *structure* resists Defender-monopoly. But word-count reality: a reader of the combined files will absorb far more Defender texture (cartoons, columns, buildings, parade) than Whip/Bee texture (no cultural-production detail — no Whip or Bee columnists, cartoonists, or signature features are named anywhere).
- The "ideological triangle" framing in Track B's lead notes (Defender = militant-mass; Whip = employment-boycott militancy; Bee = middle-class respectability) is the right corrective, but it rests partly on a **disputed** premise — the Bee's political orientation is internally contradictory in the sources (see §4, item z). If the Bee's orientation can't be fixed, the triangle wobbles.
- **Recommendation:** (a) add a one-paragraph "archival-survival caveat" to Track A's top, mirroring Track B's excellent lead note ("the record is thinnest where the archives are gone, not where the history was small"); (b) commission one more pass on Whip/Bee cultural content (columnists, cartoons, women's pages) before any public narrative locks in Defender-as-synonym-for-Black-press.

## 2. Missing women journalists/photographers

**Finding: The tracks are unusually self-aware here (Track D flags gaps explicitly), but real absences remain.**

- Present and well-documented: Ida B. Wells-Barnett, Olive M. Diggs, Ethel Payne, Alice Dunnigan, Era Bell Thompson, Hazel B. Garland, Jackie Ormes, Dorothy Leavell, Hermene Hartman, Etta Moten Barnett, Gwendolyn Brooks, Katherine E. Williams-Irvin.
- **Explicitly flagged as gaps by Track D (good):** no verifiable women staff photographers at any publication (major gap); Marian Campfield (Defender women's page editor — name only, no biography); Margaret Burroughs's specific Defender role unresolved.
- **Absent and should be present:**
  - **Charlotte L. Lyons**, Ebony food editor ("A Date with a Dish") and operator of the Ebony Test Kitchen — surfaced in my verification search (WBEZ, 2018), absent from all five tracks.
  - **Fay M. Jackson**, ANP Hollywood correspondent (covered George VI's coronation, 1937) — named in Track B's entities but missing from Track D's people track.
  - **Doris E. Saunders**, JPC books division editor — not researched anywhere.
  - Women in business/operations roles (e.g., Myrtle Sengstacke; JPC's female executives besides Linda Johnson Rice and Desirée Rogers); women typesetters, clerks, ad-sales staff.
  - Women vendors, subscription agents, and readers as economic actors (see §3).
- **Recommendation:** prioritize the Defender photo morgue (Abbott-Sengstacke Papers, CPL) and JPC archive staff lists for women photographers; add Lyons and Fay M. Jackson to the entity tables.

## 3. Missing working-class press and everyday-life coverage

**Finding: Distribution is covered better than labor; readers appear as multipliers, not people.**

- **Covered well:** Pullman porter network (all tracks, multiple sources); Abbott's door-to-door selling; the 4–5 readers-per-copy multiplier; newsboys (Track E, provisional; Bud Billiken's origin honoring delivery boys per Michaeli).
- **Missing:**
  - **Labor inside the plants:** compositors, pressmen, mailers, wages, working conditions, strikes. Track A's "first Black paper to unionize" is single-sourced (In These Times review) and sits unexamined next to Abbott's documented anti-union history and the Bee/Defender flip on the Brotherhood of Sleeping Car Porters (Track B). The tension between Abbott's nine goals ("open all trade unions") and his labor practices is never addressed.
  - **The Defender/JPC as employers:** headcounts exist (68 staff in 1921, per Michaeli second-hand) but no workforce history.
  - **Subscription agents and Southern stringers:** the porter network's economics (were porters paid? commissions?) are asserted, not evidenced — Track A grades the mechanics "Provisional (single popular source)" and that's correct; don't let it harden.
  - **JPC's printers:** Track E correctly refuses to claim JPC owned a plant; my search found R.R. Donnelley printed Ebony/Jet and took a ~$12M mortgage against JPC HQ in 2009 over unpaid printing bills — a material decline-narrative fact missing from all tracks.
  - **Readers' letters, classifieds, church/barbershop economics** — the everyday-life texture of the papers' pages is absent; all tracks treat papers as institutions, not as reading experiences.
- **Recommendation:** add a labor/workforce section to the next research pass; treat the R.R. Donnelley debt as a required addition to the decline narrative.

## 4. Disputed dates and figures — consolidated

**Resolved by this review (new evidence):**
- **a. Defender daily→weekly: RESOLVED as 2008.** Track A leaned 2008; Track E graded "2003" as Verified (Wikipedia). My check found E&P's contemporary report "'Chicago Defender' Going Weekly" (Mark Fitzgerald, Feb 2008): the paper moved to Wednesday weekly publication on **Feb. 13, 2008**, after cutting from five-day to four-day frequency ~2006. Smithsonian (2019) and ndinsider (2019) corroborate "weekly since 2008." Wikipedia's "until 2003" is **wrong**. → Track E's claim should be corrected, not merely disputed. Track A's lean is confirmed.
- **b. Real Times sale 2002 vs 2003: RESOLVED — not a real dispute.** E&P: probate court approved the sale Nov 4, 2002; control transferred January 2003. Both dates are true of different milestones. → Consolidate to "approved Nov 2002; completed Jan 2003" in all tracks.
- **c. Pittsburgh Courier purchase: lean 1965 (correct Track D).** Track A says 1965; Track D says 1966/1967. My check: Wikipedia's Pittsburgh Courier infobox lists Sengstacke as owner **1965–1966**, final issue Oct 22, 1966, reopened 1967 as New Pittsburgh Courier; the New Pittsburgh Courier article says "purchased… in 1965." The 1966 date comes from Sengstacke-biography sources (aaregistry, Wikipedia Sengstacke). → Recommend standardizing on **acquired 1965; relaunched 1967**, with a note that Sengstacke-bio sources say 1966.
- **d. JPC HQ sale to Columbia College: RESOLVED as a 2010–2011 transaction.** Track C says 2010; Track E says Jan 2011 (Provisional). My check: Columbia's own site says "acquired by Columbia in 2011" but "vacant since 2010"; REJournals, GlobeSt, CoStar say 2010; Wikipedia says January 2011. → Standardize: "sold late 2010; transaction closed January 2011."

**Confirmed disputes (unresolved — see track-f-gaps.md for research paths):**
- **e. Abbott birth:** Nov 24, 1868 (Georgia Encyclopedia, Britannica, Coastal Georgia guide, Chicago Literary HoF) vs Dec 24, 1870 (Wikipedia, BlackPast). All tracks flag; none resolve. Note Track D's claim "most institutional sources favor 1868" is fair but not dispositive.
- **f. Defender founding:** May 5, 1905 (IL House Resolution, Britannica, Smithsonian, Defender's own history) vs May 6 (BlackPast Tolly). Lean May 5; Track D grades May 5 Verified without noting BlackPast's dissent — add the note.
- **g. Bee founding 1925 vs 1926; end 1946 vs 1947.** Track B/E: Disputed. Track D grades "founded 1925" and "folded 1947" as **Verified** — inconsistent with B/E. → Downgrade both to Disputed (see §12).
- **h. ANP launch:** March 2, 1919 (Wikipedia) vs March 21, 1919 (Zinn). Needs charter document (Barnett papers, CHM).
- **i. ANP closure:** 1964 (Wikipedia) vs operating until Barnett's 1967 death (AA Registry). Track B: Disputed (lean: wound down 1964–67). Track D grades "ceased upon his death in 1967" as **Verified** — inconsistent. → Downgrade to Disputed (see §12).
- **j. Jet's Till issue:** Sept 15, 1955 (LOC Civil Rights History Project, Metress/NYT, TMJ4) vs Sept 22, 1955 (Wikipedia Jet). Lean Sept 15 — better attested and matches the funeral timeline. Track C already leans correctly.
- **k. Era Bell Thompson birth:** 1905 (ND governor, JBHE, AA Registry) vs 1906 (mic.com). Lean 1905.
- **l. Half-Century Magazine end:** 1925 (Rooks, Rutgers UP, peer-reviewed) vs 1947 (Wikipedia Bee article). Lean 1925.
- **m. 3435 S. Indiana tenure:** 1920–1956 (E&P/AP: move at daily conversion) vs 1920–1960 (Chicago Landmark record). Possibly the building was retained after the move; needs city directories or masthead imprints.
- **n. Whip run:** 1919–1939 claimed (Wikipedia) vs digitized 1919–1931 only (Chronicling America/IDNC, 177 issues). The 1932–39 tail is undocumented — do not assert 1939 without holdings evidence.
- **o. Broad Ax end:** 1931 (Taylor's Defender obituary) vs last surviving issue Sept 10, 1927. Lean 1931, thin.
- **p. Jet final print:** Track C "print ended June 2014 (announced May 7, 2014)" vs Track E "ended print May 2014… switching to digital in June 2014." Standardize: final print issue June 2014, announced May 7, 2014.
- **q. Tri-State Defender city:** Memphis (Wikipedia, 2004 Congressional Record, Wikipedia Sengstacke infobox) vs Nashville (HistoryMakers Palmer finding aid). Lean Memphis; treat "Nashville" as a finding-aid error.
- **r. Gary Crusader:** 1941 (Rep. Davis, 2015 Congressional Record) vs 1961 (Rep. Mrvan, 2023 Congressional Record). Lean 1961; note that the Congressional Record contradicts itself.
- **s. Bob Johnson (Jet editor) death:** Dec 27, 1995 (Track D, via Congress.gov) vs "1922–1996" (Track C entity table). Flag and verify.
- **t. Bee political orientation:** "middle-class, conservative, Republican-aligned" vs "known for its support of liberal causes" — adjacent sentences in the same Wikipedia article. This underpins Track B's "ideological triangle"; it needs primary-issue evidence before any public claim.
- **u. "Peaking at 9 million subscribers"** (Wikipedia, John H. Johnson): Track C correctly flags as irreconcilable with all other figures (Ebony ~2.3M peak; Jet ~1M). Treat as erroneous unless a primary source appears.
- **v. Lu Palmer's PhD:** Wikipedia/HistoryMakers say PhD (Iowa, 1950); Congressional Record says coursework only, no dissertation. Track D handles correctly — do not assert.
- **w. Alice Dunnigan death day:** May 3 vs May 6, 1983 (1983 certain). Minor.

## 5. Weak sources: Verified claims on thin chains → recommended downgrades

| Claim (track) | Current | Problem | Recommended |
|---|---|---|---|
| Defender "did not use the words 'Negro' or 'black'" (A) | Verified | Single source (BlackPast) | **Provisional** |
| Princess Mysteria columnist 1920–1930 (A) | Verified | Single source (Wikipedia) | **Provisional** |
| Bud Billiken Parade "largest African-American parade in the U.S." (A) | Verified | Promotional superlative (Wikipedia/encyclopedia of holidays) | **Provisional** |
| ANP "ceased operating upon Barnett's death in 1967" (D) | Verified | Contradicted: 1964 claim documented in Track B | **Disputed** |
| Bee "founded 1925" (D) | Verified | Track B/E document 1925/1926 dispute | **Disputed** |
| Bee "folded in 1947" (D) | Verified | Track B documents 1946/1947 dispute | **Disputed** |
| Defender "returned to weekly in 2003" (E) | Verified | Disproved by E&P's Feb 2008 contemporary report | **Incorrect → correct to 2008** |
| "Gentry coined 'Bronzeville' / Bee's Mayor of Bronzeville originated the nickname" (B) | Verified | Single citation chain (Wikipedia→scholarship, uninspected); major cultural claim | **Provisional** |
| Bee staff "predominantly female" (B) | Verified | Single chain; keep Olive Diggs herself Verified (finding aid) | **Provisional** (Diggs stays Verified) |
| Chicago World "~40,000 circulation" (B) | Verified | Single source | **Provisional** |
| "First Black paper to reach 100,000 circulation" (A: Provisional; E: Verified) | Inconsistent | E's chain (UW-Madison/ProQuest, Congressional Record context) is stronger | **Standardize to Verified** with E's sourcing |
| Bud Billiken Club founded 1923 by Abbott + Lucius Harper (D: Provisional; A: Verified via Chicago History Museum) | Inconsistent | CHM is institutional | **Standardize to Verified** |
| "JFK would have lost in 1960 without the Defender's support" (A, via Michaeli dust jacket) | Provisional | Publisher marketing copy; causal claim implausible as stated | **Disputed** |
| Johnson "first African American on Forbes 400 (1982)" (C) | Provisional | Widely repeated; Forbes list not checked | Keep Provisional (correct) |

## 6. Duplicated entities with inconsistent details

- **Ben Burns** (A: Defender's first white editor, WWII "Victory Through Unity" edition; C: founding editor of Negro Digest/Ebony/Jet 1942–54, fired 1954): consistent and complementary — keep as a deliberate cross-track bridge, but note the Medill claim ("only white journalist working in black media") sits uneasily beside other white staffers; don't overstate.
- **Langston Hughes** (Defender columnist per A; ANP contributing columnist per B): consistent; no conflict.
- **Pittsburgh Courier acquisition year** (1965 A vs 1966 D): resolved in §4c — standardize 1965.
- **Moneta Sleet Jr.** (C and D): consistent (1926–1996; JPC 1955–1996; 1969 Pulitzer).
- **Ethel Payne** (A: 1951–1978, DC bureau 1953–1973; D: joined 1951, CBS 1972): consistent.
- **Era Bell Thompson dates** (C: co-managing 1951–64; D: 1951–1964 per ND governor vs 1941–1964 per AA Registry): minor; standardize on ND governor (official).
- **JPC HQ chronology** (C: moved Dec 1971; E: dedicated May 16, 1972): consistent (move-in vs dedication).
- **Robert "Bob" Johnson death year** (C: 1922–1996; D: d. Dec 27, 1995): flag — verify against the Congressional Record tribute D cites.
- **Defender founding date** (A documents May 5/May 6 dispute; D asserts May 5 without noting dissent): add the footnote in D.
- **Chicago Conservator "first" vs "oldest"**: B grades "Chicago's first Black newspaper (1878)" Verified (Wikipedia citing scholarship); D grades the same claim Provisional (nrawomen.com, unconfirmed). → Align grades and inspect the underlying citation (Walker 1996) before locking either.

## 7. Famous-person bias

**Finding: Better than expected — but the floor is thin.**

- Credit: tracks name working journalists, not just icons — Vernon Jarrett, Lu Palmer, Louis E. Martin, Bob Johnson, Lerone Bennett, Moneta Sleet, David Jackson, Dan Burley, Jay Jackson, Metz Lochard, Lucius Harper, Le Mont Mac Lemore, Billy Abernathy, Olive Diggs, Dorothy Leavell, Hermene Hartman. Track D's method note explicitly sought this.
- Gaps: (a) several are single-mention names with no career texture (Mac Lemore, Abernathy, Fay M. Jackson); (b) **no rank-and-file workers at all** — compositors, pressmen, mailroom, ad sales, circulation staff, secretaries; (c) **JPC's broadcast arm is entirely missing**: JPC bought WGRT in May 1973 ($1.8M), renamed it WJPC — the first Black-owned radio station in Chicago — operating until Dec 1994 (found in verification search; absent from tracks C and E). For a project on "media infrastructure," omitting the company's radio station is a significant hole. (d) The Defender's daily-era newsroom (1956–2008) has no staff history beyond editors.
- **Recommendation:** add WJPC to Track C/E entities and timelines; commission a workforce/labor pass (see §3).

## 8. Geographic bias

**Finding: Chicago-centrism is the brief, but the chain papers are names without histories.**

- ANP's national/Pan-African scope is handled appropriately in Track B (150 U.S. papers, ~100 African papers, correspondents in Africa/London/Caribbean, World News Service/OAU). Good.
- **Thin:** Michigan Chronicle (Detroit), Tri-State Defender (Memphis), New Pittsburgh Courier — appear only as chain-membership facts. The Courier gets indirect depth via Garland/Ormes/Harrington in Track D, but Detroit and Memphis get nothing: no editors, no circulation, no editorial lines.
- **One-directional:** the Defender's Chicago→nation projection is well covered (porters, migration); the nation→Chicago flow (Southern correspondents, stringers, syndicated content from other Black papers) is not.
- **Recommendation:** acceptable for a Chicago-rooted project, but flag in public outputs that the Sengstacke chain's non-Chicago papers are under-researched here; add at minimum founding editors and lifespans for the Chronicle and Tri-State.

## 9. Survivorship bias

**Finding: Track B names the problem; the other tracks don't apply the lesson.**

- Track B's lead note is exemplary: "The record is thinnest where the archives are gone, not where the history was small" (Bee's 1925–35 run lost; Whip's 1932–39 tail undigitized; Broad Ax's 1927–31 tail surviving only as an obituary claim). This caveat must be project-wide.
- **Lost evidence treated as settled history:** Track A's "firsts" (first Black paper over 100,000 circulation; first to own its printing plant; first health column; first to unionize) are claims about a field whose competitors' records are largely destroyed. "First verifiable" ≠ "first." Recommend qualifying all "first" claims with the archival-survival caveat.
- **Fabrication flagged well:** Track B's exposure of oldnews.com's "Whip founded 1933 by John H. Johnson" (Johnson was born 1918) is exactly the kind of corrupted-web-memory check CTL should systematize.
- **Recommendation:** add a standing "archival survival" disclaimer to every comparative claim; qualify "firsts."

## 10. Misleading causal claims

- **The Defender "caused" the Great Migration.** Tracks present Abbott's campaign (Great Northern Drive, May 15, 1917; job listings; train schedules) alongside the 110,000-migration figure (1916–18) in ways readers will read as causation. Scholarship (Grossman, *Land of Hope*) treats wartime labor demand, boll weevil, and floods as primary drivers and the Defender as a major accelerant/information channel. → Distinguish catalyst from cause in public outputs.
- **"Integration killed the Black press."** Track B's lead note ("the ANP's collapse coincided with the mainstream press finally covering Black news and hiring Black journalists — a direct 'integration killed the institution' arc") and Track E's CJR quote ("a casualty of the integration it had long championed") present Horne's thesis as settled. Counter-causes documented in the tracks themselves: ad-market discrimination, debt and mismanagement (JPC's R.R. Donnelley arrears/mortgage), the Defender's estate-tax forced sale, changing media economics. → Present integration as one evidenced cause among several; distinguish Horne's argument from consensus.
- **"The Defender's support elected Truman and JFK"** (Michaeli dust jacket, Track A Provisional): marketing copy, not evidence. → Disputed (see §5).
- **2019 digital-only move** attributed to "declining print advertising + readers shifting to digital": this is Real Times CEO Hiram Jackson's stated reason, properly attributable — keep with attribution.
- **Whip's "Don't Spend" campaign → 15,000+ jobs:** Track B correctly grades Provisional (WTTW via Wikipedia, thinly sourced). Keep; needs primary evidence.
- **"World's Greatest Weekly" borrowed from the Chicago Tribune** (A, Provisional, single source): colorful, keep provisional.

## 11. Copyright / rights concerns

- **JPC photo archive (~4M images): joint ownership by Smithsonian NMAAHC and the J. Paul Getty Trust** (consortium purchase July 2019 for $30M by Ford, Getty Trust, MacArthur, Mellon + Smithsonian; formal joint transfer reported 2025; Getty committing an additional $30M for digitization; public availability target ~2029 per Track C). **Implications for CTL: nothing in this archive is free to reuse.** Licensing must go through NMAAHC/Getty; commercial vs. editorial terms are TBD pending digitization. Underlying photographer rights add complexity (e.g., Gordon Parks was freelance, not staff — Track C correctly flags this; freelancer images may carry separate rights). **Top rights concern: do not publish, scrape, or assume fair use over JPC archive images.**
- **Defender issues:** ProQuest's 1909–2010 run is **subscription access, not a rights grant**. Copyright holder for the paper's content is Real Times Media (successor owner). U.S. rule of thumb: issues **before 1929 are public domain** (as of Sept 2026, through 1930; 1931 issues enter PD Jan 1, 2027); 1929–1963 issues need copyright-renewal checks; post-1963 issues are almost certainly still in copyright. CTL can freely reuse pre-1929 scans; everything later needs Real Times permission or a renewal analysis.
- **Whip (Chronicling America, 1919–1931):** 1919–1930 issues are public domain and LOC scans are free to reuse; 1931 issues PD Jan 2027.
- **Bee:** almost no surviving issues — rights are moot for lost material (orphan-work risk for the 12 surviving 1938–46 UIUC issues; rights holder unclear, likely the Overton estate or successor).
- **Abbott-Sengstacke Family Papers (CPL):** donation ≠ copyright transfer. E&P reports the donor kept the archive in Chicago after a Smithsonian purchase offer — but physical custody does not convey publication rights. CTL must clear rights with the rights holder (likely the Sengstacke family/estate) before publishing photos or documents, even though access is open to patrons.
- **Harsh Collection digitization (Mellon $2M, 2024, 300,000 pieces):** digitization ≠ rights clearance. Check CPL's rights statements per item.
- **HistoryMakers oral histories** (Jarrett, Palmer, Bobby Sengstacke, Johnson, Etta Moten Barnett): rights held by The HistoryMakers — permission required for clips/transcripts.
- **CHM's on-site-only Defender database:** access restriction plus underlying ProQuest/Real Times rights — no republication.
- **Getty Images photos** used as building references: licensed stock, not free.
- **Safe:** Congressional Record (public domain), municipal landmark reports (public records), Chronicling America pre-1929 scans, pre-1929 newspaper issues generally.
- **Recommendation:** build a rights matrix per collection before any public-facing use; open a licensing conversation with NMAAHC/Getty for the JPC archive and with Real Times Media for Defender content; treat the JPC archive as the critical path (public access target 2029).

## 12. Unsupported claims graded Verified (summary)

Consolidated from §§4–5: (1) ANP ceased 1967 (D) → Disputed; (2) Bee founded 1925 / folded 1947 (D) → Disputed; (3) Defender style rule on "Negro"/"black" (A) → Provisional; (4) Princess Mysteria (A) → Provisional; (5) "largest African-American parade" (A) → Provisional; (6) Defender weekly reversion 2003 (E) → incorrect, correct to 2008; (7) "Bronzeville" coinage / Mayor of Bronzeville genesis (B) → Provisional; (8) Bee staff "predominantly female" (B) → Provisional; (9) Chicago World 40,000 circulation (B) → Provisional; (10) JFK-1960 causal claim (A) → Disputed. Grade-alignment fixes: "first Black paper over 100,000" → Verified (E's sourcing); Bud Billiken founders → Verified (CHM); Real Times sale → consolidate (Nov 2002 approval / Jan 2003 transfer); Pittsburgh Courier purchase → 1965; JPC HQ sale → late 2010/Jan 2011; Jet final print → June 2014 issue.

---

## Red-team notes on track quality (for the parent)

- Track B is the strongest: disputes are explicit, weak sources are flagged (including a fabricated source, oldnews.com), and the lead notes show historiographical awareness. Use it as the grading model.
- Track A is the most thorough but the most credulous: several single-source claims sit at Verified, and marketing copy (Michaeli dust jacket) is treated gently.
- Track D did the most honest gap-flagging (women photographers, Campfield, Burroughs, DeCarava exclusion, Marvel Cooke exclusion) — that discipline should be copied everywhere.
- Track C's Gordon Parks correction (freelancer, not staff) is exactly right and prevents a common error.
- Track E's refusal to claim JPC owned a printing plant ("Do NOT claim") is exemplary negative-space documentation; more of this is needed (e.g., Defender–ANP relationship, Defender's daily-era printers).
