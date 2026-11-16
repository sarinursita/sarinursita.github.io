---
title: "Catatan Nik: Tiga Kotak Kosong di Layar Proyektor Lantai 28, Ilusi Angka Pengalaman, dan Seni Memilih Saat Masa Depan Remang-Remang"
subtitle: "Gue kira rapat keputusan cuma soal siapa yang paling yakin, sampai klien minta angka probabilitas untuk slide yang isinya tiga kotak pastel tanpa satu pun hitungan."
type: blog
date: 2026-11-16T05:00:00+07:00
draft: true
ws_chat: 1730
ws_msg: 21969
category: Collab Journal
tags: ["study", "collab-journal", "MMSI", "analisa-dan-desain-smart-system", "decision-tree", "catatan-nik"]
summary: "Pekan ini materinya soal mengambil keputusan saat jawabannya belum pasti: tiga unsur yang wajib ada, pohon keputusan dan nilai harapan, jaringan Bayes dengan prior dan posterior, sampai diagram pengaruh. Di kantor gue, satu rekomendasi relokasi gedung hampir dibawa ke hadapan klien cuma bermodal kalimat \"berdasarkan pengalaman belasan tahun\"."
hook: "Slide rekomendasi itu rapi, tiga kotak pastel, dan sama sekali nggak punya angka probabilitas di baliknya."
---

Layar proyektor di ruang rapat lantai 28 kantor konsultan properti tempat gue kerja masih menyala terang, memantulkan tiga kotak persegi panjang berwarna pastel. Judul slidenya terdengar mentereng: *Rekomendasi Strategis Okupansi Fasilitas Klien*. Di bawah judul itu, cuma ada tiga opsi yang dijajarkan rapi: Opsi A Pindah Gedung, Opsi B Negosiasi Ulang Kontrak, dan Opsi C Tetap di Tempat. 

Vina, *head of sales* kami yang selalu tampil memukau dengan setelan blazer krem dan intonasi bertenaga, berdiri di depan layar sambil mengayunkan tangannya dengan penuh keyakinan. "Klien butuh efisiensi anggaran segera. Menurut kalkulasi tim, opsi negosiasi ulang kontrak bakal menghemat pengeluaran sewa hingga dua puluh persen. Ini skenario paling ideal," ujar Vina lugas.

Di ujung meja, perwakilan divisi pengadaan dari pihak klien mencondongkan badan. Raut wajahnya nggak terbeli-beli oleh senyum percaya diri Vina. "Dua puluh persen itu probabilitas keberhasilannya berapa besar, Mbak? Terus kalau negosiasi mandek selama tiga bulan dan kami kena denda keterlambatan konfirmasi perpanjangan gedung yang sekarang, biayanya membengkak jadi berapa? Opsi tetap di tempat kenapa cuma ditulis satu kalimat tanpa analisis risiko?"

Vina terdiam sepersekian detik, sebelum tersenyum diplomatis. "Itu angka estimasi terbaik kami berdasarkan pengalaman belasan tahun menangani sewa komersial di kawasan segitiga emas, Pak."

Gue yang duduk di samping Aris cuma bisa menunduk sambil mencoret-coret buku catatan. Aris, analis data junior kami yang duduk kaku di samping laptopnya, melirik gue dengan tatapan panik. Di balik slide cantik itu, memang nggak ada angka probabilitas apa pun. Nggak ada hitungan biaya masa tunggu, nggak ada simulasi skenario gagal, dan opsi tidak melakukan apa-apa diperlakukan sekadar pajangan pemanis slide. Keputusan sebesar relokasi korporat mau diambil murni karena suara orang yang paling lantang di ruang rapat.

Momen itu langsung menyentil ingatan gue ke materi kuliah SSAD pertemuan 7 yang lagi gue pelajari pekan ini, Sar. Sesi lima ngasih gue kacamata bias kognitif buat menyadari betapa ringkihnya penilaian manusia. Sesi enam membongkar masalah sampai ke tulang sumsumnya pakai fishbone dan memisahkan ketidakpastian aleatorik versus epistemik. Tapi obeng dan kacamata itu bakal sia-sia kalau kita nggak punya kompas. Sesi tujuh ini adalah kompasnya: bagaimana cara kita mengambil keputusan secara cerdas saat jawabannya serba tidak pasti.

