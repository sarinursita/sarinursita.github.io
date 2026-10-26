---
title: "Catatan Nik: Ketika Semua Orang Setuju Butuh AI tapi Nggak Ada yang Tahu Masalahnya Apa"
subtitle: "Rapat dua jam, sembilan orang mengangguk, dan sebulan kemudian nol progres. Yang nggak pernah ada bukan anggaran atau niat, tapi rumusan masalah yang bisa gagal."
type: blog
date: 2026-10-26T07:28:46.999399+07:00
draft: false
ws_chat: 1628
ws_msg: 21639
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "analisa-dan-desain-smart-system", "catatan-nik"]
summary: "Materi pekan ini soal problem framing: masalah bisnis vs masalah AI, tujuh langkah menerjemahkannya, dan kenapa tujuan yang nggak bisa gagal itu tandanya tujuan yang palsu. Di kantor gue, rapat lintas divisi soal sistem yang lebih pintar mandek sebulan karena nggak ada satu pun yang mau jadi pemilik keputusan."
hook: "\"Nol besar.\" Dua jam rapat, sembilan orang mengangguk, satu inisiatif AI yang disebut empat puluh kali. Sebulan kemudian belum ada satu baris kode, karena nggak ada satu pun yang tahu masalah apa yang sebenarnya mau dipecahkan."
---

Sebulan yang lalu, gue duduk di ruang rapat lantai 28 SCBD bareng sembilan orang lainnya. Agendanya mentereng banget: *Kick-off Inisiatif Smart Valuation & Client Recommendation System*. Ada Vina dari tim *sales*, perwakilan tim valuasi, dua orang dari tim IT regional via Zoom, dan Aris yang duduk di ujung meja sambil megang buku catatan barunya. Rapat itu berlangsung dua jam penuh. Ada presentasi slide dengan grafis futuristik, ada diagram alur panah-panah yang saling menyambung, dan ada kata *artificial intelligence* yang disebut minimal empat puluh kali.

Waktu rapat ditutup, semua orang mengangguk mantap. Vina bilang, "Keren banget, *this is exactly what we need* biar kita nggak ketinggalan zaman." IT bilang, "*Sounds good*, kami siap *support*."

Tahu apa yang terjadi setelah rapat megah itu selama sebulan penuh? *Nol besar.* 

Nggak ada satu pun baris kode yang ditulis. Nggak ada satu pun *dataset* yang diekstrak. Proyek itu membeku di tempat. Kemarin sore waktu gue cek ke IT, mereka bilang, "Kami masih nunggu *requirement* yang jelas dari tim bisnis." Waktu gue tanya ke Vina, dia malah melotot heran, "Lho, kan di rapat sebulan lalu udah gue jelasin panjang lebar? Kita butuh sistem yang lebih pintar biar *conversion rate* naik! Masa mereka nggak paham?" Sementara Aris di sudut kubikel cuma bisa garuk-garuk kepala karena bingung mau bikin model apa kalau definisi input dan output-nya aja nggak ada.

Semua orang merasa sudah sepakat, padahal sebenarnya nggak ada satu pun yang tahu masalah apa yang sedang dipecahkan. Nggak ada pemilik keputusan, nggak ada angka target, dan yang paling parah: nggak ada skenario kegagalan yang bisa diukur.

Ini persis materi kuliah gue minggu ini, Sar: *Problem Framing*. Gue sering banget terburu-buru ngomongin data, algoritma, atau arsitektur model, sampai lupa kalau kesalahan paling mahal dalam proyek sistem cerdas itu bukan memilih algoritma yang keliru, melainkan membangun algoritma yang sempurna untuk masalah yang salah sama sekali.

---

## Berhenti Dulu: Kenapa Kita Harus Mundur Selangkah?

Tiga minggu kemarin gue udah babak belur berkutat sama urusan teknis data. Mulai dari definisi sistem cerdas, jenis-jenis data, cara *scraping* dan pengumpulan, sampai pusingnya bersihin *dirty data* dan bikin Exploratory Data Analysis (EDA) yang estetik. Rasanya gatal pengen langsung lompat melatih model regresi atau nge-lempar data ke algoritma *random forest*.

Tapi di fase ini, dosennya sengaja narik rem tangan. Gue dipaksa mundur selangkah dan ditampar pakai pertanyaan paling mendasar: *sebenarnya masalah apa yang mau lo pecahkan, dan untuk mengubah keputusan yang mana?*

