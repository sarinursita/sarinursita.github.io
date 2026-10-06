---
title: "Catatan Nik: Ketika \"Yang Penting Jalan\" Berubah Jadi Bencana Ratusan Juta"
subtitle: "Vendor bilang sistemnya sudah selesai seratus persen karena semua fiturnya bisa diklik. Dua minggu kemudian tim marketing balik nyatet di Google Sheets pribadi, dan gue baru ngerti kenapa dari bab satu Sommerville."
type: blog
date: 2026-10-07T06:39:11.641535+07:00
draft: false
ws_chat: 1546
ws_msg: 21364
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "software-design"]
summary: "Kode yang jalan belum tentu software. Dari empat atribut kualitas Sommerville sampai vendor yang milih bungkam soal celah keamanan demi termin pembayaran."
hook: "\"Sistem sudah selesai 100%, semua fiturnya bisa diklik.\" Sistem mahal itu sekarang terbengkalai, dan bukan karena error."
---

Sar, rumah lagi senyap banget: Dylan udah balik ke asrama, jadi yang nemenin gue malam ini cuma *mug* teh *chamomile* anget sama catatan silabus kuliah. Kelas *Software Design* perdananya malam ini, dan gue nyempetin baca bab satu bukunya Sommerville dulu biar gak blank pas dosennya mulai ngomong. 

Jujur, modul di LMS kampus gue emang masih digembok rapat sama prodi, tapi begitu baca *Software Engineering 10th edition* bab pembuka, kepala gue langsung cenat-cenut. Kenapa? Karena apa yang ditulis Sommerville tuh bukan sekadar teori akademis di atas menara gading. Ini cerminan nyata dari kekacauan kantor konsultan properti SCBD tempat gue kerja seminggu terakhir ini. 

Lo tahu kan, pasca Bram cabut tempo hari, manajemen regional Singapura makin agresif maksain standardisasi sistem. Nah, minggu lalu kantor kita resmi kena getahnya gara-gara cara pandang purba yang mikir kalau *software* itu cuma urusan teknis baris kode. Gue tumpahin semua unek-unek gue di sini ya, biar kita berdua dapet *sense* nyata sebelum kelas dimulai.

---

## Kode Bagus Itu Cuma Pucuk Es Bergunung-gunung

Banyak orang awam, termasuk para bos di kantor gue, mikir kalau *software* itu ya aplikasi yang bisa lo klik ikonnya terus kebuka di layar. Titik. Padahal Sommerville di Bab 1 udah nampol paradigma sempit kayak gitu. *Software* itu bukan sekadar kode program yang berhasil di-*compile*. *Software* adalah kesatuan utuh antara program yang bisa dieksekusi, dokumentasi lengkap arsitektur dan desainnya, serta data konfigurasi yang bikin sistem itu bisa jalan dengan benar di lingkungan operasionalnya.

Karakteristiknya unik banget kalau dibandingin sama produk manufaktur gedung apartemen atau ruko yang tiap hari gue pasarin. *Software* itu *intangible*, gak ada wujud fisiknya. Kita gak bisa ngetuk bodinya buat ngecek apakah besinya kokoh atau kopong. Selain itu, *software* itu direkayasa (*engineered*), bukan diproduksi massal di pabrik dengan cetakan mesin. 

Satu hal yang paling bikin gue merinding dari Sommerville: *software doesn't wear out, but it deteriorates as it is changed*. Kalau lift di gedung kantor aus karena gesekan roda dan kabel baja seiring berjalannya waktu, *software* justru rusak gara-gara tangan manusia yang ngutak-ngatik kodenya tanpa rekayasa yang bener. Setiap kali ada perubahan *requirement* yang ditambal sembarangan tanpa mikirin struktur aslinya, kompleksitasnya meledak dan sistemnya menua sebelum waktunya.

Di kantor gue kemarin, divisi *tenant management* heboh luar biasa. Tim IT regional nunjuk *vendor software house* lokal buat bikin sistem *customized* alias *bespoke* buat mengelola data sewa perkantoran premium. Tujuannya keren, mau bikin portal komparasi harga sewa dan *matching* investor. Tapi apa yang terjadi pas diserahterimakan? 

