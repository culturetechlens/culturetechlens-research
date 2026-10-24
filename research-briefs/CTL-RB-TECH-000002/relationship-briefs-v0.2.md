# CULTURETECHLENS
## "Culture, Clearly Seen."
### Black Cultural Intelligence

---

# Relationship Briefs — CTL-RB-TECH-000002 v0.2
## Proposed edges for the afterlife entities
**Version:** v0.2 (2026-10-08) · **Status:** Research (not publication) · **Briefs only — no edges created, nothing merged.**

Every proposal below was checked against `knowledge-graph/schema.json` (64 relationship types, each with `from_types`/`to_types`). Only edges the matrix allows are proposed. Rejected candidates are documented with the schema reason.

**Schema citations used:**
- `related_to`: from `[Person, Practice, Event]` → to `[Person, Practice, Event]`
- `founded_by`: from `[Business, Church, Institution, Organization, Publication, RadioStation, School, Venue, Archive, Person, Event]` → to `[Person]`
- `founded`: from `[Person]` → to `[Organization, Publication, Institution]`
- `located_in`: from `[Institution, Venue, Business, Church, School, Publication, Organization, Archive, RadioStation, Address]` → to `[Neighborhood]`

---

## PROPOSED EDGE R-1

- **Type:** `related_to` ✓ (Person → Practice allowed)
- **From:** Chief Keef (CTL-E-0064, Person)
- **To:** Chicago drill (proposed Practice entity)
- **Claim:** Chief Keef's "Bang" (2011) was drill's breakout artifact — the association between the artist and the practice.
- **Grade:** PROVISIONAL (the "Bang"/400K claim is unsourced; the artist–practice association itself is the edge's substance).
- **Source hunt:** contemporary 2011–2012 profiles linking Keef to drill's emergence.

## PROPOSED EDGE R-2

- **Type:** `related_to` ✓ (Practice → Person allowed)
- **From:** Chicago drill (proposed Practice entity)
- **To:** Chief Keef (CTL-E-0064, Person)
- **Claim:** Inverse of R-1, enabling graph traversal in both directions.
- **Grade:** PROVISIONAL (same basis as R-1).
- **Note:** The schema models `related_to` as directed; both directions are proposed because neither is declared as the canonical inverse.

## PROPOSED EDGE R-3

- **Type:** `founded_by` ✓ (Publication → Person allowed)
- **From:** The TRiiBE (proposed Publication entity)
- **To:** Morgan Elise Johnson (proposed Person entity)
- **Claim:** Johnson co-founded The TRiiBE in 2017.
- **Grade:** SUPPORTED (Wikipedia; Northwestern Magazine).

## PROPOSED EDGE R-4

- **Type:** `founded_by` ✓ (Publication → Person allowed)
- **From:** The TRiiBE (proposed Publication entity)
- **To:** Tiffany Walden (proposed Person entity)
- **Claim:** Walden co-founded The TRiiBE in 2017; serves as editor-in-chief.
- **Grade:** SUPPORTED (Wikipedia; Northwestern Magazine; Medill Reports).

## CONDITIONAL EDGE R-5 (held — needs one fact)

- **Type:** `founded` ✓ (Person → Publication allowed)
- **From:** Tiffany Walden (proposed Person) → **To:** The TRiiBE (proposed Publication)
- **Status:** HELD pending the entity-minting brief. The edge is schema-valid; it is listed here so the minting brief includes both directions (`founded` + `founded_by`) rather than discovering the gap later.

## CONDITIONAL EDGE R-6 (held — needs one fact)

- **Type:** `located_in` ✓ (Publication → Neighborhood allowed)
- **From:** The TRiiBE (proposed Publication) → **To:** a Chicago Neighborhood entity (TBD)
- **Status:** HELD. Northwestern Magazine places The TRiiBE's newsroom in Homan Square (Free Spirit Media's learning newsroom), but no Homan Square Neighborhood entity has been confirmed in the graph, and HQ locations move. Do not attach until a neighborhood entity is confirmed and the location is verified as current.

---

## REJECTED CANDIDATES (documented, not proposed)

1. **"The TRiiBE published_in Chicago."** No `published_in` type exists in the 64-type matrix. The Chicago association is carried by claim T-1 (SUPPORTED) instead.
2. **"Defender published_online 2019" as an edge.** No matrix type connects a Publication to a temporal/event endpoint for a format transition (`related_to` excludes Publication endpoints; `archived_at` targets Archive entities). Kept as claim CL-020 (SUPPORTED).
3. **"Chief Keef performed drill."** No performance edge takes a Practice endpoint (`performed_at` is Person/Practice → Venue; no venue in scope). `related_to` (R-1/R-2) carries the association.
4. **BlackPlanet ~15M users as an edge.** A user count is a quantitative claim, not a relationship; kept as enrichment claim on CTL-E-4510 (PROVISIONAL).

---

## Schema-widening note (for review, not action)

The 64-type matrix has no Publication→Event, Publication→temporal, or quantitative-claim edge types — which is why the Defender's 2019 format transition and BlackPlanet's user count can only live as claims. If the graph is to model media-format transitions as first-class facts, that is a schema-widening decision for separate review, per the merge-package policy (never inside a merge).

---

*Cite as: CultureTechLens, "Relationship Briefs — CTL-RB-TECH-000002 v0.2," 2026-10-08.*
*Source: CultureTechLens.*
