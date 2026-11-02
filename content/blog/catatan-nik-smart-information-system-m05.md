---
title: "Catatan Nik: Ilusi Kotak Ajaib dan Kolom yang Nggak Sepakat Definisi"
subtitle: Gue kira masalahnya cuma demo vendor yang gebleg. Ternyata yang bikin keringet dingin itu definisi satu kolom aja beda rumus antar cabang klien.
type: blog
date: 2026-11-05T05:00:00+07:00
draft: true
ws_chat: 1646
ws_msg: 21698
category: Collab Journal
tags: ["study", "collab-journal", "MMSI", "smart-information-system", "catatan-nik"]
summary: "Materi kuliah gue pekan ini soal representasi pengetahuan: hierarki DIKW, tacit vs eksplisit, sampai empat teknik dari rule-based, semantic network, frame, dan logika predikat. Di kantor gue, klien teler liat demo vendor di LinkedIn dan minta dashboard colok-langsung-jalan, padahal data mereka berantakan dan heuristik valuernya cuma ada di kepala."
hook: Pernah nggak lo ditawarin sistem yang katanya tinggal colok data, terus pas dicek, definisi satu kolom aja beda-beda antar cabang?
---

Layar monitor 27 inci di meja kerja gue pagi ini nampilin rekaman video presentasi durasi dua menit yang dikirim Vina lewat pesan instan subuh tadi, lengkap dengan tiga tanda seru merah. Isinya tipikal video *marketing* teknologi kelas atas: transisi visual mengilap, grafik tiga dimensi berputar mulus, dan seorang presenter dengan jas necis yang membual soal bagaimana platform mereka bisa "mengubah tumpukan data transaksi properti menjadi keputusan investasi otomatis dalam hitungan detik berkat *artificial intelligence*."

Vina, seperti biasa dengan insting *head of sales* yang mencium komisi besar, langsung menyambar umpan itu. Klien korporat yang sedang kami dekati, konglomerasi ritel dan aset komersial raksasa, melihat video serupa di LinkedIn. Sekarang mereka menuntut proposal sistem valuasi otomatis persis seperti demo vendor tersebut. Klien itu bilang ke Vina, mereka mau dashboard pintar yang langsung bisa ngasih rekomendasi: beli, tahan, atau lepas aset tanah di koridor luar Jakarta tanpa perlu mikir panjang lagi.

Gue sempat menghela napas panjang waktu Vina menelpon gue jam delapan pagi dari lobi lantai 28 gedung kantor kami di SCBD. Suara langkah sepatunya berderap cepat di lantai marmer, berpacu dengan ambisinya yang meledak-ledak.

"Nik, tolong ya, kita tinggal colok data mereka kan? Vendornya bilang arsitektur mereka *plug and play*. Klien punya catatan transaksi puluhan tahun di gudang data mereka. Kita tinggal masukin mesin inferensi, beres! Lo bikin arsitekturnya di proposal sebelum jam makan siang!"

Gue menatap Aris, yang duduk di seberang bilik kerja dengan muka bantal dan mata merah. Aris, yang kemarin seharian mengutak-atik ekstrak data klien itu, cuma bisa melempar senyum kecut sambil mengangkat satu bundel map tebal berisi cetakan *spreadsheet* acak-kadut. 

"Mbak Vina nggak tahu aja," bisik Aris pelan waktu panggilan telepon ditutup. "Data mereka itu bukan cuma kotor, Mbak. Tapi definisi satu kolom 'harga pasar wajar' antar cabang aja beda rumus. Sebagian valuer mereka nentuin nilai diskon cuma pake *feeling* pas ngopi di lobi hotel. Gimana caranya bikin mesin mikir kalau kita sendiri nggak tahu apa yang ada di kepala mereka?"

Kalimat Aris langsung menghantam ingatan gue ke materi kuliah minggu ini: *Knowledge Representation*. Banyak orang di level bisnis mengira bahwa pengetahuan (*knowledge*) itu cuma versi mewah dari sekumpulan data yang ditumpuk di server berkapasitas *terabyte*. Mereka pikir kalau kita punya data segunung, otomatis kita punya sistem yang bijak (*wise*). Padahal, jarak antara data mentah dengan mesin yang bisa mengambil keputusan rasional itu sejauh bumi ke galaksi tetangga, Sari.

