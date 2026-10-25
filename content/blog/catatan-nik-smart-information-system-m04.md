---
title: 'Catatan Nik: Tagihan Siluman Vendor dan Dongeng "Sistem Pakar" yang Hilang Akal'
subtitle: 'Gue lagi nahan emosi liat invoice per user yang mendadak melambung tinggi, padahal engine yang dijual ke kantor cuma susunan IF-THEN kopong tanpa nalar.'
type: blog
date: 2026-10-29T05:00:00+07:00
draft: true
ws_chat: 1616
ws_msg: 21615
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "smart-information-system", "catatan-nik"]
summary: 'Materi pekan ini soal expert system: basis pengetahuan, mesin inferensi, fasilitas penjelasan, sampai forward dan backward chaining. Di kantor gue, vendor lisensi naikin biaya per user diam-diam sambil ngaku sistemnya punya kecerdasan pakar, padahal isinya cuma aturan IF-THEN dangkal.'
hook: 'Pernah nggak lo nemu software korporat berharga miliaran yang pas ditanya kenapa dia ngasih rekomendasi A, dia cuma bisa diem plonga-plongo kayak orang bingung?'
---

Notifikasi tagihan vendor di layar laptop gue tadi siang bener-bener sukses bikin kopi susu di meja hampir tumpah. Bukan cuma karena nominal per *user license* yang tiba-tiba melompat tanpa pemberitahuan resmi di adendum kontrak, tapi karena baris deskripsi layanannya ditulis dengan sangat percaya diri: *Cognitive AI and Expert Valuation Engine Enterprise Tier*. 

Gue langsung manggil Aris ke meja kerja gue lewat panggilan video singkat. Muka analis data junior itu udah keliatan kusut banget dari pagi. Matanya merah, latar belakang kamarnya berantakan, dan di tangannya ada setumpuk berkas komparasi hasil hitungan valuasi gedung perkantoran di kawasan segitiga emas Jakarta. 

"Mbak Nik," suara Aris kedengeran putus asa, "ini sistem beneran nggak masuk akal. Masa ada satu aset ruko tiga lantai di koridor TB Simatupang dinilai drop tiga puluh persen cuma gara-gara variabel lebar jalan gue isi sembilan koma delapan meter, padahal batas standarnya sepuluh meter? Pas gue cari tau logikanya di menu sistem, nggak ada keterangan apa pun. Nggak ada audit *trail*, nggak ada alasan logis."

Gue narik napas panjang. Fenomena klasik SCBD: Vina, *head of sales* kita yang super persuasif itu, beberapa waktu lalu kepincut demo vendor yang presentasinya serba mengkilap. Waktu demo, vendor itu nunjukin *dashboard* interaktif dengan animasi grafik futuristik dan bilang kalau sistem ini berhasil meng-encode intuisi dan penalaran penilai senior ke dalam algoritma pintar. Katanya, kepergian penilai senior kaliber Bram yang dulu sempat bikin kantor limbung nggak bakal kerasa lagi karena "otak" sang pakar sudah dipindahkan ke dalam basis data komputer. Vina langsung setuju buat *rollout* ke tim valuasi komersial.

Tapi kenyataan di lapangan berkata lain. Pas tagihan lisensi per *seat* melonjak gila-gilaan bulan ini, gue sama Aris baru nyadar kalau kita bukan lagi beli sistem pakar modern. Kita cuma lagi diperas buat bayar ribuan baris aturan kaku *hardcoded* yang ditulis amatir, dibungkus antarmuka web yang cantik, dan sama sekali nggak punya kemampuan bernalar layaknya seorang pakar sejati. 

Materi kuliah modul minggu ini di kampus gue kebetulan banget lagi ngebahas tuntas soal *Expert System* atau Sistem Pakar. Dan makin gue dalami materinya, makin keliatan betapa parahnya penipuan label "AI" yang sering dijual vendor-vendor nakal ke manajemen perusahaan.

---

## Membongkar Esensi: Apa Sebenarnya Sistem Pakar Itu?

Di modul minggu ini, dosen di kelas gue ngasih penekanan yang tegas banget: *Expert System* adalah salah satu cabang klasik dari *Artificial Intelligence* yang fokusnya spesifik untuk meniru penalaran seorang pakar manusia dalam domain yang sempit (*narrow domain*). Kata kuncinya ada dua: domain sempit dan penalaran pakar. 

