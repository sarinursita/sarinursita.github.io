---
title: "Catatan Nik: Menyisir Benang Kusut: Cara Kita Berhenti Menyalahkan Kode Saat Manusia yang Berantakan"
subtitle: "Gue masuk kelas ini mikir bakal belajar arsitektur dan framework, ternyata yang paling sering dibahas manusia yang nggak bisa bilang apa yang mereka mau."
type: blog
date: 2026-11-26T05:00:00+07:00
draft: true
ws_chat: 1735
ws_msg: 21979
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "software-design", "evaluasi", "catatan-nik"]
summary: "Gue rangkum tujuh sesi Software Design: matkul ini sebenarnya ilmu mengendalikan kekacauan lewat proses, bukan menulis kode lebih cepat. Dari etika profesi dan model proses, Agile dan Scrum, sampai requirement engineering."
hook: "Bertahun-tahun gue nyalahin kode, padahal yang berantakan biasanya kesepakatan sama manusianya."
---

Secangkir kopi yang sudah dingin di samping keyboard mendadak terasa pas banget menggambarkan isi kepala gue malam ini. Di layar, tujuh dokumen catatan kuliah gue dari beberapa pekan ke belakang kebuka berdampingan sama berkas evaluasi proyek portal klien yang sempat bikin geger kantor tempo hari. 

Gue perhatiin lagi lembar demi lembar catatan itu. Rasanya aneh menyadari betapa cepatnya kita sampai di titik jeda tengah semester ini. Kalau dipikir-pikir, sebelum kita masuk ke kelas pertama, bayangan gue soal rekayasa perangkat lunak atau *software development* itu sangat teknikal: baris kode, arsitektur *database*, *framework* JavaScript terbaru, atau algoritma rumit yang cuma dipahami anak IT. Gue pikir mata kuliah ini bakal memaksa kita bertransformasi jadi programmer dadakan.

Ternyata, makin ke sini gue makin sadar kalau mata kuliah ini sebenarnya ilmu tentang manusia yang mencoba mengendalikan kekacauan. 

Di dunia nyata, software itu bukan sekadar tumpukan logika biner yang hidup di ruang hampa. Software adalah kesepakatan sosial antara bisnis yang nggak sabaran, pengguna yang punya kebiasaan unik, dan tim pengembang yang harus menjaga sistem tetap waras. Inti dari seluruh disiplin ini adalah bagaimana kita membangun sesuatu yang abstrak secara terstruktur, terukur, dan bertanggung jawab, di tengah dunia yang setiap hari berubah pikiran.

---

## Dari Tanggung Jawab Moral Menuju Rantai Pengiriman: Membaca Peta Tujuh Sesi

Kalau ditarik garis lurus dari pertemuan pertama sampai sesi terakhir, materi kuliahnya sebenarnya nggak pernah melompat acak. Semuanya tersusun seperti jalan setapak yang sengaja dibangun buat membongkar ilusi kita soal proyek teknologi.

Perjalanan kita dimulai dari fondasi yang paling mendasar: memahami hakikat perangkat lunak, profesionalisme, dan etika. Di sesi pertama, kita disadarkan bahwa software bukan karya seni privat yang selesai begitu fungsinya jalan di laptop pembuatnya. Ketika sistem dipakai publik atau korporasi, ada dimensi keselamatan, privasi, dan tanggung jawab hukum yang melekat di pundak kita. Kita nggak bisa asal lempar fitur tanpa memikirkan dampak sosialnya. 

Dari kesadaran etis itu, kita langsung dihadapkan pada kenyataan pahit di sesi kedua: sistem perangkat lunak itu hidup di lingkungan yang dinamis. Di sinilah konsep *software process* masuk. Kita belajar empat pilar aktivitas fundamental yang nggak bisa ditawar, yaitu spesifikasi kebutuhan, perancangan dan implementasi, validasi, serta evolusi sistem. Tanpa proses yang jelas, organisasi cuma bakal reaktif menghadapi perubahan dan akhirnya tenggelam dalam biaya perbaikan yang membengkak.

Begitu memahami bahwa proses itu wajib ada, pertanyaan berikutnya muncul: kendaraan apa yang mau kita pakai untuk menjalani proses tersebut? Sesi ketiga menjawabnya lewat spektrum model proses. Kita membedah model sekuensial seperti Waterfall yang menuntut kepastian sejak awal, pendekatan bertahap lewat *Incremental*, fleksibilitas iteratif ala Agile, manajemen risiko berlapis pada model Spiral, hingga pembuatan *Prototyping* buat menjinakkan ketidakpastian pengguna. Di sesi ini, kita belajar bahwa nggak ada model yang suci; memilih model proses itu soal mencocokkan karakter masalah, tingkat risiko, dan stabilitas kebutuhan.