---

## Dari Angka Mentah ke Kebijaksanaan: Tragedi Hierarki DIKW yang Sering Disunat

Sari, lo pasti udah khatam sama piramida DIKW (*Data, Information, Knowledge, Wisdom*). Tapi di dunia praktika konsultan bisnis, piramida ini sering banget dipangkas paksa. Manajemen atau klien maunya loncat langsung dari D ke W. Mereka punya Data, lalu berharap besok pagi keluar Wisdom.

Mari kita bedah pelan-pelan supaya kita nggak ikutan halu kayak kliennya Vina:

1. **Data**: Ini fakta mentah, simbol objektif tanpa konteks atau interpretasi. Contoh di kasus kantor gue: deretan angka transaksi "15.000.000", string "Jaksel", dan tanggal "12-08-2023". Kalau cuma berdiri sendiri, deretan angka ini nggak ada artinya sama sekali.
2. **Information**: Data yang sudah diproses, diorganisasi, distrukturkan, dan diberi konteks sehingga punya makna (*meaning*). Ketika angka tadi dirangkai jadi "Harga sewa ruang kantor grade A di SCBD Jakarta Selatan rata-rata Rp15.000.000 per meter persegi per tahun per kuartal tiga 2023", itu baru jadi informasi. Ada jawaban atas pertanyaan *who, what, where,* dan *when*.
3. **Knowledge**: Nah, ini titik kritisnya. Pengetahuan adalah pemahaman kognitif, integrasi informasi dengan pengalaman, aturan, model mental, dan konteks terapan. Ini menjawab pertanyaan *how* dan *why*. Pengetahuan memberi tahu kita: "Kalau harga sewa SCBD menyentuh Rp15.000.000 per meter persegi tapi tingkat keterisian (*occupancy rate*) anjlok di bawah 70%, maka pemilik gedung kemungkinan besar akan memberikan insentif *fit-out* gratis selama enam bulan ketimbang menurunkan harga sewa resmi di atas kertas demi menjaga valuasi pinjaman bank." Mesin butuh pemahaman hubungan kausalitas dan pola ini supaya bisa bertindak.
4. **Wisdom**: Tingkat tertinggi yang melibatkan pertimbangan etis, nilai jangka panjang, konteks situasional yang unik, dan penilaian kritis. Wisdom tahu kapan sebuah aturan umum harus dilanggar demi tujuan strategis yang lebih mulia atau menghindari bencana sistemik.

Klien kami punya segudang Data, sedikit Informasi yang terpencar di puluhan lembar kerja Excel, tapi nol besar dalam hal Knowledge yang terdokumentasi rapi. Mereka mengira perangkat lunak kecerdasan buatan itu semacam wadah ajaib: lo tuang angka mentah ke dalamnya, lalu keluar keajaiban strategi bisnis. 

Kalau mesin inferensi cuma dikasih tumpukan data tanpa representasi pengetahuan yang valid, yang keluar bukan sistem cerdas, melainkan mesin halusinasi berkecepatan tinggi.

---

## Jurang Pemisah Antara yang Tersirat dan yang Tersurat

Tantangan terbesar yang bikin Aris garuk-garuk kepala seharian adalah kenyataan pahit dalam *knowledge engineering*: mengubah *tacit knowledge* menjadi *explicit knowledge*.

*Explicit knowledge* itu gampang. Itu pengetahuan yang sudah dikodifikasi, ditulis dalam SOP, disimpan dalam buku panduan valuasi standar, atau dibukukan dalam tabel regulasi perpajakan tanah. Kita bisa dengan mudah membaca dan memindahkannya ke dalam kode program atau basis data.

Tapi di dunia nyata, 80 persen keputusan bisnis krusial diambil berdasarkan *tacit knowledge*. Ini pengetahuan yang tersimpan di dalam kepala para pakar senior: akumulasi intuisi, pengalaman lapangan puluhan tahun, insting membaca gestur pemilik tanah, kebiasaan lokal yang nggak pernah tertulis di regulasi resmi, serta trik mengatasi situasi anomali. 

