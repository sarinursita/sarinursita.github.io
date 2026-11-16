---
title: "Catatan Nik: Formulir Empat Belas Kolom, Excel Rahasia Mas Danu, dan Seni Bertanya yang Benar"
subtitle: "Gue kira sistem baru cukup diwawancarakan ke para manajer, sampai Mas Danu membuka spreadsheet yang dia pakai tiap malam karena formulir kami minta empat belas kolom."
type: blog
date: 2026-11-18T05:00:00+07:00
draft: true
ws_chat: 1731
ws_msg: 21971
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "software-design", "requirement-engineering", "catatan-nik"]
summary: "Pekan ini materinya proses requirement engineering: empat aktivitas yang berputar, sumber dan masalah elicitation, delapan teknik penggalian beserta batasnya, lalu cara menyaring bahan mentah jadi kebutuhan yang bisa diuji. Di kantor gue, portal kunjungan klien yang baru rilis langsung ditinggal agen lapangan karena yang ditanya cuma para manajer."
hook: "Portal itu baru sehari dipakai, dan spreadsheet rahasia Mas Danu sudah balik lagi ke meja."
---

Mas Danu menggeser kursinya mundur, lalu memutar layar laptop lamanya ke arah meja rapat lantai 28. Di layar itu tidak ada portal web mahal yang baru diluncurkan tim konsultan. Yang terpampang cuma satu lembar *spreadsheet* kumal berjudul *Catatan_Sewa_Real_Jangan_Dihapus.xlsx*.

Vina, yang duduk di sebelah gue sambil memegang cangkir kopi, langsung mengernyitkan dahi. Di depan kami, tiga orang manajer operasional klien yang dulu memvalidasi seluruh rancangan sistem tampak saling lirik dan berdeham pelan.

"Mas Danu," Vina membuka suara dengan nada diplomatis andalannya, "portal kunjungan klien kan sudah *live*. Tinggal buka lewat peramban ponsel, masukin detail unit, lalu klik *submit*. Kenapa tim sewa lapangan masih nyatet di lembar kerja terpisah?"

Mas Danu cuma tersenyum tipis, jenis senyum lelah dari orang yang setiap hari harus jalan kaki menyusuri koridor gedung komersial sambil mendampingi calon penyewa. "Mbak Vina, form baru itu minta empat belas kolom wajib diisi. Ada estimasi anggaran lima tahun, profil korporasi induk, sampai proyeksi kebutuhan daya listrik gedung. Kemarin ada calon klien masuk lobi. Waktunya cuma tujuh menit buat ngecek ruang kosong lantai sembilan sebelum harus ke bandara. Kalau dipaksa berdiri di lobi demi ngisi empat belas kolom itu, dia bakal kabur ke gedung seberang. Makanya dua angka gue catat di kertas, gue ketik ulang di lembar kerja ini pas malam, dan portal kantor gue biarkan kosong."

Ruang rapat mendadak senyap. Tiga manajer klien yang dulu diwawancarai panjang lebar waktu perancangan sistem tiba-tiba sibuk membaca map masing-masing.

Gue langsung teringat materi kuliah pertemuan tujuh yang baru gue baca semalam di sela-sela rekap kampanye bulanan. Gue sering kali merasa sudah merancang solusi masa depan, padahal yang gue bangun cuma monumen megah yang lahir dari obrolan dengan orang yang salah.

---

## Membedakan Daftar Belanja dan Cara Bertanya ke Penghuni Rumah

Sesi enam isinya membedah *apa* itu kebutuhan, mulai dari memisahkan *functional requirement* alias fungsi nyata yang harus dijalankan sistem seperti tombol simpan atau kalkulasi tarif, sampai *non-functional requirement* yang mengatur kualitas kerja sistem seperti kecepatan respon dan standar keamanan data. Di situ juga dibahas level kebutuhan dari sudut pandang pengguna sampai ke spesifikasi teknis sistem.

Nah, sesi tujuh ini posisinya berpasangan tapi fokusnya beda total. Kalau sesi enam itu ibarat menyusun daftar belanja, sesi sekarang adalah seni mencari tahu cara bertanya ke penghuni rumah.

