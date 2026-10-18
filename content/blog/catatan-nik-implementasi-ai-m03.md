---
title: "Catatan Nik: Ketika Sales Jual Dongeng AI dan Realitas Machine Learning Menampar SCBD"
subtitle: "Gue kira bagian tersulit dari bikin model itu ngoding. Ternyata yang bikin pusing justru milih metrik yang nggak bisa dibohongin orang bisnis."
type: "blog"
date: "2026-10-20T05:00:00+07:00"
draft: true
ws_chat: "1602"
ws_msg: 21536
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "implementasi-artificial-intelligence", "catatan-nik"]
summary: "Materi pekan ini soal machine learning: Big Data 5V, data mining, tiga tipe belajar mesin, sampai metrik evaluasi. Di kantor gue, tim sales udah nawarin fitur prediksi ke klien sebelum tim data sempat bangun apa pun."
hook: "\"Bisa demo dashboard-nya minggu depan?\" Klien nanya gitu di ujung presentasi, dan satu-satunya orang di ruangan yang tahu model itu belum ada sama sekali cuma gue."
---

Layar proyektor di *meeting room* lantai 28 masih nampilin slide nomor 14 pas kepala gue mendadak berdenyut kencang. Di slide itu, terpampang diagram lingkaran warna neon dengan tulisan mentereng: *"Next-Gen AI Predictive Valuation Engine: Real-Time Commercial Forecasting"*. 

Klien kami, salah satu grup konglomerat pengembang terbesar di Jakarta, langsung pasang tampang antusias. Salah satu direktur mereka condongin badan ke depan, natap tim *commercial leasing* kantor gue, lalu nanya hal paling fatal yang bikin lidah gue kelu: *"Menarik banget ini. Jadi algoritma prediksinya udah ditraining pakai data transaksi sewa riil kuartal lalu, ya? Bisa demo dashboard-nya minggu depan?"*

Gue ngelirik ke arah Vina, *head of sales* yang dari tadi presentasi dengan gaya menggebu-gebu khas anak *business development* SCBD. Vina cuma senyum tenang, ngangguk mantap, dan ngejawab dengan santainya, *"Tentu, Pak. Engine machine learning kami sudah fully automated dan tinggal integrasi API saja ke data internal Bapak."*

Dada gue rasanya mau rontok, Sar. Di balik meja, tangan gue langsung buka Slack dan ngetik panik ke kanal internal anak tim data. Respons lead data engineer kami cuma satu: emoji tengkorak, disusul kalimat singkat berhuruf kapital: *"ENGINE APAAN ANJIR? KITA BARU BIKIN REKAP CSV MANUAL MINGGU LALU."*

Drama klasik D2 akhirnya meledak di depan muka gue: tim sales ngejual fitur futuristik yang bahkan satu baris kodenya pun belum pernah ditulis. Mereka pikir *machine learning* itu semacam fitur *magic button* di Canva atau saklar lampu yang tinggal lo cetek langsung nyala. Padahal, materi modul *Introduction to AI* pertemuan ketiga kampus gue minggu ini ngebahas tuntas realitas di balik dongeng AI: komputer itu nggak punya kesaktian magis. Komputer cuma belajar dari data, dan proses bikin dia bisa belajar itu jalannya panjang, berdarah-darah, dan butuh fondasi ilmiah yang solid.

---

## Arthur Samuel, Dongeng Komputer Pintar, dan Realitas "Data is the New Oil"

Sebelum sales kantor gue jualan mimpi lebih jauh, mari kita tarik rem darurat dan bedah konsep dasarnya dulu. Modul kita buka sesi ini dengan mengutip Arthur Samuel dari era 1959. Beliau mendefinisikan *machine learning* sebagai bidang studi yang ngasih komputer kemampuan buat belajar tanpa harus diprogram secara eksplisit (*explicitly programmed*).

Bedanya apa sama pemrograman tradisional, Sar? Lo pasti udah hafal luar kepala, tapi anak sales kantor gue jelas nggak paham. 

Di *traditional programming*, manusia ngasih dua hal ke komputer: data dan aturan (*rules* atau logika *if-else*). Komputer cuma mesin hitung patuh yang ngejalanin aturan itu buat ngeluarin *output*. Misalnya: *IF luas bangunan > 500m² AND lokasi == SCBD THEN harga_sewa = tinggi*. Kaku banget, kan? Begitu dinamika pasar berubah, aturan lo langsung basi.