Valuer senior di klien itu tahu kapan sebuah dokumen sertifikat tanah terlihat mencurigakan hanya dari cap notarisnya atau riwayat sengketa keluarga pemiliknya. Waktu ditanya bagaimana caranya dia tahu, jawabannya cuma: "Ya berasa aja, pengalamannya beda."

Nah, tugas seorang *knowledge engineer* adalah menjadi jembatan. Lo harus bisa mengekstraksi isi kepala orang-orang ini, merumuskannya, lalu mengodekannya ke dalam format formal yang bisa dimengerti oleh algoritma inferensi. Kalau proses akuisisi ini gagal, sistem cerdas apa pun yang dibangun vendor dengan biaya miliaran rupiah cuma bakal jadi rongsokan digital.

Kita nggak bisa merepresentasikan semua pengetahuan dengan satu cara seragam. Secara teoretis, kita mengenal beberapa jenis pengetahuan yang harus diwadahi:

* **Pengetahuan Deklaratif (*Declarative Knowledge*)**: Fakta tentang dunia luar, konsep, atau statemen "tahu bahwa" (*know-what*). Misalnya: "Gedung Menara X memiliki luas sewa 45.000 meter persegi dan terletak di zona komersial primer."
* **Pengetahuan Prosedural (*Procedural Knowledge*)**: Instruksi langkah demi langkah tentang cara menyelesaikan sesuatu (*know-how*). Misalnya: urutan kalkulasi metode diskonto arus kas (*discounted cash flow*) untuk menentukan nilai kini bersih dari portofolio properti.
* **Pengetahuan Heuristik (*Heuristic Knowledge*)**: Aturan praktis (*rules of thumb*) yang didapat dari pengalaman empiris bertahun-tahun. Ini bukan hukum pasti seperti matematika, tapi cara cepat yang terbukti benar sebagian besar waktu. Contoh: "Kalau pengembang menunda serah terima unit lebih dari dua kali dalam setahun, asumsikan ada krisis arus kas internal minimal 30 persen."
* **Meta-pengetahuan (*Meta-knowledge*)**: Pengetahuan tentang pengetahuan itu sendiri. Sistem harus tahu batasan apa yang dia ketahui, kapan sebuah aturan relevan dipakai, dan aturan mana yang harus diutamakan kalau terjadi konflik logika.
* **Pengetahuan Struktural (*Structural Knowledge*)**: Hubungan relasional antar konsep atau objek, seperti hubungan bagian-keseluruhan (*part-whole*) atau taksonomi hierarkis (misalnya: *penthouse* adalah bagian dari apartemen mewah, apartemen mewah adalah subkelas dari properti residensial).

Belum lagi kalau kita bicara soal dimensi kepastian: apakah pengetahuan itu bersifat deterministik (pasti, mutlak 100 persen benar) atau probabilistik (mengandung ketidakpastian, bias, dan probabilitas bersyarat). Kebanyakan data bisnis nyata berada di ranah probabilistik, yang bikin proses pemodelannya makin menantang.

---

## Menimbang Lima Pilar Representasi Pengetahuan

Sebelum kita latah memilih format teknis untuk menampung pengetahuan tersebut, literatur menetapkan lima syarat kualitas yang harus dipenuhi oleh skema representasi pengetahuan yang ideal. Gue sempat menuliskan kelima poin ini di papan tulis kaca lantai 28 buat menyadarkan Vina dan tim sales:

