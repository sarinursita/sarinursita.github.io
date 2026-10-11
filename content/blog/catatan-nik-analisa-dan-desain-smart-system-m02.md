---
title: "Catatan Nik: Ketika Tumpukan Excel Warisan Bram Dianggap Big Data"
subtitle: "Antara Ilusi AI dan Realitas CRISP-DM"
type: blog
date: 2026-10-12T05:00:00+07:00
draft: true
ws_chat: 1576
ws_msg: 21446
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "analisa-dan-desain-smart-system"]
summary: "Materi SSAD pertemuan 2 soal CRISP-DM, jenis data, dan skala NOIR dijahit ke drama kantor Nik: manajemen mau lempar arsip valuasi 15 tahun langsung ke machine learning, padahal datanya belum pernah dibaca sebagai data."
hook: "\"Kenapa nggak langsung lempar aja semua data itu ke model machine learning?\" kata salah satu petinggi di all-hands meeting. Nik tersedak kopi, karena materi pekan ini justru bilang: data bukan tujuan."
---

Rumah gue hening banget sore ini, Sar. Sejak Dylan balik ke asrama hari Minggu kemarin, nggak ada lagi suara dia yang bolak-balik buka kulkas nyari camilan atau ribut nyari kaos basketnya yang nyelip. Hening kayak gini justru ngasih gue waktu buat selonjoran di sofa ruang tengah, ditemani secangkir *earl grey* hangat, sambil buka modul pekan kedua mata kuliah Analisis dan Perancangan Sistem Cerdas (*Smart System Analysis and Design* / SSAD). Di luar, hujan udah turun deras dari jam dua siang, dan itu makin bikin gue nggak punya alasan buat beranjak dari posisi ini.

Gue beneran butuh *grounding* akademis ini, Sar. Soalnya kalau nggak, kepala gue bisa meledak ngeliat kelakuan orang-orang kantor di SCBD sepanjang minggu ini.

Lo inget kan cerita gue kemarin pas Bram cabut mendadak sambil bawa dua *lead valuer* andalannya? Nah, kepanikan manajemen bukannya mereda, malah makin absurd. Di *all-hands meeting* kemarin lusa, salah satu petinggi dengan entengnya bilang di depan semua orang: *"Kita kan punya arsip penilaian properti lima belas tahun terakhir di server. Kenapa nggak langsung kita lempar aja semua data itu ke model machine learning? Bikin automated valuation engine minggu depan, biar kita nggak tergantung sama orang lagi."*

Gue yang lagi nyeruput kopi langsung tersedak di depan layar Zoom. Rasanya pengen banget gue interupsi dan teriak: *"Pak, lo pikir machine learning itu panci presto yang tinggal lo cemplungin bahan mentah acak-acakan terus mateng sendiri jadi gulai?"*

Obrolan kantor yang halu itu bener-bener pas banget sama materi yang lagi kita pelajari sekarang: fase *Data Understanding* dalam kerangka kerja CRISP-DM, pemahaman jenis data, skala pengukuran NOIR, sampai instrumen pengumpulan informasi awal. Mari kita bedah bareng-bareng kebodohan korporat ini pakai kacamata MMSI yang waras.

---

## CRISP-DM dan Hobi Manajemen Melompati Tangga

Di kampus lo udah masuk materi CRISP-DM (*Cross-Industry Standard Process for Data Mining*) kan? Kerangka kerja ini ibarat kompas buat siapa pun yang mau bikin sistem analitik atau sistem cerdas biar nggak nyasar ke jurang halusinasi.

Ada enam fase berulang yang udah teruji puluhan tahun:
1. *Business Understanding*
2. *Data Understanding*
3. *Data Preparation*
4. *Modeling*
5. *Evaluation*
6. *Deployment*

Penyakit akut di banyak korporasi, termasuk kantor konsultan properti gue, adalah nafsu besar buat langsung lompat dari *Business Understanding* yang masih setengah matang langsung loncat ke fase 4: *Modeling*. Begitu ada masalah bisnis (kehilangan tim *valuer*), mereka pengen langsung bikin model AI yang canggih. Fase 2 (*Data Understanding*) dan fase 3 (*Data Preparation*) dianggap cuma remah-remah teknis yang bisa disulap dalam semalam.