Sistem pakar bukan *Artificial General Intelligence* yang bisa ngobrolin segala hal kayak asisten virtual serba tahu. Sistem pakar juga bukan sekadar kalkulator formula Excel yang cuma ngitung angka mentah pake rumus matematika linier. 

Sistem pakar dirancang buat situasi di mana masalahnya nggak bisa diselesaikan dengan algoritma komputasi biasa, melainkan butuh kombinasi antara fakta terstruktur dan *rules of thumb* alias heuristik. Heuristik ini adalah sari pati dari pengalaman bertahun-tahun seorang ahli: intuisi praktis, tebakan terdidik, cara pintas logis, dan pertimbangan kontekstual yang biasanya cuma ada di kepala orang-orang senior di industri tertentu.

Karakteristik utama dari sebuah sistem pakar yang beneran otentik itu punya batas tegas yang membedakannya dari program komputer konvensional:

Pertama, sistem pakar punya performa tinggi pada domain spesifik. Kalau domainnya valuasi properti komersial, dia harus paham seluk-beluk regulasi tata ruang lokal, koefisien dasar bangunan, tren yield pasar, sampai risiko hukum sertifikasi tanah. Dia nggak dirancang buat paham diagnosis penyakit paru-paru atau cara benerin traktor.

Kedua, responnya cepat dan konsisten. Manusia bisa capek, bisa bias karena lagi bad mood, atau bisa salah hitung karena ngantuk setelah lembur. Sistem pakar nggak kenal capek dan bakal ngeluarin keputusan yang konsisten untuk kondisi input yang identik.

Ketiga, dan ini yang paling sakral tapi diabaikan sama vendor kantor gue: adanya pemisahan yang sangat tegas antara *knowledge base* (basis pengetahuan) dan *inference engine* (mesin inferensi). 

Di program komputer biasa atau skrip buatan vendor abal-abal, pengetahuan bisnis dicampuradukkan langsung di dalam kode program (*hardcoded IF-THEN logic*). Kalau ada aturan pajak baru atau perubahan regulasi tata ruang dari gubernur, *developer* harus bongkar kodingan inti aplikasi baris demi baris. Risikonya luar biasa besar, aplikasinya bisa langsung *crash*. 

Sebaliknya, pada sistem pakar sejati, arsitekturnya dirancang terpisah secara elegan. Mesin berpikirnya berdiri sendiri, sementara basis pengetahuannya disimpan di repositori terpisah yang modular. Jadi, kalau ada penilai senior yang mau nambahin aturan baru atau ngoreksi aturan lama, mereka tinggal memodifikasi basis pengetahuan tanpa perlu nyentuh logika mesin inferensinya sama sekali.

---

## Anatomi Inti: Komponen yang Wajib Ada di Bawah Kap Mesin

Pas gue bedah arsitektur sistem dari modul kuliah gue bareng catatan kerjaan kantor, makin jelas komponen apa aja yang mestinya ada di dalam sebuah sistem pakar yang utuh. Ada lima pilar utama yang saling mengunci:

```
+-------------------+
|   USER INTERFACE  |
+-------------------+
     ^         |
input|         |rekomendasi
     |         v
+----------+  +----------+
|EXPLANATION|<-| WORKING |
| FACILITY  |  | MEMORY  |
+----------+  +----------+
        ^         |
        | fakta   |
        v         v
+-------------------+
|  INFERENCE ENGINE |
| forward/backward  |
+-------------------+
        ^
        | aturan
        v
+-------------------+
|  KNOWLEDGE BASE   |
|   aturan IF-THEN  |
+-------------------+
```

### 1. Basis Pengetahuan (*Knowledge Base*)
Ini adalah jantung dari sistem pakar. Isinya bukan cuma sekadar tabel data mentah kayak database SQL, tapi representasi pengetahuan dalam bentuk fakta dan aturan (*production rules*). Format standarnya biasanya berbentuk pasangan kondisi dan aksi: 

*IF kondisi terpenuhi, THEN lakukan aksi atau tetapkan kesimpulan tertentu.*

