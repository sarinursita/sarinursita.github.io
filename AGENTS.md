# AGENTS.md — sarinursita.github.io

## What

Situs personal Sari Nursita di `https://sarinursita.my.id` (GitHub Pages, dulu sarinursita.github.io): portofolio buku dan blog. Hugo,
tema mengikuti gaya Twenty Twenty supaya senada dengan WordPress lama, tapi kontennya di GitHub.
Ini yang dimaksud user kalau bilang "blog".

## Map — source of truth

| Data | File |
|---|---|
| Struktur situs, alur tulis | `README.md` |
| Beranda | `content/_index.md` |
| Halaman buku | `content/buku/` (type `buku`) |
| Tulisan blog | `content/blog/` (type `blog`) |
| Template | `layouts/` |
| Aset | `assets/` |
| Jurnal kolaborasi | `COLLAB-JOURNAL.md` |
| Catatan IAN | `IAN-NOTEBOOK.md` |
| Portofolio lama | `_legacy-portfolio/` (arsip) |

## Run

```bash
hugo            # build
git push origin main   # GitHub Pages deploy
```

## Rules

- Konten baru = file markdown di `content/blog/` atau `content/buku/`. Jangan edit HTML hasil build.
- Tema meniru Twenty Twenty. Kalau mengubah layout, cek juga tampilan di ponsel.
- `git pull --rebase` sebelum menulis.
- `_legacy-portfolio/` hanya arsip, jangan dipakai lagi.

## Don't

- Jangan edit `public/` manual.
- Jangan commit secret/credential (ref: `vaultwarden:<item>/<field>`).
- Jangan mengubah struktur URL blog tanpa approval — sudah tersebar di media sosial.

## State

`STATE.md` — baca di awal sesi, **update sebelum berhenti**.
