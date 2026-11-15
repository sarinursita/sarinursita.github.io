---
title: "Catatan Nik: Skor 74,2, Lantai 28 yang Panas Dingin, dan Neural Network yang Keburu Jatuh Cinta"
subtitle: "Satu angka di halaman ringkasan eksekutif sudah cukup buat mengubah nasib sebuah gedung di mata klien, dan gue cuma bisa ngitung berapa banyak gedung sehat lain yang bakal kena cap yang sama."
type: blog
date: 2026-11-19T05:00:00+07:00
draft: true
ws_chat: 1725
ws_msg: 21958
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "smart-information-system", "fuzzy-logic", "catatan-nik"]
summary: "Materi kuliah minggu ini soal cara mesin menilai hal yang sebenarnya nggak hitam putih, dari derajat keanggotaan sampai jaringan saraf yang belajar dari tumpukan data. Di kantor gue, satu gedung di Thamrin kena cap Tidak Layak gara-gara skor 74,2, sementara Aris sudah mau mengganti seluruh tabel penilaian klien dengan model yang datanya belum cukup."
hook: "Gedung yang masih sehat bisa kena cap tidak layak cuma karena kalah 0,8 poin dari angka bulat yang nggak pernah diuji siapa pun."
---

Sar, gue baru saja keluar dari ruang rapat kaca di lantai 28 SCBD dengan telinga agak berdengung dan kopi yang sudah dingin sejak dua jam lalu. Di layar proyektor barusan, ada satu angka merah mencolok yang bikin suara Vina naik setengah oktaf waktu menjawab telepon dari direksi klien: **74,2**.

Gara-gara angka itu, satu gedung perkantoran dua puluh lantai di kawasan Thamrin resmi dicap **"Tidak Layak"** di laporan evaluasi kondisi bangunan yang sudah terlanjur dikirim ke meja direksi klien kemarin sore. Masalahnya, Sar, gedung itu aslinya masih gagah banget. Lobi marmernya kinclong, struktur beton utamanya mulus tanpa retak struktural, dan tingkat okupansinya masih di atas delapan puluh persen. Dia cuma kepeleset tipis di satu parameter sistem pendingin cadangan yang memang baru dijadwalkan ganti suku cadang bulan depan.

Gara-gara sistem *scoring* lama milik internal klien pakai aturan potong leher di angka 75, selisih 0,8 poin itu langsung melempar sebuah aset bernilai ratusan miliar ke keranjang yang sama dengan gedung tua yang atapnya bocor di mana-mana. Vina yang kemarin paling pede meyakinkan klien bahwa skrip penilaian cepat itu sudah beres, tadi pagi langsung kena semprot pertanyaan bertubi-tubi. Pas Vina keluar ruangan sambil memijat pelipisnya, gue iseng nyeletuk ke Aris yang duduk di pojokan meja rapat dengan wajah ikutan tegang: kenapa sih penilaian gedung di dunia nyata yang penuh nuansa masih saja dipaksa masuk kotak hitam atau putih?

---

## Ketika Angka 74,2 Membunuh Gedung yang Masih Sehat

Celetukan gue soal kotak hitam-putih itu ternyata langsung nyambung ke materi *Soft Computing* yang baru gue baca semalam buat kuliah Sistem Informasi Strategis gue. Di kampus, dosen gue mendefinisikan ***Soft Computing*** sebagai cabang pendekatan komputasi yang sengaja merangkul ketidakpastian dan perkiraan supaya sistem bisa mengambil keputusan yang luwes seperti cara berpikir manusia. Berbeda sama sistem komputer konvensional yang menuntut semua syarat harus persis benar atau salah mutlak, dunia properti itu isinya penuh kondisi setengah matang yang susah dipaksa pakai angka kaku.

Di lantai 28, skrip lama yang dipakai klien itu masih tunduk sama logika klasik biner. Dalam logika klasik, sebuah pernyataan cuma punya dua kemungkinan nilai: 0 atau 1, salah atau benar, layak atau tidak layak. Begitu skor gedungnya 75,00, dia dapat label 1 alias "Layak". Begitu turun jadi 74,99, dia jatuh bebas jadi 0 alias "Tidak Layak". Tidak ada ruang napas, padahal selisihnya nggak sampai satu persen.

