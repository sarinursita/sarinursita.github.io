---
title: "Catatan Nik: Tujuh Tikungan di Lantai 28 dan Cara Otak Gue Berhenti Dibodohi Angka"
subtitle: "Gue kira matkul ini soal rumus dan model, sampai gue sadar tujuh sesi ini yang dibongkar justru cara gue membaca angka di ruang rapat."
type: blog
date: 2026-11-24T05:00:00+07:00
draft: true
ws_chat: 1733
ws_msg: 21975
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "analisa-dan-desain-smart-system", "evaluasi", "catatan-nik"]
summary: "Gue rangkum tujuh sesi mata kuliah ini: apa sebenarnya yang diajarkan, peta perjalanan dari definisi sistem cerdas sampai pohon keputusan, dan apa yang berubah di cara gue membaca slide klien."
hook: "Tujuh sesi itu nggak bikin gue jago ngoding, tapi bikin gue berhenti percaya angka tanpa nanya asalnya."
---

Gue lagi memandangi tumpukan catatan di sisi kiri meja kerja, tepat di samping cangkir kopi yang sudah dingin sejak jam dua siang. Di layar laptop, ada dokumen presentasi klien korporasi besar yang baru saja selesai kami revisi bareng tim valuasi. Tiga bulan lalu, slide presentasi seperti ini bakal gue telan mentah-mentah. Isinya penuh jargon *machine learning*, visualisasi warna-warni yang kelihatan futuristik, dan janji efisiensi biaya sewa sampai sekian persen. Dulu, gue cuma terpukau sama kosmetiknya.

Sekarang, saat membaca ulang draf itu, mata gue malah otomatis mencari lubang logikanya. Di mana letak asumsi dasarnya? Data historis apa yang dipakai buat menarik garis tren itu? Kenapa ketidakpastian pasar properti kuartal depan cuma diringkas jadi satu angka pasti tanpa rentang probabilitas? 

Perubahan cara pandang ini bukan datang tiba-tiba. Menjelang evaluasi tengah semester untuk Analisis dan Desain Sistem Cerdas, gue baru sadar kalau tujuh pertemuan yang gue jalani sebenarnya bukan soal menghafal rumus matematika atau skrip pemrograman. Tujuh sesi ini bekerja seperti operasi katarak di kepala gue.

---

## Sebenarnya, Mata Kuliah Ini Mau Mengajari Kita Apa?

Kalau ada orang kantor yang nanya kenapa anak *marketing* di konsultan properti komersial SCBD bela-belain kuliah manajemen sistem informasi, jawaban gue sekarang jauh lebih jernih. Mata kuliah ini intinya cuma satu: seni berpikir terstruktur saat berhadapan dengan masalah rumit yang penuh ketidakpastian, sebelum kita sok tahu menyuruh komputer menyelesaikannya.

Di industri properti komersial tempat gue kerja, semua orang suka mengklaim kantor kami bergerak ke arah *smart system*. Gedung pencakar langit dibilang cerdas kalau lampu koridornya mati otomatis saat sepi. Sistem manajemen properti dibilang pintar kalau bisa mengeluarkan grafik proyeksi pendapatan sewa sepuluh tahun ke depan. Padahal, memberi label *smart* ke sebuah algoritma yang cuma menjalankan rumus perkalian Excel itu penipuan publik yang paling lazim terjadi di koridor bisnis.

Sistem cerdas bukan soal seberapa keren *interface* aplikasinya, bukan juga soal seberapa canggih teknologi *cloud* yang disewa dari vendor luar negeri. Inti dari sistem cerdas adalah kemampuan mesin untuk menerima sinyal lingkungan yang kotor, memahami pola di balik ketidakpastian itu, lalu mengambil tindakan rasional yang meminimalkan risiko bisnis. Kalau logika bisnisnya dari awal sudah bengkok, teknologi tercanggih di dunia cuma bakal mempercepat kekacauan dengan biaya yang jauh lebih mahal.

Di titik itulah peran analis sistem informasi menjadi krusial. Kita bukan tukang ketik kode, Sari. Tugas kita adalah menjadi benteng logika: memastikan masalah yang mau diselesaikan itu nyata, data yang dipakai mewakili kenyataan lapangan, dan keputusan yang dihasilkan mesin bisa dipertanggungjawabkan secara moral maupun finansial.