---

## Tiga Unsur yang Hilang dan Jebakan Akurasi Semu

Begitu rapat selesai dan klien meninggalkan lantai 28 dengan ekspresi menggantung, gue mengajak Aris mampir ke pantry buat bikin kopi hitam. Anak itu langsung menghela napas panjang. "Mbak Nik, tadi gue deg-degan banget pas ditanya probabilitas negosiasi. Kan memang nggak ada datanya di arsip tim valuasi. Kalau gue masukin angka tebakan, malah makin salah kan?"

Gue tersenyum tipis sambil menyodorkan stoples gula. "Ris, setiap kali kita mau mengambil keputusan di bawah ketidakpastian, harus ada tiga unsur yang berdiri barengan. Kalau salah satu hilang, presentasi kita tadi itu bukan analisis bisnis, tapi cuma tebak-tebakan berhadiah yang dibungkus tipografi rapi."

Tiga unsur itu fundamental banget, Sar:

1. **Pilihan (*decision*)**: kumpulan tindakan konkret yang benar-benar berada di bawah kendali kita untuk diambil. Ini bukan cuma soal memilih alternatif A atau B, tapi wajib menyertakan pilihan *do nothing* alias tidak melakukan apa-apa. Di kantor tadi, opsi tetap di tempat cuma dianggap formalitas, padahal tidak melakukan apa-apa sering kali punya biaya risiko dan peluang tersendiri.
2. **Ketidakpastian (*chance*)**: peristiwa atau kondisi di luar kendali kita yang memengaruhi hasil akhir. Hal-hal ini nggak bisa kita atur sesuka hati, tapi wajib diberi bobot probabilitas, bukan diraba pakai perasaan atau diklaim sepihak atas nama pengalaman.
3. **Nilai (*objective/utility*)**: tolok ukur seberapa berharga atau buruknya hasil dari suatu keputusan bagi organisasi. Bentuknya bisa berupa keuntungan bersih, pengeluaran kas, efisiensi waktu, hingga risiko reputasi jangka panjang.

Gue selalu ingat pertanyaan uji cepat dari dosen gue: kalau di suatu skenario sama sekali nggak ada ketidakpastian, apakah kita masih butuh analisis probabilistik? Jawabannya jelas nggak butuh. Kalau masa depan itu pasti, kita cuma butuh kalkulator biasa buat menghitung perbandingan biaya langsung. Analisis probabilistik baru punya taring ketika hasil akhir langkah kita disandera oleh peristiwa yang belum kita ketahui kepastiannya.

Di sini juga letak kesalahan fatal yang sering gue temukan di proyek teknologi maupun bisnis: orang sering mengira model prediksi dengan akurasi sembilan puluh lima persen otomatis menghasilkan keputusan bisnis yang bagus. Padahal prediksi itu cuma bahan baku mentah, sedangkan keputusan adalah produk jadi yang siap dikonsumsi. 

Model cerdas bisa saja punya akurasi tinggi tapi keputusannya tetap berantakan karena tiga penyakit:

Pertama, **ambang keputusan (*decision threshold*)** yang nggak pernah dipikirkan. Ambang keputusan adalah batas probabilitas numerik yang ditetapkan untuk memicu sebuah tindakan nyata. Kalau sistem analitik memuntahkan probabilitas nol koma empat bahwa negosiasi sewa bakal gagal, terus tim manajemen harus ngapain? Angka nol koma empat itu mati gaya kalau bisnis nggak menetapkan ambang tegas kapan harus mundur dan kapan harus bertahan.

Kedua, **biaya salah yang tidak simetris (*asymmetric error cost*)**, yaitu kondisi di mana kerugian akibat satu jenis kesalahan jauh lebih fatal daripada kerugian akibat jenis kesalahan yang berlawanan. Membatalkan relokasi kantor padahal sebenarnya pemilik gedung mau menurunkan harga sewa mungkin cuma bikin kita kehilangan potensi diskon. Tapi nekat mengosongkan gedung lama sebelum kontrak gedung baru ditandatangani bisa bikin ratusan karyawan terlunta-lunta tanpa meja kerja. Akurasi rata-rata selalu memperlakukan kedua jenis salah ini setara, padahal dunia nyata nggak pernah seberbaik itu.