Gue akhirnya buka papan tulis kaca di ruang rapat dan mulai menggambar ulang logika yang jauh lebih manusiawi: ***Fuzzy Logic*** yang diperkenalkan Lotfi Zadeh sejak tahun 1965. *Fuzzy Logic* adalah sistem logika yang memperluas nilai biner 0 atau 1 menjadi derajat keanggotaan kontinu antara 0 sampai 1 untuk mengolah konsep yang sifatnya samar seperti rendah, sedang, atau tinggi. Jadi, gedung dengan skor 74,2 itu nggak langsung divonis mati, melainkan bisa diakui sebagai gedung yang "sebagian besar masih layak, cuma punya sedikit catatan di sisi teknis".

Waktu Aris mulai buka laptop buat nyoba konsep ini, dia sempat bingung bagaimana komputer bisa paham kalimat "sebagian besar masih layak". Di situlah gue kenalin konsep **variabel linguistik**, yaitu variabel yang nilainya bukan deretan angka mentah, melainkan kata-kata alami yang biasa dipakai manusia saat mengobrol seperti "sehat", "mulai aus", atau "kritis". Untuk menilai kondisi gedung klien, kami akhirnya sepakat memecah skor teknis ke dalam tiga label linguistik: "Kurang", "Cukup", dan "Baik".

Supaya kata-kata manusia itu nggak bikin mesin bingung, setiap label tadi harus dipetakan ke dalam **himpunan *fuzzy*** (*fuzzy set*), yaitu kelompok kategori di mana satu angka yang sama boleh ikut menjadi anggota di lebih dari satu label sekaligus dengan tingkat kedekatan yang berbeda. Angka 74,2 tadi, misalnya, bisa punya derajat 0,85 di label "Baik" dan sekaligus punya derajat 0,15 di label "Cukup". Jadi dia nggak diusir sepenuhnya dari kelompok gedung sehat.

Nah, cara menerjemahkan angka mentah 74,2 menjadi derajat 0,85 dan 0,15 itu membutuhkan sebuah alat hitung bernama **fungsi keanggotaan** (*membership function*). Fungsi keanggotaan adalah kurva matematis yang mengubah angka mentah dari lapangan menjadi skor keanggotaan di rentang 0 sampai 1. Di catatan belajar gue, ada empat bentuk kurva yang paling sering dipakai dan masing-masing punya karakter sendiri tergantung sifat datanya:

1. **Kurva segitiga (*triangular*)**: kurva dengan satu titik puncak tajam untuk menandai satu nilai yang dianggap paling ideal di sebuah kategori.
2. **Kurva trapesium (*trapezoidal*)**: kurva dengan atap datar untuk menggambarkan rentang nilai yang sama-sama dianggap masuk seratus persen ke satu kategori tanpa harus memihak satu titik saja.
3. **Kurva *Gaussian***: kurva berbentuk lonceng mulus yang sering dipakai saat perpindahan antar kategori terasa alami dan tidak patah-patah.
4. **Kurva *sigmoid***: kurva berbentuk huruf S yang paling cocok dipakai untuk kategori di ujung kiri atau ujung kanan karena nilainya naik atau turun secara perlahan menuju batasnya.

Ngomongin soal kurva ini, Sar, percobaan pertama gue dan Aris tadi siang sempat menghasilkan bencana mini yang bikin kami berdua ketawa getir. Karena buru-buru mau nunjukin ke Vina sebelum rapat sore, Aris asal memasang kurva segitiga dengan rentang tumpang tindih yang kelewat sempit buat parameter umur mesin *chiller* dan kondisi atap. Pas skripnya dijalankan buat simulasi dua belas gedung milik klien, gedung baru yang umurnya baru tiga tahun malah keluar skor kelayakan cuma 42, sedangkan gudang tua yang sudah reyot malah dapat angka 68. Selidik punya selidik, ternyata ada celah kosong di antara dua kurva segitiga yang nggak bersentuhan sama sekali, jadi skor gedung bagus tadi nyangkut di area nol dan nggak terbaca oleh kategori mana pun. Pelajaran mahal banget di lapangan: kalau kurva fungsi keanggotaannya bolong, mesinnya langsung buta warna.

---

## Mesin Inferensi, Dua Mazhab Aturan, dan Satu Kemenangan Kecil

Setelah kami rapikan kurva trapesium untuk ujung bawah dan kurva segitiga yang saling bertaut rapi di tengah, barulah kami merakit alur utuhnya supaya bisa diuji di depan manajer aset klien. Dalam teori sistem informasi, seluruh rangkaian mesin pengambil keputusan berbasis nilai samar itu disebut ***Fuzzy Inference System*** (FIS), yaitu sistem penalaran utuh yang mengolah angka mentah menjadi keputusan logis lewat empat tahap berurutan.

