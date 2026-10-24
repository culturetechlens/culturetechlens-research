# Preservation Priority Framework
### CTL-DR-PRESERVE-001 — "The Black Memory Emergency" · Synthesis deliverable (promoted from the framework track)
**CULTURETECHLENS** · *Culture, Clearly Seen.* · Black Cultural Intelligence
Version 1.0 — 2026-09-28

---

## 1. Purpose

Black cultural memory is disappearing faster than it can be saved: newspapers folding, founders dying, tapes degrading, buildings burning, servers lapsing. Preservation resources — money, archivist hours, cold storage, grant attention — are scarce. This framework answers one question, transparently:

> **Given scarcity, which at-risk Black collections should preservation action reach first?**

It is a **triage tool**, not a canon. Every rating must be reproducible by an independent reader from public evidence. There is no black-box score, no weighted index, no intuition. Four observable factors, each with defined levels, combine through an explicit ordered rule set. If you disagree with a tier, you can point to the exact factor rating and rule you dispute — that is the design working as intended.

**Privacy constraint (standing CTL rule):** location is recorded at city/institution granularity only. Private collection addresses are never published in framework outputs.

---

## 2. The four factors

### Factor 1 — RISK SEVERITY
*How imminent and irreversible is the threat?* Rate the **worst credible, documented threat**, not a hypothetical one.

| Level | Observable criteria (any one suffices) |
|---|---|
| **Critical** | Loss mechanism already triggered or scheduled within ~12 months: demolition permit issued; auction date set; eviction or foreclosure in motion; domain/hosting expiring with no renewal plan; active water, mold, fire, or pest damage; nitrate film actively decomposing; custodian deceased with heirs dispersing the material; format unreadable and no working playback equipment exists. |
| **High** | Credible threat within ~1–3 years: building vacant or for sale; organization insolvent or founder-dependent with founder incapacitated/deceased; format obsolescence with no migration plan (e.g., magnetic tape >20 years old in uncontrolled storage); operating reserves under 12 months with no pipeline; single point of failure with a known departure (retiring archivist, sunsetting platform). |
| **Moderate** | No active threat, but fragile custody: volunteer-run with no succession plan; no climate control; uncataloged (loss would be invisible); one copy in one place; platform-dependent digital presence (social media, proprietary site) with no backup. |
| **Low** | Stable institutional custody: climate-controlled storage, cataloged/finding aid, backup or duplication in place, succession plan or endowed position, line-item preservation budget. |

### Factor 2 — HISTORICAL SIGNIFICANCE
*The collection's documented importance.* Significance must be **evidenced**, not asserted. Any of the listed evidence qualifies the level.

| Level | Observable criteria |
|---|---|
| **Exceptional** | National recognition (National Register/National Historic Landmark tie, National Film Registry, major national award) **or** sole documentation of a nationally significant movement, event, or person **or** sustained scholarly corpus (cited across 20+ publications and/or major exhibitions) **or** demonstrated public use at national scale (1M+ annual users). |
| **High** | Fills a documented gap in the scholarly record (cited in multiple publications, exhibitions, or documentaries) **or** formal designation at state/regional level **or** demonstrated research demand (finding-aid requests, digitization queues, course adoptions) **or** sustained community use evidenced over years (anniversaries, pilgrimages, active descendant community). |
| **Moderate** | Local/regional importance with some documented use; significance plausible but thinly cited. |
| **Low** | Importance asserted by the holder but not yet documented by any external use, citation, or designation. (Low significance does **not** mean low worth — see §7.) |

### Factor 3 — FEASIBILITY
*How preservable is it, right now?* Feasibility is about **actionability**, not desirability. Cost scale bands: community-scale (<$50k), institutional grant ($50–250k), major grant/consortium ($250k–$1M), national campaign (>$1M).

| Level | Observable criteria |
|---|---|
| **High** | Custodian willing and authorized; rights clear or clearly clearable; formats stable or migration straightforward; cost within a typical single-grant range. |
| **Moderate** | One or two solvable obstacles: rights negotiation needed, format migration required, custodian capacity limited but cooperative, cost at the top of grant range. |
| **Low** | Multiple hard obstacles: disputed ownership or active litigation, custodian uncooperative or unreachable, severe format degradation requiring specialist labs, cost requiring multi-funder campaign. |
| **Not feasible now** | Legal bar (court order, frozen estate), total format loss already occurred, or custodian/community explicitly refuses intervention. **Action: document and monitor only; reassess if conditions change.** Refusal is respected — see §7. |

