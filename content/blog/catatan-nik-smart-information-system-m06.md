---
title: "Catatan Nik: Skor Ajaib di Layar Monitor, Prospek yang Hilang, dan Seni Menakar Keraguan"
subtitle: "Satu angka bulat di dashboard lebih dipercaya daripada keraguan yang sebenarnya bisa kami ukur, dan gue yang harus jelasin ke manajemen kenapa satu prospek besar lewat begitu saja."
type: blog
date: 2026-11-12T09:52:14.650011+07:00
draft: false
ws_chat: 1688
ws_msg: 21836
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "smart-information-system", "certainty-factor", "catatan-nik"]
summary: "Materi pekan ini soal dua cara mesin menakar keraguan: angka keyakinan yang memisahkan percaya dan ragu, lalu cara narik kesimpulan dari fakta yang sudah ada sebelum bertanya soal kesimpulan. Di kantor gue, skrip skor prioritas tanpa dokumentasi bikin satu prospek besar kelewat, dan yang paling kacau justru saat dua aturan harus dipilih salah satu."
hook: "Kalau dua aturan sama-sama bilang prioritas, siapa yang menang kalau nggak ada yang pernah nulis urutannya?"
---

Tangkapan layar spreadsheet dengan sel warna merah bata mendarat di grup percakapan tim tepat pukul tujuh pagi. Pengirimnya Vina, lengkap dengan tiga tanda seru dan satu kalimat pembuka yang langsung bikin tensi naik: *"Kenapa mandat gedung di Mega Kuningan nggak masuk daftar prioritas minggu lalu?"*

Gue masih memegang cangkir kopi pertama waktu membaca pesan itu. Di layar laptop, dashboard internal kami menampilkan angka keramat yang beberapa minggu ini diagung-agungkan di lantai 28 SCBD: skor prioritas prospek. Bentuknya sederhana, cuma angka bulat antara 0 sampai 100. Angka di atas 80 berarti tim bisnis harus langsung bergerak bikin proposal, sementara angka di bawah 50 otomatis masuk antrean dingin alias diabaikan dulu sampai ada waktu luang.

Masalahnya, gedung perkantoran tiga puluh lantai di Mega Kuningan itu cuma dapat skor 42.

Tadi pagi, kompetitor kami resmi pasang plang pengumuman sebagai agen tunggal penyewaan gedung tersebut. Komisi potensial bernilai ratusan juta amblas begitu saja ke tangan kantor sebelah, cuma gara-gara sistem internal kami menganggap prospek itu masuk kategori dingin.

Saat Vina menelepon dengan nada panik bercampur heran, gue menatap baris kode Python yang dikirim Aris lewat pesan pribadi. Aris menulis catatan pendek di bawahnya: *"Mbak, rumusnya cuma ngegabungin persentase dari form input. Katanya Mas Bram dulu pesannya yang penting ada angkanya dulu biar manajemen senang."*

Pagi itu, gue sadar satu hal: kantor kami sedang menjalankan operasional miliaran rupiah di atas ilusi kepastian. Kami sok tahu memberi angka pasti pada data yang sebenarnya penuh keraguan.

---

## Misteri Angka 42 dan Logika yang Saling Bertubrukan

Dashboard penentu nasib prospek ini sebenarnya baru aktif sekitar dua bulan. Idenya datang dari rapat maraton manajemen yang ingin proses bisnis terlihat modern, berbasis data, dan terotomasi. Aris, yang waktu itu baru masuk dan langsung dipaksa membereskan warisan sistem tanpa kamus data, disuruh meracik satu algoritma penilai prospek.

Aturan yang dimasukkan ke sistem sebenarnya terdengar masuk akal kalau dibaca satu per satu:

1. Kalau perkiraan nilai transaksi di atas lima puluh miliar rupiah, maka prospek sangat layak diprioritaskan.
2. Kalau klien adalah entitas lama yang pernah memakai jasa kami, maka prospek layak diprioritaskan.
3. Kalau ruang kantor yang dicari masih berstatus sengketa atau belum *clear legal*-nya, maka prospek tidak layak diprioritaskan.
4. Kalau perantara atau broker pihak ketiga reputasinya belum terverifikasi, maka keabsahan prospek patut diragukan.

