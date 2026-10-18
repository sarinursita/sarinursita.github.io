---
title: "Catatan Nik: Perang Dingin CRM Baru vs Warisan SQL"
subtitle: "Enam dimensi kualitas data itu kedengeran kayak istilah akademik. Gue nemu empat di antaranya cuma dalam satu sore."
type: "blog"
date: "2026-10-19T05:00:00+07:00"
draft: true
ws_chat: 1601
ws_msg: 21534
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "analisa-dan-desain-smart-system", "catatan-nik"]
summary: "Materi pekan ini soal kualitas data dan EDA. Di kantor gue, sistem SQL warisan dan CRM baru ngasih angka beda buat klien yang sama, dan dua divisi saling tunjuk sambil nyalahin data orang lain."
hook: "\"Datanya yang salah, bukan sistem kita.\" Dua divisi ngomong kalimat yang sama di rapat yang sama, dan gue yang harus nebak angka mana yang bener sebelum presentasi ke klien."
---

Gelas kopi susu gula aren di meja gue udah tinggal es batu yang mencair, rasanya hambar mirip suasana *townhall* dadakan tadi siang. 

Gue baru aja cabut dari *meeting room* virtual yang isinya dua puluh orang saling todong di kolom *chat*. Gara-garanya sederhana tapi bikin tensi sekantor naik sampai ubun-ubun: angka total nilai transaksi properti komersial kuartal ini beda hampir empat puluh miliar rupiah antara laporan tim *business development* dan tim *finance operations*. 

Tim BD dengan bangga pamer angka fantastis dari CRM *cloud* berbasis SaaS yang baru kelar *rollout* dua bulan lalu. Sementara tim *finance*, yang masih setia megang *pipeline* SQL gabungan lembar kerja lawas peninggalan era Bram dulu, langsung menyanggah sambil melempar tabel rekapitulasi tandingan. Dua kubu saling tunjuk hidung. Tim sales nuduh *finance* kolot dan nggak bisa *move on* dari sistem purba, sedangkan *finance* ngamuk bilang tim sales halusinasi karena masukin *deal* fiktif. 

Melihat kekacauan itu, gue mendadak teringat materi kuliah SSAD pertemuan ketiga kita minggu ini tentang *Data Understanding* dan *Exploratory Data Analysis* (EDA). Fenomena lempar batu sembunyi tangan kayak gini klasik banget di korporat: manajemen buru-buru pasang *dashboard* keren dan migrasi ke *tools* serba modern, tapi begitu dua sistem ditautkan, datanya tabrakan parah. Nggak ada yang pernah bener-bener duduk buat ngecek kualitas data dasarnya apalagi ngelakuin eksplorasi yang benar.

---

## Membongkar Enam Dosa Kualitas Data (*Data Quality Dimensions*)

Sebelum kita latah ngomongin algoritma canggih, *machine learning*, atau bikin grafik warna-warni yang bikin takjub bos, fondasi paling dasar yang wajib diberesin adalah audit kualitas data (*data quality assessment*). Kalau datanya sampah, hasil akhirnya cuma halusinasi yang dipoles rapi (*garbage in, garbage gospel*). 

Di kasus kantor gue tadi siang, setelah gue bedah bareng tim analitik, kita nemu borok dari enam dimensi kualitas data yang selama ini diabaikan:

```
[Sumber Data Mentah]
        |
        v
+-------------------------------------------------------+
|            Uji 6 Dimensi Kualitas Data                |
|  Accuracy | Completeness | Consistency | Timeliness   |
|               Validity   | Uniqueness                 |
+-------------------------------------------------------+
        |
        v
[Eksplorasi Data Awal / EDA (Tukey, 1977)]
  - Univariate (Distribusi, Outlier)
  - Bivariate (Korelasi, Hubungan Dua Variabel)
  - Multivariate (Heatmap, Interaksi Kompleks)
        |
        v
[Modal Kerja: Dokumentasi, Traceability, Desain Sistem]
```

