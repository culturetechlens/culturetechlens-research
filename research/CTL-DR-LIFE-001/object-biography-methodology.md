# Object Biography Methodology — CTL-DR-LIFE-001 / W4

**Project:** CTL-DR-LIFE-001, "How We Lived: An Encyclopedia of Black Everyday Life"
**Workstream:** W4 — Object Biography System
**Created:** 2026-09-28

## 1. Purpose

The Object Biography System gives ten ordinary objects a documented life history: who made them,
how they were designed, sold, used, pictured, collected, and remembered. It is built for the
CultureTechLens evidence architecture — every project feeds shared Entity → Evidence → Source →
Geography → Timeline → Media → Relationship registries.

## 2. The fixed chain

Every biography follows the same 11-step chain, in order, with one link record per step:

1. **object** — the physical artifact and its accessioned/attested instance
2. **manufacturer** — who made or distributed it
3. **design** — materials, form, markings, design features
4. **period** — when the object type was made, sold, and used
5. **advertising** — how it was marketed or announced
6. **symbolism** — what it meant, *as documented in contemporary sources*
7. **consumer use** — how people actually used it
8. **photographs** — dated photographic documentation
9. **museum holdings** — verified collection records holding an instance
10. **related people** — documented persons tied to the object
11. **related movements** — documented movements tied to the object

A chain is "full" when all 11 links exist as records — **not** when every link is Verified.
Unresolved links are recorded as Unresolved, never filled with plausible narrative.

## 3. Link record schema

Every link carries its own evidence:

```json
{
  "step": "object | manufacturer | design | period | advertising | symbolism | consumer_use | photographs | museum_holdings | related_people | related_movements",
  "value": "the claim being made",
  "evidence": "what specifically supports the claim",
  "source": "where the evidence was observed (URL or citation)",
  "primary": true | false,
  "publication_date": "date the source was published, or null",
  "uncertainty": "what is still uncertain about this claim",
  "verification": "Verified | Provisional | Disputed | Unresolved"
}
```

## 4. Verification grades

| Grade | Meaning |
|---|---|
| **Verified** | Direct primary evidence, or a strong institutional record (Smithsonian museums, MoMA, Sixth Floor Museum, MTSU archives, city landmark reports, the Fitzwilliam Museum, Columbia Journalism Review, Smithsonian Magazine), and the claim matches the evidence precisely. |
| **Provisional** | Credible but indirect, single-source, or uncorroborated evidence — specialist discographies, reputable press quoting a scholar, Wikipedia, archived company histories, commercial listings. Details not independently corroborated stay Provisional. |
| **Disputed** | Materially conflicting credible claims exist. The conflict is recorded in the link; no side is chosen without primary evidence. |
| **Unresolved** | Insufficient evidence found in this pass. Recorded as Unresolved rather than narrated. |

### 4.1 What counts as primary

- Museum catalog records are **primary for** accession, description, rights statement, cataloged maker/date, and the fact of the holding. They are **not** primary evidence for broad cultural meaning.
- Patents, advertisements, catalogs, packaging, period journalism, oral histories, and dated photographs can be primary **depending on the claim** they support.
- Modern museum essays and scholarship are **secondary** unless they quote a traceable contemporary source.

### 4.2 Symbolism rule — no speculative symbolism

Symbolic meaning is graded **Verified** only when documented from: contemporary Black press,
creator testimony, period advertising, oral history, provenance-based museum cataloging, or
documented movement use. Researcher inference is never a Verified symbolism link. Where a
modern scholar's framing is the only source, the link is Provisional at best.

### 4.3 Chicago evidence

Chicago-specific evidence is attached where documented (the project's Chicago root). Where only
comparative or national evidence exists, that is stated and the Chicago link is marked
Unresolved. Distinct objects are never merged: a biography may cover Sears *and* Montgomery
Ward catalogs as a category, but their makers, dates, and holdings stay separate in the record.

## 5. Red-flag rules (enforced)

- **No speculative symbolism.** See 4.2.
- **No "first Black-owned" brand mythology.** "First" claims require primary evidence; the
  hot-comb/Madam C.J. Walker case in this batch is the warning example — the conventional
  account is explicitly rejected by NMAAHC and the link is graded Disputed.
- **No nostalgia bias.** Affection for an object is not evidence of how it was used or what it meant.
- **Never manufacture** manufacturers, dates, or museum holdings. Holdings are checked against
  actual collection databases (all museum links in this batch were read from live object records).
- **Contradictory evidence is recorded**, not smoothed over (see gaps.md).

## 6. File responsibilities

- `object-biographies.json` — the 10 biographies × 11 links = 110 link records, all grades.
- `timeline.json` — **Verified dated events only.** Bounded institutional dates (e.g., "1972–1976" on a MoMA record) are included with the bound stated.
- `relationships.json` — **Verified relationships only**, each with evidence and source. Includes one verified *negative* relationship (the refuted Walker invention claim) because refutations are evidence.
- `sources.md` — full bibliography; primary vs. secondary marked; weak sources used only provisionally are flagged.
- `gaps.md` — every Unresolved link, every contradiction, every rejected candidate source.
- `rights.md` — one entry per referenced product, advertisement, catalog, and museum-object image, using `{"item","rights_status","notes"}` with rights_status in `unknown | public domain | likely copyrighted — needs clearance`. NMAAHC's "No Known Copyright Restrictions" statements are recorded in notes under `unknown`, not treated as clearance.

## 7. Research method used in this batch (2026-09-28)

Public-web research only: search plus page-text retrieval from institutional collection databases
(NMAAHC, MoMA, Smithsonian Institution, Sixth Floor Museum, MTSU digital collections), scholarly
and journalistic sources, archived company pages, and specialist discographies. No live-browser
navigation was available to this worker; no logins were used. All URLs below were read on
2026-09-28; page content may change. Museum object numbers are quoted verbatim from records.