Masalah terbesarnya, penghuni rumah hampir tidak pernah bisa menjelaskan secara jernih apa yang sebenarnya mereka butuhkan. Kadang mereka cuma menyebut apa yang mereka inginkan saat itu, atau malah mengulang istilah keren yang mereka dengar di seminar tanpa paham dampaknya di dapur sendiri. Formatnya diskusi sinkronus dua arah, dan dosen pengampu memang mau melihat ketajaman argumentasi saat menghadapi kasus nyata di lapangan, bukan sekadar hafalan definisi baku.

Ian Sommerville membagi proses *Requirement Engineering* atau rekayasa kebutuhan perangkat lunak ke dalam empat aktivitas besar yang sifatnya berputar tanpa henti:

1. *Elicitation and analysis*, yaitu aktivitas menggali kebutuhan mentah dari para pemangku kepentingan lalu membedahnya menjadi informasi yang masuk akal. Ini fokus utama yang kita bahas hari ini.
2. *Specification*, yaitu proses menuangkan kebutuhan tersebut ke dalam dokumen terstruktur yang bisa diuji seperti dokumen spesifikasi kebutuhan perangkat lunak.
3. *Validation*, yaitu tahap verifikasi bersama pengguna untuk memastikan bahwa apa yang tertulis memang benar-benar sesuai dengan kenyataan operasional mereka.
4. *Requirements management*, yaitu tata kelola untuk melacak dan mengendalikan perubahan kebutuhan selama masa pengembangan sistem berlangsung.

Kenapa empat tahapan ini harus berjalan berulang dan haram hukumnya dianggap selesai dalam sekali jalan? Karena begitu proses penggalian tahap awal selesai, hampir selalu muncul tiga kejutan pahit: ada dua kebutuhan divisi yang saling bertubrukan, ada fitur idaman yang secara teknis mustahil dieksekusi dengan anggaran yang ada, dan mendadak muncul pemangku kepentingan baru yang selama ini tidak pernah diajak bicara. Kalau tim mengira penggalian tuntas di awal, semua bom waktu itu bakal meledak di tahap pengujian penerimaan pengguna saat biaya revisi kodenya sudah membengkak puluhan kali lipat.

---

## Menggali Apa yang Sudah Hidup di Lapangan

Kalau dipikir lagi, *requirement elicitation* itu cuma bahasa mentereng untuk pekerjaan detektif: menggali apa yang dibutuhkan sistem baru dari manusia, tumpukan berkas, dan kebiasaan kerja yang sebetulnya sudah lama berjalan.

Kata kuncinya ada pada frasa "sudah ada". Sistem baru jarang sekali berangkat dari ruang hampa. Kebutuhan operasional itu biasanya sudah berdenyut di kebiasaan harian staf, di rumus-rumus tersembunyi dokumen lembar kerja, di kepala para senior, atau di sistem warisan lama yang penuh dengan aturan tidak tertulis. Tugas tim analis bukan menciptakan roda baru dari imajinasi, melainkan memindahkan realitas yang berserakan itu ke atas meja kerja.

Biar tidak tersesat seperti kasus formulir empat belas kolom Mas Danu tadi, ada empat sumber kebutuhan yang wajib disisir secara berimbang:

1. **Orang**: Ini mencakup pengguna langsung di garis depan, manajer penanggung jawab, operator entri data, hingga pihak luar yang ikut terdampak sistem.
2. **Dokumen**: Berupa prosedur standar operasional resmi, formulir kertas manual, kebijakan direksi, klausul kontrak klien, hingga berkas keluhan pelanggan yang masuk ke meja bantuan.
3. **Sistem lama**: Rekaman log transaksi, tabel basis data lama, dan alur kerja aplikasi sebelumnya. Data historis ini adalah saksi paling jujur karena angka tidak pernah berbohong untuk menutupi kemalasan kerja.
4. **Pengetahuan domain**: Aturan main baku, standar hukum, atau kepatuhan regulasi yang berlaku khusus di industri tersebut, seperti regulasi sewa properti komersial, perpajakan, atau standar akuntansi perbankan.