Tahap pertama di pintu masuk adalah ***fuzzifier*** (fuzzifikasi), yaitu komponen yang memecah angka mentah hasil inspeksi teknisi di lapangan menjadi derajat keanggotaan pada tiap himpunan *fuzzy*. Misalnya, suhu ruang panel listrik dan indeks getaran lift diubah dulu jadi label "Normal 0,7" dan "Mulai Panas 0,3".

Setelah data masuk dan punya label kata-kata, sistem melangkah ke tahap kedua, yaitu mencocokkannya dengan **basis aturan *IF-THEN*** (*rule base*), yang merupakan kumpulan kalimat logika "jika kondisi begini, maka kesimpulannya begitu" yang disusun langsung dari pengalaman pakar lapangan. Kami minta bantuan tim inspektur teknis senior buat merumuskan aturan-aturan ini, contohnya: *IF* kondisi struktur *Baik* *AND* sistem mekanikal *Cukup*, *THEN* kelayakan gedung *Layak dengan Catatan Ringan*.

Semua aturan yang aktif tadi lalu diproses di tahap ketiga oleh **mesin inferensi** (*inference engine*), bagian inti yang bertugas menggabungkan berbagai aturan yang menyala secara bersamaan untuk melahirkan satu kesimpulan sementara yang bentuknya masih samar. Kalau gedung A menyalakan dua aturan sekaligus dengan kekuatan berbeda, mesin inferensi inilah yang menimbang bobot keduanya biar tidak saling tabrak.

Terakhir, karena manajer di lapangan butuh angka tegas dan bukan cuma kurva gambar, sistem menutup alurnya lewat ***defuzzifier*** (defuzzifikasi), yaitu komponen di pintu keluar yang memadatkan kesimpulan samar berbentuk kurva gabungan kembali menjadi satu angka tunggal yang siap dipakai bertindak.

Waktu gue lagi menyusun mesin inferensi ini sama Aris, kami sempat berhenti sebentar karena ada dua mazhab besar yang cara kerjanya beda banget di tahap kesimpulan aturan. Yang pertama adalah **metode Mamdani**, yaitu pendekatan *fuzzy* di mana bagian *THEN* atau kesimpulan aturannya masih berbentuk himpunan *fuzzy* berupa kurva kata-kata sehingga alur logikanya sangat gampang dibaca dan diaudit manusia. Yang kedua adalah **metode Sugeno**, yaitu pendekatan yang bagian kesimpulan aturannya tidak lagi memakai kurva, melainkan langsung berupa angka konstanta atau fungsi linier matematika sehingga proses hitung komputernya jauh lebih ringkas dan cepat.

Kami akhirnya memilih metode Mamdani. Alasannya simpel: kalau nanti tim audit klien nanya kenapa sebuah gedung dapat status tertentu, gue sama Vina bisa nunjuk langsung ke kalimat aturan *IF-THEN* yang persis bahasa manusia tanpa bikin orang non-teknis pusing melihat rumus aljabar di belakangnya.

Pilihan ke Mamdani itu membawa konsekuensi di tahap akhir defuzzifikasi, karena kami harus memilih cara memotong atau menimbang kurva gabungan hasil aturan menjadi satu angka pasti. Ada tiga teknik **defuzzifikasi** yang sempat kami bandingkan di papan tulis:

- ***Center of Gravity*** (CoG): teknik mencari satu angka akhir dengan menghitung titik pusat keseimbangan dari seluruh luas area kurva gabungan, yang hasilnya paling halus dan akurat meski hitungannya sedikit lebih berat.
- ***Mean of Maximum*** (MoM): teknik yang jauh lebih sederhana karena hanya mengambil nilai rata-rata dari titik-titik yang punya derajat keyakinan tertinggi di puncak kurva, tapi sering terasa agak kaku saat dua aturan bertarung imbang.
- ***Bisector***: teknik yang mencari satu garis vertikal untuk membelah area kurva kesimpulan menjadi dua bagian kiri dan kanan yang luasnya persis sama.

