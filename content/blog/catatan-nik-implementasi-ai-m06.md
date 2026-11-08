---
title: "Catatan Nik: Bau Debu Gipsum Lantai 28, Migrasi Abal-Abal, dan Hype Deep Learning yang Bikin Pusing"
subtitle: "Ruang server di lantai 28 digusur pagi ini, sistem dipaksa pindah ke cloud tanpa uji penuh, dan Vina sudah menjual model mirip ChatGPT ke klien sebelum satu baris data kami beres."
type: blog
date: 2026-11-10T05:00:00+07:00
draft: true
ws_chat: 1687
ws_msg: 21834
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "implementasi-artificial-intelligence", "deep-learning", "catatan-nik"]
summary: "Materi pekan ini soal Deep Learning: bedanya sama machine learning biasa, cara jaringan saraf belajar dari kesalahannya sendiri, dan kenapa kata deep bukan berarti cerdas. Di kantor gue, migrasi cloud dadakan bikin data porak-poranda sementara Vina sudah menjanjikan model ala ChatGPT ke klien, padahal yang kami punya cuma 420 baris data bolong."
hook: "Kalau data cuma 420 baris dan sepertiganya bolong, model paling canggih pun cuma bisa salah dengan percaya diri."
---

Aroma karpet basah bercampur debu gipsum menusuk hidung gue begitu pintu lift lantai 28 terbuka. Suara bor listrik dan dentuman palu godam kontraktor terdengar saling bersahut-sahutan dari ujung lorong timur. Ruang *server on-premise* yang selama belasan tahun mendekam tenang di sudut kantor resmi dieksekusi pagi ini, digusur demi ambisi manajemen membangun *VIP lounge* baru buat menyambut calon pembeli lahan komersial kelas kakap. 

Masalahnya, proyek migrasi sistem ke *cloud* yang ditargetkan selesai akhir kuartal mendadak dipangkas tenggat waktunya jadi serba kilat. Tanpa *load testing* yang layak, tanpa validasi *data pipeline*, akhir pekan kemarin tim dipaksa melakukan *lift-and-shift* darurat. Hasilnya langsung berantakan. Senin pagi dimulai dengan puluhan tiket keluhan: *query* sistem valuasi *time out*, relasi antar-tabel putus, dan *dashboard* analitik internal cuma menampilkan layar putih dengan ikon muter tanpa ujung.

Di tengah kepanikan itu, Vina melangkah santai ke area meja gue sambil menenteng *tumbler* kopi. Dengan senyum penuh percaya diri khas orang *business development*, dia melempar celetukan yang bikin kepala gue langsung berdenyut nyeri. 

"Nik, barusan gue paparan ke calon klien konsorsium ritel. Gue bilang ke mereka, kantor kita lagi transisi sistem ke *cloud* karena kita lagi *deploy* model *Deep Learning* mutakhir mirip ChatGPT. Nanti sistem kita bisa otomatis memprediksi valuasi ribuan ruko dan tanah cuma dari ketikan santai di kolom *prompt*. Keren, kan?"

Gue menatap Vina tanpa berkedip. Di seberang meja, Aris yang lagi berkutat menelusuri *log database* yang korup nyaris tersedak air mineral. 

"Vin," kata gue pelan, berusaha mengontrol intonasi biar nggak meledak di depan orang-orang. "Sistem kita yang jalan di *cloud* sekarang aja belum bisa bedain format tanggal transaksi properti antara versi regional sama versi lokal. Gimana ceritanya lo udah jualan *Deep Learning* ke klien?"

Vina cuma tertawa kecil sambil mengibaskan tangan. "Kan namanya juga jualan visi, Nik. Zaman sekarang kalau kita cuma bilang pakai analisis statistik biasa, klien mana mau bayar mahal? Semua orang maunya *deep learning*, maunya yang ada embel-embel *neural network* dan AI canggih."