Di metodologi CRISP-DM (*Cross-Industry Standard Process for Data Mining*), fase pertama itu bukan *Data Understanding*, apalagi *Data Preparation*. Fase pertamanya adalah *Business Understanding*. Ini fondasi absolut, bukan sekadar basa-basi kata pengantar di proposal. EDA lo mau serapi apa pun, visualisasi lo mau seindah apa pun di Tableau, semuanya nggak bakal ada gunanya kalau target akhirnya kabur kayak masa depan.

Urutan berpikir yang waras dalam rekayasa sistem cerdas itu hierarkis:
1. Pahami masalahnya.
2. Identifikasi keputusan apa yang perlu diambil.
3. Kumpulkan data yang relevan dengan keputusan itu.
4. Bangun model yang mengoptimalkan keputusan tersebut.

Kenyataan di lapangan seringnya kebalik: kantor punya tumpukan log transaksi bertahun-tahun, manajemen kepincut tren AI, panggil *data scientist* atau vendor, terus bilang, "Kita punya banyak data nih, tolong bikinin AI yang canggih dong." Itu cara paling cepat membakar anggaran ratusan juta tanpa menghasilkan apa-apa selain kekecewaan.

---

## Dua Bahasa yang Sering Bikin Miskomunikasi: Masalah Bisnis vs Masalah AI

Akar keributan antara Vina dan tim IT di kantor gue kemarin sebenarnya sederhana: mereka berbicara dalam dua bahasa yang berbeda tapi merasa lagi ngomongin hal yang sama.

Satu proyek analitik itu wajib punya dua rumusan yang terpisah namun saling terhubung secara rigid:

### 1. Masalah Bisnis (*Business Problem*)
Masalah bisnis selalu memakai bahasa manajemen. Isinya berkisar di seputar metrik uang, efisiensi waktu, risiko kerugian, atau peluang pasar. 
Contohnya:
* "Pendapatan sewa gedung komersial kita kuartal ini anjlok 18% dibanding kuartal lalu."
* "Klien korporat banyak yang nggak memperpanjang kontrak konsultasi setelah tahun pertama."
* "Waktu yang dihabiskan tim valuasi buat bikin laporan awal terlalu lama, bikin prospek kabur ke kompetitor."

Cirinya jelas: ada konsekuensi finansial atau operasional, ada pihak yang bertanggung jawab atas keputusan tersebut, tapi rumusannya **belum bisa dieksekusi oleh mesin**. Lo nggak bisa nyuruh algoritma Python: `model.fit(selesaikan_penurunan_pendapatan)`. Komputer bakal bengong.

### 2. Masalah AI atau Analitik (*AI/Analytics Problem*)
Ini adalah hasil translasi masalah bisnis ke dalam instruksi matematis yang bisa dipecahkan oleh komputer. Ciri wajibnya ada empat:
* **Unit analisis:** satu baris data mewakili objek atau peristiwa apa?
* **Target atau label:** nilai apa yang ingin diprediksi atau dikelompokkan secara spesifik?
* **Metrik evaluasi teknis:** bagaimana cara mengukur apakah tebakan model itu bagus atau jelek?
* **Data yang tersedia:** variabel prediktor apa saja yang sah digunakan saat prediksi dilakukan?

Contoh hasil terjemahannya:
* Dari masalah "klien banyak yang kabur", diterjemahkan menjadi: *Klasifikasi biner untuk memprediksi probabilitas seorang klien korporat tidak memperpanjang kontrak dalam 60 hari ke depan, dievaluasi menggunakan metrik ROC-AUC dan recall pada threshold 0,4.*

Provost dan Fawcett di buku pegangan yang gue baca sudah menegaskan berkali-kali: nilai dari *data science* itu nggak pernah berhenti di level *insight*. Nilai riilnya ada pada **perubahan keputusan**. Kalau lo berhasil bikin model dengan akurasi 98%, tapi ujung-ujungnya tim *sales* tetap menghubungi klien pakai insting acak kayak biasanya, maka nilai ekonomis dari model lo itu persis nol rupiah. Model lo cuma jadi pajangan PDF buat laporan tahunan.

---

## Tujuh Langkah Problem Framing: Jangan Ada yang Di-skip

