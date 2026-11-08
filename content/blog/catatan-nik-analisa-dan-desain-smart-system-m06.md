---
title: "Catatan Nik: Kursor Merah di Kolom Revenue, Nafsu Belanja Tool Baru, dan Seni Mencari Biang Keladi"
subtitle: "Vina udah mau beli platform analytics baru cuma gara-gara grafik revenue nyungsep, padahal yang berubah bukan algoritmanya. Gue minta satu hal dulu sebelum ada yang gesek kartu kredit kantor: tulis gejalanya, lalu uji satu dugaan."
type: blog
date: 2026-11-09T05:00:00+07:00
draft: true
ws_chat: 1701
ws_msg: 21868
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "analisa-dan-desain-smart-system", "catatan-nik"]
summary: "Materi pekan ini soal cara membongkar masalah sampai akarnya: tiga lapis masalah, fishbone 6M, 5 Whys, sampai beda ketidakpastian aleatorik dan epistemik. Di kantor gue, satu rapat pagi hampir berakhir dengan belanja lisensi baru untuk penyakit yang salah lapis."
hook: "Grafik merah di slide jam sembilan pagi itu belum tentu sakit di algoritmanya."
---

Tangkapan layar slide presentasi jam sembilan pagi tadi masih membekas di kepala gue: sebuah grafik garis merah menukik tajam ke pojok kanan bawah, memotong target kuartalan tanpa ampun. Tiga kuartal berturut-turut, *revenue* per cabang dari klien ritel terbesar kami rontok pelan-pelan. Suasana ruang rapat virtual mendadak sedingin kabin pesawat 🥶 

Belum sempat Aris menarik napas buat menjelaskan rekap angkanya, Vina langsung memotong dengan nada bicara yang cepat dan penuh keyakinan khas dia. Solusinya sudah siap di ujung lidah: model prediksi valuasi gue ketinggalan zaman, algoritmanya tumpul, dan kantor gue butuh langganan *platform analytics* berbasis AI generasi terbaru yang baru saja dia lihat di seminar hotel bintang lima pekan lalu. Harganya ribuan dolar per lisensi tahunan. 

Aris, yang duduk lemas menatap layar laptopnya, langsung mencatat instruksi Vina buat "ngoprek ulang algoritma malam ini juga". Gue yang kebetulan ikut rapat karena diminta memantau retensi akun komersial cuma bisa memijat pelipis. Polanya berulang lagi. Setiap kali angka bisnis berdarah, sistem komputasi yang dijadikan kambing hitam, lalu solusinya adalah beli mainan baru. 

Padahal kalau dilihat sekilas saja dari profil transaksinya, yang berubah drastis belakangan ini bukan akurasi mesin hitung gue, melainkan komposisi segmen pelanggan baru yang masuk ke cabang-cabang itu. Mesinnya cuma membaca apa yang lewat di depannya. Sebelum Vina mengajukan proposal belanja ke meja direksi dan sebelum Aris begadang membongkar skrip Python yang sebenarnya tidak rusak, gue buru-pelan menyela rapat. Gue minta satu hal sederhana: tolong tulis gejalanya lengkap dengan angka dan periode yang presisi, lalu uji satu dugaan paling mendasar sebelum ada yang gesek kartu kredit kantor buat beli lisensi.

Momen itu pas banget sama materi kuliah sistem cerdas pekan ini di kampus gue. Kalau pekan lalu gue sibuk membahas bias kognitif dan kacamata penilai manusia yang sering kabur, pekan ini dosen gue ngasih gue obeng dan tang: teknik identifikasi akar masalah. Alat kerja buat membedah jeroan sistem sebelum kita asal tebak penyakit.

---

## Tiga Lapis Masalah: Kenapa Solusi Sering Nyasar ke Tetangga? 🎯

Kesalahan paling fatal saat sistem cerdas mulai ngaco adalah mencari masalah persis di titik gejalanya meletus. Dalam arsitektur sistem berbasis data, masalah itu punya tiga lapis yang beda sifat, beda wujud, dan beda obatnya.

