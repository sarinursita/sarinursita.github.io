#!/usr/bin/env python3
"""Tayangkan post Ian's Notebook yang jatuh tempo hari ini, lalu cetak payload pesan.

Dijalankan cron Sen/Rab/Jum 05:15 WIB (no_agent, stdout = pesan yang dikirim ke #tekpen-digest).

Alur:
1. Cari post di content/blog/ians-notebook-*.md yang `date:`-nya = HARI INI (Asia/Jakarta).
2. Kalau masih `draft: true` -> ubah jadi `draft: false`, commit, push (memicu GitHub Actions build).
3. Tunggu URL-nya hidup (poll).
4. Cetak payload: judul + hook + link. Kalau tidak ada yang jatuh tempo: tidak mencetak apa pun.
"""
import datetime
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
AUTHOR = ["-c", "user.name=Sari Nursita", "-c", "user.email=sari.nursita@gmail.com"]

TODAY = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Jakarta")).date()


def git(*args, check=True):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, check=check)


def parse(text):
    """-> (front matter dict-ish accessor, body)"""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = m.group(1) if m else ""

    def field(name):
        mm = re.search(r'^%s:\s*(.+?)\s*$' % name, fm, re.M)
        if not mm:
            return ""
        val = mm.group(1).strip()
        if len(val) > 1 and val[0] == '"' and val[-1] == '"':
            val = val[1:-1]
        return val

    return field


def main():
    due = []
    for f in sorted(BLOG_DIR.glob("ians-notebook-*.md")):
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
        if m and datetime.date.fromisoformat(m.group(1)) == TODAY:
            due.append((f, text))

    if not due:
        return  # tidak ada yang jatuh tempo -> cron tidak mengirim apa pun

    path, text = due[0]
    field = parse(text)
    title, slug = field("title"), path.stem
    published_now = False

    if re.search(r"^draft:\s*true", text, re.M):
        try:
            git("pull", "--rebase", "origin", "main", check=False)
            path.write_text(re.sub(r"^draft:\s*true", "draft: false", text, count=1, flags=re.M), encoding="utf-8")
            git("add", str(path.relative_to(REPO)))
            git(*AUTHOR, "commit", "-m", "Publish " + slug)
            git("push", "origin", "main")
            published_now = True
        except subprocess.CalledProcessError as e:
            err = (e.stderr or e.stdout or str(e))
            print("⚠️ Post Ian's Notebook hari ini gagal ditayangkan: %s\n   %s" % (slug, err.strip()[:300]))
            return
        time.sleep(20)  # kasih waktu GitHub Actions mulai

    url = "%s/blog/%s/" % (BASE_URL, slug)
    key = re.sub(r"^Ian's Notebook:\s*", "", title)
    key = key.split(":")[0][:40].strip()
    live = False
    for _ in range(30):  # sampai ~5 menit
        try:
            html = urllib.request.urlopen(url, timeout=20).read().decode("utf-8", "ignore")
            if key in html:
                live = True
                break
        except Exception:
            pass
        time.sleep(15)

    if not live:
        print("⚠️ Post Ian's Notebook sudah di-push tapi belum kebaca live (>5 menit): %s" % url)
        return

    out = ["📖 *Ian's Notebook hari ini*", "", "*%s*" % title]
    hook = field("hook")
    if hook:
        out.append(hook)
    out.append(url)
    if published_now:
        out += ["", "_Baru tayang pagi ini._"]
    print("\n".join(out).strip())


if __name__ == "__main__":
    sys.exit(main())