---

## Menyambung Benang Merah: Dari Ilusi Cerdas Sampai Mengurai Peluang

Tujuh pekan ke belakang terasa seperti maraton yang melelahkan, tapi kalau dilihat dari helikopter, alurnya sangat rapi. Dosen gue nggak nyuruh gue langsung terjun bikin sistem; gue justru dipaksa melangkah mundur berkali-kali untuk melihat gambaran utuh.

### 1. Menanggalkan Romantisme Teknologi (Sesi 1)
Perjalanan kita dimulai dari melucuti ilusi. Kita diajak membedah apa yang membuat sebuah sistem layak disebut cerdas dan di mana batas keras kemampuannya. Di sesi awal ini, gue belajar membedakan sistem berbasis aturan kaku dengan sistem adaptif yang benar-benar belajar dari pola. Yang paling menempel di kepala gue adalah pembahasannya soal tantangan etis dan kerapuhan sistem cerdas. Sebuah sistem bisa kelihatan sangat jenius di lingkungan terkontrol, tapi langsung lumpuh begitu disodori data dunia nyata yang berisik dan dinamis.

### 2. Berkenalan dengan Realitas Lewat Data (Sesi 2 & Sesi 3)
Dari pemahaman batas kemampuan itu, kita langsung dihadapkan pada bahan bakar utamanya, yaitu data mentah. Kita masuk ke kerangka kerja *CRISP-DM*, menatap kenyataan bahwa data di dunia nyata jarang sekali berbentuk tabel rapi dengan kolom lengkap. Di sesi dua, kita belajar mengidentifikasi jenis data, memahami dari mana angka-angka itu ditarik, dan menguji konteks pengumpulannya. 

Lalu di sesi tiga, teknik eksplorasi data (*Exploratory Data Analysis*) masuk sebagai pisau bedah. Gue ingat betul pembahasan kita soal bagaimana distribusi data yang menceng, *outlier* yang menipu, atau korelasi semu bisa menjebak seorang analis yang malas memeriksa lapangan. Di properti, kita nggak bisa cuma melihat angka rata-rata harga sewa per meter persegi tanpa melihat sebaran variansinya di tiap koridor jalan. Data adalah cermin buram dari realitas, dan tugas pertama kita adalah menyeka debunya.

### 3. Disiplin Membingkai Masalah (Sesi 4)
Setelah tahu kondisi data kita, ujian sebenarnya baru dimulai: apakah kita benar-benar tahu apa yang sedang kita cari solusinya? Di sesi empat, kita belajar *problem framing*. Ini sesi yang paling menampar gue. Kita membedah jurang lebar antara bahasa bisnis dan bahasa analitik. Ketika klien bilang, "Tingkat hunian gedung kami turun, tolong bikin sistem prediksi penyewa yang mau kabur," itu bukan rumusan masalah sistem cerdas. Itu cuma keluhan bisnis.

Di sesi ini, kita dilatih menerjemahkan kepanikan manajemen menjadi tujuan matematis yang bisa diukur: variabel target apa yang diprediksi, metrik keberhasilan apa yang dipakai, dan apa batasan operasionalnya. Tanpa kemampuan menerjemahkan ini, proyek analitik cuma jadi kuburan anggaran yang menghasilkan visualisasi indah tanpa guna.

### 4. Perang Melawan Jebakan Pikiran Sendiri (Sesi 5)
Begitu masalah selesai dibingkai, muncul bahaya baru yang bukan datang dari komputer, melainkan dari tengkorak kepala kita sendiri. Sesi lima membawa kita menyelami psikologi kognitif Daniel Kahneman. Kita melihat bagaimana *System 1* di otak kita sangat haus jalan pintas, gampang silau oleh *anchoring bias*, dan terlalu percaya diri karena *confirmation bias*. 

Di sini kita mulai membedah dua jenis ketidakpastian yang tidak boleh dicampuradukkan: ketidakpastian karena data kita memang belum cukup (*epistemic uncertainty*) lawan ketidakpastian yang memang sifat alamiah dari sistem itu sendiri (*aleatoric uncertainty*). Mengetahui perbedaan keduanya mencegah kita buang-buang duit membeli *server* mahal demi memprediksi sesuatu yang dasarnya memang acak.