Kekacauan terjadi pada kasus Mega Kuningan. Pemilik gedungnya adalah konglomerat properti lama yang relasinya sangat dekat dengan direksi kami. Nilai transaksinya raksasa. Namun, pihak yang memasukkan berkas pertama kali adalah broker independen baru yang belum punya rekam jejak, dan ada selentingan bahwa sertifikat induk tanahnya sedang dipecah di BPN.

Vina, dengan insting *business development*-nya yang selalu optimis, melihat ini sebagai peluang emas: *"Nilainya gede banget, kliennya teman lama, hajar ajalah!"*

Tapi sistem berpikir lain. Di mata skrip yang dibikin Aris, ketidakjelasan dokumen legal langsung memotong nilai secara brutal. Yang bikin makin berantakan, Aris memperlakukan semua variabel itu seperti nilai ujian sekolah: dihitung rata-rata bobotnya. Ketidakpastian soal broker dan sertifikat digabung paksa dengan kepastian nilai transaksi.

Hasil akhirnya keluar angka 42. Sistem langsung menyimpulkan: jangan buang waktu di sini. Dua aturan saling bertabrakan, tidak ada aturan yang memandu siapa yang harus mengalah, dan akhirnya keputusan bisnis kami disetir oleh angka yang pembuatnya sendiri tidak paham dari mana asal usulnya.

Kebetulan di kelas gue minggu ini, kami baru saja membedah cara sistem cerdas menangani ketidakpastian dunia nyata. Sambil melihat Aris yang tampak pucat di meja kerjanya saat kami sinkronisasi lewat panggilan video, gue membatin: andai saja kantor ini paham konsep *Certainty Factor* sebelum sok-sokan bikin sistem penilai otomatis.

---

## Keyakinan Bukan Soal Persen: Warisan dari Bangsal Rumah Sakit Stanford

Dunia bisnis properti itu kotor dan ambigu, mirip dengan dunia medis. Waktu seorang dokter memeriksa pasien, pasien jarang datang dengan kepastian seratus persen seperti *"gue kena infeksi bakteri X"*. Pasien cuma datang bawa serpihan gejala: demam tiga hari, leukosit agak naik, dan sakit kepala ringan.

Pada pertengahan dekade 1970-an, para peneliti di Stanford University (Shortliffe dan Buchanan) bikin sistem pakar legendaris bernama MYCIN buat mendiagnosis infeksi darah bakterial. Mereka mentok kalau cuma pakai teori probabilitas klasik Bayes. Kenapa? Karena di lapangan, probabilitas apriori sering kali tidak ada datanya, dan gejala medis tidak saling bebas (*conditionally independent*).

Dari sanalah lahir konsep **Certainty Factor (CF)**. Inti dari konsep ini sederhana tapi mendalam: tingkat keyakinan manusia terhadap suatu hipotesis tidak bisa diukur cuma pakai satu angka persentase tunggal dari 0 sampai 100 persen.

Certainty Factor memecah keyakinan jadi dua sumbu yang jalan sendiri-sendiri. Sumbu pertama, *measure of belief* (MB): seberapa besar satu bukti menambah keyakinan bahwa hipotesisnya benar. Sumbu kedua, *measure of disbelief* (MD): seberapa besar bukti yang sama menambah keraguan. Dua-duanya rentangnya nol sampai satu.

Tingkat keyakinan akhirnya cuma selisih dua angka itu, MB dikurangi MD, dan hasilnya bergerak dari minus satu sampai plus satu. Plus satu artinya buktinya membuktikan hipotesisnya benar tanpa sisa. Minus satu artinya bukti itu membuktikan hipotesisnya salah total. Nol artinya bukti tadi nggak ngomong apa-apa.