Biar kita nggak tersesat kayak rapat sebulan lalu, perumusan masalah sistem cerdas harus lewat tujuh tahapan sistematis ini:

### 1. Tentukan Tujuan Bisnis dan Konteks Pemakaian
Siapa aktor yang bakal menggunakan output dari model ini? Keputusan apa yang diambil berdasarkan output tersebut? Seberapa sering keputusan itu dieksekusi (harian, mingguan, *real-time*)? Dan yang paling krusial: apa dampak buruknya kalau model kita salah menebak? Tanpa jangkar operasional ini, metrik teknis lo bakal melayang tanpa makna.

### 2. Terjemahkan ke Tipe Tugas Analitik (*Analytical Task*)
Jangan semua masalah dihajar pakai "klasifikasi" atau "regresi". Pilih tipe tugas yang paling merefleksikan kebutuhan keputusan:
* **Regresi:** Menebak angka kontinu. Misalnya, memprediksi nilai transaksi wajar suatu aset properti komersial dalam miliaran rupiah.
* **Klasifikasi:** Menebak kategori atau kelas diskrit. Misalnya, memilah apakah sebuah *lead* masuk kategori potensial tinggi (*hot*) atau rendah (*cold*).
* **Ranking:** Mengurutkan prioritas. Misalnya, mengurutkan daftar 50 portofolio klien yang paling mendesak untuk dihubungi minggu ini oleh tim Vina.
* **Clustering:** Mengelompokkan data tanpa label awal untuk mencari pola tersembunyi. Misalnya, segmentasi profil penyewa ruang kantor berdasarkan pola mobilitas dan utilisasi ruang.
* **Deteksi Anomali:** Menemukan pola ganjil yang menyimpang drastis dari distribusi normal. Misalnya, mendeteksi manipulasi data valuasi aset atau anomali biaya pemeliharaan properti.
* **Peramalan Deret Waktu (*Time Series Forecasting*):** Memproyeksikan pola historis yang berurutan ke masa depan. Misalnya, memproyeksikan tingkat okupansi ruang perkantoran Jakarta untuk 6 bulan ke depan.
* **Inferensi Kausal (*Causal Inference*):** Mengukur efek kausal dari suatu intervensi atau perlakuan (*treatment*). Misalnya, mengukur apakah diskon *service charge* sebesar 10% benar-benar secara langsung menaikkan retensi penyewa, ataukah penyewa memang akan bertahan terlepas dari diskon tersebut.

### 3. Tetapkan Unit Analisis (*Unit of Analysis*)
Ini bagian yang sering bikin model hancur berantakan kalau diremehkan di awal. Satu baris di tabel data lo itu merepresentasikan apa? Apakah satu klien? Satu properti? Satu transaksi transaksi-hari? Atau satu kontrak perpanjangan? Pilihan unit analisis ini menentukan bagaimana data diagregasi, bagaimana fitur dibentuk, dan bagaimana memotong kebocoran data (*data leakage*) saat membagi data latih dan data uji.

### 4. Pilih Label atau Target yang Sah
Label harus benar-benar ada di dunia nyata, terdefinisi secara konsisten, dan **sudah tersedia saat prediksi dilakukan**, bukan baru ketahuan berbulan-bulan kemudian. Kalau lo mau memprediksi gagal bayar sewa bulan depan, jangan masukkan variabel "total denda keterlambatan bulan berjalan" sebagai fitur prediktor. Itu namanya *label leakage*, lo ngasih sontekan masa depan ke dalam model.

### 5. Sepakati Metrik Ganda (*Dual Metrics*)
Harus ada jembatan antara metrik laboratorium komputer dan metrik ruangan direksi:
* **Metrik ML (Teknis):** MAE, RMSE, Log-Loss, F1-Score, Precision, Recall, PR-AUC.
* **Metrik Bisnis (Dampak Finansial/Operasional):** Tambahan *net revenue*, efisiensi jam kerja per valuasi, biaya penalti yang berhasil dicegah, atau rasio konversi *leads*.

Keduanya harus punya rumus konversi yang disepakati di awal. Kalau F1-score naik 0,05, berapa juta rupiah penghematan yang dibawa ke meja manajemen? Kalau nggak bisa dihitung, manajemen nggak akan pernah peduli sama F1-score lo.