Nah, *machine learning* ngebalik paradigma itu 180 derajat. Kita nggak ngasih aturan ke mesin. Kita ngasih komputer data mentah dan *jawaban* (hasil transaksi historis masa lalu), lalu ngebiarin si algoritma nyari sendiri pola, korelasi, dan rumusan matematisnya. Hasil dari proses belajar itu disebut **model**. Model inilah yang nantinya dikasih data baru buat ngelakuin prediksi.

Makanya sering muncul adagium populer: *"Data is the new oil, AI is the new electricity"*. 

Data itu minyak mentah. Kalau cuma lo simpen di tangki atau lo timbun di *folder* Google Drive tanpa diolah, dia nggak ada gunanya sama sekali, bahkan bisa bikin polusi dan menuh-menuhin *storage*. Supaya minyak mentah itu bisa jadi bensin beroktan tinggi yang ngegerakkin mesin AI, lo butuh proses yang namanya **Data Mining**. Lo harus ngegali, ngebersihin, ngekstraksi pola-pola tersembunyi (*hidden patterns*), dan memvalidasi informasi berharga dari tumpukan data raksasa itu.

Masalahnya, minyak mentah di kantor konsultan properti kayak tempat gue kerja bentuknya bukan sumur minyak yang rapi, melainkan tumpukan lumpur hisap bernama *Big Data*.

---

## Jeratan 5V: Kenapa Bikin Model Prediksi Properti Nggak Segampang Mulut Sales

Tim sales kantor gue mikir, modal arsip transaksi properti kantor sejak era Bram masih mimpin divisi valuasi dulu udah cukup buat langsung disulap jadi AI. Mereka nggak paham kalau tumpukan data transaksi puluhan tahun itu kena hantaman badai **5V** yang jadi karakteristik utama *Big Data*:

1. **Volume (Ukuran Data)**  
Data transaksi gedung, catatan sewa, biaya *maintenance*, sampai lalu lintas logistik penyewa selama bertahun-tahun itu ukurannya masif. Buat melatih model prediktif yang handal, lo butuh ribuan hingga jutaan baris data representatif, bukan cuma 50 lembar laporan tahunan yang dirangkum rapi.

2. **Velocity (Kecepatan Perubahan Data)**  
Harga properti di Jakarta itu dinamis banget. Perubahan suku bunga BI, regulasi tata ruang baru, atau pembukaan stasiun LRT baru langsung ngubah nilai kapitalisasi suatu kawasan dalam hitungan minggu. Kalau data lo statis, model lo bakal memprediksi masa depan pakai kacamata masa lalu yang udah usang.

3. **Variety (Keragaman Format Data)**  
Ini mimpi buruk anak data di kantor gue. Datanya nggak cuma angka di tabel SQL. Ada denah arsitektur dalam format CAD, scan sertifikat tanah berformat PDF buram, catatan notulen *meeting* negosiasi dalam format Word, sampai chat WhatsApp antara broker dan pemilik gedung. Gimana caranya algoritma matematika mencerna data yang variasinya seberantakan itu tanpa tahap ekstraksi yang matang?

4. **Veracity (Tingkat Kepercayaan & Kebersihan Data)**  
Data properti lokal itu rawan *noise* dan inkonsistensi. Ada nilai transaksi yang sengaja dikecilin di atas kertas demi urusan pajak, ada kolom luas tanah yang satuannya campur aduk antara meter persegi dan hektar, bahkan ada *human error* salah ketik nol. Kalau data kotor ini lo lolosin, model ML lo bakal menganut prinsip abadi komputer: *Garbage In, Garbage Out*.

5. **Value (Nilai Bisnis Riil)**  
Ini yang paling sering dilupakan orang bisnis. Buat apa lo keluar biaya ratusan juta buat sewa server GPU dan nyewa data scientist kalau hasil prediksinya cuma ngasih tahu hal yang udah jelas diketahui manusia biasa, kayak: *"Gedung di Sudirman lebih mahal dibanding gedung di pinggiran luar tol"*. Nilai bisnis baru muncul kalau model itu bisa nemuin anomali pasar atau peluang arbitrase sewa yang luput dari mata manusia.