Dosa paling fatal bagi tim pengembang pemula adalah cuma menyambangi sumber nomor satu, itu pun hanya memilih orang-orang berstatus manajer yang mudah ditemui di ruang rapat berpendingin udara. Agen lapangan seperti Mas Danu ditinggal di luar pintu rapat, dan hasilnya adalah portal canggih yang langsung mandek di hari pertama peluncuran.

---

## Empat Tembok Besar yang Menghadang Proses Penggalian

Sommerville mencatat ada empat kesulitan klasik yang membuat proses penggalian kebutuhan selalu penuh drama. Ini langganan keluar di soal esai, Sar, jadi perhatikan baik-baik dinamika di baliknya.

Pertama, pemangku kepentingan sering kali tidak tahu apa yang mereka butuhkan. Mereka sangat paham bagian mana dari pekerjaan harian yang bikin punggung pegal atau memicu omelan atasan, tapi mereka buta soal bentuk solusi teknologinya. Kalau lo mendatangi mereka lalu bertanya klise seperti "fitur apa yang mau ditambahin di aplikasi baru nanti?", jawabannya pasti cuma permintaan dangkal seperti tombol ekspor otomatis atau tampilan warna-warni yang tidak menyentuh akar masalah.

Kedua, perbedaan bahasa antarpihak di dalam satu organisasi. Bu Retno dari bagian keuangan mengartikan kata "validasi" sebagai verifikasi kelengkapan faktur pajak dan bukti potong legal. Di sisi lain, Aris si analis data menganggap "validasi" hanyalah pengecekan apakah kolom input angka tidak diisi huruf. Kalau tim pengembang tidak menyusun kamus istilah bersama sejak awal, satu kalimat kebutuhan dalam dokumen bakal dipahami dengan tiga cara berbeda oleh orang keuangan, pemasar, dan pemrogram.

Ketiga, benturan kebutuhan yang tak terhindarkan antarbagian. Tim penjualan pimpinan Vina mau formulir seringkas mungkin agar prospek cepat masuk tanpa hambatan administrasi. Sebaliknya, Pak Fajar di tim keuangan butuh rincian sedalam mungkin demi mitigasi risiko kredit dan kepatuhan audit. Dua kubu ini tidak ada yang berniat jahat; mereka cuma menjalankan mandat divisinya masing-masing. Di titik ini, tugas rekayasa kebutuhan bukan mencari kompromi abu-abu yang membingungkan, melainkan memfasilitasi keputusan bisnis yang tegas, disepakati pimpinan, dan dicatat alasannya.

Keempat, dinamika politik dan struktur kekuasaan organisasi. Kehadiran sistem teknologi baru sering kali mengubah alur distribusi informasi dan menggeser wewenang pengambilan keputusan. Pihak yang merasa kendalinya terpangkas oleh transparansi sistem baru biasanya akan melakukan penolakan halus. Menariknya, resistensi politik ini hampir selalu dibungkus rapi dalam rupa keluhan teknis yang terdengar rasional, misalnya berdalih antarmukanya membingungkan atau menuntut integrasi rumit yang sebenarnya tidak mendesak.

Belum lagi kalau kita menghitung faktor perubahan lingkungan eksternal. Di tengah proyek yang memakan waktu berbulan-bulan, regulasi pajak bisa terbit mendadak, skema komisi pasar bergeser, atau kompetitor meluncurkan skema sewa baru. Kebutuhan yang kita catat dengan rapi di bulan pertama bisa basi total di bulan keenam.

---

## Ragam Teknik Penggalian dan Batas Kekuatannya

Materi kuliahnya menekankan evaluasi dan argumentasi pemilihan teknik. Dosen gue pasti nggak akan puas kalau lo cuma membeberkan daftar nama teknik tanpa bisa menjelaskan kapan teknik itu bersinar dan di mana batas kelemahannya.