Bukan sembarang IF-THEN dangkal, Sar. Aturan di sini mencakup keterkaitan relasional yang kompleks dan sering kali dilengkapi dengan faktor kepastian (*certainty factors*) buat mengakomodasi keraguan dunia nyata. Misalnya: *IF peruntukan lahan komersial AND akses jalan utama kurang dari sepuluh meter AND tidak ada jalur logistik alternatif, THEN tetapkan diskon likuiditas pasar sebesar lima belas persen dengan tingkat keyakinan delapan puluh persen.*

### 2. Memori Kerja (*Working Memory*)
Kadang disebut juga *blackboard*. Ini adalah ruang penyimpanan sementara yang nyatet fakta-fakta spesifik dari kasus yang lagi ditangani saat itu. Waktu Aris masukin data ruko di TB Simatupang tadi, data luas tanah, lebar jalan, zonasi wilayah, dan harga penawaran awal disimpan di memori kerja ini. Memori kerja ini dinamis banget; dia bakal terus diperbarui seiring berjalannya proses penalaran saat mesin inferensi menemukan fakta-fakta baru.

### 3. Mesin Inferensi (*Inference Engine*)
Kalau *knowledge base* itu otaknya, maka *inference engine* adalah proses berpikirnya. Ini adalah komponen perangkat lunak yang bertugas mengevaluasi aturan-aturan di basis pengetahuan dengan mencocokkannya ke fakta yang ada di memori kerja. Mesin inferensi inilah yang menentukan aturan mana yang relevan, menyelesaikan konflik kalau ada beberapa aturan yang bertabrakan (*conflict resolution*), dan mengarahkan alur penalaran sampai kesimpulan akhir tercapai.

### 4. Fasilitas Penjelasan (*Explanation Facility*)
Nah, ini dia biang kerok yang bikin gue naik darah ke vendor tadi siang! Fasilitas penjelasan, atau sering disebut *justifier*, adalah komponen vital yang memungkinkan sistem menjelaskan alur logikanya sendiri ke pengguna. Komponen ini wajib bisa menjawab dua pertanyaan kritis:

* **Pertanyaan "Why":** Kenapa sistem menanyakan informasi tertentu ke pengguna? Pengguna berhak tahu alasan di balik pertanyaan sistem di tengah-tengah sesi penginputan data.
* **Pertanyaan "How":** Bagaimana sistem bisa sampai pada kesimpulan atau angka rekomendasi akhir tersebut? Sistem harus bisa membeberkan rantai penalaran (*reasoning chain*) yang dilewatinya dari fakta awal sampai vonis akhir.

Sistem valuasi kantor yang dibeli Vina sama sekali nggak punya fasilitas penjelasan ini. Pas nilainya drop tiga puluh persen, sistemnya cuma nampilin angka dingin tanpa argumen pendukung. Padahal dalam dunia korporat, klien kita butuh laporan audit yang bisa dipertanggungjawabkan di mata hukum dan perbankan. Lo nggak bisa bilang ke klien, "Ya nilainya segini karena AI-nya bilang begitu." Bisa ditertawakan asosiasi penilai se-Indonesia kita kalau jawab begitu!

### 5. Fasilitas Akuisisi Pengetahuan (*Knowledge Acquisition Facility*)
Ini adalah antarmuka khusus yang dipakai oleh *knowledge engineer* bareng pakar domain buat memperbarui, menambah, atau memvalidasi basis pengetahuan. Mengambil pengetahuan dari kepala seorang ahli (*tacit knowledge*) buat diubah jadi aturan formal (*explicit knowledge*) itu salah satu pekerjaan paling rumit di dunia sistem informasi. Proses ini dikenal sebagai *knowledge engineering*, dan alat bantu akuisisi inilah yang memfasilitasi proses transfer tersebut supaya nggak terjadi kontradiksi logika di dalam sistem.

---

## Mesin Penalaran: Duel Forward Chaining vs Backward Chaining

Bagian paling seru di materi kuliah minggu ini adalah waktu ngebahas cara kerja mesin inferensi dalam menelusuri aturan. Ada dua strategi utama yang punya karakteristik berlawanan: *Forward Chaining* dan *Backward Chaining*. Memahami dua pendekatan ini bikin mata gue terbuka lebar soal kenapa sistem kantor kita saat ini berantakan parah.

```
FORWARD CHAINING (data-driven):
fakta -> cocokkan aturan -> kesimpulan

BACKWARD CHAINING (goal-driven):
hipotesis -> cari bukti -> validasi fakta
```

