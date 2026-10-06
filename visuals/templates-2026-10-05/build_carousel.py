"""Black Memory Emergency carousel — 10 slides, 1080x1080. All stats from the real paper."""
from ctl_cards import *

SLIDES = [
    dict(tex="texture-crimson-bronze.png", dark=0.35, no="01",
         brow="BLACK CULTURAL INTELLIGENCE",
         head="THE BLACK\nMEMORY\nEMERGENCY",
         body="What happens when Black history disappears.",
         stat=None,
         cta="A ten-slide story  →  swipe"),
    dict(tex="texture-archival-dark.png", dark=0.55, no="02",
         brow="THE RESEARCH",
         head="It was never\nabout a lack of\ncollecting.",
         body=("Black cultural memory in America is not primarily threatened by a lack of "
               "collecting — but by everything that happens after. CTL mapped 84 collections, "
               "119 entities, 70 timeline events, and 304 sources to find where the chain breaks."),
         stat="84 collections · 304 sources",
         cta=None),
    dict(tex="texture-archival-dark.png", dark=0.55, no="03",
         brow="DESTROYER 01 · CATALOGING BACKLOGS",
         head="Saved and\nsimultaneously\nlost.",
         body=("The AFRO-American Newspapers archive: ~3 million photographs, 130 years of a "
               "family-owned Black press — about 5% processed since October 2022. An uncataloged "
               "collection cannot be found, used, cited, or defended in a budget fight."),
         stat="3,000,000 photos · ~5% processed",
         cta=None),
    dict(tex="texture-archival-dark.png", dark=0.55, no="04",
         brow="DESTROYER 02 · OWNERSHIP CHANGE",
         head="The fastest-\nacting destroyer.",
         body=("The Johnson Publishing Company archive — 4 million+ images of Black American life — "
               "reached a bankruptcy auction in July 2019. Four foundations assembled in two days "
               "and paid just under $30 million. The rescue is the exception that maps the rule."),
         stat="4,000,000+ images · one bid away",
         cta=None),
    dict(tex="texture-archival-dark.png", dark=0.55, no="05",
         brow="DESTROYER 03 · THE COLLECTOR'S MORTALITY",
         head="The ticking\nclock.",
         body=("In 2025, photographer John Simmons's life's-work negatives burned in a friend's "
               "garage during a move. Teenie Harris's ~80,000 negatives survived only because the "
               "Carnegie Museum bought them from his family in 2001."),
         stat="~80,000 negatives · one purchase",
         cta=None),
    dict(tex="texture-archival-dark.png", dark=0.55, no="06",
         brow="DESTROYER 04 · RIGHTS UNCERTAINTY",
         head="The silent\nblocker.",
         body=("Eyes on the Prize — the landmark civil-rights documentary — vanished from circulation "
               "for roughly a decade over expired music licenses. It took $850,000+ in foundation "
               "grants to begin renewing the rights."),
         stat="~10 years vanished · $850,000+ to return",
         cta=None),
    dict(tex="texture-crimson-bronze.png", dark=0.35, no="07",
         brow="DESTROYER 05 · PLATFORM DELETION",
         head="Platform memory\nis not memory.",
         body=("In September 2026, BET Digital permanently deleted its entire written news archive "
               "in a \"video-first pivot\" — no warning, no migration. MySpace lost ~50 million songs. "
               "Pew: 18% of 2020–2022 #BlackLivesMatter tweets were already gone by 2023."),
         stat="199,000 articles · saved by the Archive",
         cta=None),
    dict(tex="texture-archival-dark.png", dark=0.55, no="08",
         brow="THE TEN-STAGE AUDIT",
         head="Abundance at\nthe start.\nBreakage in\nthe middle.",
         body=("CATALOGED is the worst-supported stage. DISCOVERABLE is the thinnest. "
               "What survives the middle passage is used powerfully — Shorefront's records fed "
               "reparations work."),
         stat="Stage 4: cataloged · worst-supported",
         cta=None),
    dict(tex="texture-archival-dark.png", dark=0.55, no="09",
         brow="THE RESPONSE",
         head="Triage,\nnot despair.",
         body=("A transparent triage framework — Risk × Significance × Uniqueness, gated by "
               "Feasibility. Every claim carries an evidence grade; a red-team audit forced 23 claim "
               "downgrades. The highest-value unresolved lead: the records of A.A. Rayner & Sons, "
               "the Chicago funeral home that handled Emmett Till's arrangements."),
         stat="23 downgrades · honesty is the method",
         cta=None),
    dict(tex="texture-crimson-bronze.png", dark=0.35, no="10",
         brow="READ THE PAPER · OPEN ACCESS",
         head="Cite the\narchive.",
         body=("The Black Memory Emergency — open access, CC BY 4.0.\n"
               "DOI 10.5281/zenodo.23173585"),
         stat="CultureTechLens · Chicago",
         cta="culturetechlens.com"),
]

for i, s in enumerate(SLIDES, 1):
    im = bg(s["tex"], darken=s["dark"])
    d = ImageDraw.Draw(im)
    slide_no(d, i, 10)
    y = eyebrow(d, 92, s["brow"])
    d.text((80, y + 10), s["head"], font=SERIF_B, fill=INK)
    # measure headline height
    lines = s["head"].count("\n") + 1
    y2 = y + 10 + lines * 108
    y2 = para(d, 80, y2 + 6, s["body"], SANS_BODY, INK, 920, leading=12)
    if s["stat"]:
        d.line([(80, y2 + 26), (200, y2 + 26)], fill=GOLD, width=3)
        stat_end = para(d, 80, y2 + 44, s["stat"], SANS_B, GOLD_BRIGHT, 920, leading=10)
        if stat_end > 918:
            print(f"LAYOUT WARNING slide {i}: stat ends at {stat_end}")
    if y2 > 918:
        print(f"LAYOUT WARNING slide {i}: body ends at {y2}")
    if s["cta"]:
        d.text((80, 892), s["cta"], font=SANS_SM_B, fill=MUTED)
    d.text((80, 940), "Source: The Black Memory Emergency, CultureTechLens, Oct 2026.",
           font=SANS_SM, fill=MUTED)
    brand_footer(d)
    save(im, f"carousel-memory-emergency-{i:02d}.png")

print("carousel done")