```
+-----------------------------------------------------------+
| 1. LAPIS TEKNIS: kode, algoritma, tuning, infrastruktur    |
+-----------------------------------------------------------+
                             |
+-----------------------------------------------------------+
| 2. LAPIS DATA: kualitas, distribusi, representasi input    |
+-----------------------------------------------------------+
                             |
+-----------------------------------------------------------+
| 3. LAPIS KONSEPTUAL: definisi tujuan dan metrik optimasi   |
+-----------------------------------------------------------+
```

Lapis pertama adalah **lapis teknis**. Ini wilayah favorit orang-orang yang gatal mau utak-atik kode: *bug*, algoritma yang tidak cocok, kapasitas komputasi yang kedodoran, atau model yang *overfitting*. Cirinya gampang dikenali: performanya jago kandang, alias akurasinya selangit di data latih (*training data*), tapi langsung hancur lebur begitu dites di data uji (*testing data*). 

Lapis kedua adalah **lapis data**. Di sini algoritmanya sebenarnya sehat walafiat, tapi bahan bakarnya bermasalah. Datanya bolong-bolong, tidak seimbang (*imbalanced*), atau cuma mewakili kelompok tertentu. Ciri khasnya: model bakal sangat akurat menebak mayoritas, tapi konsisten meleset untuk kelompok minoritas atau segmen baru yang polanya belum pernah terekam.

Lapis ketiga adalah **lapis konseptual**, lapis yang paling sering diabaikan karena letaknya di ruang rapat pengambil keputusan, bukan di baris kode. Lapis ini bicara soal apakah tujuan sistemnya sendiri sudah benar sejak awal. Contoh klasik yang sering bikin bencana: sistem rekomendasi dioptimalkan murni buat mengejar *click-through rate*, padahal tujuan bisnis jangka panjangnya adalah bikin pengguna betah dan loyal (*retention*). Akibatnya, mesin bakal merekomendasikan judul-judul *clickbait* murahan yang bikin orang mengklik sekali lalu kapok seumur hidup.

Kenapa pemisahan lapis ini krusial? Karena perbaikan harus cocok dengan lapisnya. Kalau lo ganti algoritma canggih untuk masalah yang sebenarnya ada di lapis data, gejalanya cuma pindah tempat, bukan hilang. Kalau lo tambah tumpukan data untuk masalah yang cacat di lapis konseptual, lo cuma bikin kesalahannya jadi terlihat lebih rapi dan meyakinkan. Dan yang paling konyol, kalau lo membakar anggaran buat menambah data demi menyelesaikan variasi acak (*noise*), usaha lo bakal berakhir dengan hasil nol besar.

Kasus Vina tadi pagi adalah contoh teladan salah lapis. Dia mau menyembuhkan pergeseran segmen pelanggan (lapis data) dengan cara mengganti *tools* dan memaksa Aris merombak model (lapis teknis). Untung belum sempat ketuk palu.

---

## Gejala, Masalah, dan Empat Pertanyaan Penguji Akar 🔍

Sebelum kita pegang alat bedah, batas antara tiga istilah ini harus tegas dulu di kepala:

* **Gejala** adalah apa yang tertangkap panca indra atau layar monitor. Misalnya: "Akurasi model turun jadi 72%" atau "Penjualan cabang ambles".
* **Masalah** adalah kesenjangan nyata antara realitas di lapangan dan harapan yang disepakati. Misalnya: "Prediksi *churn* meleset parah khusus di segmen pelanggan ritel baru yang mendaftar via aplikasi promo."
* **Akar masalah** adalah kondisi terdalam yang kalau diperbaiki, gejalanya bakal lenyap dan tidak akan muncul lagi di tempat lain.

Biar kita tidak tertipu sama dugaan liar di ruang rapat, ada empat pertanyaan filter buat menguji apakah suatu hal pantas disebut akar masalah:

