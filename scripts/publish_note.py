#!/usr/bin/env python3
"""Tayangin satu WS *note* (bukan chat) jadi post blog, lengkap dengan metadata.

Bedanya dengan daily_blog.py: daily_blog.py menarik **pesan chat** (pipeline persona
Ian's Notebook / Catatan Nik, ada gerbang approve + ws_chat/ws_msg). Script ini menarik
**note** WS (`/api/note/<id>`) — dipakai untuk tulisan yang Sari tulis/ketik sendiri di
catatan project WS: balasan ke post persona, catatan kelas, catatan proyek. Karena yang
punya tulisan itu Sari sendiri, tidak ada gerbang approve: `draft: false` langsung.

Alur:
  1. tarik note dari WS  ->  GET /api/note/<id>
  2. rapikan body (CRLF, H1, footer link mentah -> link markdown yang bisa diklik)
  3. tulis content/blog/<slug>.md dengan front matter lengkap
  4. hugo build lokal sebagai cek (lewati dengan --no-build)
  5. pull --rebase, commit, push origin main
  6. tunggu live, cetak link yang bisa diklik

Contoh:
  python3 scripts/publish_note.py --note 1839 --dry-run
  python3 scripts/publish_note.py --note 1839 \
      --title "Balasan untuk Ian: Tiga Topi Ajaib" \
      --subtitle "Balasan untuk Ian's Notebook #001: Tiga Topi Ajaib" \
      --category Kelas --tags "balasan,kelas-online,tiga-topi-pendidik" \
      --summary "..." --hook "..."

Aturan: lihat skill `ws-note-to-blog` (metadata, formatting, link). Script ini tidak
menulis prosa — prosa metadata (title/summary/hook) ditulis dulu, baru dioper ke sini.
"""
import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys
import time
import urllib.request
import zoneinfo

REPO = pathlib.Path(__file__).resolve().parents[1]
BLOG_DIR = REPO / "content" / "blog"
BASE_URL = "https://sarinursita.github.io"
WS_BASE = "http://43.134.103.31:58234"
WS_API = WS_BASE + "/api"
SECURE_KEY_FILE = pathlib.Path("/home/saristudio/secure/writerstudio-apikey.md")
AUTHOR = ["-c", "user.name=Sari Nursita", "-c", "user.email=sari.nursita@gmail.com"]
TZ = zoneinfo.ZoneInfo("Asia/Jakarta")


# ---------- WS ----------

def ws_key():
    lines = SECURE_KEY_FILE.read_text(encoding="utf-8").split("\n")
    i = next(i for i, l in enumerate(lines) if l.startswith("## PROD"))
    return next(l for l in lines[i:] if l.startswith("- Key:")).split(":", 1)[1].strip()


def ws_get(path):
    req = urllib.request.Request(WS_API + path, headers={"Authorization": "Bearer " + ws_key()})
    return json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore"), strict=False)


def get_note(note_id):
    data = ws_get("/note/%s" % note_id)
    if "note" not in data:
        raise RuntimeError("note %s tidak ketemu: %s" % (note_id, str(data)[:200]))
    return data["note"]


# ---------- blog helpers ----------

def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    return (m.group(1), m.group(2)) if m else ("", text)


def field(fm, name, default=""):
    mm = re.search(r"^%s:\s*(.+?)\s*$" % name, fm, re.M)
    if not mm:
        return default
    val = mm.group(1).strip()
    return val[1:-1] if len(val) > 1 and val[0] == '"' and val[-1] == '"' else val


def page_title(slug):
    """Judul post lain yang sudah ada, buat label link internal."""
    f = BLOG_DIR / (slug + ".md")
    if f.exists():
        return field(front_matter(f.read_text(encoding="utf-8"))[0], "title")
    return ""


def page_label(slug):
    """Label pendek link internal: `Ian's Notebook #001` (bukan judul penuh yang panjang)."""
    title = page_title(slug)
    short = title.split(":")[0].strip() if title else slug
    m = re.search(r"-(\d{3})-", slug)
    if m:
        short = "%s #%s" % (short, m.group(1))
    return short


def yaml_str(s):
    """JSON string = YAML double-quoted scalar yang aman."""
    return json.dumps(" ".join(s.split()), ensure_ascii=False)


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.UNICODE)
    return re.sub(r"[\s_]+", "-", s).strip("-")


# ---------- body ----------

BARE_URL = re.compile(r"(?<![\(\[])(?<!\]\()(https?://[^\s)<>\"']+)")


