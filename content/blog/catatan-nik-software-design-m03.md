---
title: 'Catatan Nik: Ketika Prototype Figma Dianggap Aplikasi Jadi dan Ilusi "Agile" SCBD'
subtitle: "Gue kira masalahnya cuma demo yang terlalu bagus. Ternyata masalahnya model proses yang dipilih dari awal."
type: blog
date: 2026-10-21T06:41:22.210943+07:00
draft: false
ws_chat: 1609
ws_msg: 21566
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "software-design", "catatan-nik"]
summary: "Demo Figma dianggap sistem jadi, padahal database belum ada. Dari situ gue belajar lima model proses dan kenapa pilihan model harus ikut stabilitas kebutuhan, risiko, dan keterlibatan pengguna."
hook: "\"Sistem ini udah 90 persen siap,\" kata Vina di depan klien. Padahal yang dia tunjukin baru mock-up Figma tanpa database."
---

Tadi siang layar monitor gue mendadak heboh gara-gara rekaman demo *client portal* yang diputar ulang di grup chat komersial. Lo harus lihat ekspresi mukanya Vina pas presentasi ke salah satu klien konglomerat kemarin lusa. Dengan gaya *pitching* andalannya yang super meyakinkan, Vina ngeklik-ngeklik purwarupa di Figma yang dibikin anak magang UI/UX, navigasinya mulus banget, ada animasi transisi grafik valuasi gedung perkantoran, lengkap sama tombol *instant PDF export*. Kliennya tepuk tangan, Vina senyum lebar, terus dengan santainya dia bilang: *"Sistem ini udah 90 persen siap, akhir bulan depan kita udah bisa go-live buat seluruh portofolio aset Bapak."*

Gue yang lagi nyeruput kopi langsung tersedak. Tim *engineer* yang ikut *join call* tanpa buka kamera mendadak hening seketika. Pas *meeting* bubar, *engineering lead* kantor gue langsung nge-ping gue di Slack: *"Mbak Nik, itu tadi cuma interaktif mock-up visual di Figma, databasenya aja belum dibikin, skema auth-nya belum disentuh, kok dibilang udah 90 persen jadi?"*

Gue cuma bisa ngelus dada. Fenomena klasik di SCBD: orang bisnis ngira kalau tampilan layarnya udah bisa diklik, berarti *software*-nya tinggal dicolok ke stopkontak. Ini nyambung banget sama materi kuliah gue minggu ini, Sar. Pekan lalu gue udah babak belur ngebahas empat aktivitas inti rekayasa perangkat lunak: *specification*, *design & implementation*, *validation*, dan *evolution*. Sekarang pertanyaannya naik kelas: gimana caranya keempat aktivitas itu diurutkan, diulang, dan diorganisir biar proyek nggak berujung bunuh diri massal kayak janjinya Vina tadi?

Jawabannya ada di **model proses**.

---

## Kenapa Kita Butuh Model (Dan Tiga Sumbu Penentunya)

Sar, lo pasti sering nemu bos atau kolega yang alergi sama istilah metodologi. Buat mereka, model proses itu birokrasi teoritis kampus yang ngabisin waktu. Padahal sederhananya, model proses itu cuma peta jalan: representasi tentang cara tahapan *software process* disusun dan dijalankan di dunia nyata. Tanpa model, tim lo cuma sekelompok orang yang lari maraton tanpa garis rute, masing-masing sibuk tapi nggak ada yang tahu arah finis.

Di materi kuliah gue minggu ini, ada tiga sumbu utama yang ngebedain satu model sama model lainnya:

1. **Urutan vs. Iterasi**: Apakah prosesnya linear sekali jalan dari hulu ke hilir kayak air terjun, atau berulang (*iterative/incremental*) dalam putaran-putaran kecil?
2. **Cara menangani perubahan**: Apakah perubahan dianggap musuh yang bikin biaya bengkak sehingga ditekan sekaku mungkin, atau justru diterima sebagai keniscayaan yang ditampung rapi di iterasi berikutnya?
3. **Cara menangani risiko dan ketidakpastian**: Apakah ketidakpastian dikelola lewat analisis risiko formal di tiap putaran (kayak *Spiral*), atau ketidakpastian kebutuhan dikurangi lewat contoh visual yang bisa dicoba langsung (kayak *Prototyping*)?