Ketika dinamika bisnis menuntut kecepatan adaptasi yang lebih ekstrem, bahasan kita bergeser ke filosofi pengembangan tangkas di sesi keempat. Kita menyelami Agile bukan sekadar sebagai metodologi kerja, melainkan cara pandang. Lewat empat nilai di Agile Manifesto dan dua belas prinsip pendukungnya, kita melihat pergeseran fokus dari dokumentasi tebal ke perangkat lunak yang benar-benar berfungsi dan kolaborasi manusia. Di sini kita juga membedah praktik teknis seperti *Extreme Programming* (XP) sekaligus batasan-batasan realistisnya saat harus diterapkan di organisasi skala besar yang birokratis.

Filosofi Agile yang abstrak itu baru terasa membumi begitu kita masuk ke sesi kelima, saat kerangka kerja Scrum dan praktik DevOps digabungkan. Scrum memberi kita struktur konkret: tiga akuntabilitas yang jelas, lima ritual waktu, serta tiga artefak dengan komitmen transparansinya. Namun, Scrum bakal pincang kalau rilis perangkat lunaknya masih manual dan memicu konflik antara tim pengembang dan operasional. Di titik temu itulah DevOps hadir bersama jalur otomatisasi CI/CD (*Continuous Integration / Continuous Delivery*), memastikan setiap iterasi kecil yang disepakati bisa meluncur ke tangan pengguna secara aman dan konsisten.

Setelah infrastruktur proses dan eksekusinya rapi, dua sesi terakhir mengajak kita menyelam ke bagian yang paling sering jadi biang kerok kegagalan proyek: *Requirement Engineering*. Di sesi keenam, kita membongkar anatomi kebutuhan. Kita membedah perbedaan tegas antara kebutuhan fungsional yang menjelaskan apa yang harus dilakukan sistem, dan kebutuhan non-fungsional yang menentukan standar kualitas performa, keandalan, sampai keamanan. Kita juga belajar membedakan bahasa kebutuhan tingkat pengguna dengan spesifikasi tingkat sistem yang siap diterjemahkan pengembang.

Rangkaian paruh pertama ini kemudian dikunci secara presisi di sesi ketujuh lewat pendalaman proses rekayasa kebutuhan itu sendiri. Kita belajar seni *elicitation* dan *analysis*: bagaimana menggali kebutuhan yang sesungguhnya dari manusia, bukan cuma mencatat daftar keinginan di permukaan. Kita membedah empat masalah klasik penggalian kebutuhan, memilih teknik wawancara atau observasi yang tepat, menyaring ambiguitas, hingga melihat bagaimana kebutuhan dikelola secara dinamis di dalam *backlog* Agile.

Kalau dirangkai, alurnya sangat rapi. Kita mulai dari kesadaran etika, menyusun prosesnya, memilih model kendaraannya, mendalami eksekusi tangkas dan otomatisasinya, lalu kembali ke akar segala masalah: memahami apa yang sebenarnya manusia butuhkan dari sistem tersebut.

---

## Saat Kacamata Teori Mengubah Cara Melihat Lantai 28

Sari, lo ingat nggak waktu proyek aplikasi portal klien kita di lantai 28 tempo hari mulai goyah? Waktu itu Vina dengan gaya khas *head of sales* yang sangat percaya diri sempat bilang di depan klien kalau tim kami tinggal bikin *mobile app* terintegrasi biar klien senang. Waktu itu respons pertama tim adalah langsung mikir arsitektur server, milih vendor, dan mendesain antarmuka yang kelihatan keren di slide presentasi.

Sebelum belajar paruh semester ini, cara pandang gue pasti sama naifnya. Kalau sistem akhirnya mandek atau ditolak pengguna, gue bakal refleks menyalahkan tim teknis yang dianggap lambat, atau menyalahkan klien yang plin-plan dan nggak tahu maunya apa.

Tapi sekarang, kacamata gue berubah total. 

