# CTL-DR-INST-001 — The Institutions That Held Communities Together
## The Black Institutional Ecosystem

**CULTURETECHLENS** · "Culture, Clearly Seen." · Black Cultural Intelligence
Research ID: CTL-DR-INST-001 · Package date: 2026-09-28 · Status: research complete (v0.1)

## Central question

What institutions performed the functions necessary for Black communities to survive, organize, educate, communicate, worship, create, build wealth, and preserve memory?

## Executive summary

This is not an institution directory. Across 81 institutions and 329 evidence-graded claims, the package answers the function question for each institution — what problem it solved, who founded and controlled it, who used it, how it was funded, what depended on it, what replaced it, whether it survives, and where its records are.

Three cross-cutting findings define the package:

1. **Institutional survival ≠ functional survival.** Newspapers survive as brands while print frequency, local ownership, archives, and Chicago employment disappear. Theaters survive as buildings with different governance. Banks survive as deposits with different owners. Provident Hospital's building and service returned under county ownership in 1993; independent Black ownership, control, and the race-specific professional-training mission never did. Seaway National Bank's 2017 FDIC resolution preserved depositor *access* but destroyed the Black-owned charter and the local deposit-to-loan allocation function. Bank resolutions save accounts; they don't save community control of capital.

2. **Governance transition predicted survival better than mission did.** Ada S. McKinley survived a century via founder-to-board transition; the Negro Fellowship League died with Ida B. Wells's personal subsidy; the Pekin Theatre collapsed after Robert T. Motts's 1911 death because heirs lacked his managerial capacity; Providence St. Mel survived 1978 Archdiocesan closure by converting to independent community-funded governance. How an institution was governed and funded mattered more than what it set out to do.

3. **Founder-infrastructure chains, not standalone institutions.** Institutions were rarely standalone: Ida B. Wells's Woman's Club (1893) → Negro Fellowship League reading room (1910) → Alpha Suffrage Club (1913) meeting in that room; rooms, methods, and organizers flowed along founder-built chains. The best-documented cross-institution dependency in the package is the 1955 Emmett Till funeral chain — Rayner funeral home → Roberts Temple Church → Burr Oak Cemetery — operating as one political-witness infrastructure.

## Coverage by institution type (81 entities)

| Type | n | Type | n |
|---|---|---|---|
| Theaters | 8 | Schools | 5 |
| Libraries | 5 | Professional associations | 5 |
| Settlement houses | 4 | Community organizations | 5 |
| Fraternal orders | 4 | Political organizations | 4 |
| Radio stations | 4 | Funeral homes | 3 |
| Banks | 3 | Credit unions | 3 |
| Hospitals | 3 | Insurance companies | 3 |
| Sports institutions | 3 | Women's club federations | 2 |
| Chambers of commerce | 2 | Museums | 2 |
| Archives | 2 | Political clubs | 2 |
| Youth organizations | 2 | Cemetery, orphanage, assembly hall, YMCA branch, women's club and home, women's service organization, civic club | 1 each |

**Evidence grades (329 claims):** 174 Verified · 115 Provisional · 11 Disputed · 29 Unresolved.
**Timeline:** 159 dated events. **Relationships:** 60 verified-only dependency edges (PERSON ↔ INSTITUTION ↔ COMMUNITY ↔ RESOURCE ↔ EVENT ↔ PLACE).

## The Survival Index

`survival-index.json` — 87 rows, descriptive indicators only (no numeric scores were assigned; criteria for scoring do not yet exist): **47 operating · 29 closed · 5 merged · 2 relocated · 4 unknown.** Verification: 33 Verified, 50 Provisional, 4 Unresolved — the 50 Provisional rows need date-level verification before any public-facing use.

Within the 81-entity core: 32 operating · 18 closed · 31 unknown. The high "unknown" share is itself a finding: defunct institutions leave thinner records, so disappearance is systematically under-documented (survivorship bias in the archive).

## The decade-ecosystem matrix

`decades.json` — 13 decades × 20 institution types (260/260 cells filled): presence rated strong 68 · moderate 64 · weak 91 · absent 11 · unknown 26. This is the dataset for the flagship visualization (select a decade, watch the ecosystem change). Weakest type: **social clubs** — unknown in all 13 decades, unresearched.

## Functions lost with no replacement (documented)

- **Negro Fellowship League (1910–1920):** Wells and Barnett's lodging and job-placement service for Black male migrants; closed when costs became unsustainable; no successor identified. The cleanest case of a function that vanished entirely.
- **Black-owned bank charters:** Seaway (2017), Covenant (2013), and earlier failures destroyed local Black control of capital allocation; FDIC resolutions preserved accounts, not charters.
- **Independent Black hospital governance:** Provident's training-school-to-employment pipeline (visiting-nurse service created 1896–1898 specifically to employ Black graduates white agencies refused) has no modern equivalent.
- **Settlement-house organizing hubs** as Black-governed multi-service anchors have thinned without institutional successors in most neighborhoods.

## What we know

- The function each major institution type performed, with evidence, for 81 institutions.
- That governance/funding transition predicts survival better than mission.
- That institutional survival and functional survival are different things, with documented cases.
- 60 verified dependency edges mapping how institutions actually connected.

## What we think we know

- The decade-presence ratings (many cells Provisional; social clubs entirely unknown).
- The "no Black-American-owned bank headquartered in Chicago" inference (2017 Chicago Fed count + documented closures through 2019) — **must be rechecked against the current FDIC MDI list before public use.**

## What remains unknown

- Records locations for most fraternal lodges (highest-value missing records: Odd Fellows, Knights of Pythias minutes).
- Founder rosters for several banks and chambers; dues/premium schedules and audited finances broadly.
- Closure dates for the Negro Fellowship League, Frederick Douglass Center, Appomattox Club, West Side Organization, American Giants' later years.
- UNIA / Chicago Garvey movement — the most obvious missing mass-membership institution (priority add).
- Black boxing gyms and youth leagues beyond Jackie Robinson West; dentists', nurses', realtists', accountants' associations.

## What CTL should investigate next

1. Fraternal lodge minutes (Harsh Collection, CHM, UIC, NPS/NRHP files).
2. FDIC MDI list recheck for the bank-headquarters claim.
3. Illinois Department of Insurance primary records for Supreme Life's 1999 takeover and Chicago Metropolitan Mutual's lineage.
4. UNIA/Chicago Garvey research pass.
5. Social-club decade research (the matrix's blank type).
6. Defender archives for church-basement meeting announcements (dependency edges).
7. FCC/NCUA/OCC primary records for WBGX ownership and WKKC air date (currently Disputed).

## Methodology note

Five parallel research tracks (A: mutual-aid & care; B: knowledge & learning; C: money & voice; D: organizing & power; E: systems synthesis) wrote to `working/track-{a,b,c,d,e}/`. The coordinator merged 86 track entities into 81 canonical records (2 cross-track duplicate pairs merged with notes), normalized schemas, and ran the red-team pass (see red-team.md). Sibling packages SCI-004 (churches), BPM-003 (press), and BCI-001 (institutions overview) were treated as depth layers — referenced for dependency edges, not re-researched. Supplementary datasets: `survival-index.json`, `decades.json`, `governance-patterns.json`.