### Factor 4 — UNIQUENESS
*Does this material exist anywhere else, in any form?* Check WorldCat, archive finding aids, and digitization registries to the extent possible; record what you checked.

| Level | Observable criteria |
|---|---|
| **Sole copy** | No known duplicate in any format anywhere. Loss = total erasure. |
| **Scarce** | 2–5 known copies, **or** only partial duplication (e.g., microfilm exists but originals are unique; Wayback Machine holds rendered pages but not the underlying corpus/database). |
| **Duplicated** | Held in preservable form by multiple institutions. |
| **Widely held** | Broadly duplicated (commercial microfilm runs, mass-digitization portals). |

---

## 3. Evidence grades

Every factor rating carries an evidence grade. **Any rating resting on C-grade evidence marks the whole assessment Provisional** — the tier stands, but flagged.

| Grade | Meaning |
|---|---|
| **A** | Primary sources: institutional statements, published finding aids, legal filings, the custodian's own published data, direct observation records. |
| **B** | Reputable secondary: major press, scholarly publications, peer-reviewed or editorially reviewed work. |
| **C** | Thin: single uncorroborated source, anecdote, inference from indirect evidence, outdated source. |

---

## 4. Combination rules

Rules are evaluated **in order; the first matching rule determines the tier.** This makes every assignment reproducible: given four ratings, there is exactly one correct tier.

**Rule 0 — Feasibility gate.** If Feasibility = *Not feasible now* → **Tier 4** (document-only; reassess if conditions change). This is evaluated before all else.

**Rule 1 — Tier 1 (Emergency)** if ANY of:
- (a) Risk = Critical **and** Uniqueness = Sole copy, *regardless of other factors*; or
- (b) Risk = Critical **and** Significance = Exceptional; or
- (c) Risk = High **and** Uniqueness = Sole copy **and** Significance = Exceptional.

**Rule 2 — Tier 2 (Urgent)** if ANY of:
- (a) Risk = Critical (and Rule 1 did not apply); or
- (b) Risk = High **and** (Significance ≥ High **or** Uniqueness ∈ {Sole copy, Scarce}); or
- (c) Risk = Moderate **and** Uniqueness = Sole copy **and** Significance = Exceptional.

**Rule 3 — Tier 3 (Planned)** if ANY of:
- (a) Risk = High (and Rules 1–2 did not apply); or
- (b) Risk = Moderate **and** (Significance ≥ Moderate **or** Uniqueness ∈ {Sole copy, Scarce}).

**Rule 4 — Tier 4 (Monitor)** — everything else: stable custody, low significance, widely duplicated, or not currently feasible.

### Tier definitions

| Tier | Name | Action horizon | Meaning |
|---|---|---|---|
| **Tier 1** | Emergency | Act within 12 months | Irreversible loss is near and the material is irreplaceable. Stabilize first, catalog later. |
| **Tier 2** | Urgent | Act within 1–3 years | Serious threat or exceptional sole-copy material in fragile custody. Fund and schedule now. |
| **Tier 3** | Planned | 3–5 year pipeline | Worth preserving; no immediate threat. Build into grant cycles. |
| **Tier 4** | Monitor | Ongoing | Stable, already preserved, widely duplicated, or document-only. Reassess on trigger events. |

### Worked-rule sanity checks (verify reproducibility)
- Critical + Sole copy + Low significance + Low feasibility → **Tier 1** (Rule 1a; feasibility Low does not demote — only *Not feasible now* gates).
- Low risk + Exceptional + Sole copy + High feasibility → **Tier 4** (nothing threatened; monitoring suffices).
- High + High + High feasibility + Widely held → **Tier 2** (Rule 2b: significance alone qualifies when risk is High).
- Moderate + Moderate + High + Duplicated → **Tier 3** (Rule 3b).
- Any combination + Not feasible now → **Tier 4 document-only** (Rule 0).

---

## 5. Worked examples

Each example shows the four factor ratings, the rule applied, the resulting tier, and the evidence grade of the underlying facts. Assessments are **time-stamped**: a tier describes a moment, not a permanent rank. Three examples are assessed retrospectively at a historical decision point to show how tiers move after intervention.

