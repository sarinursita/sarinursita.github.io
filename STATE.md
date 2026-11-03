# STATE.md

<!-- Ditimpa setiap akhir sesi. Satu-satunya sumber posisi kerja. -->

## Now

**Seri baru: Dean's Message (Catatan UTS Andika, 6 matkul, Nov 2026).** Rubrik Collab Journal,
persona Dean (mubaleg tugas di Australia, S1 Psikologi Islam IOU, S2 Komunikasi + konseling
keluarga muslim). Surat ke Dika (adik kelas, semester 1, mondok). Bentuk: drama-first, bukan
rangkuman; nomor sesi DILARANG di badan cerita (cuma di peta materi + saran urutan baca).

Live: PPOP (2 Nov 08:15), PLDP (2 Nov 12:00), PCPS (3 Nov 06:29, telat dari slot 06:00 karena
approve datang jam 06:20). Semua 6 matkul sudah approved.
Sisa jadwal: ENES 3 Nov 12:00, PPIP 4 Nov 06:00, ISGS 4 Nov 12:00.

Slug pakai topik, bukan kode matkul (standar sama dengan catatan-nik):
deans-message-hukuman-bukan-perubahan, -anak-yang-terlalu-mudah-berpindah-tangan,
-celana-basah-di-ruang-konseling, -tiga-kali-buka-bab-yang-sama,
-sajadah-basah-hati-hidup, -pecah-sebelum-mimbar-berdiri.
Tiga slug lama pakai `aliases:` supaya link yang sudah beredar tidak 404. Tag `IOU` dibuang.

Catatan Nik **#026 (SD m05)** draft di queue: `content/blog/catatan-nik-software-design-m05.md`
(`draft: true`, WS chat 1668 / msg 21752, 2.867 kata).

## Next

1. Tunggu approve Sari per matkul → set `approved: true`, cron yang tayangin jam 06:00/12:00 WIB.
2. Urutan ikut jadwal kelas: PLDP (Sen pagi), PCPS (Sen malam), ENES (Sel pagi), PPOP (Sel malam),
   PPIP (Rab pagi), ISGS (Rab malam). PPOP udah tayang duluan, slotnya dipakai PLDP.

## Blockers / open questions

- — (link Gitea writing-repository 404 kalau dibuka tanpa login: repo private, bukan link salah)

## Dead ends (jangan diulang)

- Script `publish-dean-due.sh` sempat push pakai askpass Gitea; repo blog cuma punya remote
  `origin` = GitHub, push-nya gagal diam-diam (`|| true`). Sudah dibenerin: cukup `git push origin`.

## Deployment / domain

Situs sekarang di **https://sarinursita.my.id** (GitHub Pages, workflow `deploy.yml`).
- DNS di panel Sumopod (NS `ns1/ns2.sumopod.com`): 3× A root @ → 185.199.109/110/111.153
  (yang .108 belum ditambah, tidak wajib), CNAME `www` → `sarinursita.github.io`.
- `static/CNAME` = `sarinursita.my.id`, `hugo.toml` baseURL ikut domain baru.
- `www` + domain lama `sarinursita.github.io` dua-duanya 301 ke domain utama. HTTPS enforced.
- Sertifikat GitHub aktif s/d 2027-02-01. Branch `custom-domain` sudah di-merge ke `main`.

## Last session

- 2026-11-04 · wiz · Ian Ep014 (ADDIE) tayang; Ep013 revisi kanon Nadia (lemburan/tapi karena); POST-LOG 013-014 dirapikan
- 2026-11-03 · max · Pindah blog ke domain sendiri `sarinursita.my.id` (DNS + Pages + HTTPS live)
- 2026-11-03 · wiz · Dean: PCPS live, 4 matkul approved, WA format dirapikan (kopi + ceklist)
- 2026-11-04 · wiz · Catatan Nik #026 SD m05: draft 2.867 kata, guardrail sweep, WS 1668/21752
