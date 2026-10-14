---
title: "Catatan Nik: Ketika Ambisi \"Pokoknya Langsung Bikin Aplikasi\" Berujung Boncos di SCBD"
subtitle: "Bos gue bilang dokumen requirement itu birokrasi yang bikin lambat. Sommerville bilang justru di situ proyek mulai boncos."
type: blog
date: 2026-10-14T13:49:36.551171+07:00
draft: false
ws_chat: 1577
ws_msg: 21457
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "software-design", "catatan-nik"]
summary: "Materi Software Design pekan ini soal software process: spesifikasi, desain, validasi, evolusi. Di kantor, bos minta anak IT langsung ngoding tanpa dokumen requirement—langsung gue sadar itu resep proyek boncos."
hook: "\"Gak usah kaku pake birokrasi dokumen requirement, yang penting anak IT langsung ngoding aja.\" Instruksi itu pas banget sama materi pekan ini: proses yang kacau bikin proyek boncos sebelum baris kode pertama jalan."
---

Setengah jam setelah rapat siang tadi bubar, gue masih betah duduk di meja kerja gue di lantai 28, Sar. Bukan karena kerjaan numpuk, tapi karena satu instruksi yang baru aja gue denger di ruang rapat bikin gue pengen ngambil napas panjang dulu sebelum pulang. 

Berhubung bobot materi pekan ini lumayan gede, gue akhirnya mutusin buat langsung bedah referensi wajibnya: Bab 2 bukunya Ian Sommerville edisi ke-10, ditambah beberapa catatan perbandingan dari Roger Pressman. Fokusnya pekan ini bener-bener nancep di fondasi paling mendasar: *software process*, empat aktivitas utamanya, dan kenapa proses yang berantakan bakal otomatis ngehancurin proyek sebelum baris kode pertama sempat di-*deploy*.

Lucunya, pas gue lagi baca konsep Sommerville soal *repeatability* dan *coping with change*, gue malah ngelamun miris ngeliat situasi di lantai kantor SCBD. Drama operasional pasca cabutnya Bram tiga minggu lalu ternyata berbuntut panjang dan mulai merembet ke mana-mana. 

Eh Sar, lo ingat kan drama tender platform *automated valuation workflow* yang gue ceritain tempo hari? Nah, proyeknya ternyata udah dimulai minggu ini. Konsultan *software house*-nya dateng, presentasi roadmap, tapi pas gue baca dokumen proposalnya, gue baru sadar: mereka paham masalah valuasi properti komersial setengah-setengah banget. *Scope* yang mereka tawarkan ngawur, campur aduk antara *market trend dashboard*, kalkulator NPV, dan *customer portal* yang sebenernya bukan kebutuhan inti divisi gue. Dan manajemen? Mereka udah tanda tangan kontrak. 

Instruksi bos gue ke tim pengembang bener-bener bikin gue elus dada: *"Gak usah kaku pake birokrasi dokumen requirement segala macem. Waktu kita sempit, yang penting anak IT langsung ngoding aja. Pokoknya dua minggu lagi prototipe jalan udah bisa dites."*

Gue cuma bisa nahan napas di pojokan ruang rapat. Di situ gue sadar, orang-orang non-teknis di level manajemen sering banget salah paham: mereka ngira rekayasa perangkat lunak itu cuma perkara mengetik sintaks di depan layar hitam bergaris hijau kayak di film *hacker*. Padahal, tanpa pemahaman mendasar soal *software process*, proyek ratusan juta itu cuma tinggal nunggu waktu buat meledak jadi biaya *rework* yang bikin boncos.

---

## Membedah Proses: Menjawab Pertanyaan "Bagaimana", Bukan Sekadar "Apa"

Mari kita lurusin dulu konsep paling dasarnya sebelum kita terjebak dalam perdebatan *framework*. Sommerville mendefinisikan *software process* sebagai sekumpulan aktivitas terstruktur yang saling terkait yang mengarah pada produksi produk perangkat lunak. Kalimat kuncinya ada di kata *bagaimana* (*how*), bukan *apa* (*what*).