Ketiga, **urutan waktu dan biaya masa tunggu (*cost of waiting*)**. Mengambil keputusan hari ini punya nilai ekonomi yang berbeda jauh dibanding menunda keputusan demi menunggu data tambahan minggu depan. Waktu tunggu itu ada argo biayanya.

---

## Membedah Pohon Keputusan: Menghitung Mundur dari Kanan ke Kiri

Sore harinya, gue duduk berdua sama Aris di meja kerjanya. Gue ambil selembar kertas kosong ukuran A4, lalu gue rebahkan secara horizontal. "Sini, Ris. Kita bedah masalah klien tadi pakai alat paling klasik tapi paling jujur: *decision tree*."

*Decision tree* (pohon keputusan) adalah diagram bercabang mirip pohon tumbang yang memetakan pilihan tindakan dan kemungkinan hasil secara berurutan dari kiri ke kanan. Strukturnya gampang dipahami begitu kita tahu tiga simbol standarnya:

- **Simpul kotak** melambangkan simpul keputusan, titik di mana kita yang memegang kendali penuh untuk memilih cabang tindakan.
- **Simpul lingkaran** melambangkan simpul peluang, titik di mana alam atau lingkungan eksternal yang menentukan nasib, dan tugas kita menempelkan angka probabilitas di setiap cabangnya.
- **Simpul segitiga atau titik ujung** melambangkan hasil akhir (*payoff*), yaitu nilai keuntungan, kerugian, atau pengeluaran bersih dari jalur skenario tersebut.

Satu garis utuh yang membentang dari akar paling kiri sampai ke ujung paling kanan disebut sebagai satu skenario tunggal.

```
[Keputusan] ---> (Peluang) ---> <Hasil Akhir / Payoff>
```

"Nah, ngitungnya gimana, Mbak Nik?" tanya Aris sambil memperhatikan gambar kotak dan lingkaran yang gue buat.

Cara menghitungnya memakai konsep *expected value* (EV) alias nilai harapan. *Expected value* adalah rata-rata tertimbang dari seluruh hasil yang mungkin terjadi dikalikan dengan probabilitas masing-masing skenario. Menariknya, perhitungannya berjalan terbalik dari kanan ke kiri, proses yang di bangku kuliah gue kenal dengan istilah *rollback* atau *backward induction* (metode menghitung pohon keputusan dari ujung hasil paling kanan mundur ke arah simpul keputusan paling kiri).

Aturan jalannya sangat mekanis dan tanpa kompromi:
1. Di setiap simpul lingkaran (peluang): hitung jumlah dari perkalian antara probabilitas dengan *payoff* pada seluruh cabang yang keluar dari lingkaran itu.
2. Di setiap simpul kotak (keputusan): bandingkan hasil nilai harapan dari cabang-cabang yang tersedia, lalu pilih nilai yang paling menguntungkan (terbesar kalau bicara profit, terkecil kalau bicara biaya).
3. Gulung terus hitungan mundur ini sampai menyentuh akar paling kiri. Cabang keputusan yang bertahan di simpul akar itulah yang menjadi rekomendasi logis kita.

Biar otak Aris nggak mengawang-awang, gue kasih contoh angka konkret dari materi kuliah gue pekan ini. Bayangkan sebuah penerbitan mau meluncurkan judul baru dan dihadapkan pada tiga opsi:

| Pilihan Tindakan | Biaya di Muka | Skenario Laku (p) | Untung Kotor Laku | Skenario Tidak Laku (p) | Untung Kotor Tidak Laku |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Cetak Skala Besar** | Rp200 juta | 0,4 | Rp500 juta | 0,6 | Rp100 juta |
| **Cetak Skala Kecil** | Rp80 juta | 0,6 | Rp250 juta | 0,4 | Rp60 juta |
| **Tidak Cetak** | Rp0 | - | Rp0 | - | Rp0 |

Mari kita hitung nilai harapan bersihnya satu per satu:
- Untuk opsi Cetak Skala Besar: `(0,4 × Rp500 juta) + (0,6 × Rp100 juta) - Rp200 juta = Rp200 juta + Rp60 juta - Rp200 juta = Rp60 juta`.
- Untuk opsi Cetak Skala Kecil: `(0,6 × Rp250 juta) + (0,4 × Rp60 juta) - Rp80 juta = Rp150 juta + Rp24 juta - Rp80 juta = Rp94 juta`.
- Untuk opsi Tidak Cetak: nilainya jelas `Rp0`.