Teknik pertama adalah wawancara. Modelnya terbagi dua, yaitu wawancara tertutup dengan daftar pertanyaan kaku yang cocok kalau ruang lingkup masalah sudah sangat jelas dan waktu terbatas, serta wawancara terbuka yang memberi ruang eksplorasi bebas untuk membedah wilayah yang belum pernah dipetakan sebelumnya. Keunggulannya cepat, murah, dan efektif menangkap alasan personal di balik suatu kebiasaan. Batasannya sangat bergantung pada kelihaian pewawancara, rawan dipenuhi opini subjektif yang sekadar mencerminkan keinginan pribadi bukan kebutuhan sistem, dan sering kali menghasilkan dua kesaksian yang saling bertolak belakang tanpa disadari oleh narasumbernya sendiri.

Teknik kedua adalah observasi langsung alias pendekatan etnografi, yaitu mengamati tindakan nyata pengguna di stasiun kerja mereka ketimbang mendengarkan presentasi mereka di ruang rapat. Kekuatan terbesarnya adalah membongkar fakta kerja nyata yang tidak akan pernah diakui di sesi wawancara resmi, persis seperti penemuan bahwa Mas Danu dan kawan-kawan lapangan diam-diam mengandalkan berkas *Catatan_Sewa_Real_Jangan_Dihapus.xlsx*. Namun, batasannya cukup nyata: teknik ini memakan waktu berhari-hari, memicu bias perilaku sesaat karena orang cenderung bekerja lebih rapi saat merasa diawasi, dan rawan melewatkan prosedur penanganan krisis langka yang kebetulan tidak terjadi selama masa pemantauan.

Teknik ketiga adalah lokakarya bersama atau *Joint Application Development* yang mempertemukan berbagai pemangku kepentingan lintas divisi di satu ruangan bersama seorang fasilitator netral. Nilai plusnya, benturan kepentingan antarbagian bisa langsung diadu dan diselesaikan saat itu juga sehingga menghasilkan kesepakatan tertulis yang mengikat. Batasannya, sesi ini gampang dibajak oleh pejabat yang punya suara paling dominan, menenggelamkan aspirasi staf lapangan yang pasif, serta menuntut fasilitator yang sangat tegas dalam memotong debat kusir.

Teknik keempat adalah kuesioner atau angket daring. Teknik ini sangat efisien untuk menjaring opini ratusan agen properti di berbagai kantor cabang dengan biaya rendah, dan sangat pas digunakan untuk memvalidasi tren yang sudah ditemukan sebelumnya. Batasannya, pertanyaan yang ambigu tidak bisa diklarifikasi di tengah jalan, jawabannya kerap dangkal karena pengguna ingin cepat selesai, dan tingkat pengembalian formulir sering kali sangat menyedihkan.

Teknik kelima adalah analisis dokumen resmi perusahaan. Tim memeriksa tumpukan prosedur operasional baku, formulir cetak, memo internal, hingga laporan rekap penalti keterlambatan sewa. Keunggulannya murah, tidak mengganggu operasional staf, dan mampu mengungkap batasan hukum yang terlupakan oleh tim bisnis. Kelemahannya, tumpukan berkas itu kerap berdebu dan tidak pernah diperbarui, sehingga hanya menggambarkan kondisi ideal di atas kertas yang sudah lama ditinggalkan di lapangan.

Teknik keenam adalah analisis sistem dan data historis, yaitu memeriksa struktur tabel basis data lama, catatan log eror, dan riwayat transaksi bertahun-tahun. Ini adalah sumber fakta paling objektif tanpa polesan diplomasi politik kantor. Kalau data log menunjukkan bahwa delapan puluh persen agen mengosongkan kolom isian tertentu, itu adalah bukti valid bahwa data tersebut tidak realistis untuk dikumpulkan di lapangan. Namun batasannya, sistem lama bisa saja mewariskan kebiasaan buruk atau jalan pintas darurat masa lalu yang seharusnya dibersihkan, bukan malah ditiru ke sistem anyar.