### 6. Uji Kelayakan (*Feasibility Test*)
Sebelum mulai *coding*, jawab lima pertanyaan pahit ini:
* Apakah datanya benar-benar ada dan izin aksesnya bisa didapat?
* Apakah labelnya berkualitas atau isinya tebakan manual orang magang?
* Berapa biaya komputasi untuk *training* dan *serving* model ini, masuk akal nggak dibanding potensi keuntungannya?
* Apakah ada batasan latensi? Kalau butuh prediksi *real-time* dalam 100 milidetik, lupakan arsitektur *ensemble* yang beratnya minta ampun.
* Apakah ada isu kepatuhan privasi (UU PDP, GDPR) atau bias etis dalam data?

Kalau ada satu saja lampu merah di uji kelayakan ini, ubah *framing* masalahnya. Jangan dipaksain jalan cuma demi gengsi.

### 7. Tetapkan Baseline yang Jujur Sebelum Mulai
Ini aturan emas yang paling sering dilanggar. Jangan pernah mengevaluasi model tanpa pembanding dasar (*baseline*). Baseline bisa berupa:
* *Do-nothing* (asumsikan kondisi masa depan sama persis dengan hari ini).
* Aturan bisnis sederhana (*heuristic rule* berbasis kondisi logika IF-THEN yang saat ini dipakai staf manual).
* Rata-rata bergerak (*moving average*) periode sebelumnya.

Kalau model *neural network* lo menghasilkan akurasi 85%, tapi aturan sederhana berupa rata-rata 3 hari terakhir menghasilkan akurasi 84,5%, maka sistem cerdas lo yang mahal itu cuma menambah kompleksitas tanpa nilai tambah yang signifikan.

---

## Jangan Sampai Terkecoh: Contoh Kasus Penerjemahan yang Tepat

Biar makin kebayang bedanya rumusan kabur vs rumusan matang, coba lo lihat perbandingan konkret ini:

* **Keluhan Bisnis:** "Banyak prospek klien yang masuk ke website tapi menguap gitu aja, tim BD kewalahan ngehubungin satu-satu."
  * **Translasi yang Salah:** "Bikin AI buat naikin penjualan dari website." (Ini bukan rumusan, ini angan-angan).
  * **Translasi yang Benar:** Tugas analitik berupa *ranking* atau klasifikasi biner. Unit analisis: *leads-sesi*. Target: probabilitas prospek memesan sesi konsultasi properti dalam 7 hari ke depan. Metrik teknis: *Precision at Top 20%* (karena kapasitas tim *sales* terbatas hanya bisa menelepon 20 prospek teratas per hari). Baseline: urutan kronologis *first-come first-served*.

* **Keluhan Bisnis:** "Diskon biaya sewa ruang kantor yang kita kasih tahun ini beneran ngefek bikin penyewa betah nggak sih?"
  * **Translasi yang Salah:** Membangun model regresi untuk memprediksi retensi penyewa berdasarkan besaran diskon. (Ini bahaya banget, karena korelasi diskon dan retensi bisa bias akibat faktor lain, misalnya penyewa yang dikasih diskon memang dari awal sudah berniat bertahan lama).
  * **Translasi yang Benar:** Masalah inferensi kausal (*Causal Inference*), bukan prediksi murni. Perlu desain kuasi-eksperimen atau metode *propensity score matching* untuk membandingkan kelompok penyewa yang dapat diskon dengan kelompok kontrol yang tidak dapat diskon namun punya profil risiko serupa.

---

## Anatomi Tujuan yang Baik: Harus Berani Menghadapi Kegagalan

Tujuan proyek sistem cerdas yang dirumuskan dengan benar itu selalu punya satu karakteristik unik: **ia punya kriteria yang jelas untuk dinyatakan gagal.**

Kalau sebuah tujuan proyek berbunyi: *"Menerapkan teknologi AI untuk mengakselerasi transformasi digital dan meningkatkan efisiensi operasional perusahaan,"* tujuan itu adalah sampah birokrasi. Kenapa? Karena kalimat itu nggak bisa disalahkan (*unfalsifiable*). Mau hasilnya jelek, mau sistemnya nggak dipakai, orang tetap bisa ngeles bilang, "Kan kita sudah bertransformasi digital."

