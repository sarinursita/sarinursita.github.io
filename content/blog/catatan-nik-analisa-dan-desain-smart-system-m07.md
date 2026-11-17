---
title: "Catatan Nik: Tiga Kotak di Layar Proyektor Lantai 28, Ilusi Angka Jam Terbang, dan Seni Menghitung Risiko Saat Masa Depan Remang-Remang"
subtitle: "Gue kira slide tiga opsi itu cuma soal presentasi yang rapi, sampai klien minta angka probabilitas dan semua angkanya ternyata cuma jam terbang."
type: blog
date: 2026-11-16T05:00:00+07:00
draft: true
ws_chat: 1732
ws_msg: 21973
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "analisa-dan-desain-smart-system", "decision-tree", "catatan-nik"]
summary: "Pekan ini materinya keputusan di bawah ketidakpastian: tiga unsur yang wajib ada, pohon keputusan dan nilai harapan, sampai influence diagram buat rapat. Di kantor gue, satu slide relokasi klien hampir lolos padahal probabilitasnya cuma jam terbang Vina."
hook: "Slide-nya rapi, tiga opsi, dan satu angka 80 persen yang nggak pernah ada di berkas kerja siapa pun."
---

Laser pointer warna merah milik Vina menari-nari di atas kaca proyektor ruang rapat lantai 28. Di layar sentral, terpampang satu *slide* dengan tata letak minimalis yang rapi banget: tiga kotak persegi panjang berwarna abu-abu muda, biru tua, dan hijau sage. Judulnya mentereng, *Strategic Workspace Recommendation*.

Kotak pertama berbunyi: *Relokasi ke Gedung Baru (Grade A SCBD)*. Kotak kedua: *Renegosiasi Kontrak Gedung Lama*. Kotak ketiga: *Tetap di Tempat (Status Quo)*.

Gaya Vina saat membawakan materi selalu memukau. Sebagai *head of sales*, intonasinya punya ritme yang bikin orang di sekeliling meja otomatis tegak. Dia berdiri dengan setelan blazer krem, memegang *clicker*, lalu mengarahkan titik merahnya tepat ke kotak hijau sage, opsi relokasi. Vina bilang, pindah ke gedung baru adalah langkah paling visioner buat menaikkan pamor korporat klien, mengefisiensikan ruang kerja pascapandemi, dan mendapatkan *concession rate* sewa yang menarik.

Semua orang di ruangan mengangguk perlahan. Sampai akhirnya perwakilan manajemen keuangan klien menyandarkan punggungnya ke kursi ergonomis, mengetuk bolpoin ke buku catatan, lalu bertanya dengan nada datar yang dingin.

"Mbak Vina, kalau kami pilih opsi renegosiasi, berapa probabilitas *landlord* gedung kami saat ini bersedia menurunkan *service charge* dan harga dasar sewa sesuai target kami? Terus, kalau kami nekat ambil opsi relokasi ke gedung baru, berapa peluang kontraktor *fit-out* molor dua bulan, dan berapa total *downtime cost* operasional kami kalau itu terjadi?"

Ruangan mendadak hening. Suara dengung AC sentral lantai 28 tiba-tiba kedengaran sangat jelas. Titik laser merah di tangan Vina sempat bergoyang sepersekian detik sebelum dia tersenyum tenang, khas konsultan kawakan.

"Berdasarkan *track record* kami dan pengalaman belasan tahun menangani portofolio komersial di kawasan segitiga emas, kami sangat optimis 80 persen negosiasi akan tembus, Pak. Untuk relokasi, angkanya sudah kami perhitungkan sangat aman berdasarkan intuisi pasar saat ini."

Aris, analis data junior kami yang duduk di pojok meja dekat stopkontak, langsung menunduk dalam-dalam sambil pura-pura sibuk memeriksa baris kode Python di layar laptopnya. Gue yang duduk di sebelahnya bisa melihat telapak tangannya sedikit basah. Kenapa? Karena kami berdua tahu persis: angka 80 persen itu nggak pernah ada di berkas kerja. Angka itu lahir murni dari rasa percaya diri Vina di detik itu juga, ditopang oleh apa yang orang-orang korporat sering sebut sebagai "jam terbang".

