# Synthesis Notes — CTL-DR-PRESERVE-001

> **CULTURETECHLENS** · *Culture, Clearly Seen.* · **Black Cultural Intelligence**

**Project:** CTL-DR-PRESERVE-001 · **Date:** 2026-09-28
How the six tracks were merged into the canonical outputs: every dedup decision, conflict, exclusion, and judgment call, recorded so the synthesis is auditable.

---

## 1. Cross-track merge table

Six canonical records were built from multiple track records. One canonical record per collection; the most complete documented values were kept; no extents, dates, or relationships were invented.

| # | Canonical record | Merged from | Key merge decisions |
|---|---|---|---|
| 1 | Johnson Publishing Company Archive (Ebony/Jet photographic and business archive) | institutional (photographic archive) + community (editorial/business archive) + digital (JPC photo archive) | Institutional record supplied the photo-archive core; community supplied business/editorial records and the Blackivists processing detail; digital supplied the digitization-status framing. Extent conflict preserved as range (4M vs. 4.5M images; 9,000 vs. 10,000 AV). |
| 2 | The HistoryMakers Digital Archive / Video Oral History Collection | institutional + digital | Institutional supplied the nonprofit/LoC custody record; digital supplied the access-model and analog-holdings detail. |
| 3 | Black Metropolis Research Consortium (BMRC) Archives Portal | institutional + digital (portal record) | Kept as a discovery layer, not a preservation repository — the distinction the digital track drew explicitly. |
| 4 | Shorefront Legacy Center community archive | institutional + community | Institutional supplied the reparations-report context; community supplied the Evanston/North Shore operational detail. |
| 5 | South Side Community Art Center archives and collections | institutional + community | Institutional supplied the AAA survey record; community supplied the living-institution detail. |
| 6 | Obsidian Collection Archives | community + digital | Community supplied the nonprofit/founder record; digital supplied the digitization-totals framing and the 2018 public-release figures. |