### Forward Chaining (*Data-Driven / Bottom-Up*)
Strategi ini bergerak maju, dimulai dari fakta-fakta yang diketahui menuju kesimpulan akhir. 

Alurnya sederhana: sistem ngumpulin semua fakta awal dari pengguna atau sensor, lalu mesin inferensi memeriksa basis pengetahuan buat nyari aturan mana yang klausul *IF*-nya cocok sama fakta tersebut. Kalau ada aturan yang cocok, aturan itu "ditembakkan" (*fired*), dan bagian *THEN*-nya menghasilkan fakta baru yang langsung dimasukkan ke memori kerja. Proses ini berulang terus menerus secara iteratif sampai nggak ada lagi aturan baru yang bisa ditembakkan atau sampai kondisi akhir tercapai.

*Forward chaining* sangat cocok buat situasi di mana:
* Fakta awalnya sangat banyak dan mudah didapatkan sejak awal.
* Tujuannya bersifat terbuka atau jumlah kemungkinan kesimpulannya sangat banyak.
* Masalahnya berkaitan dengan tugas *monitoring*, *forecasting*, perencanaan, atau kontrol proses industri.

Misalnya di dunia properti: Sistem menerima ratusan data pasar harian, indikator inflasi, suku bunga BI, pergerakan indeks harga konsumen, dan data volume transaksi properti di Jabodetabek. Dari ribuan fakta ini, sistem secara maju menyimpulkan kondisi makro: *pasar properti komersial kuartal depan diprediksi mengalami oversupply di sub-sektor ruang kantor grade B*.

### Backward Chaining (*Goal-Driven / Top-Down*)
Strategi ini bergerak mundur, dimulai dari hipotesis atau tujuan yang ingin dibuktikan, lalu bekerja ke belakang mencari fakta-fakta yang mendukung hipotesis tersebut.

Mesin inferensi bakal milih satu tujuan dulu (misalnya: *Apakah aset ini layak dijadikan jaminan kredit dengan plafon sepuluh miliar rupiah?*). Dari tujuan ini, sistem bakal nyari aturan di basis pengetahuan yang klausul *THEN*-nya menyatakan kesimpulan tersebut. Begitu ketemu, sistem bakal ngeliat klausul *IF* dari aturan itu: kondisi apa yang harus dipenuhi? Kondisi-kondisi itu sekarang jadi sub-tujuan baru (*sub-goals*). Sistem bakal terus mundur ke belakang, menelusuri sub-tujuan sampai dia menemukan fakta di memori kerja yang membenarkannya, atau sistem bakal nanya langsung ke pengguna buat memastikan fakta tersebut.

*Backward chaining* sangat ideal untuk:
* Masalah diagnosis, *troubleshooting*, atau audit kepatuhan.
* Situasi di mana data yang relevan harus dicari secara selektif, bukan dikumpulkan semuanya di muka.
* Kasus di mana pengguna sudah punya dugaan awal atau pilihan hipotesis yang jumlahnya terbatas.

Kelemahan sistem kantor kita yang dibeli Vina adalah si vendor mencoba memaksakan logika *forward chaining* kaku pada masalah valuasi yang hakikatnya butuh pembuktian *backward chaining*. Penilai manusia yang berpengalaman biasanya berangkat dari hipotesis kelayakan nilai pasar wajar berdasarkan properti komparabel terdekat, lalu bekerja mundur memverifikasi atribut fisik, legalitas sertifikat, dan kepatuhan zonasi untuk menguji hipotesis nilai tersebut. Karena vendor mencampuradukkan kedua logika ini tanpa mesin inferensi yang benar, hasilnya jadi acak-acakan.

---

## Jebakan Maut: Hambatan Akuisisi dan Kerapuhan Sistem Pakar

Waktu sesi diskusi di kelas gue, ada satu konsep yang bikin gue langsung teringat momen waktu Bram masih duduk di kantor SCBD sebelum dia resign dan bawa gerbong kliennya: *the knowledge acquisition bottleneck*.

Mengekstraksi pengetahuan dari kepala seorang pakar manusia itu susahnya minta ampun. Pakar penilai kayak Bram selama belasan tahun menilai gedung tinggi nggak cuma ngandelin buku teks. Mereka punya *tacit knowledge*, yaitu pemahaman bawah sadar yang nggak gampang diartikulasikan dalam bentuk kata-kata, apalagi ke dalam aturan *IF-THEN* biner. 