Sepulang klien dari lantai 28, Aris menyenggol siku gue dengan napas tertahan. "Mbak Nik, gue panik setengah mati pas ditanya probabilitas tadi. Kita beneran nggak punya dasar hitungan matematisnya di *slide* itu."

Gue cuma tersenyum tipis, membuka catatan kuliah gue, lalu menarik papan tulis kaca kecil di dekat meja kerja kami. Ini momen yang tepat banget buat membongkar kenapa menyodorkan tiga kotak polos tanpa struktur probabilitas adalah malapraktik paling umum di dunia manajemen, Sar.

---

## Prediksi Keren Bukan Berarti Keputusan Benar: Tiga Unsur yang Sering Hilang di Ruang Rapat

Di kelas, dosen gue sempat menekankan satu prinsip fundamental yang sering banget dilupakan para praktisi: prediksi itu cuma bahan baku, sedangkan keputusan adalah produk akhirnya. Banyak orang mengira kalau kita punya tebakan yang terdengar akurat atau punya analis data yang jago memprediksi tren, kita otomatis bakal menghasilkan keputusan bisnis yang brilian. Padahal jarak antara prediksi dan tindakan nyata itu luar biasa jauh.

Sebuah keputusan rasional dalam sistem informasi manajemen nggak bisa berdiri di atas keyakinan verbal semata. Supaya suatu masalah bisa dianalisis secara probabilistik, kita wajib mengidentifikasi tiga unsur pokok secara eksplisit:

1. **Alternatif tindakan (*alternatives*)**: kumpulan pilihan nyata yang berada penuh di bawah kendali pengambil keputusan. Kita yang menentukan mau melangkah ke cabang mana, misalnya pindah gedung, memperpanjang kontrak, atau merenovasi ruang lama.
2. **Kejadian tidak pasti (*uncertainties* atau *states of nature*)**: peristiwa di masa depan yang berada di luar kendali kita, tetapi memiliki dampak langsung terhadap hasil tindakan. Misalnya, apakah pemilik gedung bersedia menurunkan tarif, apakah izin renovasi keluar tepat waktu, atau apakah ekonomi makro memicu resesi sewa kantor. Setiap kejadian tidak pasti ini punya peluang kejadian atau probabilitas.
3. **Konsekuensi atau hasil (*payoff/values*)**: nilai akhir terukur, bisa berupa keuntungan finansial, total biaya kepemilikan (*total cost of ownership*), atau utilitas operasional yang diperoleh dari kombinasi tertentu antara pilihan tindakan dan peristiwa tidak pasti yang akhirnya benar-benar terjadi.

*Slide* yang dipresentasikan Vina tadi pagi runtuh telak saat diuji oleh tiga pilar ini. Vina cuma menyajikan alternatif di kotak proyektor, tanpa pernah mendefinisikan kejadian tidak pastinya, dan tanpa memetakan konsekuensi numerik yang jujur kalau skenario terburuk terjadi. Opsi "Tetap di Tempat" bahkan cuma dijadikan pajangan pelengkap penderita supaya slidenya terlihat punya opsi pembanding, padahal dalam banyak kasus nyata, tidak melakukan apa-apa (*doing nothing*) sering kali merupakan strategi dasar (*baseline*) yang harus dihitung biayanya secara ketat.