1. **Bisa diubah?** Kalau hal itu berada di luar kendali tim (misalnya inflasi nasional atau regulasi suku bunga BI), itu bukan akar masalah. Itu kondisi lingkungan yang harus diterima sebagai batasan sistem.
2. **Bisa diuji dengan data?** Kalau lo tidak punya metrik atau cara buat membuktikannya secara empiris, itu baru sebatas asumsi atau gosip koridor, bukan temuan ilmiah.
3. **Kalau diperbaiki, gejalanya hilang?** Ini ujian pamungkas. Kalau faktor itu dihilangkan tapi grafik performanya masih jeblok, berarti lo baru memegang cabang masalah, bukan akarnya.
4. **Menjelaskan gejala lain juga?** Akar masalah yang sejati biasanya punya daya jelajah luas. Begitu akar ini disentuh, serangkaian gejala aneh lain yang tadinya tampak terpisah bakal ikut terjawab.

Kalau satu dugaan belum lolos empat saringan ini, jangan pernah izinkan tim lo mengetik baris kode solusi atau menggelontorkan anggaran. Tahan diri dulu.

---

## Menghidupkan Fishbone Tanpa Menjadikannya Sekadar Poster 🐟

Alat pertama yang dibahas di kelas adalah diagram tulang ikan alias *Fishbone* (Ishikawa). Lo pasti sudah sering lihat bentuknya: garis lurus horizontal dengan kepala ikan di sebelah kanan yang memuat masalah utama, lalu tulang-tulang miring berisi kategori penyebab.

Di lingkungan industri, orang biasa pakai kategori **6M**: *Man* (keterampilan dan keputusan manusia), *Machine* (server, versi model, perangkat lunak), *Method* (SOP, alur kerja, logika bisnis), *Material* (kualitas input dan sumber data), *Measurement* (definisi metrik dan instrumentasi), serta *Environment* (kondisi pasar, tren musiman, regulasi). Kalau di ranah jasa atau layanan digital, biasanya lebih luwes pakai **4P**: *People*, *Process*, *Policy*, dan *Place*.

```
(MAN / PEOPLE)             (MACHINE)            (METHOD / PROCESS)
      \                        \                        \
       \                        \                        \
        +------------------------+------------------------+-----> [ MASALAH UTAMA:
       /                        /                        /        Angka & Periode ]
      /                        /                        /
(MATERIAL / DATA)         (MEASUREMENT)           (ENVIRONMENT)
```

Tapi jujur saja, Sar, lo tahu kan berapa banyak diagram *fishbone* yang cuma berakhir jadi hiasan presentasi di kantor konsultan? Dibuat buru-buru setengah jam sebelum rapat, diisi kata-kata klise, ditempel di lampiran PDF tebal, lalu ditinggal tidur. 

Biar *fishbone* berubah dari sekadar pajangan dinding jadi alat intelijen yang tajam, langkah mainnya harus disiplin:

* **Tulis efek di kepala ikan dengan angka dan periode spesifik.** Jangan pernah tulis "performa model jelek" atau "pendapatan turun". Tulis dengan telanjang: "Pendapatan bersih segmen komersial turun 43 persen dibanding periode yang sama tahun lalu". Angka yang spesifik membatasi ruang gerak orang-orang yang suka melebih-lebihkan keadaan.
* **Pilih tulang yang relevan saja.** Tidak ada kewajiban sakral memakai semua 6M. Kalau masalahnya ada di sistem analitik internal, empat tulang yang solid jauh lebih berguna daripada memaksakan kategori pabrik yang bikin bingung.
* **Tumpahkan dulu semua penyebab lewat curah pendapat (*brainstorming*).** Tulis tanpa dihakimi. Biarkan tim mengeluarkan dugaannya secara bebas di tahap awal.
* **Tembus tiap cabang dengan teknik 5 Whys.** Jangan berhenti di lapisan permukaan.
* **Tandai penyebab yang bisa diuji dengan data.** Ini garis demarkasi antara analis yang kompeten dan tukang dongeng. Tiap tulang harus punya status verifikasi.
* **Urutkan prioritas berdasarkan bukti konkret, bukan berdasarkan siapa yang suaranya paling lantang di ruang rapat.**

Ada tes cepat buat menguji apakah isi tulang ikan lo berbobot atau kosong: tiap cabang tulang harus bisa dijawab dengan kalimat "sudah kami cek datanya, dan hasilnya membuktikan X". Kalau tim lo cuma bisa bilang "kayaknya sih gara-gara itu", berarti cabang itu masih berstatus dugaan mentah.

