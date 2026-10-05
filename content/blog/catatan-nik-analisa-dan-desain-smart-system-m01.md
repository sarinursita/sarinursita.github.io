---
title: "Catatan Nik: Jebakan Batman Analisis Sistem Cerdas dan Warisan Bram yang Bikin Pusing"
subtitle: "Catatan analisis dan desain sistem cerdas, pertemuan 1"
type: blog
date: 2026-10-05T05:00:00+07:00
draft: true
ws_chat: 1542
ws_msg: 21352
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "analisa-dan-desain-smart-system"]
summary: "Manajemen kantor Nik minta \"bikin AI aja\" buat gantiin valuer yang cabut bawa portofolio klien. Nik bedah materi SSAD pertemuan 1: bedanya payung AI sama sistem cerdas, siklus hidupnya, dan kenapa *problem framing* itu jebakan pertama yang paling mahal."
hook: "\"Kenapa nggak bikin sistem AI aja?\" kata salah satu petinggi di rapat kantor Nik. Dosen SSAD-nya bilang justru di situ jebakan pertamanya."
---

Hujan di Bogor malam ini turun deras banget, Sar. Suara air yang nabrak kanopi jendela kamar kerja gue sampai ngalahin suara dosen di Zoom yang baru aja bubar jam sembilan malam tadi. Dylan sempat telepon kemarin sore dari asramanya, suaranya kedengeran capek sehabis latihan basket, tapi obrolan lima belas menit sama dia lumayan jadi *mood booster* sebelum gue harus menghadapi kenyataan: masuk semester baru, ketemu mata kuliah Analisis dan Perancangan Sistem Cerdas (*Smart System Analysis and Design* alias SSAD), dan sialnya, LMS kampus gue masih terkunci rapat.

Enam belas topik kuliah masih berstatus *locked*, cuma RPS tiga SKS ini yang bisa diakses. Dosen pengampu gue malam ini cuma ngasih kuliah pengantar satu setengah jam, terus ninggalin satu pesan sakral: *"Pertemuan pertama bobotnya lima persen ya, silakan pelajari definisinya baik-baik sebelum masuk ke perancangan arsitektur minggu depan."* 

Lucunya, apa yang dibahas di kelas tadi malam berbanding lurus seratus delapan puluh derajat sama drama kantor gue di SCBD siang tadi. 

Gue rasa efek kepergian Bram, mantan *Senior Director of Commercial Valuation* kita yang resign sambil bawa kabur dua *lead valuer* andalan plus segepok portofolio klien kakap, beneran bikin lantai eksekutif kebakaran jenggot. Manajemen panik luar biasa karena *turnaround time* buat bikin laporan valuasi aset komersial melonjak sampai tiga kali lipat. Klien korporat mulai komplain karena proyek akuisisi mereka ketahan akibat kita kekurangan orang yang punya lisensi dan jam terbang tinggi buat naksir harga gedung.

Lalu, lo tebak apa solusi brilian yang keluar dari salah satu petinggi pas *internal meeting* siang tadi via Teams?

*"Kenapa kita nggak bangun sistem AI aja? Masukin semua data transaksi properti sepuluh tahun terakhir, terus biar algoritmanya yang keluarin nilai valuasi otomatis. Praktis, murah, dan kita nggak bakal disandera sama valuer manusia lagi!"*

Mendengar itu, gue cuma bisa menatap layar sambil *mute* mikrofon dan elus dada. Di kepala gue langsung terngiang materi kuliah SSAD yang baru aja gue baca silabusnya. Orang-orang non-teknis sering banget menganggap kata *Artificial Intelligence* itu semacam tongkat sihir Harry Potter. Lempar masalah lo ke dalam kotak hitam bernama AI, simsalabim, semua beres. Padahal kenyataannya? Itu tiket sekali jalan menuju bencana jutaan dolar kalau lo nggak paham fondasi analisis sistemnya.

Yuk, kita bedah materi pertemuan pertama ini bareng-bareng, sekalian gue tumpahkan hasil kontemplasi gue malam ini buat bekal tesis lo juga.

---

## Payung AI vs Sistem Cerdas: Berhenti Menyamakan Semua Hal sebagai "AI"