### 5. Membongkar Gejala Sampai ke Titik Terdalam (Sesi 6)
Melanjutkan pertempuran melawan bias, sesi enam membekali kita dengan peralatan bedah kausalitas. Kita belajar bahwa apa yang dikeluhkan orang di ruang rapat hampir selalu cuma gejala (*symptom*), bukan penyakit aslinya. Lewat diagram *fishbone*, teknik *5 Whys*, dan analisis Pareto, kita dipaksa untuk tidak puas pada jawaban pertama. 

Kita belajar melacak tiga lapis masalah: dari lapis kejadian fisik, lapis pola perilaku, sampai ke lapis struktur sistem dan kebijakan internal yang menciptakan kekacauan tersebut. Kalau kita cuma mengobati gejalanya, sistem secanggih apa pun cuma akan mengotomatisasi inefisiensi yang sudah ada di kantor.

### 6. Menghitung Risiko Saat Masa Depan Remang-Remang (Sesi 7)
Puncaknya ada di pertemuan ketujuh gue. Ketika semua akar masalah sudah dipetakan tapi masa depan tetap tidak pasti, kita belajar mengambil keputusan secara kuantitatif lewat pendekatan probabilistik. Kita membedah pohon keputusan (*decision tree*), menghitung *Expected Monetary Value*, mengukur nilai dari sebuah informasi lewat *Expected Value of Perfect Information*, sampai merangkai ketergantungan antarvariabel menggunakan *Bayesian network* dan diagram pengaruh (*influence diagram*).

Materi ini menutup separuh semester gue dengan sangat elegan: kita mengakui bahwa kepastian mutlak di dunia bisnis itu omong kosong, tapi ketidakpastian bukan alasan untuk bertaruh memakai intuisi buta. Kita bisa memetakan peluang, memberi bobot risiko pada tiap cabang pilihan, dan memilih langkah paling rasional berdasarkan bukti terbaik yang kita pegang saat itu.

---

## Ruang Rapat Lantai 28 dan Mata yang Mulai Awas

Dua hari lalu, Vina melangkah cepat ke ruang rapat lantai 28 dengan map tebal di tangan. Gayanya selalu penuh energi, khas pimpinan penjualan yang siap menutup kesepakatan besar. Klien korporasi multinasional kami sedang bimbang: kontrak sewa lima lantai mereka akan habis, dan mereka butuh rekomendasi apakah harus pindah ke gedung baru di koridor TB Simatupang, menegosiasikan ulang tarif sewa di SCBD, atau bertahan dengan mengurangi luasan lantai kantor.

Tim internal kami awalnya menyodorkan satu slide ringkasan berisi tiga kolom perbandingan. Di kolom paling kanan, opsi negosiasi ulang diberi tanda bintang tebal dengan catatan kaki: *Sangat Direkomendasikan berdasarkan pengalaman tim*.

Kalau ini terjadi sebelum semester ini dimulai, gue pasti ikut mengangguk setuju. Opsi itu kelihatan paling aman, paling hemat di atas kertas, dan sesuai dengan reputasi senioritas kantor kami. Tapi ingatan gue langsung melayang ke materi pohon keputusan dan bias kognitif.

"Vin," gue memotong pelan sebelum Vina melangkah ke slide berikutnya. "Tiga opsi ini punya asumsi keberhasilan yang beda jauh. Kalau kita sarankan negosiasi ulang, seberapa besar probabilitas pemilik gedung mau menurunkan *service charge* di tengah inflasi sekarang? Terus kalau negosiasi itu gagal setelah memakan waktu empat bulan, berapa biaya kesempatan yang hilang karena kita melewatkan masa penawaran sewa gedung di Simatupang?"

Vina sempat terdiam, menatap gue dengan dahi berkerut. Aris, yang duduk di ujung meja dengan laptop terbukanya, mendadak menatap gue dengan mata berbinar. Dia langsung menyambar, menjelaskan bahwa tim analitik sebenarnya punya data historis negosiasi pemilik gedung sekelas SCBD selama dua tahun terakhir, tapi angka-angka itu nggak pernah dimasukkan ke model karena format laporannya cuma meminta tabel perbandingan kualitatif.