Poin yang bikin gue berhenti baca dua kali: **MB dan MD nggak harus berjumlah satu**. Di probabilitas biasa, kalau peluang hujan tujuh puluh persen, otomatis peluang nggak hujan tiga puluh persen. Kepala manusia nggak begitu. Nggak ada bukti bahwa klien bermasalah bukan berarti bukti bahwa klien itu bersih. Ketidakhadiran bukti bukan bukti ketidakhadiran.

Contohnya begini. Bisa saja gue punya bukti kuat bahwa nilai transaksi sebuah gedung memang wajar, keyakinannya nol koma delapan. Di saat yang sama, gue juga memegang bukti lain bahwa perantaranya mencurigakan, keraguannya nol koma enam. Angka keyakinan akhirnya bukan rata-rata dari dua angka itu, tapi nol koma delapan dikurangi nol koma enam, jadi tinggal plus nol koma dua.

Lalu plus nol koma dua itu artinya apa? Panduan sistem pakar klasik membagi skalanya jadi sebelas tingkat, dari pasti tidak sampai pasti. Yang perlu lo inget cuma tiga wilayah: di atas nol koma enam keyakinannya kuat, di bawah minus nol koma enam keyakinannya kuat ke arah sebaliknya, dan di sekitar nol artinya masih abu-abu. Angka plus nol koma dua masuk wilayah abu-abu itu. Sistem yang benar seharusnya ngasih sinyal ke Vina: data ini masih gelap, butuh manusia yang ngecek. Bukan malah ngeluarin satu angka bulat yang langsung nyampahin prospek ke daftar tolak.

---

## Logika Kombinasi: Seni Merajut Keraguan

Masalah di kantor nggak berhenti pada satu aturan tunggal. Dalam praktiknya, satu kesimpulan bisnis ditarik dari rantai aturan yang panjang, dan di situ kesalahannya numpuk.

Pertama, aturannya sendiri belum tentu yakin, dan buktinya juga belum tentu yakin. Cara hitungnya sederhana: keyakinan terhadap aturan dikali keyakinan terhadap buktinya. Kalau aturannya cuma nol koma delapan yakin, sementara buktinya masih sebatas desas-desus calo tanah dengan keyakinan nol koma lima, hasilnya nol koma empat. Masih sebatas mungkin, belum boleh dijadikan vonis mati.

Kedua, satu aturan sering butuh beberapa syarat sekaligus. Kalau syaratnya harus terpenuhi semua (AND), yang dipakai adalah angka **terlemah** di antara syarat-syarat itu, karena kepastian satu proposal cuma sekuat rantai paling lemahnya. Kalau direktur keuangan sudah sembilan puluh sembilan persen setuju tapi izin tata ruangnya masih gelap, kepastian proposal itu tetap tertahan di angka izin tata ruangnya. Sebaliknya, kalau cukup salah satu syarat saja (OR), yang dipakai angka **terkuat**.

Ketiga, ini bagian yang bikin gue sadar betapa fatalnya kesalahan skrip Aris. Dua aturan berbeda bisa sama-sama menyimpulkan hal yang sama, dan hasilnya **nggak boleh dirata-rata**. Ada tiga situasi.

1. **Kalau dua-duanya positif:** keyakinannya naik, tapi cara naiknya bukan dijumlah biasa. Bukti kedua cuma ngisi sisa ruang yang belum yakin. Kalau yang pertama nol koma enam, sisa ruangnya nol koma empat, dan bukti kedua nol koma lima cuma ngisi separuh dari sisa itu. Hasilnya sekitar nol koma delapan, dan nggak pernah lewat satu.
2. **Kalau dua-duanya negatif:** makin tenggelam ke arah minus satu, dengan cara yang sama dari sisi sebaliknya.
3. **Kalau tandanya berlawanan:** dua bukti itu saling mengurangi, dan hasilnya nggak pernah lebih besar dari bukti yang paling kuat. Bukti positif nol koma delapan ketemu bukti negatif nol koma lima jatuhnya nol koma enam, bukan nol koma tiga, karena yang lemah itu memotong porsi, bukan menghapus angkanya.