Teknik ketujuh adalah pembuatan prototipe awal, yaitu membangun tiruan antarmuka kasar tanpa fungsi logika rumit di belakangnya untuk memancing umpan balik langsung. Orang biasanya gagap saat disuruh mendeskripsikan kebutuhan dari nol, tapi mereka mendadak sangat vokal dan kritis begitu disodori barang visual yang bisa diklik. Kelemahannya, pengguna kerap terdistraksi memperdebatkan pemilihan warna tombol ketimbang alur data, rawan salah paham mengira prototipe itu sudah siap dipakai besok pagi, serta membutuhkan waktu ekstra untuk pengembangannya.

Teknik kedelapan adalah penyusunan skenario tugas dan use case, yaitu mendokumentasikan langkah demi langkah interaksi pengguna dalam menuntaskan satu misi operasional, lengkap dengan cabang kondisi gagalnya. Kekuatannya luar biasa dalam memaksa tim memikirkan skenario darurat yang biasanya luput dari obrolan santai, menjadikannya sarana paling hemat untuk mendeteksi celah aturan bisnis yang tersembunyi.

Kunci rahasia di dunia konsultan sebetulnya sederhana: jangan pernah mengandalkan satu teknik tunggal. Formula yang waras adalah gabungan bertahap. Lo mulai dengan wawancara manajemen untuk memetakan arah strategis, terjun lewat observasi lapangan demi memotret kerja nyata, bedah dokumen dan data historis untuk mengonfirmasi batasan angka, kumpulkan para pihak di lokakarya demi membereskan perselisihan, petakan skenario use case buat mengunci alur, dan tutup dengan prototipe kasar guna memastikan pemahaman visual kedua belah pihak sudah selaras.

Kalau dosen besok melempar pertanyaan studi kasus bertipe "teknik apa yang bakal lo ambil dan apa alasannya", jangan sekali-kali menjawab berdasarkan preferensi pribadi lo. Bedah dulu anatomi masalahnya: kalau problem utamanya adalah friksi antarbagian, jawabannya lokakarya terpandu; kalau problemnya adalah kesenjangan antara aturan resmi dan kebiasaan lapangan, observasi dan audit log data adalah harga mati.

---

## Menyaring Bahan Mentah Menjadi Kebutuhan Valid

Proses penggalian cuma menghasilkan tumpukan materi mentah yang berantakan: rekaman suara wawancara, corat-coret papan tulis, tumpukan tangkapan layar, dan lembar keluhan staf. Langkah berikutnya adalah *requirement analysis*, yaitu dapur pengolahan yang menyaring kotoran dari bahan mentah tersebut hingga berubah menjadi daftar kebutuhan sistem yang siap dieksekusi pemrogram.

Ada tujuh tahapan sistematis di ruang analisis ini:

Pertama, klasifikasi kebutuhan. Di tahap ini, tumpukan catatan dipilah ke dalam empat laci rapi: fungsi sistem, batasan performa non-fungsional, kendala teknis lingkungan operasi, dan kebutuhan arsitektur data. Pisahkan juga kepemilikan kebutuhan berdasarkan peran aktor yang akan mengoperasikannya.

Kedua, deteksi duplikasi dan konflik. Analis data harus jeli menemukan dua divisi yang sebetulnya meminta barang serupa namun memakai kosa kata berbeda, atau justru memakai satu istilah yang sama persis untuk dua tujuan yang saling bertentangan.

Ketiga, negosiasi terarah. Ketika konflik kepentingan terdeteksi, tim analis memfasilitasi kompromi bisnis. Poin krusialnya: opsi mana pun yang akhirnya terpilih harus didokumentasikan secara transparan, lengkap dengan alasan logis kenapa opsi pihak yang kalah terpaksa dikesampingkan, agar tidak ada dendam operasional di kemudian hari.

Keempat, penentuan prioritas menggunakan kerangka kerja baku seperti MoSCoW, yaitu membagi kebutuhan menjadi *Must have* untuk fitur vital tanpa kompromi, *Should have* untuk fungsi krusial yang masih bisa ditunda lewat prosedur manual sementara, *Could have* untuk pemanis yang dikerjakan jika ada sisa waktu, dan *Won't have* untuk permintaan yang disepakati batal dikerjakan pada rilis berjalan. Tanpa ketegasan memotong skala prioritas, semua orang akan mengklaim permintaannya berkategori wajib, dan proyek bakal kolaps dihantam beban kerja.

