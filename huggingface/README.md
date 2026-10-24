---
license: cc-by-4.0
language:
  - en
pretty_name: "CultureTechLens Research Corpus"
tags:
  - black-culture
  - chicago
  - knowledge-graph
  - archives
  - cultural-heritage
---

# CultureTechLens Research Corpus

CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

**CultureTechLens NFP** is a Chicago 501(c)(3) building Black cultural intelligence: evidence-graded research on Black cultural history in which every claim carries its grade (VERIFIED / SUPPORTED / PROVISIONAL / DISPUTED / UNRESOLVED), its sources, and a public corrections record.

This dataset packages the public corpus for machine use:

| Path | Contents |
|---|---|
| `data/entities.json` | Knowledge Graph Public Edition (2026-10-06): 2,822 entities, full records with evidence grades |
| `data/relationships.json` | The same edition: 4,500 relationships with evidence and grades |
| `data/PROVENANCE.md` | Provenance, checksums, and which ledger this snapshot is (and is not) |
| Corpus manifest | One row per corpus item — in the GitHub repository at `citation/manifest.csv` (single source of truth; copied into this dataset at publish — see `PUBLISH.md`) |

## The corpus behind the data

14 flagship Deep Research packages, 26 research briefs, and 9 dossiers — Bronzeville, the Black press, Chess Records' Chicago, 63rd Street, gospel and house music, Black technology, the Black memory emergency — published at [culturetechlens.com](https://culturetechlens.com) and deposited in the [public research repository](https://github.com/culturetechlens/culturetechlens-research).

## How to cite

```bibtex
@misc{culturetechlens_kg_public_2026,
  author = {Maxey, William and {CultureTechLens NFP}},
  title  = {CTL Black Cultural Knowledge Graph — Public Edition},
  year   = {2026},
  doi    = {10.5281/zenodo.23253532},
  url    = {https://doi.org/10.5281/zenodo.23253532},
  note   = {Public snapshot, 2026-10-06: 2,822 entities and 4,500 relationships, every record carrying its evidence grade. Concept DOI for the graph series: 10.5281/zenodo.23403147.}
}

@misc{culturetechlens_index_2026,
  author = {Maxey, William and {CultureTechLens NFP}},
  title  = {CultureTechLens Index, Edition 2026-10: Artifacts},
  year   = {2026},
  doi    = {10.5281/zenodo.23081630},
  url    = {https://doi.org/10.5281/zenodo.23081630}
}
```

Citation forms for humans, the corpus manifest, and the Dublin Core record live in the repository's `citation/` folder. How to cite us, in one place: [culturetechlens.com/cite](https://culturetechlens.com/cite/).

## License

Content and data: **CC BY 4.0**. Code: MIT (in the GitHub repository).

---

*CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence · Source: CultureTechLens*