Lebih parah lagi, klaim "80 persen pasti tembus berdasarkan pengalaman" itu menjebak kita ke dalam bias kognitif klasik. Di materi probabilitas, kita belajar bahwa akurasi atau keyakinan tinggi sama sekali tidak menjamin kualitas keputusan yang baik kalau kita mengabaikan kondisi dasar atau *base rate*. Misalnya nih, seorang konsultan merasa analisanya punya akurasi 90 persen dalam menebak keberhasilan negosiasi sewa. Tapi kalau secara umum kondisi pasar perkantoran sedang ketat dan pemilik gedung Grade A jarang sekali mau mengalah pada penyewa skala menengah (katakanlah probabilitas dasarnya cuma 10 persen), maka optimisme 80 atau 90 persen itu adalah ilusi yang berbahaya.

Tanpa memisahkan antara pilihan tindakan kita dan ketidakpastian lingkungan, keputusan akhir di ruang rapat biasanya cuma jatuh ke tangan siapa yang bicaranya paling lantang atau siapa yang jabatannya paling tinggi. Begitu klien menagih kalkulasi terukur di atas kertas, seluruh narasi percaya diri itu langsung menguap tanpa sisa.

---

## Membedah Kekacauan dengan Pohon Keputusan dan Seni Menghitung Nilai Ekspektasi

Melihat Aris yang masih tegang memandangi layar kosong, gue langsung mengambil spidol papan tulis. "Ris, daripada lo stres ngebayangin revisi dek presentasi buat Vina, mending kita bedah kasus klien tadi pakai *decision tree*. Kita bikin model formalnya sekarang."

Pohon keputusan (*decision tree*) adalah alat analisis grafis dan kuantitatif yang mengurutkan kronologi keputusan secara sekuensial dari kiri ke kanan. Keunggulannya ada pada ketegasannya: model ini memaksa kita membedakan secara visual mana hal yang bisa kita pilih dan mana hal yang cuma bisa kita pasrahkan pada peluang.

Strukturnya dibangun dari tiga jenis simpul standar:
- **Simpul keputusan (*decision node*)**, disimbolkan dengan bentuk **persegi**. Ini adalah titik persimpangan di mana pengambil keputusan memegang kendali penuh untuk memilih satu dari beberapa alternatif tindakan.
- **Simpul peluang (*chance node*)**, disimbolkan dengan bentuk **lingkaran**. Ini adalah titik percabangan di mana masa depan berbicara melalui ketidakpastian di luar kendali kita. Cabang-cabang yang keluar dari lingkaran ini mewakili seluruh kejadian yang mungkin terjadi, dan total probabilitas dari seluruh cabang yang keluar dari satu simpul lingkaran wajib berjumlah persis 1,0 (atau 100 persen).
- **Simpul hasil atau terminal (*terminal/payoff node*)**, disimbolkan dengan bentuk **segitiga**. Ini adalah ujung pemberhentian dari setiap jalur ranting pohon, tempat kita mencantumkan nilai hasil akhir finansial atau kerugian riil yang konsisten satuannya.

Gue mengajak Aris menyederhanakan dilema klien properti tadi ke dalam angka simulasi yang masuk akal. Katakanlah klien punya dua alternatif utama di simpul persegi pertama: **Alternatif A (Renegosiasi Kontrak Lama)** dan **Alternatif B (Relokasi ke Gedung Baru)**.

Mari kita bedah jalurnya satu per satu.

Kalau klien memilih **Alternatif A (Renegosiasi)**, muncul simpul lingkaran ketidakpastian dengan dua kemungkinan cabang:
1. Pemilik gedung lama kooperatif dan menyetujui diskon sewa. Berdasarkan data historis okupansi kawasan, peluang kejadian ini adalah **0,60**. Jika skenario ini terwujud, nilai penghematan bersih perusahaan mencapai **Rp 800 juta**.
2. Pemilik gedung lama menolak bernegosiasi dan memberlakukan tarif standar. Peluangnya adalah **0,40** (karena 1,0 dikurangi 0,60). Dalam skenario ini, klien terpaksa membayar biaya sewa normal dengan kerugian operasional atau biaya peluang sebesar minus **Rp 200 juta**.