**Deliberately NOT merged (kept distinct):**
- **Chicago Defender photo morgue vs. Obsidian Collection Archives.** The Defender morgue is the *source collection* (the newspaper's photographic archive); Obsidian is the *digitization nonprofit and partner* founded to digitize it. Merging them would erase the custody/provenance distinction. They are linked by relationship, not merged.
- **Muhammad Speaks newspaper archives vs. the Black Archives of Mid-America 18-box run.** The unresolved paper's own morgue is not the same thing as the documented 18-box run (1967–1997, finding aid AC58). Conflating them would launder an Unresolved custodianship into a documented holding.
- **Stony Island Arts Bank's JPC reference library vs. the JPC photographic/business archive.** The Arts Bank holds Johnson Publishing's *reference library* (12,000–15,000+ vols.), a separate corpus from the photographic/business archive now at NMAAHC/Getty.
- **Freedmen's Bureau Records (NARA, institutional) vs. Freedmen's Bureau Project (digital).** The federal record series (RG 105) and the 2015 crowdsourcing project that indexed it are different entities; both appear, cross-referenced.

---

## 2. Grade conflicts

**No merged record required weakening.** All six merges drew on track records whose grades agreed (Verified), so the "keep the weaker grade" rule was never triggered at merged-record level. This is recorded here rather than assumed: the rule was applied and produced no conflicts.

Point-value conflicts (not grade conflicts) were preserved as documented ranges:
- JPC: 4M vs. 4.5M images; 9,000 vs. 10,000 AV recordings
- Harsh Collection: 70,000 vs. 80,000+ books; 250+ manuscript collections vs. ~300,000 pieces (different counting unit — noted, not reconciled)
- Moorland-Spingarn: 17,000 vs. 18,000+ linear feet; 200 vs. 650 collections (source/date-dependent)
- Schomburg: 10M vs. 11M items; NMAAHC: 37,000 vs. 45,000 objects; Amistad: 800 vs. 900 collections
- Teenie Harris: 70,000+ vs. ~80,000 negatives

**Record-level grade coverage:** 28 collections Verified, 2 Provisional, 54 "Not graded" — the institutional and community track files grade substantive *claims*, not collection records, and no record-level grade was documented there. This is stated honestly in the records rather than backfilled. All entity claims (119 entities) carry full claim/evidence/source/grade structures; all 70 timeline events are Verified; all 78 relationships are Verified-only.

---

## 3. Excluded from the collection map (with rationale)

The memory map contains **collections**. The following were excluded from it by design and appear instead in entities, timeline, gaps, or the brief:

- **BET.com digital article wipe (2026), #BlackLivesMatter tweet decay, Twitter/X API restriction, Myspace server-migration loss, Eyes on the Prize rights blackout** — pure loss/event cases, not collections. They are event entities and timeline events.
- **Documenting the Now** — a concept/tool project (social-media archiving methodology), not a collection.
- **Internet Archive** — a custodian/platform, not a collection. It appears as a custodian entity (backstop for BET rescue, WVON airchecks).
- **Taylor Cassidy (Fast Black History) and HomeTeam History** — creator-led channels. Judgment call: they are collection-*like* (curated bodies of Black historical content) but platform-hosted creator outputs, not archives with custodianship; excluded from the map, noted here. A future pass could consistently treat creator-led corpora as a collection class — the current exclusion is documented, not principled against it.
- **Black Panther Party records** — an *absence*: no centralized archive exists. It appears as a collection entity (the absent archive) and in the risk register, but not as a memory-map collection, because there is no collection to map.

**Arithmetic check (red-team reconciled, 2026-09-28):** 91 track-level input records = 32 institutional-origin + 29 community-origin + 21 digital-origin (17 pure-digital + 4 absorbed into merges) + 5 framework-derived + 4 risk-derived. Six merged records absorbed 13 track records into 6 canonical records (JPC absorbed 3; five others absorbed 2 each), a net −7 → **84 canonical records**. The origin counts sum above 84 only if merged records are double-counted; canonically each is counted once.

---

## 4. Privacy normalization

- All locations normalized to **city/institution level**. The Moorland-Spingarn source record contained a public-campus street address; the canonical record uses only "Washington, DC."
- **Public-landmark exception (red-team disclosed, 2026-09-28):** 7 canonical records of public museums/landmarks retain their *published* street addresses as their sources publish them. The normalization rule above applies to private and ambiguous locations; this exception is documented rather than silently inconsistent.
- No private residences, precise storage locations, or collector home addresses published. WVON aircheck collectors, family collections, and the Calhoun-McCormick evacuation are described at aggregate level.
- Burial/funeral records (Illinois rescue, King and King, Richard Funeral Home) carry privacy notes; no record-level personal data published; shuttered firms' names withheld where the sources withheld them.
- Living photographers and private collectors (Ovie Carter, Bob Black, John Simmons) are treated at non-sensitive granularity; disposition claims are hedged to Provisional where inference is involved.
- A.A. Rayner & Sons: no intrusive inquiry proposed; flagged as a holder-initiated lead only.
- Automated privacy scan of the final memory map (street-address pattern): **0 flags.**

---

## 5. Event vs. collection decisions

Rule applied: if the thing is a *body of material with (or needing) custodianship*, it is a collection; if it is something that *happened to* material, it is an event. Borderline cases:

- **BET Digital written archive (deleted):** treated as a collection entity (it *was* a corpus) AND a 2026 event (the deletion). Both, cross-referenced — the loss is the finding.
- **Chess Records masters (destroyed):** collection entity (the destroyed corpus) + 2008 fire event. Kept in the map because the destroyed corpus is itself a documented collection with a defined extent claim.
- **Pilgrim Baptist Church archive (destroyed):** same treatment — the archive is mapped; the fire is an event.
- **#BlackLivesMatter tweets:** not a collection (no corpus boundary, no custodian); event + risk case only.
- **Eyes on the Prize:** not a collection in this corpus (the series is a distributed work, not an archive); event + copyright-risk case.

---

## 6. Known limitations of the synthesis

- The corpus is **Chicago-anchored by design**; national coverage is opportunistic, not systematic.
- Web-visible by method: the community track states plainly that the most important collections are the ones no search can find.
- Two risk types have **no documented case** (building demolition, domain expiration) — recorded as negative findings, not safety.
- Timeline dates are exact only where documented; eras ("ca. 1995–2005") are used where sources are approximate.
- The framework track has no separate source list; its worked examples cite the other tracks' evidence.
- Creator-led digital corpora (excluded, §3) may deserve a consistent collection class in a future pass.

---

*CULTURETECHLENS — Culture, Clearly Seen. — Black Cultural Intelligence.*