def linkify(text, reply_label=None):
    """Ubah URL mentah jadi link markdown. URL blog sendiri -> label = judul post-nya."""
    def repl(m):
        url = m.group(1).rstrip(".,")
        trail = m.group(1)[len(url):]
        mm = re.match(r"^https?://sarinursita\.github\.io/blog/([^/?#]+)/?$", url)
        label = page_label(mm.group(1)) if mm else None
        label = label or reply_label or url
        return "[%s](%s)%s" % (label, url, trail)

    return BARE_URL.sub(repl, text)


REPLY_LINE = re.compile(r"^(this post is my reply to|balasan ini untuk)\s+(.*?)\s*[-–:]\s*(https?://\S+)\s*$", re.I | re.M)


def tidy_reply_line(text, reply_label=None):
    """`This post is my reply to Ian's Notebook - <url>` -> kalimat yang sama tapi linknya bisa diklik,
    tanpa pengulangan nama seri (`Ian's Notebook - Ian's Notebook #001`)."""
    def repl(m):
        url = m.group(3).rstrip(".,")
        if reply_label:
            return "%s [%s](%s)." % (m.group(1)[0].upper() + m.group(1)[1:], reply_label, url)
        return "%s [%s](%s)." % (m.group(1)[0].upper() + m.group(1)[1:], m.group(2).strip(), url)

    return REPLY_LINE.sub(repl, text)


def format_body(content, reply_label=None):
    """Sari punya tulisan di note. Fungsi ini CUMA nambah markup + benerin link;
    kalimatnya tidak diubah."""
    text = content.replace("\r\n", "\n").replace("\r", "\n")
    lines = [l.rstrip() for l in text.split("\n")]

    # header ekspor WS (kalau ada) dibuang: baris sebelum --- pertama
    if lines and lines[0].strip() == "---":
        try:
            end = lines.index("---", 1)
            lines = lines[end + 1:]
        except ValueError:
            pass

    while lines and not lines[0].strip():
        lines.pop(0)
    # judul sudah di front matter
    while lines and lines[0].startswith("# "):
        lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)

    body = "\n".join(lines).strip("\n")

    # footer "This post is my reply to X - <url>" -> tanpa pemisah --- mentah
    parts = re.split(r"\n-{3,}\n", body)
    if len(parts) > 1 and re.search(r"https?://", parts[-1]):
        body = parts[0].rstrip() + "\n\n" + parts[-1].strip()

    body = tidy_reply_line(body, reply_label)
    body = linkify(body, reply_label)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.rstrip() + "\n"


def dash_report(body):
    hits = []
    for i, l in enumerate(body.split("\n"), 1):
        if "—" in l or "–" in l:
            hits.append((i, l.strip()[:90]))
    return hits


# ---------- publish ----------

def build_front_matter(note, title, subtitle, category, tags, summary, hook, draft, now, reply_to):
    rows = [
        ("title", yaml_str(title)),
        ("subtitle", yaml_str(subtitle)) if subtitle else None,
        ("type", "blog"),
        ("date", now.isoformat()),
        ("draft", "true" if draft else "false"),
        ("ws_note", str(note["id"])),
        ("ws_project", str(note.get("project_id", ""))),
        ("category", yaml_str(category)) if category else None,
        ("tags", "[%s]" % ", ".join(yaml_str(t) for t in tags)) if tags else None,
        ("summary", yaml_str(summary)) if summary else None,
        ("hook", yaml_str(hook)) if hook else None,
        ("reply_to", yaml_str(reply_to)) if reply_to else None,
    ]
    return "\n".join("%s: %s" % (k, v) for k, v in rows if v)


def git(*args, check=True):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, check=check)


def wait_live(url, key, tries=16):
    """Maks ~4 menit: build GitHub Actions biasanya 1-2 menit. Jangan lebih lama,
    biar script tetap selesai di dalam timeout tool/cron."""
    for _ in range(tries):
        try:
            html = urllib.request.urlopen(url, timeout=20).read().decode("utf-8", "ignore")
            if not key or key in html:
                return True
        except Exception:
            pass
        time.sleep(15)
    return False


