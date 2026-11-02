---
title: "Catatan Nik: Demo Viral LinkedIn, Halusinasi Klien SCBD, dan Seni Menemukan Pola Tanpa Kunci Jawaban"
subtitle: Gue baru aja liat klien minta dashboard ajaib cuma bermodal video demo di LinkedIn, padahal data yang mereka kirim masih setengah kosong dan tanpa satu pun label.
type: blog
date: 2026-11-03T06:49:17.150776+07:00
draft: false
ws_chat: 1637
ws_msg: 21681
category: Collab Journal
tags: ["study", "collab-journal", "MMSI", "implementasi-artificial-intelligence", "catatan-nik"]
summary: "Materi kuliah gue pekan ini soal unsupervised learning dan reinforcement learning: ngelompokin data tanpa kunci jawaban, dari K-Means sampai dendrogram, plus kenapa janji RL di atas spreadsheet statis itu cuma dongeng jualan. Di kantor gue, Vina jual dashboard clustering ke klien ritel yang datanya berantakan, dan Aris yang musti nyelamatin."
hook: Pernah nggak lo liat demo AI yang mulus di video, terus pas data aslinya dibuka, isinya spreadsheet setengah kosong tanpa label?
---

Layar monitor ultrawide milik Aris di lantai 28 SCBD siang tadi muter video demo yang sama sampai empat kali. Di video itu, sebuah dashboard proptech asal California kelihatan begitu mulus: titik-titik data tenant pusat perbelanjaan bergerak sendiri membentuk gelembung-gelembung warna pastel, grafik konversi melompat dinamis, dan tiba-tiba muncul notifikasi pintar yang merekomendasikan penataan ulang denah lantai secara otomatis. 

Vina, *head of sales* kantor kami, berdiri tepat di belakang kursi Aris sambil menyesap matchanya. Dengan gaya khas *business development* papan atas yang selalu penuh determinasi, dia menepuk partisi kubikel. 

"Klien kita dari konsorsium ritel tadi pagi nodong gue, Ris, Nik," kata Vina tanpa basa-basi. "Mereka lihat video ini di LinkedIn dan minta kita pasang dashboard yang persis kayak gini di proyek evaluasi portofolio mereka. Katanya, mereka pengen sistem kita bisa langsung klaster tenant mana yang bakal nunggak sewa dan tenant mana yang potensial dinaikkan tarifnya, otomatis tanpa perlu disuapin aturan manual. Gue bilang ke mereka, tenang aja, tim analitik kami lagi develop smart clustering berbasis *reinforcement learning* biar sistemnya adaptif dan belajar sendiri."

Gue cuma bisa memijat pelipis pelan, sementara Aris langsung tersedak Americano dinginnya. 

---

## Ketika Klien Pengen "Dashboard Ajaib" Bermodal Video Demo

Masalah klasiknya bukan pada ambisi Vina, Sar. Ambisi jualan itu bahan bakar kantor konsultan properti kayak tempat gue kerja. Masalahnya ada pada jurang raksasa antara apa yang klien tonton di internet dengan realitas data yang mereka lempar ke tim kami lewat Google Drive kemarin sore.

Setelah Vina melenggang pergi ke ruang rapat kaca di ujung koridor lantai 28, gue narik kursi ke samping meja Aris buat memeriksa folder data kiriman klien tersebut. Lo tahu apa isinya?

Tiga belas file spreadsheet dengan format berantakan. Kolom nama *tenant* diisi manual tanpa standarisasi: ada yang nulis "PT Kopi Senja Pagi", "Kopi Senja Pagi - GF 02", sampai cuma singkatan "KSP Lt. Dasar". Kolom omzet bulanan setengahnya bolong, catatan komplain fasilitas mall cuma berupa teks bebas sepanjang dua paragraf di kolom keterangan, dan sama sekali nggak ada label historis yang mendefinisikan mana penyewa "bermasalah" versus "berkinerja unggul". 

Klien menuntut dashboard yang bisa berpikir sendiri layaknya manusia super cerdas, tapi data yang disetor cuma serpihan puzzle yang basah kuyup kena tumpahan air. Dan yang bikin gue geleng-geleng kepala adalah istilah yang diobral Vina ke klien: mencampuradukkan *unsupervised clustering* dengan *reinforcement learning* seolah-olah keduanya cuma bumbu penyedap yang bisa dituang barengan ke dalam sup data mentah.