Sekarang kita lihat **Alternatif B (Relokasi)**. Cabang ini juga berujung pada simpul lingkaran ketidakpastian:
1. Proses pindahan dan renovasi interior (*fit-out*) berjalan mulus tepat waktu. Peluang skenario optimis ini adalah **0,50**, dengan potensi efisiensi ruang kerja jangka panjang senilai **Rp 1,2 miliar**.
2. Pindahan mengalami keterlambatan perizinan dan kontraktor molor selama dua bulan. Peluang skenario ini juga **0,50**. Keterlambatan ini menimbulkan biaya sewa ganda dan disrupsi operasional kantor, sehingga mendatangkan kerugian bersih sebesar minus **Rp 400 juta**.

Setelah seluruh struktur pohon tergambar rapi di papan tulis, langkah berikutnya adalah melakukan perhitungan mundur atau yang di modul kuliah gue disebut sebagai prosedur *rollback* (mengevaluasi pohon dari kanan ke kiri, dari daun kembali ke akar).

Di setiap simpul lingkaran peluang, kita menghitung nilai ekspektasi atau *Expected Value* (EV), yaitu penjumlahan dari hasil kali antara probabilitas kejadian dengan nilai *payoff* di ujung cabang:

`EV = jumlah dari (probabilitas x payoff)` di setiap cabang

Aris langsung mengambil kalkulator di ponselnya dan mulai menghitung:

Untuk simpul peluang pada **Alternatif A (Renegosiasi)**:
`EV-A = (0,60 x Rp 800 juta) + (0,40 x -Rp 200 juta)`
`EV-A = Rp 480 juta - Rp 80 juta = Rp 400 juta`

Untuk simpul peluang pada **Alternatif B (Relokasi)**:
`EV-B = (0,50 x Rp 1.200 juta) + (0,50 x -Rp 400 juta)`
`EV-B = Rp 600 juta - Rp 200 juta = Rp 400 juta`

Mata Aris membelalak melihat hasil akhir di layar ponselnya. "Mbak Nik, nilai ekspektasi kedua alternatifnya persis sama, sama-sama empat ratus juta rupiah!"

"Tepat banget, Ris," sahut gue sambil mengetuk papan tulis. "Dan inilah bukti nyata kenapa presentasi Vina tadi pagi sangat rapuh. Vina jualan opsi relokasi karena terpesona sama angka Rp 1,2 miliar di skenario terbaik. Tapi dia menutup mata bahwa relokasi membawa risiko jurang kerugian minus Rp 400 juta kalau jadwalnya molor, sementara opsi renegosiasi punya lantai risiko yang jauh lebih aman, paling buruk cuma minus Rp 200 juta."

Di titik simpul keputusan persegi paling kiri, seorang analis sistem informasi nggak cuma bertugas memilih angka rata-rata tertimbang tertinggi. Nilai ekspektasi adalah panduan awal untuk kondisi netral terhadap risiko (*risk-neutral*). Namun bagi klien korporat yang kondisi keuangannya sedang ketat pascarestrukturisasi, mereka biasanya memiliki sikap menghindari risiko (*risk-averse*). Bagi mereka, opsi yang memiliki simpangan kerugian ekstrem wajib dihindari meskipun skenario puncaknya terlihat sangat menggiurkan. Menyerahkan angka *expected value* yang dilengkapi profil risiko kerugian jauh lebih bermartabat daripada sekadar bilang *trust me, it works*.

---

## Saat Ranting Terlalu Lebat: Merapikan Ruang Rapat Menggunakan *Influence Diagram*

Puas melihat perhitungan pohon keputusan di papan tulis, Aris mendadak menggaruk kepalanya. "Tapi Mbak Nik, ini kan baru dua variabel acak. Gimana kalau kita masukin variabel biaya penalti terminasi sewa awal, terus probabilitas kenaikan kurs dolar yang memengaruhi harga material impor partisi kantor, ditambah kemungkinan landlord lama ngasih *rent-free period* satu bulan? Ranting pohonnya bakal meledak jadi puluhan cabang. Kalau Vina bawa gambar pohon selebat itu ke direksi klien minggu depan, mereka pasti langsung pusing sebelum sempat baca angkanya."

