---
title: 'Catatan Nik: Spidol Whiteboard Lantai 28, Drama Tulang Ikan, dan Jebakan Angka Pertama'
subtitle: 'Diagram fishbone karya Aris difoto, dihapus sebelum makan siang, dan nggak satu pun dugaan yang diuji: gue baru nyadar bias kognitif kantor itu sistemik.'
type: blog
date: 2026-11-02T05:00:00+07:00
draft: true
ws_chat: 1653
ws_msg: 21712
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "analisa-dan-desain-smart-system", "catatan-nik"]
summary: 'Materi pekan ini soal bias kognitif, diagram fishbone, dan ketidakpastian aleatorik vs epistemik. Di kantor gue, rapat akar masalah berakhir dengan diagram yang jadi lampiran audit dan satu angka jangkar yang nggak pernah diuji.'
hook: 'Pernah nggak lo ikut rapat yang kata manajemennya "cari akar masalahnya", tapi sejam kemarin semuanya udah sepakat pake feeling orang paling senior dan diagramnya dihapus sebelum makan siang?'
---

Tiga spidol *boardmarker* beda warna tergeletak berantakan di atas meja rapat lantai 28. Di papan tulis kaca sepanjang empat meter, ada gambar kerangka ikan raksasa yang digambar Aris dengan sangat rapi sampai garis tulang cabangnya pakai penggaris lipat.

Di bagian kepala ikan, tertulis kalimat tebal pakai spidol hitam: *Tingkat Adopsi Portal Valuasi Komersial Drop 41%*. 

Di tulang-tulangnya, Aris memetakan kategori *6M* dengan sangat teliti. Ada tumpukan catatan kecil di cabang *Machine* soal latensi API, di cabang *Method* soal alur kurasi properti yang berbelit, sampai ke cabang *People* soal kebiasaan tim penilai senior yang masih hobi simpan catatan di map manual peninggalan era Bram dulu.

Rapat evaluasi itu berlangsung dua jam. Manajemen puncak minta peta akar masalah demi kelengkapan berkas audit proyek sistem cerdas yang kami kembangkan. Tapi tahu nggak apa yang terjadi di menit ke sembilan puluh? 

Vina tiba-tiba mengetuk meja dua kali dengan pulpennya, lalu bilang dengan nada paling percaya diri sedunia, "Menurut *gut feeling* gue, masalah utamanya tetap di edukasi pengguna. Target konversi kita kan dari awal harusnya bisa tembus 85 persen. Sayang banget kalau proyek sebesar ini dievaluasi ulang, modal dan waktu yang jalan udah terlalu banyak. Jadi diagram di papan tulis ini kita foto aja, jadikan *Appendix C* di laporan akhir, terus kita fokus bikin kampanye promo fitur baru."

Semua orang di ruangan itu mengangguk. Diagram karya Aris difoto lewat ponsel, dihapus sampai bersih sebelum jam makan siang, dan proyek jalan terus tanpa satu pun tulang dugaan di papan itu pernah diuji lewat data. Angka 85 persen yang dilempar Vina tanpa dasar itu seketika jadi patokan suci semua orang di ruangan.

Gue cuma bisa menatap remah-remah penghapus papan tulis di karpet sambil teringat materi kuliah *Smart System Analysis and Design* di kelas gue kemarin. Kita sering banget terjebak bikin formalitas analisis, padahal otak kita sendiri sedang disandera oleh bias kognitif yang parah.

---

## Ilusi Otak Cepat dan Jebakan Berpikir Analis

Di bahan kajian buat pekan ini di kelas gue, ada bahasan mendasar soal cara kerja kognisi manusia dari Daniel Kahneman yang pas banget menampar kejadian tadi siang.

Otak kita punya dua mode operasional:

* **Sistem 1:** Cepat, otomatis, emosional, dan sangat hemat energi. Sistem ini bekerja tanpa lo minta, langsung mengambil kesimpulan kilat berdasarkan pola masa lalu yang paling gampang diingat.
* **Sistem 2:** Lambat, sadar, analitis, dan butuh banyak energi mental. Ini mode yang dipakai waktu kita menghitung statistik rumit, membandingkan distribusi data, atau memeriksa korelasi palsu.

Masalah terbesarnya adalah Sistem 2 itu malas. Dia gampang capek dan gampang menyerah. Kerap kali, keputusan bisnis atau arsitektur sistem diambil secara impulsif oleh Sistem 1, lalu Sistem 2 dipanggil belakangan cuma buat jadi pengacara pembela: mencari-cari pembenaran logis, bikin grafik yang mendukung, dan merapikan data biar kelihatan ilmiah.

Sebagai analis sistem cerdas, kita nggak kebal dari ilusi ini. Saat merancang sistem cerdas, bias manusia yang nggak disadari bakal langsung bocor ke dalam pemilihan fitur, cara kita merumuskan masalah, sampai cara kita menafsirkan *output* model.

Ada sepuluh bias kognitif yang paling sering merusak perancangan sistem cerdas:

1. **Anchoring.** Angka atau informasi pertama yang didengar langsung jadi jangkar yang mengunci seluruh diskusi. Begitu Vina nyebut "target 85 persen", kepala semua orang langsung berputar di sekitar angka itu, padahal *baseline* riil sistem penilai kami sebelum otomatisasi cuma ada di angka 58 persen.
2. **Availability Bias.** Kita menilai frekuensi sesuatu berdasarkan seberapa gampang hal itu melintas di ingatan kita. Kegagalan sistem server yang sempat viral di grup WhatsApp kantor terasa seperti masalah harian, padahal secara log sistem cuma terjadi sekali dalam enam bulan.
3. **Confirmation Bias.** Kebiasaan cuma mencari bukti yang membuktikan dugaan awal kita, sambil menutup mata rapat-rapat dari data yang membantahnya. Analis sering cuma memasukkan variabel yang "terasa masuk akal" ke dalam model dan membuang variabel anomali yang justru menyimpan pola penting.
4. **Overconfidence dan Kalibrasi.** Rentang keyakinan kita terlalu sempit. Tim sering bilang dengan enteng, "Proyeksi transaksi properti bulan depan pasti di kisaran 1.200 unit." Padahal varians aslinya bisa merentang lebar dari 500 sampai 2.100 unit. Model prediktif yang kita latih pun bisa tertular penyakit ini, mengeluarkan nilai probabilitas 0,96 padahal akurasi aslinya di lapangan cuma 65 persen.
5. **Framing Effect.** Keputusan kita berubah cuma gara-gara cara penyampaian. Kalimat "Sistem rekomendasi ini punya peluang berhasil 75 persen" kedengaran jauh lebih menarik di depan direksi daripada "Sistem ini punya risiko salah prediksi sebesar 25 persen", padahal nilai faktualnya identik.
6. **Sunk Cost Fallacy.** Mempertahankan proyek yang salah arah cuma karena anggaran sudah cair separuh dan tim sudah begadang berminggu-minggu. Ini yang tadi siang bikin Vina menolak evaluasi akar masalah: rasa sayang pada modal yang sudah terlanjur hangus.
7. **Survivorship Bias.** Cuma menganalisis entitas yang sukses bertahan. Di kantor gue, tim sering cuma membedah profil agen properti yang berhasil menutup transaksi bernilai raksasa, sementara ratusan transaksi yang gagal di tengah jalan nggak pernah disentuh datanya. Padahal resep kegagalan sistem justru ada di tumpukan data yang terabaikan itu.
8. **Base Rate Neglect.** Terlalu fokus pada sinyal spesifik sampai lupa frekuensi dasar di populasi umum. Kalau alat deteksi anomali valuasi punya akurasi 95 persen, tapi anomali riil di pasar properti cuma ada 0,5 persen, sebagian besar alarm yang dibunyikan sistem sebenarnya cuma alarm palsu (*false positive*).
9. **Hindsight Bias.** Begitu sebuah tren terjadi, semua orang mendadak merasa pintar dan bilang, "Tuh kan, dari awal gue juga udah nebak polanya bakal begitu." Efeknya fatal: tim berhenti belajar dari data historis yang objektif dan malah menyusun narasi dongeng masa lalu.
10. **Bias Kelompok (*Groupthink / HiPPO Bias*).** Rapat selalu tunduk pada pendapat orang dengan gaji paling tinggi (*Highest Paid Person's Opinion*). Suara Aris yang membawa data log sistem kalah total oleh kepercayaan diri manajerial yang dominan.

---

## Protokol Menahan Diri: Praktik, Bukan Sekadar Niat Baik

Di kelas, dosen gue menegaskan satu hal penting: kita nggak bisa menghilangkan bias kognitif cuma dengan niat baik atau slogan "mari kita objektif". Bias itu sifatnya sistemik. Satu-satunya cara menahannya adalah dengan membangun protokol kerja yang memaksa otak kita melambat:

* **Tulis hipotesis sebelum buka data.** Catat dugaan awal di lembar kerja terpisah, beri nomor urut, baru setelah itu buka tabel data. Jangan membolak-balik urutannya biar kita nggak mencocok-cocokkan data dengan intuisi sesaat.
* **Jalankan sesi *premortem*.** Sebelum kode pertama ditulis atau sebelum arsitektur sistem disetujui, kumpulkan tim di satu meja. Tanyakan satu hal: "Bayangkan enam bulan dari sekarang sistem cerdas ini gagal total, jadi bahan tertawaan klien, dan bikin kantor rugi. Apa saja penyebab kegagalannya?" Pertanyaan ini langsung membongkar risiko tersembunyi yang biasanya tabu diucapkan saat rapat formal.
* **Cari bukti penyangkal (*disconfirming evidence*).** Wajibkan minimal satu analisis data yang tugasnya murni membantah hipotesis utama. Kalau lo yakin penurunan performa disebabkan oleh fitur baru, cari data yang menunjukkan fitur baru itu justru disukai pengguna.
* **Gunakan *naive baseline* sebagai jangkar pembanding.** Jangan mengagumi model cerdas berakurasi 75 persen sebelum lo bandingkan dengan *baseline* sederhana, misalnya tebakan rata-rata bergerak mingguan. Kalau model machine learning lo cuma menang 2 persen dari tebakan naif, model itu nggak layak dipertahankan.
* **Pisahkan penyusun model dan auditor.** Orang yang merancang logika sistem cerdas nggak boleh jadi orang yang sama dengan yang menguji kelayakannya. Perlu mata orang luar yang nggak punya beban emosional terhadap kode yang ditulis.
* **Tulis rentang, haramkan angka tunggal.** Mulai biasakan menyajikan estimasi dalam format interval kepercayaan, misalnya "penjualan berada di rentang 1.200 sampai 1.600 dengan tingkat kepercayaan 90 persen", bukan "penjualan 1.400".
* **Buat buku catatan keputusan (*decision log*).** Catat apa yang diputuskan, opsi apa yang ditolak, dan asumsi apa yang mendasarinya hari ini. Ini penangkal paling mujarab buat *hindsight bias* tiga bulan ke depan.

---

## Diagram Fishbone: Dari Alat Analisis Jadi Hiasan Rapat

Alat yang tadi pagi digambar Aris di papan tulis lantai 28 sebenarnya adalah diagram *fishbone* alias diagram Ishikawa. Alat ini diciptakan buat satu tujuan: memetakan dugaan rantai kausalitas dari satu masalah spesifik ke dalam kategori-kategori terstruktur.

Masalahnya, banyak organisasi menurunkan derajat alat ini menjadi sekadar karya seni hiasan rapat.

```
       CAUSE                                            EFFECT
  Method             Machine           Man
    \                  \               /
     \                  \             /
      +------------------+-----------+----------> [ Penurunan Adopsi ]
     /                  /             \            [  Sistem 41%     ]
    /                  /               \
  Material       Measurement       Environment
```

Untuk industri manufaktur atau operasional teknis, kategori *6M* (*Man, Machine, Method, Material, Measurement, Mother Nature/Environment*) sering dipakai. Sementara untuk proses layanan atau perancangan sistem informasi, pendekatan *4P* (*People, Process, Policy, Place*) biasanya terasa lebih relevan.

Langkah menyusunnya seharusnya sangat disiplin:

1. **Rumuskan efek secara presisi dan kuantitatif.** Jangan tulis "kinerja portal jelek". Tulis: "Penurunan adopsi portal valuasi komersial sebesar 41% pada kuartal ketiga di kantor cabang Jakarta".
2. **Pilih tulang utama yang masuk akal.** Nggak usah memaksakan harus ada enam kategori kalau memang sistem informasinya cuma bersinggungan dengan empat area utama.
3. **Curah pendapat tanpa sensor.** Masukkan semua kemungkinan penyebab di rantai tulang kecil tanpa menghakimi di awal.
4. **Terapkan teknik *5 Whys*.** Setiap kali satu penyebab muncul di rantai tulang, tanyakan "mengapa" sampai lo menyentuh faktor fundamental yang bisa diintervensi oleh sistem atau kebijakan.
5. **Beri tanda pada dugaan yang bisa diuji data.** Ini garis pemisah antara analis beneran dengan tukang corat-coret. Setiap cabang kecil harus ditandai: apakah dugaan ini bisa divalidasi lewat log aktivitas, data transaksi, atau metrik sistem?
6. **Prioritaskan berdasarkan bukti riil, bukan suara pejabat tertinggi.**

Ingat batasan mutlaknya: **diagram fishbone tidak pernah membuktikan apa pun**. Fishbone hanyalah mesin pembuat hipotesis. Gambar tulang yang lengkap bukan kesimpulan akhir, melainkan daftar pekerjaan rumah untuk tim data. Kalau setelah digambar diagramnya cuma difoto lalu dihapus kayak tadi siang, fishbone itu cuma jadi formalitas birokrasi tanpa nilai analitis.

---

## Menavigasi Ketidakpastian: Aleatorik vs Epistemik

Waktu sebuah sistem cerdas menghasilkan prediksi yang meleset, manajemen sering buru-buru menyimpulkan bahwa datanya kurang banyak. Padahal dalam teori sistem cerdas, ketidakpastian itu terbelah jadi dua jenis yang sifatnya bertolak belakang:

### 1. Ketidakpastian Aleatorik (Keacakan Alami)

Ini adalah ketidakpastian yang melekat pada sifat dunia dan sistem itu sendiri. Sifatnya acak, bising (*noise*), dan **tidak akan pernah bisa dihilangkan** sebanyak apa pun lo menambah volume data atau memperbesar parameter model. 

Contohnya: calon penyewa gedung mana yang mendadak batal survei unit hari ini karena urusan keluarga mendadak, atau fluktuasi menit ke menit dari pengunjung web yang cuma iseng berselancar. Menambah satu juta baris data histori transaksi properti nggak akan pernah bisa menghilangkan keacakan ini. Lo cuma buang-buang komputasi.

### 2. Ketidakpastian Epistemik (Kekurangan Pengetahuan)

Ini adalah ketidakpastian yang muncul murni karena kita belum tahu atau belum mengukur variabel yang relevan. Ketidakpastian ini **bisa dikurangi** secara signifikan dengan cara menambah sampel data yang representatif, memperbaiki instrumen pengukuran, atau memperdalam riset domain. 

Contohnya: kita nggak tahu seberapa besar minat investor asing terhadap gedung ramah lingkungan di koridor Sudirman karena tim pemasaran belum pernah mengumpulkan data segmen tersebut secara terstruktur.

Ketidakpastian di sistem cerdas biasanya bersumber dari beberapa celah:
* Data historis yang bolong, terlambat disetor, atau sengaja dimanipulasi unit kerja demi mengejar KPI.
* Sampel data latih yang timpang dan nggak mewakili populasi pengguna sebenarnya.
* Perubahan perilaku lingkungan setelah model dirilis (*distribution shift*). Misalnya, pola transaksi properti perkantoran yang berubah permanen setelah era kerja hibrida diberlakukan.
* Ketidakkonsistenan penilaian manusia yang dijadikan label dasar (*ground truth*). Waktu Pak Fajar masih aktif memegang alur penagihan, standar pencatatan biaya operasional bisa beda sudut pandang dengan analis junior penggantinya.

Cara mengelola ketidakpastian ini bukan dengan menutup mata dan pura-pura yakin di depan pimpinan. Terapkan langkah teknis berikut:
* Sajikan hasil estimasi sebagai interval probabilitas atau rentang skenario (*worst-case, expected, best-case*).
* Jalankan analisis sensitivitas: goyang asumsi kunci satu per satu untuk melihat seberapa rapuh rekomendasi sistem lo saat kondisi pasar berubah sedikit saja.
* Terapkan pendekatan pembaruan keyakinan (*Bayesian updating*), di mana keyakinan awal model terus disesuaikan secara dinamis setiap kali data faktual baru masuk ke pipa data.
* Siapkan sistem pemantauan distribusi data (*data drift monitoring*) secara berkala untuk mendeteksi kapan model sudah mulai usang dan butuh pelatihan ulang.

---

## Catatan Khusus Buat Tesis Lo: Membedah GPBSales

Membaca materi minggu ini langsung bikin gue kepikiran progres tesis lo, GPBSales, dataset penjualan buku digital lo. 

Kemarin lo sempat cerita di telepon kalau lo lagi pusing melihat pendapatan bersih yang anjlok drastis dibanding bulan sebelumnya, dan proyeksi bulan depan kelihatan cuma separuh dari biasanya. Kecurigaan lo langsung tertuju pada diskon besar-besaran yang lo duga memotong penerimaan bersih per eksemplar.

Jangan buru-buru loncat ke kesimpulan itu dulu, Sar. Jangan sampai lo mengulangi kesalahan rapat lantai 28 tadi siang: mengambil tebakan Sistem 1, lalu mencari algoritma yang cuma membenarkan kecurigaan itu.

Coba lo petakan dulu gejalanya pakai fishbone sebelum lo menyentuh skrip koding lo lagi.

```
                            FISHBONE GPBSALES
        Method                                    Machine
  Strategi Diskon Ekstrem               Algoritma Rekomendasi
  (Potongan terlalu dalam)              (Bias ke buku populer)
            \                                      /
             \                                    /
              +----------------------------------+-------> [ Pendapatan Bersih ]
             /                                    \        [ Turun Tajam       ]
            /                                      \
        Material                               Measurement
  Katalog Judul Baru Lemah              Distorsi Definisi Bersih
  (Ketiadaan buku pilar)                (Biaya transaksi platform)
```

Lo bisa membedah akar masalahnya lewat beberapa cabang terstruktur:
* **Method:** Kebijakan diskon yang lo curigai. Apakah diskon terlalu dalam sehingga lonjakan volume penjualan sama sekali nggak mampu menutup margin yang tergerus?
* **Machine:** Algoritma sistem rekomendasi di platform lo. Apakah promosi cuma terkonsentrasi merekomendasikan seri-seri buku yang sebenarnya tanpa dipromosikan pun pembacanya sudah loyal dan pasti beli?
* **Material:** Komposisi katalog. Jangan-jangan penurunan ini terjadi karena bulan ini nggak ada rilis judul unggulan baru, sementara pembaca lama sudah selesai melahap katalog lama?
* **Measurement:** Cara lo menghitung metrik pendapatan bersih. Apakah lo memperhitungkan biaya komisi platform, potongan *payment gateway*, dan retur secara konsisten antarperiode?
* **Environment:** Faktor musiman di luar sistem. Apakah ada tren pembaca sedang sibuk ujian semester atau liburan sehingga pola konsumsi buku digitalnya bergeser?
* **Man:** Kebiasaan tim kurasi konten lo yang mungkin cuma memilih genre tertentu untuk dipajang di spanduk utama aplikasi.

Dua dugaan pertama (kebijakan diskon dan alokasi algoritma rekomendasi) adalah hipotesis paling berharga yang wajib lo uji duluan lewat data historis lo.

Satu hal lagi yang penting buat bab metode penelitian lo nanti: sadari batasan ketidakpastian data lo. Meskipun lo memegang jutaan baris data transaksi historis di *GPBSales*, data itu cuma mencatat apa yang sudah terjadi di bawah aturan diskon masa lalu. 

Status data lo itu tetap menyimpan **ketidakpastian epistemik** untuk menjawab pertanyaan kausal: *"Apakah diskon benar-benar menjadi penyebab tunggal turunnya pendapatan bersih?"*

Buat membuktikannya, lo butuh kelompok pembanding (*control period*) di mana buku-buku serupa dijual tanpa promo diskon pada rentang waktu yang setara. Jangan cuma mengandalkan model prediksi berbasis korelasi. 

Lalu untuk modul analitik yang lo rancang di tesis lo, wajibkan sistem lo mengeluarkan prediksi dalam bentuk rentang interval kepercayaan, pasang angka dasar naif berupa rata-rata transaksi tujuh hari terakhir sebagai pembanding performa, dan rancang mekanisme peringatan jika terjadi pergeseran distribusi pola belanja pembaca.

---

## Buat Obrolan Kita Selanjutnya

Biar kepala lo makin terasah sebelum lo mulai mengutak-atik bab analisis data lo, coba lo renungkan tiga pertanyaan ini:

1. Di dataset *GPBSales* lo, gimana cara konkret lo membuktikan secara empiris bahwa penurunan pendapatan bersih lo bukan akibat keacakan alami (*ketidakpastian aleatorik*) seperti pola musiman pembaca, melainkan masalah sistemik (*ketidakpastian epistemik*) pada strategi penentuan diskon?
2. Kalau lo diminta merancang satu skenario *premortem* untuk sistem rekomendasi dan penentuan harga buku lo, apa satu skenario kegagalan paling buruk yang paling mungkin luput dari perhatian lo saat ini?
3. Dari sekian banyak variabel di data lo, variabel apa yang paling rentan bikin lo terjebak *confirmation bias* karena kelihatannya sangat masuk akal di grafik tapi ternyata cuma korelasi semu?

Tadi pas gue mau beres-beres tas di kubikel SCBD, Aris sempat menghampiri gue sambil memegang kertas hasil cetakan log sistem. Wajahnya kelihatan letih banget, persis wajah mahasiswa S2 yang tugas kodingnya kena *error* di baris terakhir. Gue cuma bisa menepuk pundaknya pelan dan bilang kalau setidaknya diagram tulang ikannya tadi siang sangat rapi secara estetika.

Kereta komuter arah Bogor yang gue tumpangi malam ini lumayan lengang, memberi jeda buat gue meluruskan punggung setelah seharian menyimak drama korporat yang nggak ada habisnya. 

Jaga kesehatan lo ya, jangan sampai begadang cuma buat meladeni model yang parameternya belum lo kalibrasi dengan benar.

Sampai ketemu di sesi belajar kita berikutnya.

Nik