Aris terbelalak melihat hasil akhirnya. "Loh, Mbak, cetak skala besar kan potensi untung kotornya gila-gilaan, bisa tembus setengah miliar! Tapi kok nilai harapannya malah kalah jauh dibanding cetak skala kecil?"

"Tepat di situ inti pelajarannya, Ris," sahut gue. Nilai harapan bukan soal mencari opsi yang paling menggiurkan kalau kita menang telak, tapi mencari opsi yang memberikan hasil rata-rata tertinggi setelah memperhitungkan risiko kegagalan dan biaya di muka. Cetak besar punya potensi profit selangit, tapi karena biaya awalnya mahal dan peluang lakunya cuma empat puluh persen, nilai harapan bersihnya tergerus oleh skenario tidak laku.

Kekuatan utama pohon keputusan ada pada kemampuannya memaksa manajemen membuka angka di atas meja. Debat kusir soal firasat langsung terhenti karena yang diperdebatkan bergeser ke validitas angka probabilitas dan estimasi biaya. Alat ini juga brilian untuk keputusan bertingkat yang saling bersambung, misalnya: uji pasar dulu, lihat hasilnya, baru putuskan investasi pabrik. 

Bahkan, kita bisa menghitung *value of information* (nilai informasi), yaitu batas biaya maksimal yang masuk akal dibayar untuk mendapatkan data tambahan sebelum mengambil keputusan. Caranya elegan banget: hitung nilai harapan sebelum riset pasar dilakukan, lalu hitung nilai harapan setelah riset pasar memberikan kepastian. Selisih dari kedua angka itulah nilai maksimal yang boleh kita bayarkan ke konsultan riset. Kalau biaya survei lebih mahal dari selisih itu, jangan dibeli.

Tapi pohon keputusan bukan tanpa cela, Sar. Batasan utamanya nyata banget:
1. **Pohon cepat meledak secara kombinatorial (*combinatorial explosion*)**. Begitu kita punya lima tahap keputusan berurutan dengan masing-masing tiga skenario kemungkinan, cabangnya langsung membengkak jadi ratusan jalur yang ruwetnya minta ampun.
2. **Ketergantungan pada sumber probabilitas**. Kalau angka nol koma empat atau nol koma enam itu cuma hasil karangan bebas demi memenangkan argumen pribadi, output pohonnya bakal rapi tapi sepenuhnya sampah.
3. **Mengabaikan selera risiko (*risk appetite*)**. Nilai harapan murni mengasumsikan organisasi bersikap netral terhadap risiko (*risk-neutral*). Padahal buat perusahaan yang arus kasnya lagi sekarat, potensi rugi seratus juta di skenario terburuk bisa langsung bikin gulung tikar. Di kondisi seperti ini, nilai harapan uang harus dikonversi menjadi *expected utility* (utilitas harapan: nilai kepuasan atau toleransi risiko subjektif yang menggantikan nilai uang murni dalam keputusan berisiko tinggi).
4. **Semua variabel dipaksa berbentuk uang**. Dampak terhadap moral karyawan, kepatuhan regulasi, atau kepercayaan publik sangat sulit diangkakan secara jujur tanpa manipulasi asumsi.

---

## Jaringan Bayes: Menghidupkan Probabilitas dari Relasi Sebab-Akibat

Mendengar batasan pohon keputusan tadi, Aris langsung menyeletuk. "Nah itu dia masalah kita di kantor tadi, Mbak Nik. Kami di tim valuasi properti nggak punya tabel angka probabilitas selengkap itu. Tapi kalau ditanya relasi logisnya, para valuer senior sebenarnya tahu: kalau suku bunga acuan naik dan pasokan ruang kantor baru di SCBD lagi banjir, kemungkinan pemilik gedung mau kasih diskon sewa pasti melonjak. Masalahnya, pengetahuannya cuma ada di kepala mereka dalam bentuk logika sebab-akibat."

"Di titik itulah kita butuh *Bayesian network*, Ris," kata gue sambil menggambar beberapa lingkaran baru di balik kertas.