Kekhawatiran Aris itu valid seratus persen. Di literatur manajemen sains, fenomena itu dikenal dengan istilah *combinatorial explosion*. Begitu kita menambahkan tiga atau empat variabel kejadian berantai, pohon keputusan kita bakal berubah jadi hutan belantara yang sulit dibaca orang awam.

Nah, di sinilah konsep ketiga kita masuk sebagai penyelamat: **Influence Diagram**.

Kalau pohon keputusan menonjolkan urutan kronologis langkah demi langkah beserta seluruh cabang numeriknya, *influence diagram* adalah representasi grafis tingkat tinggi yang memetakan struktur hubungan dependensi antarvariabel secara sangat ringkas. Berbeda dengan jaringan Bayes (*Bayesian network*) yang murni memetakan ketergantungan probabilistik antarvariabel acak tanpa menyediakan simpul aksi manajerial, *influence diagram* memperluas kemampuan itu dengan memasukkan variabel tindakan nyata yang bisa kita kontrol serta tujuan akhir yang ingin kita capai.

Dalam *influence diagram*, satu variabel hanya diwakili oleh satu simpul tunggal, tidak peduli berapa banyak status atau nilai yang dimilikinya. Simbolnya dibagi menjadi tiga bentuk geometris yang sangat tegas:
- **Simpul keputusan (*decision node*)**, digambarkan dalam bentuk **persegi panjang**. Ini mewakili variabel pilihan tindakan kita (misalnya: Keputusan Strategi Ruang Kerja).
- **Simpul peluang (*chance node*)**, digambarkan dalam bentuk **oval atau lingkaran**. Ini mewakili variabel acak tidak pasti yang ada di lingkungan bisnis (misalnya: Sikap Pemilik Gedung Lama, Kelancaran Renovasi Kontraktor, Fluktuasi Tarif Sewa Pasar).
- **Simpul utilitas (*utility node*)**, digambarkan dalam bentuk **belah ketupat (*diamond*)**. Ini mewakili simpul evaluasi akhir atau fungsi objektif yang ingin kita maksimalkan (misalnya: Total Penghematan Finansial dan Kelancaran Bisnis Klien).

Hubungan antar-simpul dihubungkan oleh anak panah berarah (*directed arcs*), yang memiliki makna berbeda tergantung simpul mana yang dituju:
- **Busur kondisional (*conditional arc*)**, yaitu panah yang mengarah ke simpul peluang. Artinya, peluang terjadinya variabel tujuan dipengaruhi oleh kondisi variabel asal.
- **Busur informasional (*informational arc*)**, yaitu panah yang mengarah ke simpul keputusan. Artinya, informasi dari variabel asal sudah harus diketahui secara pasti oleh manajemen sebelum keputusan tersebut diambil.
- **Busur fungsional (*functional arc*)**, yaitu panah yang mengarah ke simpul utilitas belah ketupat. Artinya, variabel asal menjadi komponen masukan langsung dalam menghitung nilai keberhasilan akhir.

Gue langsung menggambar diagram pengaruh itu di sebelah pohon keputusan Aris:

```
[ Keputusan ]
      |
      v
( Renovasi ) --> < Nilai Bersih >
      ^
      |
( Kontraktor )
```

"Lihat bedanya, Ris," kata gue sambil menunjuk diagram sederhana di kaca. "Di satu diagram ringkas ini, direksi klien bisa langsung paham gambaran besarnya dalam sepuluh detik. Mereka bisa melihat bahwa keputusan relokasi yang mereka ambil bakal memengaruhi risiko kelancaran renovasi, dan utilitas keuntungan akhir mereka disandera oleh kinerja kontraktor. Nggak ada drama ranting bercabang-cabang yang bikin mata sepet."