### 1. *Accuracy* (Akurasi)
Data harus mencerminkan kenyataan riil di lapangan. Pas gue cek CRM baru, ada satu transaksi sewa gedung kantor di koridor Sudirman yang tercatat nilainya sembilan ratus triliun rupiah. Usut punya usut, staf BD yang input salah ketik kode mata uang: niatnya masukin angka dalam Rupiah, tapi sistem mencatatnya dalam satuan ribuan US Dollar. Secara komputasi angkanya valid berupa nominal, tapi secara realitas bisnis itu ngawur total.

### 2. *Completeness* (Kelengkapan)
Kelengkapan ini soal seberapa banyak nilai kosong (*missing values*) di variabel-variabel krusial. Di sistem SQL lama, kolom *handover date* (tanggal serah terima unit) terisi rapi karena wajib diisi buat penagihan invoice. Tapi di CRM baru, karena formulir input dibikin terlalu fleksibel biar tim sales nggak malas mengisi, kolom itu dibiarkan opsional. Hasilnya? Tujuh puluh persen baris transaksi baru status tanggalnya bolong.

### 3. *Consistency* (Konsistensi)
Ini biang kerok utama perang dingin tadi siang. Sistem warisan mencatat nama gedung dengan format baku kode pos dan entitas resmi (misal: "Gedung Bursa Efek Indonesia, Tower 2"), sementara tim sales di CRM baru nulis seenak jidat: ada yang nulis "BEI T2", "IDX Tower II", sampai "Bursa Efek SCBD". Ketika kedua tabel digabung pakai perintah *JOIN*, sistem gagal mengenali kalau tiga baris itu merujuk ke aset fisik yang sama persis.

### 4. *Timeliness* (Ketepatan Waktu)
Data harus cukup segar untuk dipakai mengambil keputusan. CRM *cloud* menarik data secara *real-time*, sedangkan repositori SQL lokal baru di-refresh setiap penutupan buku akhir bulan (*batch update*). Membandingkan data hari ini dari CRM dengan data SQL yang belum disinkronisasi jelas bikin angkanya jomplang puluhan miliar.

### 5. *Validity* (Validitas)
Validitas mengukur kepatuhan data terhadap aturan, format, atau rentang logika bisnis (*business rules*). Pas dicek, banyak kolom nomor pokok wajib pajak (NPWP) perusahaan penyewa yang diisi angka *dummy* seperti "00000000" atau "99999999" cuma gara-gara *form validator* di antarmuka CRM mewajibkan kolom itu diisi sebelum tombol *submit* bisa diklik. Formatnya sah berupa angka, tapi nilainya nggak valid secara hukum bisnis.

### 6. *Uniqueness* (Keunikan)
Nggak boleh ada duplikasi entitas (*single source of truth*). Di CRM baru, tim BD membuat satu entri baru setiap kali ada revisi negosiasi harga sewa. Akibatnya, satu transaksi sewa lantai perkantoran yang direvisi empat kali tercatat sebagai empat transaksi berbeda yang nilainya terakumulasi. Pantas saja angka BD membengkak fantastis.

---

## Anatomi Nilai Hilang, Anomali, dan Kebisingan Data

Begitu kita melangkah lebih dalam ke pemahaman data awal, ada beberapa jebakan anatomi data yang nggak boleh ditelan mentah-mentah:

### Tiga Mazhab *Missing Values*
Nilai kosong itu bukan sekadar sel kosong yang bisa langsung dihapus atau diisi nilai rata-rata (*mean imputation*). Kita harus paham mekanisme hilangnya data:

*   **MCAR (*Missing Completely at Random*):** Data hilang murni karena faktor acak yang tidak berhubungan dengan variabel mana pun. Contohnya: jaringan putus waktu anak magang submit survei kepuasan penyewa, sehingga satu lembar kuesioner hilang acak.
*   **MAR (*Missing at Random*):** Data hilang secara sistematis, tapi ketergantungannya ada pada variabel lain yang teramati, bukan variabel itu sendiri. Contoh: klien dari sektor perbankan multinasional jarang mengisi kolom "perkiraan budget renovasi", bukan karena mereka malu dengan angkanya, tapi karena regulasi kepatuhan internal bank melarang mereka membeberkan anggaran sebelum proses lelang resmi dibuka.
*   **MNAR (*Missing Not at Random*):** Ini jenis yang paling berbahaya dan licik. Nilai itu hilang justru karena faktor nilai dari variabel itu sendiri. Contoh klasiknya: *tenant* yang nilai tunggakan sewanya paling tinggi justru sengaja mengosongkan kolom omzet bulanan di laporan berkala karena takut diusir atau dikenai denda penalti. Kalau data MNAR ini lo buang begitu saja, analisis finansial kantor bakal menghasilkan estimasi risiko yang bias dan terlalu optimistis.

