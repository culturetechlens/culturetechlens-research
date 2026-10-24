# Visuals — CTL-RB-MUS-000001
*"Why Chicago Became a Gospel Center"*

Visual-first register. Every item records: type, status (`sourced` / `build-at-publish` / `unavailable-with-reason`), creator, date, institution, rights/license, full source URL, caption, and context. Videos follow the CTL Video Directive (official channels only; relevance assessed via title/description; embed never replaces textual evidence).

**Counts:** 2 sourced images · 4 built graphics · 1 unavailable-with-reason · 1 embedded video · 1 reference video link.

---

## Sourced images

### V1 — Dorsey's Pilgrim rehearsal piano (sourced)
- **Type:** museum object photograph (photographer credit per NMAAHC page at publish time)
- **Status:** `sourced`
- **Creator:** The Cable Piano Company (Conover), Chicago — 1930s manufacture
- **Date:** 1930s (object); photograph n.d. (NMAAHC digital asset)
- **Institution:** Smithsonian National Museum of African American History and Culture (NMAAHC), object 2015.134.1a-g
- **Rights/license:** "No Known Copyright Restrictions" (per NMAAHC object record: "Restrictions & Rights — No Known Copyright Restrictions. Proper usage is the responsibility of the user.")
- **Source URL:** https://nmaahc.si.edu/object/nmaahc_2015.134.1a-g
- **Caption:** "The 1930s Conover baby grand Thomas A. Dorsey used as a rehearsal piano at Pilgrim Baptist Church, Chicago. When the congregation bought new instruments, the piano passed to Pastor Junius C. Austin's household, where Dorsey played it on visits. Gift of the Keller family; NMAAHC."
- **Context:** A material witness to the church-music-director institution at the center of the brief. Objects avoid performer publicity-rights questions entirely. One of the few surviving artifacts of Pilgrim's music program after the 2006 fire.