Vendor bilang, "Sistem sudah selesai 100% karena semua fitur di dokumen kontrak sudah bisa diklik." Tapi pas kita minta manual integrasinya, mereka gelagapan. Gak ada kamus data, gak ada dokumentasi skema database, bahkan konfigurasi *endpoint API* dibikin *hardcoded* di dalem kode programnya. 

Begitu tim gue di marketing mau narik data *historical comps* buat bikin proyeksi ke calon investor, datanya acak-acakan karena konfigurasi *database* gak sinkron sama format input kita. Di situ gue sadar sejelas-jelasnya: tanpa dokumentasi yang bener dan konfigurasi yang rapi, baris-baris kode canggih mereka itu gak lebih dari tumpukan sampah digital.

---

## "Sekadar Ngoding" vs Rekayasa Perangkat Lunak: Jurang Pemisah yang Bikin Boncos

Sering banget orang menyamakan antara *programming* sama *software engineering*. Padahal perbedaannya tuh kayak tukang yang bisa masang bata doang dibanding insinyur sipil yang merancang struktur gedung tahan gempa 40 lantai.

*Programming* itu fokusnya personal dan sempit: gimana caranya bikin logika program jalan dan ngeluarin *output* yang bener buat masalah tertentu saat itu juga. Lo duduk, ngetik kode, selesai. 

Tapi *software engineering*? Sommerville negasin kalau ini adalah disiplin *engineering* yang menangani seluruh siklus hidup perangkat lunak. Tujuannya ada tiga pilar utama: mengelola kompleksitas, mengantisipasi perubahan yang pasti terjadi di masa depan, serta mengendalikan biaya dan jadwal biar gak boncos.

Ada empat aktivitas fundamental yang gak boleh dipotong kompas dalam rekayasa perangkat lunak:
1. **Specification**: Mendefinisikan apa yang harus dilakukan sistem dan batasan operasionalnya. Bukan cuma maunya bos pas lagi *meeting*, tapi bener-bener batasan fungsional dan non-fungsionalnya.
2. **Development**: Proses memproduksi arsitektur, desain, dan kode programnya.
3. **Validation**: Memastikan bahwa sistem yang dibangun bener-bener sesuai sama apa yang dibutuhkan pengguna (*are we building the right product?*) dan berfungsi tanpa cela (*are we building the product right?*).
4. **Evolution**: Memodifikasi sistem buat merespons perubahan kebutuhan bisnis dan pasar seiring berjalannya waktu.

Kalau kita pinjam perspektif Roger Pressman, ada empat dimensi proyek yang wajib dipegang: *people, product, process, project*. Kemarin vendor kantor gue cuma fokus ke *product* setengah matang, tapi abai sama *process* dan gak pernah komunikasi secara manusiawi sama *people* yang bakal jadi pengguna akhir.

Waktu gue tanya ke teknikal representatif vendornya, "Kenapa pas ada perubahan skema komisi *broker* kemarin, sistemnya langsung *crash* total?" Jawabannya enteng banget, "Iya Bu, soalnya kami bikin logikanya langsung nempel di *controller*, jadi kalau diubah satu, variabel lain kena efek domino." 

Astaga, gue yang anak marketing tapi lagi belajar MMSI langsung tepok jidat di depan layar Zoom. Mereka ngoding kayak lagi ngerjain tugas mingguan semester satu sarjana, bukan bangun sistem kelas *enterprise*. Mereka gak nerapin rekayasa perangkat lunak, mereka cuma sekadar ngoding biar kelihatan jalan pas demo di depan direksi.

---

## Empat Cermin Kualitas yang Menampar Proyek Kantor Gue

Sommerville nyebutin ada empat atribut esensial yang membedakan perangkat lunak yang dikembangkan secara profesional sama yang dikerjain ala kadarnya. Pas gue baca bagian ini, gue beneran ngerasa Sommerville lagi nyindir sistem baru di kantor gue. Coba lo bedah satu per satu bareng gue, Sar.

