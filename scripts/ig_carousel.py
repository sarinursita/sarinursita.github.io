#!/usr/bin/env python3
"""Ian's Notebook -> IG carousel (1080x1350), Cerivitas warm/homeschool style v2.

Design notes (from Sari, 28 Okt 2026):
  - warm + fun, not corporate. Speak to "Moms" directly.
  - name the concept out loud ("kenalan yuk sama microlearning")
  - warm-up first, saveable core later, one idea per slide
Usage: python3 scripts/ig_carousel.py <slug> --out /tmp/ig-out
"""
import argparse
import pathlib

from PIL import Image, ImageDraw, ImageFont

FONTS = pathlib.Path.home() / ".hermes/profiles/wiz/workspace/fonts"
W, H = 1080, 1350
M = 80

INK = "#23303E"
CREAM = "#FFF7EC"
CORAL = "#FF6B4A"
TEAL = "#1F9E8F"
MUSTARD = "#FFC24B"
PEACH = "#FFE3D6"
GREEN = "#DCF8C6"
GREY = "#F1EAE0"
MUTED = "#7A8797"
LINE = "#E6D8C4"


def display(size, weight=800):
    f = ImageFont.truetype(str(FONTS / "Baloo2.ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def body(size, weight=600):
    f = ImageFont.truetype(str(FONTS / "Nunito.ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def wrap(text, f, max_w):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if f.getlength(t) <= max_w:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def para(d, text, f, x, y, max_w, lh, fill):
    for ln in wrap(text, f, max_w):
        d.text((x, y), ln, font=f, fill=fill)
        y += int(f.size * lh)
    return y


def header(d, n, total):
    pill_w = int(body(24, 800).getlength("Ian's Notebook") + 66)
    d.rounded_rectangle((M, 62, M + pill_w, 118), radius=28, fill=INK)
    d.ellipse((M + 18, 82, M + 34, 98), fill=CORAL)
    d.text((M + 46, 76), "Ian's Notebook", font=body(24, 800), fill=CREAM)
    t = "x Cerivitas"
    d.text((W - M - body(24, 700).getlength(t), 80), t, font=body(24, 700), fill=MUTED)
    # progress dots
    x = M
    for i in range(total):
        d.ellipse((x, H - 74, x + 12, H - 62), fill=CORAL if i == n - 1 else LINE)
        x += 24


def foot(d, text=""):
    if text:
        d.text((W - M - body(24, 700).getlength(text), H - 82), text,
               font=body(24, 700), fill=MUTED)


def sticker(d, text, xy, fill=CORAL, fg=CREAM, angle=8, size=30):
    f = body(size, 800)
    w = int(f.getlength(text)) + 44
    h = int(size * 2.1)
    layer = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.rounded_rectangle((20, 20, 20 + w, 20 + h), radius=h // 2, fill=fill)
    ld.text((20 + 22, 20 + h // 2), text, font=f, fill=fg, anchor="lm")
    layer = layer.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    d._image.paste(layer, (xy[0] - 20, xy[1] - 20), layer)


def bullet_row(d, y, text, color=CORAL, num=None, tick=False):
    r = 30
    if tick:
        d.rounded_rectangle((M, y, M + 2 * r, y + 2 * r), radius=14, fill=color)
        d.line([(M + 16, y + 31), (M + 26, y + 41), (M + 45, y + 18)], fill=CREAM, width=7)
    else:
        d.ellipse((M, y, M + 2 * r, y + 2 * r), fill=color)
        d.text((M + r, y + r), str(num), font=body(30, 800), fill=CREAM, anchor="mm")
    yy = para(d, text, body(39, 700), M + 2 * r + 26, y + 6, W - 2 * M - 2 * r - 26, 1.35, INK)
    return max(y + 2 * r + 34, yy + 24)


def card(d, box, fill="#FFFFFF", radius=34, outline=None):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2)


# ---------------------------------------------------------------- slides

def s_cover():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img); d._image = img
    header(d, 1, 8)
    sticker(d, "buat Moms & guru", (W - 400, 200), fill=TEAL, angle=-6, size=27)

    d.text((M, 330), "Moms,", font=display(130, 800), fill=CORAL)

    t = "anak bisa selesaiin proyek 5 hari cuma modal chat 5 menit tiap pagi?"
    y = para(d, t, display(84, 800), M, 500, W - 2 * M, 1.14, INK)

    sub = "Bukan trik ajaib. Namanya "
    word = "microlearning."
    f = body(44, 700)
    yy = y + 44
    d.text((M, yy), sub, font=f, fill=INK)
    xw = M + f.getlength(sub)
    d.rounded_rectangle((xw - 10, yy + 46, xw + f.getlength(word) + 10, yy + 96), radius=12, fill=PEACH)
    d.text((xw, yy), word, font=f, fill=CORAL)

    d.text((M, H - 300), "Satu resep. Lima menit. Tiap pagi.", font=display(42, 800), fill=TEAL)
    d.text((M, H - 210), "geser", font=display(40, 800), fill=CORAL)
    d.line([(M + 130, H - 178), (M + 210, H - 178)], fill=CORAL, width=6)
    d.polygon([(M + 210, H - 178), (M + 190, H - 190), (M + 190, H - 166)], fill=CORAL)
    foot(d, "")
    return img


def s_pain():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img); d._image = img
    header(d, 2, 8)
    d.text((M, 160), "kenapa sih", font=body(30, 800), fill=CORAL)
    y = para(d, "Hari Rabu, grup WA-nya sepi.", display(70, 800), M, 206, W - 2 * M, 1.15, INK)

    bubbles = [
        ("l", "kak, materi rekamannya di mana ya?", "09:12"),
        ("r", "Sudah di drive ya, Mom. Link-nya di pesan Senin.", "09:20"),
        ("l", "Anak saya belum sempat buka, besok ya", "10:41"),
    ]
    fb = body(30, 600)
    laid = []
    for side, text, tm in bubbles:
        lines = wrap(text, fb, 540)
        bh = 34 + int(30 * 1.35) * len(lines) + 34
        bw = int(max(fb.getlength(l) for l in lines)) + 56
        laid.append((side, lines, tm, bh, bw))

    top = y + 40
    card_h = 96 + sum(b[3] + 22 for b in laid) + 26
    card(d, (M, top, W - M, top + card_h), fill="#FFFFFF", outline=LINE)
    d.rounded_rectangle((M, top, W - M, top + 96), radius=34, fill=TEAL)
    d.rectangle((M, top + 60, W - M, top + 96), fill=TEAL)
    d.ellipse((M + 34, top + 24, M + 84, top + 74), fill=CREAM)
    d.text((M + 59, top + 49), "K", font=display(30, 800), fill=TEAL, anchor="mm")
    d.text((M + 104, top + 28), "Kelas Cerita Anak", font=body(32, 800), fill=CREAM)
    d.text((M + 104, top + 64), "12 peserta", font=body(22, 600), fill="#D8F1EC")

    by = top + 126
    for side, lines, tm, bh, bw in laid:
        if side == "l":
            box = (M + 30, by, M + 30 + bw, by + bh)
            fill = GREY
        else:
            box = (W - M - 30 - bw, by, W - M - 30, by + bh)
            fill = GREEN
        d.rounded_rectangle(box, radius=22, fill=fill)
        yy = by + 18
        for ln in lines:
            d.text((box[0] + 26, yy), ln, font=fb, fill=INK)
            yy += int(30 * 1.35)
        d.text((box[2] - 62, box[3] - 30), tm, font=body(19, 700), fill=MUTED)
        by += bh + 22

    para(d, "Senin semangat. Rabu hilang. Bukan karena anaknya males.",
         body(38, 700), M, top + card_h + 50, W - 2 * M, 1.4, INK)
    foot(d, "")
    return img


def s_concept():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img); d._image = img
    header(d, 3, 8)
    d.text((M, 190), "kenalan dulu", font=body(30, 800), fill=CORAL)
    y = para(d, "Kenalan yuk sama microlearning", display(74, 800), M, 236, W - 2 * M, 1.15, INK)

    top = y + 44
    card(d, (M, top, W - M, top + 258), fill="#FFFFFF", outline=LINE)
    d.text((M + 44, top + 32), "microlearning", font=body(26, 800), fill=TEAL)
    para(d, "Materi kecil yang bisa berdiri sendiri: maksimal 5 menit, satu ide, satu aksi.",
         body(44, 700), M + 44, top + 82, W - 2 * M - 88, 1.38, INK)

    yy = top + 366
    f = body(40, 700)
    d.text((M, yy), "Bukan video 1 jam dipotong 12.", font=f, fill=MUTED)
    wpx = f.getlength("Bukan video 1 jam dipotong 12.")
    d.line([(M, yy + 40), (M + wpx, yy + 40)], fill=CORAL, width=7)

    para(d, "Sosis dipotong tipis ya tetap sosis, bukan sushi.", display(40, 800), M, yy + 84, W - 2 * M, 1.2, INK)

    card(d, (M, yy + 164, W - M, yy + 164 + 176), fill=PEACH, radius=28)
    para(d, "Microlearning itu unit utuh yang bisa dipakai sendirian. Bukan potongan dari yang panjang.",
         body(32, 700), M + 34, yy + 194, W - 2 * M - 68, 1.4, INK)
    foot(d, "")
    return img


def s_stat():
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img); d._image = img
    header(d, 4, 8)
    d.text((M, 196), "angka dari program yang Ian desain", font=body(28, 700), fill="#9FB0C8")
    d.text((M - 10, 244), "14%", font=display(300, 800), fill=CORAL)
    y = para(d, "yang selesai. 86% kabur di minggu kedua.", display(64, 800), M, 630, W - 2 * M, 1.2, CREAM)
    y = para(d, "Bukan karena pesertanya males. 45 menit sekali duduk itu kebanyakan buat kepala yang udah penuh.",
             body(38, 600), M, y + 28, W - 2 * M, 1.45, "#C9D5E4")
    d.text((M, y + 28), "Di kelas anak, polanya sama. Cuma lebih cepat.", font=display(40, 800), fill=MUSTARD)
    foot(d, "")
    return img


def s_rules():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img); d._image = img
    header(d, 5, 8)
    d.text((M, 180), "biar nggak salah sebut", font=body(30, 800), fill=CORAL)
    y = para(d, "3 syarat microlearning", display(76, 800), M, 226, W - 2 * M, 1.15, INK)

    y += 40
    y = bullet_row(d, y, "Maksimal 5 menit per unit. Lewat dari itu, fokus udah keburu hilang.", num=1)
    y = bullet_row(d, y + 6, "Satu ide aja. Jangan rakus masukin warna, layout, dan tipografi sekaligus.", num=2)
    y = bullet_row(d, y + 6, "Ditutup satu aksi kecil yang bisa kelar dari HP.", num=3)

    card(d, (M, y + 40, W - M, y + 190), fill=PEACH, radius=30)
    para(d, "Kalau lewat 5 menit, namanya bukan microlearning. Namanya PR.",
         body(36, 800), M + 36, y + 72, W - 2 * M - 72, 1.35, INK)
    foot(d, "")
    return img


def s_example():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img); d._image = img
    header(d, 6, 8)
    d.text((M, 170), "contoh, tinggal comot", font=body(30, 800), fill=CORAL)
    y = para(d, "Misi pagi yang bisa kamu kirim besok", display(62, 800), M, 214, W - 2 * M, 1.16, INK)

    top = y + 44
    bx0, by0, bx1 = M + 34, top + 34, W - M - 60
    fb = body(32, 600)
    lines = [
        ("Misi Pagi 5 Menit: Bikin tokoh kamu punya cacat unik", True),
        ("", False),
        ("Tokoh yang terlalu sempurna itu bosenin. Superman aja lemes kena batu hijau.", False),
        ("", False),
        ("Tentukan SATU hal aneh yang bikin tokoh kamu panik setengah mati.", False),
        ("", False),
        ("Ketik nama tokoh + kelemahannya di grup ini sekarang.", False),
    ]
    yy = by0 + 30
    laid = []
    for text, bold in lines:
        f = body(32, 800) if bold else fb
        if not text:
            yy += 18
            continue
        for ln in wrap(text, f, bx1 - bx0 - 60):
            laid.append((ln, f, yy))
            yy += int(32 * 1.4)
    bh = yy + 48 - by0
    card(d, (M, top, W - M, by0 + bh + 34), fill="#ECE5DD", radius=36)
    d.rounded_rectangle((bx0, by0, bx1, by0 + bh), radius=24, fill=GREEN)
    for ln, f, yl in laid:
        d.text((bx0 + 30, yl), ln, font=f, fill=INK)
    d.text((bx1 - 96, by0 + bh - 32), "07:02", font=body(20, 700), fill="#5E7B52")
    d.text((bx1 - 44, by0 + bh - 34), "\u2713\u2713", font=body(20, 700), fill="#4F9BD9")

    para(d, "30 detik baca, 10 detik ngetik. Nggak perlu buka laptop, nggak perlu login.",
         body(34, 700), M, by0 + bh + 80, W - 2 * M, 1.35, INK)
    foot(d, "")
    return img