### V2 — Mahalia Jackson, 1962 (sourced)
- **Type:** portrait photograph
- **Status:** `sourced`
- **Creator:** Carl Van Vechten (1880–1964)
- **Date:** April 16, 1962
- **Institution:** Library of Congress, Prints and Photographs Division, Carl Van Vechten Collection (reproduction no. LC-USZ62-91314)
- **Rights/license:** Public domain per LOC: "There are no known copyright restrictions"; restrictions on use expired 1986; credit the photographer; do not crop or colorize. (https://web.archive.org/web/20231226162654/https://www.loc.gov/rr/print/res/079_vanv.html)
- **Source URL:** https://en.wikinews.org/wiki/File:Mahalia_Jackson_1962,_van_Vechten,_LC-USZ62-91314.jpg
- **Publicity-rights review:** Subject died January 27, 1972. Illinois deceased-personality rights are reported to extend 50 years post-mortem; the stated period elapsed January 27, 2022. Recorded here, not relied on as legal advice.
- **Caption:** "Mahalia Jackson, photographed by Carl Van Vechten, April 16, 1962. Jackson migrated to Chicago in 1927 and credited the city's organizational and business environment with opening possibilities. Library of Congress."
- **Context:** The migrant-artist node of the network — the Great Migration made visible in one career.

### V3 — Pilgrim Baptist Church building photograph (unavailable-with-reason)
- **Type:** architectural photograph (exterior/interior)
- **Status:** `unavailable-with-reason`
- **Reason:** Candidate files exist (Wikimedia Commons Category: Pilgrim Baptist Church (Chicago), including a June 1964 HABS survey photo), but the per-file license page returned HTTP 403 in this pass and could not be verified; the City of Chicago landmarks report reproduces HABS and 1930s photos without rights metadata. Per the visuals directive, **no image is used without per-file license verification.** The piano (V1) and institutional map (V6) carry Pilgrim's visual weight instead. Revisit if LOC publishes an item-level HABS record with an explicit rights statement.

---

## Built graphics (data-driven; build at publish)

### V4 — Network constellation diagram (build-at-publish)
- **Type:** network diagram (nodes = institutions/people; edges = graded relationships)
- **Status:** `build-at-publish`
- **Data source:** `relationships.json` (28 triples) + `claim-ledger.json` grades
- **Specification:** Four concentric rings — (1) Churches: Ebenezer, Pilgrim, First Church of Deliverance, Metropolitan; (2) People: Dorsey, Austin, Frye, Sallie Martin, Roberta Martin, Morris, Cobbs, Smith, Jackson, Cleveland; (3) Publishing & convention: Dorsey House of Music, Bowles' House of Music, Martin & Morris, NCGCC; (4) Media & labels: 1935 radio broadcast, Hammond organ, Vee-Jay. Edges labeled with predicates; **SUPPORTED edges rendered dashed with visible grade tags; VERIFIED edges (R25, R26) solid; DISPUTED edges (R06, NCGCC date) rendered in red with a "disputed" flag.** Dorsey, Sallie Martin, and Pilgrim are the three highest-degree nodes — the brief's thesis made visible.
- **Caption:** "The Chicago gospel network, c. 1931–1956. Solid lines: verified; dashed: supported; red: disputed. Grades follow the claim ledger."
- **Context:** Answers the bounded question in one image: institutions and networks, not a lone founder.

### V5 — Timeline, 1927–2006 (build-at-publish)
- **Type:** horizontal timeline
- **Status:** `build-at-publish`
- **Data source:** `brief.md` §12 (15 dated rows)
- **Specification:** 1927 (Jackson migrates) → Dec 1931 (Ebenezer chorus call) → 1931/32 (Dorsey to Pilgrim) → Jan 1932 (Ebenezer chorus debut) → 1932 (convocation; Dorsey House of Music) → 1932/33 (NCGCC — marked DISPUTED, split marker) → 1933 (Martin-Frye Quartet) → 1935 (radio) → 1936 (Roberta Martin Singers) → 1939 (Hammond) → 1940 (Martin & Morris) → 1956 ("Uncloudy Day") → 2006 (fire — archive-loss marker, distinct styling). Include the grade of each event in small type.
- **Caption:** "Chicago gospel infrastructure, 1927–2006. Disputed dates flagged; the 2006 fire marks the archive's destruction."

### V6 — Bronzeville institutional map (build-at-publish)
- **Type:** neighborhood map (stylized street grid, not a satellite image)
- **Status:** `build-at-publish`
- **Data source:** documented addresses — Pilgrim Baptist, 3301 S. Indiana Ave.; Ebenezer Missionary Baptist, 4501 S. Vincennes Ave.; First Church of Deliverance, 4315 S. Wabash Ave. (all Bronzeville, South Side)
- **Specification:** Plot the three addresses with year labels (1922 / 1931–32 / 1935–39); annotate the ~1.5-mile corridor to show institutional density; note "addresses from Congressional Record, city landmark report, and NPR reporting."
- **Caption:** "Three institutions, a few South Side blocks: the physical footprint of Chicago's gospel network."

### V7 — "Birthplace" claims comparison (build-at-publish)
- **Type:** two-column evidence comparison graphic
- **Status:** `build-at-publish`
- **Data source:** CL04 (DISPUTED)
- **Specification:** Left column: Ebenezer — Dec 6, 1931 call; Frye/Dorsey; Jan 1932 ~100-voice debut; institutional self-claim. Right column: Pilgrim — Dorsey hired 1931/32 by Austin; decades-long directorship; NMAAHC "birthplace of gospel music" caption. Footer, verbatim: **"Attributed, not adjudicated — the definition of 'gospel choir' is unsettled."** No winner declared, by design.
- **Caption:** "Two 'birthplace' claims, two evidence columns — why CTL does not declare a winner."

---

## Videos

### VID1 — PBS *GOSPEL* official trailer (embed)
- **Title:** "Official Trailer for Henry Louis Gates Jr.'s 'Gospel,' Premiering Feb. 12 on PBS"
- **Channel:** PBS (official)
- **Video ID / URL:** `wiCYTuSahnw` · https://www.youtube.com/watch?v=wiCYTuSahnw
- **Upload date:** Not verified in this pass (trailer for the series announced August 28, 2023; series premiered February 12–13, 2024 — PBS/WETA)
- **Uploader:** PBS (official channel)
- **Why selected:** Explanatory framing — the trailer's narration traces gospel's origin story "coming out of slavery, blending with the blues tradition, and soaring to new heights during the Great Migration," matching the brief's Great Migration frame (CL02). Context illustration only.
- **Timestamp range:** Full trailer (short-form; no segment selection needed)
- **Embed status:** **Not verified in-browser in this pass** (no live browser available to subagent). YouTube embeds are enabled by default on official PBS uploads; **re-check at publication time.** If embedding is disabled, cite as a link instead.
- **Music-specific note:** The trailer contains performance snippets; per the video directive, performance footage **illustrates** a claim about the scene — it does not evidence it. The claim ledger's textual evidence stays primary. No lyrics are quoted; no full songs are used.

### VID2 — WTTW *Chicago Tonight: Black Voices* — "'The Birth of Gospel' Documentary Premieres on WTTW" (reference link, not embedded)
- **Title:** "Chicago Tonight: Black Voices | 'The Birth of Gospel' Documentary Premieres on WTTW"
- **Channel:** WTTW / PBS video portal (no official YouTube upload found in this pass)
- **URL:** https://watch.montanapbs.org/video/birth-gospel-g2hl6i/
- **Date:** May 7, 2022 (clip, 2m 47s)
- **Why selected:** Directly previews the documentary tracing gospel's birth and growth in Chicago — Dorsey's Great Migration arrival, his "gospel blues," and the debut of the first gospel choirs at Ebenezer and Pilgrim. The most on-brief audiovisual source found; cited as a link because no verifiable official-channel YouTube upload exists.
- **Embed status:** n/a — cited as link per the directive's rule for non-embeddable video.

**Excluded:** Full-album uploads, unknown-provenance reuploads, reaction videos, and AI-generated or misattributed content were screened out; none are listed.

---

## Link-rot plan
- Full identity metadata (title, channel, ID, URL, dates, uploader, rationale) is recorded above for every video.
- **Embed status for VID1 must be re-checked at publication time** (verify the YouTube embed endpoint allows embedding; fall back to a plain link if disabled).
- Sourced-image rights statements were captured with archived URLs (LOC Van Vechten statement via web.archive.org); re-verify file pages before any print or licensed reuse.
- V3 (Pilgrim building photo) remains the top candidate for a future sourced addition if an LOC item-level HABS record with explicit rights appears.
