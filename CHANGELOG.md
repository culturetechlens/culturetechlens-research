# CultureTechLens Research Repository Changelog

## October 2026

### Corpus deposit and citation infrastructure — October 24, 2026

The corpus the website has always pointed to is now actually here. A link audit of culturetechlens.com (2026-10-24) found all 49 per-item GitHub source links returning 404 — the site linked to `research-briefs/`, `research-dossiers/`, and `research/` folders that did not exist in this repository. They do now:

- `research-briefs/` — 26 research briefs in their governed packages (full text, claim ledgers, entities, relationships, sources, red-team, gaps), with a section index. CTL-RB-MUS-000006 is a deposit note only: the brief is a completed draft pending founder publication approval, and its package is not disclosed until publication.
- `research-dossiers/` — all 9 dossiers in their governed packages.
- `research/` — the 14 flagship Deep Research packages (CTL-DR series). The pre-existing `RESEARCH/` (Index record, Sports lane) is untouched.
- Text and data only. Photographs stay on culturetechlens.com; each package's `visuals.md` carries the per-image provenance and rights record.

Citation infrastructure added the same day: `CITATION.cff` (powers GitHub's "Cite this repository" widget), and a `citation/` folder — BibTeX, CodeMeta, a corpus manifest (CSV + JSON, one row per item), a Dublin Core collection record, and suggested LCSH headings. Staged packs, not submitted anywhere: `wiki/` (Wikidata statement sheet for Q141705779; a Wikipedia draft with an honest notability self-assessment) and `huggingface/` (a ready-to-push dataset pack carrying the Knowledge Graph Public Edition data). Brand furniture added under `assets/brand/` (Cornerstone wordmark header; a social-preview image awaiting a web-UI upload). Repository topics set. All 49 previously dead links re-checked after the deposit: HTTP 200.


### Sports lane dossiers — October 7, 2026

Five research dossiers for the Sports lane ("The Black Athletic Record") added under `RESEARCH/sports-lane/`:

- `01-chicago-american-giants-dossier.md` — the Chicago American Giants: Rube Foster, the Negro National League, and Black baseball's Chicago dynasty
- `02-nineties-bulls-dossier.md` — the 1990s Bulls as global Black cultural export
- `03-chicago-sky-dossier.md` — the Chicago Sky and the economics of the WNBA
- `04-jackie-robinson-chicago-press-dossier.md` — Jackie Robinson's Chicago press story: the *Chicago Defender* as actor in baseball's integration
- `05-black-quarterbacks-dossier.md` — Black quarterbacks' desegregation, from Fritz Pollard to Super Bowl LVII

Each dossier is evidence-graded throughout (VERIFIED / SUPPORTED / PROVISIONAL / DISPUTED / UNRESOLVED) with named sources, a Chicago connection, image notes with license status, and a gaps section stating what could not be verified. Lane README at `RESEARCH/sports-lane/README.md`.

**Status: DRAFT.** Research foundations, not publications. CC BY 4.0.

### Visual assets — October 5, 2026

Shareable visual assets added under `visuals/` (93 PNGs, CC BY 4.0, all original programmatic renders — no AI faces, no stock imagery):

- `visuals/audience-pack-2026-10-05/` — 13 social cards: CTL 10 Index leaderboard and data-story graphics, Clear Ear Award shortlist, quote cards, archive promos, working-paper promos; includes manifest and re-runnable build script.
- `visuals/templates-2026-10-05/` — 16 cards: reusable monthly Index announcement template set, 10-slide Black Memory Emergency carousel, Clear Ear Award countdown set; includes manifests and build scripts.
- `visuals/true-size-of-africa-2026-10-05/` — "True Size of Africa" graphic (11 countries to true relative scale inside 30.37M km²; UN/FAO-sourced areas).
- `visuals/african-flags-2026-10-05/` — 55 African flags + diaspora-strip composite banner; per-flag accuracy notes in manifest.
- `visuals/educators-2026-10-05/` — 7 classroom visuals: lesson hook cards + evidence-grades poster.
- `visuals/README.md` — collection guide, licensing, and honesty notes (flag approximations, data sources).

### Content expansion — October 5, 2026

Published research and program records added to the public repository:

- `papers/` — metadata for all four Zenodo deposits: the CTL Index Edition 2026-10 (DOI 10.5281/zenodo.23081630) and the three working papers (The Black Memory Emergency, Who Controls the Story?, Black Technology; DOIs 10.5281/zenodo.23173585, 10.5281/zenodo.23173917, 10.5281/zenodo.23173962). Open access, CC BY 4.0; full texts live on Zenodo.
- `RESEARCH/index/` — CTL-IDX-001 methodology v1.1 (2026-09-28) plus Edition 2026-10 raw scores CSV (10 subjects, composite and component scores, 30-day pageviews).
- `docs/` — operational transparency documents: API design spec and Index promotion playbook (both 2026-10-05).

## September 2026

### Version 1.0

Initial public research repository established.

Initial release includes:

- research methodology;
- citation guide;
- source-register structure;
- research-project guidance;
- data guidance;
- correction policy;
- public repository README.

**Methodology:** Version 1.0  
**Publication month:** September 2026