Gue teringat momen waktu ngobrol langsung sama Mas Danu, agen senior tim sewa di sisi klien yang kesehariannya bolak-balik mendampingi calon penyewa di lobi gedung. Di saat para petinggi rapat menuntut aplikasi canggih dengan belasan menu, Mas Danu cuma butuh dua angka tarif bersih dalam waktu sepuluh detik lewat ponselnya saat berdiri di samping lift. Dia bahkan diam-diam bikin catatan di Excel pribadi karena formulir sistem baru yang dibangun terlalu bertele-tele dan minta empat belas kolom wajib isi. Di sisi lain, Bu Retno dari bagian keuangan punya aturan perhitungan pajak sewa yang ketat dan sama sekali belum diakomodasi di sistem itu karena dia nggak pernah diajak bicara sejak awal.

Melihat adegan itu, gue langsung teringat materi kita di sesi enam dan tujuh. Masalah kantor kami tempo hari sama sekali bukan masalah teknis pemrograman. Kodenya mungkin bersih, *framework*-nya mungkin mutakhir. Tapi sistem itu gagal karena kami melompat ke solusi sebelum memahami masalah. Kami mencampuradukkan kebutuhan fungsional dengan keinginan di permukaan (*wants* vs *needs*), mengabaikan kebutuhan non-fungsional soal kecepatan akses di lapangan, dan salah memilih narasumber saat penggalian kebutuhan. Kami mendengarkan manajer yang ingin laporan visual, tapi menulikan telinga dari Mas Danu yang menjadi ujung tombak operasional.

Lebih dari itu, kegagalan koordinasi antara janji manis penjualan dan kenyataan pengiriman mengingatkan gue pada materi etika profesional dan integrasi Scrum-DevOps di sesi satu dan lima. Menjanjikan fitur tanpa proses rekayasa yang matang bukan cuma bikin proyek rugi, tapi melanggar etika profesionalisme terhadap klien dan membakar habis energi tim di belakang layar.

Sekarang, setiap kali gue duduk di ruang rapat lantai 28 atau meninjau draf kerjaan, gue nggak lagi gampang terpesona sama istilah teknis yang muluk-muluk. Pertanyaan pertama gue selalu kembali ke fondasi: proses apa yang sedang kita jalankan, apakah model pengembangannya cocok dengan risiko yang ada, dan apakah kita benar-benar sedang menyelesaikan masalah manusia yang nyata.

---

## Ruang Uji Cara Berpikir Kita

Nah, mumpung besok-besok kita bakal diuji pemahamannya secara menyeluruh, gue nggak mau kita cuma ngafal definisi atau daftar istilah. Coba lo bedah tiga situasi reflektif ini pakai seluruh peta konsep yang sudah kita lalui:

1. Bayangkan ada sebuah startup teknologi di bidang kesehatan yang sedang membangun sistem rekam medis darurat untuk ambulans. Timnya bersikeras menggunakan pendekatan Agile murni dengan rilis fitur dua mingguan tanpa banyak dokumentasi awal, dengan alasan regulasi dan kebutuhan rumah sakit masih sering berubah. Berdasarkan pemahaman lo soal model proses, manajemen risiko, dan etika profesional perangkat lunak, di mana letak bahaya terbesar dari keputusan tim tersebut, dan bagaimana lo menyarankan kompromi model proses yang paling bertanggung jawab?
2. Sering kali dalam proyek pengadaan sistem korporat, manajemen puncak meminta solusi berupa "kami butuh *dashboard* berbasis kecerdasan buatan" atau "kami butuh aplikasi mobile". Sebagai analis sistem yang memahami siklus *Requirement Engineering*, langkah konkret apa yang akan lo ambil untuk membedah pernyataan solusi tersebut agar tidak terjebak membangun fitur yang salah tanpa menyinggung ego pemangku kepentingan yang memegang anggaran?
3. Di sesi lima kita mempelajari integrasi Scrum dan DevOps, sementara di sesi tujuh kita mendalami bagaimana kebutuhan dikelola di dalam *Product Backlog*. Jika sebuah tim pengembangan merasa sudah menjalankan Scrum secara sempurna namun tetap gagal memberikan nilai bisnis yang nyata ke pengguna setiap akhir Sprint, di titik mana antara rekayasa kebutuhan (*elicitation/analysis*) dan pipa pengiriman (*CI/CD*) kemungkinan besar terjadi sumbatan logika? Bagaimana lo mendiagnosisnya?

Gue mau rapiin tumpukan kertas ini dulu sebelum narik selimut. Masih ada beberapa catatan studi kasus lama yang perlu gue baca ulang sambil ngecek email masuk. 

Selamat menyiapkan amunisi logika, Sari. Sampai ketemu di ruang diskusi berikutnya dengan kepala yang jernih.

Nik