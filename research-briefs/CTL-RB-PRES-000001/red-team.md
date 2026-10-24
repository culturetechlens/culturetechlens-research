# Red-Team Review — CTL-RB-PRES-000001: "Who Preserves Black Chicago?"

> CULTURETECHLENS · Culture, Clearly Seen. · Black Cultural Intelligence
> Version 0.1 (Research) · 2026-09-28
> This document records the adversarial review of the brief **before** structured data was derived. Corrections applied during red-teaming are listed below; unresolved items remain flagged in the brief and claim ledger.

## 1. Corrections applied during red-teaming

1. **Black-press displacement framing (corrected).** Earlier drafts said "the two largest Black-press archives rooted in Chicago have both been displaced" / "two greatest Black-press archives displaced." Red-team verdict: this overstates equivalence. The JPC archive genuinely left Chicago (verified). The Abbott-Sengstacke *family* papers never left Chicago — they were kept here by donor choice. The Defender's *corporate/operational* archive is a separate, unresolved question. The brief now says: "Chicago's Black-press heritage has been displaced or left incomplete" with the three archival components distinguished (JPC displaced; founding-family papers retained; business archives unresolved).
2. **Institution count (corrected).** Draft said "~24 institutions" while also quoting the BMRC video's "26 archives, libraries and museums." Corrected to "roughly two dozen institutions" to avoid false precision.
3. **DuSable access attribution (strengthened).** Draft cited only a February 2025 podcast interview. Red-team found and added the 2018 Hamilton Institute Reading Room announcement (appointment-only, Tue–Sat) as corroborating evidence. Still graded SUPPORTED (no primary policy page located) — not VERIFIED.
4. **Newberry access (upgraded).** Draft stated "Reading rooms free with registration" without a firm source. Red-team verified against newberry.org's own Quick Guide (free reader account; free reader card issued at registration; reading-room hours). Upgraded to VERIFIED.
5. **Post-cutoff events (removed).** The Obama Presidential Center's 2026 opening with Gates's JPC-image frieze was removed from the timeline/events during an earlier edit pass — post–2026-09-28 completions must not be described as completed facts.

## 2. Claims that could not be verified (remain flagged)

- **Defender corporate-archive custodianship (C066, UNRESOLVED).** The paper's own business/operational archives after the July 2019 print shutdown are unaccounted for. The brief explicitly distinguishes this from the Abbott-Sengstacke family papers. Do not let future versions merge them.
- **Rebuild research-access policy (C053, UNRESOLVED).** Holdings are well-documented; the stated policy under which researchers may use them is not.
- **Shorefront day-to-day access terms (C048, UNRESOLVED).** NPR documents the archive's existence, founder, site, and contents; not its researcher-facing access policy.
- **Collection-level extents for ~11 BMRC members (C074, UNRESOLVED).** DePaul, Loyola, IIT, Roosevelt, Dominican, North Park, Northern Illinois universities; Oak Park Public Library; the Art Institute of Chicago; Northwestern — covered only at portal level.
- **Processing-backlog sizes** at Harsh, DuSable, and SSAC (mentioned in analysis; unquantified).
- **JPC art collection disposition** (separate from the photo archive).
- **Defender pre-2019 photo morgue** — survival and location unknown.

## 3. Disputed claim

- **DuSable collection size (C013, DISPUTED).** Wikipedia: 13,000 artifacts. Wintrust profile: 15,000+ items. The brief keeps both visible and does not reconcile them. The claim ledger marks DISPUTED; the brief's Data section notes the discrepancy as unresolved.

## 4. Source-quality assessment

| Source class | Count | Assessment |
|---|---|---|
| Primary (institution pages, finding aids, official records) | 16 | Strong on access policies (Harsh, CHM, Cook County, BMRC, Newberry, AAA survey, NMAAHC). Weakest point: no primary access-policy page located for DuSable archives, UIC, Rebuild, Shorefront. |
| Reputable secondary | 15 | NPR, UChicago News, E&P, Hyperallergic/Art Newspaper, City landmark report are solid. Podcast interview (DuSable) and 2018 announcement are weaker — graded SUPPORTED. |
| Excluded | — | Social-media-only announcements, unsourced aggregators, AI summaries were excluded. This may omit real but poorly documented holdings (church, funeral-home, fraternal records) — noted in Limitations. |