def reply_label_for(url):
    """Label link = judul pendek post blog kita sendiri (kalau URL-nya internal)."""
    mm = re.match(r"^https?://sarinursita\.github\.io/blog/([^/?#]+)/?$", url or "")
    return page_label(mm.group(1)) if mm else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--note", required=True, help="id note WS")
    ap.add_argument("--slug")
    ap.add_argument("--title")
    ap.add_argument("--subtitle")
    ap.add_argument("--category")
    ap.add_argument("--tags", help="dipisah koma")
    ap.add_argument("--summary")
    ap.add_argument("--hook")
    ap.add_argument("--reply-to", dest="reply_to", default="", help="URL post yang dibalas (jadi link di footer)")
    ap.add_argument("--draft", action="store_true", help="tahan sebagai draft (jangan tayang)")
    ap.add_argument("--backlink", help="slug post yang dibalas: tambahkan link ke post baru ini di akhir post itu")
    ap.add_argument("--dry-run", action="store_true", help="cetak hasilnya, jangan tulis/push")
    ap.add_argument("--no-build", action="store_true", help="lewati hugo build lokal")
    a = ap.parse_args()

    note = get_note(a.note)
    title = a.title or re.sub(r"^\s*re:\s*", "", note["name"].replace("-", ": ", 1), flags=re.I).strip()
    slug = a.slug or slugify(title)
    tags = [t.strip() for t in (a.tags or "").split(",") if t.strip()]
    if not a.summary:
        first = next((p for p in format_body(note["content"]).split("\n\n") if p.strip()), "")
        a.summary = " ".join(first.split())[:220]
    if not a.hook:
        a.hook = a.summary

    body = format_body(note["content"], reply_label=reply_label_for(a.reply_to))

    now = datetime.datetime.now(TZ)
    fm = build_front_matter(note, title, a.subtitle, a.category, tags, a.summary, a.hook, a.draft, now, a.reply_to)
    out = "---\n%s\n---\n\n%s" % (fm, body)

    print("📝 note #%s  \"%s\"  (project %s, dibuat %s)" % (note["id"], note["name"], note.get("project_id"), note.get("created_at", "?")[:16]))
    print("   slug : content/blog/%s.md" % slug)
    print("   kata : %d" % len(body.split()))
    hits = dash_report(body)
    print("   em/en dash: %d %s" % (len(hits), hits if hits else ""))

    if a.dry_run:
        print("\n" + out)
        return

    path = BLOG_DIR / (slug + ".md")
    if path.exists():
        print("⚠️ %s sudah ada — batal. Pakai --slug lain atau edit file itu langsung." % path.name)
        sys.exit(1)
    path.write_text(out, encoding="utf-8")
    print("   tulis : %s" % path.relative_to(REPO))

    # link balik di post yang dibalas, biar pembacanya bisa langsung klik ke balasan ini
    extra, backlink_src, backlink_old = [], None, None
    if a.backlink:
        src = BLOG_DIR / (a.backlink + ".md")
        if not src.exists():
            print("⚠️ --backlink %s: file tidak ada, link balik dilewati." % a.backlink)
        else:
            backlink_src = src
            backlink_old = src.read_text(encoding="utf-8")
            line = "*Sari sudah balas catatan ini: [%s](%s/blog/%s/)*" % (title, BASE_URL, slug)
            if line in backlink_old:
                print("   balik : link balik sudah ada di %s" % src.name)
            else:
                src.write_text(backlink_old.rstrip() + "\n\n---\n\n" + line + "\n", encoding="utf-8")
                extra.append(str(src.relative_to(REPO)))
                print("   balik : %s -> link ke %s" % (src.name, slug))

    if not a.no_build:
        r = subprocess.run(["hugo", "--minify", "--cleanDestinationDir"], cwd=str(REPO), capture_output=True, text=True)
        if r.returncode != 0:
            path.unlink()
            if backlink_src is not None and backlink_old is not None:
                backlink_src.write_text(backlink_old, encoding="utf-8")
            print("⚠️ hugo build gagal, file dibatalkan:\n%s" % (r.stderr or r.stdout)[-1500:])
            sys.exit(1)
        print("   build : ok (%s)" % next((l.strip() for l in r.stdout.splitlines() if "pages" in l), ""))

    try:
        git("pull", "--rebase", "origin", "main", check=False)
        git("add", str(path.relative_to(REPO)), *extra)
        git(*AUTHOR, "commit", "-m", "Publish %s (WS note %s)" % (slug, note["id"]))
        git("push", "origin", "main")
        print("   push  : ok")
    except subprocess.CalledProcessError as e:
        print("⚠️ gagal push:\n%s" % ((e.stderr or e.stdout or str(e)).strip()[:400]))
        sys.exit(1)

    url = "%s/blog/%s/" % (BASE_URL, slug)
    key = " ".join(body.split()[:8])
    if wait_live(url, key):
        print("\n✅ *Tayang:* [%s](%s)" % (title, url))
    else:
        print("\n⚠️ sudah di-push tapi belum kebaca live (>5 menit): %s" % url)


if __name__ == "__main__":
    main()