Hal pertama yang ditekankan dosen gue tadi malam, dan ini penting banget buat kita yang ada di manajemen sistem informasi: *Artificial Intelligence* itu adalah payung disiplin ilmunya, sementara *Smart System* (Sistem Cerdas) adalah wujud nyata penerapannya di dunia operasional.

Banyak orang mengira kalau mereka pasang satu model *machine learning*, mereka otomatis sudah punya sistem cerdas. *No, honey, it doesn't work that way.* AI itu keilmuan tentang bagaimana bikin mesin meniru atau menambah kemampuan kognitif manusia, mulai dari belajar (*learning*), menalar (*reasoning*), sampai mengambil keputusan (*decision making*). Tapi sistem cerdas? Sistem cerdas adalah ekosistem rekayasa perangkat lunak yang utuh.

Di sistem cerdas, arsitekturnya harus membentuk rantai nilai tertutup: **Data $\to$ Model $\to$ Keputusan $\to$ Aksi**.

Kalau salah satu dari empat pilar itu patah, lo nggak punya sistem cerdas. Lo cuma punya *gimmick* algoritma. 

Ambil contoh drama di kantor konsultan properti gue tadi siang. Manajemen pengen "AI Valuasi Properti". Oke, katakanlah tim data science bisa bikin model regresi canggih atau *deep neural network* yang bisa memprediksi harga gedung perkantoran di koridor Sudirman. Modelnya ada di atas kertas (atau di dalam *Jupyter Notebook*). Tapi bagaimana data sertifikat tanah, kondisi fisik gedung, dan fluktuasi suku bunga perbankan bisa masuk secara otomatis dan bersih ke sistem? Itu pilar **Data**.

Setelah model mengeluarkan prediksi, bagaimana sistem tersebut mengubah angka tersebut menjadi sebuah rekomendasi yang bisa dipertanggungjawabkan di depan badan regulator dan bank penjamin emisi? Itu pilar **Keputusan**.

Lalu, apa yang terjadi setelah rekomendasi keluar? Apakah sistem langsung memicu pembuatan draf kontrak resmi, mengirim notifikasi risiko ke komite kredit, atau memperbarui inventaris portofolio secara terintegrasi? Itu pilar **Aksi**.

Tanpa integrasi data, keputusan, dan aksi, model canggih itu cuma bakal jadi artefak pajangan yang berakhir di server lokal tanpa ada yang mau pakai. Dan di situlah letak peran orang MMSI: kita bukan sekadar tukang koding yang melatih algoritma, tapi arsitek yang merancang bagaimana kecerdasan buatan itu bernapas di dalam tubuh organisasi.

---

## *Problem Framing*: Jebakan Batman Antara Masalah Bisnis dan Masalah AI

Bagian paling krusial dari ruang lingkup SSAD adalah *problem framing*. Dosen gue mengulang poin ini berkali-kali: keterampilan termahal seorang analis sistem cerdas adalah kemampuannya membedakan antara *business problem* dan *AI problem*.

Kegagalan proyek sistem cerdas di dunia nyata hampir selalu berakar dari ketidakmampuan menjembatani dua kutub ini. Manajemen biasanya datang membawa keluhan bisnis yang abstrak, emosional, dan sarat tekanan finansial. Tugas kita adalah membongkar keluhan tersebut sampai ke akarnya, lalu menilai: apakah ini benar-benar butuh pendekatan sistem cerdas, atau jangan-jangan cuma butuh perbaikan prosedur operasi standar dan *database relational* yang bener?

Balik lagi ke kantor gue:
*   **Business Problem:** Kantor kehilangan dua *lead valuer* senior, menyebabkan *turnaround time* valuasi melonjak dari tiga hari menjadi dua minggu, yang berisiko menghilangkan potensi *revenue* miliaran rupiah dari klien institusi.
*   **Asumsi Salah Manajemen:** Bikin "AI" buat menggantikan pekerjaan *lead valuer* secara penuh.

Apakah masalah di atas otomatis menjadi *AI problem*? Belum tentu! 

Kalau kita lakukan *problem framing* secara disiplin, kita harus memetakan dulu: komponen apa dari pekerjaan valuer yang menuntut kapasitas kognitif manusia, dan komponen apa yang cuma komputasi repetitif? 

Menghitung depresiasi bangunan berdasarkan tabel penyusutan fiskal itu bukan masalah AI, itu masalah matematika dasar yang bisa diselesaikan pakai skrip Python lima baris atau rumus Excel biasa. Menarik data pembanding harga sewa di SCBD dari internet itu masalah otomatisasi *data scraping*, bukan AI.