Begitu kami jalankan metode Mamdani dengan defuzzifikasi *Center of Gravity*, akhirnya datang juga satu kemenangan kecil sore itu. Gedung Thamrin yang tadi pagi bikin Vina hampir kehabisan napas gara-gara angka 74,2 langsung bergeser ke skor **78,4** dengan label **"Layak dengan Catatan Ringan"**. Saat kami tampilkan ulang di panggilan video singkat bareng manajer aset klien, mereka langsung mengangguk paham karena kelihatan jelas di bagian mana asetnya masih prima dan di komponen cadangan mana anggaran perawatan harus segera turun. Ketegangan di lantai 28 turun drastis dalam lima belas menit.

---

## Rem Mendadak untuk Aris yang Keburu Jatuh Cinta Sama Neural Network

Kemenangan kecil itu sayangnya cuma bertahan dua puluh menit di kepala Aris. Pas Vina keluar ruangan buat mengabarkan pembaruan itu ke grup pimpinan, Aris menatap layar laptopnya sambil nyeletuk pelan: kalau aturan *IF-THEN* tadi harus ditulis manual satu per satu buat puluhan parameter bangunan yang berbeda, kenapa nggak sekalian saja ganti semua tabel itu pakai model yang belajar sendiri dari arsip laporan inspeksi lima tahun terakhir?

Gue langsung menoleh. Gue tahu Aris anak yang cerdas, dan sejak kepergian Bram dulu dia memang punya dorongan kuat buat nunjukin kalau tim valuasi sekarang sanggup membangun sistem analitik yang lebih modern. Tapi begitu dengar idenya mau langsung menyingkirkan aturan pakar ke model yang belajar sendiri, alarm di kepala gue langsung bunyi. Aris lagi ngomongin ***Neural Network*** (Jaringan Saraf Tiruan), sebuah sistem komputasi yang meniru cara kerja jaringan saraf di otak manusia untuk mengenali pola tersembunyi langsung dari tumpukan data.

Biar obrolan kami nggak melantur jadi debat kusir soal istilah keren, gue ajak Aris membedah apa sebenarnya isi mesin yang mau dia bangun itu. Seperti otak kita yang penuh sambungan sel saraf, jaringan ini tersusun dari ribuan unit pemroses kecil bernama ***neuron***, yaitu sel hitungan terkecil yang tugasnya menerima sinyal angka dari luar, menjumlahkannya, lalu memutuskan apakah sinyal itu layak diteruskan ke bagian berikutnya.

Setiap sinyal yang masuk ke dalam *neuron* tidak diperlakukan sama rata, melainkan dikalikan dulu dengan **bobot sinaptik** (*synaptic weight*), yaitu angka pengali yang menentukan seberapa besar pengaruh sebuah faktor masukan terhadap keputusan akhir si *neuron*. Selain bobot pengali, ada juga **bias**, yaitu angka penyesuai tambahan di dalam *neuron* agar posisi perhitungannya bisa digeser naik-turun dan tidak terjebak di titik nol saat semua input lagi kosong. Setelah semua masukan dikalikan bobot lalu ditambah bias, totalnya disaring oleh **fungsi aktivasi** (*activation function*), yaitu rumus penyaring di ujung *neuron* yang memetakan hasil hitungan tadi menjadi sinyal keluaran dengan rentang nilai tertentu.

Jutaan *neuron* itu tentu nggak ditumpuk berantakan, melainkan disusun rapi ke dalam tiga bagian lapisan yang saling terhubung dari depan ke belakang. Bagian terdepan disebut **lapisan *input*** (*input layer*), gerbang pertama tempat data mentah seperti umur gedung, nilai kekuatan beton, dan riwayat bocor disuntikkan ke jaringan. Di tengahnya ada **lapisan tersembunyi** (*hidden layer*), yaitu lapisan berlapis-lapis di bagian dalam tempat jaringan meracik kombinasi pola rumit secara bertingkat tanpa bisa langsung dilihat dari luar. Lalu di paling ujung ada **lapisan *output*** (*output layer*), barisan terakhir yang memuntahkan prediksi atau label keputusan akhirnya.