Satu kunci pegangan buat ujian gue nanti: *nggak ada satu model yang paling superior atau paling suci.* Kalau ada dosen atau konsultan *agile* yang bilang satu metode bisa nyelesaiin semua masalah dunia, fiks dia lagi jualan seminar. Pemilihan model selalu bergantung pada tiga variabel: **stabilitas kebutuhan (*requirements stability*)**, **kompleksitas sistem**, dan **tingkat risiko proyek**.

---

## Peta Lima Model dalam Sekali Tarikan Napas

Sebelum kita bedah anatominya satu per satu, ini rangkuman satu kalimat per model yang gue bikin buat contekan belajar gue:

* **Waterfall**: Linear berurutan; tiap tahap harus selesai dan dikunci dulu sebelum tahap berikutnya boleh jalan.
* **Incremental**: Sistem dipecah jadi beberapa potongan fungsional (*increment*); tiap bagian yang kelar langsung bisa dipakai dan diuji oleh pengguna.
* **Agile**: Iterasi pendek berulang (*sprint*), menuntut kolaborasi intensif, dan punya respons super cepat terhadap perubahan kebutuhan.
* **Spiral**: Iterasi berbasis manajemen risiko; tiap putaran fokus utama kerjanya adalah mengidentifikasi dan memitigasi ketidakpastian teknis maupun bisnis.
* **Prototyping**: Membangun versi awal sistem (UI, alur, atau fungsionalitas kunci) demi memperjelas kebutuhan pengguna yang masih abu-abu.

---

## Membedah Lima Model: Anatomi, Realita, dan Jebakannya

### 1. Waterfall (Model Air Terjun)

Alurnya lurus dan disiplin: *requirements* dikunci, lalu turun ke *system design*, masuk ke *implementation* (ngoding), lanjut ke *testing*, dan terakhir *maintenance*. Nggak ada jalan putar balik tanpa konsekuensi finansial yang berdarah-darah.

* **Kekuatan**: Batas tiap tahap sangat tegas, alur kerja jelas, dan dokumennya super rapi. Progresnya gampang banget dipantau manajemen atau auditor eksternal lewat *milestone chart*. Model ini sangat cocok untuk proyek yang kebutuhannya sudah terdefinisi secara presisi dan hampir mustahil berubah di tengah jalan.
* **Keterbatasan**: Sangat kaku. Kalau di tahap *testing* baru ketahuan ada salah paham di tahap *requirements*, biayanya langsung berlipat ganda karena efek dominonya merembet ke mana-mana. Masalah terbesarnya: *user feedback* baru muncul di ujung akhir proyek saat semuanya sudah terlanjur jadi batu.
* **Kapan lo pakai**: Proyek regulasi perbankan, kepatuhan audit pemerintah, integrasi API sistem perpajakan negara, atau proyek pengadaan dengan kontrak nilai tetap (*fixed-price contract*) yang spesifikasinya sudah dikunci dari tender.

### 2. Incremental (Model Bertahap)

Alih-alih nungguin satu sistem raksasa selesai dalam dua tahun, model ini memecah sistem jadi beberapa paket fungsionalitas (*increment*). Tiap *increment* menjalankan aktivitas inti sendiri (analisis, desain, koding, uji coba) dan hasilnya langsung diserahkan ke pengguna untuk dipakai operasional.