def s_recipe():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img); d._image = img
    header(d, 7, 8)
    d.text((M, 170), "yang bikin mereka balik", font=body(30, 800), fill=CORAL)
    y = para(d, "Satu proyek = 5 keping, bukan 1 batu", display(64, 800), M, 212, W - 2 * M, 1.16, INK)

    rows = [("Senin", "nama tokoh + satu kelemahan konyol"),
            ("Selasa", "tempat tinggal, satu foto referensi"),
            ("Rabu", "dua kalimat dialog pas tokoh kesel"),
            ("Kamis", "satu masalah mendadak"),
            ("Jumat", "sambung 4 catatan jadi draf cerita")]
    y += 34
    for i, (day, txt) in enumerate(rows):
        card(d, (M, y, W - M, y + 74), fill="#FFFFFF", radius=22, outline=LINE)
        d.text((M + 26, y + 22), day, font=body(28, 800), fill=TEAL)
        d.text((M + 160, y + 20), txt, font=body(30, 700), fill=INK)
        y += 84

    card(d, (M, y + 20, W - M, y + 190), fill=MUSTARD, radius=30)
    d.text((M + 34, y + 46), "Kirim jam 7 pagi, bukan jam 2 siang.", font=body(34, 800), fill=INK)
    para(d, "Tangki willpower paling penuh habis bangun tidur.",
         body(30, 600), M + 34, y + 96, W - 2 * M - 68, 1.35, "#4A3B14")
    foot(d, "")
    return img