Ini momen yang pas banget buat gue bedah materi kuliah gue pertemuan lima ini, Sar. Kenapa? Karena di dunia kerja nyata, ilusi terbesar orang bisnis adalah menganggap machine learning non-supervised itu semacam kotak hitam magis yang bisa menyulap sampah menjadi emas tanpa pemahaman struktur matematis di baliknya.

---

## Membedah Unsupervised Learning: Menemukan Pola Tanpa Kunci Jawaban

Di modul kuliah gue pekan lalu, gue belajar *supervised learning*, di mana model bekerja kayak anak sekolah yang memegang buku latihan lengkap dengan kunci jawaban di halaman belakang. Ada input X, ada label target Y. Kalau model salah menebak label, fungsi *loss* menghitung selisihnya, lalu bobot diperbaiki lewat optimasi.

Nah, *unsupervised learning* adalah permainan yang sama sekali beda dimensinya. Di sini, kita cuma punya tumpukan data tanpa selembar pun kunci jawaban. Nggak ada label "penyewa macet", nggak ada kategori "pelanggan loyal", nggak ada status "transaksi curang". Algoritma dibiarkan menyelam sendirian ke dalam ruang vektor multidimensi untuk menemukan struktur tersembunyi (*hidden structure*) yang luput dari pandangan mata manusia.

Secara filosofis, *unsupervised learning* bukan bertujuan memprediksi masa depan berdasarkan masa lalu yang berlabel, melainkan memetakan realitas yang ada hari ini. Sutton dan Barto, serta para begawan machine learning lainnya, selalu menekankan bahwa ketiadaan label supervisi memaksa algoritma bersandar murni pada metrik intrinsik data itu sendiri: jarak, kepadatan, probabilitas distribusi, atau variansi.

Di dunia manajemen sistem informasi dan analitik korporat, tugas utama *unsupervised learning* biasanya terbagi menjadi tiga ranah besar:

1. **Clustering (Pengelompokan):** Mempartisi observasi ke dalam kelompok-kelompok homogen di mana anggota dalam satu kelompok punya kemiripan (*similarity*) setinggi mungkin, sementara perbedaan antar kelompok dibuat sebesar-besarnya.
2. **Association Rule Mining (Analisis Asosiasi):** Menemukan keterikatan antar atribut dalam satu kejadian bersama, seperti analisis keranjang belanja (*market basket analysis*) klasik yang legendaris itu.
3. **Dimensionality Reduction (Reduksi Dimensi):** Memadatkan puluhan atau ratusan variabel fitur menjadi beberapa dimensi representatif tanpa menghilangkan informasi penting, seperti pada Principal Component Analysis (PCA) atau t-SNE.

Ketika klien Vina minta sistem yang bisa memetakan ribuan tenant mall tanpa data historis berlabel, mereka sebenarnya sedang butuh *clustering* untuk *exploratory data analysis* (EDA) dan segmentasi, bukan mesin peramal nasib.

---

## Spektrum Klastering: Dari yang Garis Keras Sampai yang Fleksibel

Waktu Aris mulai membuka Jupyter Notebook buat merapikan data tenant tadi, kami sempat berdebat soal algoritma apa yang paling masuk akal dipakai. Di sinilah teori klastering dari ruang kuliah langsung berbenturan dengan realitas bisnis di lantai 28.

Klastering itu nggak monolitik. Pendekatannya punya spektrum yang lebar, dan salah memilih tipe klastering bisa bikin interpretasi manajemen jadi ngawur total.

### 1. Exclusive Clustering (Klastering Eksklusif / Hard Clustering)
Pendekatan ini menganut prinsip hitam-putih. Setiap baris data wajib masuk ke tepat satu klaster, nggak boleh mendua. Contoh paling klasiknya adalah K-Means. Algoritma ini menempatkan sejumlah k titik pusat (*centroid*) di ruang data, lalu setiap observasi ditarik ke centroid terdekat berdasarkan jarak Euclidean atau Manhattan.