* **Kekuatan**: Klien atau pengguna nggak perlu nunggu berbulan-bulan buat ngerasain manfaat sistem. Umpan balik didapat jauh lebih awal. Fitur prioritas tertinggi dikerjakan duluan, dan sistem lebih lentur karena masukan pengguna bisa diselipkan ke *increment* berikutnya. Nilai plusnya dibanding Agile: strukturnya tetap formal dan punya kerangka arsitektur yang solid.
* **Keterbatasan**: Pembagian arsitektur di awal harus sangat matang. Kalau salah potong modul, urusan integrasi di tengah jalan bakal jadi mimpi buruk. Koordinasi antar-bagian butuh kontrol ketat biar nggak ada konflik data atau duplikasi fungsi.
* **Kapan lo pakai**: Sistem enterprise yang kompleks di mana operasional bisnis nggak bisa nunggu lama, kebutuhan utamanya bisa dirilis bertahap, tapi organisasi lo masih butuh kepastian jadwal dan tata kelola yang terstruktur rapi.

### 3. Agile

Agile itu bukan cuma soal papan Trello atau *daily standup*, Sar. Esensinya adalah siklus pendek berulang (biasanya dua sampai empat minggu). Tiap siklus menghasilkan produk kerja yang fungsional, langsung dievaluasi bareng *stakeholder*, dan hasilnya dipakai buat menentukan arah siklus berikutnya.

* **Kekuatan**: Adaptabilitasnya juara. Kalau kompetitor tiba-tiba rilis fitur baru atau tren pasar bergeser, tim nggak perlu panik merombak rencana tahunan. Keterlibatan *end-user* yang konstan bikin produk akhir bener-bener menjawab kebutuhan riil, bukan asumsi orang teknis semata.
* **Keterbatasan**: Menuntut disiplin komunikasi yang luar biasa tinggi. Tanpa kedewasaan tim, fleksibilitas Agile gampang berubah jadi anarki: ruang lingkup melebar tanpa batas (*scope creep*), dokumentasi formal terbengkalai, dan pas diaudit internal divisi ini bakal gelagapan nyari dokumen spesifikasi arsitektur.
* **Kapan lo pakai**: Pengembangan produk digital baru, *startup environment*, aplikasi berbasis tren konsumen, atau proyek apa pun di mana lingkungannya bergerak sangat cepat dan persyaratannya masih terus berkembang.

### 4. Spiral

Model ini dirancang khusus oleh Barry Boehm buat proyek-proyek raksasa yang taruhannya gede banget. Alurnya bergerak memutar keluar: di tiap putaran spiral, tim menentukan objektif, melakukan **analisis dan mitigasi risiko**, bikin prototipe atau rekayasa teknis, evaluasi hasil, lalu merencanakan putaran spiral berikutnya.

* **Kekuatan**: Manajemen risikonya eksplisit di setiap putaran. Sebelum tim nulis kode baris pertama, risiko terbesarnya (misal: kebocoran data, skalabilitas server, kegagalan integrasi pihak ketiga) dianalisis dan dicari mitigasinya dulu. Ini ngasih tingkat kepastian dan kontrol kualitas paling tinggi di antara semua model.
* **Keterbatasan**: Mahal banget dan berat secara proses. Lo butuh ahli analisis risiko yang senior, bukan sekadar *project manager* biasa. Untuk proyek skala kecil atau menengah, pakai Spiral itu ibarat mau belanja sayur ke warung depan kompleks naik helikopter Apache: boros dan nggak masuk akal.
* **Kapan lo pakai**: Proyek infrastruktur kritikal perbankan, sistem navigasi penerbangan, proyek migrasi data *core-banking* multi-miliar rupiah, atau sistem *enterprise* yang kalau sampai *down* sejam aja bisa bikin perusahaan kena denda miliaran rupiah.

### 5. Prototyping

Filosofi dasarnya: manusia sering kali baru tahu apa yang mereka butuhkan setelah mereka melihat dan menyentuh barangnya. Tim ngebangun versi awal berupa antarmuka grafis (*mockup* interaktif) atau fungsionalitas kunci yang disederhanakan, lalu diserahkan ke pengguna untuk dievaluasi bolak-balik sampai kebutuhannya benar-benar jernih.

