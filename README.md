# sarinursita.github.io — situs personal Sari Nursita

Situs statis (**Hugo**) untuk **https://sarinursita.github.io** — portofolio buku &
blog. Tema mengikuti gaya theme WordPress *Twenty Twenty* (theme yang dipakai di
`sarinursita.wordpress.com`), supaya tampilannya senada tapi kontennya GitHub.

## Struktur

```
content/
  _index.md        # beranda (Tentang + Buku + tulisan terbaru)
  buku/            # halaman per buku (type: buku)
  blog/            # tulisan (type: blog)
layouts/           # theme (mirip Twenty Twenty)
assets/css/        # style.css + blocks.css
static/            # gambar, robots.txt
```

## Tambah konten

- **Buku baru:** buat `content/buku/<slug>.md` (front matter: `type: buku`, `title`,
  `cover`, `penerbit`, `penulis`, `halaman`, `tahun`, `buyLink`, `summary`).
- **Tulisan blog:** buat `content/blog/<slug>.md` (front matter: `type: blog`, `title`,
  `date`, opsional `category`, `cover`, `summary`, `subtitle`). Set `draft: false` untuk tayang.

## Rubrik Collab Journal

Blog ini punya rubrik **Collab Journal**: catatan belajar S2 yang ditulis bersama persona
fiktif (Max / Nik / Pak Sam). Aturan gaya, template, dan riwayat koreksi ada di
**[COLLAB-JOURNAL.md](COLLAB-JOURNAL.md)** — baca dulu sebelum menulis tulisan rubrik ini.

Komentar pembaca: **giscus** (GitHub Discussions, kategori *Announcements*), dipasang via
`layouts/partials/comments.html`.

## Build & deploy

Deploy otomatis: push ke `main` → GitHub Actions build Hugo → publish ke GitHub Pages.

```bash
hugo server -D      # preview lokal (termasuk draft)
hugo --minify       # build ke public/
```