1. **Kecukupan Representasional (*Representational Adequacy*)**: Kemampuan skema tersebut untuk menangkap dan mengekspresikan semua jenis pengetahuan yang dibutuhkan dalam domain tertentu. Kalau domain lo penuh aturan bernuansa waktu atau ketidakpastian, skema logika kaku jelas nggak memadai.
2. **Efisiensi Inferensi (*Inferential Efficiency*)**: Kemampuan sistem untuk mengarahkan proses pencarian kesimpulan ke arah yang paling menjanjikan tanpa membuang waktu menjelajahi jutaan kemungkinan jalan buntu. Representasi yang terlalu rumit bisa bikin mesin *freeze* atau butuh waktu berjam-jam cuma buat menjawab satu pertanyaan sederhana.
3. **Kemudahan Akuisisi (*Acquisition Efficiency*)**: Seberapa mudah kita memasukkan pengetahuan baru ke dalam sistem. Bisnis properti itu dinamis; regulasi pajak berganti tiap tahun. Kalau nambah satu aturan valuasi saja butuh merombak ulang seluruh kode arsitektur dari awal, sistem itu bakal segera ditinggalkan penggunanya.
4. **Transparansi (*Transparency / Explanability*)**: Sistem cerdas nggak boleh jadi *black box* mutlak bagi pengambil keputusan. Sistem harus bisa menunjukkan jejak logika dan alasan mengapa ia merekomendasikan keputusan tertentu. Klien korporat nggak akan mau mempertaruhkan uang puluhan miliar hanya karena "komputer bilang begitu."
5. **Fleksibilitas (*Flexibility*)**: Skema representasi harus tahan banting terhadap modifikasi, skalabel saat volume data melonjak, dan mudah diintegrasikan dengan modul perangkat lunak lain.

---

## Empat Mazhab Menata Otak Komputer

Sekarang, mari kita masuk ke inti tekniknya, Sari. Bagaimana sebenarnya para ilmuwan komputer dan praktisi sistem cerdas mengodekan pengetahuan manusia ke dalam mesin? Secara umum ada empat teknik klasik yang fundamental:

### 1. Representasi Berbasis Aturan (*Rule-Based Systems*)
Ini teknik paling populer dan paling intuitif, terutama di sistem pakar konvensional. Pengetahuan direpresentasikan dalam bentuk pasangan kondisi-aksi: **IF <kondisi> THEN <konsekuensi/aksi>**.

Keunggulannya jelas: formatnya sangat dekat dengan cara pikir manusia, mudah dibaca, dan modular. Lo bisa menambah atau menghapus aturan tanpa merusak struktur dasar program. 

Mesin inferensi biasanya mengeksekusi aturan ini lewat dua strategi utama:
* **Forward Chaining (Data-Driven)**: Dimulai dari fakta-fakta yang diketahui di lapangan, lalu mesin mencari aturan yang kondisinya terpenuhi untuk menghasilkan fakta baru, terus bergerak maju sampai tujuan atau kesimpulan akhir tercapai. Ini cocok untuk masalah diagnosis awal, pemantauan, atau penilaian kelayakan instan.
* **Backward Chaining (Goal-Driven)**: Dimulai dari hipotesis atau tujuan akhir (misal: "Apakah lahan ini layak dibeli?"), lalu mesin bekerja mundur memeriksa apakah kondisi-kondisi pendukung yang disyaratkan dalam aturan terpenuhi oleh fakta yang ada. Ini sangat pas untuk verifikasi, audit, atau pembuktian hipotesis tertentu.

Tapi kelemahannya fatal kalau jumlah aturannya membludak jadi ribuan: bisa terjadi konflik antaraturan (*rule conflict*), inkonsistensi, dan kinerja pencarian yang melambat drastis jika basis pengetahuannya tidak terindeks rapi.

### 2. Jaringan Semantik (*Semantic Networks*)
Teknik ini memodelkan pengetahuan dalam bentuk graf berarah (*directed graph*). Objek, konsep, atau situasi direpresentasikan sebagai simpul (*node*), sedangkan hubungan antarsimpul direpresentasikan sebagai busur (*arc/link*) berlabel.

Ciri khas paling kuat dari jaringan semantik adalah adanya relasi hierarkis seperti **IS-A** (merupakan subkelas dari) dan **HAS-A** (memiliki bagian dari). Dari relasi ini muncul konsep pewarisan sifat (*property inheritance*). 

Misalnya:
* *Komersial* IS-A *Properti*.
* *Pusat Perbelanjaan* IS-A *Komersial*.
* Simpul *Properti* memiliki atribut: *dikenai pajak bumi dan bangunan*.
* Secara otomatis, tanpa perlu kita definisikan ulang, mesin tahu bahwa *Pusat Perbelanjaan* juga pasti *dikenai pajak bumi dan bangunan* karena mewarisi atribut dari leluhur hierarkinya.