Fenomena latah ini persis seperti bahasan yang baru gue pelajari di kelas gue minggu ini. Banyak orang bisnis menganggap *Deep Learning* itu tongkat sihir serba bisa yang bisa disulap dalam semalam, padahal di baliknya ada fondasi arsitektur, kebutuhan data raksasa, dan komputasi masif yang kalau dipaksakan ke data berantakan cuma bakal menghasilkan bencana mahal.

---

## Ilusi Kata "Deep": Bukan Soal Kesadaran Magis, Tapi Lapisan Representasi

Mari kita luruskan dulu hierarki yang sering diacak-acak orang kantor kayak Vina. *Artificial Intelligence* (AI) itu payung besarnya: payung keilmuan yang mencakup segala teknik agar mesin bisa meniru kecerdasan manusia, termasuk sistem berbasis aturan logika (*rule-based*) yang sederhana. Di dalam AI, ada cabang bernama *Machine Learning* (ML), yaitu mesin yang belajar mengenali pola langsung dari data tanpa harus diprogram secara eksplisit aturan demi aturan.

Lalu, di mana posisi *Deep Learning* (DL)? 

*Deep Learning* adalah sub-cabang dari *Machine Learning*. Fondasi utamanya bertumpu pada *Artificial Neural Network* (ANN) atau jaringan saraf tiruan yang memiliki banyak lapisan tersembunyi (*multi-layered hidden layers*). Kata *deep* di sini sama sekali bukan berarti modelnya punya "pemikiran mendalam" atau kesadaran filosofis. Kata *deep* itu murni terminologi struktural arsitektur: model tersebut memiliki kedalaman lapisan transformasi matematis yang bertingkat-tingkat.

Perbedaan fundamental antara *Machine Learning* tradisional dan *Deep Learning* terletak pada bagaimana fitur diekstraksi dari data mentah:

*   **Machine Learning Tradisional:** Sangat bergantung pada *feature engineering* manual. Manusia atau analis data harus memeras otak memilih fitur mana yang relevan. Misalnya, kalau Aris mau memprediksi harga gedung pakai algoritma *Random Forest* atau regresi linear, Aris harus mendefinisikan kolom secara manual: luas tanah, rasio luas lantai, jarak ke stasiun MRT terdekat, dan umur bangunan. Kalau fiturnya jelek atau tidak lengkap, modelnya bakal gagal.
*   **Deep Learning:** Mampu melakukan *feature representation* atau *feature extraction* secara otomatis dan bertingkat (*hierarchical feature learning*). Lapisan-lapisan awal jaringan saraf akan menangkap pola primitif (seperti garis tepi atau sudut pada citra satelit properti), lapisan tengah mulai menggabungkannya jadi bentuk atau tekstur (seperti atap, kontur jalan, kepadatan bangunan), dan lapisan akhir mengenali objek utuh (seperti area pergudangan atau kawasan residensial padat).

Proses ini bekerja secara *end-to-end learning*, dari data mentah langsung dipetakan ke target prediksi tanpa intervensi rekayasa fitur manual yang rumit. Tapi keajaiban ini menuntut bayaran mahal: *Deep Learning* baru benar-benar unggul ketika disuapi data berukuran masif (sering kali data tidak terstruktur seperti gambar, audio, atau teks bebas) serta sokongan komputasi GPU yang haus daya listrik.

---

## Anatomi Jaringan Saraf Tiruan: Dari Dot Product Sampai Turunan Parsial

Secara mekanistis, apa sih yang terjadi di dalam satu unit terkecil pemrosesan *Deep Learning*? Unit itu kita sebut neuron buatan (*artificial neuron* atau *perceptron*). Cara kerjanya terinspirasi dari prinsip transmisi sinyal dendrit dan akson pada neuron biologis, meski formulasi matematisnya sebenarnya sangat lugas.

