#!/usr/bin/env bash
# publish-dean-due.sh — tayangkan post Dean's Message yang SUDAH di-approve
# dan jam tayangnya sudah lewat. Dipanggil cron 2x sehari (06:00 & 12:00 WIB).
# Aman: hanya menyentuh file deans-message-*.md dengan approved: true.
set -euo pipefail
cd /home/saristudio/repos/sarinursita.github.io
git pull --quiet origin main || true

now=$(TZ=Asia/Jakarta date +%s)
changed=0

for f in content/blog/deans-message-*.md; do
  [ -e "$f" ] || continue
  grep -q '^approved: true' "$f" || continue
  grep -q '^draft: true' "$f" || continue
  d=$(grep -m1 '^date: ' "$f" | cut -d' ' -f2)
  ds=$(TZ=Asia/Jakarta date -d "$d" +%s 2>/dev/null || echo 0)
  [ "$ds" -le "$now" ] || continue
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
  git push origin main --quiet || true
  echo "$(TZ=Asia/Jakarta date '+%F %H:%M WIB') tayang $changed post"
else
  echo "$(TZ=Asia/Jakarta date '+%F %H:%M WIB') tidak ada post due"
fi
