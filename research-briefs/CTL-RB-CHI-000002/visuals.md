# Visuals — CTL-RB-CHI-000002: The Rise of Bronzeville

**Date:** 2026-09-28
**Rule:** every visual performs an explanatory function for the forces question. Archival images are rights-cleared and downloaded into `visuals/`; data graphics are specified for build at publish (no clearance needed). Nothing decorative. No AI-generated historical scenes.

**Inventory:** 3 sourced archival images · 4 data graphics (build at publish) · 0 unavailable · 2 videos selected.

---

## A. Sourced archival images (downloaded, rights-cleared)

### V-IMG-1 — Wabash Avenue YMCA (anchor-institution force)
- **File:** `visuals/wabash-ymca_cc-bysa-3.0_jameson-2010.jpg` (2998×2172, JPEG)
- **What it shows:** Exterior of the Wabash Avenue YMCA, 3763 S. Wabash Ave., the five-story brick building completed 1913.
- **Why it explains:** Visual anchor for F3 — the pre-existing institutional carrying capacity. This single building hosted the ASNLH founding (1915) and Negro History Week organizing (1926); it is the "migrants arrived into organization, not vacuum" claim made visible.
- **Creator:** Andrew Jameson (Wikimedia Commons user), 2010-08-29. **Source institution:** Wikimedia Commons (own work by contributor).
- **Rights:** CC BY-SA 3.0 — verified via Commons API extmetadata (`LicenseShortName: CC BY-SA 3.0`, `LicenseUrl: https://creativecommons.org/licenses/by-sa/3.0`) and corroborated by NPS.gov's attribution on its Wabash YMCA place page. **Reuse requires attribution + share-alike.**
- **Source URL (file page):** https://commons.wikimedia.org/wiki/File:Wabash_Avenue_YMCA_Chicago_IL.jpg
- **Caption draft:** "The Wabash Avenue YMCA (completed 1913) at 3763 S. Wabash — the anchor institution where Carter G. Woodson founded the Association for the Study of Negro Life and History (1915) and where Negro History Week was organized (1926). Photo: Andrew Jameson, CC BY-SA 3.0, via Wikimedia Commons."
- **Context:** Pair with claim-ledger entries on anchor institutions (F3). Status: **sourced**.

### V-IMG-2 — Overton Hygienic Building (Black-capital force)
- **File:** `visuals/overton-hygienic_cc-bysa-3.0_jameson-2010.jpg` (2784×1530, JPEG)
- **What it shows:** The Overton Hygienic Building, 3619–27 S. State St. (commissioned 1922), headquarters of Anthony Overton's cosmetics/manufacturing empire; also housed Victory Life Insurance and Douglass National Bank.
- **Why it explains:** Visual anchor for F4 — Black capital formation concentrated on the State Street core. The building *is* the "Black-owned 35th–39th & State" claim; it lets the page show, not tell, the honest commercial geography (contrast with the white-developed 47th Street complex, which has no single Black-owned architectural equivalent).
- **Creator:** Andrew Jameson, 2010-08-29. **Source institution:** Wikimedia Commons.
- **Rights:** CC BY-SA 3.0 — verified via Commons API extmetadata. **Reuse requires attribution + share-alike.**
- **Source URL (file page):** https://commons.wikimedia.org/wiki/File:Overton_Hygienic_Building_Chicago_IL.jpg
- **Caption draft:** "The Overton Hygienic Building (1922), 3619–27 S. State — Anthony Overton's headquarters and the architectural signature of the Black-owned commercial core at 35th–39th & State. Photo: Andrew Jameson, CC BY-SA 3.0, via Wikimedia Commons."
- **Context:** Pair with F4 evidence (Binga/Overton/Douglass Bank). Status: **sourced**.