Sebuah neuron menerima sekumpulan nilai masukan, misalnya luas bangunan, tahun renovasi, jarak ke jalan tol. Setiap masukan diberi bobot (*weight*) sendiri-sendiri, dan bobot itu menunjukkan seberapa penting masukan tadi buat keputusan yang mau diambil. Semua masukan dikalikan bobotnya, dijumlahkan, lalu ditambah satu angka penyeimbang yang disebut *bias*. Hasil penjumlahan itu namanya nilai linear. Nilai ini harus dilewatkan ke dalam sebuah fungsi non-linear yang disebut fungsi aktivasi (*activation function*). Tanpa fungsi non-linear ini, berapapun ratusan lapisan yang lo tumpuk di dalam jaringan, seluruh sistem cuma akan runtuh menjadi satu transformasi linear biasa (sama saja kayak regresi linear raksasa).

Beberapa fungsi aktivasi populer yang sering kita temukan:
*   **Sigmoid:** Mengompres nilai output ke rentang antara 0 sampai 1. Bagus untuk klasifikasi probabilitas biner, tapi punya kelemahan fatal bernama *vanishing gradient* kalau jaringannya terlalu dalam (gradiennya mendekati nol sehingga bobot berhenti belajar).
*   **Tanh (Hyperbolic Tangent):** Mirip sigmoid, tapi rentang nilainya dari -1 sampai 1. *Zero-centered*, lebih stabil dibanding sigmoid, tapi tetap rentan terhadap isu *vanishing gradient*.
*   **ReLU (Rectified Linear Unit):** Aturannya paling sederhana dari semua fungsi aktivasi: kalau nilainya negatif, jadikan nol, kalau positif biarkan apa adanya. Murah secara komputasi, dan itu sebabnya jadi pilihan default di hampir semua model modern.

Jaringan saraf utuh dibangun dari tiga jenis lapisan:
1.  *Input Layer:* Lapisan penerima data mentah.
2.  *Hidden Layer(s):* Lapisan tersembunyi tempat transformasi representasi non-linear terjadi. Semakin banyak lapisan dan neuronnya, semakin tinggi kapasitas jaringan memetakan fungsi yang luar biasa kompleks.
3.  *Output Layer:* Lapisan akhir yang memuntahkan hasil prediksi, baik berupa probabilitas klasifikasi (menggunakan fungsi aktivasi *Softmax*) maupun angka kontinu untuk regresi.

Bagaimana jaringan ini belajar? Prosesnya terjadi lewat tarian siklus yang terus berulang:
*   **Forward Propagation:** Data masukan mengalir dari *input layer*, melintasi *hidden layers*, hingga menghasilkan nilai prediksi di *output layer*. Prediksi ini kemudian dibandingkan dengan nilai target aktual menggunakan *loss function* (fungsi kerugian) untuk menghitung seberapa besar eror yang terjadi.
*   **Backpropagation:** Sinyal eror dari *loss function* dialirkan mundur dari lapisan output kembali ke lapisan awal. Di sini matematikanya kerja: eror itu diurai mundur lapis demi lapis buat tahu bobot mana yang paling bertanggung jawab, lalu bobot itu digeser sedikit ke arah yang bikin eror mengecil. Nilai gradien ini dipakai oleh algoritma optimasi, biasanya *Gradient Descent* atau variannya seperti Adam (*Adaptive Moment Estimation*), untuk memperbarui bobot agar pada putaran berikutnya nilai eror semakin mengecil.

---

## Seni Menjinakkan Model: Hyperparameter, Overfitting, dan Kotak Hitam

Melatih *Deep Learning* itu lebih mirip seni memasak daripada sekadar menjalankan skrip Python. Lo nggak bisa cuma melepas data ke algoritma lalu berharap hasilnya langsung sempurna. Ada sekumpulan setelan manual di luar bobot internal yang harus diatur oleh kita sebagai praktisi, yang disebut *hyperparameters*:

*   **Learning Rate:** Ukuran langkah yang diambil algoritma saat menuruni lereng gradien demi mencari titik minimum fungsi *loss*. Kalau *learning rate* disetel terlalu besar, proses belajar bakal liar, melompat-lompat melewati titik optimal, bahkan bisa divergen. Sebaliknya, kalau disetel terlalu kecil, proses *training* bakal berjalan sangat lambat kayak siput atau terjebak selamanya di titik *local minima*.
*   **Batch Size:** Jumlah sampel data yang diproses oleh jaringan dalam satu siklus propagasi maju dan mundur sebelum bobot diperbarui. Ukuran *batch* yang kecil memberikan efek regulasi acak yang membantu generalisasi, sementara ukuran *batch* besar memanfaatkan komputasi paralel GPU secara efisien.
*   **Epoch:** Satu siklus penuh di mana seluruh sampel dalam *dataset training* telah dilewatkan maju dan mundur ke dalam jaringan saraf sebanyak satu kali.

Dua momok terbesar dalam melatih model *Deep Learning* adalah *underfitting* dan *overfitting*. *Underfitting* terjadi saat model terlalu dungu untuk menangkap pola dasar data (biasanya karena jaringannya terlalu dangkal atau durasi latihannya kurang). 

Namun, yang jauh lebih sering terjadi di lapangan adalah *overfitting*: model terlalu pintar menghafal setiap baris data latihan sampai ke derau-derau (*noise*) terkecilnya. Di data latihan akurasinya nyaris 100%, tapi begitu diuji dengan data baru yang belum pernah dilihat sebelumnya di dunia nyata, prediksinya hancur total.

Selain *overfitting*, ada satu konsekuensi etis dan operasional yang sangat krusial: sifat *black box*. 

Model *Deep Learning* bisa memiliki jutaan hingga ratusan miliar parameter bobot. Ketika model memutuskan bahwa sebuah proposal aset properti di koridor TB Simatupang nilainya diprediksi anjlok 30% tahun depan, kita nggak bisa dengan mudah menarik garis lurus dan bilang, "Oh, variabel A yang bikin nilainya turun." Kita cuma tahu inputnya apa dan outputnya apa; logika internal di dalam lapisan tersembunyinya luar biasa rumit untuk dijelaskan ke komite direksi atau auditor perbankan.

---

## Mengenal Sang Bintang: Arsitektur Utama Deep Learning

Nggak semua masalah diselesaikan dengan jenis jaringan saraf yang sama. Selama dua dekade terakhir, evolusi arsitektur *Deep Learning* melahirkan spesialisasi yang luar biasa:

### 1. Convolutional Neural Networks (CNN)
CNN adalah raja dalam domain *Computer Vision*. CNN dirancang untuk mengolah data yang memiliki struktur kisi spasial (*spatial grid*), seperti citra visual. Inti dari CNN adalah operasi konvolusi: menggunakan matriks kecil bernama *filter* atau *kernel* yang bergeser di atas piksel gambar untuk mendeteksi fitur lokal secara invarian terhadap posisi. 

Di industri properti, arsitektur ini yang dipakai kalau kita mau memproses ribuan foto kondisi fisik bangunan untuk mendeteksi retak struktural beton secara otomatis, atau menganalisis citra satelit untuk memetakan pertumbuhan kawasan hijau perkotaan.

### 2. Recurrent Neural Networks (RNN) dan LSTM
CNN jago melihat ruang spasial, tapi payah dalam memahami urutan waktu (*sequential data*). Untuk data yang memiliki ketergantungan temporal seperti runtun waktu (*time series*) harga sewa kantor atau untaian kata dalam kalimat, kita butuh RNN. RNN punya semacam lup internal yang bikin informasi dari langkah waktu sebelumnya disimpan sebagai memori buat memproses langkah waktu yang sekarang.

Kelemahan RNN klasik adalah memorinya sangat pendek karena masalah *vanishing gradient*. Untuk mengatasi ini, lahirlah varian seperti *Long Short-Term Memory* (LSTM) dan *Gated Recurrent Unit* (GRU). LSTM memiliki gerbang khusus (*forget gate*, *input gate*, *output gate*) yang secara selektif mengatur informasi mana yang perlu diingat, diperbarui, atau dibuang sepanjang rentang waktu yang panjang.

