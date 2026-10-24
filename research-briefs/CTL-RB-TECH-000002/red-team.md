# Red Team — CTL-RB-TECH-000002 "Black Chicago Goes Online"
**Version:** v0.1 (2026-09-28). Adversarial review of the brief's claims, sourcing, and reasoning.

## 1. Unsupported claims
- **No VERIFIED claims exist.** Every Chicago institutional date is SUPPORTED or below. The brief states this openly (§14, §16); risk is low as long as the published version preserves the grades. **Action:** any future edit that drops a grade label must be reverted.
- The CONJECTURAL Obama 2003 date rests on one enthusiast blog. If the blog's Wayback reading is wrong (e.g., version numbering), the claim collapses. **Action:** flag prominently; do not promote.

## 2. Circular sourcing
- The two *Editor & Publisher* items share a trade-press milieu; the retrospective (item 4) may itself draw on the 2005 report's framing. They are corroborating, not independent. **Action:** the brief asks for an archived December 2004 page as the independent confirmation (v0.2).
- The Final Call's 1995 date is self-reported by the institution across its own pages — one institutional voice, not independent corroboration. **Action:** seek a 1995–96 third-party mention (e.g., newspaper coverage of the Million Man March online promotion).

## 3. Date errors / anachronism
- "December 2004" is inferred from "last December" in a 2005 article framed around a May 2005 centennial. If the article published early in 2005, "last December" = December 2004; if it published in January 2005 it could theoretically mean December 2003 — checked: centennial framing pins it to 2005, so December 2004 stands. Low risk, noted.
- "Podcast" (2005) is the trade press's own contemporary term — not anachronistic. Do not retro-fit "social media" language onto this period.

## 4. Geographic errors
- **Highest risk in the brief.** AfroLink (1990) and AfroNet (1993) are national facts that a careless reader will take as Chicago evidence. **Mitigations in place:** separate timeline lane, separate `scope_note` fields in entities.json, explicit §5 F5 and §20 disambiguation. Verify at publication that no sentence merges them into Black Chicago.
- NTIA figures are national; the brief labels them national in §9, §11, the chart caption, and the visual itself. Same publication check required.

## 5. Causation
- The brief does not claim the access gap *caused* late institutional adoption (e.g., the Defender's 2004 holdout). It claims presence and access diverged. **Check:** no sentence should imply "the Defender waited because Black households lacked computers" — that is unproven and likely wrong (newsroom economics, ownership, and strategy are likelier drivers, also unproven here).

## 6. Survivorship / selection / celebrity bias
- The record overrepresents durable, well-resourced, nationally visible actors (Defender, Final Call, McIlwain's scholarship subjects). Defunct BBSs, dead listservs, and the unnamed NOI students are the counterweight the archive cannot supply. **Mitigation:** §16–§21 name the bias explicitly; §23 proposes oral-history recovery.
- Celebrity bias: Barack Obama's 2003 campaign site is the best-documented 2003 artifact partly because Obama became famous. A no-name 2003 church site would not have an enthusiast retrospective. Noted in §18 counterarguments.

## 7. Missing women, ordinary people, institutions
- Named actors skew male and institutional (see §19). The skew is sourced, not editorial — but a published version must not present it as the whole story. **Action:** keep §19 and the ENT-020 entity group; prioritize oral histories of women operators in CTL-DR-TECH-001.

## 8. Weak rights provenance
- The two actual visuals are locally built data graphics: zero rights risk. **Passed.**
- The three video selections: V1/V2 are the director's own uploads of his CC BY-SA work — strong. V3 is cited via the official Data & Society page; exact YouTube URL to be resolved at publication (never guessed). Embed-only; never download/re-upload. **Action:** re-check embed status at publication.
- The LOC Sengstacke photograph was NOT verified at file level and is NOT used. **Passed** (marked unavailable-with-reason).
- Wayback screenshots are not redistributable; none used. **Passed.**

## 9. Duplicate entities
- AfroLink vs AfroNet: checked distinct (1990 BBS software/company vs 1993 FidoNet network; different founders). §20 disambiguates. **Passed.**
- Defender website vs podcast: two launches, kept separate. **Passed.**
- Obama for Illinois (2003) vs Obama '08: kept separate. **Passed.**
- McIlwain tagged scholar, not adopter — prevents "inventor of Black internet history" slippage. **Passed.**

## 10. "First" claims
- The brief contains no "first Black website" claim. The Final Call (1995) is presented as the earliest *dated* Chicago institutional presence in the recovered record, explicitly not a first. **Passed.** Publication check: ensure no headline or caption compresses this into "first."

## Verdict
The brief is publishable at v0.1 research status with grades intact. The single most valuable v0.2 addition is one archived launch page (Defender Dec 2004 or Final Call 1995–96) — it would convert the brief's first claim to VERIFIED and anchor the timeline in primary evidence.
