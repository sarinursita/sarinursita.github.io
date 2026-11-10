---
title: "Catatan Nik: Bau Debu Gipsum Lantai 28, Migrasi Abal-Abal, dan Hype Deep Learning yang Bikin Pusing"
subtitle: "Ruang server di lantai 28 digusur pagi ini, sistem dipaksa pindah ke cloud tanpa uji penuh, dan Vina sudah menjual model mirip ChatGPT ke klien sebelum satu baris data kami beres."
type: blog
date: 2026-11-10T05:00:00+07:00
draft: true
ws_chat: 1687
ws_msg: 21905
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "implementasi-artificial-intelligence", "deep-learning", "catatan-nik"]
summary: "Materi pekan ini soal Deep Learning: bedanya sama machine learning biasa, cara jaringan saraf belajar dari kesalahannya sendiri, dan kenapa kata deep bukan berarti cerdas. Di kantor gue, migrasi cloud dadakan bikin data porak-poranda sementara Vina sudah menjanjikan model ala ChatGPT ke klien, padahal yang kami punya cuma 420 baris data bolong."
hook: "Kalau data cuma 420 baris dan sepertiganya bolong, model paling canggih pun cuma bisa salah dengan percaya diri."
---

Aroma karpet basah campur debu gipsum nyerang hidung gue begitu pintu lift lantai 28 kebuka. Ruang *server* yang belasan tahun diam di sudut lorong timur pagi ini dibongkar kontraktor, diganti *VIP lounge* buat calon pembeli lahan komersial. Bor sama palu godam udah nyahut-nyahutan dari jam sembilan.

Efek sampingnya, migrasi ke *cloud* yang tadinya dijadwalin akhir kuartal dipotong jadi satu akhir pekan. Tanpa uji beban, tanpa validasi *pipeline*, tim disuruh mindahin sistem apa adanya. Senin pagi gue buka laptop langsung disambut puluhan tiket: *query* sistem valuasi *time out*, relasi tabel putus, *dashboard* internal cuma layar putih sama ikon muter.

Belum selesai gue baca tiket ketujuh, Vina mendarat di meja gue bawa *tumbler* kopi.

"Nik, barusan gue paparan ke calon klien konsorsium ritel. Gue bilang kantor kita lagi transisi ke *cloud* karena lagi *deploy* model *Deep Learning* mutakhir, mirip ChatGPT. Nanti sistem kita otomatis prediksi valuasi ribuan ruko cuma dari ketikan di kolom *prompt*."

Aris, yang di seberang meja lagi ngubek *log database* korup, nyaris tersedak air mineral.

"Vin, sistem yang jalan sekarang aja belum bisa bedain format tanggal transaksi versi regional sama versi lokal. Lo udah jualan *Deep Learning*?"

"Ya namanya juga jualan visi," Vina ngibasin tangan. "Kalau kita cuma bilang pakai statistik biasa, klien mana mau bayar mahal."

---

## Sebelum bahas *deep*, kita urutin dulu pohonnya

Sepulang dari rapat tadi gue sempetin buka modul. Baru dua paragraf, gue udah ngerti kenapa Vina gampang banget jualan kata *deep*: kedengerannya kayak mesin yang mikir. Padahal di modul, kata itu cuma nunjuk jumlah lapisan.

Urutannya begini. *Artificial Intelligence* itu payung paling lebar, isinya semua teknik biar mesin bisa niru kecerdasan, termasuk sistem aturan kaku kayak *if-else* di mesin absensi. Di dalamnya ada *Machine Learning*, mesin yang nyari pola sendiri dari data tanpa dikasih aturan satu-satu. *Deep Learning* ada di lapisan paling dalam: *Machine Learning* yang pakai jaringan saraf dengan banyak lapisan.

Nah, jaringan saraf itu apa? Ini yang bikin gue ngerem dan baca ulang. Jaringan saraf tiruan itu kumpulan unit kecil yang mereka sebut neuron, namanya dipinjem dari sel saraf di otak, tapi isinya cuma hitungan. Tiap neuron nerima beberapa angka masuk, misalnya luas bangunan, umur gedung, jarak ke tol. Angka-angka itu dikali bobot sesuai seberapa penting perannya, dijumlahin, terus ditambah angka penyeimbang namanya *bias*.

Hasilnya dilewatkan ke fungsi aktivasi, penyaring yang bikin jaringan bisa bengkok ngikutin pola, bukan cuma narik garis lurus. Yang paling sering dipakai namanya ReLU, aturannya sederhana banget: angka negatif jadi nol, angka positif dibiarkan. Tanpa fungsi ini, tumpukan lapisan secanggih apa pun bakal runtuh jadi satu hitungan linear biasa, alias regresi yang mahal.

Lapisan-lapisannya disusun jadi tiga bagian: input buat nerima data mentah, lapisan tersembunyi buat ngubah bentuk datanya, output buat ngeluarin jawaban. Yang bikin dia *deep* ya jumlah lapisan tersembunyi itu, bukan kualitas mikirnya.

Lo mungkin nanya, gimana dia bisa belajar. Ini bagian favorit gue. Data ngalir maju sampai keluar tebakan. Tebakan dibandingin sama jawaban asli, selisihnya dihitung. Selisih itu dikirim mundur lapis demi lapis buat tahu bobot mana yang paling bersalah, namanya *backpropagation*. Tiap bobot digeser sedikit ke arah yang bikin selisihnya mengecil, besar geserannya diatur *learning rate*. Geseran kelewat besar bikin model loncat-loncat nggak pernah mendarat, kelewat kecil bikin latihannya jalan kayak siput.