Masalah yang benar-benar layak disebut *AI problem* di sini mungkin adalah: bagaimana memprediksi tingkat hunian (*occupancy rate*) gedung komersial dalam lima tahun ke depan berdasarkan variabel makroekonomi, tren kerja jarak jauh, dan sentimen pasar yang terdistribusi di ribuan artikel berita? Nah, itu baru masalah sistem cerdas! Karena di situ ada ketidakpastian tinggi, ada pola tersembunyi yang sulit ditangkap logika deterministik biasa, dan ada kebutuhan adaptasi dinamis.

Dari *problem framing* ini, kita baru bisa menurunkan kebutuhan sistem:
1.  **Kebutuhan Fungsional:** Apa yang harus dilakukan sistem secara eksplisit. Misalnya: sistem harus mampu mengekstraksi teks dari dokumen legalitas PDF yang diunggah, mengidentifikasi klausul anomali, memberikan skor risiko properti, dan mengeluarkan estimasi rentang harga pasar wajar beserta interval kepercayaannya (*confidence interval*).
2.  **Kebutuhan Non-Fungsional:** Ini yang sering bikin sistem cerdas rontok di tengah jalan. Seberapa cepat model harus mengeluarkan inferensi (*latency*)? Apakah sistem harus bisa memproses data transaksi paralel saat jam sibuk (*throughput*)? Seberapa aman data kepemilikan gedung milik klien rahasia kita (*data privacy*)? Dan yang paling penting di sistem cerdas: apa batas toleransi *drift* model sebelum performanya dianggap usang dan harus dilatih ulang?

---

## Siklus Hidup Sistem Cerdas yang Sering Dipotong Kompas

Di RPS SSAD, ada siklus hidup tujuh tahap yang dipaparkan dosen gue. Siklus ini sekilas mirip SDLC (*Software Development Life Cycle*) konvensional yang sering kita pelajari di S1, tapi dinamika di dalamnya beda total:

1.  **Identifikasi Masalah:** Memetakan fenomena lapangan dan menguji apakah masalah tersebut memang membutuhkan solusi cerdas.
2.  **Pengumpulan & Analisis Data:** Memeriksa ketersediaan, relevansi, dan integritas data historis.
3.  **Formulasi Masalah + Tujuan:** Mengonversi sasaran bisnis ke metrik teknis AI (misalnya dari "menurunkan waktu valuasi" menjadi "meminimalkan *Mean Absolute Percentage Error* di bawah 5%").
4.  **Desain & Arsitektur Sistem:** Merancang bagaimana komponen basis pengetahuan, *machine learning*, antarmuka pengguna, dan basis data saling bertukar pesan.
5.  **Integrasi Komponen:** Menjahit pipa data, kontainer model, API, dan sistem warisan (*legacy systems*).
6.  **Evaluasi & Validasi:** Menguji bukan cuma akurasi matematis model di lingkungan lab, tapi performa operasional sistem saat dihadapkan pada data kotor dunia nyata.
7.  **Dokumentasi:** Mencatat seluruh asumsi desain, batasan model, dan karakteristik data secara transparan.

Di dunia konsultan tempat gue kerja, manajemen biasanya pengen langsung lompat dari tahap satu (Identifikasi Masalah) ke tahap lima (Integrasi Komponen). Mereka mau langsung beli sistem jadi dari vendor luar atau maksa tim internal bikin model instan, tanpa pernah melewati tahap dua, tiga, dan empat dengan benar.

Padahal di sistem cerdas, sifat perangkat lunak itu bergantung pada data (*data-dependent*). Di sistem konvensional, kalau kodenya benar, perilakunya bakal selalu konsisten: input A ditambah input B akan selalu menghasilkan output C. 

Di sistem cerdas, perilakunya ditentukan oleh data masa lalu yang lo gunakan buat melatih sistem. Kalau data yang lo punya bias, cacat, atau nggak relevan, sistem lo bukan cuma bakal salah, tapi salahnya secara konsisten dan percaya diri. Itu yang bikin siklus hidup sistem cerdas bersifat iteratif tiada henti, lo nggak akan pernah bisa bilang sebuah sistem cerdas sudah seratus persen selesai secara permanen.

---