### EX-01 · Johnson Publishing Company photo archive (Ebony / Jet) — assessed July 2019
~4 million images documenting Black American life across the Ebony and Jet decades. Parent company in bankruptcy; archive put up for auction. A four-foundation consortium (Ford, Getty, MacArthur, Mellon) won the auction after a two-day diligence sprint; the archive was destined for the Getty Research Institute and the Smithsonian's National Museum of African American History and Culture.
- **Risk: Critical** — bankruptcy auction underway; competing creditor claims on the photographs. *(Evidence A)*
- **Significance: Exceptional** — the defining visual archive of 20th-century Black American life; national press and institutional commitment. *(Evidence A)*
- **Feasibility: Moderate** — complex bankruptcy, art-law, IP, and employment claims; 4M images; but a funded, willing consortium. *(Evidence A)*
- **Uniqueness: Sole copy** — the archive itself; no duplicate. *(Evidence A)*
- **Combination:** Rule 1a (Critical + Sole copy) → **TIER 1**
- **Outcome:** rescued. Reassessment today: Risk Low → **Tier 4 (Monitor)**. Tiers expire; intervention works.
- *Sources: The Art Newspaper, 2019-08-02 (interview with transaction counsel).*

### EX-02 · BlackPast.org — assessed 2026-09 (current)
Digital-only encyclopedia of African American and global African history: 5,000+ entries, ~6M annual visits, recognized as a resource by the Library of Congress, ALA, and NYPL. Founder Quintard Taylor died in 2025. The $300k/year budget is donation-funded; the site's own banner states "funding cannot keep pace… the platform becomes vulnerable."
- **Risk: High** — founder loss + self-reported funding gap; digital-only = single point of failure; no shutdown announced, but the 1–3 year threat window fits. *(Evidence A for funding statement; B for reach/recognition)*
- **Significance: High** — millions of annual users; institutional recognition; volunteer corps near 1,000 contributors. *(Evidence B)*
- **Feasibility: High** — willing nonprofit operator; owns its content; digital formats; modest cost. *(Evidence A/B)*
- **Uniqueness: Scarce** — underlying corpus is a sole copy; rendered pages partially duplicated in the Wayback Machine. *(Evidence B)*
- **Combination:** Rule 2b (High risk + Significance ≥ High) → **TIER 2**
- **Recommended action:** sustainability endowment + dark-archive deposit (e.g., Internet Archive partnership); succession governance after founder's death.
- *Sources: blackpast.org (site statements, FAQ); History News Network; WGRZ/Cox Media Group, 2026.*

### EX-03 · Knoxville College institutional records & campus heritage — assessed 2026-09 (current) · **PROVISIONAL**
HBCU founded 1875 (Knoxville, TN); MLK gave the 1960 commencement address. Lost accreditation 1997; campus closed February 2017 after buildings were deemed unsafe; EPA seized the science building (2014); a 100+-year-old historic building was destroyed by fire in November 2024. The board is pursuing re-accreditation and working with preservation planners (Knox Heritage).
- **Risk: High** — unoccupied decaying campus; an actual fire destroyed a historic building within the last two years. *The custody and condition of the institutional records themselves are not publicly documented — this rating is inferential.* *(Evidence B for campus; C for records → Provisional)*
- **Significance: High** — 150 years of Black higher education in East Tennessee; NRHP-listed campus. *(Evidence B)*
- **Feasibility: Moderate** — board exists and is cooperating with preservation planners; essentially no money. *(Evidence B)*
- **Uniqueness: Sole copy** (institutional records) — *Provisional; unverified.* *(Evidence C)*
- **Combination:** Rule 2b (High + Significance ≥ High) → **TIER 2 · PROVISIONAL**
- **Recommended action:** emergency records survey before the next building loss; oral histories with alumni while the community persists.
- *Sources: WVLT, 2024-11-05 (fire); JBHE, 2018; Inside Higher Ed; Knoxville News Sentinel via ndinsider, 2018.*

