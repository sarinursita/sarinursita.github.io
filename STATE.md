# STATE.md

<!-- Ditimpa setiap akhir sesi. Satu-satunya sumber posisi kerja. -->

## Now

**Catatan Nik edisi evaluasi pra-UTS: SUDAH TERBIT SEMUA (5 post, 21 Nov 2026).**
Sari memutuskan publish borongan hari ini (bukan bertahap 23-27 Nov seperti rencana awal), karena UTS Senin 23 Nov.

| # | Post | Matkul | Jam terbit |
|---|---|---|---|
| 037 | `catatan-nik-evaluasi-ssad-m07` | SSAD | 05:50 |
| 038 | `catatan-nik-evaluasi-implementasi-ai-m07` | IAI | 06:00 |
| 039 | `catatan-nik-evaluasi-software-design-m07` | Software Design | 06:10 |
| 040 | `catatan-nik-evaluasi-smart-information-system-m07` | SIS | 06:20 |
| 041 | `catatan-nik-evaluasi-metodologi-penelitian-m07` | Metpen | 06:30 |

- `draft: false` kelimanya; tanggal digeser ke 21 Nov (jam-jamnya sudah lewat saat publish).
- Deploy: GitHub Actions run `44897612021` success; kelima URL dicek balas 200.
- Halaman matkul `msi.cerivitas.com/materi/<matkul>/` sekarang menaut "Refleksi Catatan Nik sebelum UTS" ke post evaluasi masing-masing (msi-study commit `06a3472`).

**Antrean draft blog: kosong.**

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

- 2026-11-21 · wiz · 5 catatan Nik evaluasi pra-UTS terbit sekaligus (SSAD/IAI/SD/SIS/Metpen), tautan dari halaman matkul msi-study disambungkan
- 2026-11-09 · wiz · Catatan Nik #030 SSAD m06 tayang 05:32 WIB; #031 SD m06 masih draft (WS 1702)
- 2026-11-08 · wiz · Jurnal Ana PCPS101 S4 tayang (msg 21710, date tetap 7 Nov); sesi 5 (3 draft) siap di WS 1697-1699
- 2026-11-05 · wiz · Jurnal Ana PLDP101 S4 tayang (msg 21708, 1.781 kata); aturan nama murid: boleh berulang kalau anak sama, jangan jadi default
- 2026-11-04 · wiz · Ian Ep014 (ADDIE) tayang; Ep013 revisi kanon Nadia (lemburan/tapi karena); POST-LOG 013-014 dirapikan
- 2026-11-03 · max · Pindah blog ke domain sendiri `sarinursita.my.id` (DNS + Pages + HTTPS live)
- 2026-11-03 · wiz · Dean: PCPS live, 4 matkul approved, WA format dirapikan (kopi + ceklist)
- 2026-11-04 · wiz · Catatan Nik #026 SD m05: draft 2.867 kata, guardrail sweep, WS 1668/21752