Kalau bos gue di SCBD cuma mikirin *apa* produknya (sebuah aplikasi kalkulator valuasi properti berbasis web), *software process* justru ngomongin disiplin kerja di balik pembuatannya. Gimana cara tim mengumpulkan kebutuhan bisnis yang ambigu? Gimana menerjemahkan logika kapitalisasi properti ke arsitektur data? Siapa yang bertanggung jawab memvalidasi kalkulasinya? Dan apa standar kelayakan sebelum modul itu boleh diakses klien?

Berdasarkan literatur rekayasa perangkat lunak standar, sebuah deskripsi proses (*process description*) yang matang wajib memuat empat elemen terstruktur:

1. **Activities (Langkah Kerja)**: Urutan aksi nyata yang harus dieksekusi, mulai dari wawancara *stakeholder*, pemodelan sistem, penulisan unit uji, sampai integrasi antarmuka.
2. **Products atau Artifacts (Luaran Nyata)**: Hasil berwujud dari setiap langkah kerja. Ini bukan cuma *executable file* atau aplikasi jadi, tapi mencakup dokumen spesifikasi kebutuhan (*SRS*), diagram arsitektur, laporan peninjauan kode (*code review*), sampai skenario uji (*test cases*).
3. **Roles (Tanggung Jawab Personal)**: Siapa ngerjain apa. Siapa yang jadi *analyst*, *architect*, *developer*, *tester*, dan siapa *domain expert* yang pegang validasi bisnis. Di kantor gue, kekacauan terjadi karena manajemen nyuruh satu anak magang IT buat merangkap semua peran ini sekaligus.
4. **Pre-conditions dan Post-conditions (Syarat Batas)**: Kondisi yang wajib terpenuhi sebelum sebuah aktivitas dimulai dan setelah aktivitas itu dinyatakan selesai. Misalnya, tim pengembang dilarang mulai merancang struktur basis data (*pre-condition*) sebelum kamus data divalidasi oleh konsultan properti senior (*post-condition* dari tahap analisis).

Gak ada satu proses tunggal yang berlaku buat semua jenis proyek di dunia ini. Proyek sistem kendali rem pesawat terbang gak mungkin pake proses yang sama dengan proyek pembuatan landing page promo apartemen akhir tahun. Proses selalu bersifat kontekstual: tergantung skala sistem, regulasi industri, kompetensi tim, dan yang paling krusial, seberapa cepat kebutuhan pengguna bakal berubah di tengah jalan.

---

## Empat Aktivitas Fundamental yang Gak Boleh Lo Langkahi

Nah, ini inti bahasan pekan kedua, Sar. Mau lo pake pendekatan tradisional yang kaku atau pendekatan modern yang serba lincah, Sommerville menegaskan kalau semua model proses rekayasa perangkat lunak di dunia ini pasti bertumpu pada empat aktivitas fundamental. Empat aktivitas ini bukan fase sekuensial yang sekali jalan langsung ditinggal, melainkan siklus berulang yang saling mengikat.

```
       +---------------------------------------------+
       |                                             |
       v                                             |
[ 1. Specification ] <---> [ 2. Design & Impl ]      | (Iterative Feedback)
       |                            |                |
       +------------+---------------+                |
                    |                                |
                    v                                |
         [ 3. Validation ] --------------------------+
                    |
                    v
         [ 4. Evolution ]
```

Mari kita bedah satu per satu pakai kacamata bisnis riil:

### 1. Software Specification (Requirements Engineering)
Ini aktivitas mendasar buat memahami dan menetapkan layanan apa yang dibutuhkan oleh sistem serta batasan operasional dan pengembangannya. Tahap ini bukan cuma duduk dengerin celotehan *user*, tapi melibatkan proses *elicitation* (eksplorasi mendalam), analisis kelayakan, dokumentasi spesifikasi, dan validasi kebutuhan.

Di sini kita wajib membedakan dua lapis kebutuhan:
*   *Functional requirements*: Sistem harus bisa ngitung *discounted cash flow* (DCF) dari aset gedung perkantoran berdasarkan variabel okupansi dan inflasi.
*   *Non-functional requirements*: Sistem harus bisa ngeluarin hasil kalkulasi dalam waktu di bawah dua detik saat diakses bersamaan oleh lima puluh konsultan, dan datanya harus terenkripsi sesuai standar UU Perlindungan Data Pribadi.

