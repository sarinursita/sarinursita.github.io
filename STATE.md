# STATE.md

<!-- Ditimpa setiap akhir sesi. Satu-satunya sumber posisi kerja. -->

## Now

**Seri baru: Dean's Message (Catatan UTS Andika, 6 matkul, Nov 2026).** Rubrik Collab Journal,
persona Dean (mubaleg tugas di Australia, S1 Psikologi Islam IOU, S2 Komunikasi + konseling
keluarga muslim). Surat ke Dika (adik kelas, semester 1, mondok). Bentuk: drama-first, bukan
rangkuman; nomor sesi DILARANG di badan cerita (cuma di peta materi + saran urutan baca).

Tayang: PPOP 101 (2 Nov 08:15), PLDP 101 (2 Nov 12:00). Draft siap: PCPS, ENES, PPIP, ISGS
(flag `approved: false`, `draft: true`).

## Next

1. Tunggu approve Sari per matkul → set `approved: true`, cron yang tayangin jam 06:00/12:00 WIB.
2. Urutan ikut jadwal kelas: PLDP (Sen pagi), PCPS (Sen malam), ENES (Sel pagi), PPOP (Sel malam),
   PPIP (Rab pagi), ISGS (Rab malam). PPOP udah tayang duluan, slotnya dipakai PLDP.

## Blockers / open questions

- — (link Gitea writing-repository 404 kalau dibuka tanpa login: repo private, bukan link salah)

## Dead ends (jangan diulang)

- Script `publish-dean-due.sh` sempat push pakai askpass Gitea; repo blog cuma punya remote
  `origin` = GitHub, push-nya gagal diam-diam (`|| true`). Sudah dibenerin: cukup `git push origin`.

## Last session

- 2026-11-02 · wiz · Dean's Message: PPOP v4 live, PLDP live, 4 draft, cron publish 06/12 WIB