### 1. Maintainability (Kemudahan Pemeliharaan)
*Software* harus dirancang sedemikian rupa supaya bisa berevolusi ngikutin perubahan kebutuhan klien. Dunia properti itu regulasinya cair banget, dari aturan pajak PPN properti sampai regulasi zonasi daerah. Kalau tiap ada perubahan regulasi pajak kita harus bongkar ulang puluhan file kode karena strukturnya semrawut (*spaghetti code*), sistem itu udah gagal total dari aspek *maintainability*. *Software* yang bagus itu modular. Ubah satu komponen, komponen lain tetap berdiri kokoh tanpa goyang.

### 2. Dependability & Security (Keandalan dan Keamanan)
Ini harga mati. Keandalan mencakup keandalan sistem (*reliability*), ketersediaan (*availability*), dan keamanan (*security*). Sistem gak boleh gampang tumbang, dan kalaupun terjadi kegagalan (*failure*), sistem harus bisa memulihkan diri tanpa ngerusak integritas data fisik maupun finansial. 

Nah, sistem sewa kantor kita kemarin malah nampilin data nilai transaksi sewa gedung konglomerat tertentu ke pengguna lain cuma gara-gara ada *session token* yang gak divalidasi ulang di sisi *server*. Bayangin kalau bocor ke publik atau kompetitor, nama baik konsultan kita bisa hancur lebur dalam satu malam.

### 3. Efficiency (Efisiensi)
Sistem gak boleh maruk sumber daya. Sommerville nekanin bahwa efisiensi itu bukan cuma soal penggunaan memori atau siklus CPU, tapi juga kecepatan respons dan konsumsi energi. Portal baru kantor kita kemarin beratnya minta ampun. Begitu tiga puluh agen properti di Jakarta buka *dashboard* secara bersamaan buat ngecek ketersediaan lantai kantor di koridor Sudirman, *server*-nya langsung megap-megap, *loading* berputar tanpa henti kayak kincir angin. Itu tanda nyata kalau manajemen *query* dan algoritmanya gak direkayasa dengan perhitungan efisiensi yang matang.

### 4. Acceptability (Diterima Pengguna)
Ini yang paling krusial buat orang bisnis kayak gue. *Software* harus *understandable, usable, and compatible* sama sistem kerja pengguna. Antarmuka sistem baru kita rumitnya gak ketulungan. Mau masukin satu data prospek klien aja butuh tujuh kali klik di halaman yang terpisah-pisah tanpa ada petunjuk yang jelas. 

Akibatnya apa? Temen-temen marketing balik lagi nyatet di *spreadsheet* Google Sheets pribadi mereka secara diam-diam. Sistem mahal ratusan juta itu akhirnya terbengkalai gak dipakai. Secara teknis programnya ada, tapi secara sosiologis dan operasional, produk itu ditolak mentah-mentah.

---

## Garis Tipis Etika: Dari Therac-25 Sampai Manipulasi Data Tenant

Nah, materi yang paling bikin gue merenung panjang pas baca bahan RPS minggu ini adalah soal etika rekayasa perangkat lunak. Dosen gue ngingetin di silabus kalau *software* itu bukan ruang hampa. Dia menyentuh keselamatan nyawa, privasi, uang, dan kepercayaan publik.

Gue jadi inget kasus klasik yang sering dibahas di literatur: insiden mesin terapi radiasi Therac-25 di tahun 1980-an. Gara-gara *race condition* sepele di kodenya dan ketiadaan sistem pengaman fisik (*hardware interlock*), pasien kanker bukannya sembuh malah dapet overdosis radiasi mematikan ribuan kali lipat. Atau meledaknya roket Ariane 5 tahun 1996 cuma berselang puluhan detik setelah meluncur gara-gara *bug* konversi data angka 64-bit ke 16-bit yang bikin sistem pemandunya macet total. Bencana jutaan dolar dan hilangnya nyawa manusia cuma karena kelalaian teknis dan arogansi bahwa kodenya "pasti aman".