Masalahnya buat kasus tenant ritel klien kami: apakah sebuah restoran waralaba besar yang omzetnya tinggi tapi sering telat bayar denda sewa bisa murni dimasukkan ke klaster "Tenant Emas"? K-Means bakal memaksanya masuk ke salah satu kotak, padahal realitas perilakunya punya karakter ganda.

### 2. Overlapping Clustering (Klastering Tumpang Tindih / Soft Clustering)
Di spektrum ini, data nggak dipaksa memilih satu rumah. Setiap observasi punya derajat keanggotaan (*membership value*) ke beberapa klaster sekaligus, misalnya dengan Fuzzy C-Means. Satu tenant ritel bisa saja memiliki 70% karakteristik klaster "Penyewa Stabil" dan 30% karakteristik "Penyewa Risiko Likuiditas". Buat analisis portofolio properti tingkat lanjut, pendekatan ini jauh lebih realistis karena dunia bisnis jarang sekali bersifat biner.

### 3. Hierarchical Clustering (Klastering Hierarkis)
Kalau K-Means mengharuskan kita menebak atau menguji nilai k di awal (misalnya lewat metode *elbow* atau *silhouette score*), klastering hierarkis membangun struktur pohon kemiripan (*dendrogram*). 
Pendekatannya bisa *agglomerative* (bottom-up: tiap data mulai sebagai klasternya sendiri lalu digabung bertahap berdasarkan jarak linkage terdekat) atau *divisive* (top-down: semua data dianggap satu klaster raksasa lalu diiris-iris sampai mengecil). 

Kelebihan klastering hierarkis buat manajemen adalah transparansi visualnya. Direksi bisa melihat di level granularitas mana sebuah kelompok tenant mulai memisahkan diri dari gerombolan utama. Sayangnya, secara komputasi algoritma ini haus memori kalau baris datanya sudah menyentuh ratusan ribu baris.

---

## Asosiasi dan Reduksi Dimensi: Merapikan Lemari yang Kepenuhan

Selain klastering, ada dua pilar *unsupervised* yang sering dilupakan orang sales kayak Vina pas jualan ke klien:

Pertama, **Analisis Asosiasi**. Kalau Vina pengen tahu tipe gerai apa yang kalau dibuka di lantai satu bakal mendongkrak trafik ke gerai lain di lantai tiga, algoritma macam Apriori atau FP-Growth yang dicari. Kita mencari aturan implikasi A itu nyambung ke B berbasis metrik *support* (seberapa sering kombinasi muncul), *confidence* (seberapa pasti B muncul kalau A ada), dan *lift* (seberapa kuat keterikatan mereka dibanding kebetulan acak).

Kedua, **Reduksi Dimensi**. Klien menyerahkan tabel dengan 45 kolom atribut per tenant: mulai dari luas lantai, daya listrik, jumlah karyawan, frekuensi pergantian display, indeks kepuasan AC, sampai histori telat bayar bulanan. Mencoba menghitung jarak klaster di ruang 45 dimensi itu bencana matematis murni yang dikenal sebagai *curse of dimensionality*. Ruang data jadi terlalu kosong (*sparse*), dan jarak antar titik menjadi nyaris seragam sehingga konsep "tetangga terdekat" kehilangan makna.

Lewat teknik reduksi dimensi, 45 variabel yang saling berkorelasi itu bisa kita proyeksikan ke ruang yang lebih ringkas, menyisakan komponen utama yang paling banyak menjelaskan variansi data. Visualisasi 2D atau 3D yang dilihat klien di LinkedIn itu hampir pasti merupakan hasil proyeksi semacam ini, bukan sihir.

---

## Reinforcement Learning: Bukan Diberitahu Benar, tapi Belajar dari Babak Belur

Nah, sekarang kita masuk ke bagian paling fatal dari janji manis Vina: mengklaim bahwa dashboard tersebut bakal ditenagai oleh *Reinforcement Learning* (RL).

Gue harus menegaskan ini ke lo, Sar, biar kita sama-sama jernih pas ujian nanti: **Reinforcement Learning bukan bagian dari Unsupervised Learning, dan cara kerjanya sama sekali bertolak belakang dengan klastering data statis.**

