# Red Team — CTL-DR-BVM-005: Bronzeville: Black Metropolis

**Date:** 2026-09-28
**Purpose:** Deliberately attack this package's weaknesses before a flagship CTL artifact is built from it.

---

## 1. Nostalgia and survivorship bias
**Risk:** The "Rise" story rewards the most photogenic survivors — the Regal, the Savoy, the Sunset — while erasing what the era actually felt like for most residents: kitchenette overcrowding, rent gouging, poverty, and vice economies.
**Check:** The package includes kitchenettes (Wright's "kitchenette" coined for exactly this), rent parties, the Black Belt's crowding statistics (Frazier 1932; Race Relations Commission 1922), and internal class geography (Strivers Row as the top of an internal class system). It rejects an uncritical "golden age" narrative as house position.
**Residual risk:** Low-medium. The visual layer of any artifact will still tilt toward the glamorous venues unless CTL deliberately commissions kitchenette and working-class imagery.

## 2. Geographic bias
**Risk:** Folding Woodlawn, Washington Park, Grand Boulevard, and Douglas into one undifferentiated "Bronzeville."
**Check:** The package keeps Douglas, Grand Boulevard, Washington Park, and Woodlawn distinct (Hansberry's 6140 S. Rhodes is explicitly in Woodlawn; the RTR is explicitly Grand Boulevard/Washington Park). The Stroll's boundaries are recorded as disputed and era-shifting, not drawn as a fixed line.
**Residual risk:** Low, provided the artifact's maps keep the distinction.

## 3. Famous-person bias
**Risk:** Louis Armstrong, Gwendolyn Brooks, and Ida B. Wells drown out the porters, domestic workers, beauticians, and rent-party hosts.
**Check:** Named-worker coverage exists: Pullman porters, packinghouse workers, beauticians/barbers, domestic workers, kitchenette residents. Women included substantively: Vivian G. Harsh, Elizabeth Lindsay Davis, Irene McCoy Gaines, Marjorie Stewart Joyner, Margaret T.G. Burroughs, Michelle Duster, and the Olive Leaf Club founders Bertie Boone and Maggie Walker.
**Residual risk:** Medium. Named barbershops, beauty shops, storefront churches, and Bronzeville-specific fraternal lodges remain thin — the working-class institutional layer is acknowledged but underbuilt.

## 4. Missing women and working-class history
**Risk:** A "great men and great venues" page.
**Check:** Women's institutions anchor the everyday-life layer (Liberty Baptist grew from a women's club; Harsh's Hall Branch was a movement institution; Gaines's committee work produced the Ida B. Wells Homes). The red-team flag on Drake & Cayton's exclusion of women is recorded. Oral-history leads (Terkel, HistoryMakers, Williams video collection) point toward primary voices.
**Residual risk:** Medium. The oral histories are identified but not consulted. A flagship should not publish "everyday life" as authority before doing that listening.

## 5. Disputed dates and weak single-source claims
**Risk:** Publishing a confident date that the evidence doesn't support.
**Check:** The package preserves, rather than resolves: Savoy closing (1948 vs. 1954), Dreamland address (3520 vs. 3618 S. State), Douglass Bank founding year (1921/1922/1923), *Hansberry v. Lee* decision day (Nov 12/13/Dec 12, 1940), Chicago Bee founding year (1925/1926), Regal architect (unknown — no attribution published), Robert Taylor unit count (4,321 vs. 4,415), Dan Ryan displacement counts (10,000 vs. 12,000 vs. unresolved), and the 18,000-figure for aggregate urban-renewal displacement. These appear in `timeline.json` `date_alternatives` and in entities' contradictory-evidence fields.
**Residual risk:** Low — the structure forces qualification — but only if the artifact layer reads the grades instead of the headlines.

## 6. Weak sources presented as strong
**Risk:** The Lindstrom 2012 compilation is the richest single venue source and also the most load-bearing single source. Several venue claims rest on it alone and are graded Provisional; internal Lindstrom inconsistencies are flagged.
**Check:** Source-type classification is honest: Wikipedia-derived claims are Provisional unless corroborated; no Verified claim rests solely on Wikipedia.
**Residual risk:** Medium. A venue-by-venue primary-source verification pass (Sanborn maps, city directories, Defender archival issues) is the single highest-value upgrade and has not been done (see gaps.md).

## 7. Single-cause decline narratives
**Risk:** "The Dan Ryan killed Bronzeville" or "public housing killed Bronzeville."
**Check:** House position is explicitly multi-causal: deindustrialization, deliberate segregation policy, demographic pressure, disinvestment, urban renewal and public-housing siting/demolition, expressway routing, and constrained-then-expanded mobility/outmigration operated together across decades. "Decline" itself is flagged as partly a narrative artifact — institutions persisted, people stayed.
**Residual risk:** Low for the research layer; the artifact's narrative discipline will decide.

## 8. The naming-origin trap
**Risk:** "The Defender coined 'Bronzeville'" — the clean, wrong version.
**Check:** The package's position: James J. Gentry (Chicago Bee theater editor) coined it ~1930; the Bee's 1930 contest failed; Gentry carried the idea to the Defender's Robert Abbott in 1932; Charles Browning built it into a Defender promotion. Simplistic "Defender coined it" claims are graded as weak.
**Residual risk:** Low.

## 9. Resident vs. visitor vs. performer conflation
**Risk:** Treating every name on a Regal marquee as a Bronzeville resident.
**Check:** The package explicitly requires residency verification and records the correction (e.g., Nat King Cole's Bronzeville residency is Provisional, not Verified; Earl Hines's is).
**Residual risk:** Medium — easy to backslide in a visual artifact full of famous faces.

## 10. BSCP and labor-history precision
**Risk:** "The first Black labor union" — wrong; it was the first labor organization led by African Americans to receive an AFL charter (1935). Porter-residency claims and "porters carried the Defender south" are unverified.
**Check:** Recorded as corrections with exact charter language.
**Residual risk:** Low.

## 11. *Black Metropolis* (1945) as unquestioned authority
**Risk:** Treating Drake & Cayton as the last word.
**Check:** The package treats it as scholarship, not scripture: it records the "ghetto story" framing critique and the exclusion of women.
**Residual risk:** Low.

## 12. Copyright and image rights
**Risk:** A visually rich artifact will want archival photographs (Regal marquees, Savoy interiors, Defender front pages, Binga and Overton portraits) whose rights are not cleared.
**Check:** Flagged in gaps.md as requiring a dedicated rights review before publication. No images are bundled with this package.
**Residual risk:** High if the artifact team skips the review. Rights clearance must be a gating checklist item, not a footnote.

## 13. Developer claims laundered as facts
**Risk:** Bronzeville Lakefront job/economic-impact figures are developer claims; the Shops at 47/Mariano's "revitalization" framing is a stakeholder narrative.
**Check:** The remaking layer presents multiple viewpoints — displacement concern, Black middle-class reinvestment, selected-tract research (poverty reduction without measurable displacement), intentional community investment, managed mixed-income growth, market-positive framing, and structural critique — and grades developer projections as such.
**Residual risk:** Medium. Current (late-2026) completion status of Phase 1 is unverified and must be checked before any "now" statement ships.

## 14. Boundary presentism
**Risk:** Drawing today's "Bronzeville" — a neighborhood that now stretches, in marketing, far beyond its historic core — onto 1920s maps.
**Check:** The research-brief's geographic-definition section distinguishes the historic Black Belt core from later and marketing expansions.
**Residual risk:** Low-medium.

## 15. The artifact-outruns-the-evidence risk
**Risk:** The biggest meta-risk. This package is a strong secondary synthesis. It is not yet a primary-source investigation. A flagship artifact that presents it as one — "from the archives" language over a literature review — would violate CTL's own evidence-before-authority principle.
**Mitigation:** The artifact's provenance layer must be honest about what is Verified, what is Provisional, what is Disputed, and what remains Unresolved. The four-grade vocabulary exists for exactly this.

---

**Net assessment:** The package's structure (grades, alternatives, contradictory evidence) is doing real work against most of these biases. The two highest residual risks are **copyright/rights clearance** and **the artifact outrunning the evidence**. The highest-value research upgrades are a **Sanborn/directory/Defender venue-verification pass** and **direct Census/NHGIS population verification**.