### *Outlier*, Duplikasi, dan Kebisingan (*Noise*)
*Outlier* atau nilai ekstrem itu bukan musuh yang harus langsung dilenyapkan. Di bisnis properti komersial, transaksi jumbo bernilai triliunan rupiah dari konglomerat teknologi memang bakal kelihatan mencolok di ujung grafik. Tapi itu bukan eror, melainkan sinyal transaksi strategis (*black swan event*). Yang jadi masalah adalah *noise* alias gangguan acak akibat salah konversi satuan: ada luas lantai yang ditulis dalam meter persegi, tapi ada staf yang terbiasa pakai *square feet* warisan ekspatriat. Tanpa standardisasi, model analisis bakal membaca data itu sebagai anomali ekstrem.

---

## Masuk ke Gelanggang EDA: Membaca Cerita di Balik Angka

Sar, ini bagian yang paling ngubah cara gue baca laporan: detektif data itu ternyata mulai dari ngobrol sama datanya dulu, bukan dari nulis hipotesis buat dibuktikan.

Setelah tumpukan data dibersihkan dari cacat logika dasar, tahap berikutnya adalah *Exploratory Data Analysis* (EDA). Konsep yang dipopulerkan oleh matematikawan John Tukey pada tahun 1977 ini menekankan pentingnya menjadi detektif data. 

Tukey mengajarkan kita untuk memeriksa data tanpa prasangka atau hipotesis kaku (*listen to the data before you speak*). Ini kontras banget dengan *Confirmatory Data Analysis* (CDA) yang kerjanya menguji hipotesis formal pakai uji signifikansi dan *p-value*. Di tahap rancang bangun sistem informasi, kita butuh EDA buat menangkap pola tersembunyi yang nggak terpikirkan saat wawancara kebutuhan sistem (*requirements gathering*).

```
Tingkatan Eksplorasi Data (EDA):
├── 1. Univariate Analysis
│   ├── Metrik: Mean, Median, Modus, IQR, Skewness, Kurtosis
│   └── Visual: Histogram, Boxplot, Density Plot, QQ-Plot
├── 2. Bivariate Analysis
│   ├── Hubungan: Scatter Plot, Korelasi (Pearson vs Spearman), Crosstab
│   └── Pola: Tren Waktu (Line Plot, Dekomposisi Musiman)
└── 3. Multivariate Analysis
    ├── Interaksi: Correlation Heatmap, Pair Plot, Plot Berkelompok
    └── Reduksi: Deteksi Pola Kompleks Lintas Dimensi
```

Dalam praktiknya, kita membedah data secara bertingkat:

### 1. *Univariate Analysis* (Eksplorasi Satu Variabel)
Kita membedah distribusi satu per satu kolom secara mandiri. Di sini kita nggak cuma ngitung *mean* (rata-rata), karena *mean* gampang banget terdistorsi oleh satu transaksi bernilai raksasa. 

Kita wajib memeriksa *median* dan *modus*, menghitung rentang antar-kuartil (*Interquartile Range* / IQR), serta mengukur *skewness* (apakah kurva condong ke kanan/kiri) dan *kurtosis* (apakah distribusinya runcing dengan ekor tebal). 
*   **Histogram & Density Plot:** Dipakai buat melihat apakah sebaran harga sewa per meter persegi membentuk kurva normal atau justru *bimodal* (dua puncak: pasar kantor kelas A vs kelas C).
*   **Boxplot:** Senjata paling ampuh buat memvisualisasikan lima angka ringkasan (*minimum*, kuartil 1, median, kuartil 3, *maximum*) dan menyaring *outlier* yang berada di luar rentang 1,5 × IQR.
*   **QQ-Plot (*Quantile-Quantile Plot*):** Membantu memastikan apakah sebaran residu data kita beneran mengikuti distribusi teoritis normal sebelum kita berani menerapkan model statistik parametrik.