Kelima, pemodelan visual. Alur kerja diterjemahkan ke dalam diagram kasus penggunaan, pemetaan diagram aktivitas, atau sekadar bagan alir sederhana. Representasi visual ini adalah senjata ampuh untuk mendeteksi jalan buntu logika yang kerap tersamar saat hanya ditulis dalam rentetan paragraf panjang.

Keenam, verifikasi kelengkapan empat jalur utama. Untuk setiap fungsi yang dibangun, tim wajib merumuskan empat skenario: jalur berhasil saat semua data ideal, jalur gagal saat validasi ditolak sistem, jalur pembatalan saat pengguna mendadak keluar di tengah proses, dan kondisi penanganan data kosong. Jalur gagal dan data kosong inilah yang paling sering dilupakan, sampai akhirnya meledakkan eror fatal di layar monitor klien.

Ketujuh, penelusuran balik atau *requirements traceability*. Setiap butir kebutuhan diberi kode identitas unik yang bisa dilacak silsilahnya: kebutuhan ini lahir dari wawancara pemangku kepentingan mana, mengacu pada klausul prosedur operasional yang mana, dan menjawab tujuan strategis bisnis yang mana. Dengan pelacak ini, tidak ada fitur siluman yang tiba-tiba diselipkan pemrogram tanpa dasar kebutuhan bisnis yang sah.

---

## Memisahkan Penggalian dari Analisis di Dunia Nyata

Banyak analis amatir mencampuradukkan penggalian dan analisis di waktu yang bersamaan. Ini jebakan psikologis yang berbahaya.

Penggalian itu murni urusan mengumpulkan fakta objektif. Pertanyaan panduannya adalah: apa yang sebetulnya orang-orang ini kerjakan, ucapkan, dan butuhkan di lapangan? Sementara analisis adalah proses menyaring dan menguji kebenaran fakta tersebut. Pertanyaannya bergeser menjadi: dari sekian banyak curhatan tadi, mana yang benar-benar kebutuhan riil sistem, dan apakah ada yang saling bertolak belakang?

Kalau dua aktivitas ini ditabrakkan dalam satu sesi, analis cenderung mengambil kesimpulan instan di tempat. Akibatnya fatal: kebutuhan sistem hanya akan mencerminkan selera orang yang paling vokal di ruangan atau terdistorsi oleh curhatan orang terakhir yang diajak bicara di dekat mesin kopi. Idealnya, ada pemisahan peran antara orang yang bertugas menggali informasi di lapangan dengan orang yang menguji konsistensi dokumen di meja analisis. Kalau terpaksa dikerjakan oleh satu kepala, buat jeda minimal satu malam antara sesi wawancara dan perumusan dokumen kebutuhan agar pikiran kembali jernih dari bias emosional narasumber.

Lalu bagaimana dinamika ini berjalan di ekosistem kerja *Agile* yang serba cepat? Di metodologi sekuensial tradisional, rekayasa kebutuhan diperlakukan seperti ritual awal yang sakral dengan target menghasilkan bundel dokumen tebal setebal kamus. Di dunia *Agile*, proses rekayasa kebutuhan dipecah dan disebar sepanjang siklus proyek:

- Format dokumen kaku diubah menjadi *user story*, yaitu narasi kebutuhan ringkas dari sudut pandang pengguna akhir: peran penggunanya siapa, tindakan apa yang dia mau, dan manfaat apa yang dia cari.
- Kumpulan kebutuhan hidup dinamis di dalam *product backlog*, tempat daftar rencana kerja terus dirombak urutan prioritasnya setiap awal siklus kerja pendek.
- Aktivitas penggalian kebutuhan tidak pernah berhenti, melainkan terus mengalir lewat percakapan harian dan demonstrasi produk berkala kepada klien.
- Kalimat spesifikasi panjang digantikan oleh contoh pengujian nyata yang disepakati di awal perancangan fitur.