**Bias checks.**
- The evidence base over-represents large, well-documented institutions (CPL, UChicago, CHM) because their published records are richest. Community archives are covered primarily through journalism (NPR for Shorefront), not their own published policies — a visibility gap, not necessarily a quality gap.
- The brief's central argument (access fragility) is driven by the single most striking verified fact — the Harsh closure — which risks overweighting one institution. The argument is corroborated by Cook County (closed), SSAC (renovation), CHM (finding aids offline), and appointment-only policies elsewhere, but the Harsh closure is time-sensitive and may resolve.
- No private or family collection was treated as institutionally custodial; scope discipline held.

## 5. Video/copyright review

- **Three embedded videos** (BMRC explainer; BMRC Archives Awareness Panel; CPL "Beyond Borders in the Archives") are from official institutional channels with documented IDs, descriptions, authority, timestamps, embed status, and publication-time recheck plans (see `visuals.md`). **Transcripts were NOT reviewed** — only titles/descriptions were retrievable. The brief does not claim transcripts were watched; `visuals.md` states the transcript gap explicitly. Under the assignment's rule, the videos are "not fully cleared" for transcript-dependent claims; all video-derived claims in the ledger are limited to what the descriptions state.
- **Photos:** two candidates evaluated and **excluded** pending exact per-file license verification. No rights-uncleared files are included. Build-at-publish graphics (4) are original constructions from verified data — no third-party rights issues.

## 6. Duplicates and contradictions check

- No duplicate entities in `entities.json` (32 unique IDs checked).
- The BMRC member count appears as "20+" (membership sources) and "26" (own video); both are attributed and the brief uses "roughly two dozen" — no silent reconciliation.
- Harsh founding chronology (1932 → 1970 → 1975 → 1998–99) is consistent across the brief's sections.
- JPC transfer facts (2019 auction $30M; July 28, 2022 transfer; joint ownership; DC housing; Getty $30M) are stated identically in Evidence, Key Findings, Data, and People/Events sections.
- Relationships: `relationships.json` contains 21 VERIFIED-only edges with provenance; 5 SUPPORTED candidates are kept in a separately labeled `candidate_edges` array, per the brief's rule.

## 7. Geographic-scope check

- Scope: Chicago, Illinois, 19th century–present. Evanston (Shorefront) is included with explicit justification (BMRC member documenting Chicagoland Black life) — not scope creep.
- Out-of-Chicago custodians (NMAAHC, Getty) appear only as custodial endpoints for the JPC archive, per the brief's exclusion rule — a documented loss, not an inventoried collection.
- All place addresses are public institutions or publicly documented sites. **Privacy audit: PASSED** — no private collection locations, private interiors, private addresses, or unauthorized identifiable private individuals anywhere in the brief, ledger, entities, relationships, visuals, sources, or this review. The Lula B. Sherman Church basement (Shorefront) and the Burroughs home (3806 S. Michigan Ave.) are the archive's own publicly stated locations in reputable coverage. Living persons are named only in public institutional roles (Irmer, Gates, Robinson, Bell, Hearn, Cook).

## 8. Residual risks for the public-facing version

1. **Time decay.** The Harsh "targeting November" reopening is the brief's most load-bearing time-sensitive claim. Recheck before any republication.
2. **The JPC displacement framing** should not harden into "Chicago lost everything" — the JPC *books/periodicals* remain at Rebuild's Stony Island Arts Bank in Chicago, and the Defender family papers remain at CPL. The brief states this; future cuts must not drop it.
3. **Access-policy grades** for DuSable, UIC, Rebuild, and Shorefront remain the weakest VERIFIED surface. Field verification is item (1) of Further Research.
4. **The ~$60M JPC figure** (purchase $30M + Getty commitment $30M) could be misread as one transaction; the brief keeps them separate — hold that.