* **Kekuatan**: Menjembatani jurang komunikasi antara bahasa teknis *programmer* dan bahasa awam pengguna bisnis. Mengubah ide abstrak jadi visual yang konkret, sehingga salah paham bisa dibereskan di awal sebelum investasi dana besar digelontorkan.
* **Keterbatasan (Empat Jebakan Maut)**:
  1. *Ekspektasi keliru*: Pengguna (atau sales kayak Vina) mengira prototipe itu sistem final yang tinggal dipakai.
  2. *Terjebak visual*: Tim dan pengguna keasyikan ngurusin warna tombol atau animasi UI, tapi lupa ngecek logika bisnis dan aliran datanya.
  3. *Fondasi rapuh*: *Developer* sering kali tergoda buat ngejadiin kode prototipe yang dibikin buru-buru itu sebagai fondasi sistem produksi. Hasilnya: arsitektur sistemnya rapuh dan gampang ambruk.
  4. *Tujuan kabur*: Tim nggak menegaskan di awal apakah prototipe ini cuma *throwaway prototype* (dibuang setelah kebutuhan jelas) atau *evolutionary prototype* (dikembangkan pelan-pelan jadi sistem nyata).
* **Kapan lo pakai**: Di tahap inisiasi saat pengguna kesulitan merumuskan apa yang mereka mau, atau saat lo butuh validasi konsep sebelum minta anggaran besar ke direksi. Ingat kuncinya: prototipe itu alat buat memahami masalah, bukan solusi akhir.

---

## Matriks Perbandingan Cepat

Biar lo gampang ngafal buat persiapan kuis atau tugas analisis kasus, gue rekap karakteristik lima model tadi ke dalam tabel ini:

| Aspek | Waterfall | Incremental | Agile | Spiral | Prototyping |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pola Alur** | Linear berurutan | Bertahap (*chunks*) | Iteratif pendek (*sprint*) | Spiral berbasis risiko | Iteratif cepat di awal |
| **Kejelasan Kebutuhan** | Stabil dan jelas sejak awal | Cukup jelas tapi butuh tumbuh | Sangat dinamis dan berubah | Belum pasti dan berisiko tinggi | Sangat kabur atau belum jelas |
| **Waktu Umpan Balik** | Di ujung akhir proyek | Di setiap *increment* | Di setiap iterasi (*review*) | Di akhir tiap putaran spiral | Terus-menerus di tiap prototipe |
| **Tingkat Risiko** | Sangat tinggi kalau spek salah | Sedang dan terkendali | Rendah sampai sedang | Dikelola paling ketat | Sedang (risiko salah paham ekspektasi) |
| **Beban Dokumentasi** | Sangat berat dan formal | Sedang dan terstruktur | Ringan dan minimalis | Sangat berat dan berbasis audit | Sangat ringan |
| **Biaya Perubahan** | Sangat mahal dan berantai | Sedang | Murah dan adaptif | Terkendali lewat mitigasi | Murah di tahap eksplorasi awal |
| **Skala Proyek Terbaik** | Proyek kontrak pasti dan jelas | Sistem *enterprise* modular | Produk digital dinamis | Sistem kritikal investasi masif | Eksplorasi konsep dan riset kebutuhan |

---

## Panduan Memilih Model: Heuristik dan Rumus Menjawab Ujian

Di lembar studi kasus nanti, dosen nggak bakal nanya definisi harfiah. Kita bakal dikasih skenario bisnis yang berantakan, terus disuruh milih model mana yang paling masuk akal beserta alasannya.

Berdasarkan silabus, ini lima pertanyaan heuristik berurutan yang harus lo tanyain ke skenario tersebut:

1. **Seberapa stabil kebutuhannya?**
   Kalau kebutuhan operasionalnya udah baku dan nggak bakal diubah sama undang-undang, pilih Waterfall. Kalau kebutuhan dasarnya jelas tapi fiturnya bakal mekar bertahap, pilih Incremental. Kalau pasarnya dinamis banget dan belum jelas ujungnya, pilih Agile. Kalau penggunanya aja masih bingung mau bikin apa, lempar Prototyping dulu.