Di skrip Aris, semua ini lenyap. Dia cuma menjumlahkan angka mentah lalu membaginya dengan jumlah variabel. Wajar kalau sinyal keraguan yang paling penting tenggelam jadi rata-rata yang menyesatkan.

---

## Mesin yang Bergerak dari Fakta: Tiga Langkah Tanpa Tabrakan

Selain salah menghitung angka keyakinan, sistem penilaian prospek di kantor kami punya cacat mendasar kedua: cara mesin menarik kesimpulan dari data.

Dalam sistem inferensi, ada dua mazhab besar. Yang pertama adalah *Backward Chaining*, pendekatan yang digerakkan oleh tujuan (*goal-driven*). Mesin menetapkan hipotesis dulu di awal (misalnya: *"Apakah prospek ini harus dibuang?"*), lalu bergerak mundur mencari bukti-bukti yang mendukung atau menggugurkan hipotesis tersebut. Pendekatan ini sangat cocok untuk diagnosis medis atau pelacakan kerusakan mesin.

Pendekatan kedua adalah **Forward Chaining**, strategi yang digerakkan oleh data (*data-driven*). Mesin mulai dari fakta-fakta mentah yang ada di tangan, mencocokkannya dengan basis aturan, lalu bergerak maju menarik kesimpulan baru sampai menemukan rekomendasi akhir.

Untuk kasus kantor properti seperti tempat gue kerja, Forward Chaining adalah pilihan yang paling natural. Setiap pagi, puluhan fakta baru masuk ke meja kami: luas tanah, anggaran sewa, nama perusahaan peminat, tanggal jatuh tempo kontrak sewa lama, sampai reputasi agen perantara. Kita tidak tahu di awal prospek ini bakal bermuara ke mana, jadi kita harus mengolah fakta yang ada ke depan.

Masalahnya, Forward Chaining di dunia nyata tidak bisa cuma berupa tumpukan perintah `if-then` yang dieksekusi dari baris pertama sampai baris terakhir. Mesin inferensi Forward Chaining harus bekerja lewat siklus tiga fase yang disiplin:

```
Fakta baru masuk
      |
      v
1. MATCH       cocokkan fakta dengan syarat aturan
      |
      v
2. CONFLICT    pilih SATU aturan dari yang terpicu
   RESOLUTION
      |
      v
3. ACT         jalankan aksi, lahir fakta baru
      |
      v
ulangi sampai nggak ada aturan yang cocok
```

Fase kedua, **Conflict Resolution**, adalah titik di mana sistem kami hancur lebur.

Ketika fakta tentang gedung Mega Kuningan dimasukkan, terjadi kondisi di mana beberapa aturan terpicu sekaligus. Kumpulan aturan yang semua premisnya terpenuhi oleh fakta ini disebut **conflict set**.
* Aturan A terpicu: Klien lama → Prioritas Tinggi.
* Aturan B terpicu: Nilai transaksi raksasa → Prioritas Sangat Tinggi.
* Aturan C terpicu: Legalitas dokumen belum verifikasi → Tahan / Prioritas Rendah.

Kalau sebuah mesin inferensi punya tiga aturan di dalam *conflict set*, dia tidak boleh menjalankan ketiganya secara serampangan atau merata-ratakannya. Mesin butuh strategi resolusi konflik yang jelas, misalnya:
1. **Rule Priority (Prioritas Aturan):** Menetapkan bobot hierarki aturan sejak awal. Misalnya, aturan kepatuhan hukum (*compliance*) selalu mengalahkan aturan potensi pendapatan komersial.
2. **Specificity (Kekhususan):** Aturan yang syaratnya paling detail dan spesifik harus dieksekusi lebih dulu daripada aturan yang sifatnya umum.
3. **Recency (Kebaruan):** Mengutamakan fakta yang paling baru diperbarui dalam basis data.
4. **Refraction:** Aturan yang sudah pernah dijalankan pada fakta yang sama tidak boleh dieksekusi ulang agar tidak terjadi perulangan tanpa henti.