Tanpa strategi *data mining* yang jelas buat ngejinakin 5V ini, janji Vina ke klien soal *engine* prediksi otomatis tadi bener-bener cuma omong kosong marketing.

---

## Tiga Mazhab Belajar Mesin: Lo Mau Mesin Lo Didikte, Dilepas, atau Dilatih Mandiri?

Biar Sari makin gampang ngebayangin fondasi teori modul 3 ini buat kerangka GPBSales lo, gue bedah tiga tipe utama *machine learning* yang kita pelajari di kampus:

```
                    ┌───────────────────────────────┐
                    │       MACHINE LEARNING        │
                    └───────────────┬───────────────┘
            ┌───────────────────────┼───────────────────────┐
            ▼                       ▼                       ▼
   [ SUPERVISED ]           [ UNSUPERVISED ]       [ REINFORCEMENT ]
   Data Berlabel            Tanpa Label            Agent vs Environment
   • Prediksi Harga (Reg)   • Segmentasi Gedung    • Dynamic Pricing
   • Klasifikasi Tenant       (Clustering)         • Reward / Penalty
```

### 1. Supervised Learning (Belajar Terbimbing)
Ini tipe yang paling banyak dipakai di dunia korporat dan paling relevan buat kasus prediksi valuasi kantor gue (serta tesis lo). Di sini, mesin dikasih data latih yang udah punya **label** (*ground truth*). Komputer dikasih soal ujian sekaligus kunci jawabannya, biar dia belajar ngenalin polanya.

*Supervised learning* kebagi jadi dua cabang besar:
*   **Regresi (*Regression*):** Kalau output yang mau ditebak berupa angka kontinu. Contohnya: memprediksi harga sewa per meter persegi di kawasan Mega Kuningan berdasarkan luas lantai, umur gedung, jarak ke stasiun MRT, dan rasio parkir.
*   **Klasifikasi (*Classification*):** Kalau output yang mau ditebak berupa kategori atau kelas diskrit. Contohnya: memprediksi apakah calon tenant bakal *default* (gagal bayar) atau lancar, atau memprediksi apakah klien bakal memperpanjang kontrak sewa (*renew vs churn*).

### 2. Unsupervised Learning (Belajar Mandiri Tanpa Label)
Di sini, kita ngasih tumpukan data mentah ke komputer **tanpa ngasih label atau kunci jawaban**. Mesin dibiarin nyari sendiri struktur, pola kesamaan, atau anomali yang ada di dalam data.

Teknik paling populernya adalah **Clustering**. Misalnya, tim riset kantor gue mau ngelompokkin 500 gedung perkantoran di Jabodetabek ke dalam beberapa klaster profil penyewa tanpa mendikte kriterianya. Algoritma bakal nemuin sendiri bahwa ada klaster gedung yang karakternya disukai oleh startup teknologi, ada klaster yang cuma diisi firma hukum dan perbankan, dan ada klaster gedung tua yang penyewanya sensitif banget sama harga service charge.

### 3. Reinforcement Learning (Belajar Lewat Interaksi & Konsekuensi)
Ini mazhab yang paling canggih sekaligus paling kompleks. Nggak ada data historis statis kayak dua tipe di atas. Di sini ada konsep **Agent** yang beroperasi di dalam suatu **Environment**. Si *agent* bakal ngambil tindakan (*action*), lalu *environment* bakal ngasih respon berupa **Reward** (kalau tindakannya bener/menguntungkan) atau **Penalty** (kalau tindakannya salah/merugikan). Tujuannya: si *agent* harus belajar memaksimalkan total *reward* dalam jangka panjang lewat *trial and error*.

Penerapannya di dunia nyata sering dipakai buat navigasi robot, mobil otonom, atau main catur/Go. Di dunia bisnis properti, ini bisa dipakai buat *dynamic pricing algorithm* kamar hotel atau *serviced apartment*, di mana sistem otomatis naikin atau turunin tarif tiap jam berdasarkan fluktuasi *demand*, cuaca, dan tingkat pembatalan demi dapet pendapatan maksimal.

---

## Anatomi ML Pipeline: Kenapa Scikit-Learn Bukan Tongkat Sihir

Pas Vina dengan entengnya bilang *"tinggal integrasi API"*, gue pengen banget nge-print diagram *machine learning pipeline* ukuran poster A0 terus gue tempel di jidatnya. Membangun model machine learning yang siap pakai di lingkungan produksi (*deployment*) itu butuh disiplin rekayasa sistem yang ketat. 