Buku legendaris Richard S. Sutton dan Andrew G. Barto (*Reinforcement Learning: An Introduction*) menegaskan sejak bab pembuka: RL adalah paradigma ketiga dalam machine learning, terpisah dari supervised dan unsupervised. RL tidak belajar dari sekumpulan data latih yang pasif. RL belajar melalui interaksi dinamis antara entitas pembelajar (*agent*) dengan lingkungannya (*environment*).

Arsitektur RL berdiri di atas fondasi formal yang disebut **Markov Decision Process (MDP)**, yang terdiri dari komponen inti:

1. **Agent:** Entitas pengambil keputusan yang sedang belajar (misalnya bot software, algoritma trading, atau sistem kendali).
2. **Environment:** Dunia tempat agent beroperasi, yang menerima tindakan dan merespons dengan kondisi baru.
3. **State:** Representasi situasi atau kondisi lingkungan pada satu langkah waktu.
4. **Action:** Tindakan yang dieksekusi oleh agent berdasarkan state saat itu.
5. **Reward:** Umpan balik berupa nilai numerik skalar dari lingkungan sebagai konsekuensi atas tindakan yang diambil. Bisa bernilai positif (hadiah) atau negatif (penalti).
6. **Policy:** Strategi atau pemetaan mental dari state ke action yang terus diperbaiki oleh agent demi memaksimalkan akumulasi reward jangka panjang (*cumulative discounted return*).

Agent RL tidak pernah diberi tahu tindakan apa yang paling benar. Dia harus menjelajah (*exploration*) untuk mencoba berbagai aksi baru, sembari memanfaatkan (*exploitation*) pengetahuan yang sudah terbukti menghasilkan reward tinggi. 

Pikirkan bagaimana AlphaZero belajar menguasai catur tanpa pernah membaca buku teori pembukaan: dia bermain melawan dirinya sendiri jutaan kali. Ketika menang, dia mendapat reward positif; ketika kalah, penalti. Dia belajar dari babak belur di papan catur virtual. Konsep yang sama dipakai pada kendali mobil otonom (*self-driving cars*) yang belajar menjaga posisi di jalur jalan raya, atau sistem dialog percakapan yang mengoptimalkan kepuasan interaksi pengguna secara berulang.

Sekarang coba lo bayangkan keganjilan logika Vina: dia menjanjikan *Reinforcement Learning* untuk sebuah tabel spreadsheet tenant properti yang sifatnya statis di Google Drive! 

Di mana lingkungannya? Tindakan apa yang bisa dieksekusi oleh agent secara mandiri? Apa reward fungsinya? Kalau agent salah mengambil aksi dan menaikkan tarif sewa 300% pada tenant utama mall sampai gerai itu gulung tikar, apakah klien mau menanggung kerugian miliaran rupiah cuma demi memberi sinyal penalti numerik ke algoritma?

Tentu saja enggak. Memaksakan RL ke dalam analisis data tabular statis korporat tanpa adanya simulator dinamis dan ruang aksi nyata adalah bentuk salah kaprah paling mahal dalam industri AI saat ini.

---

## Menghubungkan Titik: Dari GPBSales Sampai Ruang Rapat Lantai 28

Sambil menenangkan Aris yang sempat panik mengira harus membangun neural network RL dari nol sebelum hari Jumat, pikiran gue langsung melayang ke tugas lo kemarin yang lagi sibuk mengutak-atik GPBSales, dataset penjualan buku digital lo yang ukurannya satu juta baris lebih itu.

Ingat nggak waktu lo cerita betapa pusingnya lo melihat data transaksi pembelian buku digital tanpa ada profil demografis pembeli yang jelas? Di situ lo cuma punya riwayat transaksi: user ID, judul buku, kategori, waktu pembelian, dan durasi membaca.

Tantangan lo di GPBSales itu adalah padanan sempurna dari apa yang kami hadapi di lantai 28. Fitur rekomendasi legendaris platform e-commerce seperti "pembaca yang membeli buku ini juga menyukai buku itu" atau "pembaca dengan selera mirip lo membaca judul-judul ini" pada dasarnya adalah aplikasi murni dari *unsupervised learning*, khususnya perpaduan antara klastering profil pengguna dan collaborative filtering berbasis kesamaan vektor (*cosine similarity*).

