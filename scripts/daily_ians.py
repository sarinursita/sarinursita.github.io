#!/usr/bin/env python3
"""Ian's Notebook — pengingat pagi + tayang setelah Sari approve.

Dipakai cron Sen/Rab/Jum 05:20 WIB lewat agent (job `attach_to_session`, jadi Sari bisa balas di thread).

  python3 daily_ians.py              -> mode PENGINGAT: cetak payload untuk #tekpen-digest,
                                        berisi judul + hook + link WS (draft dibaca di WS). Kosong kalau tidak ada post jatuh tempo.
  python3 daily_ians.py --approve    -> mode TAYANG: ambil isi post dari WS (versi terbaru, termasuk kalau Sari edit di WS),
                                        tulis ke file blog, draft: false, commit, push, tunggu live, cetak link blog.

Alur: Minggu batch generate -> draft di blog repo (draft: true) + chat WS -> Sen/Rab/Jum pagi kirim link WS ->
Sari baca/edit di WS -> balas `ok` -> script dijalankan dengan --approve -> post tayang di blog.
"""
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
PROJECT_ID = 155
SECURE_KEY_FILE = pathlib.Path("/home/saristudio/secure/writerstudio-apikey.md")
AUTHOR = ["-c", "user.name=Sari Nursita", "-c", "user.email=sari.nursita@gmail.com"]
TZ = zoneinfo.ZoneInfo("Asia/Jakarta")


# ---------- helpers ----------

def git(*args, check=True):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, check=check)


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("front matter tidak ketemu")
    return m.group(1), m.group(2)


def field(fm, name, default=""):
    mm = re.search(r"^%s:\s*(.+?)\s*$" % name, fm, re.M)
    if not mm:
        return default
    val = mm.group(1).strip()
    return val[1:-1] if len(val) > 1 and val[0] == '"' and val[-1] == '"' else val


def ws_key():
    lines = SECURE_KEY_FILE.read_text(encoding="utf-8").split("\n")
    i = next(i for i, l in enumerate(lines) if l.startswith("## PROD"))
    return next(l for l in lines[i:] if l.startswith("- Key:")).split(":", 1)[1].strip()


def ws_get(path):
    req = urllib.request.Request(WS_API + path, headers={"Authorization": "Bearer " + ws_key()})
    return json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore"), strict=False)


def normalize_body(body):
    """Buang H1 (judul sudah di front matter) + rapikan tanda tangan + buang header ekspor WS."""
    lines = body.strip("\n").split("\n")
    while lines and (lines[0].strip() == "" or lines[0].startswith("# ")):
        if lines[0].startswith("# "):
            lines = lines[1:]
            break
        lines = lines[1:]
    body = "\n".join(lines).strip("\n")
    body = re.sub(r"\n\*\*Ian\*\*\s*$", "\n— Ian", body)
    body = re.sub(r"\n- Ian\s*$", "\n— Ian", body)
    return body.rstrip() + "\n"


def queued():
    """Semua post yang masih draft, urut tanggal."""
    out = []
    for f in sorted(BLOG_DIR.glob("ians-notebook-*.md")):
        fm, body = front_matter(f.read_text(encoding="utf-8"))
        if field(fm, "draft") == "true":
            out.append((f, fm, body))
    out.sort(key=lambda x: field(x[1], "date"))
    return out


def ws_content(chat_id, msg_id):
    data = ws_get("/chat/%s/messages" % chat_id)
    msgs = data.get("messages", [])
    if msg_id:
        for m in msgs:
            if str(m.get("id")) == str(msg_id):
                return m.get("content") or ""
        raise RuntimeError("pesan WS %s tidak ketemu di chat %s" % (msg_id, chat_id))
    ai = [m for m in msgs if m.get("sender") != "user"]
    if not ai:
        raise RuntimeError("tidak ada pesan model di chat WS %s" % chat_id)
    return ai[-1].get("content") or ""