---

## Menancapkan 5 Whys di Setiap Tulang

Di sinilah teknik kedua masuk: **5 Whys**. Konsepnya sederhana banget, tanyakan kata "kenapa" secara berulang sampai lo mentok di sebuah penyebab fundamental yang bisa diperbaiki oleh tim.

Tapi ada tiga aturan main ketat yang sering dilanggar orang:

1. **Jawabannya harus faktual, bukan spekulasi.** Begitu lo tidak tahu data pastinya, jangan mengarang bebas demi mengisi kekosongan. Tulis sejujur-jujurnya: "belum diketahui", lalu jadikan itu tugas rumah buat menarik log data.
2. **Berhenti saat jawabannya sudah masuk ke ranah yang bisa diperbaiki tim.** Kalau di pertanyaan keempat jawabannya sudah menyentuh "karena perang dagang global", ya lo tidak usah lanjut ke pertanyaan kelima buat mencari tahu kenapa perang dagang terjadi. Fokus ke variabel yang kuasanya ada di tangan lo.
3. **Jalankan secara bercabang, bukan garis lurus tunggal.** Bahaya terbesar memakai 5 Whys sendirian tanpa *fishbone* adalah ilusi bahwa masalah dunia nyata itu linear seperti rantai sepeda. Padahal masalah sistem cerdas itu selalu bercabang dan saling silang. Karena itulah 5 Whys harus ditempatkan **di dalam** masing-masing tulang *fishbone*, bukan berdiri sendiri sebagai jalan pintas.

Sebagai pendukung, dosen gue juga menyinggung sekilas soal **Pohon Masalah (*Problem Tree*)** dan **Analisis Pareto 80/20**. Pohon masalah itu enak dipakai waktu lo mau memetakan akibat ke arah atas (dahan) dan penyebab ke arah bawah (akar), jadi manajemen bisa memilih di tingkat mana mereka mau menembakkan sumber daya. Sementara prinsip Pareto dipakai setelah semua penyebab terdaftar: hitung kontribusi volumenya. Hampir selalu, delapan puluh persen kekacauan di dasbor lo cuma dipicu oleh dua puluh persen jenis galat di belakang layar. Sikat yang dua puluh persen itu duluan.

---

## Memisahkan yang Acak dari yang Bodoh: Aleatorik vs Epistemik 🎲

Bagian ini yang bikin mata gue terbuka lebar waktu mendengarkan penjelasan dosen. Sistem cerdas itu bekerja di bawah kabut ketidakpastian. Masalahnya, ketidakpastian itu datang dari dua pintu yang sama sekali berbeda sifatnya, dan kalau lo mencampurnya, hancur sudah seluruh kalkulasi bisnis lo.

```
+-------------------------------------------------------------------------+
|                          SUMBER KETIDAKPASTIAN                          |
+------------------------------------+------------------------------------+
|       ALEATORIK (KEACAKAN)         |    EPISTEMIK (KURANG PENGETAHUAN)  |
+------------------------------------+------------------------------------+
| - Melekat pada sifat alami data    | - Berasal dari ketidaktahuan kita  |
| - Tidak hilang walau model canggih | - Bisa dikurangi dengan data/riset |
| - Contoh: Siapa yg klik app hari ini| - Contoh: Dampak diskon ekstrem    |
| - Obat: Cadangan & probabilitas    | - Obat: Eksperimen & tambah data   |
+------------------------------------+------------------------------------+
```

Pintu pertama adalah **ketidakpastian aleatorik (*aleatory uncertainty*)**. Ini adalah keacakan intrinsik yang memang melekat pada alam semesta atau perilaku manusia di sistem tersebut. Sifatnya bawaan lahir. Lo mau pakai superkomputer termahal di dunia atau algoritma tercanggih sejagat raya, keacakan ini tidak akan pernah bisa dihilangkan. Contohnya: pelanggan mana yang tiba-tiba iseng membuka aplikasi properti kantor gue saat sedang terjebak macet di jalan tol hari ini. Itu murni variasi acak (*noise*). 