Bedanya sama *Machine Learning* biasa ada di siapa yang milih ciri. Regresi linear butuh lo tentuin sendiri kolom mana yang relevan, dan kalau kolomnya jelek ya modelnya jelek. *Deep Learning* nyari cirinya sendiri: lapisan awal nangkep garis dan sudut, lapisan tengah ngerangkai jadi atap dan kontur jalan, lapisan akhir kenal kawasan. Enak, tapi bayarannya data segudang dan GPU, kartu grafis buat hitungan berat, yang nagih listrik.

---

## Model bagus itu yang nggak sekadar hafal

Sorenya Aris nanya satu hal yang bikin gue sadar urusannya bukan cuma arsitektur. "Kalau nanti modelnya jadi, kita tahu dia bagus dari mana?"

Pertanyaan bagus, karena model yang kelihatan pintar bisa cuma hafal. Satu putaran penuh seluruh data latihan lewat jaringan namanya satu *epoch*. Data kami 420 baris, kalau dilatih dua ratus *epoch* modelnya bukan belajar pola, dia ngapal.

Itu *overfitting*: akurasi di data latihan nyaris sempurna, tapi ketemu data baru langsung ambruk. Kayak murid yang hafal kunci jawaban tapi nggak paham soalnya. Kebalikannya *underfitting*, modelnya terlalu dangkal sampai pola paling gampang pun nggak ketangkep.

Masalah kedua lebih susah dijelasin ke atasan: *black box*. Model bisa punya ratusan juta bobot, dan waktu dia bilang harga sewa ruko di koridor TB Simatupang bakal turun 30% tahun depan, gue nggak bisa nunjuk satu variabel penyebabnya. Buat tim valuasi yang tiap angka harus dipertanggungjawabkan di depan komite dan auditor bank, ini bukan detail kecil.

---

## Tiga bentuk jaringan, tiga jenis data

"Jadi kita butuh yang mana?" Vina nyela dari balik monitor.

Tergantung datanya, dan ini yang paling sering kelewat. *CNN* buat gambar: dia geser filter kecil ke seluruh piksel buat nyari pola lokal kayak tepi, sudut, tekstur. *RNN* buat data berurutan yang urutannya penting, misal harga sewa per bulan; dia bawa ingatan dari langkah sebelumnya. Versi yang ingatannya lebih tahan lama namanya LSTM. *Transformer* buat teks: dia nggak baca kata satu-satu, tapi ngeliat semua kata sekaligus dan ngitung mana yang paling nyambung sama mana. Ini fondasi ChatGPT.

Di luar tiga itu masih ada yang khusus bikin gambar, dan AlphaFold yang nebak bentuk protein. Buat sekarang cukup tahu mereka ada, nggak perlu gue bedah.

Balik ke Aris, gue minta dia buka dataset transaksi ruko Jakarta Selatan yang dia rapihin minggu lalu. 420 baris. Luas bangunan penuh, harga sewa historis bolong 35%, deskripsi kondisi fisik ditulis singkat-singkat, dan nggak ada satu pun foto bangunan.

"Vin, *Deep Learning* itu mesin roket. Butuh bahan bakar berton-ton dan landasan beton. Kalau bahan bakarnya solar setengah jeriken dan landasannya tanah becek, dia nggak terbang, dia meledak."

| Dimensi | Machine Learning biasa | Deep Learning |
| :--- | :--- | :--- |
| **Jumlah data** | Ratusan sampai puluhan ribu baris | Ratusan ribu sampai jutaan |
| **Jenis data** | Tabel rapi: spreadsheet, database | Gambar, audio, video, teks bebas |
| **Komputasi** | CPU laptop, hitungan menit | Klaster GPU, hitungan jam sampai hari |
| **Ciri** | Dipilih manual oleh analis | Dicari sendiri oleh lapisan jaringan |
| **Bisa dijelaskan?** | Ya, arah tiap variabel kelihatan | Susah, isi lapisannya terlalu rumit |

Di 420 baris tabel kayak punya Aris, *Deep Learning* hampir pasti kalah. Yang lebih masuk akal pohon keputusan kayak XGBoost, model yang nyusun aturan bercabang sendiri dari data, atau regresi yang dikasih pemahaman bisnis. Lebih murah, lebih cepat, dan yang paling penting: bisa dijelasin ke klien tanpa bilang "mesinnya misterius".

Vina diam beberapa detik, natap angka di monitor Aris yang masih berantakan gara-gara migrasi akhir pekan.

"Jadi kita nggak bisa pasang model kayak ChatGPT buat valuasi ruko minggu depan?"

"Bisa aja kalau lo mau kantor kita dituntut klien gara-gara salah hitung aset miliaran," sahut gue. "Langkah pertama bukan sewa GPU buat gaya-gayaan. Langkah pertama nambal pipa data yang bocor gara-gara ruang *server* digusur, rapihin kamus data, baru bangun model yang masuk akal buat ukuran portofolio kami."

Vina nghela napas panjang, lalu balik ke mejanya buat revisi surel klarifikasi ke calon klien sebelum janji manisnya jadi komitmen kontrak.

---

## Menurut Lo Gimana?

1. Kalau lo jadi gue, kriteria apa yang lo pakai buat bilang "ini memang butuh *Deep Learning*" ke tim sales, tanpa harus nunggu proyeknya gagal dulu?
2. Di industri yang diaudit, lo pilih akurasi lebih tinggi atau model yang bisa dijelasin? Batasnya di mana?
3. Punya data 420 baris yang sepertiganya bolong: lo bersihin dulu, atau turunin target proyeknya?

Debu gipsum di lantai 28 kayaknya baru reda menjelang tengah malam, barengan Aris yang akhirnya berhasil mindahin basis data cadangan ke klaster baru.

Gue balik dulu ke tiket yang numpuk. Jangan lupa makan siang, Sar.

Nik
