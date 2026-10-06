# CultureTechLens Public API — Design Spec

**CULTURETECHLENS** · "Culture, Clearly Seen." · Black Cultural Intelligence
**Status:** DESIGN SPEC — nothing here is deployed until William approves it.
**Date:** October 5, 2026
**Author:** CultureTechLens (internal design document)

> Cite as: CultureTechLens, "Public API Design Spec," October 2026. Source: CultureTechLens.

---

## 0. What this is

This spec designs the machine-readable layer over CTL's two crown assets:

- The **1,441-entity knowledge graph** (live on culturetechlens.com under `/graph/entities/`)
- The **CultureTechLens Index** (CTL-IDX-003, Edition 2026-10: Artifacts; methodology CTL-IDX-001 v1.1)

No servers are provisioned by this document. No accounts created. This is the design; §5 specifies the Phase 1 build that ships on the existing static site.

---

## 1. Endpoint map (REST)

Base URL (Phase 1, static): `https://culturetechlens.com/api/v1/`
Base URL (Phase 2, live server — proposed): `https://api.culturetechlens.com/v1/`

All responses are JSON. All responses carry `evidence_grade` fields — see §2.
All responses carry an `attribution` block — see §3.

### 1.1 `GET /v1/entities`

List entities, paginated.

**Example request:**
```
GET /api/v1/entities?limit=2&offset=0
```

**Example response** (fields modeled on the real entity record — see §1.2):
```json
{
  "data": [
    {
      "id": "CTL-E-1000",
      "name": "Englewood Square",
      "type": "place",
      "description": "Opened 2016 on the former Englewood Mall footprint area. Original tenants included Whole Foods, Starbucks, Chipotle, Villa, Oak Street Health; PNC followed. A 2012 city study estimated $127M in annual retail leakage from the area.",
      "evidence_grade": "PROVISIONAL",
      "source_package": "CTL-DR-BCI-001",
      "page_url": "https://culturetechlens.com/graph/entities/ctl-e-1000/"
    }
  ],
  "pagination": { "limit": 2, "offset": 0, "total": 1441 },
  "attribution": { "source": "CultureTechLens", "license": "CC-BY-4.0", "url": "https://culturetechlens.com/how-to-cite-us/" }
}
```

**Query parameters:** `limit` (default 20, max 100), `offset`, `type` (person | place | institution | organization | event | cultural_work | publication | technology | object | movement | archive), `grade` (filter by evidence grade).

### 1.2 `GET /v1/entities/{id}`

One entity, full claim ledger.

**Example request:**
```
GET /api/v1/entities/CTL-E-1000
```

**Example response** — built from the real public record for Englewood Square
(live at https://culturetechlens.com/graph/entities/ctl-e-1000/; claim-grade
structure mirrors the CTL research claim ledgers):
```json
{
  "id": "CTL-E-1000",
  "name": "Englewood Square",
  "type": "place",
  "description": "Opened 2016 on the former Englewood Mall footprint area. Original tenants included Whole Foods, Starbucks, Chipotle, Villa, Oak Street Health; PNC followed. A 2012 city study estimated $127M in annual retail leakage from the area.",
  "evidence_grade": "PROVISIONAL",
  "claims": [
    {
      "claim": "Opened 2016 on the former Englewood Mall footprint area.",
      "evidence_grade": "VERIFIED",
      "sources": [{ "source": "<source record>", "source_type": "secondary" }]
    }
  ],
  "relationships": [],
  "source_package": "CTL-DR-BCI-001",
  "page_url": "https://culturetechlens.com/graph/entities/ctl-e-1000/",
  "attribution": { "source": "CultureTechLens", "license": "CC-BY-4.0", "url": "https://culturetechlens.com/how-to-cite-us/" }
}
```

Notes on field reality: entity pages on the live site carry all five grades
(VERIFIED / SUPPORTED / PROVISIONAL / DISPUTED / UNRESOLVED) across their
claim ledgers, plus a Sources section and a "Trust & evidence" block. The
research-stage entities carry per-claim fields: claim, evidence, source,
source_type, uncertainty, verification_status. The API normalizes
`verification_status` → `evidence_grade` (title-case → uppercase; "Verified"
→ "VERIFIED"). Relationship edges ship with their grade visible; only
VERIFIED edges may be treated as graph-safe, per the standing research rule.

### 1.3 `GET /v1/index/editions`

List Index editions.

**Example request:**
```
GET /api/v1/index/editions
```

**Example response** (real edition record):
```json
{
  "data": [
    {
      "edition_id": "CTL-IDX-003",
      "edition": "2026-10",
      "title": "Artifacts",
      "methodology": "CTL-IDX-001 v1.1",
      "published": "2026-09-28",
      "doi": "10.5281/zenodo.23081630",
      "page_url": "https://culturetechlens.com/research/culturetechlens-index/2026-10-artifacts/",
      "methodology_url": "https://culturetechlens.com/research/culturetechlens-index/methodology/",
      "subjects": 10
    }
  ],
  "attribution": { "source": "CultureTechLens", "license": "CC-BY-4.0", "url": "https://culturetechlens.com/how-to-cite-us/" }
}
```