Pintu kedua adalah **ketidakpastian epistemik (*epistemic uncertainty*)**. Ketidakpastian jenis ini muncul murni karena kita yang belum tahu atau kita yang kekurangan informasi. Sifatnya sementara dan bisa direduksi. Lo bisa memangkas ketidakpastian ini dengan cara mengumpulkan data baru yang representatif, mendesain eksperimen terkontrol, atau memperbaiki instrumen pengukuran. Contohnya: bagaimana perilaku konversi calon pembeli kalau gue kasih diskon biaya provisi sebesar 70 persen, padahal skema diskon sedalam itu belum pernah diuji coba sama sekali dalam sejarah kantor gue.

Kenapa manajer sistem informasi wajib paham bedanya? Karena respons organisasinya bertolak belakang:

* Kalau masalahnya **aleatorik**, jangan buang duit buat menggaji konsultan baru atau melatih model berminggu-minggu demi mengejar akurasi sempurna. Terima keacakan itu, kelola risikonya dengan probabilitas, dan pasang bantalan (*buffer*) finansial.
* Kalau masalahnya **epistemik**, di situlah uang riset lo boleh digelontorkan. Bikin *pilot project*, jalankan eksperimen *A/B testing*, dan kumpulkan data spesifik di segmen yang gelap itu.

Biar gue nggak dituduh jualan kecap di depan para direktur, dosen gue ngasih panduan etis buat menyatakan ketidakpastian secara jujur di laporan analitik:

1. **Sebutkan rentang, jangan menjual ilusi satu angka pasti.** Menyajikan estimasi "prospek transaksi berada di kisaran 120 sampai 160 unit" jauh lebih bertanggung jawab secara ilmiah daripada menulis angka tunggal "145 unit" seolah-olah masa depan sudah tertulis di batu nisan.
2. **Sertakan interval kepercayaan (*confidence interval*) untuk metrik-metrik utama.**
3. **Lakukan analisis sensitivitas (*sensitivity analysis*).** Goyang satu asumsi kunci (misalnya asumsi kenaikan suku bunga KPR naik satu persen), lalu tunjukkan ke manajemen seberapa jauh proyeksi keuntungan mereka bakal tergeser.
4. **Sajikan skenario manajerial.** Selalu pecah proyeksi ke dalam tiga jalur: skenario pesimis, skenario dasar (*baseline*), dan skenario optimis.
5. **Gunakan pembaruan Bayesian (*Bayesian updating*).** Jangan menganggap keyakinan awal kita kaku. Begitu bukti empiris baru masuk, bobot keyakinan sistem harus diperbarui secara proporsional.
6. **Pantau pergeseran data (*distribution shift*) secara berkala.** Model yang akurasinya 95 persen di data historis tiga tahun lalu bisa langsung jadi rongsokan kalau pola demografi atau daya beli pasar sudah bergeser tanpa kita sadari.

Dua poin terakhir ini yang rencananya bakal jadi menu utama materi kuliah gue pekan depan: bagaimana cara mengambil keputusan saat semua indikator berada di wilayah abu-abu.

---

## Alur Kerja Delapan Langkah Menghadapi Masalah

Biar lo punya gambaran utuh bagaimana semua teori ini dirangkai jadi satu tarikan napas kerja, berikut alur kerja standar yang mestinya dijalankan sebelum ada yang teriak-teriak minta migrasi sistem:

1. **Tulis gejala dengan angka dan periode yang presisi.** Tanpa metrik yang jelas, rapat cuma jadi ajang adu gengsi antarmanajer.
2. **Tentukan lapis masalahnya.** Diagnosis sejak dini: apakah ini penyakit teknis, kelaparan data, atau kekeliruan konseptual di ruang rapat pimpinan?
3. **Susun diagram fishbone.** Petakan semua dugaan penyebab ke dalam tulang-tulang yang relevan secara objektif.
4. **Tembus tiap penyebab penting dengan 5 Whys.** Kejar sampai menyentuh batas yang masih bisa diubah dan dikendalikan oleh tim.
5. **Tandai penyebab yang bisa diuji.** Singkirkan dugaan gaib yang tidak punya jejak audit. Yang tidak bisa dibuktikan dengan data, turunkan ke prioritas paling bawah.
6. **Uji hipotesis secara empiris.** Pegang prinsip ketat: satu hipotesis, satu pengujian data, satu kesimpulan faktual.
7. **Petakan sumber ketidakpastiannya.** Pilah mana bagian yang murni keacakan alamiah (aleatorik) dan mana ketidaktahuan yang masih bisa diteliti (epistemik).
8. **Rumuskan ulang masalah dalam format yang tahan uji.** Bawa kembali masalah yang sudah bersih dari bias ini ke kerangka pemecahan masalah yang benar.

