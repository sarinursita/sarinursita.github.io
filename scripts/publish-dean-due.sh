#!/usr/bin/env bash
# publish-dean-due.sh — tayangkan post Dean's Message yang SUDAH di-approve
# dan jam tayangnya sudah lewat. Dipanggil cron 2x sehari (06:00 & 12:00 WIB).
# Aman: hanya menyentuh file deans-message-*.md dengan approved: true.
set -euo pipefail
cd /home/saristudio/repos/sarinursita.github.io
git pull --quiet origin main || true

stamp=$(TZ=Asia/Jakarta date '+%F %H:%M WIB')
now=$(TZ=Asia/Jakarta date +%s)
changed=0
skipped=()

for f in content/blog/deans-message-*.md; do
  [ -e "$f" ] || continue
  name=$(basename "$f" .md | sed 's/^deans-message-//')
  # sudah tayang, bukan urusan kita
  grep -q '^draft: true' "$f" || continue
  # belum di-approve -> catat alasannya, jangan diam-diam
  if ! grep -q '^approved: true' "$f"; then
    skipped+=("$name (belum approved)")
    continue
  fi
  d=$(grep -m1 '^date: ' "$f" | cut -d' ' -f2)
  ds=$(TZ=Asia/Jakarta date -d "$d" +%s 2>/dev/null || echo 0)
  if [ "$ds" -gt "$now" ]; then
    skipped+=("$name (jadwal $(TZ=Asia/Jakarta date -d "$d" '+%d %b %H:%M'))")
    continue
  fi
  python3 - "$f" <<'PY'
import re,sys
p=sys.argv[1]; t=open(p).read()
t=re.sub(r'^draft: true$','draft: false',t,count=1,flags=re.M)
open(p,'w').write(t)
PY
  git add "$f"
  /home/saristudio/repos/agent-router/bin/commit wiz -m "blog: tayang $(basename "$f" .md)" >/dev/null
  changed=$((changed+1))
done

if [ "$changed" -gt 0 ]; then
  # repo blog hanya punya remote origin = GitHub; jangan pakai askpass Gitea
  if git push origin main --quiet; then
    echo "$stamp tayang $changed post: OK"
  else
    echo "$stamp TAYANG $changed post TAPI PUSH GAGAL - cek manual: pull dulu, lalu git push origin main" >&2
    exit 1
  fi
else
  echo "$stamp tidak ada post due${skipped[*]:+ | nunggu: ${skipped[*]}}"
fi