Tujuan yang sehat harus memenuhi kaidah SMART:
1. **Actionable:** Output model langsung menentukan tindakan operasional yang spesifik. Jika probabilitas churn > 0,65, kirim tim relasi khusus; jika di bawah itu, kirim buletin rutin.
2. **Terukur (Measurable):** Memiliki metrik teknis dan metrik bisnis dengan ambang batas tegas. Misalnya: *RMSE prediksi harga properti maksimal 5% dari harga penutupan aktual.*
3. **Berbasis baseline:** Harus mengalahkan kinerja metode yang sedang berjalan saat ini dengan margin yang sepadan dengan biaya komputasinya.
4. **Realistis:** Dibangun atas data historis yang benar-benar kita miliki saat ini, bukan mengandalkan data impian yang "katanya mau dikumpulin tahun depan".
5. **Berlingkup jelas (Bounded):** Terbatas pada segmen tertentu, horizon waktu tertentu, dan wilayah tertentu. Misalnya: hanya untuk segmen gedung perkantoran Grade A di area CBD Jakarta untuk jangka waktu prediksi 30 hari.

---

## Delapan Jebakan Problem Framing yang Sering Bikin Tim Terjebak

Gue bikin daftar dosa problem framing ini sambil mengingat-ingat muka rekan-rekan kerja gue di kantor:

1. **Solution-First (Jatuh Cinta pada Algoritma):** Datang ke rapat dengan tekad bulat mau pakai *Deep Learning* atau *LLM Agent*, baru kemudian sibuk mencari-cari masalah bisnis yang kira-kira cocok buat ditempelkan ke algoritma itu.
2. **Proxy Metric yang Menyesatkan:** Mengoptimalkan metrik yang kelihatannya bagus tapi justru merusak bisnis. Contoh klasik: mengoptimalkan jumlah klik atau unduhan brosur properti, padahal yang terpenting adalah nilai transaksi nyata. Jumlah unduhan naik tajam karena promosi gratis, tapi pendapatan kantor malah jeblok.
3. **Label Leakage:** Memasukkan fitur yang secara kronologis baru tercipta setelah target kejadian berlangsung. Model kelihatan luar biasa pintar saat diuji coba di laptop analis, tapi langsung lumpuh total saat di-deploy ke lingkungan produksi.
4. **Target yang Terlalu Luas:** Mencoba menyelesaikan masalah "kepuasan klien" dalam satu model tunggal. Kepuasan itu gabungan dari harga, keramahan staf, kecepatan respons, dan kondisi fisik gedung. Harus dipecah menjadi modul-modul spesifik.
5. **Tanpa Baseline yang Jujur:** Membanggakan performa model akurasi 90% pada data dengan ketidakseimbangan kelas (*imbalanced data*) di mana 90% labelnya memang bernilai negatif. Model naif yang cuma menebak "TIDAK" untuk semua data pun bakal dapat akurasi 90%.
6. **Mengklaim Kausalitas dari Pola Observasional:** Melihat korelasi tinggi antara pengiriman *newsletter* mingguan dengan perpanjangan sewa, lalu langsung menyimpulkan bahwa *newsletter* adalah penyebab utama klien bertahan, padahal klien yang membaca *newsletter* memang sudah sejak awal loyal.
7. **Mengabaikan Asimetri Biaya Kesalahan (*Asymmetric Cost of Errors*):** Menganggap biaya salah tebak positif (*False Positive*) sama dengan biaya salah tebak negatif (*False Negative*). Dalam valuasi aset, meremehkan risiko struktural bangunan fatal akibatnya, jauh lebih berisiko dibanding salah menduga retakan kecil sebagai masalah besar.
8. **Skop yang Membengkak (*Scope Creep*):** Awalnya cuma mau memprediksi harga sewa, lalu di tengah jalan ditambahi fitur rekomendasi renovasi, prediksi arus kas penyewa, dan integrasi chatbot. Akhirnya satu pun modul nggak ada yang selesai sampai batas waktu proyek berakhir.

---

## Catatan Pribadi: Kaitan Langsung ke Tesis GPBSales Milik Lo

Nah, Sar, sekarang bagian paling krusial buat agenda riset lo. Gue dari tadi nulis materi ini sambil terus kepikiran dataset GPBSales lo, data penjualan buku digital yang lagi lo bedah buat tesis.

Di catatan lo sebelumnya, lo sempat cerita kalau masalah bisnis utama lo adalah: **pendapatan bersih (*net revenue*) anjlok drastis dalam dua bulan terakhir, dan pemberian promo diskon justru memotong margin keuntungan bersih per eksemplar cukup dalam.**