Di tiap lapisan itu, jenis fungsi aktivasi yang dipasang juga beda-beda tergantung tugasnya. Di dalam *hidden layer*, praktisi biasanya memasang ***ReLU*** (*Rectified Linear Unit*), fungsi penyaring cepat yang langsung memangkas semua angka negatif menjadi nol dan membiarkan angka positif lewat apa adanya supaya proses perhitungan tidak lemot. Sementara di *output layer*, pilihannya tergantung bentuk jawabannya. Kalau klien cuma butuh klasifikasi biner dua pilihan seperti "Layak" atau "Tidak Layak", ujungnya dipasangi ***Sigmoid***, fungsi aktivasi yang memeras angka bebas berapa pun menjadi rentang 0 sampai 1 berbentuk peluang. Tapi kalau pilihannya lebih dari dua kelas sekaligus, misalnya "Prima", "Perawatan Ringan", "Renovasi Sedang", sampai "Kritis", ujungnya wajib memakai ***Softmax***, fungsi yang mengubah deretan skor mentah menjadi peluang persentase yang total seluruh kelasnya pas seratus persen.

Gue tanya ke Aris, bagaimana cara jaringan ini tahu angka bobot sinaptik yang benar tanpa dikasih aturan *IF-THEN* oleh manusia. Aris langsung menerangkan siklus latihan berulangnya dengan mata berbinar. Pertama, jaringan melakukan ***forward propagation***, yaitu aliran hitungan data dari lapisan *input* maju terus melewati *hidden layer* sampai lapisan *output* buat menebak jawaban awal secara acak. Karena bobot awalnya masih ngawur, tebakan itu hampir pasti meleset, dan seberapa jauh selisih melesetnya diukur memakai ***loss*** (*loss function*).

Begitu ketahuan melesetnya seberapa parah, sistem langsung menjalankan ***backpropagation***, proses menelusuri jejak kesalahan dari lapisan belakang berjalan mundur ke depan buat mengoreksi angka bobot sinaptik di tiap jalur satu per satu. Arah dan besarnya koreksi bobot di setiap langkah itu dipandu oleh ***gradient descent***, algoritma navigasi langkah demi langkah yang menggeser nilai bobot ke arah kemiringan paling curam supaya nilai *loss* cepat turun ke dasar lembah. Siklus maju-hitung salah-mundur ini diulang ribuan kali sampai tebakan jaringannya presisi.

Makin ke sini, Aris malah makin semangat nunjukin bahwa di dunia *Neural Network* ada banyak arsitektur berbeda yang bisa dipakai buat aset properti. Untuk data inspeksi gedung yang bentuknya tabel Excel berisi skor angka per komponen, arsitektur dasarnya adalah ***FNN*** atau ***MLP*** (*Feedforward Neural Network* / *Multilayer Perceptron*), yaitu jaringan klasik yang aliran sinyalnya cuma bergerak maju satu arah untuk mengolah data tabular. Kalau nanti tim teknis klien punya ribuan foto retakan dinding atau korosi pipa dari kamera drone, mereka bisa memakai ***CNN*** (*Convolutional Neural Network*), arsitektur khusus yang dibekali filter pemindai untuk membaca pola visual di dalam data citra atau gambar. Dan kalau klien punya catatan log sensor suhu harian atau arsip teks keluhan penyewa selama bertahun-tahun, baru deh masuk ke ***RNN*** atau ***LSTM*** (*Recurrent Neural Network* / *Long Short-Term Memory*), arsitektur yang punya ingatan berantai dari langkah sebelumnya untuk membaca pola pada data berurutan seperti teks atau deret waktu (*time series*).

Semua teori yang keluar dari mulut Aris itu benar secara buku teks, Sar. Tapi di titik itu, gue terpaksa narik rem tangan kuat-kuat sebelum dia terlanjur bikin presentasi tandingan buat klien. Masalahnya ada di empat tantangan klasik *Neural Network* yang nggak bisa ditawar oleh semangat anak muda.

Pertama, jaringan saraf itu sangat rakus data, butuh ribuan bahkan puluhan ribu baris contoh supaya pola bobotnya matang. Gue tanya balik ke Aris berapa baris arsip inspeksi historis yang dimiliki klien sekarang. Aris terdiam sebentar, lalu mengaku cuma ada sekitar enam puluh empat laporan gedung dari lima tahun terakhir. Data sekecil itu kalau dipaksa masuk ke jaringan saraf bakal langsung kena ***overfitting***, yaitu kondisi fatal ketika model terlalu menghafal detail kecil dan kebetulan di data latihan sampai performanya ambyar total begitu ketemu satu gedung baru di lapangan.