Namun jangan keliru memahami *Agile*. Metodologi lincah ini sama sekali tidak menghapus empat kesulitan klasik penggalian yang kita bahas tadi. Pengguna tetap saja bingung membedakan kebutuhan dan keinginan, istilah antarbagian tetap saja berbenturan, dan dinamika politik kantor tetap saja mewarnai proyek. *Agile* cuma mengubah satu variabel: ongkos kesalahannya jadi jauh lebih murah karena sistem diuji coba per dua pekan, sehingga kegagalan konsep seperti formulir empat belas kolom Mas Danu bisa terdeteksi di bulan pertama, bukan setelah ratusan juta rupiah hangus dibakar.

---

## Sepuluh Lubang Jebakan di Proses Requirement

Belajar dari kekacauan sistem kunjungan klien di kantor, gue merangkum sepuluh jebakan fatal yang paling sering diulang tim konsultan:

1. Hanya menginterogasi jajaran atasan pemegang anggaran, sementara pengguna riil yang berkeringat di lantai operasi tidak pernah dilibatkan.
2. Menganggap wawancara formal di ruang rapat sudah cukup untuk merekam realitas operasional bisnis.
3. Menghindari benturan antarbagian dengan cara mencatat semua permintaan yang bertentangan ke dokumen, lalu melempar tanggung jawab penyelesaiannya ke pemrogram di tengah masa penulisan kode.
4. Tidak punya nyali menetapkan skala prioritas kebutuhan, sehingga semua item dilabeli wajib dan berakhir dengan kegagalan massal saat tenggat waktu tiba.
5. Hanya mendesain jalur mulus tanpa pernah merinci mekanisme penanganan galat, pembatalan alur, dan input data kosong.
6. Menggabungkan peran penggali data dan analis logika tanpa ada proses telaah kritis independen.
7. Menganggap dokumen kebutuhan yang sudah diteken sebagai prasasti mati, padahal roda bisnis terus bergerak mengubah aturan main.
8. Membiarkan istilah rancu berkeliaran di dokumen tanpa batas definisi yang terukur secara matematis.
9. Melupakan keberadaan pemangku kepentingan pasif yang ikut terdampak sistem namun tidak memegang jabatan struktural untuk diundang rapat.
10. Terlena menganggap prototipe antarmuka visual sudah otomatis menggantikan dokumen perincian aturan logika bisnis.

---

## Bahan Diskusi untuk Lo

Setelah Mas Danu menutup laptopnya dan ruang rapat lantai 28 kembali hening, gue sadar satu hal: portal sewa klien itu sedang berada di persimpangan jalan antara dipaksa pakai dengan ancaman surat peringatan manajer, atau dirombak ulang alur pengumpulannya dari bawah.

Ada tiga pertanyaan reflektif yang mau gue lempar ke meja belajar lo buat bahan sesi sinkronus pekan ini:

1. Kalau lo ditunjuk jadi analis utama untuk menyelamatkan proyek portal sewa Mas Danu yang sudah terlanjur meluncur tapi ditolak lapangan ini, kombinasi teknik penggalian apa yang bakal lo gelar dalam dua pekan pertama, dan bagaimana lo membagi porsi antara Mas Danu di lobi gedung dengan Bu Retno di meja keuangan?
2. Di tengah situasi di mana manajer operasional klien merasa kehilangan muka karena formulir empat belas kolom buatannya ditolak stafnya sendiri, bagaimana strategi lo menjalankan aktivitas negosiasi kebutuhan dan penentuan prioritas tanpa memicu boikot politik dari pihak manajemen pemegang anggaran?
3. Bayangkan skenario jika proyek ini sejak awal dirancang menggunakan pendekatan *Agile*. Menurut analisa lo, instrumen *Agile* mana yang paling efektif mencegah agen lapangan diam-diam membuat *spreadsheet* cadangan seperti yang dilakukan Mas Danu?

Gue beresin berkas catatan di meja kerja, mematikan monitor laptop yang mulai memantulkan lampu temaram ruang tengah, lalu melangkah ke dapur buat menyeduh cangkir teh kamomil hangat sebelum istirahat malam.

Salam secangkir teh hangat dari meja kerja,

Nik