Dalam metodologi rekayasa sistem pengambilan keputusan, kedua alat ini sebenarnya bukan untuk diadu, melainkan saling melengkapi. Praktik terbaik di industri adalah menggunakan *influence diagram* di awal proses konsultasi saat duduk bersama pemangku kepentingan (*stakeholders*) untuk menyepakati batasan masalah, variabel apa saja yang relevan, dan bagaimana keterkaitannya. Setelah strukturnya disepakati bersama di ruang rapat lantai 28, baru tim analis di belakang layar mengonversinya menjadi *decision tree* untuk menghitung nilai ekspektasi dan menentukan titik keputusan optimalnya.

Aris menghela napas panjang, lalu bersandar di kursinya. Senyumnya mulai balik lagi. Beban ketakutan menghadapi revisi dek presentasi Vina tampaknya sudah mencair menjadi rencana aksi yang terstruktur rapi.

---

## Ruang Kerja, Logika, dan Hal-Hal yang Belum Tuntas

Menjelang magrib, suasana kantor SCBD lantai 28 mulai berangsur lengang. Dari dinding kaca di samping meja kerja gue, hamparan lampu jalanan Jakarta Selatan mulai menyala satu per satu, bersaing dengan deretan lampu merah kendaraan yang merayap perlahan ke arah selatan.

Gue merapikan tas kerja, memasukkan binder catatan, dan mematikan monitor eksternal. Drama tiga kotak kosong di layar proyektor tadi siang benar-benar jadi pengingat berharga buat kita berdua yang lagi mendalami magister sistem informasi. Di dunia profesional, sering kali godaan terbesarnya adalah tampil meyakinkan dengan istilah-istilah bombastis dan persentase yang dipetik dari udara hampa, demi menenangkan klien dalam jangka pendek.

Padahal, tugas utama seorang analis sistem bukan menciptakan ilusi kepastian di tengah ketidaktahuan, melainkan menyediakan kerangka berpikir yang jujur untuk menavigasi ketidakpastian itu sendiri. Mengetahui kelemahan model kita dan menyampaikannya secara terukur justru merupakan bentuk kompetensi tertinggi.

Gue mau melempar tiga hal ini buat bahan perenungan catatan lo berikutnya, Sar:

1. Di skenario pohon keputusan tadi, nilai ekspektasi (*expected value*) antara opsi renegosiasi dan opsi relokasi berakhir persis sama di angka Rp 400 juta. Namun, rentang variansi kerugian keduanya sangat jomplang. Menurut kacamata lo, bagaimana kita merancang sistem pendukung keputusan (*decision support system*) yang bisa mengintegrasikan fungsi utilitas risiko klien secara kuantitatif, supaya sistem tidak bias merekomendasikan opsi berisiko tinggi hanya karena nilai puncaknya besar?
2. Jika manajemen klien bersedia mengalokasikan anggaran riset tambahan sebesar Rp 50 juta untuk menyewa auditor independen guna memeriksa kelayakan kontraktor sebelum mengambil keputusan relokasi, konsep nilai informasi sempurna (*expected value of perfect information* / EVPI) dari modul gue kan membatasi batas atas biaya riset tersebut. Dalam konteks sistem informasi manajemen, bagaimana cara kita menilai apakah investasi pada sistem pengumpul data baru (*data acquisition*) sebanding dengan potensi penurunan risiko salah pilih keputusan?
3. Saat sebuah organisasi menghadapi permasalahan strategis yang sangat rumit dengan belasan variabel acak yang saling bertaut, kapan saat yang tepat bagi seorang *system analyst* untuk berhenti memperluas *influence diagram* agar modelnya tidak jatuh menjadi terlalu rumit dan kehilangan daya gunanya di level operasional?

Suara denting lift lantai 28 berbunyi pelan menandakan mobil jemputan gue sudah mendekat di lobi bawah. Gue tutup dulu catatan ini sebelum baterai laptop gue benar-benar habis di perjalanan pulang.

Sampai ketemu di catatan berikutnya, ya.

Nik