Waktu tim manajemen kantor gue bilang "langsung ngoding aja", mereka sebenernya lagi membuang aktivitas spesifikasi ke tong sampah. Akibatnya fatal. Begitu pengembang gak dapet batasan yang jelas, mereka bakal berasumsi. Dan di dunia sistem informasi, asumsi teknis yang keliru dari awal adalah resep paling jitu buat ngebakar anggaran perusahaan.

### 2. Software Design & Implementation
Aktivitas ini adalah jembatan yang mengubah dokumen kebutuhan abstrak tadi menjadi sistem perangkat lunak yang beneran jalan. Desain perangkat lunak merancang struktur perangkat lunak yang merealisasikan spesifikasi, sedangkan implementasi menerjemahkan struktur tersebut menjadi program yang dapat dieksekusi mesin.

Tahapan desain itu krusial banget: lo nentuin arsitektur sistem secara makro (*high-level architecture*), struktur basis data, antarmuka antar-komponen, sampai algoritma spesifik yang mau dipakai. Tanpa fase desain yang bener, *developer* bakal nulis kode secara spageti. Di kantor gue, gara-gara gak ada perancangan skema data valuasi yang bener, nilai sewa properti dalam mata uang asing dicampuradukkan dalam satu kolom numerik tanpa indikator kurs. Begitu dicoba *run*, seluruh proyeksi *yield* investasi langsung berantakan total.

### 3. Software Validation
Validasi adalah proses memastikan bahwa perangkat lunak yang dibangun bener-bener memenuhi ekspektasi dan kebutuhan riil dari pelanggan. Sommerville ngasih penekanan tajam soal perbedaan dua konsep kembar yang sering bikin mahasiswa S2 kebolak-balik: *Verification* dan *Validation* (V&V).

*   **Verifikasi**: *"Are we building the product right?"* (Apakah kita membangun produk dengan benar sesuai standar teknis?). Ini urusan apakah kodenya bebas *bug*, sintaksnya rapi, arsitekturnya efisien, dan lolos uji unit teknis.
*   **Validasi**: *"Are we building the right product?"* (Apakah kita membangun produk yang benar sesuai kebutuhan bisnis?). Ini urusan apakah aplikasi yang udah bebas *bug* tadi beneran bisa nyelesaiin masalah kerja sehari-hari pengguna.

Bisa aja tim IT bikin kalkulator valuasi yang sempurna tanpa eror teknis sama sekali (verifikasi sukses), tapi pas dicoba ke konsultan properti, rumusnya ternyata pake metode valuasi residensial sederhana yang gak relevan buat gedung perkantoran bertingkat banyak (validasi gagal total). Tanpa aktivitas validasi yang melibatkan peninjauan pengguna (*user acceptance testing*), lo cuma lagi memproduksi rongsokan digital yang mahal.

### 4. Software Evolution
Ini realitas pahit yang wajib dipahami orang-orang manajemen: perangkat lunak gak pernah bener-bener selesai. Berbeda sama jembatan beton atau gedung pencakar langit di Sudirman yang bakal aus secara fisik kemakan cuaca, perangkat lunak gak kenal aus fisik. Tapi perangkat lunak bakal "menua" (*software ages*) setiap kali lingkungan bisnis, regulasi, dan kebutuhan penggunanya bergeser.

Evolusi perangkat lunak adalah aktivitas menyesuaikan, memodifikasi, dan memperluas sistem yang udah beroperasi agar tetap relevan. Ketika regulasi perpajakan tanah komersial berubah tahun depan, sistem valuasi tadi harus diubah kodenya. Kalau arsitektur awalnya dirancang berantakan tanpa proses yang rapi, proses evolusi ini bakal jadi mimpi buruk teknis (*technical debt*). Setiap kali ada baris kode baru yang ditambal, dua modul lama lainnya bakal ikutan jebol.

---

## Mengapa Keterkaitan Proses Menentukan Biaya Riil Perusahaan?

Di level magister kayak kita sekarang, Sar, sudut pandang kita gak boleh cuma berhenti di buku teks teknis. Kita harus bisa narik garis lurus antara teori proses rekayasa perangkat lunak dengan kalkulasi untung-rugi di neraca keuangan perusahaan.

