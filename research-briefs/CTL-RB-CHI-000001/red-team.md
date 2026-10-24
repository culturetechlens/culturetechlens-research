# CTL-RB-CHI-000001 — Red Team Report
**"Why 63rd Street Mattered" · 2026-09-28**

Attempt-to-disprove pass over this brief. Verdicts below; unresolved items are preserved as gaps, not patched.

## 1. Unsupported claims — checked
- **"Transit made commerce" (C003):** Supported by chicago-l.org for 63rd & Halsted specifically. NOT asserted for the Woodlawn strip or Chicago Lawn. Verdict: PASS with scope noted.
- **Grade lift "second busiest" PROVISIONAL→SUPPORTED (C002):** Three independent corroborators now, two of them City of Chicago designation reports. But the *original metric and primary source remain untraced* — the brief says this explicitly (§20, §08). Verdict: PASS — the lift is to SUPPORTED, not VERIFIED, and the missing root is flagged.
- **Sears 1934 date in video description (Sweet Old America):** The rejected video asserts "Sears opened in 1934 with full air conditioning" — matching one side of the DISPUTED construction-date pair. It does not resolve the dispute. Verdict: PASS — kept as DISPUTED.

## 2. Circular sourcing — checked
- chicago-l.org is cited for both the mall history (C004/C005) and transit displacement (C003). chicago-l.org is the *sibling's own recommended corroborator*, not a sibling source — no circularity with CTL-DR-PLACE-001. The landmark designation reports are independent government documents. Verdict: PASS.
- LISC 2005 appears both as sibling source and in this brief's new retrieval — counted as one corroborator, not two. Verdict: PASS (noted in C002 evidence).