### 2. *Bivariate Analysis* (Eksplorasi Dua Variabel)
Melihat bagaimana dua variabel saling berinteraksi.
*   **Scatter Plot:** Melihat korelasi visual antara luas ruang kantor yang disewa dengan durasi masa sewa (*lease term*).
*   **Korelasi Pearson vs Spearman:** Kalau hubungannya linear murni dan terdistribusi normal, kita pakai korelasi *Pearson*. Tapi kalau hubungan datanya monoton tapi tidak linear, atau datanya berupa skala ordinal berperingkat, korelasi *Spearman* jauh lebih tangguh dan nggak gampang tertipu data pencakar langit.
*   **Crosstab & Boxplot Terkelompok:** Melihat variasi harga sewa jika dikelompokkan berdasarkan sub-pasar (misalnya SCBD vs TB Simatupang).
*   **Analisis Rangkaian Waktu (*Time Series*):** Memakai *line plot* dan dekomposisi musiman untuk melihat apakah ada pola siklus di mana penandatanganan kontrak properti selalu menumpuk di kuartal empat karena sisa alokasi anggaran belanja korporat.

### 3. *Multivariate Analysis* (Eksplorasi Banyak Variabel Sekaligus)
Dunia nyata nggak pernah sesederhana hubungan dua variabel.
*   **Correlation Heatmap:** Matriks korelasi berwarna yang memudahkan mata kita menangkap multikolinearitas (kondisi di mana dua variabel independen saling menjelaskan hal yang sama, misalnya luas kotor bangunan dan luas bersih bangunan).
*   **Pair Plot & Scatter Tersegmentasi:** Memplot interaksi antara harga sewa, tingkat hunian (*occupancy rate*), dan biaya *service charge*, lalu diwarnai (*hue*) berdasarkan kelas gedung komersial.

Untuk menyaring *outlier*, selain aturan praktis 1,5 × IQR pada boxplot, kita juga bisa menghitung *z-score*. Kalau suatu observasi punya nilai absolut z > 3 (artinya berjarak lebih dari tiga standar deviasi dari rata-rata pada distribusi normal), baris tersebut wajib ditandai untuk diverifikasi ulang: apakah itu terobosan bisnis yang sah atau murni eror manusia saat entri data.

---

## Dari Detektif Data Menuju Arsitektur Sistem

Banyak analis pemula menganggap EDA itu cuma fase bikin laporan presentasi PowerPoint yang penuh grafik visual menarik buat memukau dewan direksi. Itu pemahaman yang keliru besar. Dalam rekayasa sistem informasi, pemahaman data awal adalah **modal kerja teknis**:

1. **Penyusunan Dokumentasi & Kamus Data (*Data Dictionary*):** Temuan dari inkonsistensi nama gedung dan duplikasi transaksi langsung kita tuangkan ke dalam kamus data baru. Kolom mana yang wajib diisi, format tanggal apa yang disepakati (*ISO 8601*), dan tipe data apa yang harus dikunci di level basis data.
2. **Keterlacakan Desain (*Traceability*):** Setiap aturan validasi yang kita pasang di sistem baru harus punya jejak audit yang jelas (*traceable*). Misalnya: "Fitur konfirmasi berulang dipasang di antarmuka CRM karena temuan EDA menunjukkan 12% transaksi salah ketik mata uang asing." Keputusan desain antarmuka dan basis data lahir dari pembuktian data lapangan, bukan selera pribadi manajer proyek.
3. **Keputusan Kesiapan Data (*Go / No-Go Decision*):** Menentukan apakah data internal kita sudah cukup matang untuk diproses ke tahap rekayasa fitur (*feature engineering*) di pekan-pekan berikutnya, atau sistem kita justru butuh integrasi API pihak ketiga (misal: data geospasial resmi pemerintah) buat mengisi kekosongan data koordinat aset.

