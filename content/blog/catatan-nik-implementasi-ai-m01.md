---
title: "Catatan Nik: Ketika Aturan Kaku Jebol dan Mesin Mulai Belajar Sendiri"
subtitle: "Warisan Bram berupa spreadsheet 50 ribu baris itu sebenernya sistem pakar yang udah usang. Semalem dosen gue ngejelasin kenapa dia nggak akan sanggup nanganin satu perubahan pasar aja."
type: blog
date: 2026-10-06T05:00:00+07:00
draft: true
ws_chat: 1539
ws_msg: 21358
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "implementasi-artificial-intelligence"]
summary: "Dari rule-based yang rapuh ke tiga cara mesin belajar: spreadsheet Bram jebol bukan karena error, tapi karena jaman udah bergeser dan sistem itu nggak bisa ikut bergeser."
hook: "Sistem kantor Nik jebol bukan karena error, tapi karena aturan kaku nggak sanggup nampung kenyataan lapangan."
---

Bogor lagi diguyur hujan deras dari sore tadi, Sar. Tipe hujan lebat yang bikin kaca jendela kamar kerja gue berembun tebal, ditemani suara tempias air yang konstan banget menghantam atap. Dylan udah balik ke asramanya sejak Minggu sore kemarin, jadi begitu rumah mendadak hening, yang tersisa cuma dengung mesin kopi, tumpukan dokumen sewa komersial SCBD di laptop kantor, dan materi kuliah perdana *Implementation of Artificial Intelligence* yang semalam kita bahas sepintas di telepon.

Gue beneran kepikiran obrolan kita soal gimana kampus lo dan kampus gue membawakan mata kuliah ini. Dosen gue langsung tancap gas ngebongkar fondasi paling mendasar: apa sih yang bikin sebuah sistem itu beneran layak disebut *intelligent*, dan kenapa dunia korporat sekarang lagi kebakaran jenggot mencoba membedakan mana sistem yang beneran "cerdas" versus mana yang cuma sekadar kalkulator canggih berkamuflase.

Sambil dengerin rekaman kuliah, gue gak bisa berhenti mikirin kekacauan di divisi gue pasca Bram cabut dua minggu lalu. Kepergian Bram beneran ninggalin lubang gede, bukan cuma karena posisi *Senior Director* itu krusial, tapi karena dia ninggalin warisan sistem kerja yang bikin gue elus dada: sebuah *spreadsheet* legendaris berisi puluhan ribu baris data prospek penyewa gedung perkantoran, yang dikunci rapat pakai logika aturan manual super rumit. Dan di sinilah letak relevansi brutal materi IAI pertemuan pertama ini sama realitas hidup kita di kantor.

---

## AI Bukan Sihir: Dari *Rule-Based* yang Rapuh Menuju Mesin yang Belajar Sendiri

Dosen gue buka sesi dengan satu definisi tegas yang menurut gue perlu kita garis bawahi bareng: *Artificial Intelligence* pada dasarnya adalah cabang ilmu komputer yang bertujuan bikin mesin mampu mengeksekusi tugas-tugas yang biasanya memerlukan kecerdasan manusia. Tapi kuncinya bukan di kata "meniru manusia" secara visual atau gaya-gayaan robotik, melainkan pada tiga pilar kognitif: kemampuan untuk belajar (*learning*), menalar (*reasoning*), dan memperbaiki diri secara mandiri (*self-correction*).

Yang paling membuka mata adalah ketika kita membedah evolusinya, Sar. Dulu, era AI klasik sangat didominasi oleh pendekatan simbolik alias *expert systems*. Mesin itu pintar cuma karena ada sekumpulan pakar manusia yang mendiktekan aturan secara eksplisit lewat logika formal: *IF-THEN* atau "JIKA-MAKA".

```
JIKA: Klien = Perusahaan Multinasional
DAN: Kebutuhan Luas Ruang > 2.000 m²
DAN: Budget Sewa > USD 30 / m² / bulan
MAKA: Kategori = Hot Prospect (Prioritas Tier 1)
```

Sistem berbasis aturan (*rule-based*) kayak begini memang punya kelebihan telak: sangat mudah dipahami (*interpretable*), transparan, dan gak bikin manajemen paranoid karena setiap keputusan ada jejak logikanya yang terang benderang. Tapi kelemahannya fatal banget: sistem ini luar biasa kaku (*rigid*) dan sangat rapuh (*brittle*). Begitu lingkungan bisnis berubah sedikit aja di luar skenario yang ditulis si pembuat aturan, sistemnya langsung lumpuh atau ngasih output yang ngaco.