Tolong hati-hati banget saat lo menuliskan Bab 1 tesis lo minggu ini. Jangan sampai lo jatuh ke jebakan yang sama kayak tim kantor gue:

Pertama, **soal efektivitas diskon promo.** Pertanyaan "apakah diskon promo menaikkan penjualan?" itu murni masalah **inferensi kausal (*Causal Inference*)**, bukan masalah prediksi biasa! Kalau lo cuma melatih model regresi biasa buat memprediksi angka penjualan berdasarkan besaran diskon, lo bakal terjebak korelasi palsu. Bisa jadi buku lo laris waktu didiskon bukan karena diskonnya sakti, tapi karena diskon itu dikasih pas tanggal gajian atau momen liburan. Framing riset lo di bagian ini harus membandingkan performa periode diskon terhadap kelompok kontrol tanpa diskon dengan karakteristik serupa. Jangan klaim diskon sebagai pemicu utama cuma dari nilai *feature importance* model prediktif lo.

Kedua, **soal modul analitik prediktif GPBSales.** Kalau lo mau bikin modul prediksi buat optimasi penjualan, definisikan empat pilar analitiknya secara kaku:
* **Unit analisis:** Harus tegas, misalnya **seri-hari** (satu baris mewakili satu judul seri buku pada satu hari tertentu). Jangan campur aduk antara level transaksi pembaca individu dengan level agregat judul buku dalam satu tabel yang sama.
* **Target variabel:** Jadikan **pendapatan bersih harian (*daily net revenue*)** sebagai target, bukan sekadar jumlah eksemplar terjual (*volume*). Apa gunanya volume penjualan tembus seribu buku kalau pendapatan bersihnya minus gara-gara diskon kebablasan?
* **Baseline wajib:** Buat baseline naif yang transparan, misalnya rata-rata bergerak 7 hari terakhir (*7-day rolling average*) dari seri buku tersebut. Model prediktif lo baru sah dikatakan bernilai kalau performa MAE (*Mean Absolute Error*) atau RMSE-nya berhasil mengalahkan baseline sederhana ini secara signifikan.
* **Metrik bisnis:** Jangan berhenti di MAE 0,5 eksemplar. Hubungkan metrik error itu ke alokasi promosi: seberapa akurat model lo membantu memutuskan buku seri mana yang layak masuk slot promo berbayar minggu depan agar menghasilkan *return on investment* maksimal?

Urutan yang jujur dalam penelitian lo harus ditulis eksplisit: selesaikan dulu analisis deskriptifnya lewat EDA yang kemarin udah lo rapihin, lakukan uji kausalitas untuk dampak promo diskon, baru susun model prediktifnya untuk perencanaan alokasi di masa depan. Jangan dibolak-balik demi kelihatan canggih di depan dosen penguji.

---

## Kotak Diskusi untuk Sari: Uji Tajam Framing Tesis Lo

Biar lo makin mantap waktu nyusun Bab 1, coba lo bedah tiga pertanyaan reflektif ini sebelum nulis draft akhir:

1. Kalau model prediktif yang lo bangun di tesis GPBSales nanti ternyata punya akurasi tinggi tapi hasil analisis kausalitas menunjukkan bahwa diskon promo sebenarnya tidak memberikan *uplift* pendapatan bersih yang signifikan bagi seri buku lama, keputusan operasional apa yang konkret harus lo ambil terkait kebijakan penetapan harga katalog lo?
2. Dalam dataset penjualan buku digital lo, skenario *label leakage* apa yang paling rawan terjadi tanpa lo sadari kalau lo mau memprediksi total pendapatan bersih mingguan suatu seri buku? Variabel apa saja yang wajib lo blokir dari data latih?
3. Seandainya dosen penguji lo menantang: "Ngapain kamu repot-repot bikin model machine learning kalau penerbit cukup pakai aturan manual diskon 20% tiap akhir bulan?", metrik ganda apa yang bakal lo sodorkan ke meja penguji untuk membuktikan bahwa sistem cerdas lo membawa nilai tambah nyata dibanding aturan heuristik sederhana itu?

Kopi dingin di meja kerja gue udah habis dari tadi, dan gue harus siap-siap lanjut baca modul berikutnya. Semangat beresin perumusan masalahnya ya, Sar.

Salam dari meja kerja yang penuh tumpukan jurnal,

Nik
