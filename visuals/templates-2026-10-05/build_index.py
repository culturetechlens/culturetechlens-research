"""Monthly Index announcement template set. Data-driven: EDITIONS dict is the only
thing that changes month to month. See template-README.md for the monthly slots."""
from ctl_cards import *

EDITIONS = {
    "2026-10": dict(
        topic="ARTIFACTS",
        method_url="culturetechlens.com/research/culturetechlens-index/methodology/",
        rows=[
            ("Cadillac (as cultural object)", 78.8, 33922),
            ("Funeral-home advertising church fan", 67.8, 6156),
            ("Yearbook (1955 Allen University 'Yellow Jacket')", 66.5, 2015),
            ("Mail-order catalog (Sears / Montgomery Ward)", 65.4, 2655),
            ("Transistor radio (Regency TR-1)", 65.3, 4624),
            ("Murray's Superior Hair Dressing Pomade (tin)", 62.4, 4611),
            ("Hot comb / pressing comb", 57.1, 958),
            ("45-rpm single (Chess 1604, 'Maybellene')", 47.5, 2928),
            ("Afro pick (fist-handle hair pick)", 46.2, 106),
            ("The Black family photograph album", 22.6, 680),
        ],
    ),
}

def render_announcement(key, ed):
    im = bg("texture-crimson-bronze.png", darken=0.35)
    d = ImageDraw.Draw(im)
    y = eyebrow(d, 92, f"THE CTL 10 · EDITION {key}")
    d.text((80, y + 10), ed["topic"], font=SERIF_B, fill=INK)
    y2 = y + 128
    d.text((80, y2), "#1", font=STAT_F, fill=GOLD_BRIGHT)
    name, score, _ = ed["rows"][0]
    para(d, 230, y2 + 8, f"{name}\nScore {score:.1f} / 100", SANS_B, INK, 770, leading=10)
    y3 = y2 + 170
    d.line([(80, y3), (1000, y3)], fill=GOLD, width=2)
    y3 += 30
    d.text((80, y3), "THE TOP THREE", font=SANS_SM_B, fill=GOLD)
    y3 += 52
    for i, (name, score, _) in enumerate(ed["rows"][1:3], 2):
        d.text((80, y3), f"{i}.", font=SANS_B, fill=GOLD_BRIGHT)
        y3 = para(d, 150, y3, f"{name} — {score:.1f}", SANS, INK, 850, leading=10) + 18
    y3 += 20
    y3 = para(d, 80, y3, "Ten artifacts ranked by public attention + CTL evidence depth.",
               SANS_SM, MUTED, 920, leading=8)
    y3 = para(d, 80, y3 + 8, "Full scores and methodology:", SANS_SM, MUTED, 920, leading=8)
    d.text((80, y3 + 8), ed["method_url"], font=URL_F, fill=GOLD_BRIGHT)
    brand_footer(d)
    save(im, f"index-{key}-announcement.png")

def render_leaderboard(key, ed):
    im = bg("texture-archival-dark.png", darken=0.55)
    d = ImageDraw.Draw(im)
    y = eyebrow(d, 70, f"CTL 10 · {key} · FULL RANKING")
    y += 6
    max_score = 100.0
    for i, (name, score, _) in enumerate(ed["rows"], 1):
        ry = y + (i - 1) * 76
        d.text((80, ry), f"{i:2d}", font=SANS_B, fill=GOLD if i <= 3 else MUTED)
        # bar
        bw = int((score / max_score) * 560)
        d.rectangle([(200, ry + 12), (200 + bw, ry + 38)], fill=BRONZE if i > 3 else GOLD_BRIGHT)
        d.text((780, ry + 4), f"{score:.1f}", font=SANS_B, fill=INK)
        label = name if len(name) <= 34 else name[:32] + "…"
        d.text((80, ry + 42), label, font=SANS_SM, fill=MUTED)
    brand_footer(d)
    save(im, f"index-{key}-leaderboard.png")

def render_paradox(key, ed):
    rows = ed["rows"]
    top = rows[0]      # Cadillac 78.8, 33,922 views
    deep = rows[8]     # Afro pick 46.2, 106 views, evidence depth 100.0
    im = bg("texture-archival-dark.png", darken=0.55)
    d = ImageDraw.Draw(im)
    y = eyebrow(d, 92, f"CTL 10 · {key} · DATA STORY")
    d.text((80, y + 10), "The attention\nparadox.", font=SERIF_B, fill=INK)
    y2 = y + 250
    y2 = para(d, 80, y2, "The artifact CTL knows best is the one the public "
                         "looks at least:", SANS, INK, 920, leading=14) + 30
    d.text((80, y2), deep[0], font=SANS_B, fill=GOLD_BRIGHT)
    y2 += 56
    d.text((80, y2), "CTL evidence depth 100.0  ·  106 Wikipedia views", font=SANS, fill=INK)
    y2 += 70
    y2 = para(d, 80, y2, "The artifact the public looks at most:", SANS, INK, 920, leading=14) + 30
    d.text((80, y2), top[0], font=SANS_B, fill=GOLD_BRIGHT)
    y2 += 56
    d.text((80, y2), f"33,922 Wikipedia views  ·  score {top[1]:.1f}", font=SANS, fill=INK)
    y2 += 90
    para(d, 80, y2, "That gap — between what we have studied and what the world "
                    "has seen — is why the archive exists.", SANS_SM, MUTED, 920, leading=10)
    brand_footer(d)
    save(im, f"index-{key}-paradox.png")

for key, ed in EDITIONS.items():
    render_announcement(key, ed)
    render_leaderboard(key, ed)
    render_paradox(key, ed)
print("index templates done")