Padahal, di buku *Data Science for Business*, Provost & Fawcett udah ngingetin satu prinsip fundamental: data itu bukan tujuan akhir (*data is not the goal*). Tanpa pemahaman konteks bisnis yang presisi, data dalam jumlah masif cuma bakal jadi tumpukan angka yang nggak punya arti. Mengumpulkan data sebanyak-banyaknya tanpa tahu apa yang relevan dengan pertanyaan bisnis lo adalah cara tercepat buat buang-buang *budget cloud storage*.

Di sinilah berlaku hukum abadi: *garbage in, garbage out* (GIGO). Kualitas input bakal menentukan seratus persen kualitas output sistem cerdas lo. Kalau data yang lo masukin ke algoritma itu bias, bolong-bolong, atau bahkan definisinya salah kaprah, model secanggih apa pun cuma bakal menghasilkan keputusan salah yang dipoles dengan grafik keren. Verifikasi kualitas data bukan pekerjaan sampingan di akhir proyek, tapi harga mati yang harus dibereskan di fase *Data Understanding*.

---

## Skala NOIR dan Tragedi Menghitung Rata-Rata Kode Pos

Kemarin tim internal sempat narik data mentah dari *database* peninggalan timnya Bram. Salah satu anak analis yang baru masuk dikasih tugas buat bikin ringkasan awal portofolio properti komersial kita. Pas gue liat draf laporannya, gue hampir pingsan. Di lembar *summary*, dia ngitung nilai rata-rata (*mean*) dan standar deviasi dari kolom kode pos gedung dan kelas zonasi wilayah.

Gue elus dada. Ini materi dasar statistik tingkat satu yang sering banget dilupain orang pas udah megang *tools* canggih kayak Python atau Tableau. Kita nggak bisa asal hajar semua operasi matematika ke sembarang kolom data. Skala pengukuran menentukan operasi statistik apa yang sah dan boleh dilakukan secara ilmiah.

Yuk, kita segarkan ingatan soal skala NOIR ini:

### 1. Nominal
Ini skala paling dasar. Angka atau label di sini cuma berfungsi sebagai nama atau kategori pembeda tanpa ada tingkatan nilai sama sekali. Relasi logisnya cuma sama dengan (=) atau tidak sama dengan (≠).
* Contoh di kantor gue: jenis properti (*Office*, *Retail*, *Industrial*), kode pos, nama kota, atau ID transaksi.
* Operasi yang sah: lo cuma boleh ngitung modus (kategori mana yang paling sering muncul) dan frekuensi.
* Dosa besar: ngitung rata-rata kode pos. Kalau gedung A ada di kode pos 12190 (SCBD) dan gedung B di kode pos 12950 (Kuningan), rata-rata 12570 itu nggak ada artinya sama sekali, Sar! Itu nama daerah lain di Jagakarsa yang karakteristik pasarnya beda total.

### 2. Ordinal
Skala kategorik yang sudah punya urutan atau peringkat logis, tapi jarak antarperingkatnya nggak bisa diukur secara pasti. Relasi logisnya adalah lebih besar dari (>) atau lebih kecil dari (<).
* Contoh: *grade* gedung perkantoran (*Grade A*, *Grade B*, *Grade C*), tingkat kepuasan klien (*Sangat Puas* sampai *Sangat Kecewa*), atau kelas risiko investasi.
* Operasi yang sah: median dan persentil, selain modus.
* Batasan: lo nggak bisa bilang jarak antara gedung *Grade A* ke *Grade B* itu sama persis dengan jarak dari *Grade B* ke *Grade C*. Jadi, melakukan operasi penambahan atau pembagian di sini secara teoritis sangat cacat.

### 3. Interval
Skala numerik yang jarak antar-nilainya bermakna dan terukur secara konstan, tapi **tidak punya nilai nol mutlak** (*arbitrary zero*).
* Contoh klasik: suhu dalam Celsius atau Fahrenheit, tahun kalender, atau skor indeks sentimen pasar properti tertentu.
* Operasi yang sah: penjumlahan dan pengurangan (+ dan -). Lo bisa ngitung nilai *mean* dan standar deviasi.
* Batasan: lo nggak bisa bikin rasio perkalian. Suhu 40 derajat Celsius bukan berarti dua kali lebih panas dari 20 derajat Celsius, karena titik 0 derajat Celsius bukan berarti ketiadaan suhu sama sekali (partikelnya masih bergerak).

