"""Shared card renderer for CTL visual packs. 1080x1080, CTL palette, tracked wordmark."""
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os

W = H = 1080
BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")

INK = (232, 224, 210)
GOLD = (201, 154, 94)
GOLD_BRIGHT = (232, 178, 42)
BRONZE = (138, 90, 43)
RED = (165, 28, 48)
MUTED = (179, 168, 148)
BLACK = (8, 8, 8)

FD = "/usr/share/fonts/truetype/dejavu/"
FN = "/usr/share/fonts/truetype/noto/"

def font(path, size):
    return ImageFont.truetype(path, size)

SERIF_B = font(FD + "DejaVuSerif-Bold.ttf", 96)
SERIF = font(FN + "NotoSerif-SemiBold.ttf", 44)
SANS = font(FD + "DejaVuSans.ttf", 40)
SANS_BODY = font(FD + "DejaVuSans.ttf", 34)
SANS_B = font(FD + "DejaVuSans-Bold.ttf", 40)
SANS_SM = font(FD + "DejaVuSans.ttf", 30)
SANS_SM_B = font(FD + "DejaVuSans-Bold.ttf", 30)
EYEBROW_F = font(FD + "DejaVuSans-Bold.ttf", 30)
STAT_F = font(FD + "DejaVuSerif-Bold.ttf", 64)
URL_F = font(FD + "DejaVuSans-Bold.ttf", 26)

_tex_cache = {}
def bg(name="texture-archival-dark.png", darken=0.55):
    if name not in _tex_cache:
        im = Image.open(os.path.join(ASSETS, name)).convert("RGB")
        im = im.resize((W, H), Image.LANCZOS)
        _tex_cache[name] = im
    im = _tex_cache[name].copy()
    overlay = Image.new("RGB", (W, H), BLACK)
    return Image.blend(im, overlay, darken)

def tracked(draw, xy, text, fnt, fill, track=6):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        w = draw.textlength(ch, font=fnt)
        x += w + track
    return x

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines

def para(draw, x, y, text, fnt, fill, max_w, leading=14, para_gap=8):
    ascent, descent = fnt.getmetrics()
    lh = ascent + descent + leading
    for pi, chunk in enumerate(text.split("\n")):
        if pi:
            y += para_gap
        for line in wrap(draw, chunk, fnt, max_w):
            draw.text((x, y), line, font=fnt, fill=fill)
            y += lh
    return y

def eyebrow(draw, y, text, x=80):
    tracked(draw, (x, y), text.upper(), EYEBROW_F, GOLD, track=5)
    return y + 52

def brand_footer(draw):
    draw.line([(80, 996), (1000, 996)], fill=GOLD, width=2)
    tracked(draw, (80, 1008), "CULTURETECHLENS", SANS_SM_B, INK, track=4)
    draw.text((80, 1040), '"Culture, Clearly Seen."  ·  culturetechlens.com',
              font=SANS_SM, fill=MUTED)

def slide_no(draw, n, total):
    t = f"{n:02d} / {total:02d}"
    draw.text((1000 - draw.textlength(t, font=SANS_SM), 44), t, font=SANS_SM, fill=MUTED)

def save(im, name):
    p = os.path.join(BASE, name)
    im.save(p)
    print("wrote", p, im.size)