Belum lagi soal biaya komputasi yang tinggi kalau nanti mau menyentuh foto drone atau data sensor berantai, padahal bujet proyek ini mepet banget. Tapi alasan paling telak yang bikin Aris akhirnya menurunkan bahunya adalah masalah **interpretabilitas rendah**, sifat *black box* di mana sistem bisa memuntahkan angka prediksi, namun tidak ada satu orang pun di ruangan ini yang sanggup menjelaskan alasan logis di balik angka tersebut ke auditor klien. Bayangin kalau direksi klien nanya kenapa nilai gedung Thamrin turun, terus kami cuma bisa jawab "kata matriks bobot di lapisan tersembunyi nomor tiga begitu, Pak". Bisa langsung diputus kontrak kami sore itu juga.

Sebagai jalan tengah biar semangat riset Aris nggak mati kutu, gue lempar satu konsep pamungkas yang ada di bagian paling akhir catatan kuliah gue: ***Neuro-Fuzzy System***. Sistem ini adalah arsitektur hibrida yang menggabungkan kemampuan belajar otomatis dari *Neural Network* dengan aturan bahasa alami manusia yang transparan milik *Fuzzy Logic*. Ide kasarnya, alih-alih kita menebak-nebak bentuk kurva trapesium atau segitiga secara manual dan sempat bolong seperti kejadian siang tadi, jaringan saraf bisa dilatih buat mencari batas kurva yang paling pas dari data historis, sementara logika akhirnya tetap terpampang jelas dalam bentuk aturan *IF-THEN* yang bisa dibaca auditor. Tentu saja, itu baru masuk akal kami jalankan kalau nanti klien sudah mengumpulkan minimal seribuan data inspeksi gedung yang rapi, bukan cuma enam puluh empat berkas PDF yang formatnya masih beda-beda.

Aris akhirnya mengangguk pelan dan menyimpan kembali niatnya buat bikin model *deep learning* malam ini. Masalahnya, Sar, drama hari ini ternyata belum tamat di situ. Barusan sebelum kami bubar dari lantai 28, Vina masuk lagi bawa pesan singkat dari sekretaris direksi klien. Mereka lega melihat penjelasan *fuzzy* soal status "Layak dengan Catatan Ringan" tadi, tapi untuk rapat ketok palu anggaran renovasi tahun depan di hari Jumat, direksi tetap minta di halaman ringkasan eksekutif hanya tertulis **satu angka bulat tunggal** sebagai skor final gedung, bukan label kalimat panjang apalagi grafik kurva. Di satu sisi mereka minta penjelasan bernuansa yang adil, tapi di ujung keputusan uang, mereka tetap rindu kepastian satu angka bulat, dan kami belum ketemu kata sepakat bagaimana angka akhir defuzzifikasi ini harus dibulatkan atau diboboti ulang tanpa mengkhianati kejujuran kondisi gedungnya.

---

## Menurut lo gmn? 🤔

1. Kalau lo jadi gue dan Aris yang harus melayani permintaan direksi klien buat tetap menampilkan satu angka bulat tunggal di halaman depan ringkasan eksekutif, apakah lo bakal tetap mempertahankan metode Mamdani dengan defuzzifikasi *Center of Gravity*, atau justru beralih ke metode Sugeno supaya angka akhirnya lebih tegas, dan pertimbangan risiko audit apa yang paling menentukan pilihan lo?
2. Mengingat kejadian kurva segitiga kami sempat bolong dan mengeluarkan skor ngaco buat gedung baru berumur tiga tahun, strategi perancangan fungsi keanggotaan seperti apa yang menurut lo paling aman dipakai supaya mesin *fuzzy* nggak pernah kecolongan menghasilkan area buta saat berhadapan sama parameter ekstrem di lapangan?
3. Seandainya dua tahun lagi klien ini beneran punya seribu lebih arsip foto retakan bangunan dan data tabel inspeksi yang rapi, bagaimana lo merancang pembagian peran antara *CNN*, *Fuzzy Logic*, dan *Neuro-Fuzzy System* supaya tim penilai tetap dapat efisiensi otomatisasi tapi nggak kehilangan kepercayaan auditor yang anti sama model *black box*?

Lampu koridor lantai 28 sudah separuh dimatikan oleh petugas gedung, sementara di layar ponsel gue barusan muncul notifikasi dari sekolah Dylan yang mengingatkan batas akhir pengumpulan izin kegiatan lapangan bulan depan. Gue rapikan dulu catatan kurva di tas sebelum turun ke lobi mengejar KRL arah selatan biar nggak kemalaman sampai rumah.

Gue pamit dulu, KRL nggak pernah nunggu orang yang masih mikirin fungsi keanggotaan.

Nik