Di GPBSales, lo nggak punya label manual yang menandai "User ini pecinta fiksi sejarah garis keras" atau "User ini pembaca musiman yang cuma beli buku diskon". Lo harus membiarkan algoritma mengelompokkan pola pembelian tersebut secara alamiah berdasarkan kedekatan jarak di matriks interaksi. Ketika dua pembeli yang belum pernah saling kenal punya jejak vektor yang berhimpitan di sepuluh judul buku yang sama, mereka otomatis masuk ke dalam klaster minat yang identik.

Itulah kekuatan sejati *unsupervised learning*: memberikan kejelasan struktural pada tumpukan data masif yang tadinya terlihat seperti kebisingan (*noise*) tanpa makna.

Sore tadi, sebelum lift SCBD membawa gue turun ke lobi, gue minta Aris menyetop mimpi buruk RL-nya. Kami sepakat menyusun proposal tandingan buat Vina. Besok pagi, kami bakal presentasikan ke Vina bahwa yang akan kita bangun untuk klien ritel bukan sistem fiksi ilmiah yang belajar sendiri di awang-awang, melainkan *pipeline unsupervised learning* yang solid:

1. Pembersihan data teks nama tenant dan standardisasi parameter finansial.
2. Reduksi dimensi menggunakan PCA untuk merangkum puluhan indikator performa tenant menjadi peta visual interaktif.
3. Klastering hierarkis dan K-Means untuk membagi tenant ke dalam empat kuadran operasional yang jelas: tenant jangkar bereputasi tinggi, tenant berkembang, tenant berisiko likuiditas, dan tenant musiman.
4. Dashboard berbasis visualisasi klaster yang memberi rekomendasi penataan zonasi berdasarkan pola kedekatan antar kategori gerai.

Vina tetap dapat visualisasi pastel canggih yang bisa dia pamerkan dengan bangga ke klien ritelnya, Aris nggak perlu mengundurkan diri karena stres, dan kami menyajikan sistem yang secara metodologis bisa dipertanggungjawabkan di ruang audit mana pun.

---

## Food for Thoughts Buat Sari

Karena lo lagi megang GPBSales dan kita sama-sama lagi menuntaskan pemahaman tentang batas tegas antara unsupervised dan reinforcement learning, gue mau lempar beberapa pertanyaan buat bahan refleksi lo di jurnal berikutnya:

1. **Evaluasi Tanpa Kunci Jawaban:** Pada *supervised learning*, kita punya metrik presisi, *recall*, atau *mean squared error* yang jelas karena ada data pembanding. Tapi kalau lo mengelompokkan pola pembeli di dataset GPBSales menggunakan K-Means tanpa adanya label kategori sama sekali, bagaimana cara lo secara objektif membuktikan ke dosen atau manajemen bahwa jumlah klaster yang lo pilih itu valid dan polanya bukan sekadar ilusi kebetulan dari persebaran data acak?
2. **Kapan RL Masuk Akal dalam Bisnis Informasi?** Kalau pada analisis data historis statis (seperti portofolio tenant atau transaksi penjualan masa lalu) *reinforcement learning* terbukti tidak cocok, di titik mana sebenarnya RL benar-benar relevan dan layak diimplementasikan dalam arsitektur sistem informasi manajemen modern? Syarat fundamental apa yang wajib ada di lingkungan bisnis agar agent RL bisa belajar secara etis dan aman tanpa merusak operasional riil perusahaan?
3. **Bahaya Overlapping vs Exclusive:** Dalam kasus segmentasi pelanggan buku digital di GPBSales lo, menurut analisis lo lebih tepat menerapkan *exclusive clustering* (seperti K-Means standar) atau *overlapping clustering* (seperti Fuzzy C-Means)? Pertimbangkan dari sisi kompleksitas komputasi versus kegunaan praktisnya buat tim marketing yang mau merancang kampanye promo personal!

Lo timbang sendiri ya, Sar, kuantitas vs kegunaan buat tim yang beneran bakal pakai hasilnya.

Jam sembilan malam. Dari jendela kamar gue, lampu-lampu tol masuk kota masih kelihatan betah, dan tumpukan modul di sebelah laptop belum juga berkurang. Gue mau nyeduh teh terakhir, baca dua halaman lagi, terus matiin lampu sebelum ngantuknya kabur.

Nik