Di kelas, dosen gue ngebedah alur kerja standar yang didukung oleh ekosistem Python dan pustaka andalannya, seperti Scikit-learn:

```
[1. Data Collection & Preprocessing]
   ├── Handling Missing Values & Outliers
   ├── Feature Engineering & Scaling
   └── Train-Test Split (e.g., 80:20)
                 │
                 ▼
[2. Model Training (Python & Scikit-learn)]
   ├── Pilih Algoritma (Linear Regression, Random Forest, etc.)
   └── Model Fit (Belajar dari data latih)
                 │
                 ▼
[3. Evaluation & Optimization]
   ├── Evaluasi Metrik (RMSE, Accuracy, Precision, Recall, F1)
   └── Hyperparameter Tuning (Cegah Overfitting)
                 │
                 ▼
[4. Model Deployment & Monitoring]
   └── API Endpoint / Integrasi ke Sistem Operasional
```

Tahap pertama, **Pengumpulan dan Pra-pemrosesan Data (*Data Preprocessing*)**, adalah lubang hitam yang biasanya ngabisin 70 sampai 80 persen total waktu proyek. Data mentah dari divisi properti itu berantakan luar biasa. Lo harus ngebuang data duplikat, nambal nilai yang hilang (*missing values* pake imputasi *mean* atau *median*), ngebuang pencilan (*outliers*) yang nggak masuk akal, ngelakuin *scaling* biar skala harga miliaran nggak ngebanting skala jumlah toilet yang cuma satuan, sampai ngubah data teks/kategori jadi angka biner (*one-hot encoding*).

Setelah datanya bersih, baru lo belah jadi data latih (*training set*) dan data uji (*testing set*), biasanya pakai rasio 80:20. Lo nggak boleh ngebiarin model ngeliat data uji selama proses latihan! Itu namanya kecurangan akademis, sama aja kayak ngasih bocoran soal ujian sebelum tes dimulai.

Tahap kedua adalah **Pemodelan (*Modeling*)**. Di sinilah Python dan Scikit-learn unjuk gigi. Lo manggil pustaka algoritma, masukin data latih, lalu biarin komputer ngelakuin proses optimasi matematika (*fitting the model*). Tapi kerjaan belum selesai di sini. Lo nggak bisa langsung bangga cuma gara-gara baris kode lo jalan tanpa *error*.

---

## Metrik Evaluasi: Ilusi Angka Akurasi yang Menipu Orang Bisnis

Ini bagian paling krusial yang wajib lo kuasai luar kepala buat tesis dan GPBSales, Sar. Orang non-teknis kayak sales atau bos-bos manajemen kantor gue cuma tahu satu kata: **Akurasi**. Mereka bakal nanya, *"Model lo akurasinya berapa persen? 95 persen? Keren, langsung jual ke klien!"*

Padahal di dunia machine learning, bersandar cuma ke angka akurasi itu jebakan betmen nomor satu yang namanya *Accuracy Paradox*.

Coba bayangin kasus klasifikasi tenant berisiko tinggi (*high-risk tenant*) di kantor gue. Dari 1.000 tenant yang nyewa gedung, realitasnya cuma ada 10 tenant yang bener-bener nakal dan kabur nggak bayar sewa. Artinya, 990 tenant adalah tenant aman.

Kalau gue bikin model bodoh yang nggak mikir sama sekali, dan model itu gue suruh nebak secara *hardcode*: *"Semua tenant pasti aman"*, tebak berapa akurasi model bodoh gue?

Akurasi = (Tebakan Benar) / (Total Data) = (990) / (1000) = 99%

Secara angka statistik, model gue kelihatan jenius dengan akurasi 99 persen! Tapi di mata bisnis, model itu sampah total. Kenapa? Karena dia gagal mendeteksi 10 tenant bermasalah yang bikin kantor boncos miliaran rupiah. 

Makanya kita butuh metrik evaluasi yang jauh lebih jujur lewat *Confusion Matrix*:

*   **Precision (Presisi):** Dari semua yang diprediksi positif oleh model, berapa banyak yang aslinya beneran positif?  
    Precision = (TP) / (TP + FP)  
    Metrik ini krusial kalau biaya akibat *False Positive* itu mahal banget. Misalnya: model lo nuduh klien korporat bonafit sebagai calon penipu (*False Positive*). Klien tersinggung, reputasi kantor ancur, deal sewa triliunan melayang.