*Bayesian network* (jaringan Bayes) adalah model grafis yang menggambarkan hubungan sebab akibat antar-variabel menggunakan teori peluang bersyarat. Model ini hadir buat menjawab masalah dunia nyata ketika angka probabilitas statistik historis sangat minim, tapi struktur pengetahuan para pakar mengenai relasi kausalitas tersedia dengan sangat kaya.

Bentuk anatominya terdiri dari:
- **Simpul (*nodes*)** yang mewakili variabel (bisa berupa kondisi lingkungan, faktor pemicu, gejala, maupun kejadian spesifik).
- **Panah berarah (*edges*)** yang melambangkan pengaruh kausal langsung. Kalau ada panah dari simpul A menuju simpul B, artinya kondisi A secara langsung memengaruhi kemunculan peristiwa B.
- Struktur grafnya wajib berwujud *Directed Acyclic Graph* (DAG), yaitu graf berarah yang jalurnya mengalir satu arah tanpa pernah berputar membentuk lingkaran tertutup. Kalau ada panah yang memutar balik membentuk siklus, perhitungan matematisnya bakal macet total.
- Setiap simpul dilengkapi dengan *Conditional Probability Table* (CPT), yaitu tabel yang mencatat peluang suatu kejadian terjadi berdasarkan kondisi atau kejadian induk yang mendahuluinya.

Simpul akar yang berada di posisi paling atas diisi oleh nilai *prior* (tingkat keyakinan atau probabilitas awal tentang suatu kejadian sebelum ada bukti atau observasi baru). Begitu di lapangan kita menemukan fakta atau bukti konkret (*evidence*), nilai *prior* ini langsung diperbarui menjadi nilai *posterior* (probabilitas yang sudah diperbarui setelah memperhitungkan bukti atau data baru yang masuk). Proses pembaruan keyakinan berbasis bukti baru ini dinamakan proses inferensi.

```
[Suku Bunga Acuan] ---> [Kondisi Finansial Pemilik Gedung]
                                  |
                                  v
[Tingkat Okupansi Area] ---> [Peluang Diskon Sewa Diberikan]
```

Kenapa jaringan Bayes ini sangat disukai di perancangan sistem cerdas? 
Pertama, dia bisa mengawinkan data historis yang sedikit dengan intuisi terstruktur dari pakar senior kantor. Kedua, modelnya sangat transparan karena panah-panah kausalitasnya bisa ditunjuk dan didebatkan secara visual, bukan seperti *black-box* jaringan saraf tiruan. Ketiga, model ini sangat tangguh menghadapi data yang bolong (*missing data*). Kalau ada satu variabel lapangan yang lupa diukur oleh tim agen, jaringan Bayes masih bisa mengalkulasi estimasi probabilitas variabel lainnya. Keempat, inferensinya berjalan dua arah: bisa bergerak maju dari penyebab untuk memprediksi gejala (*forward prediction*), atau melompat mundur dari gejala yang terlihat untuk mendiagnosis akar penyebab (*backward diagnosis*).

Namun, ada satu jebakan klasik di dunia probabilitas Bayes yang sering bikin orang paling pintar sekalipun terjungkal: *base rate neglect* (kecenderungan manusia mengabaikan prevalensi dasar suatu populasi saat menilai kemungkinan suatu kejadian spesifik).

Gue kasih simulasi kasus medis klasik yang sempat ditekankan dosen gue, Sar. Bayangkan ada sebuah penyakit langka yang cuma menjangkiti satu persen dari total populasi masyarakat (`P(Sakit) = 0,01`). Sebuah laboratorium menciptakan alat tes canggih dengan tingkat sensitivitas sembilan puluh sembilan persen, artinya kalau orang benar-benar sakit, probabilitas hasil tes positif mencapai sembilan puluh sembilan persen. Namun alat ini punya tingkat positif palsu (*false positive*) sebesar lima persen, artinya ada lima persen orang sehat yang dites tapi hasilnya keliru dinyatakan positif.

Sekarang bayangkan ada seorang staf kantor kita iseng ikut tes medis massal, dan hasil tesnya keluar: **Positif**. Berapa probabilitas bahwa staf tersebut benar-benar mengidap penyakit langka itu?