### V-IMG-3 — Eighth Regiment Armory, c. 1915 (civic-institution force)
- **File:** `visuals/eighth-regiment-armory_pd_chicago-daily-news.jpg` (480×380, JPEG)
- **What it shows:** Contemporary exterior view of the newly built Eighth Regiment Armory (3533 S. Giles Ave.) — the first armory built for an African-American regiment ("Fighting 8th").
- **Why it explains:** Shows a second, non-church/non-commercial institutional force: Black civic-military organization *before* the migration peak. It widens "anchor institutions" beyond the usual church/YMCA pair and is genuinely period (c. 1915), unlike the modern photos above.
- **Creator:** Chicago Daily News (glass-negative collection). **Source institution:** Wikimedia Commons (scan of Chicago Daily News photo; DN-006 series).
- **Rights:** **Public domain** — verified via Commons API extmetadata (`LicenseShortName: Public domain`); a pre-1929 published newspaper photograph. No attribution legally required; credit line retained as practice.
- **Source URL (file page):** https://commons.wikimedia.org/wiki/File:Eighth_Regiment_Armory.jpg
- **Caption draft:** "The Eighth Regiment Armory (c. 1915), the first armory built for an African-American regiment — Black civic organization already in place before the Great Migration's peak. Photo: Chicago Daily News, public domain, via Wikimedia Commons."
- **Context:** F3 institutional layer. Low resolution (480×380) — use at modest display size. Status: **sourced**.

**Rights-verification note:** Commons file pages returned HTTP 403 to the page-fetch tool; licenses were verified instead via the Wikimedia Commons API (`imageinfo/extmetadata`) and, for V-IMG-1/2, corroborated by NPS.gov's published CC BY-SA 3.0 attribution. Re-verify at publication.

---

## B. Data graphics (build at publish — no rights clearance needed)

### V-DATA-1 — The demographic engine: Chicago Black population, 1900–1950
- **Type:** bar + line chart (population bars; share-of-city line).
- **Data source:** claim-ledger §16 table (NPS census table; UIC/Chicago Urban League; Encyclopedia of Chicago Demography). Fields: year (1900/1910/1920/1930/1940/1950), population (30150/44103/109458/233903/277731/586598), share (—/2%/4.1%/7%/8%/14%).
- **Rendering notes:** annotate 1910–20 (+148%), 1940–50 (second wave, 277,731→586,598); footnote the 1920 variant (109,894 per EoC Bronzeville entry). Explains F1: the scale of the human influx.
- **Status:** build at publish.

### V-DATA-2 — Forces diagram: how confinement made a cultural center
- **Type:** causal-loop diagram.
- **Nodes/edges:** Great Migration (people + wages) → Confinement complex (covenants/HOLC/violence) → Density (40-block corridor) → Captive markets → {Black-owned business; packed venues; dues-paying institutions} → Cultural output (music, press, gospel, literature) → "Bronzeville" identity (1930/32) → national circulation (Defender) → feedback to migration. Counterforce branch: Depression (1930) → Black bank collapse; Shelley (1948) → confinement unwound → outmigration.
- **Data source:** brief §§07–09 causal model; grades attached per edge (Verified/Supported/interpretive).
- **Rendering notes:** edges labeled with force numbers F1–F7; interpretive edges visually distinguished from evidenced ones. Explains the brief's central thesis (§09).
- **Status:** build at publish.