Di dunia profesional modern, etika ini dituangkan dalam *ACM/IEEE Software Engineering Code of Ethics*. Ada delapan prinsip utama yang menuntut praktisi buat selalu mengutamakan kepentingan publik (*Public interest*), bersikap adil ke klien dan pemberi kerja, menjaga standar kualitas produk tertinggi, menjaga independensi penilaian profesional, mempraktikkan manajemen yang beretika, memajukan martabat profesi, mendukung kolega, serta terus belajar seumur hidup.

Empat isu etika praktis yang ditekankan Sommerville bener-bener nampar kenyataan di depan mata gue:
* **Confidentiality**: Menjaga kerahasiaan data klien tanpa memanfaatkannya buat keuntungan pribadi.
* **Competence**: Kejujuran untuk gak menerima pekerjaan yang jelas-jelas di luar kapasitas dan keahlian teknis kita.
* **Intellectual Property**: Menghargai hak kekayaan intelektual, gak comot pustaka kode bajakan atau melanggar lisensi *open source*.
* **Computer Misuse**: Gak menyalahgunakan wewenang dan keterampilan teknis buat merugikan orang lain atau membobol sistem.

Spill drama kantor yang bikin gue geram kemarin: gue gak sengaja denger obrolan petinggi vendor sama tim IT regional. Ternyata, vendor itu sadar betul ada celah keamanan fatal di modul autentikasi sistem properti kita dua hari sebelum jadwal *go-live*. Tapi kalau mereka nunda rilis buat nambal celah itu, mereka bakal kena denda penalti keterlambatan kontrak dan termin pembayaran kuartal tiga mereka gak cair. 

Tahu apa yang mereka lakuin? Mereka milih bungkam! Mereka nutupin *bug* itu pake trik manipulasi tampilan sementara di *front-end*, lalu mendesak orang kantor gue buat nandatanganin berita acara serah terima (*acceptance sign-off*). 

Mereka mempertaruhkan kerahasiaan data ribuan klien demi ngejar target finansial jangka pendek. Ini pelanggaran telak terhadap prinsip *Public interest* dan *Product quality*. Mereka melanggar pilar integritas profesional paling mendasar cuma demi menyelamatkan kantong sendiri.

---

## Bahan Renungan Buat Kita Berdua

Pas gue baca bagian akhir catatan pengantar ini, gue langsung kepikiran lo, Sar. Lo udah khatam banget ngebangun dan ngerawat sistem sendiri, yang tiap hari lo *deploy*, lo pantau, dan lo tambal sendiri kalau ada yang rusak. Pasti lo ngerasain banget betapa pedihnya kalau salah satu atribut kualitas Sommerville itu diabaikan.

Mumpung forum LMS sebentar lagi kebuka dan sistem kelas gue nuntut analisis berbasis kasus nyata, gue mau lempar beberapa pertanyaan reflektif buat mengasah pisau analisa kita berdua:

1. Kalau lo ada di posisi gue pas tahu vendor sengaja nutupin celah keamanan demi ngejar termin pembayaran dan terhindar dari penalti kontrak, langkah mitigasi teknis dan organisasional apa yang paling etis buat diambil tanpa bikin relasi bisnis meledak begitu aja?
2. Di antara empat atribut utama Sommerville (*maintainability, dependability/security, efficiency, acceptability*), menurut lo mana yang paling sering dikorbankan developer pas dihadapkan pada *deadline* manajemen yang gak masuk akal? Berdasarkan pengalaman lo ngerawat aplikasi lo sendiri, gimana cara lo ngejaga keseimbangan keempatnya?
3. Kenapa kebanyakan organisasi korporat masih aja terjebak nganggep *software development* itu cuma sekadar urusan *programming* murah yang bisa di-*outsource* ke penawar terendah, dan apa argumen terkuat lo dari kacamata manajemen sistem informasi buat ngubah pola pikir purba kayak gitu?

Coba lo renungin sambil minum kopi hangat di sana. Gue mau lanjut baca bab berikutnya sebelum jam tidur Dylan di asrama mati lampu dan dia telepon buat *bedtime catch-up*.

Warmest hug from the rainy city 🩷  
Nik