### EX-04 · Muhammad Speaks collection, Black Archives of Mid-America (Kansas City) — assessed 2026-09 (current)
19.88 linear feet (18 boxes), 1967–1997 (bulk 1967–1976): the Nation of Islam's national newspaper (1960–1975) plus successor titles. Held by a small nonprofit Black archive; access unrestricted; finding aid warns "newspapers are fragile, handle with care."
- **Risk: Moderate** — fragile newsprint; small nonprofit custodian; no imminent threat documented. *(Evidence A)*
- **Significance: High** — 15-year run of a major Black national newspaper covering the civil-rights era; cited in scholarship. *(Evidence A/B)*
- **Feasibility: High** — cooperative institution, unrestricted reproduction, straightforward digitization. *(Evidence A)*
- **Uniqueness: Scarce** — *other partial runs likely exist in research libraries; completeness of this run unverified.* *(Evidence C → Provisional on this factor)*
- **Combination:** Rule 3b (Moderate + Significance ≥ Moderate) → **TIER 3 · PROVISIONAL** (on uniqueness)
- **Recommended action:** place in digitization grant pipeline; verify duplication against WorldCat before spending.
- *Sources: Black Archives of Mid-America finding aid AC58.*

### EX-05 · The Obsidian Collection / Chicago Defender photo morgue — assessed 2026-09 (current)
Chicago nonprofit (founded 2017 by Angela Ford) digitizing ~250,000 images from the *Chicago Defender*, *Baltimore Afro-American*, and 12+ other Black newspapers; public exhibits via Google Arts & Culture. Digitization is underway, but the organization is founder-dependent and small; long-term physical custody and climate control of the original negatives are not publicly documented.
- **Risk: Moderate** — active project but single-founder dependency; physical originals' storage conditions unclear. *(Evidence B; physical-custody facts Provisional)*
- **Significance: Exceptional** — the *Defender* (1905–) was the most influential Black newspaper in America; its photo morgue is the visual record of the Great Migration and civil-rights Chicago. *(Evidence A/B)*
- **Feasibility: High** — willing custodian, Google partnership, digitization in motion. *(Evidence B)*
- **Uniqueness: Sole copy** — original negatives/prints. *(Evidence B)*
- **Combination:** Rule 2c (Moderate + Sole copy + Exceptional) → **TIER 2**
- **Recommended action:** succession planning; cold-storage survey of originals — digitization must not substitute for preservation of the physical archive.
- *Sources: Mic, 2018; Atlas Obscura, 2018; Chicago Magazine via ABHM; Essence.*

### EX-06 · DJ Screw Collection, University of Houston Libraries — assessed 2026-09 (current)
Personal papers, 1,600+ vinyl records, original "screw tapes," photographs, and equipment of Robert Earl Davis Jr. (DJ Screw, 1971–2000), originator of the chopped-and-screwed sound. Donated by his father beginning 2011; cataloged, partially digitized, exhibited.
- **Risk: Low** — stable institutional custody with finding aid and digital access. *(Evidence A)*
- **Significance: High** — foundational Houston hip-hop archive; global influence on Southern hip-hop. *(Evidence A/B)*
- **Feasibility: High.** *(Evidence A)*
- **Uniqueness: Sole copy** — personal papers and original tapes. *(Evidence A)*
- **Combination:** Rule 4 → **TIER 4 (Monitor)**
- **Retrospective note:** at the 2011 acquisition decision point — private family custody after Screw's 2000 death, magnetic tape degrading — this rated Risk High → **Tier 2**. Intervention moved it to Tier 4. The framework describes rescue; it does not permanently rank.
- *Sources: UH Libraries finding aid 2010-023; UH Digital Collections; BET, 2011.*

### EX-07 · Surviving Oscar Micheaux film elements — assessed 2026-09 (current)
Micheaux (1884–1951) wrote, produced, and directed 40+ features (1918–1948), the foundational Black independent cinema. Roughly 30 titles are lost entirely; about 10 survive, several as single incomplete prints on decomposing nitrate stock (*Within Our Gates* survived as one print found in Spain, 1990; *The Symbol of the Unconquered* as a partial print found in Belgium). Surviving elements are scattered across archives (Library of Congress, George Eastman Museum) and private hands.
- **Risk: Critical** — nitrate decomposition is active and irreversible; single-print survival means one accident = total loss. *(Evidence B)*
- **Significance: Exceptional** — "the most important Black filmmaker who ever lived" (Jacqueline Stewart); earliest surviving Black-directed features. *(Evidence B)*
- **Feasibility: Low** — scattered holdings, specialist photochemical restoration, murky rights, high cost. *(Evidence B)*
- **Uniqueness: Sole copy** — per surviving title, single or partial prints. *(Evidence B)*
- **Combination:** Rule 1a (Critical + Sole copy) → **TIER 1** *(Low feasibility does not demote — only "Not feasible now" gates.)*
- **Recommended action:** international survey for unidentified holdings; cold storage; duplication to safety stock. Acknowledge the ~30 lost titles as document-only: name what is gone so the loss is recorded.
- *Sources: KOLUMN Magazine, 2025; Smithsonian Magazine; Il Cinema Ritrovato festival notes; Indiana University ScholarWorks (Orphans symposium transcript).*