2. **Seberapa besar risiko dan biaya kegagalannya?**
   Kalau kegagalan sistem bisa bikin perusahaan bangkrut atau ada bahaya fatal, langsung kunci ke Spiral (atau minimal Incremental yang diperketat dengan mitigasi risiko formal).
3. **Seberapa besar dan tersebar tim pengembangnya?**
   Tim raksasa lintas negara yang beda zona waktu butuh dokumen arsitektur yang kuat (Incremental/Waterfall). Tim kecil berisi sepuluh orang yang duduk semeja atau intensif di Discord bisa lari kencang pakai Agile.
4. **Apakah pengguna bisa diajak kolaborasi rutin?**
   Kalau klien atau penggunanya bisa diajak *sync meeting* tiap minggu buat ngetes fitur, hajar pakai Agile atau Prototyping. Tapi kalau klien lo cuma mau ketemu pas tanda tangan kontrak dan pas serah terima kunci, jangan ngimpi pakai Agile, lo bakal mati kutu. Pilih Incremental atau Waterfall.
5. **Apakah ada kewajiban audit ketat atau kontrak pengadaan kaku?**
   Kalau ada pasal-pasal penalti hukum dan regulasi kepatuhan (*compliance*), dokumentasi formal di Waterfall atau Spiral adalah harga mati.

### Rumus Justifikasi Nilai A

Waktu presentasi tugas atau jawab soal esai, jangan cuma sebut kelebihannya doang. Pola kalimat yang dinilai tinggi sama dosen penguji itu wajib memuat keterbatasan dan mitigasi:

> *"Untuk kasus [Nama Kasus], gue memilih model [Nama Model] karena (a) karakteristik kebutuhan yang bersifat [...], (b) tingkat risiko proyek yang [...], (c) ukuran dan sebaran tim yang [...], serta (d) keterlibatan pengguna yang [...]. Keterbatasan dari model ini adalah [...], dan mitigasi yang kami terapkan untuk mengatasi keterbatasan tersebut adalah [...]."*

Contoh nyatanya gini: kalau lo milih Agile buat proyek korporat, lo harus langsung ngomong bahwa keterbatasan Agile adalah dokumentasi formal yang minim sehingga rawan masalah pas audit. Mitigasinya: tim wajib menyisipkan artefak dokumentasi arsitektur di akhir tiap iterasi sebagai *definition of done*. Kalimat mitigasi itulah yang ngebuktiin lo mikir sebagai calon manajer sistem informasi, bukan sekadar tukang ngapal definisi buku teks.

---

## Bahan Diskusi Pekan Ini

Sari, berkaca dari kekacauan demo purwarupa Figma Vina di kantor gue tadi siang dan materi model proses yang barusan gue bedah, coba deh lo asah pisau analisis lo buat ngejawab dua skenario ini di catatan lo berikutnya:

1. **Skenario Kantor SCBD**: Divisi komersial kantor gue mau bangun platform otomasi valuasi aset properti komersial yang melibatkan perhitungan finansial sensitif, integrasi data dari tiga vendor eksternal yang API-nya sering *time-out*, dan penggunanya adalah para *valuer* senior yang terkenal gaptek serta super skeptis sama sistem baru. Vina ngotot minta tim pakai Agile murni dua mingguan biar cepet kelihatan hasilnya ke klien. Kalau lo jadi konsultan IT-nya, apakah usulan Vina itu realistis? Model apa yang bakal lo rekomendasikan, dan gimana lo mengemas rekomendasinya pakai format justifikasi di atas lengkap dengan mitigasi risikonya?
2. **Skenario Dilema Prototipe**: Gimana strategi konkret buat ngedidik *stakeholder* bisnis (termasuk orang-orang tipe sales) supaya mereka nggak gampang kejebak menganggap *clickable prototype* sebagai produk akhir yang siap rilis, tanpa bikin mereka patah semangat buat ngasih *feedback* desain?

Gue mau lanjut bikin laporan mingguan dulu. Kopi ketiga udah dingin, dan Vina masih kirim screenshot demo ke grup.

Selamat ngutak-ngatik, Sar.

Nik