Di sistem buatan Aris, strategi ini nihil. Skrip Python-nya cuma mengeksekusi kamus data sesuai urutan iterasi memori komputer. Siapa aturan yang dibaca paling akhir, dialah yang menimpa kesimpulan sebelumnya. Prospek Mega Kuningan terbuang bukan karena bisnis kami secara sadar memutuskan untuk menolak, melainkan karena urutan baris kode di skrip Aris menempatkan variabel risiko legalitas di baris paling bawah.

---

## Sore yang Gerah dan Prospek yang Melayang

Tadi sore, suasana rapat evaluasi penjualan di lantai 28 terasa canggung. Pimpinan divisi berkali-kali menyindir kenapa kami bisa kalah cepat dari agen kompetitor di kawasan segitiga emas. Vina berusaha membela diri dengan mengatakan tim bisnis tidak pernah menerima notifikasi prioritas dari dashboard. Aris cuma menunduk sambil mengutak-atik kabel tetikusnya, tidak berani membantah.

Gue tidak menyalahkan Aris. Anak itu dilempar ke dalam sistem tanpa dokumentasi, tanpa panduan pemodelan pengetahuan, dan disuruh membuat sistem yang menyimpulkan sesuatu dari ketiadaan SOP. Ketika manajemen menuntut angka bulat 0 sampai 100 tanpa mau repot memahami probabilitas dan keraguan, ya inilah hasilnya: sistem yang kelihatannya presisi, padahal sebetulnya cuma kebetulan yang fatal.

Waktu Dylan menelepon tadi sore dari asrama buat menanyakan senar raket bulutangkisnya yang putus, gue mendengarkan suaranya sambil menatap baris-baris data prospek yang masih menumpuk di monitor. Hidup anak tiga belas tahun saja penuh perhitungan prioritas yang jelas: latihan fisik dulu, belajar malam kemudian, baru boleh main di akhir pekan. Sementara itu, sistem di kantor konsultan multinasional tempat gue bekerja justru berjalan tanpa kompas resolusi konflik yang waras.

Prospek Mega Kuningan sudah resmi melayang, dan manajemen sekarang minta sistem penilaian itu "diperbaiki rumusnya" paling lambat akhir minggu. Mereka masih mengira ini cuma masalah menggeser bobot persentase dari 20 persen ke 30 persen. Mereka belum tahu saja kalau seluruh fondasi logikanya yang harus dibongkar dari nol.

---

## Menurut Lo Gimana? 🤔

1. Kalau lo diminta merancang strategi *conflict resolution* untuk kasus di kantor gue, di mana aturan *profit* bertabrakan langsung dengan aturan *legal risk*, strategi mana yang paling tepat lo terapkan (apakah *rule priority*, *specificity*, atau yang lain) dan bagaimana lo membenarkan pilihan itu ke orang bisnis seperti Vina?
2. Dalam formulasi Certainty Factor, nilai antara -0,19 sampai +0,19 dikategorikan sebagai zona tidak signifikan (*unknown/insignificant*). Menurut lo, dalam perancangan sistem informasi manajemen, tindakan apa yang seharusnya dieksekusi oleh mesin inferensi ketika sebuah prospek jatuh di zona abu-abu ini, alih-alih memaksakan kesimpulan rekomendasi ya atau tidak?
3. Kenapa penggabungan bukti menggunakan pendekatan Certainty Factor (bukti kedua cuma ngisi sisa ruang keyakinan yang belum terisi) jauh lebih realistis untuk memodelkan intuisi analis bisnis dibanding pendekatan rata-rata terbobot (*weighted moving average*) yang selama ini dipakai Aris?

Kopi kedua gue sudah dingin di meja, dan Aris baru saja mengirim draf diagram alur baru yang masih kelihatan berantakan di layar kedua. Besok bakal jadi hari yang panjang di kantor.

Semoga minggu belajar lo jauh lebih masuk akal dibanding logika dashboard kantor gue.

Nik