Sar, dari tiga poin itu, yang paling bikin gue deg-degan justru yang terakhir. Kalau datanya ternyata belum cukup, artinya jadwal presentasi ke klien harus diulang dari nol, dan gue yang kena omel paling dulu karena gue yang bawa materinya ke rapat.

---

## Catatan Pribadi: Proyek Tesis GPBSales

Melihat kisruh di SCBD tadi bikin gue makin waspada waktu ngerjain basis data buat draf tesis GPBSales gue sendiri. Proyek sistem penjualan buku ini kelihatannya sepele di permukaan, tapi kalau nggak teliti di tahap pemahaman data awal, hasilnya bisa menyesatkan model analitik promosi yang mau gue bangun:

*   **Identifikasi Keunikan Baris:** Gue harus selalu ingat bahwa kolom `order_id` **bukan** entitas unik per baris. Satu pesanan transaksi pembelian bisa berisi lima judul buku berbeda, yang artinya `order_id` bakal terulang lima kali di tabel transaksi detail. Kunci unik gabungannya (*composite key*) harus melibatkan kombinasi `order_id` dan `book_id`.
*   **Logika Nilai Negatif dan Nol:** Di tabel transaksi buku, nominal penjualan bernilai negatif bukan berarti data rusak atau eror sistem, melainkan penanda transaksi retur (*refund*) buku yang cacat cetak. Begitu juga baris dengan nilai `amount = 0`, itu bukan data kosong, tapi catatan promosi buku gratis atau program *giveaway* untuk peluncuran penulis baru. Kedua kategori ini nggak boleh sembarangan dibuang saat pembersihan data.
*   **Uji Kualitas Judul dan Seri:** Konsistensi penulisan nama seri buku sering kacau karena input manual kasir (misalnya "Seri Manajemen 01" ditulis "Mgmt Series Vol. 1"). Kalau inkonsistensi teks ini nggak distandardisasi dari awal, agregasi data per judul bakal pecah.
*   **Rencana EDA Lanjutan:** Akhir pekan ini gue mau mulai memetakan distribusi total penjualan per kategori penulis pakai *boxplot* buat melihat apakah penjualannya timpang di beberapa penulis mega-*bestseller*, menarik korelasi *Spearman* antara durasi diskon promosi terhadap volume pesanan harian, serta memeriksa pola musiman penjualan buku pelajaran di awal semester ajaran baru.

---

## Bahan Diskusi Analisis

1. Kalau lo dihadapkan pada situasi perang dingin antardivisi kayak di kantor gue tadi, di mana sistem warisan SQL dianggap lebih akurat oleh tim operasional tapi sistem CRM baru punya data yang lebih kaya secara interaksi pelanggan, langkah sistematis apa yang bakal lo ambil buat menetapkan *single source of truth* tanpa bikin salah satu tim merasa disingkirkan?
2. Dalam konteks penanganan nilai hilang bertipe MNAR (*Missing Not at Random*), kenapa metode imputasi statistik standar seperti mengisi sel kosong dengan nilai *mean*, *median*, atau *k-nearest neighbors* (KNN) justru bisa merusak validitas sistem informasi secara fatal? Berikan contoh kasus nyata di industri tempat lo bekerja.
3. John Tukey menekankan bahwa EDA harus bebas dari hipotesis kaku. Tapi di lingkungan korporat yang serba diburu tenggat waktu, manajemen sering menuntut analis data untuk langsung membuktikan hipotesis bisnis mereka (misalnya: "Buktikan kalau platform baru ini menaikkan produktivitas tim sales"). Gimana cara lo menyeimbangkan eksplorasi bebas ala EDA dengan tuntutan target bisnis yang bias konfirmasi (*confirmatory bias*) dari para pemangku kepentingan?

---

Mata gue udah sepet banget mantengin layar monitor yang isinya perbandingan baris data beda format dari dua sistem yang saling ngambek ini. Rasanya malam ini gue butuh *log off* lebih awal, bikin secangkir teh chamomile hangat, terus teleponan santai sama Dylan buat dengar cerita turnamen basket asramanya akhir pekan kemarin biar isi kepala gue nggak melulu isinya tabel dan angka selisih puluhan miliar.

Tabik dari meja kerja yang penuh tumpukan draf skema data,

Nik
