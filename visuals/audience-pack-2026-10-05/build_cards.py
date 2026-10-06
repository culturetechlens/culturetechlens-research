#!/usr/bin/env python3
"""CTL audience-pack card generator — 1080x1080 PNGs, Pillow-rendered (no AI faces, exact text)."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.expanduser("~/workspace/goals/build-culturetechlens/files/visuals/audience-pack-2026-10-05")
os.makedirs(OUT, exist_ok=True)

W = H = 1080
BLACK = (8, 8, 8); PAPER = (14, 12, 10)
RED = (165, 28, 48); RED_DEEP = (110, 18, 32)
BRONZE = (138, 90, 43); BRONZE_SOFT = (201, 154, 94)
BONE = (232, 224, 210); MUTED = (179, 168, 148); LINE = (58, 48, 39)

FD = "/usr/share/fonts/truetype/dejavu/"
serif_b = ImageFont.truetype(FD + "DejaVuSerif-Bold.ttf", 44)
serif = ImageFont.truetype(FD + "DejaVuSerif.ttf", 40)
serif_i = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf", 40)
sans = ImageFont.truetype(FD + "DejaVuSans.ttf", 30)
sans_b = ImageFont.truetype(FD + "DejaVuSans-Bold.ttf", 30)

def font(path, size):
    return ImageFont.truetype(path, size)

def tracked(draw, xy, text, fnt, fill, tracking=6):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x

def center(draw, y, text, fnt, fill):
    tw = draw.textlength(text, font=fnt)
    draw.text(((W - tw) / 2, y), text, font=fnt, fill=fill)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

def center_in(draw, x0, x1, y, text, fnt, fill):
    tw = draw.textlength(text, font=fnt)
    draw.text((x0 + (x1 - x0 - tw) / 2, y), text, font=fnt, fill=fill)

def center_block(draw, y, text, fnt, fill, max_w, lh):
    for line in wrap(draw, text, fnt, max_w):
        center(draw, y, line, fnt, fill); y += lh
    return y

def base(eyebrow, source_line):
    """Common chrome. Returns (img, draw, content_top_y)."""
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    # subtle vertical gradient
    for yy in range(H):
        t = yy / H
        d.line([(0, yy), (W, yy)], fill=(int(8 + 8 * t), int(8 + 5 * t), int(8 + 4 * t)))
    # top bronze strip + header
    d.rectangle([0, 0, W, 8], fill=BRONZE)
    tracked(d, (60, 40), "CULTURETECHLENS", serif_b, BONE, tracking=8)
    d2 = ImageDraw.Draw(img)
    d2.text((60, 100), "Culture, Clearly Seen.", font=font(SERIF_I, 30), fill=BRONZE_SOFT)
    d.line([60, 152, W - 60, 152], fill=RED, width=3)
    tracked(d, (60, 178), eyebrow.upper(), sans_b, BRONZE_SOFT, tracking=4)
    # footer
    f1 = "CultureTechLens \u2014 Culture, Clearly Seen.  culturetechlens.com"
    tw = d.textlength(f1, font=sans_b)
    d.text(((W - tw) / 2, H - 92), f1, font=sans_b, fill=BONE)
    sw = d.textlength(source_line, font=sans)
    sf, ssize = sans, 30
    while d.textlength(source_line, font=sf) > 940 and ssize > 18:
        ssize -= 2
        sf = font(SANS, ssize)
    sw = d.textlength(source_line, font=sf)
    d.text(((W - sw) / 2, H - 52), source_line, font=sf, fill=MUTED)
    return img, d

def save(img, name):
    p = os.path.join(OUT, name)
    img.save(p)
    print("wrote", p)

SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SERIF = FD + "DejaVuSerif.ttf"
SERIF_I = "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf"
SANS = FD + "DejaVuSans.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"

# ---------- CARD 1: CTL 10 leaderboard ----------
def card1():
    img, d = base("The CTL 10 \u00b7 Edition 2026-10 \u00b7 Artifacts",
                  "Source: CTL Index Edition 2026-10 \u00b7 DOI 10.5281/zenodo.23081630")
    center(d, 236, "Ten artifacts. Scored, not vibes.", font(SERIF_B, 58), BONE)
    d.text((60, 320), "RANK", font=font(SANS_B, 22), fill=MUTED)
    d.text((170, 320), "ARTIFACT", font=font(SANS_B, 22), fill=MUTED)
    rows = [("Cadillac", 78.8), ("Church fan", 67.8), ("1955 yearbook", 66.5),
            ("Mail-order catalog", 65.4), ("Transistor radio", 65.3),
            ("Murray\u2019s pomade", 62.4), ("Hot comb", 57.1),
            ("45-rpm single", 47.5), ("Afro pick", 46.2), ("Photo album", 22.6)]
    y = 356
    for i, (name, score) in enumerate(rows, 1):
        rk = font(SERIF_B, 36); nm = font(SANS, 30); sc = font(SANS_B, 30)
        d.text((60, y), f"#{i}", font=rk, fill=BRONZE_SOFT)
        d.text((170, y + 4), name, font=nm, fill=BONE)
        st = f"{score:.1f}"
        sw = d.textlength(st, font=sc)
        d.text((W - 60 - sw, y + 4), st, font=sc, fill=BONE)
        bw = int((score / 80.0) * 330)
        d.rounded_rectangle([W - 470, y + 46, W - 60, y + 56], radius=5, fill=LINE)
        d.rounded_rectangle([W - 470, y + 46, W - 470 + bw, y + 56], radius=5, fill=RED)
        y += 62
    save(img, "01-index-leaderboard.png")

# ---------- CARD 2: attention paradox ----------
def card2():
    img, d = base("Index data story \u00b7 Edition 2026-10",
                  "Source: CTL Index Edition 2026-10 \u00b7 culturetechlens.com")
    center(d, 240, "The deepest evidence.", font(SERIF_B, 62), BONE)
    center(d, 312, "The fewest eyes.", font(SERIF_B, 62), BRONZE_SOFT)
    # two panels
    for x0, title, lookups, ev, rank, accent in [
        (60, "Cadillac", "33,922", "75.0", "Index #1", RED),
        (560, "Afro pick", "106", "100.0", "Index #9", BRONZE)]:
        x1 = x0 + 460
        d.rounded_rectangle([x0, 430, x1, 800], radius=16, outline=LINE, width=2)
        d.rectangle([x0, 430, x1, 442], fill=accent)
        center_in(d, x0, x1, 470, title, font(SERIF_B, 44), BONE)
        center_in(d, x0, x1, 540, "lookups (30d)", font(SANS, 24), MUTED)
        center_in(d, x0, x1, 576, lookups, font(SERIF_B, 88), BONE)
        center_in(d, x0, x1, 690, f"evidence depth {ev}", font(SANS_B, 32), BRONZE_SOFT)
        center_in(d, x0, x1, 736, rank, font(SANS, 28), MUTED)
    center_block(d, 848, "The Index scores what the crowd overlooks. Public attention is only 40% of the story.",
                 font(SANS, 30), BONE, 920, 44)
    save(img, "02-attention-paradox.png")

# ---------- CARD 3: pageviews skew ----------
def card3():
    img, d = base("Index data story \u00b7 Edition 2026-10",
                  "Source: CTL Index Edition 2026-10 \u00b7 Wikipedia 30-day lookups, published with the edition")
    center(d, 240, "33,922 vs. 106.", font(SERIF_B, 72), BONE)
    center(d, 326, "Public attention, 320\u00d7 apart.", font(SERIF_I, 36), BRONZE_SOFT)
    bars = [("Cadillac", 33922, RED), ("Church fan", 6156, BRONZE),
            ("Transistor radio", 4624, BRONZE_SOFT), ("Afro pick", 106, MUTED)]
    y = 440
    for name, v, col in bars:
        d.text((60, y), name, font=font(SANS, 30), fill=BONE)
        vs = f"{v:,}"
        vw = d.textlength(vs, font=font(SANS_B, 30))
        d.text((W - 60 - vw, y), vs, font=font(SANS_B, 30), fill=BONE)
        bw = max(6, int(v / 33922 * 800))
        d.rounded_rectangle([120, y + 48, 120 + bw, y + 66], radius=9, fill=col)
        y += 108
    center_block(d, 890, "Same edition. Same method. The crowd looked at the Cadillac 320 times for every look at the Afro pick.",
                 font(SANS, 29), MUTED, 920, 42)
    save(img, "03-pageviews-skew.png")

# ---------- CARD 4: score anatomy (stacked contributions) ----------
def card4():
    img, d = base("Index data story \u00b7 how the score works",
                  "Source: CTL Index Edition 2026-10 \u00b7 methodology CTL-IDX-001 v1.1")
    center(d, 240, "Inside a score.", font(SERIF_B, 64), BONE)
    center(d, 318, "Attention 40% \u00b7 Evidence 40% \u00b7 Momentum 20%", font(SANS, 32), BRONZE_SOFT)
    rows = [("Cadillac", 40.0, 30.0, 8.8, 78.8),
            ("Church fan", 28.2, 31.8, 7.8, 67.8),
            ("1955 yearbook", 20.4, 33.6, 12.4, 66.5)]
    cols = [RED, BRONZE, MUTED]
    y = 440
    for name, a, e, m, tot in rows:
        d.text((60, y), f"#{['1','2','3'][rows.index((name,a,e,m,tot))]} {name}", font=font(SANS_B, 30), fill=BONE)
        ts = f"{tot:.1f}"
        tw = d.textlength(ts, font=font(SANS_B, 30))
        d.text((W - 60 - tw, y), ts, font=font(SANS_B, 30), fill=BONE)
        x = 60; scale = 960 / 80.0
        for val, col in zip((a, e, m), cols):
            wseg = val * scale
            d.rounded_rectangle([x, y + 52, x + wseg, y + 76], radius=12, fill=col)
            x += wseg
        d.text((60, y + 88), f"{a:.1f} attention  +  {e:.1f} evidence  +  {m:.1f} momentum",
               font=font(SANS, 26), fill=MUTED)
        y += 160
    center(d, 930, "Every edition publishes its math.", font(SERIF_I, 32), BRONZE_SOFT)
    save(img, "04-score-anatomy.png")

# ---------- CARD 5: Clear Ear Award ----------
def card5():
    img, d = base("The Clear Ear Award \u00b7 2026",
                  "Source: culturetechlens.com/music/sound-award/ \u00b7 shortlist 15 \u2192 25, Oct 5, 2026")
    center(d, 250, "25 albums.", font(SERIF_B, 96), BONE)
    center(d, 356, "One standard.", font(SERIF_B, 96), BRONZE_SOFT)
    center_block(d, 500, "One album per year. Judged in lanes \u2014 R&B, hip-hop, soul, jazz, gospel, house and Afro-house, Afrobeats.",
                 font(SANS, 32), BONE, 920, 46)
    center(d, 660, "Winner announced December 2026.", font(SERIF_I, 36), BRONZE_SOFT)
    d.rounded_rectangle([60, 760, W - 60, 880], radius=16, outline=BRONZE, width=2)
    center(d, 786, "The 2026 shortlist is live.", font(SANS_B, 32), BONE)
    center(d, 828, "Read it. Argue with it. Cite it.", font(SANS, 30), MUTED)
    save(img, "05-clear-ear-25.png")

# ---------- CARDS 6-8: quote cards ----------
def quote_card(num, slug, quote, attr, sub):
    img, d = base("In his words", "Source: William Maxey, Founder and President, CultureTechLens NFP")
    d.rectangle([60, 300, 72, 760], fill=RED)
    y = center_block(d, 320, "\u201c" + quote + "\u201d", font(SERIF, 52), BONE, 860, 72)
    d.text((110, y + 40), "\u2014 " + attr, font=font(SANS_B, 32), fill=BRONZE_SOFT)
    d.text((110, y + 88), sub, font=font(SANS, 28), fill=MUTED)
    save(img, f"{num:02d}-quote-{slug}.png")

def card6():
    quote_card(6, "cite", "You are not an institution when you post. You are an institution when others have to cite you.",
               "William Maxey", "Founder and President")

def card7():
    quote_card(7, "trust", "It must be trust. I have been doing this all this time.",
               "William Maxey", "Founder and President")

def card8():
    quote_card(8, "founder", "Institutions just make the lens outlive the founder.",
               "William Maxey", "Founder and President")

# ---------- CARD 9: archive 1441 ----------
def card9():
    img, d = base("The Black Cultural Knowledge Graph",
                  "Source: culturetechlens.com/graph/ \u00b7 1,441 entity pages live")
    center(d, 300, "1,441", font(SERIF_B, 190), BONE)
    center(d, 500, "entities. One archive.", font(SERIF_B, 72), BRONZE_SOFT)
    center_block(d, 640, "Every entity evidence-graded. Every claim sourced. Searchable, dated, tagged \u2014 built so others have to cite it.",
                 font(SANS, 32), BONE, 920, 46)
    d.rounded_rectangle([60, 800, W - 60, 890], radius=16, outline=BRONZE, width=2)
    center(d, 824, "Explore the graph.", font(SANS_B, 32), BONE)
    save(img, "09-archive-1441.png")

# ---------- CARD 10: five grades ----------
def card10():
    img, d = base("How CTL works \u00b7 the evidence grades",
                  "Source: culturetechlens.com \u00b7 the canonical five-grade scale")
    center(d, 250, "Five grades.", font(SERIF_B, 72), BONE)
    center(d, 336, "Zero guesswork.", font(SERIF_B, 72), BRONZE_SOFT)
    grades = ["VERIFIED", "SUPPORTED", "PROVISIONAL", "DISPUTED", "UNRESOLVED"]
    y = 470
    for g in grades:
        gf = font(SANS_B, 40)
        gw = d.textlength(g, font=gf)
        d.rounded_rectangle([(W - gw) / 2 - 40, y - 12, (W + gw) / 2 + 40, y + 52], radius=30, fill=RED_DEEP, outline=RED, width=2)
        center(d, y, g, gf, BONE)
        y += 92
    center(d, 940, "Every claim carries its grade.", font(SERIF_I, 34), BRONZE_SOFT)
    save(img, "10-five-grades.png")

# ---------- CARDS 11-13: paper promos ----------
def paper_card(num, slug, eyebrow, title, stat_head, stat_sub, doi):
    img, d = base(eyebrow, f"Open access \u00b7 CC BY 4.0 \u00b7 DOI {doi}")
    center_block(d, 250, title, font(SERIF_B, 56), BONE, 940, 70)
    d.line([60, 470, W - 60, 470], fill=RED, width=3)
    y = center_block(d, 520, stat_head, font(SERIF_B, 52), BRONZE_SOFT, 940, 68)
    center_block(d, y + 24, stat_sub, font(SANS, 30), BONE, 920, 44)
    center(d, 880, "Read the paper. Cite the paper.", font(SERIF_I, 34), BRONZE_SOFT)
    save(img, f"{num:02d}-paper-{slug}.png")

def card11():
    paper_card(11, "memory", "CTL research paper", "The Black Memory Emergency",
               "Four million images. One auction away from dispersal.",
               "The Johnson Publishing archive \u2014 Ebony and Jet\u2019s photographic memory of Black American life \u2014 reached a bankruptcy auction in July 2019. A four-foundation consortium rescued it for just under $30 million.",
               "10.5281/zenodo.23173585")

def card12():
    paper_card(12, "story", "CTL research paper", "Who Controls the Story?",
               "Fewer than 180 of 11,000+ U.S. commercial radio stations are Black-owned.",
               "About 1.6% \u2014 per the National Association of Black Owned Broadcasters, 2020. The largest assets targeting Black audiences are not Black-owned.",
               "10.5281/zenodo.23173917")

def card13():
    paper_card(13, "technology", "CTL research paper", "Black Technology",
               "22 verified patents. 165 years of continuous Black invention.",
               "From an 1821 dry-scouring patent to a 1986 squirt-gun patent \u2014 each checked against patent records and primary sources. Myths collapse; the real achievements don\u2019t need them.",
               "10.5281/zenodo.23173962")

if __name__ == "__main__":
    card1(); card2(); card3(); card4(); card5()
    card6(); card7(); card8(); card9(); card10()
    card11(); card12(); card13()
    print("done")