Persis ini yang terjadi di kantor gue sekarang. Sistem *scoring* prospek peninggalan Bram itu murni sistem pakar berbasis aturan kaku. Waktu ekonomi stabil dan pola okupansi kantor masih konvensional, rumus *IF-THEN* bikinan dia keliatan jenius. Tapi pasca tren kerja *hybrid* meledak dan lanskap bisnis bergeser, puluhan rumus itu jadi sampah. Ada *startup fintech* unicorn yang secara formal gak masuk kriteria Bram karena umur perusahaannya masih muda, tapi kemampuan bayar mereka gila-gilaan. Sistem Bram menolak mereka, ngasih skor rendah, dan akhirnya mereka malah sewa lima lantai di gedung kompetitor kita lewat agen lain. Manajemen mencak-mencak, dan tim analis cuma bisa bengong sambil bilang, *"Tapi rumusnya memang bilang begitu, Pak."*

Nah, AI modern membalik paradigma itu 180 derajat lewat *Machine Learning* dan *Deep Learning*. Alih-alih manusia yang capek-capek ngetik ratusan aturan kaku, kita membiarkan mesin yang belajar sendiri (*learning from data*). Mesin disodori tumpukan data historis transaksi, karakteristik penyewa, fluktuasi harga sewa, tren makroekonomi, hingga pola perilaku negosiasi. Dari data mentah itulah algoritma secara statistik mengekstraksi pola, membangun model penalaran internalnya sendiri, dan otomatis melakukan koreksi saat tebakannya meleset.

Fleksibilitasnya luar biasa tinggi dan skalabilitasnya eksponensial. Tapi tentu aja ada harganya: model modern ini sering kali berubah jadi *black box*. Mesin bisa memprediksi dengan akurasi 95% bahwa sebuah calon penyewa bakal *default* atau gak memperpanjang kontrak sewa tahun depan, tapi waktu direksi nanya, *"Kenapa mesin lo nyimpulin gitu? Di baris rumus mana dia bilang begitu?"*, kita gak bisa langsung nunjukin satu baris logika *IF-THEN* yang sederhana. Ini dilema tata kelola yang riil banget buat anak sistem informasi kayak kita.

---

## Tiga Mazhab Pembelajaran Mesin: Dari Dikte Guru Sampai Belajar dari Hukuman

Di sesi kedua, materi masuk ke tiga pilar utama cara mesin belajar. Bagian ini bener-bener bikin gue inget sama topik tesis lo dan sistem GPBSales, proyek penjualan buku digital, yang lagi lo oprek, Sar. Dosen gue membaginya jadi tiga mazhab besar:

### 1. *Supervised Learning* (Belajar Berdampingan dengan Kunci Jawaban)

Ini pendekatan paling umum dan paling matang di industri saat ini. Konsep dasarnya sederhana banget: kita ngasih makan algoritma dengan data yang sudah berlabel (*labeled data*). Artinya, ada pasangan antara fitur input (soal) dan target output (kunci jawaban). Mesin bertugas mencari fungsi matematis yang menghubungkan input ke output tersebut, lalu menguji kemampuannya pada data baru yang belum pernah dilihat sebelumnya.

Contoh paling klasiknya ya filter email *spam* di kotak masuk kita. Algoritma dikasih ribuan sampel email yang udah ditandai manual oleh manusia: "ini spam", "ini bukan spam". Dari situ mesin belajar kosakata, struktur kalimat, dan metadata mana yang punya probabilitas tinggi sebagai penipuan.

Nah, ini klop banget sama yang lo kerjain!
- Di **GPBSales**, lo menganalisis tren penjualan buku digital dengan menyodorkan data historis berlabel: variabel kategori, harga, rating, jumlah ulasan, dan volume pembelian harian. Mesin belajar memetakan korelasi fitur-fitur itu ke angka nominal penjualan (*regression problem*).
- Di **tesis lo soal analisis sentimen**, itu murni *Supervised Learning* untuk pemrosesan bahasa alami (*Natural Language Processing* / NLP). Lo punya ribuan baris teks ulasan pengguna yang udah dikasih label sentimen: positif, negatif, atau netral. Model lo bakal belajar membedakan semantik dan bobot kata untuk menentukan sentimen ulasan baru yang masuk tanpa bantuan manusia lagi.

Tantangan terbesarnya apa? *Labeling* itu mahal, makan waktu, dan rawan bias manusia. Kalau orang yang ngasih label awal udah punya persepsi melenceng, mesin lo bakal belajar jadi sistem yang ikutan melenceng dengan sangat percaya diri (*garbage in, garbage out*).

### 2. *Unsupervised Learning* (Menemukan Pola Tersembunyi Tanpa Contekan)

Gimana kalau kita punya gunung data tapi sama sekali gak punya label target? Gak ada kunci jawaban. Gak ada yang ngasih tahu baris mana yang bener atau salah. Di sinilah *Unsupervised Learning* unjuk gigi. Tugas mesin murni mencari struktur alami, korelasi tersembunyi, atau anomali di dalam kumpulan data tersebut (*finding hidden patterns*).