### 3. Transformers dan Mekanisme Attention
Sejak makalah legendaris *"Attention Is All You Need"* dirilis pada 2017, arsitektur *Transformer* menggeser dominasi RNN di ranah pemrosesan bahasa alami (*Natural Language Processing* / NLP). Transformer membuang mekanisme pemrosesan sekuensial yang lambat dan menggantinya dengan mekanisme *Self-Attention*. 

Dengan *Self-Attention*, model bisa melihat seluruh kata dalam satu dokumen secara simultan (*parallel processing*) dan menghitung seberapa kuat hubungan antar-kata tanpa memedulikan jarak posisinya di dalam teks. Inilah fondasi utama yang melahirkan model bahasa raksasa (*Large Language Models* / LLM) seperti GPT yang mendasari ChatGPT, Claude, dan sejenisnya.

### Ragam Terobosan Lainnya
Kekuatan *Deep Learning* nggak berhenti di analisis teks dan gambar. Arsitektur generatif seperti *Generative Adversarial Networks* (GAN) dan model difusi (*diffusion models*) merevolusi pembuatan gambar fotorealistis dan desain arsitektur sintetis. Di bidang sains fundamental, model seperti *AlphaFold* berhasil memecahkan teka-teki pelipatan struktur tiga dimensi protein yang membingungkan biolog selama setengah abad. Di jalan raya, sistem persepsi kendaraan otonom memadukan CNN dan Transformer untuk membaca rambu, mendeteksi pejalan kaki, dan mengambil keputusan dalam hitungan milidetik.

---

## Realitas Lapangan: Kapan Kita Butuh Deep Learning, Kapan Cukup Regresi Sederhana?

Kembali ke kekacauan di lantai 28. Setelah Vina selesai membanggakan ide liarnya, gue mengajak dia duduk di dekat meja Aris. Gue minta Aris membuka salah satu *folder dataset* yang selama ini dipakai tim valuasi gue.

"Aris, coba buka rekapitulasi data transaksi ruko komersial Jakarta Selatan yang kemarin lo beresin," pinta gue.

Aris membuka berkas tersebut di layar monitornya. Totalnya cuma ada 420 baris data. Dari 420 baris itu, kolom luas bangunan terisi lengkap, tapi kolom harga sewa historis bolong-bolong di 35% baris, deskripsi kondisi fisik cuma ditulis manual dengan singkatan-singkatan informal yang nggak baku, dan sistem lama kita sama sekali nggak punya repositori foto terstruktur dengan resolusi tinggi.

Gue menoleh ke arah Vina yang mulai mengerutkan kening.

"Vin, *Deep Learning* itu ibarat mesin roket luar angkasa. Mesin roket butuh bahan bakar berton-ton dan landasan peluncuran yang kokoh. Kalau bahan bakar lo cuma solar sisa setengah jeriken dan landasan lo tanah becek, roketnya nggak bakal terbang; meledak di tempat iya."

Tabel perbandingan mental ini yang selalu gue pegang saat mengevaluasi kelayakan proyek data:

| Dimensi Evaluasi | Machine Learning Tradisional | Deep Learning |
| :--- | :--- | :--- |
| **Volume Data** | Efektif pada data kecil hingga menengah (ratusan hingga puluhan ribu baris). | Membutuhkan data raksasa (ratusan ribu hingga jutaan sampel) agar tidak *overfitting*. |
| **Tipe Data** | Sangat unggul untuk data tabular (*spreadsheet*, relasional *database*). | Sangat unggul untuk data tidak terstruktur (citra, audio, video, teks bebas). |
| **Kebutuhan Komputasi** | Cukup dijalankan di CPU laptop standar dalam hitungan detik/menit. | Memerlukan klaster GPU berkemampuan tinggi dengan waktu komputasi berjam-jam/berhari-hari. |
| **Feature Engineering** | Memerlukan intuisi domain dan rekayasa fitur manual secara teliti. | Fitur diekstraksi secara otomatis oleh lapisan jaringan (*end-to-end*). |
| **Interpretabilitas** | Cenderung transparan (*white/grey-box*), mudah diinspeksi signifikansi variabelnya. | Cenderung *black-box*, sangat sulit menelusuri rantai penalaran matematis internalnya. |