Waktu Bram ngecek sebuah gedung, dia bisa ngerasain hal-hal non-teknis: integritas pengembangnya, suasana politik lokal perizinan, sampai bau lembap di *basement* yang nandain ada masalah drainase kronis yang bakal bikin biaya operasional membengkak lima tahun lagi. Coba lo bayangin, gimana caranya seorang *knowledge engineer* muda yang cuma lulusan ilmu komputer bisa mengonversi "firasat profesional" kayak gitu ke dalam aturan sistem pakar tanpa distorsi? 

Di situlah letak kebuntuan (*bottleneck*) terbesarnya. Sering kali apa yang dikatakan pakar saat diwawancarai berbeda dengan apa yang sebenarnya dia lakukan di lapangan. Dan kalau transfer pengetahuannya cacat, aturan yang tertanam di sistem pakar bakal jadi dangkal dan menyesatkan.

Masalah kedua dari sistem pakar adalah kerapuhan (*brittleness*). 

Sistem pakar itu luar biasa tajam dan presisi selama masalah yang dihadapi berada persis di dalam batas sempit basis pengetahuannya. Tapi begitu ada kasus yang melenceng sedikit saja dari batas domain tersebut, performanya langsung anjlok bebas ke titik nol. Dia nggak punya *common sense*. 

Manusia punya akal sehat. Kalau seorang penilai manusia nemu jalan raya lebarnya sembilan koma delapan meter alih-alih sepuluh meter, akal sehatnya bakal ngomong: "Dua puluh sentimeter ini nggak signifikan karena trotoarnya lebar dan truk kontainer tetep bisa papasan dengan leluasa." Tapi sistem pakar yang rapuh bakal langsung memotong valuasi secara brutal karena aturan *IF lebar < 10 THEN diskon 30%* tereksekusi tanpa kompromi akal sehat. 

Ini yang bikin gue geregetan banget sama klaim vendor kantor kita. Mereka menjual sistem yang kaku dan rapuh ini dengan label "AI Revolusioner". Padahal sistem pakar generasi simbolik (*Symbolic AI*) punya batas toleransi yang sangat jelas dan nggak boleh dipasarkan sebagai entitas yang serba bisa beradaptasi sendiri layaknya model pembelajaran mesin probabilistik modern.

---

## Bentang Implementasi: Dari Diagnosis Medis Hingga Pertanian Presisi

Biar catatan gue ini nggak melulu isinya keluhan soal drama tagihan SCBD, gue mau rekap beberapa studi kasus penerapan sistem pakar di berbagai bidang yang dibahas di modul kuliah gue. Menarik banget ngeliat gimana teknologi ini sebenarnya sangat berdaya guna kalau diterapkan pada tempat yang tepat dengan arsitektur yang jujur.

### 1. Sektor Kesehatan: Jejak Legendaris MYCIN dan Diagnosis Klinis
Sejarah sistem pakar nggak bisa lepas dari MYCIN, sistem yang dikembangkan di Stanford University pada era 1970-an untuk mendiagnosis infeksi bakteri darah dan merekomendasikan dosis antibiotik yang sesuai. 

Meskipun saat itu belum pernah dipakai secara resmi di praktik klinis karena masalah pertanggungjawaban hukum dan etika, MYCIN membuktikan bahwa sistem berbasis aturan bisa menandingi akurasi dokter spesialis dalam domain penyakit menular tertentu. Yang paling brilian dari MYCIN adalah pengenalan konsep *Certainty Factors* (faktor kepastian) buat menangani ketidakpastian bukti medis, serta fasilitas penjelasannya yang transparan. 

Dokter nggak bakal mau nurut sama anjuran komputer kalau komputernya nggak bisa jelasin rantai logika medis di balik resep obat keras yang disarankan. Di dunia medis modern, turunan sistem pakar klinis (*Clinical Decision Support Systems*) masih dipakai aktif untuk menyaring interaksi obat berbahaya dan memandu triase gawat darurat.

### 2. Sektor Keuangan: *Underwriting* dan Persetujuan Kredit Otomatis
Di industri perbankan dan asuransi, sistem pakar adalah tulang punggung dari otomasi penilaian risiko. Saat seseorang mengajukan pinjaman pemilikan rumah atau fasilitas kredit korporasi, sistem pakar mengevaluasi kelayakan calon debitur menggunakan aturan-aturan ketat regulasi perbankan yang dipadukan dengan heuristik analis kredit senior.