Bentuk paling populernya adalah segmentasi pelanggan (*clustering*). Di kantor gue misalnya, kita punya ribuan data riwayat interaksi klien korporat: frekuensi mereka minta jadwal *viewing*, durasi negosiasi draf kontrak, sensitivitas mereka terhadap kenaikan *service charge*, jam operasional kantor mereka, sampai preferensi sertifikasi bangunan hijau (*ESG compliance*). 

Gue gak tahu ada berapa jenis profil penyewa di Jakarta pasca-pandemi ini secara pasti. Tapi dengan algoritma *clustering*, mesin bisa mengelompokkan data itu sendiri menjadi beberapa kluster unik:
- Kluster A: Korporat multinasional konservatif yang gak peduli harga sewa mahal asal gedung punya sertifikasi *green building* platinum.
- Kluster B: Perusahaan lokal berkembang pesat yang sangat sensitif harga dan cuma butuh ruang fleksibel jangka pendek.
- Kluster C: Institusi finansial yang menuntut infrastruktur keamanan data ekstra ketat tanpa kompromi.

Mesin gak ngasih tahu kita nama kluster-kluster itu; mesin cuma ngelompokin berdasarkan kedekatan matematis titik data. Manajer pemasaran kayak gue yang kemudian harus menafsirkan maknanya dan merancang strategi penawaran yang pas untuk tiap kelompok.

### 3. *Reinforcement Learning* (Belajar Mandiri Lewat Coba-Coba dan Konsekuensi)

Ini mazhab yang paling liar sekaligus menarik. Gak ada data berlabel statis kayak di *supervised*, dan bukan sekadar memetakan kluster kayak di *unsupervised*. Di sini, kita menciptakan sebuah entitas otonom yang disebut agen (*agent*). Si agen ditaruh di dalam sebuah lingkungan tertentu (*environment*), dan dia bebas mengambil tindakan (*action*).

Tiap kali tindakan yang dia ambil mendekatkan dia ke tujuan akhir, lingkungan bakal ngasih dia *reward* (hadiah/skor positif). Sebaliknya, kalau tindakannya salah atau bikin celaka, dia dapet *penalty* (hukuman/skor negatif). Melalui jutaan siklus uji coba (*trial and error*), agen ini belajar merumuskan strategi optimal (*policy*) untuk memaksimalkan total *reward* jangka panjang.

Contoh paling gamblang ya AI yang jago main catur atau Go, di mana algoritma mengalahkan juara dunia bukan karena diajarin taktik pembukaan catur oleh manusia, melainkan karena dia bertanding melawan dirinya sendiri jutaan kali dan belajar dari tiap kekalahan. 

Di ranah bisnis nyata, konsep ini mulai diadopsi buat algoritma *dynamic pricing*. Bayangkan sebuah sistem otomatis yang mengelola harga sewa ruang ritel di lobi gedung perkantoran SCBD secara harian atau mingguan. Sistem menaikkan atau menurunkan harga berdasarkan okupansi, trafik pengunjung, dan musim. Kalau sistem menaikkan harga terlalu tinggi dan ruangannya kosong berbulan-bulan, dia kena penalti finansial. Kalau dia pasang harga terlalu murah, ruangannya laku tapi margin labanya tipis, reward-nya kecil. Lama-lama, sistem itu nemuin titik keseimbangan harga sewa paling optimal yang gak pernah terpikirkan oleh tim manajemen konvensional.

---

## Dilema *Black Box* dan Ujian Manajemen yang Sesungguhnya

Sepanjang kuliah tadi, gue nyadar satu hal penting yang bikin gue makin yakin kenapa kita ngambil S2 Manajemen Sistem Informasi, bukan murni ilmu komputer murni. 

Tantangan terbesar implementasi AI di perusahaan saat ini bukan lagi sekadar nulis kode program atau milih algoritma paling mutakhir. *Tools* pemodelan sekarang udah semakin terdemokratisasi; lo bisa panggil pustaka *machine learning* cuma dengan beberapa baris kode Python. Ujian sesungguhnya ada di level manajemen: **kepercayaan, etika, dan tata kelola**.

Waktu AI klasik (*expert systems*) gagal di divisi gue setelah Bram pergi, tim gue panik karena ternyata aturan manual itu rapuh. Tapi pas gue lontarkan ide ke manajemen buat mulai migrasi ke model prediktif berbasis *Machine Learning* untuk menganalisis risiko penyewa mangkir bayar, respons manajemen level atas malah skeptis. Bos gue yang baru nyeletuk santai di ruang rapat kemarin:

*"Nik, kalau mesin lo bilang kita harus nolak perpanjangan kontrak sewa satu lantai dari klien X yang udah lima tahun di sini, gue butuh alasan legal dan bisnis yang masuk akal buat dipresentasikan ke dewan komisaris. Gue gak bisa bilang ke pemilik gedung kalau keputusan ini diambil gara-gara algoritma neural network lo nemuin korelasi matematis abstrak yang lo sendiri gak bisa jelasin kalimat sebab-akibatnya."*

*Deg.* Di situ gue terdiam. Dosen IAI gue tadi malam ngomong hal yang persis sama: semakin tinggi akurasi dan fleksibilitas model AI modern (terutama *Deep Learning*), tingkat keterpahamannya (*interpretability*) sering kali berbanding terbalik. Mesin menjadi *black box*. 

Ini ironi manajemen modern. Kita pengen sistem yang pintar, adaptif, dan mampu mengolah miliaran parameter liar yang otak manusia gak sanggup proses. Tapi di sisi lain, tata kelola korporat menuntut transparansi, kepatuhan audit, dan akuntabilitas hukum. Kalau ada keputusan bisnis bernilai miliaran rupiah yang salah langkah gara-gara rekomendasi AI, siapa yang bakal diseret ke ruang sidang? Data scientist-nya? Algoritmanya? Atau manajer yang menelan mentah-mentah rekomendasi mesin tanpa menalar ulang?

Aplikasi AI sekarang memang udah merambah ke mana-mana, dari *computer vision* buat mendeteksi kerusakan struktural gedung lewat drone, NLP buat bedah ribuan halaman klausul kontrak komersial secara kilat, sampai sistem rekomendasi yang lo bikin di GPBSales. Tapi batas antara efisiensi brilian dan malapetaka bisnis ternyata tipis banget kalau kita gak ngerti arsitektur pembelajaran di balik mesin tersebut.

---

## Giliran Lo yang Bongkar Otak Gue

Materi pertemuan pertama ini jujur bikin kepala gue berdengung, tapi sekaligus bikin gue luar biasa antusias. Dari penjelasan dosen gue tadi malam ditambah komparasi sama studi kasus di kantor gue dan proyek tesis lo, gue mau ngelempar beberapa hal krusial buat lo bedah. Gue beneran butuh kacamata analisa lo buat beberapa pertanyaan ini:

1. **Trade-off Transparansi vs Performa:** Di industri dengan risiko finansial dan kepatuhan hukum yang luar biasa tinggi kayak investasi properti komersial atau analisis risiko kredit perbankan, sejauh mana batas toleransi manajemen bisa mengorbankan transparansi (*explainability*) demi mengejar akurasi prediksi model *Machine Learning* yang bersifat *black box*? Kalau lo jadi pembuat keputusan, kapan lo bakal tetap bertahan pakai sistem pakar berbasis aturan kaku, dan kapan lo berani memaksa organisasi migrasi total ke model pembelajaran mesin otonom?

2. **Tantangan Metodologis Supervised Learning:** Lo kan lagi mendalami *Supervised Learning* buat analisis sentimen di tesis dan tren penjualan di GPBSales. Masalah terbesar pendekatan ini ada pada ketergantungan mutlak terhadap kualitas data berlabel historis. Pertanyaan gue: gimana cara sistem lo mendeteksi dan memitigasi risiko *concept drift* alias pergeseran konteks dunia nyata? Misalnya ketika istilah slang baru di media sosial membalikkan arti sebuah kalimat ulasan, atau ketika pola penjualan buku tiba-tiba berubah drastis bukan karena kategori atau harganya, melainkan karena satu judul yang viral di media sosial, hal yang belum pernah terekam di data historis sebelumnya?

3. **Manajemen Perubahan Budaya Organisasi:** Belajar dari kasus kantor gue pasca Bram cabut, resistensi terbesar transisi dari *rule-based* ke data-driven AI ternyata bukan pada teknologinya, melainkan pada ego manusia yang udah bertahun-tahun merasa intuisinya paling benar. Menurut analisa lo dari sudut pandang tata kelola sistem informasi, langkah strategis apa yang harus disiapkan oleh manajemen puncak agar tim operasional gak sekadar "patuh buta" pada output algoritma AI, tapi juga gak resisten menolak sistem cerdas baru yang meruntuhkan aturan-aturan lama mereka?

Hujan di luar makin awet nih, Sar. Kopi gue udah tandas dari setengah jam lalu, dan gue mau lanjut ngerapihin log variabel buat tugas kelompok minggu depan. Tulis pemikiran lo sejelas mungkin ya di catatan lo berikutnya. Gue pengen lihat gimana lo membedah kekacauan ini dari sudut pandang kampus lo.

Warmest hug from the rainy city 🩷  
Nik
