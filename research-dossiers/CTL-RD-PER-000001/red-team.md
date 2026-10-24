# CTL Red-Team Report — CTL-RD-PER-000001: Ida B. Wells

**Dossier:** CTL-RD-PER-000001 · **Evidence file:** CTL-EF-PER-000001
**Version:** 1.0.0 — 2026-09-28
**Checklist:** Appendix C of the Type 03 template (18 items)

> **CULTURETECHLENS** — *Culture, Clearly Seen.* — Black Cultural Intelligence

- [x] **Unsupported claims: every §15 claim traces to §16 evidence** — PASS. All 47 ledger claims have condensed evidence in dossier §16 and full 10-part records in CTL-EF-PER-000001; automated cross-check confirmed 1:1 text and grade reconciliation (CLAIM-047 via the UNRESOLVED↔UNVERIFIABLE crosswalk).
- [x] **Circular sourcing: no source corroborated only by its own repetitions** — PASS. VERIFIED claims pair primary accounts with contemporary/independent sources (§16, sources.md). Popular-source convergence was checked for independence.
- [x] **Myths repeated as facts: §27 adjudicates every widely repeated claim** — PASS. §27 covers: "burned" vs "destroyed" (corrected); Stewart first-name variant (recorded, not adjudicated); sibling count seven-vs-eight (recorded); NAACP "founder" conventional-vs-formal (nuance recorded); "first statistical study" as conventional description; Abbott birth-year dispute (no bare year printed); CLAIM-047 held UNRESOLVED rather than repeated.
- [x] **Date conflicts: checked against contradictions.json harmonizations** — PASS. Defender founding May 5, 1905 (BlackPast May 6 dissent footnoted); Abbott 1868-vs-1870 DISPUTED with no bare year printed; move-to-Memphis year recorded as a range (1881–1883).
- [x] **Name ambiguity: §04 disambiguates; no two entities share an ID** — PASS. 68 entities, all IDs unique (validated). canon-ida-b-wells-homes distinct from Wells and the Wells-Barnett House; canon-chicago-defender distinct from Defender buildings; Stewart name variants recorded under one entity.
- [x] **Geographic errors: addresses verified; community areas not collapsed** — PASS. 3624 S. King Drive with residence dates; Holly Springs / Memphis / Chicago kept distinct; Bronzeville named for the monument; People's Grocery at the Curve (south Memphis) per Ben Hooks Institute.
- [x] **Anachronisms: every dated claim checked against the timeline** — PASS. Chronology §08 spans 1862–2021; no claim predates its context (e.g., NAACP 1909 not backdated; *Defender* 1905 not conflated with the *Free Speech* years).
- [x] **Causation without evidence: no "led to" / "caused" without documented mechanism** — PASS. The WCTU claim is phrased as the USC project's synthesis ("in response to pressure from Wells"); the Moss lynchings are described as catalytic per Wells's own account and convergent scholarship, not as sole cause.
- [x] **Selection bias: what survives in archives vs. what existed** — PASS. §28 names the lost *Free Speech* corpus as the largest gap; the dossier does not treat the surviving record as the whole record.
- [x] **Celebrity bias: ordinary people and workers included where documented** — PARTIAL. Moss, McDowell, Stewart, Fleming, Baker, Squire are named as actors, not backdrop; the BSCP support (CLAIM-037) gestures at labor. Deeper worker-level sourcing deferred to gaps.
- [x] **Survivorship bias: defunct/closed subjects' thinner records acknowledged** — PASS. Destroyed *Free Speech* office, demolished Wells Homes (2002–2011), and lost papers are explicitly marked as thin-record zones.
- [x] **Missing women: explicitly searched for, not assumed absent** — PASS. This dossier exists to fill MEDIA-001's "missing woman publisher" gap; Squire, Terrell, Duster, Warrenton Wells are entities with claims.
- [x] **Missing institutions: the subject's institutional context mapped** — PASS. 12+ organization entities: press (*Free Speech*, *Age*, *Conservator*, *Defender*, *Inter Ocean*, *Living Way*), clubs (NFL, Alpha Suffrage, Wells Women's Club, Third Ward WPC, NACW, Afro-American Council, Colored Press Association), WCTU, BSCP, NAACP, UChicago archive.
- [x] **Duplicate entities: checked against duplicates.json canonical clusters** — PASS. Audit canonical IDs used: canon-chicago-defender, canon-ida-b-wells-homes, canon-oscar-de-priest, canon-robert-sengstacke-abbott.
- [x] **Weak visual provenance: every image/video has creator, date, source, rights** — PASS. visuals.md: V-01 (Garrity, c. 1890s, public domain, full chain), V-02 (1893, public domain); no video selected; no AI-generated imagery.
- [x] **Copyright/rights: §33 log complete; nothing reproduced without clearance** — PASS. Both images public domain; data graphics are original CTL works.
- [x] **Privacy: no private locations or sensitive personal information exposed** — PASS. Only public/historical addresses (a landmarked house); no living persons' private data.
- [x] **Sensitive subjects: dignity maintained; no sensationalism** — PASS. Lynching content is handled as documented history with named victims and evidentiary framing, not spectacle.

## Convention deviations noted

- Entity IDs use dossier-local semantic slugs (`per-wells-ida`, `org-free-speech`) rather than the template's `RD-<DOSSIER>-###` pattern; audit `canon-<slug>` IDs are used where established. IDs are unique and namespaced to this dossier's directory.
- §14 human-readable predicates occasionally paraphrase edge predicates (e.g., "co-owned" for `part_owner_of`); every entry maps to a real edge in relationships.json (verified this pass; two missing edges were added: rel-076, rel-077).

## Residual risks

1. Six ledger claims (035–038, 042, 043) lean on single weak sources with corroboration flags — the dossier's honesty mechanism, not a hidden weakness.
2. CLAIM-047 (Barnett death timing) is UNRESOLVED and should be refuted or removed once Barnett's death record is checked.
3. The *Free Speech* corpus gap caps how far the "woman publisher" thesis can go on primary evidence.