## Kotak Hitam, Dimensi Tinggi, dan Realita Pahit di Balik Layar

Materi penutup sesi kuliah malam ini menyentuh aspek tantangan, dan menurut gue ini bagian yang paling membuka mata. Membangun sistem cerdas itu seksi pas bikin proposal presentasi di hadapan direksi, tapi mimpi buruk pas harus mengelolanya di server produksi. Ada empat tantangan utama yang harus kita antisipasi dari awal perancangan:

Pertama, **kualitas dan ketidakseimbangan data (*data imbalance*)**. Di kantor gue, kita punya ribuan data transaksi ruko dan apartemen kelas menengah, tapi transaksi untuk gedung pencakar langit bernilai triliunan rupiah di SCBD mungkin cuma terjadi dua atau tiga kali dalam setahun. Datanya sangat langka dan timpang (*imbalanced*). Kalau lo telan mentah-mentah data itu buat melatih sistem rekomendasi atau valuasi, sistem lo bakal sangat pintar menaksir ruko pinggiran Jakarta, tapi bakal halusinasi parah pas disuruh menilai gedung perkantoran empat puluh lantai.

Kedua, **dimensi tinggi (*curse of dimensionality*)**. Nilai sebuah aset properti komersial nggak cuma dipengaruhi oleh luas tanah dan luas bangunan. Ada faktor zonasi tata kota, lebar jalan masuk, reputasi pengembang, tingkat suku bunga acuan, sentimen politik menjelang pemilu, hingga akses transportasi umum. Begitu semua variabel ini dimasukkan ke dalam model, dimensi data meledak. Ruang data menjadi sangat kosong (*sparse*), dan risiko model mengalami *overfitting* jadi sangat tinggi. Lo butuh keahlian analisis arsitektur tingkat lanjut buat memilih representasi fitur yang benar-benar bermakna tanpa bikin komputasi lo jebol.

Ketiga, **sifat kotak hitam (*black box problem*) dan kebutuhan *Explainability***. Ini poin yang bikin gue senyum-senyum sendiri di kelas Zoom tadi. Bayangkan gue ikut usulan manajemen kantor gue: kita deploy sistem cerdas yang sepenuhnya otomatis untuk menentukan nilai valuasi gedung klien senilai dua triliun rupiah. Sistemnya mengeluarkan angka: "1,4 Triliun Rupiah."

Klien datang sambil gebrak meja: *"Kenapa gedung gue dinilai 1,4 triliun? Dasar perhitungannya dari mana? Variabel apa yang bikin nilainya jatuh 600 miliar dari ekspektasi kita?"*

Apa yang bakal kita jawab? *"Mohon maaf Pak, bobot tersembunyi di layer ketujuh jaringan saraf tiruan kami bilang begitu"*? Bisa-bisa izin operasional kantor kita dicabut minggu depannya juga!

Di domain berisiko tinggi seperti keuangan, medis, dan properti komersial, akurasi tanpa *explainability* (kemampuan untuk dijelaskan) itu sama sekali nggak ada harganya. Itulah kenapa di RPS tadi disinggung pentingnya instrumen dokumentasi modern seperti:
*   ***Model Card:*** Dokumen standar yang menjelaskan batasan model, metrik performa, konteks penggunaan yang dituju, dan kondisi di mana model tersebut tidak boleh digunakan sama sekali.
*   ***Datasheet for Datasets:*** Catatan transparan mengenai asal-usul data, bagaimana data tersebut diambil, kurasi yang dilakukan, potensi bias bawaan, hingga implikasi privasi subjek di dalam data.

Terakhir, **bias kognitif dan implikasi etika bisnis**. Sistem cerdas itu mencerminkan sejarah masa lalunya. Kalau selama sepuluh tahun terakhir ada kecenderungan bias dari para valuer manusia yang sering memandang sebelah mata kawasan suburban tertentu, model yang dilatih dari data tersebut bakal mereplikasi bias yang sama, bahkan memperkuatnya secara sistemik. Ironis kan? Alih-alih menghilangkan ketergantungan pada manusia, kita malah mengaburkan bias manusia ke dalam balutan kode matematika yang terkesan objektif.

---

## Catatan Buat Tesis GPBSales Lo

Nah, Sar, sekarang bagian paling seru yang mau gue sambungin langsung ke rencana riset lo. 