Kalau kita memaksakan model *Deep Learning* untuk memprediksi harga sewa pada 420 baris data tabel milik tim Aris, hasilnya dijamin dua hal: kalau nggak *overfitting* parah sampai prediksinya ngawur total, ya proses latihannya bakal gagal konvergen. 

Untuk data tabular berukuran kecil-menengah yang rapi, algoritma pohon keputusan seperti *XGBoost* atau *LightGBM*, bahkan regresi multivariat sederhana yang diperkuat dengan pemahaman bisnis (*domain knowledge*), hampir selalu mengalahkan performa *Deep Learning*. Selain jauh lebih murah biaya komputasinya, kita bisa menjelaskan koefisien bobotnya secara transparan ke hadapan klien korporat tanpa harus berlindung di balik alasan "mesinnya memproses secara misterius".

Vina terdiam beberapa detik, menatap angka-angka di monitor Aris yang masih berantakan akibat migrasi *cloud* darurat akhir pekan kemarin.

"Jadi... kita nggak bisa pasang model kayak ChatGPT buat valuasi ruko minggu depan?" tanyanya dengan nada suara yang turun beberapa oktaf, mulai kehilangan arogansi awalnya.

"Bisa aja kalau lo mau kantor kita dituntut klien gara-gara salah hitung aset miliaran rupiah," sahut gue sambil tersenyum tipis. "Langkah pertama kita bukan sewa server GPU mahal buat gaya-gayaan *Deep Learning*, Vin. Langkah pertama kita adalah bantu Aris nambal pipa data yang bocor gara-gara ruang *server* digusur, rapihin kamus data, baru kita bangun model prediktif berbasis *Machine Learning* yang memang masuk akal buat ukuran portofolio kita saat ini."

Vina menghela napas panjang, lalu pamit kembali ke mejanya untuk merevisi surel klarifikasi ke calon klien sebelum janji manisnya terlanjur jadi komitmen kontrak legal.

---

## Menurut Lo Gimana?

Melihat fenomena di kantor gue hari ini dan membedah materi *Deep Learning* di kelas minggu ini, ada beberapa dilema yang bikin gue terus kepikiran:

1. Di tengah gelombang euforia korporasi yang menuntut serba *Generative AI* dan *Deep Learning*, bagaimana lo merumuskan kerangka kerja (*framework*) penilaian kelayakan yang objektif untuk menentukan kapan sebuah masalah bisnis memang membutuhkan arsitektur *Deep Learning*, dan kapan cukup diselesaikan dengan algoritma *Machine Learning* klasik atau otomasi berbasis aturan?
2. Karakteristik *black box* pada model *Deep Learning* sering kali menjadi penghalang adopsi pada industri yang diregulasi ketat seperti keuangan, valuasi properti, atau layanan kesehatan. Dari perspektif manajemen sistem informasi, bagaimana organisasi seharusnya menyikapi kompromi (*trade-off*) antara tingginya akurasi prediksi model kompleks versus kebutuhan transparansi (*explainability*) bagi pemangku kepentingan?
3. Banyak arsitektur mutakhir seperti *Transformers* membutuhkan biaya komputasi, konsumsi energi, dan volume data yang luar biasa besar untuk proses pelatihannya. Menurut lo, apakah tren ketergantungan pada model raksasa ini sehat untuk keberlanjutan inovasi teknologi jangka panjang, atau justru bakal memicu monopoli baru yang hanya bisa dimainkan oleh segelintir korporasi teknologi raksasa berdana tak terbatas?

Debu gipsum di lantai 28 tampaknya baru bakal benar-benar reda menjelang tengah malam nanti, beriringan dengan Aris yang akhirnya berhasil memulihkan replikasi basis data cadangan ke klaster baru.

Sampai ketemu di diskusi catatan berikutnya.

Nik