## 3. Myths-as-facts — checked
- "Second-busiest shopping district": upgraded but not mythologized; root untraced, stated. PASS.
- "People didn't leave; stores left" (rejected video's framing): not in the brief. PASS.
- "1968 white flight caused decline": brief explicitly refuses single-cause explanations (§09, §19). PASS.
- The Congressional Record's celebratory language ("voice during the civil rights movement") is attributed, not stated as independent fact. PASS.

## 4. Date conflicts — checked
- Pedestrian mall: sibling UNRESOLVED (1969 vs ~1973); chicago-l.org gives Daley's dedication 1969 → brief treats 1969 as VERIFIED dedication, reopening/end date UNRESOLVED. Coherent. PASS.
- WVON launch: sibling + Congressional Record both April 1, 1963. No conflict. PASS.
- Sears 1929 vs 1934: preserved as DISPUTED. PASS.

## 5. Name ambiguity — checked
- McKie Fitzhugh vs "McKee Fitzhugh" (Congressional Record roster): noted in C008. PASS.
- "The Woodlawn Organization" naming: sibling already corrected; brief uses the corrected form. PASS.
- "63rd Street" vs "the corridor": defined in §05 before use. PASS.

## 6. Geographic errors — checked
- Trianon at 6201 S. Cottage Grove is one block off 63rd; brief states the address (§13, caption V3) — within the corridor definition (§05). PASS.
- WVON at 3350 S. Kedzie is NOT on 63rd; the brief does not claim a 63rd studio address — it claims a media *function* via WVON's service to the corridor and Fitzhugh's employment. PASS.
- Chicago Lawn fenced off from the decline narrative (§07 finding 7, §09). PASS.

## 7. Anachronisms — checked
- No function is projected outside its dated evidence range. The 1963–1997 "unravelling" window overlaps "civic-media production 1963–present" — intentional overlap, functions coexisted; stated in G3 rendering notes. PASS.
- "Black Belt southern edge 1920–1930" not extended past the documented window. PASS.

## 8. Causation without evidence — checked
- Dan Ryan → decline: not claimed (follows sibling). PASS.
- Mall failure "exacerbated" decline: attributed to chicago-l.org, flagged as judgment not fact (C005 notes). PASS.
- 1997 demolition → blocked redevelopment: presented as community leaders' stated rationale, retrospective judgment graded PROVISIONAL. PASS.
- One soft spot: "the entertainment function outlived the streetcar era because it was sustained by Black migration demand" (§09 analysis) — this is *inference*, stated as analysis, not graded as a claim. Acceptable but flag for the parent: it's the brief's interpretive leap. Verdict: PASS with flag.

## 9. Selection / celebrity / survivorship bias — checked
- Performer names (Jamal, Parker, Davis) appear but are anchored to *recorded output on the corridor* (Jamal's Pershing recordings) and Black ownership — not pure celebrity name-dropping. PASS.
- Entertainment function rests on 15 Defender-verified clubs, not just famous rooms. PASS.
- Deliberate counterweight: V4/V5 NARA photos center ordinary 1973 riders and the street itself against nostalgia imagery. PASS.
- The "re-anchoring" section lists verified investments (Kennedy-King, WPNB approval) with status qualifiers — not boosterism. PASS.

## 10. Missing women / missing ordinary people / missing institutions — checked
- Women: inherited gap. The brief carries it forward in §20 and §22 (church anniversary books, Defender social pages) rather than papering over it. PASS (preserved, not filled).
- Ordinary people: addressed via V4/V5 visuals and the explicit §21 limitation on the experience layer (beauty/barbershop, congregational life). PASS.
- Missing institutions: mosques (no mosque on 63rd proper verified — stated as gap not absence); Latino Chicago Lawn communities (thin, noted); small congregations (provisional). PASS.

## 11. Weak visual provenance — checked
- All 5 archival images: license verified on each Commons file page (4× PD-old, 1× PD-postcard 1924); both NARA images PD-federal; all downloaded into visuals/. PASS.
- Rejected: Getty/Chicago History Museum images (rights unclear), nostalgia-channel video (provenance), colorized-footage channels. PASS.
- Vd1/Vd2 caveats recorded (not 63rd-specific; captions must say so). PASS.
- Chicago City Bank building: no cleared image found — represented as data (C019) and landmark-report citation, not as an image. PASS (honest absence).

## 12. Copyright problems — checked
- No images reproduced beyond public-domain downloads. No video downloaded. No newspaper clippings reproduced. Data graphics are original works. PASS.

## 13. Duplicate entities — checked
- PL-HALSTED/PL-COTTAGE/63rd Street corridor: three distinct entities (two nodes + corridor). The first relationships.json edge was self-referential (PL-HALSTED→PL-HALSTED); corrected to corridor→PL-HALSTED. PASS after fix.
- ORG-CCB merges two bank institutions under one id — acceptable for the *function* claim (banking node), with individual buildings as PL-CCB/PL-WPNB. PASS.

## 14. Unresolved-boundary violations — checked
- Sibling's three forbidden wholesale fills: (1) 63rd platting date — not attempted (carried in §20). (2) Defender archives 1915–1975 — not touched; listed as Phase 2. (3) Women business owners — not researched; listed as gap. PASS.

## 15. Residual concerns for the parent
1. **Word count is 3,932** — inside the 1,500–4,000 band but near the ceiling; any parent-requested additions should be offset by cuts.
2. **C021 graded SUPPORTED not VERIFIED** — population figures are "verified as quoted" per sibling but pending Census API re-verification; the brief is more conservative than the sibling here. Deliberate.
3. **§09's migration-demand inference** (flagged in §8 above) is the brief's one analytic leap; it is fenced in "Analysis," not the claim ledger.
4. **§17 was rewritten** after the VISUALS DIRECTIVE — substantive-section word count was re-verified post-edit (3,932). Note: the word-count band covers §§01–22 only; §17 is inside the band. If a parent recounts, expect ~3,930–3,940.
5. **No live-browser verification** of the Congressional Record, designation reports, or chicago-l.org pages was possible (text-fetch only) — a browser-capable agent should directly view these before publication, per the sibling's Phase 2E protocol.

**Red-team verdict: PASS — publishable as a Phase 1 research package with the flagged limitations visible.**