Secara naluriah, orang awam di ruang rapat bakal langsung panik dan berteriak, "Wah, sembilan puluh sembilan persen pasti sakit itu!" Padahal kalau kita hitung pakai teorema Bayes, angkanya bikin mata terbelalak:

1. Peluang orang tersebut benar-benar sakit dan hasil tesnya positif:  
   `P(Sakit dan Positif) = 0,99 × 0,01 = 0,0099`
2. Peluang orang tersebut sebenarnya sehat tapi tesnya keliru memunculkan positif:  
   `P(Sehat tapi Positif) = 0,05 × (1 - 0,01) = 0,05 × 0,99 = 0,0495`
3. Total probabilitas munculnya hasil tes positif dari seluruh populasi:  
   `Total Positif = 0,0099 + 0,0495 = 0,0594`
4. Probabilitas posterior bahwa orang yang hasil tesnya positif memang benar-benar sakit:  
   `P(Sakit | Positif) = 0,0099 / 0,0594 ≈ 0,1667` alias **cuma sekitar 17 persen!**

Aris ternganga menatap coretan kalkulator di ponselnya. "Mbak Nik, serius cuma tujuh belas persen? Padahal alat tesnya dibilang akurat sembilan puluh sembilan persen!"

"Iya, Ris," sahut gue. Kenapa bisa anjlok begitu? Karena populasi orang sehat jauh lebih masif (sembilan puluh sembilan persen), sehingga limpahan lima persen positif palsu dari orang sehat jumlah kepalanya jauh lebih banyak dibanding orang sakit yang benar-benar terdeteksi positif. 

Ini pelajaran paling mahal buat kita di manajemen sistem informasi: angka akurasi tinggi pada distribusi data yang timpang (*imbalanced data*) hampir selalu menipu akal sehat. Hal ini mengikat langsung materi sesi lima gue soal data berprasangka dengan metrik evaluasi mesin cerdas di mata kuliah lain.

Tentu jaringan Bayes juga punya batas kelemahan:
- Kalau struktur DAG awalnya salah dibuat karena sok tahu membalik arah panah sebab-akibat, model bakal menghasilkan output angka yang terlihat meyakinkan padahal sesat pikir.
- Tabel probabilitas bersyarat (CPT) bakal meledak secara ukuran kalau satu simpul anak dipaksa punya terlalu banyak simpul induk.
- Sangat sensitif terhadap nilai keyakinan awal (*prior*). Kalau asumsi awal kita ngawur, probabilitas akhir yang dimuntahkan juga bakal ikut ngawur.

---

## Diagram Pengaruh: Menyelamatkan Ruang Rapat Tanpa Bikin Pusing Direksi

"Kalau begitu, Mbak Nik," tanya Aris sambil memandangi tumpukan coretan pohon keputusan dan jaringan Bayes yang mulai berantakan, "pas presentasi ke klien atau direksi lantai 28 minggu depan, kita harus buka yang mana? Kalau kita keluarin pohon keputusan dengan ratusan cabang, mereka pasti pusing terus kabur. Kalau kita sodorin rumus Bayes, kita bakal dibilang dosen teoritis."

Gue tertawa kecil. "Makanya di sesi tujuh dikenalkan alat ketiga: *influence diagram*."

*Influence diagram* (diagram pengaruh) adalah representasi grafis tingkat tinggi yang memadukan pilihan keputusan, faktor ketidakpastian, dan sasaran nilai tanpa harus menggambar seluruh cabang skenario. Diagram ini mengawinkan kepraktisan pohon keputusan dengan keanggunan jaringan Bayes dalam satu kanvas sederhana.

Diagram ini cuma memakai empat bentuk geometri dasar:
1. **Kotak Persegi**: simpul keputusan, hal yang bisa langsung dipilih oleh manajemen.
2. **Lingkaran / Oval**: simpul peluang, variabel ketidakpastian yang berada di bawah kendali probabilitas.
3. **Belah Ketupat (*diamond*)**: simpul nilai atau tujuan, metrik akhir yang ingin dimaksimalkan atau diminimalkan oleh organisasi (misalnya: efisiensi kas total atau kepuasan penyewa).
4. **Lingkaran Ganda / Persegi Oval**: simpul deterministik, yaitu simpul penengah yang nilainya dihitung pasti melalui formula pasti tanpa ketidakpastian lagi (misalnya: `Total Biaya = Harga Sewa per Meter × Luas Unit`).