Pendekatan ini sangat visual, natural untuk menyusun taksonomi, dan hemat ruang memori karena prinsip pewarisan tadi. Namun, jaringan semantik murni sering kali kesulitan merepresentasikan kuantifikasi logika formal (seperti konsep "semua" atau "ada beberapa") serta bisa menjadi sangat semrawut seperti sarang laba-laba raksasa jika relasinya terlalu kompleks.

### 3. Representasi Frame (*Frames*)
Digagas oleh Marvin Minsky di era 1970-an, *frame* adalah struktur data yang mengorganisasi pengetahuan berbasis stereotipe atau prototipe dari suatu objek atau situasi. Kalau lo familiar dengan konsep *Object-Oriented Programming* (OOP), *frame* ini adalah leluhur konseptualnya.

Sebuah *frame* terdiri dari kumpulan slot (*slots*), dan setiap slot bisa diisi oleh nilai tertentu (*fillers*). Slot bisa berisi:
* Nilai atribut sederhana (nama, ukuran, lokasi).
* Hubungan ke frame lain (sub-frame).
* Nilai bawaan (*default value*): nilai yang diasumsikan benar kecuali ada bukti sebaliknya. Misalnya, frame *Kantor Standar* punya nilai bawaan *ketinggian plafon = 2,8 meter*.
* Prosedur penanganan (*demons/procedural attachments*): potongan kode yang otomatis dieksekusi saat slot diakses atau dimodifikasi, seperti *if-needed* (dijalankan saat nilai slot kosong dan harus dihitung) atau *if-added* (dijalankan saat ada nilai baru dimasukkan untuk memicu validasi integritas).

Kekuatan utama *frame* adalah kemampuannya menangani ekspektasi dunia nyata lewat nilai bawaan dan kemudahan pemodelan objek kompleks yang terstruktur.

### 4. Logika Formal (*Formal Logic*)
Ini pendekatan paling murni, matematis, dan memiliki landasan teoretis paling kokoh. Ada dua cabang utama:
* **Logika Proposisional (*Propositional Logic*)**: Pernyataan deklaratif yang hanya bernilai benar (*True*) atau salah (*False*), dihubungkan oleh operator logika standar (AND, OR, NOT, Implikasi, Ekuivalensi). Kelemahannya, logika proposisional sangat terbatas karena tidak bisa melihat struktur internal kalimat; ia hanya memperlakukan sebuah kalimat utuh sebagai satu simbol tunggal.
* **Logika Predikat Orde Pertama (*First-Order Predicate Logic / FOPL*)**: Jauh lebih ekspresif. FOPL memungkinkan kita memecah kalimat menjadi predikat, argumen/objek, fungsi, serta menggunakan kuantor universal, yang artinya untuk semua dan kuantor eksistensial, yang artinya ada yang memenuhi.

Dengan FOPL, kita bisa menuliskan aturan dengan ketepatan tanpa celah. Misalnya: "Untuk setiap properti X, jika X berada di kawasan cagar budaya Y, maka X tidak boleh dirobohkan."
Keunggulan FOPL adalah presisinya yang tanpa ambigu dan bukti penalarannya dapat dijamin kebenarannya secara matematis (*soundness and completeness*). Tapi bayarannya mahal: komputasinya sangat berat (*computationally expensive*), sulit dipahami oleh orang bisnis non-matematikawan, dan kaku jika dihadapkan pada ketidakpastian dunia nyata yang penuh area abu-abu.

---

## Kenyataan di Lapangan: Hibrida Adalah Kunci

Setelah membedah keempat teknik tadi, satu hal yang langsung gue sadari waktu menyusun draf proposal balasan buat Vina: **nggak ada satu pun teknik tunggal yang menang mutlak di segala lini**.