*   **Recall (Sensitivitas):** Dari semua data yang kenyataannya positif, berapa banyak yang berhasil ditangkap oleh model?  
    Recall = (TP) / (TP + FN)  
    Metrik ini wajib diprioritaskan kalau lo nggak boleh kecolongan *False Negative*. Di kasus tenant nakal tadi, *Recall* harus tinggi! Mending kita salah mencurigai tenant baik buat diverifikasi ulang (*False Positive*), daripada kecolongan tenant nakal yang bikin rugi (*False Negative*).
*   **F1-Score:** Rata-rata harmonik (*harmonic mean*) antara *Precision* dan *Recall*.  
    F1-Score = 2 × (Precision × Recall) / (Precision + Recall)  
    Ini metrik penyelamat kalau sebaran kelas data lo timpang parah (*imbalanced dataset*), kayak data transaksi properti, deteksi fraud, atau prediksi penjualan produk langka lo di GPBSales.

Selain metrik, kita juga harus ngelakuin optimasi model. Lo harus ngecek apakah model lo kena penyakit **Overfitting** (model terlalu ngafal data latih sampai ke detail *noise*-nya, jadi pas dikasih data baru performanya jeblok) atau malah **Underfitting** (model terlalu goblok dan terlalu sederhana, bahkan gagal nangkep pola dasar di data latih sendiri). Di Scikit-learn, kita atasi ini pakai teknik *hyperparameter tuning* (seperti *Grid Search* atau *Random Search*) dan validasi silang (*k-fold cross-validation*) biar model kita bener-bener *robust* pas dideploy ke sistem nyata.

---

## Ruang Diskusi: Menyelamatkan Wajah Kantor dari Janji Palsu

Sari, drama sales overpromise ini sekarang resmi jadi beban moral gue dan tim analis. Besok pagi tim gue diminta manajemen buat bikin draf proposal klarifikasi ke klien, biar ekspektasi mereka bisa ditarik balik ke bumi tanpa bikin kantor kehilangan muka atau batal kontrak. 

Mumpung lo lagi mendalami pipeline data penjualan di GPBSales dan ngerancang metodologi tesis lo, gue mau nodong perspektif analitis lo soal beberapa hal ini:

1. **Menghadapi 5V pada Data Historis:**  
Klien minta model estimasi sewa properti komersial yang presisi, tapi data historis kantor kami penuh dengan format campur aduk (PDF, Excel beda versi warisan masa lalu, dan catatan kualitatif negosiasi). Sebagai arsitek sistem informasi, gimana strategi lo menyortir mana data yang layak masuk tahap *preprocessing* dan mana yang harus direlakan dibuang demi menjaga *Veracity* tanpa mengorbankan *Volume*?

2. **Dilema Metrik Bisnis vs Metrik Teknis:**  
Kalau lo jadi konsultan teknis gue, metrik apa yang bakal lo taruh di slide presentasi klarifikasi ke jajaran direktur klien: *Precision*, *Recall*, atau *F1-Score*? Gimana cara lo menjelaskan urgensi metrik pilihan lo itu pakai bahasa bisnis yang gampang dipahami orang non-teknis, biar mereka paham kenapa model dengan akurasi 88% tapi F1-score tinggi jauh lebih menguntungkan daripada model dengan akurasi semu 98%?

3. **Etika Pipeline Deployment:**  
Dari kacamata manajemen sistem informasi, apa *governance policy* atau pagar pembatas SOP yang harus dibangun di level organisasi biar divisi bisnis/marketing nggak bisa seenak jidat nge-pitch kapabilitas algoritma machine learning yang belum tervalidasi pada tahap *deployment*?

---

Tumpukan mug kopi di samping laptop gue udah dingin semua, dan grup Slack tim data kantor masih berisik debat kusir soal revisi dokumen *scope of work* buat klien besok pagi. Tolong kasih pencerahan lo sebelum gue bener-bener khilaf ngelempar slide presentasinya Vina ke tempat sampah daur ulang.

Sampai ketemu di sesi belajar akhir pekan ini, Sar. Tetap waras di tengah gempuran deadline tesis dan selamat ngulik data!

Nik