Arah panah di diagram pengaruh punya makna semantik yang sangat presisi:
- Panah yang menusuk ke dalam **simpul keputusan** berarti informasi ketersediaan: informasi dari simpul asal sudah harus diketahui oleh pengambil keputusan tepat pada saat pilihan itu dieksekusi.
- Panah yang mengalir ke **simpul peluang atau nilai** melambangkan pengaruh fungsional atau ketergantungan kondisional: kondisi di simpul asal secara langsung mengubah besaran peluang atau nilai di simpul tujuan.

Kenapa diagram pengaruh ini senjata paling ampuh di ruang rapat direksi?
Pertama, dia luar biasa ringkas. Satu gambar sederhana seukuran kartu pos sanggup merangkum puluhan ribu kemungkinan skenario yang kalau digambar pakai pohon keputusan bakal menghabiskan gulungan kertas sepanjang lorong SCBD. 
Kedua, fokusnya murni pada keterkaitan keputusan bisnis, membuang detail percabangan yang nggak relevan.
Ketiga, urutan waktunya luwes dan tidak kaku harus berbaris dari kiri ke kanan. 
Dan yang paling penting di dunia nyata: gambar ini ramah bagi mata para eksekutif. Analisis secanggih apa pun nggak akan pernah dieksekusi kalau audiens penentu anggaran gagal memahami logikanya dalam sepuluh detik pertama.

Gue merangkum korelasi ketiga alat analisis cerdas ini di papan tulis kecil pantry:
- **Bayesian network** bertugas menjawab: *seberapa besar peluang terjadinya suatu kondisi?*
- **Decision tree** bertugas menghitung secara mekanis: *pilihan mana yang secara matematis menghasilkan nilai rata-rata terbaik langkah demi langkah?*
- **Influence diagram** bertugas memetakan gambaran helikopter: *bagaimana struktur hubungan besar antara pilihan, ketidakpastian, dan tujuan bisnis kita?*

Dalam alur proyek konsultan yang waras, urutannya selalu dimulai dari atas: kita gambar diagram pengaruh bersama para pemangku kepentingan untuk menyepakati kerangka berpikir masalahnya. Begitu strukturnya disepakati, baru kita turunkan menjadi pohon keputusan atau jaringan Bayes di belakang layar untuk memproses perhitungan angka rincinya.

---

## Kapan Memakai yang Mana, Plus Tujuh Dosa Analisis Keputusan

Biar kepala lo nggak berputar waktu membaca catatan ini, Sar, gue rapikan komparasi situasi lapangannya ke dalam tabel ringkas:

| Kondisi Masalah di Lapangan | Alat yang Paling Tepat | Landasan Alasan Logis |
| :--- | :--- | :--- |
| Pilihan tindakan sedikit, urutan kejadian kaku dan beruntun, angka estimasi tersedia | **Decision Tree** | Nilai harapan (*expected value*) bisa langsung dihitung lewat *backward induction*. |
| Banyak variabel saling silang, data historis minim, ada intuisi logis pakar | **Bayesian Network** | Mampu menggabungkan data terbatas dengan struktur kausalitas, tahan nilai kosong. |
| Butuh menyepakati kerangka masalah di hadapan direksi atau klien non-teknis | **Influence Diagram** | Visualnya bersih, ringkas, dan fokus pada sasaran nilai tanpa keruwetan cabang. |
| Ingin menguji apakah anggaran riset pasar atau survei lapangan layak dikeluarkan | **Decision Tree** | Memungkinkan kalkulasi selisih nilai harapan sebelum dan sesudah informasi (*value of information*). |
| Butuh mendeteksi akar anomali sistem berdasarkan gelagat atau gejala luar | **Bayesian Network** | Mendukung inferensi diagnostik dua arah dari gejala mundur ke penyebab. |
| Keputusan berulang di mana biaya salah memprediksi bersifat sangat asimetris | **Decision Tree + Ambang Batas** | Memaksa bisnis menetapkan ambang risiko, bukan sekadar melihat nilai rata-rata EV. |