Kunci utama dari rekayasa perangkat lunak modern sebenernya adalah *coping with change*, gimana cara kita mengelola perubahan kebutuhan tanpa bikin proyek bangkrut di tengah jalan. Sommerville nyebutin dua strategi operasional yang sangat relevan buat ngurangin biaya perubahan:

1. **Prototyping**: Membangun versi kasar atau visualisasi awal dari sistem secara cepat, semata-mata buat divalidasi ke *stakeholder*. Tujuannya biar *user* bisa ngeliat, nyentuh, dan ngoreksi kesalahan pemahaman sistem sebelum tim teknis ngabisin waktu ratusan jam buat nulis kode arsitektur yang sebenarnya.
2. **Incremental Delivery**: Daripada nahan aplikasi di dalam goa laboratorium selama setahun penuh demi ngejar rilis tunggal yang raksasa, tim menyerahkan sistem sedikit demi sedikit dalam siklus rilis bertahap. Modul yang paling kritikal nilainya bagi bisnis diserahkan duluan, dapet *feedback* nyata dari pasar, baru lanjut ke modul pendukung berikutnya.

Kalau keempat aktivitas utama tadi gak dirangkai dalam proses yang disiplin, fenomena klasik di dunia korporat bakal terulang lagi: *rework* alias kerja dobel. Biaya ngebenerin salah paham kebutuhan pas fase spesifikasi itu murah banget, paling cuma modal revisi dokumen atau gambar diagram di papan tulis. Tapi kalau kesalahan spesifikasi itu baru ketahuan pas sistem udah jalan di level operasional (fase evolusi), biayanya bisa melonjak seratus kali lipat karena lo harus bongkar basis data, tulis ulang logika kode, dan bayar kompensasi ke klien yang datanya rusak.

Ini juga kenapa ada konsep *process improvement* kayak kerangka CMMI (*Capability Maturity Model Integration*). Perusahaan yang dewasa gak cuma mengandalkan kejeniusan individu tertentu (kayak ketergantungan kantor gue ke sosok Bram). Ketergantungan ke satu orang itu rapuh banget. Organisasi yang sehat bakal nerapin siklus **measure -> analyze -> change** secara berkala. Kualitas kerja tim distandarkan lewat proses yang bisa diulang (*repeatable*), sehingga siapa pun yang masuk atau keluar, mutu perangkat lunak yang dihasilkan perusahaan tetap terjamin dan terprediksi jadwalnya.

Pekan depan kita bakal ngeliat gimana aktivitas-aktivitas fundamental ini disusun dalam berbagai bentuk pola arketipe, mulai dari *Waterfall* yang linier kaku, pendekatan *Agile* yang fleksibel adaptif, sampai model *Spiral* yang berorientasi mitigasi risiko. Tapi lo gak bakal bisa milih model proses yang pas kalau lo belum paham anatomi dari empat aktivitas dasarnya hari ini.

---

## Bahan Diskusi Buat Catatan Lo Berikutnya

Biar otak lo ikutan panas dan kita bisa lanjut diskusi pekan depan, gue mau ninggalin beberapa pertanyaan analitis nih buat lo. Coba lo bedah pakai perspektif manajemen sistem informasi:

1. Mengingat karakter industri konsultan properti di kantor gue yang ritmenya serba dinamis dan sering kali regulasi valuasinya berubah mendadak dari otoritas pemerintah, menurut lo, di antara aktivitas *software specification* dan *software validation*, mana yang membawa risiko finansial paling besar kalau dipangkas demi ngejar *deadline* peluncuran sistem?
2. Kalau lo diposisikan sebagai manajer proyek di kantor gue yang lagi krisis pasca hengkangnya Bram, gimana argumen lo meyakinkan jajaran direksi bahwa langsung terjun ke penulisan kode tanpa dokumen spesifikasi yang tervalidasi justru bakal memperpanjang durasi proyek dan melipatgandakan anggaran?
3. Sommerville bilang perangkat lunak gak aus secara fisik melainkan menua akibat modifikasi (*evolution*). Dalam konteks tata kelola enterprise, tanda-tanda konkret apa yang menunjukkan bahwa sistem warisan di sebuah perusahaan udah masuk fase kadaluarsa dan biayanya lebih murah dibangun ulang daripada terus-menerus dirawat?

Sambil nyeduh teh chamomile kedua sebelum nyiapin bahan presentasi kantor buat besok pagi,

Nik