def s_cta():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img); d._image = img
    header(d, 8, 8)
    y = para(d, "Simpan dulu. Dipakai pas liburan.", display(76, 800), M, 250, W - 2 * M, 1.15, INK)

    y = para(d, "Versi lengkapnya 1.300 kata: anatomi pesan WA-nya, contoh misi lain, dan kenapa jam 7 pagi penting.",
             body(38, 600), M, y + 40, W - 2 * M, 1.45, INK)

    top = y + 50
    card(d, (M, top, W - M, top + 240), fill=INK)
    d.text((M + 40, top + 34), "catatan lengkapnya di", font=body(26, 700), fill="#9FB0C8")
    d.text((M + 40, top + 76), "iansnotebook.my.id", font=display(52, 800), fill=CORAL)
    d.text((M + 40, top + 160), "tiap Rabu & Jumat, satu resep 5 menit", font=body(26, 600), fill="#C9D5E4")

    ny = top + 300
    d.text((M, ny), "Follow @cerivitas", font=display(46, 800), fill=TEAL)
    para(d, "buat proyek kreatif yang bisa dikerjain anak beneran.",
         body(32, 600), M, ny + 66, W - 2 * M, 1.4, MUTED)
    foot(d, "")
    return img


SLIDES = {
    "microlearning": [s_cover, s_pain, s_concept, s_stat, s_rules, s_example, s_recipe, s_cta],
}


def render(slug, outdir):
    out = pathlib.Path(outdir); out.mkdir(parents=True, exist_ok=True)
    paths = []
    for i, fn in enumerate(SLIDES[slug], 1):
        p = out / f"slide-{i}.png"
        fn().save(p)
        paths.append(p)
    return paths


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", choices=list(SLIDES))
    ap.add_argument("--out", default="/tmp/ig-carousel")
    a = ap.parse_args()
    for p in render(a.slug, a.out):
        print(p)