Pas dosen tadi memaparkan kerangka kerja: **Fenomena $\to$ Problem Framing $\to$ Analisis Kebutuhan $\to$ Desain Arsitektur $\to$ Evaluasi**, kepala gue langsung loncat ke dataset yang lagi lo pegang buat tesis: GPBSales dengan 1,08 juta baris data transaksi penjualan aplikasi di Google Play Store itu.

Dataset sebesar 1,08 juta baris itu adalah berkah sekaligus kutukan. Jangan sampai lo jatuh ke perangkap yang sama kayak manajemen kantor gue: punya data banyak, terus langsung mikir "pokoknya gue mau hajar pakai *deep learning* atau algoritma canggih biar kelihatan keren di depan penguji." Jangan ya, Sar!

Lo harus mulai persis dari kerangka SSAD ini:

1.  **Fenomena Bisnisnya Apa?** Jutaan aplikasi bersaing di Google Play Store, tapi mayoritas developer independen gagal membaca dinamika penetapan harga (*pricing strategy*), segmentasi pasar, dan pola unduhan berbayar yang menghasilkan konversi berkelanjutan.
2.  ***Problem Framing*: Masalah AI-nya di Mana?** Apakah lo mau membangun sistem rekomendasi harga dinamis untuk aplikasi baru berdasarkan metrik kategori dan tren pasar? Atau lo mau membangun sistem cerdas deteksi anomali untuk membedakan transaksi unduhan organik vs unduhan manipulatif (*fake downloads*) yang merusak ekosistem penjualan? Dua tujuan itu menuntut arsitektur dan paradigma sistem yang beda total.
3.  **Analisis Kebutuhannya Bagaimana?** Dengan 1,08 juta baris data, kebutuhan non-fungsional lo bakal sangat ketat di urusan *scalability*, efisiensi memori, dan integritas data. Bagaimana sistem cerdas lo menangani jutaan *missing values*, data penjualan bernilai nol (*sparse matrices*), dan *outliers* dari aplikasi raksasa yang transaksinya jomplang banget dibanding aplikasi reguler?

Tesis lo itu laboratorium hidup buat mata kuliah SSAD ini. Kalau lo bisa menstrukturkan bab metodologi penelitian lo mengikuti siklus hidup sistem cerdas yang diajarkan di RPS pertemuan satu ini, gue yakin penguji lo nggak bakal punya celah buat mendebat fondasi berpikir lo.

---

## Obrolan Meja Belajar Kita

Berhubung tugas pertemuan satu kita berbobot lima persen buat bikin analisis kritis aplikasi sistem cerdas, sekalian buat mematangkan fondasi bab satu dan bab tiga di draf tesis lo, gue mau lempar beberapa pertanyaan reflektif yang mengganjal di kepala gue sejak kelas kelar tadi:

1.  Melihat skala dataset GPBSales lo yang tembus satu juta baris lebih, gimana lo melakukan *problem framing* yang presisi agar sistem cerdas yang lo rancang nggak sekadar jadi latihan statistik deskriptif atau regresi biasa, tapi benar-benar memenuhi kriteria sistem kognitif yang memadukan pilar Data, Model, Keputusan, dan Aksi?
2.  Di domain aplikasi digital dengan volume transaksi sebesar itu, tantangan *curse of dimensionality* dan *data imbalance* pasti muncul (misalnya aplikasi gratisan mendominasi dibanding aplikasi berbayar). Menurut analisis lo, kebutuhan fungsional dan non-fungsional apa yang paling kritis harus disiapkan di level arsitektur sistem cerdas lo buat mengatasi masalah tersebut?
3.  Kalau dikaitkan sama kasus kantor gue di SCBD yang mau bikin sistem valuasi otomatis, instrumen *Explainability* (seperti *Model Card* atau *Datasheet*) itu sering dianggap beban administratif tambahan sama praktisi industri. Menurut sudut pandang lo, gimana cara membuktikan ke manajemen bahwa dokumentasi transparansi model itu sebenarnya adalah mitigasi risiko bisnis yang vital, bukan sekadar teori akademis?

Gue tunggu coretan pemikiran lo di catatan lo selanjutnya ya, Sar. Mari kita bedah bareng-bareng sebelum modul minggu depan dibuka dan kita makin dikejar tumpukan tugas analisis arsitektur.

Warmest hug from the rainy city 🩷  
Nik