Sistem ini bisa memeriksa riwayat kredit, rasio utang terhadap pendapatan, stabilitas industri tempat pemohon bekerja, dan nilai agunan. Penggunaan *backward chaining* di sini sangat populer: tujuannya adalah membuktikan apakah pemohon masuk dalam kategori *low-risk*, *medium-risk*, atau *high-risk*. Fasilitas penjelasannya pun sangat krusial di ranah ini karena aturan perbankan di banyak negara mewajibkan lembaga keuangan memberikan alasan eksplisit jika sebuah pengajuan kredit ditolak (*adverse action notice*).

### 3. Sektor Manufaktur dan Industri Berat: *Fault Diagnosis* Mesin Kompleks
Di pabrik manufaktur semen, pembangkit listrik tenaga uap, atau pemeliharaan armada pesawat terbang, *downtime* mesin bisa menelan kerugian miliaran rupiah per jam. Sistem pakar dipakai untuk mendeteksi sumber kerusakan (*troubleshooting*) mesin-mesin raksasa ini berdasarkan pola suara sensor getaran, fluktuasi temperatur pelumas, dan tekanan oli hidrolik.

Teknisi lapangan yang masih junior bisa berinteraksi dengan sistem pakar lewat komputer portabel. Sistem bakal memandu teknisi langkah demi langkah: *Cek komponen katup tekanan nomor empat. Apakah ada kebocoran cairan?* Jika teknisi menjawab "Ya", sistem langsung melompat ke aturan penanganan kontinjensi untuk mencegah ledakan kompresor. Di sini, sistem pakar bertindak sebagai mentor ahli virtual yang mendampingi pekerja operasional di garis depan.

### 4. Sektor Pertanian Presisi: Deteksi Penyakit Tanaman dan Manajemen Hara
Siapa bilang sistem pakar cuma main di gedung ber-AC dan pabrik baja? Di sektor agrikultur, sistem pakar membantu petani mendiagnosis serangan hama tanaman pangan seperti padi, jagung, atau kelapa sawit.

Petani atau petugas penyuluh lapangan memasukkan gejala visual yang tampak pada daun, batang, atau akar tanaman (misalnya: bercak cokelat melingkar di pelepah daun dengan tepian kuning). Sistem kemudian mencocokkan gejala tersebut dengan basis pengetahuan patologi tanaman untuk mengidentifikasi jenis jamur patogen yang menyerang dan merekomendasikan takaran fungisida yang tepat berdasarkan fase pertumbuhan tanaman dan tingkat kelembapan udara. Sistem pakar pertanian bahkan mengintegrasikan data kondisi tanah buat merekomendasikan formulasi pupuk presisi, membantu petani menghemat biaya input kimiawi secara signifikan.

---

## Rekapitulasi: Sistem Pakar vs Machine Learning

Biar gambaran di kepala kita berdua makin jernih buat bahan ujian tengah semester nanti, gue bikin tabel ringkasan perbandingan antara Sistem Pakar (*Symbolic AI*) dan Pembelajaran Mesin (*Machine Learning / Statistical AI*). Kadang orang bisnis di SCBD suka menyamaratakan dua hal ini seolah-olah barang yang sama, padahal filosofi dasarnya beda kutub.

| Dimensi Perbandingan | Sistem Pakar (*Expert System*) | Pembelajaran Mesin (*Machine Learning*) |
| :--- | :--- | :--- |
| **Sumber Pengetahuan Utama** | Pakar manusia (*Human Experts*) melalui wawancara dan *knowledge engineering*. | Data historis mentah dalam jumlah besar (*Big Data*). |
| **Bentuk Representasi** | Aturan simbolik eksplisit (*IF-THEN rules*), logika formal, semantik. | Bobot numerik, matriks probabilitas, vektor matematis. |
| **Transparansi Penalaran (*Explainability*)** | Sangat tinggi; punya fasilitas penjelasan (*Why & How*) yang transparan dan dapat diaudit. | Cenderung rendah (*Black Box*), terutama pada algoritma *Deep Learning*. |
| **Toleransi Data Baru di Luar Domain** | Sangat rapuh (*Brittle*); langsung gagal jika fakta berada di luar aturan basis pengetahuan. | Relatif adaptif; mampu melakukan interpolasi dan menemukan pola tersembunyi selama distribusinya mirip. |
| **Biaya & Tantangan Pemeliharaan** | *Knowledge acquisition bottleneck*; sulit memperbarui aturan secara massal tanpa konflik logika. | Ketergantungan tinggi pada kualitas dan kebersihan data (*Garbage in, garbage out*). |
| **Paling Optimal Digunakan Untuk** | Domain dengan regulasi ketat, aturan deterministik, dan butuh akuntabilitas audit hukum. | Pengenalan pola kompleks, prediksi citra/suara, estimasi probabilitas tren dinamis. |