Ingat baik-baik urutannya, Sar: **desain solusi baru boleh dirancang setelah langkah kedelapan selesai.** Kalau tim lo sudah sibuk merancang arsitektur sistem baru di langkah kedua, lo tinggal menunggu waktu buat mengulang bencana yang sama tahun depan.

---

## Sepuluh Jebakan Diagnostik yang Bikin Analis Tersandung 🕳️

Sambil mencatat kuliah, gue mendata sepuluh dosa besar yang paling sering dilakukan tim analitik di kantor korporat saat menghadapi sistem yang pincang:

1. **Menjadikan fishbone sekadar hiasan seremonial.** Diagramnya cantik berbobot tiga puluh megabita di slide presentasi, tapi tidak ada satu pun cabang yang benar-benar dicek ke log basis data.
2. **Menaruh gejala di cabang tulang.** Menulis "klien komplain" atau "pengguna tidak puas" di tulang *fishbone* itu konyol. Itu gejala di kepala ikan, bukan faktor penyebab di tulang.
3. **Berhenti di lapisan pertama.** Malas bertanya "kenapa" lebih dari sekali, sehingga yang diobati cuma gejala lapis kedua yang kebetulan terlihat di depan mata.
4. **Semua tulang diisi penuh tapi tidak ada prioritas.** Tim merasa puas karena diagramnya ramai seperti pasar malam, padahal terlalu banyak dugaan tanpa filter sama saja artinya dengan tidak punya fokus kerja.
5. **Menyamakan korelasi dengan sebab-akibat (*correlation vs causation*).** Dua grafik yang menanjak bersamaan di bulan yang sama belum tentu punya hubungan darah. Bisa saja itu cuma kebetulan musiman.
6. **Memaksakan satu angka mutlak untuk semua orang.** Mengabaikan rentang estimasi dan menyembunyikan tingkat ketidakpastian demi terlihat meyakinkan di depan dewan direksi.
7. **Memperlakukan masalah acak sebagai kurang pengetahuan.** Menghabiskan puluhan jam lembur buat mencari pola matematis dari fluktuasi yang aslinya memang murni kebetulan liar.
8. **Menderita amnesia pergeseran data (*distribution shift*).** Begitu model dinyatakan lulus uji validasi saat rilis perdana, model itu dibiarkan bekerja bertahun-tahun tanpa kalibrasi ulang, padahal dunia nyata sudah lama berganti musim.
9. **Membiarkan ambang batas keputusan (*decision threshold*) ditentukan mesin secara buta.** Menentukan ambang batas persetujuan kredit atau valuasi properti itu keputusan bisnis tentang siapa yang menanggung risiko kalau tebakan salah, bukan melulu soal mencari skor akurasi tertinggi di kurva ROC.
10. **Debiasing cuma jadi wacana di atas kertas.** Di ruang rapat semua orang mengangguk-angguk setuju soal bahaya bias konfirmasi, tapi begitu bekerja, tidak ada satu pun prosedur operasional standar (*SOP*) yang dijalankan buat mencegahnya.

---

## Catatan Buat Lo: Menambal Lubang di Proposal Tesis

Materi pekan ini jujur saja jadi tamparan buat kerangka tesis lo soal GPBSales, dataset penjualan buku digital lo. Kemarin-kemarin kerangka lo baru sebatas mengidentifikasi tiga lapis masalah, bias representasi, dan bias otomasi. Tapi masih ada lubang besar di metodologinya: bagaimana cara membuktikan dugaan itu secara empiris tanpa terjebak korelasi palsu.