### 4. Rasio
Ini kasta tertinggi dalam skala pengukuran data. Jaraknya bermakna, dan dia **punya nilai nol mutlak**. Angka nol di sini bener-bener berarti ketiadaan atribut tersebut secara absolut.
* Contoh: harga sewa per meter persegi, luas bangunan, tingkat okupansi (*occupancy rate*), total nilai kapitalisasi gedung, dan jumlah lantai.
* Operasi yang sah: semua operasi matematika dasar (+, -, ×, ÷). Lo bisa ngomong kalau harga sewa gedung di Sudirman senilai 300 ribu rupiah per meter persegi itu bener-bener dua kali lipat lebih mahal dibanding gedung di TB Simatupang yang sewanya 150 ribu rupiah per meter persegi. Di sini, rasio itu valid secara matematika dan bisnis.

Kalau tim kita mau bikin sistem penilaian otomatis tapi dari awal udah salah memperlakukan variabel ordinal seolah-olah data rasio, sistem cerdas itu bakal ngeluarin estimasi valuasi yang ngawur dari akarnya.

---

## Dari PDF Berdebu Sampai Log Server: Realitas Struktur Data

Tantangan kedua yang bikin pusing pas gue audit data warisan Bram adalah bentuk dan strukturnya. Orang non-teknis di manajemen sering mikir kalau data perusahaan itu bentuknya selalu tabel rapi kayak di buku pelajaran. Faktanya? Nyaris 70 persen data penting yang ditinggalin Bram itu *unstructured* alias berantakan.

Biar rapi, mari kita petakan spektrum struktur data yang kita hadapi di lapangan:

* **Data Terstruktur (*Structured*)**: Data yang punya skema kaku, tersusun rapi dalam baris dan kolom, dan sangat ramah buat basis data relasional (SQL). Di kantor, ini mencakup data transaksi sewa yang udah masuk sistem penagihan, tabel master properti, dan histori pembayaran *service charge*. Semuanya punya tipe data yang jelas: *integer*, *varchar*, *date*, atau *float*.
* **Data Semi-Terstruktur (*Semi-structured*)**: Data yang nggak punya struktur tabel relasional formal, tapi masih punya penanda internal atau hierarki (*tags*) yang bikin elemennya bisa dipisahkan secara terprogram. Contohnya data log aktivitas user di portal klien kami, pertukaran data API dari vendor riset pasar properti dalam format JSON atau XML, sampai *metadata* email korespondensi negosiasi harga.
* **Data Tidak Terstruktur (*Unstructured*)**: Ini tambang emas sekaligus mimpi buruk terbesar. Bram dan timnya selama bertahun-tahun nyimpen laporan valuasi akhir dalam bentuk ribuan dokumen PDF, catatan hasil survei lapangan yang diketik bebas di Word, foto-foto kondisi fisik gedung dan keretakan dinding, rekaman suara wawancara dengan pengelola gedung, sampai denah lantai dalam format CAD/gambar.

Kalo manajemen mau bikin sistem valuasi otomatis, mereka nggak bisa cuma ngandelin data terstruktur yang jumlahnya sedikit. Tapi buat narik informasi dari ribuan lembar PDF dan foto itu butuh teknik pengolahan informasi awal yang sama sekali beda: butuh OCR (*Optical Character Recognition*), pemrosesan bahasa alami (NLP), dan *computer vision*. Bukan sekadar *load database* terus jalanin regresi linear!

Selain soal struktur, kita juga harus cermat membedakan data berdasarkan dimensi waktu:
* Apakah data kita berupa *cross-sectional*, yaitu potret satu titik waktu tertentu (misalnya harga sewa semua gedung perkantoran di Jakarta per kuartal 3 tahun 2024)?
* Atau data kita berbentuk *time-series* / *longitudinal*, yang melacak satu atau beberapa properti yang sama secara berurutan dalam rentang waktu panjang buat ngeliat tren fluktuasi harga?
* Kalau kita gabungin keduanya (banyak gedung diamati selama puluhan tahun secara berkala), kita dapet **data panel**, yang analisis ekonometrikanya jauh lebih kompleks tapi paling akurat buat nangkep dinamika pasar.