Melihat tabel ini, gue makin yakin kalau langkah vendor kantor kita yang mematok harga selangit sambil menyamarkan sistem *rule-based* dangkal sebagai mesin kognitif modern adalah tindakan yang nggak etis secara bisnis teknologi informasi. Sistem mereka nggak punya transparansi sistem pakar sejati, tapi juga nggak punya fleksibilitas statistik dari *machine learning*. Jadinya cuma produk nanggung yang bikin tim operasional kita makan hati.

---

## Refleksi dan Pertanyaan Buat Diskusi Kita

Gue tadi sore sempet debat kecil sama Vina di ruang rapat lantai empat kantor kita di SCBD sebelum gue balik ke Bogor. Vina masih keukeuh membela vendor itu dengan dalih: "Tapi Nik, sistem ini udah memangkas waktu kerja tim valuasi sampai empat puluh persen di fase penginputan awal!"

Gue cuma bisa membalas tenang: "Iya Vin, memangkas waktu input empat puluh persen, tapi kita ngabisin waktu tiga ratus persen lebih banyak buat benerin anomali angka yang nggak bisa dijelasin asal-usulnya pas klien kita nanya rincian metodologinya." Vina langsung diem, nggak bisa bantah lagi.

Nah Sar, berhubung lo orangnya paling kritis soal arsitektur sistem dan tata kelola teknologi informasi, gue mau ngelempar tiga pertanyaan reflektif ini buat ngelatih ketajaman analisa lo:

1. Di tengah gempuran tren *Deep Learning* dan *Generative AI* yang serba probabilistik dan sering dijuluki *black box*, menurut analisis lo, apakah pendekatan *Expert System* simbolik berbasis aturan (*rule-based*) ini masih punya relevansi strategis untuk dipertahankan di arsitektur sistem informasi enterprise modern? Di sektor mana sistem pakar murni secara mutlak tetap tak tergantikan oleh *machine learning*, dan apa argumen fundamentalnya?
2. Kalau lo diposisikan sebagai *Chief Information Officer* (CIO) di kantor gue yang lagi menghadapi dilema ini, gimana langkah sistematis lo mengaudit dan memitigasi risiko dari software vendor yang nggak transparan kayak kasus di atas? Kriteria evaluasi apa yang wajib dimasukkan ke dalam SLA (*Service Level Agreement*) dan dokumen pengadaan perangkat lunak kecerdasan buatan supaya manajemen nggak tertipu ilusi "AI" yang aslinya cuma skrip aturan dangkal?
3. Salah satu kelemahan terbesar sistem pakar adalah *knowledge acquisition bottleneck* dan kerapuhan (*brittleness*). Mungkinkah kedua kelemahan inheren ini diatasi dengan membangun arsitektur sistem hibrida (*Hybrid Intelligent System*) yang mengawinkan ketajaman inferensi simbolik sistem pakar dengan daya adaptasi pengenalan pola *machine learning*? Bisakah lo uraikan skenario arsitektur logisnya untuk kasus valuasi aset properti komersial yang kompleks?

Layar monitor gue udah mulai redup karena fitur penghemat daya otomatis nyala. Dylan barusan ngabarin lewat pesan teks dari Magelang kalau dia baru selesai apel malam dan mau siap-siap tidur di asrama. Kamar kerja gue mulai terasa gerah karena pendingin ruangan kayaknya butuh diservis minggu ini. 

Gue mau rehat dulu sebelum besok pagi harus berhadapan lagi sama draft negosiasi ulang kontrak lisensi vendor itu bareng tim legal kantor. 

Tetap waras di tengah tumpukan tugas kuliah dan drama korporat ya, Sar.

Nik