Sistem cerdas di dunia nyata hampir selalu mengadopsi pendekatan hibrida (*hybrid architecture*). Pola yang paling sering dipakai di industri:
1. Kita menggunakan **Frame** untuk menstrukturkan data objek portofolio aset properti klien (menyimpan slot spesifikasi fisik, nilai default biaya pemeliharaan per meter persegi, dan *demon* untuk menghitung amortisasi otomatis).
2. Frame-frame tersebut dihubungkan ke dalam **Jaringan Semantik** guna memodelkan hierarki kepemilikan holding, zona wilayah tata ruang kota, dan hubungan ketergantungan antar fasilitas infrastruktur.
3. Di atas struktur frame dan graf semantik itu, kita menancapkan mesin **Rule-Based** yang bertugas mengeksekusi logika bisnis, regulasi valuasi dinamis, dan strategi portofolio berdasarkan kondisi pasar terkini.

Dengan arsitektur hibrida ini, Aris nggak perlu memaksakan ratusan aturan IF-THEN yang rumit cuma untuk mendefinisikan relasi hierarkis kepemilikan aset, dan klien tetap mendapatkan laporan keputusan yang transparan serta mudah diaudit.

Tadi siang, gue menarik Vina ke meja rapat kecil di sudut lantai 28. Gue tunjukkan sketsa kasar arsitektur hibrida ini dan betapa bahayanya kalau kami menelan mentah-mentah janji vendor di LinkedIn itu. 

"Vin," kata gue pelan tapi tegas, "kalau kita janjikan dashboard pintar minggu depan tanpa membereskan ontologi dan representasi aturan valuasi mereka, sistem ini bakal merekomendasikan klien buat beli tanah sengketa cuma karena angkanya murah di spreadsheet. Dan saat itu terjadi, nama konsultan kita yang bakal hancur."

Vina terdiam beberapa detik, menatap tumpukan berkas data berantakan milik klien, lalu menarik napas panjang. Dia setuju mengubah narasi proposal ke klien: bukan lagi jualan "AI instan colok langsung jalan", melainkan fase rekayasa pengetahuan (*knowledge engineering phase*) untuk merapikan representasi aturan bisnis mereka terlebih dahulu sebelum mesin inferensi diaktifkan.

---

## Bahan Diskusi Kita, Sari

Melihat kasus kantor gue hari ini dan relevansinya sama bab representasi pengetahuan yang lagi kita pelajari, ada beberapa pertanyaan yang terus berputar di kepala gue. Gue mau tahu perspektif lo dari kacamata perancangan sistem dan riset tesis lo:

1. Di tengah gempuran tren *Generative AI* dan *Large Language Models* (LLM) yang berbasis representasi probabilistik/vektor laten (*sub-symbolic*), menurut lo apakah pendekatan representasi pengetahuan simbolik klasik (seperti *Rules*, *Frames*, dan *FOPL*) ini masih relevan untuk dipertahankan di sistem informasi cerdas enterprise? Di titik mana LLM gagal menggantikan peran logika simbolik dalam pengambilan keputusan kritis perusahaan?
2. Kalau lo dihadapkan pada situasi seperti yang dialami Aris, di mana *tacit knowledge* dari para pakar senior saling bertentangan satu sama lain (misalnya dua valuer senior punya heuristik yang bertolak belakang soal faktor risiko tanah di kawasan suburban), metodologi atau teknik apa yang paling tepat untuk mendamaikan (*reconcile*) dan merepresentasikannya ke dalam basis pengetahuan tanpa menghilangkan nuansa keahlian mereka?
3. Dari sudut pandang efisiensi inferensi versus transparansi, skema representasi hibrida seperti apa yang paling optimal lo terapkan pada dataset digital lo (seperti GPBSales, dataset penjualan buku digital lo yang sempat lo ceritakan tempo hari) kalau lo dituntut membuat modul rekomendasi penentuan harga promo otomatis yang keputusannya harus bisa dipertanggungjawabkan ke pihak penerbit?

Mikirin yang nomor satu, gue jadi ingat debat panjang Aris sama dirinya sendiri waktu nyusun draf proposal tadi sore.

Jam tujuh malam. Dari dapur kedengaran suara air mendidih, dan satu halaman catatan soal frame dan slot masih setia nunggu gue sebelum makan. Selamat nyicil modulnya, Sar.

Nik