### V-DATA-3 — Institutional density & ownership map, c. 1928 (peak)
- **Type:** schematic corridor map (not to survey scale; labeled schematic).
- **Data source:** entities.json place records with addresses: Binga Bank/Arcade, Overton Hygienic, Bee Building, Supreme Life (Black-owned, 35th–39th & State — one color); Regal, Savoy, South Center (white-developed 47th/South Parkway — second color); Wabash YMCA, Pilgrim, Ebenezer, Quinn Chapel, Olivet, Phillips, DuSable, Hall Branch (institutions — third color). Corridor outline: 22nd–51st, State to Cottage Grove.
- **Rendering notes:** must visually separate the two commercial geographies (the brief's honesty corrective); boundary disclaimer ("schematic; the Stroll's boundaries are disputed"). Explains F2/F3/F4: where the forces landed.
- **Status:** build at publish.

### V-DATA-4 — Forces timeline, 1844–1950
- **Type:** horizontal timeline with force-coded bands.
- **Data source:** brief §10 timeline table (20 events with grades). Bands: Migration (green), Confinement (red), Institutions (blue), Capital (gold), Culture/Identity (purple), Counterforces (gray).
- **Rendering notes:** show grade per event on hover/footnote; include the 1948 policy break as a visual hinge ("confinement unwound"). Explains sequence — forces compounding, not coinciding.
- **Status:** build at publish.

---

## C. Video

**Policy:** video illustrates only; every claim still needs its claim-ledger source. Descriptions read in full; relevance assessed against the forces question; AI-generated or misattributed content excluded (two candidate documentaries disclosed AI-generated visuals/narration and were rejected). Embed status checked via YouTube oEmbed 2026-09-28 — re-check at publication. Link rot: full identity metadata recorded below.

### VID-1 — "Bronzeville, the Black Metropolis"
- **Channel:** The Language & Life Project (NC State University) — institutional/academic. **Author URL:** https://www.youtube.com/@TheLanguageLifeProject
- **Video ID / URL:** `u6WRG66ZwU0` — https://www.youtube.com/watch?v=u6WRG66ZwU0
- **Upload date:** c. 2017 (search-index metadata; exact date unverified — confirm at publish)
- **Uploader:** The Language & Life Project, NC State (producer of the PBS documentary *Talking Black in America*, 2019)
- **Why selected:** Oral-history interview clip — Harold Lucas on Bronzeville's history. The narration states the brief's exact causal chain: Great Migration → housing covenants confining Black Chicagoans to "a narrow band" → "within the overcrowded area, which came to be known as Bronzeville, arts and culture flourished." Directly illustrates F1 + F2 + the confinement→concentration thesis.
- **Caution:** the description's "twenty thousand African-Americans arrived each day" is an inflated error — the video illustrates; it does not evidence migration volume. Cite the claim-ledger, not the video.
- **Timestamp range:** whole clip (short excerpt; confirm runtime at publish).
- **Embed status:** **embeddable** (oEmbed returned title/author 2026-09-28). Re-check at publication.

### VID-2 — "Goin' to Chicago" (1994)
- **Channel:** California Newsreel — official distributor channel (nonprofit distributor). **Author URL:** https://www.youtube.com/@CaliforniaNewsreel
- **Video ID / URL:** `idRvPi7Z3d4` — https://www.youtube.com/watch?v=idRvPi7Z3d4
- **Upload date:** unverified (channel upload; film released 1994, dir. George King) — confirm at publish
- **Uploader:** California Newsreel (distributor; description links to newsreel.org for the full film/DVD)
- **Why selected:** The canonical documentary of the forces question: Mississippi Delta migrants' oral histories of sharecropping → the journey up Highway 61 → building "a vibrant city-within-a-city of thriving black businesses and civic institutions, proudly referred to as 'Bronzeville'" → the fair-housing struggle → deindustrialization's blow. Covers F1 (push/pull), F2–F4 (the built community), and the counterforces in one arc. Posted by the rights-holding distributor, not a reupload.
- **Timestamp range:** confirm at publish (appears to be a trailer/excerpt; the full 60-minute film is via newsreel.org).
- **Embed status:** **embeddable** (oEmbed returned title/author 2026-09-28). Re-check at publication. If the upload proves to be excerpt-only, cite as link alongside the distributor page.

**Rejected:** "How the Great Migration Built a Secret Chicago Nightlife (Bronzeville, 1941)" — well-sourced stills (FSA/LOC) but unknown-provenance channel, not institutional; "Bronzeville, 1955: The REALITY…" and "Bronzeville, Chicago: The Kitchenette Flats…" — both disclose AI-generated images/narration → excluded per directive.
