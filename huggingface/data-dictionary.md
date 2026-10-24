CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# Data Dictionary — CultureTechLens Hugging Face Pack

Cite as: CultureTechLens, "Data Dictionary — CultureTechLens Hugging Face Pack," October 24, 2026.
Source: CultureTechLens

## `data/entities.json` — one record per entity (2,822)

| Field | Meaning |
|---|---|
| `id` | CTL entity identifier (CTL-E-…) |
| `name` | Canonical name |
| `aliases` | Alternate names and spellings |
| `type` / `subtype` | Entity type (person, place, institution, work, event…) and its subtype |
| `description` | Short evidence-based description |
| `era` | Period the entity belongs to |
| `project_ids` | CTL research packages the entity appears in |
| `sources` | Sources behind the record |
| `verification` | Evidence grade: VERIFIED / SUPPORTED / PROVISIONAL / DISPUTED / UNRESOLVED |

## `data/relationships.json` — one record per relationship (4,500)

| Field | Meaning |
|---|---|
| `from` / `to` | Entity IDs the relationship connects |
| `type` | Relationship type |
| `source` | The source the relationship rests on |
| `evidence` | The evidence note for the edge |
| `verification` | Evidence grade (same controlled vocabulary) |

## Corpus manifest (`citation/manifest.csv` in the GitHub repository; copied in at publish)

| Column | Meaning |
|---|---|
| `id` | CTL ID (CTL-RB-…, CTL-RD-…, CTL-DR-…) or, for deposits, the DOI |
| `title` | Item title |
| `type` | Research brief · Research dossier · Flagship research package · Index record · Sports lane dossier · Working paper |
| `date` | Research/publication date (ISO) |
| `status` | Completion and publication status, stated plainly (drafts are labeled DRAFT) |
| `site_url` | Canonical culturetechlens.com URL, where one exists |
| `doi` / `doi_basis` | Zenodo DOI where one is on record, and the record it rests on. Blank means none — never inferred |
| `repo_path` | Path inside the GitHub research repository |
| `license` | CC BY 4.0 |

Unknowns stay labeled: a grade of UNRESOLVED, an empty DOI, or a DRAFT status is a statement about the record, not a gap in it.

---

*CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence*