Kalau kerangka materi pekan ini lo terapkan ke fenomena anjloknya pendapatan bersih di data toko buku daring itu, anatomi kasusnya jadi jauh lebih rapi:

* **Gejala empiris:** Pendapatan bersih (*net revenue*) penerbit merosot tajam dalam dua bulan terakhir berturut-turut, padahal volume unduhan buku digital tercatat naik tipis.
* **Lapis masalah:** Masalah ini jelas ada di lapis konseptual dan lapis data, bukan lapis teknis. Infrastruktur servernya lancar jaya, model prediksinya bekerja tanpa eror, dan transaksi kasir digital tidak mengalami kendala.
* **Dugaan utama (hipotesis kerja):** 
  * Dugaan pertama: algoritma penetapan harga dinamis memberikan diskon yang terlalu dalam demi mendongkrak volume penjualan, tapi margin keuntungan tergerus habis.
  * Dugaan kedua: promosi potongan harga terkonsentrasi secara agresif pada judul-judul buku yang sebenarnya tanpa diskon pun permintaannya sudah sangat tinggi (*deadweight loss*).
* **Rencana pengujian data:** Lo harus membandingkan penerimaan bersih per eksemplar pada periode diskon dalam versus diskon dangkal, dengan mengontrol variabel kategori genre buku dan efek musiman (*seasonality*).
* **Menakar ketidakpastian:** Data transaksi historis sebanyak satu juta baris yang lo pegang memang sangat solid buat memotret pola masa lalu, tapi statusnya tetap merupakan ketidakpastian **epistemik** kalau dipakai buat mengklaim hubungan sebab-akibat kebijakan diskon. Kenapa? Karena data historis itu tidak mencatat apa yang bakal terjadi kalau promosi ditiadakan sama sekali. Makanya, desain tesis lo mutlak membutuhkan data periode kontrol tanpa promo sebagai pembanding yang adil, bukan cuma bersandar pada kemampuan kurva prediksi algoritma regresi.

---

## Bahan Diskusi Kita Pekan Ini

Nah, sekarang giliran lo, Sar. Mengingat lo sering banget berurusan sama analisis kebutuhan sistem dan integrasi data antarunit kerja, gue mau melempar tiga skenario buat melatih pisau bedah lo sebelum kita masuk ke materi teori keputusan pekan depan:

1. Di kantor konsultan gue tadi pagi, Vina ngotot mau beli *tool* analitik baru karena yakin algoritma gue yang ketinggalan zaman dalam memprediksi *revenue* cabang klien ritel, padahal dugaan awal gue masalahnya ada di pergeseran segmen pelanggan baru (*distribution shift*). Kalau lo jadi Aris yang ditugaskan memverifikasi situasi ini secara objektif, bagaimana lo menyusun satu pengujian data sederhana buat membuktikan atau membantah dugaan Vina sebelum bos menyetujui anggaran ratusan juta rupiah?
2. Dalam praktiknya, garis batas antara ketidakpastian aleatorik (keacakan alami) dan ketidakpastian epistemik (kurang pengetahuan) sering kali kabur di mata manajer nonteknis. Coba ambil satu contoh kasus nyata di tempat lo, lalu jelaskan bagaimana cara lo meyakinkan pemangku kepentingan bahwa menambahkan data atau mempercanggih algoritma pada kasus tersebut adalah tindakan buang-buang uang karena masalahnya murni bersifat aleatorik.
3. Dari sepuluh jebakan diagnostik yang gue daftarkan di atas, nomor berapa yang paling sering lo lihat terjadi secara terang-terangan di lingkungan kerja lo, dan apa mekanisme pertahanan prosedural yang paling masuk akal buat menghentikannya tanpa bikin ruang rapat jadi ajang perang urat saraf?

Jangan biarkan Vina-Vina lain di luar sana menghabiskan anggaran kantor buat mengobati penyakit yang salah.

Kopi seduh dingin di botol kaca gue akhirnya habis juga, selamat membongkar tumpukan data lo,

Nik