def wait_live(url, key):
    for _ in range(30):
        try:
            html = urllib.request.urlopen(url, timeout=20).read().decode("utf-8", "ignore")
            if key and key in html:
                return True
        except Exception:
            pass
        time.sleep(15)
    return False


# ---------- mode ----------

def mode_reminder():
    today = datetime.datetime.now(TZ).date()
    for f, fm, body in queued():
        d = field(fm, "date")
        if not d or datetime.date.fromisoformat(d[:10]) != today:
            continue
        chat = field(fm, "ws_chat")
        out = [
            "📖 *Ian's Notebook hari ini*", "",
            "*%s*" % field(fm, "title"),
            field(fm, "hook"), "",
            "📝 *Masih draft* — baca nyamannya di WS:",
            "%s/view-chat.php?project_id=%s&chat_id=%s" % (WS_BASE, PROJECT_ID, chat), "",
            "_Kalau udah oke, balas `ok` di sini, nanti aku tayangin ke blog. Mau ngubah dulu? Edit langsung di WS, aku ambil versi terakhirnya._",
        ]
        print("\n".join(out))
        return
    # tidak ada yang jatuh tempo -> tidak mengirim apa pun


def mode_approve(slug=None):
    cands = queued()
    if slug:
        cands = [c for c in cands if c[0].stem == slug]
    if not cands:
        print("⚠️ Tidak ada post Ian's Notebook yang menunggu tayang.")
        return
    today = datetime.datetime.now(TZ).date()
    due = [c for c in cands if field(c[1], "date")[:10] == today.isoformat()]
    path, fm, body = (due or cands)[0]
    chat_id, msg_id = field(fm, "ws_chat"), field(fm, "ws_msg")
    title = field(fm, "title")

    # `publish_from: file` = teks di repo yang dipakai (dipakai kalau editnya diterapkan
    # ke file, bukan diedit Sari di WS). Default: ambil versi terbaru dari WS.
    if field(fm, "publish_from", "ws") == "file":
        print("(pakai versi di repo, bukan tarik dari WS)")
    else:
        try:
            fresh = normalize_body(ws_content(chat_id, msg_id))
            if len(fresh.split()) < 400:
                raise RuntimeError("isi WS kelihatan terpotong (%d kata)" % len(fresh.split()))
            body = fresh
        except Exception as e:
            print("⚠️ Gagal ambil isi terbaru dari WS (%s) — pakai isi yang sudah ada di repo." % e)

    now = datetime.datetime.now(TZ)
    fm_new = re.sub(r"^draft:\s*true", "draft: false", fm, count=1, flags=re.M)
    fm_new = re.sub(r"^date:\s*.*$", "date: %s" % now.isoformat(), fm_new, count=1, flags=re.M)
    path.write_text("---\n%s\n---\n\n%s" % (fm_new, body), encoding="utf-8")

    try:
        git("pull", "--rebase", "origin", "main", check=False)
        git("add", str(path.relative_to(REPO)))
        git(*AUTHOR, "commit", "-m", "Publish " + path.stem)
        git("push", "origin", "main")
    except subprocess.CalledProcessError as e:
        print("⚠️ Gagal push post Ian's Notebook:\n%s" % ((e.stderr or e.stdout or str(e)).strip()[:300]))
        return

    url = "%s/blog/%s/" % (BASE_URL, path.stem)
    key = re.sub(r"^Ian's Notebook:\s*", "", title).split(":")[0][:40].strip()
    if wait_live(url, key):
        print("✅ *Tayang:* [%s](%s)\n_Dari %d kata, versi terakhir dari WS._" % (title, url, len(body.split())))
    else:
        print("⚠️ Sudah di-push tapi belum kebaca live (>5 menit): %s" % url)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    if args and args[0] == "--approve":
        mode_approve(args[1] if len(args) > 1 else None)
    else:
        mode_reminder()