### 1.4 `GET /v1/index/editions/{edition}/scores`

Full scored table for one edition.

**Example request:**
```
GET /api/v1/index/editions/2026-10/scores
```

**Example response** — real scores from Edition 2026-10 (signal weights:
40% attention / 40% evidence / 20% momentum):
```json
{
  "edition_id": "CTL-IDX-003",
  "edition": "2026-10",
  "title": "Artifacts",
  "methodology": "CTL-IDX-001 v1.1",
  "weights": { "attention": 0.40, "evidence": 0.40, "momentum": 0.20 },
  "scores": [
    {
      "rank": 1,
      "name": "Cadillac (as cultural object)",
      "score": 78.8,
      "signals": { "attention": 100.0, "evidence": 75.0, "momentum": 44.0 },
      "pageviews_30d": 33922,
      "pageviews_prior_30d": 38520,
      "evidence": { "verified_claims": 5, "provisional_claims": 5, "relationships": 1, "has_object_biography": true },
      "source_package": "CTL-DR-LIFE-001"
    },
    {
      "rank": 9,
      "name": "Afro pick (fist-handle hair pick)",
      "score": 46.2,
      "signals": { "attention": 0.0, "evidence": 100.0, "momentum": 30.9 },
      "pageviews_30d": 106,
      "pageviews_prior_30d": 172,
      "evidence": { "verified_claims": 6, "provisional_claims": 4, "relationships": 4, "has_object_biography": true },
      "source_package": "CTL-DR-LIFE-001"
    }
  ],
  "attribution": { "source": "CultureTechLens", "license": "CC-BY-4.0", "url": "https://culturetechlens.com/how-to-cite-us/" }
}
```

Scores are relative within each edition's set (within-set normalization) —
the spec must say this on the record, per the peer-review packet's question #4.
No edition is recomputed after publication; corrections land as new versions.

### 1.5 `GET /v1/search`

Full-text search across entities and Index subjects.

**Example request:**
```
GET /api/v1/search?q=cadillac
```

**Example response:**
```json
{
  "query": "cadillac",
  "results": [
    {
      "kind": "index_subject",
      "edition": "2026-10",
      "name": "Cadillac (as cultural object)",
      "rank": 1,
      "score": 78.8,
      "evidence_grade": "SUPPORTED",
      "snippet": "The car's documented role as a vessel of Black aspiration and mobility."
    }
  ],
  "total": 1,
  "attribution": { "source": "CultureTechLens", "license": "CC-BY-4.0", "url": "https://culturetechlens.com/how-to-cite-us/" }
}
```

---

## 2. The evidence-grade contract

This is the API's constitutional clause, and it is non-negotiable:

1. **Every response carries evidence grades.** `evidence_grade` is a required field on every entity, claim, score detail, and search result. Grades are never optional, never null.
2. **Grades never stripped.** The open-core endpoints, the keyed tier, and any commercial extract serve the SAME grades. There is no clean-room version without uncertainty. (Commercial red line #2 in the licensing proposal.)
3. **Grade vocabulary (canonical five):** `VERIFIED` · `SUPPORTED` · `PROVISIONAL` · `DISPUTED` · `UNRESOLVED`. The research-stage `REFUTED` and `UNVERIFIABLE` statuses fold to `DISPUTED` and `UNRESOLVED` respectively in API responses, per the portfolio-wide reconciliation rule.
4. **No invented grades.** If a record's grade is unknown, the response says `UNRESOLVED` — never a guessed grade, never omitted.
5. **Index scores carry provenance.** Every score ships with its signal breakdown, pageview counts, evidence counts, source package, and methodology version — so no consumer can launder a ranking into a verdict.

Violating this contract terminates the design. A consumer who wants data
without grades gets nothing.

---

## 3. Auth and rate limits

### 3.1 Free tier — the open core

- **No key required.** `GET` on all endpoints, open to everyone.
- **License:** CC BY 4.0. Attribution required: "Data: CultureTechLens" with link to culturetechlens.com.
- **Rate limit (Phase 2 live server):** 1,000 requests/day per IP, 60/minute. Static Phase 1 has no rate limiting to configure — it inherits the CDN.
- **What it serves:** everything the public site serves — all entities, all Index editions and scores, search.

### 3.2 Keyed tier — commercial and research licenses

- **API key** issued with a Research, Institutional, or Commercial License (see the licensing proposal). Key in `Authorization: Bearer <key>`.
- **What the key buys** (matching the licensing proposal's value ladder — the open data stays identical):
  - **Currency:** keyed endpoints serve new graph tranches and Index editions on a schedule (e.g. weekly), before the monthly public snapshot rebuild
  - **Convenience:** bulk download endpoints (`/v1/bulk/entities`, `/v1/bulk/index`) with custom extracts (by category, grade floor, source package)
  - **Access:** pre-release edition preview for research licensees under embargo terms
  - **Limits:** 100,000 requests/day, 600/minute; bulk downloads excluded from rate counting
- **What the key never buys:** a different dataset. Red lines hold — no sponsored rankings, no stripped grades, no exclusive open core, no implied endorsement. The keyed tier is the same archive, delivered better.
- **Monitoring:** per-key usage logs; abuse (attribution stripping, misrepresentation) triggers the license termination clause.

---

## 4. Build-vs-buy recommendation

### Option A — static JSON snapshots (recommended Phase 1)

- **What:** generated `.json` files committed into the site build, served from `https://culturetechlens.com/api/v1/`.
- **Cost:** $0. Build time: one script, one deploy — the existing `build-site.py` pipeline plus the manual Cloudflare upload William already runs.
- **Constraints:** no live queries (search = a prebuilt index file), no per-key auth, no rate limits beyond the CDN, data refreshes on deploy cadence (monthly Index drumbeat).
- **Fit:** perfect for the open core. The open core is CC BY 4.0 and public by design — it needs no auth, no keys, no server.

### Option B — live API server

- **What:** a small service (e.g. Cloudflare Workers, Fly.io, or a managed VPS) with routing, key management, rate limiting, usage logging, and a query engine over the graph database.
- **Cost:** ~$5–$30/month infrastructure + engineering time to build and maintain + ongoing ops attention (William's scarcest resource). Key issuance and license enforcement are administrative, not just technical.
- **Fit:** required only when the keyed tier launches — i.e., when there are paying licensees whose currency/convenience/access needs justify a server. Until then it's an expense with no customer.

### Recommendation — the phased path

1. **Phase 1 (now): static JSON snapshots.** Ship `/api/v1/` on the existing site. Zero cost, zero new infrastructure, deployable in the next package. This makes CTL's data machine-readable and citable TODAY.
2. **Phase 2 (trigger: first keyed-license interest):** a live API server behind `api.culturetechlens.com`, built only when a Research/Institutional/Commercial licensee needs the keyed tier's currency and bulk access. The static files remain the free tier's backbone — the server never becomes the only door.
3. **Phase 3 (trigger: scale):** full query engine, webhooks for new editions, SDKs.

The phased path respects the standing rule: the open core never gets fenced,
and the server never gets built before the customer exists.

---

## 5. Phase 1 deliverable spec — the static files

### 5.1 Files to generate

| File | Contents | Source |
|---|---|---|
| `/api/v1/entities.json` | All 1,441 entities: id, name, type, description, evidence_grade, source_package, claims (claim + grade + sources), relationships (subject/object/type/grade), page_url | Research `entities.json` packages + entity page records |
| `/api/v1/index-editions.json` | All Index editions: edition_id, edition, title, methodology version, published date, DOI, subjects | `programs/culturetechlens-index/editions/*/` |
| `/api/v1/index-scores.json` | Per-edition scored tables: rank, name, score, signal breakdown, pageviews, evidence counts, source package | `index-scores.csv` per edition |
| `/api/v1/search-index.json` | Prebuilt search index: name, kind (entity/index_subject), id or edition, snippet, grade | Derived from the two files above |
| `/api/v1/meta.json` | API metadata: version `1.0.0-phase1`, generated timestamp, entity count, edition count, license, citation block, changelog | Generated at build time |

### 5.2 Schema notes

- `entities.json`: array of entity objects per §1.2. One object per entity. Sorted by `id` (`CTL-E-0001` … `CTL-E-1441`).
- `index-scores.json`: object keyed by edition (`"2026-10"`), each value the per-edition record per §1.4.
- Every file carries a top-level `attribution` block and a `generated` timestamp.
- Evidence grades: uppercase five-grade vocabulary only; research-stage title-case statuses normalized (`"Verified"` → `"VERIFIED"`).
- Size estimate: entities.json ~3–8 MB uncompressed (1,441 entities with claim ledgers). Acceptable for a static file on a CDN.

### 5.3 Where they live

- Generated into `~/workspace/culturetechlens/website/build/api/v1/` by a new build step in `build-site.py` (or a standalone generator script, `build-api.py`, run before packaging).
- Served at `https://culturetechlens.com/api/v1/*.json` after the next deploy ZIP.
- Documented at a new site page `/api/` (human-readable endpoint map + the evidence-grade contract + citation guidance + keyed-tier "coming when licensees arrive" note).
- Versioned by date: Phase 1 snapshots carry their `generated` date; breaking schema changes bump `/api/v2/` — old versions stay live (William's "don't delete anything" rule).

### 5.4 Build script requirements

- Reads the research `entities.json` packages and the Index `index-scores.csv` files — never hand-edits.
- Validates: every entity has `id`, `name`, `evidence_grade`; every grade in the five-grade vocabulary; no `id` collisions; every Index score carries its signal breakdown.
- Fails loudly on validation errors — never ships a partial snapshot.

---

## 6. Open questions for William

1. Does the free tier need any registration at all, or is it fully anonymous (spec says anonymous)?
2. Should the Phase 1 `/api/` docs page go live with the next deploy, or wait until the static files land in a later package?
3. Bulk-download format for the keyed tier: JSONL, Parquet, or both?
4. Who holds the key-issuance pen — William personally, or the future independent board?

---

*Design only. William decides. — Prepared October 5, 2026.*