Belum lagi kalau kita ngomongin karakteristik *Big Data* lewat lensa 5V:
* **Volume**: Berapa ratus gigabyte data yang mau kita olah?
* **Velocity**: Seberapa cepet data transaksi properti baru masuk ke sistem kita?
* **Variety**: Seberapa campur aduk format tabel, teks laporan, denah arsitektur, dan gambar satelit yang kita punya?
* **Veracity**: Seberapa jauh kita bisa percaya keakuratan catatan survei manual yang dibikin tim *junior valuer* lima tahun lalu?
* **Value**: Dari semua tumpukan itu, mana yang bener-bener berdampak ke akurasi valuasi dan profitabilitas bisnis perusahaan?

Kebanyakan orang cuma silau sama *Volume*, tapi buta total soal *Veracity* dan *Value*.

---

## Fondasi yang Sering Ditinggalkan: Kamus Data, Profiling, dan Jeratan Hukum

Sebelum seorang analis berani nyentuh algoritma apa pun, ada dua instrumen dasar yang wajib hukumnya untuk dibuat: **Data Dictionary** (Kamus Data) dan **Data Profiling**.

Kamus data itu semacam kitab suci. Dia mendefinisikan secara gamblang arti dari setiap kolom di *dataset*. Di tabel warisan Bram, ada kolom bernama `rent_adj`. Nggak ada dokumentasi sama sekali! Apakah itu *rent adjustment* (diskon sewa), *rental adjusted for inflation*, atau malah biaya sewa tambahan di luar *service charge*? Kalau analis yang mengolah salah mengartikan kolom ini, seluruh model prediksi bakal hancur lebur. Kamus data harus mencakup nama variabel, tipe data, skala pengukuran (NOIR tadi), satuan pengukuran (apakah Rupiah per meter persegi atau per *square feet*), rentang nilai yang valid, serta arti dari kode-kode kategorik tertentu.

Setelah kamus datanya jelas, kita harus jalanin **data profiling**. Kita bedah isi perut datanya secara statistik deskriptif awal:
* Berapa jumlah baris dan kolom yang unik?
* Berapa banyak *missing values* (nilai kosong) di setiap atribut?
* Bagaimana distribusi frekuensi tiap kategori?
* Apakah ada nilai-nilai yang aneh di luar rentang wajar (misalnya ada gedung yang luasnya tercatat minus sepuluh meter persegi)?

Dan yang paling krusial dari semuanya di era sekarang, Sar: **aspek etika dan legalitas**.

Waktu gue buka sebagian arsip yang ditinggalin tim Bram, gue merinding. Di dalam folder-folder survei pasar itu, bertebaran salinan perjanjian sewa menyewa yang mencantumkan nama lengkap penyewa individu, nomor KTP, nomor rekening bank, sampai nomor ponsel pribadi pemilik properti kelas kakap (*Ultra High Net Worth Individuals*).

Di Indonesia sekarang udah berlaku penuh Undang-Undang Perlindungan Data Pribadi (UU PDP). Kita nggak bisa sembarangan nyedot data mentah yang ada data pribadinya ke server pengolahan, apalagi kalau server komputasi awan yang mau kita pakai server pihak ketiga di luar negeri! Perusahaan bisa kena sanksi pidana dan denda puluhan miliar rupiah kalau sampai data sensitif itu bocor atau diolah tanpa *informed consent* eksplisit dari subjek datanya.

Sebelum data itu boleh dipakai buat melatih sistem cerdas apa pun, harus ada proses *anonymization* (penghilangan identitas permanen) atau minimal *pseudonymization* (penggantian identitas dengan kode pengenal buatan). Memastikan kepatuhan regulasi privasi ini adalah pintu gerbang mutlak di tahap pengumpulan informasi awal.

---

## Analogi dari Tesis Penjualan Buku Digital

