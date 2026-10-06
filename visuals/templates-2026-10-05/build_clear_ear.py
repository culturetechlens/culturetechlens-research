"""Clear Ear Award 2026 countdown set — 3 graphics. All albums verified from the real shortlist."""
from ctl_cards import *

# 1 — the standard
im = bg("texture-crimson-bronze.png", darken=0.35)
d = ImageDraw.Draw(im)
y = eyebrow(d, 130, "THE CLEAR EAR AWARD · 2026")
d.text((80, y + 20), "25 albums.\nOne standard.", font=SERIF_B, fill=INK)
para(d, 80, y + 300, "R&B · hip-hop · soul · jazz · gospel · house / Afro-house · Afrobeats — "
     "judged in lanes, scored on critical consensus, cultural impact, and evidence depth.",
     SANS, INK, 920, leading=14)
brand_footer(d)
save(im, "clear-ear-01-standard.png")

# 2 — the date
im = bg("texture-archival-dark.png", darken=0.55)
d = ImageDraw.Draw(im)
y = eyebrow(d, 130, "THE CLEAR EAR AWARD · 2026")
d.text((80, y + 20), "The winner is\nannounced\nDecember 2026.", font=SERIF_B, fill=INK)
para(d, 80, y + 380, "One album of the year. Nothing here is ranked yet — "
     "that is December's work.", SANS_SM, MUTED, 920, leading=10)
brand_footer(d)
save(im, "clear-ear-02-december.png")

# 3 — shortlist teaser (5 of 25, all real; Metacritic scores from the shortlist page)
teasers = [
    ("Ezra Collective", "Here Because Of Hope", "Metacritic 90"),
    ("Genesis Owusu", "REDSTAR WU & THE WORLDWIDE SCOURGE", "Metacritic 88"),
    ("Vince Staples", "Cry Baby", "Metacritic 87"),
    ("Jill Scott", "To Whom This May Concern", None),
    ("CeCe Winans", "The Hymns", None),
]
ARTIST_F = font(FD + "DejaVuSans-Bold.ttf", 34)
ALBUM_F = font(FD + "DejaVuSans.ttf", 30)
im = bg("texture-archival-dark.png", darken=0.55)
d = ImageDraw.Draw(im)
y = eyebrow(d, 70, "CLEAR EAR AWARD · 2026 · SHORTLIST")
d.text((80, y + 6), "Five of twenty-five.", font=font(FD + "DejaVuSerif-Bold.ttf", 64), fill=INK)
y += 108
for artist, album, mc in teasers:
    d.text((80, y), artist, font=ARTIST_F, fill=GOLD_BRIGHT)
    y += 48
    line = f"— {album}" + (f"  ·  {mc}" if mc else "")
    y = para(d, 80, y, line, ALBUM_F, INK, 920, leading=8) + 26
    if y > 830:
        print(f"LAYOUT WARNING clear-ear-03: teasers end at {y}")
        break
para(d, 80, 884, "The full 25: culturetechlens.com/music/sound-award/2026/",
     SANS_SM_B, MUTED, 920, leading=8)
brand_footer(d)
save(im, "clear-ear-03-teaser.png")

print("clear ear done")