Sebelum kita terjun menerapkan alat-alat ini, ada tujuh dosa besar dalam analisis keputusan yang wajib kita hindari biar nggak mengulang kekacauan presentasi Vina tadi pagi:

1. **Berhenti hanya pada angka nilai harapan (EV)**. Menelan mentah-mentah EV tertinggi tanpa mengecek selera risiko organisasi sama saja bunuh diri finansial kalau skenario terburuknya membawa potensi bangkrut.
2. **Memakai probabilitas tanpa jejak sumber**. Kalau angka persentase nggak bisa dipertanggungjawabkan asalnya dari data historis, pengujian terukur, atau dokumen konsensus pakar, itu bukan probabilitas ilmiah, itu selera subjektif pembuat slide.
3. **Mengabaikan prevalensi dasar (*base rate neglect*)**. Lupa memperhitungkan proporsi awal populasi saat membaca akurasi sistem, persis seperti simulasi tes medis yang menipu tadi.
4. **Menggambar seluruh cabang skenario yang ada di alam semesta**. Pohon keputusan bukan arsip museum sejarah. Cabang-cabang yang tidak mengubah arah pilihan akhir harus berani dipangkas (*pruned*).
5. **Mencampur aduk prediksi model dengan keputusan final**. Menyatukan kedua hal ini dalam satu slide hanya memicu perdebatan kusir mengenai akurasi algoritma, padahal yang mendesak disepakati adalah batas ambang risikonya.
6. **Lupa memasukkan biaya masa tunggu (*cost of waiting*)**. Menunda eksekusi keputusan selalu menyedot biaya peluang dan biaya denda operasional yang wajib dibukukan ke dalam pohon keputusan.
7. **Mengultuskan model probabilistik sebagai ramalan mutlak**. Model ini cuma kompas pemandu estimasi arah dan perbandingan selisih antarpilihan, bukan bola kristal peramal masa depan.

---

## Bahan Diskusi Kita Pekan Ini

Sore tadi gue akhirnya mengajak Aris menyusun ulang slide rekomendasi untuk klien relokasi itu dari nol. Kami sepakat membuang tiga kotak statis tanpa dasar milik Vina, dan menggantinya dengan diagram pengaruh sederhana untuk sesi dengar pendapat ulang lusa. 

Nah, mumpung ingatan lo masih segar dari sesi review mandiri lo, gue mau melempar tiga hal buat melatih ketajaman analisis lo, Sar:

1. Di skenario klien sewa kantor tadi, misal mereka punya pilihan tambahan: menyewa konsultan riset pasar independen seharga lima puluh juta rupiah untuk memetakan kepastian apakah pemilik gedung bersedia menurunkan tarif sewa atau tidak. Berdasarkan prinsip *value of information*, parameter apa saja yang harus lo hitung lebih dulu sebelum lo bisa memutuskan apakah membayar lima puluh juta itu langkah cerdas atau pemborosan kas?
2. Pada kasus *base rate neglect*, bayangkan kantor gue meluncurkan sistem cerdas pendeteksi unit ruko yang berisiko gagal bayar sewa tahunan. Dari total populasi, hanya dua persen penyewa yang benar-benar gagal bayar. Model itu punya sensitivitas 95 persen dan tingkat positif palsu empat persen. Bagaimana lo menjelaskan ke tim penagihan bahwa mayoritas penyewa yang ditandai lampu merah oleh sistem sebenarnya masih sanggup membayar tepat waktu?
3. Di tengah kultur korporat yang sering mendewakan senioritas dan klaim "berdasarkan pengalaman belasan tahun" seperti gaya Vina tadi pagi, bagaimana strategi lo memposisikan *decision tree* tanpa membuat tim bisnis merasa diserang atau dianggap tidak kompeten?

Gue mau merapikan berkas di meja kerja dulu sebelum bersiap menyeduh teh melati hangat. Dylan tadi sore sempat telepon singkat di sela waktu istirahat asramanya cuma buat pamer kalau tim basketnya lolos ke babak semifinal antar-sekolah akhir pekan ini, bikin senyum gue bertahan sampai malam.

Semoga catatan panjang ini bikin kepala lo makin terang bedah materi S2 kita minggu ini.

Salam hangat dari sudut hening meja kerja Bogor,

Nik