Di situ gue sadar, cara kerja kepala gue sudah bergeser jauh. Gue nggak lagi melihat sebuah proposal bisnis sebagai sekadar narasi persuasif untuk memuaskan ego direksi. Gue melihatnya sebagai diagram keputusan hidup: ada cabang-cabang keputusan yang harus dipilih, ada simpul probabilitas yang di luar kendali kita, dan ada konsekuensi nilai di setiap ujung daunnya. 

Kuliah ini pelan-pelan menyembuhkan gue dari penyakit latah korporat. Gue berhenti kagum pada istilah-istilah mentereng yang dilempar vendor teknologi saat mereka pamer presentasi. Setiap kali ada yang bilang sebuah sistem punya akurasi tinggi, pertanyaan gue refleks: data uji mana yang dipakai? Seberapa seimbang proporsi kelas datanya? Masalah bisnis apa yang sedang lo selesaikan, dan kenapa harus pakai pendekatan cerdas kalau logika sederhana saja belum lo uji?

---

## Tiga Ujian Pikiran untuk Kita Berdua

Karena besok lusa gue sudah harus duduk menghadapi lembar evaluasi tengah semester, gue nggak mau kita terjebak menghafal definisi kata per kata dari catatan kuliah. Dosen gue jelas lebih tertarik melihat ketajaman logika kita saat menghadapi studi kasus yang bengkok.

Coba lo renungkan tiga pertanyaan ini, Sar. Bayangkan lo lagi berhadapan langsung dengan pemangku kepentingan yang keras kepala di ruang rapat:

1. **Tentang Batas Antara Masalah Bisnis dan Solusi Teknis:**
   Sering kali manajemen mendatangi tim analitik dengan kalimat seperti ini: *"Tolong bangunkan model prediksi berbasis neural network untuk memproyeksikan gedung mana saja yang bakal telat bayar uang sewa kuartal depan."* Kalau lo diminta membedah permintaan ini lewat kacamata *problem framing* dan tiga lapis analisis masalah, pertanyaan-pertanyaan apa yang bakal lo ajukan pertama kali ke manajemen sebelum menyetujui proyek tersebut? Kapan kita tahu bahwa masalah itu sebenarnya tidak membutuhkan sistem cerdas sama sekali?

2. **Tentang Ilusi Kausalitas dan Bias di Balik Angka Bersih:**
   Misalkan sebuah sistem klasifikasi risiko penyewa gedung menunjukkan bahwa perusahaan rintisan teknologi memiliki kecenderungan menunggak sewa tiga kali lebih tinggi dibanding perusahaan manufaktur konvensional. Sebelum manajemen memutuskan untuk menolak semua calon penyewa dari sektor teknologi, bagaimana lo memanfaatkan kerangka *epistemic uncertainty* versus *aleatoric uncertainty*, ditambah analisis *fishbone*, untuk menguji apakah korelasi data tersebut adalah akar masalah yang sebenarnya atau cuma bias penarikan sampel masa lalu?

3. **Tentang Nilai Sebuah Keputusan dalam Ketidakpastian:**
   Di sesi ketujuh, kita mempelajari konsep *Expected Value of Perfect Information* (EVPI). Dalam konteks investasi properti atau sistem informasi, sering kali eksekutif ngotot membeli data riset pasar tambahan atau menyewa konsultan pihak ketiga yang sangat mahal demi *memastikan* keputusan mereka tepat. Menurut lo, bagaimana cara kita menjelaskan kepada pimpinan non-teknis mengenai batas maksimal dana yang rasional untuk dibelanjakan demi mencari data tambahan tersebut menggunakan logika pohon keputusan?

Gue mau menyeduh teh hangat dulu sambil merapikan sisa berkas di meja. Laptop kantor sudah gue tutup, tinggal tumpukan binder kuliah gue yang masih terbuka di bab diagram pengaruh.

Selamat menyiapkan diri, Sar. Gue mau matiin laptop dulu.

Nik