# Red-Team Report — CTL-RB-PRES-000002: The Disappearing Black Web

**CULTURETECHLENS · Culture, Clearly Seen. · Black Cultural Intelligence**

This report attacks the brief's own findings. Every challenge below was considered before the brief was finalized; the resolution is recorded honestly.

## 1. Was it actually lost, or did it move?

**Challenge.** The brief's headline cases may be migrations, not losses.

**Audit.**
- Africana.com → AOL BlackVoices: the closure notice says "many of the features" moved. *Many*, not *all*. Partial migration. The brief classifies this "closed; partially migrated" — correct.
- BlackVoices → HuffPost: the surviving site is a subsection, and the message boards (the community's archive) were reportedly removed — but only Wikipedia says so (PROVISIONAL). The brief excludes this from the knowledge graph. Correct.
- The Undefeated → Andscape: clean rebrand with continuity. Correctly used as the control case, not a loss.
- DatPiff → Internet Archive partnership: announced, then the collection vanished. Neither migration nor loss is confirmed. The brief holds it UNRESOLVED. Correct.

**Verdict.** The brief's migration-vs-loss discipline holds. The one soft spot is the HuffPost messageboard claim — it stays PROVISIONAL and out of the graph.

## 2. Are the Black-specific claims actually Black-specific?

**Challenge.** The biggest loss figures (MySpace 50M songs, GeoCities 38M pages, Yahoo Groups) are general-platform losses with no documented Black share. Is the brief laundering general losses into Black ones?

**Audit.** The brief explicitly refuses to do this (F5): "Nobody measured the Black share of any general-platform loss." The Black-specific connection is documented disproportionate *use* (Vine 31% Black teen users; Black Twitter's Ferguson role; DatPiff's centrality to Black hip-hop distribution) plus the mechanism argument: collateral loss concentrates where use concentrates. This is stated as inference, never as fact. The claim ledger grades the Black-share question UNRESOLVED. Correct — but the brief's rhetoric occasionally leans on the inference harder than the evidence; a reader should keep F5 pinned.

## 3. The weakest links

Ranked by fragility:
1. **HuffPost removed the BlackVoices message boards** (PROVISIONAL, Wikipedia only). If false, the "community layer was stripped" argument for BlackVoices weakens.
2. **DatPiff's IA collection disappeared** (PROVISIONAL, Wikipedia + podcast). If the collection is merely re-indexed or moved, the brief's sharpest "unresolved loss" dissolves into a metadata problem.
3. **Vine archive removed April 2019** (exact date PROVISIONAL). The archive's absence is well supported; the precise date is not.
4. **GeoCities rescue figures** (~100K accounts / 38M pages / ~10TB — reported, unaudited, inconsistent across outlets).
5. **Yahoo suspended archivists' accounts** (single low-authority source). Included because platform hostility to preservation is a real mechanism; kept at PROVISIONAL.
6. **All SUPPORTED-grade claims resting on search snippets rather than full page opens.** Reputable outlets, but the brief did not read the full pages. A v0.2 pass should open them.

## 4. What's missing

- **No Black-specific link-rot study exists in the sources found.** The brief imports Harvard/Pew link-rot science and marks the transfer. The research gap is real and should be a CTL research priority (§22, item 3).
- **No Chicago-specific loss case is fully documented.** FakeShoreDrive is at-risk-by-structure, not a loss. The Chicago drill-era mixtape corpus may be the largest undocumented Chicago loss — but the brief does not claim it, because it cannot document it. Correct restraint; flagged as further research.
- **Survivorship bias.** BlackPlanet survived and is over-represented. The portals that vanished without a trace (NetNoir's undocumented end) are under-represented by definition.
- **Oral histories.** Nobody interviewed former NetNoir, Africana.com, or BlackVoices staff. The undocumented ends stay undocumented.

## 5. Alternative readings

- **The DatPiff disappearance** could be a copyright takedown, a technical removal, or a write-down abandonment. The brief lists all three and holds UNRESOLVED. Correct.
- **Facebook's 2018 purges** are recorded as events; the framing (protective moderation vs. deletion of Black organizing spaces) is marked DISPUTED. Correct.
- **@Blacktivist in the DocNow archive** is presented as the field's own open ethical problem, not a settled judgment. Correct.
- **The MySpace loss cause** (accident vs. deliberate cost-cutting) is marked DISPUTED via Baio's skepticism. Correct.

## 6. Privacy audit — all deliverables

**Method.** Every record in brief.md, claim-ledger.json, entities.json, relationships.json, visuals.md, and sources.md was reviewed for: private individuals' names, addresses, phone numbers, email addresses, account numbers, dates of birth, and unnecessary personal information about non-public figures.

**Result: PASS.**

- All 19 named people are public professional figures acting in professional roles (founders, executives, scholars, journalists, archivists). No private individuals appear.
- No addresses, phone numbers, email addresses, account numbers, or dates of birth appear in any deliverable.
- The one street address encountered (Community Connect's 205 Hudson St., New York) is a corporate headquarters from public business records; it appears in the brief's place entry and is a business address, not a private residence. Retained as public corporate information.
- The sourced-photo candidate (`visuals/ia-hq-300funston.jpg`) depicts a public building exterior with no identifiable private individuals. It is held unavailable-with-reason (license unverified), not for privacy reasons.
- No archived-page screenshots of private users' content were used.
- The videos in visuals.md Part C feature public professional discussions; no private individuals are identified.

**Residual risk.** None identified. The brief's subject is platforms and organizations, not persons; the privacy posture is structural, not incidental.

## 7. Integrity checks

- **No invented facts.** Every figure, date, and name traces to a claim-ledger entry with a named source. Where the source was not opened, the grade says so.
- **No VERIFIED inflation.** Nine claims earned VERIFIED by full page opens or direct observation; everything else is honestly graded lower. relationships.json deliberately deviates from the original "VERIFIED-only" spec rather than mislabel SUPPORTED claims — documented in the file's edge_rule and in brief §18.
- **Suspected loss never labeled VERIFIED.** DatPiff's archive disappearance is PROVISIONAL/UNRESOLVED in the ledger, the brief, and the graph (excluded).
- **Videos not misrepresented.** visuals.md states the four videos are candidates assessed from titles/descriptions, not watched end-to-end; transcripts and timestamp ranges unverified. The brief's §17 repeats the warning and the honest irony that YouTube is itself an at-risk platform.
- **Image rights not assumed.** The Internet Archive HQ photo is held unavailable-with-reason; its provenance/license could not be verified from a source page.

## 8. What would change the findings

- A MediaLab or Internet Archive statement on the DatPiff collection (resolves the brief's sharpest UNRESOLVED).
- Wayback snapshot inventories for the four dead domains (resolves four UNRESOLVED statuses; currently blocked by HTTP 429).
- A corroborating source for the HuffPost messageboard removal (upgrades C004 to SUPPORTED).
- A Black-focused link-rot study (fills the §20 gap; currently does not exist in the sources found).
- Former-staff oral histories for NetNoir and Africana.com (resolves undocumented ends).