Sambil mikirin kekacauan data properti di kantor, gue jadi inget waktu kita bahas rencana tesis lo tempo hari soal *dataset* transaksi penjualan buku digital global (GPBSales) yang jumlahnya tembus satu juta baris lebih itu.

Logika CRISP-DM dan skala NOIR ini persis sama penerapannya di sana, Sar. Di *dataset* buku digital itu:
* Kolom seperti `author`, `series`, judul buku, negara pembeli, dan `order_id` atau ID transaksi adalah skala **Nominal**. Operasi yang valid cuma melihat judul buku mana yang paling sering dibeli (modus) atau sebaran penjualan per negara (frekuensi). Menghitung rata-rata dari ID transaksi jelas tindakan absurd.
* Kolom seperti periode bulan rilis atau kuartal penerbitan bisa masuk skala **Ordinal** kalau kita cuma ngeliat urutan siklus rilisnya.
* Kolom `amount` (nilai transaksi rupiah/dolar) dan kuantitas unit buku yang dibeli jelas merupakan skala **Rasio**. Ada nilai nol mutlak kalau buku itu dibagikan gratis (harga = 0) atau tidak ada yang terjual sama sekali. Di sini lo sah menghitung rata-rata pendapatan per hari, standar deviasi omzet bulanan, atau membandingkan bahwa penjualan buku A tiga kali lipat lebih laris dibanding buku B.
* Dimensi waktunya jelas berbentuk **time-series** longitudinal lewat kolom `transaction_date`, di mana urutan waktu transaksi punya pengaruh besar terhadap analisis tren musiman (*seasonality*, misal lonjakan penjualan pas liburan sekolah).

Kalau dari awal lo salah memetakan jenis data ini di tesis lo, algoritma klasifikasi atau klasterisasi yang lo rancang di tahap *Modeling* nanti bakal ngasih hasil yang bias dan nggak bisa dipertanggungjawabkan di depan penguji sidang.

Pekan depan, di Pertemuan 3, materi kita bakal melompat lebih dalam ke verifikasi kualitas data (enam dimensi kualitas data, penanganan *missing values*, *outliers*, duplikasi) dan teknik *Exploratory Data Analysis* (EDA). Tapi sebelum lo bisa bersihin data di Pertemuan 3, lo harus ngerti dulu anatomi data mentah lo di Pertemuan 2 ini.

---

## Catatan Diskusi untuk Lo

Gue pengen denger sudut pandang lo, Sar. Coba lo bayangin posisi lo sebagai konsultan sistem informasi independen yang diminta bantuin kantor gue keluar dari jebakan warisan Bram ini.

Gue punya tiga pertanyaan analitis buat lo renungkan:

1. Kalau manajemen kantor gue tetep ngotot pengen manfaatin ribuan dokumen PDF laporan penilaian properti lama yang formatnya nggak standar dan penuh teks narasi bebas, pendekatan pengumpulan dan penataan data awal (*data ingestion & structuring*) seperti apa yang paling realistis lo rekomendasikan sebelum data itu bisa dipakai buat sistem cerdas?
2. Terkait UU PDP dan etika bisnis, langkah konkret apa yang harus diambil tim data saat menemukan tumpukan data transaksi masa lalu yang memuat informasi finansial privat klien korporat dan individu, sementara manajemen menolak menghapus data tersebut karena dianggap sebagai fitur penentu akurasi model valuasi?
3. Di *dataset* tesis lo (atau kasus analitik buku digital yang kita bahas tadi), ada atribut nominal (seperti nama penulis) yang jumlah kategori uniknya bisa mencapai ribuan (*high-cardinality nominal features*). Dari perspektif persiapan data untuk sistem cerdas, tantangan analitis apa yang bakal muncul kalau variabel nominal dengan kardinalitas tinggi seperti ini dipaksakan masuk ke model prediktif, dan bagaimana lo membedakan perlakuannya dengan variabel rasio murni?

Hujan di luar udah mulai reda nih, menyisakan hawa dingin khas Bogor yang menusuk tulang. Gue mau siap-siap bikin mi instan kuah dulu sambil nunggu kelas asinkronus berikutnya dibuka di LMS.

Warmest hug from the rainy city 🩷  
Nik