### EX-08 · Mother Bethel AME Church records — retrospective assessment at 2013 decision point
Mother Bethel (Philadelphia), founded 1794 by Richard Allen — birthplace of the AME denomination. By 2013 the church archives had run out of space; the archivist moved materials to the Presbyterian Historical Society for climate-controlled, secure storage; a Pennsylvania Abolition Society grant funded digitization, completed 2021.
- **Risk: High (2013)** — outgrown storage, no climate control, collection at the "we must move it or lose it" point. *(Evidence A/B)*
- **Significance: Exceptional** — founding congregation of the first independent Black denomination in America. *(Evidence A)*
- **Feasibility: High** — willing archivist and congregation; PHS partnership; grant funding secured. *(Evidence A)*
- **Uniqueness: Sole copy** — congregational records. *(Evidence B)*
- **Combination:** Rule 2b (High + Significance ≥ High) → **TIER 2**
- **Outcome:** digitized 2021; reassessment today → **Tier 4 (Monitor)**. A Tier 2 rating correctly triggered action that resolved the risk.
- *Sources: The Christian Post, 2021-02-11; Presbyterian Historical Society.*

### Tier distribution across worked examples

| Tier | Examples |
|---|---|
| Tier 1 — Emergency | EX-01 (JPC archive, 2019), EX-07 (Micheaux elements) |
| Tier 2 — Urgent | EX-02 (BlackPast.org), EX-03 (Knoxville College, Provisional), EX-05 (Obsidian/Defender morgue), EX-08 (Mother Bethel, 2013 retrospective) |
| Tier 3 — Planned | EX-04 (Muhammad Speaks @ BAMA, Provisional on uniqueness) |
| Tier 4 — Monitor | EX-06 (DJ Screw @ UH — rescued) |

---

## 6. Reassessment protocol

Tiers are time-bound, not permanent. Reassess:
1. **Annually** for Tier 1 and Tier 2 items;
2. **On trigger events**: fire, flood, death of custodian/founder, auction or sale announcement, grant award, completed digitization, institutional acquisition, building condemnation;
3. **Tier expiry:** any assessment older than 24 months without review is marked **Stale** — the tier is not quoted until re-rated.

Record for each assessment: assessor, date, the four ratings with evidence grades, the rule applied, and sources. (See `framework.json` for the machine-readable schema.)

---

## 7. What this framework does NOT do

- **It does not rank cultural worth.** A Tier 4 item is not less Black, less loved, or less important than a Tier 1 item. The tiers rank *preservation urgency under scarcity* — nothing else. A widely-held, well-preserved collection (Tier 4) may be among the most culturally precious things in existence; it simply does not need emergency action.
- **It does not compare Black memory to anyone else's.** This framework exists because Black cultural memory faces specific, documented patterns of loss — it is not an argument about relative value between communities.
- **It does not override custodian or community consent.** A Tier 1 rating is a recommendation to *offer help*, never a license to extract. If a community says no, Feasibility becomes *Not feasible now* (Rule 0) — the framework respects the refusal and moves to document-and-monitor. Preservation without consent is not preservation; it is acquisition.
- **It is not a canon.** Inclusion or tier placement confers no official status, and omission confers no judgment. The framework covers what has been assessed; unassessed does not mean unimportant.
- **It does not substitute for provenance and rights research.** Feasibility ratings assume good-faith rights diligence; contested ownership must be resolved before action, not after.
- **Its ratings are only as good as their evidence.** Provisional markings must travel with the tier wherever it is quoted. A Tier 2 (Provisional) is an invitation to verify, not a finding.
- **It does not promise rescue.** Tier 1 means "act first," not "will be saved." Some losses — like Micheaux's ~30 lost films — are already irreversible; the framework's honest job there is to name the loss and protect what remains.

---

## 8. Version history

- **v1.0 — 2026-09-28**: Initial framework: 4 factors, 4 levels each, ordered rule set (Rules 0–4), evidence grades A/B/C, 8 worked examples (2 retrospective, 1 provisional-heavy), reassessment protocol, limitations.
