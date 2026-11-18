---
title: "Catatan Nik: Angka 96 Persen yang Bikin Rapat Lantai 28 Membeku"
subtitle: "Angka 96 persen di halaman depan deck bikin seisi ruang rapat manggut-manggut, dan gue cuma bisa diam sambil bayangin berapa unit bagus yang bakal kelewat gara-gara model yang nggak pernah diuji ulang."
type: blog
date: 2026-11-17T05:00:00+07:00
draft: false
ws_chat: 1717
ws_msg: 21942
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "implementasi-artificial-intelligence", "evaluasi-model", "catatan-nik"]
summary: "Materi kuliah minggu ini soal cara menilai model AI dengan benar, dari accuracy, precision, recall, sampai siklus hidup proyek yang utuh. Di kantor gue, satu platform vendor dipuja karena akurasi 96 persen, padahal modelnya cuma menebak satu jawaban yang sama untuk hampir semua unit."
hook: "Model yang selalu menjawab hal yang sama masih bisa kelihatan pintar, asal datanya cukup timpang buat menutupi kebodohannya."
---

Layar proyektor di ruang rapat kaca lantai 28 masih menyala terang, memantulkan grafik berwarna merah menyala yang bikin Vina mendadak diam seribu bahasa. Di ujung meja panjang, Pak Fajar mengetuk-ngetukkan pulpennya ke atas tumpukan laporan tagihan proyek, sementara Aris menatap layar laptopnya dengan ekspresi orang yang sudah berusaha mengingatkan tapi tetap disuruh minggir. Gue sendiri duduk di kursi tengah sambil memegangi gelas es americano yang es batunya sudah mencair habis, mencoba mencerna pemandangan tragis di depan mata.

Sar, kalau lo duduk di sebelah gue siang ini, lo pasti ikut meringis melihat betapa kontrasnya suasana ruangan dibanding satu kuartal lalu. Waktu itu, Vina masuk ke ruangan yang persis sama dengan senyum penuh kemenangan, membawa *deck* presentasi dari sebuah vendor platform analitik properti dengan satu angka raksasa di halaman depan: **96 persen**. Angka itu langsung jadi bintang rapat di hadapan jajaran direksi karena vendornya mengklaim model AI mereka sanggup memprediksi unit kantor mana saja yang bakal lama kosong versus unit yang cepat tersewa. Sekarang, sesudah sistemnya dipaksa jalan selama tiga bulan, angka prediksinya melenceng berjamaah dari realita di lapangan.

---

## Rahasia di Balik Angka 96 Persen yang Kelihatan Cantik

Sebelum gue lanjut cerita soal kehancuran kuartal ini, gue tarik dulu ke momen awal saat angka 96 persen itu pertama kali dipuja-puja di rapat direksi. Vina memang tipe *head of sales* yang gampang jatuh cinta sama janji manis teknologi selama kelihatan keren buat dijual ke klien, dan angka setinggi itu jelas bikin siapa pun di meja eksekutif langsung manggut-manggut. Masalahnya, nggak ada satu orang pun di ruangan waktu itu yang nanya gimana cara vendor melakukan **evaluasi model** mereka sebelum berani memajang angka keramat tersebut. Evaluasi model itu sendiri adalah proses mengukur kinerja sebuah model AI pakai tolok ukur yang tepat untuk menjamin modelnya memang layak dipakai, bukan sekadar memoles angka biar kelihatan mentereng di *slide*.

Untungnya, di tim valuasi ada Aris yang tangannya gatal buat ngecek ulang isi dapur vendor pakai data internal kantor gue. Waktu Vina masih semangat memuji betapa tingginya ***accuracy*** platform itu, Aris pelan-pelan membuka lembar kerja berisi ribuan baris riwayat unit perkantoran yang selama ini dikelola tim. Sebagai catatan singkat, *accuracy* itu ukuran paling polos yang cuma menghitung berapa persen tebakan model yang benar dibandingkan total seluruh data yang diuji.

Begitu Aris membedah komposisi data uji yang dipakai, ketahuanlah penyakit utamanya yang dalam dunia data dikenal sebagai ***data imbalance***. *Data imbalance* ini adalah kondisi timpang ketika satu kategori mendominasi jauh lebih banyak jumlah datanya dibandingkan kategori lain. Di sampel portofolio gedung perkantoran kelas B yang dipakai waktu itu, memang 96 persen unitnya berstatus lama kosong, sedangkan cuma 4 persen sisanya yang tergolong unit *fast-moving* alias cepat tersewa.

Tahu nggak apa yang dilakukan model pintar kebanggaan vendor itu? Modelnya praktis cuma menebak satu label yang sama, yaitu "lama kosong", untuk hampir seluruh baris data tanpa repot-repot membedakan mana unit yang potensial laku cepat. Karena kenyataannya memang 96 persen unitnya lama kosong, tebakan malas itu otomatis mencetak *accuracy* 96 persen, padahal secara bisnis modelnya sama sekali nggak berguna karena gagal total mengenali 4 persen unit emas yang justru dicari mati-matian oleh tim pemasaran untuk ditawari promo ke prospek panas.

Supaya direksi dan Vina nggak terus-terusan terhipnotis satu angka persenan, Aris lalu menggambar empat kotak sederhana di papan tulis kaca yang disebut ***confusion matrix***. *Confusion matrix* ini adalah tabel pencocokan antara tebakan model dan kenyataan di lapangan yang memetakan hasil kerja AI ke dalam empat kotak berbeda. Lewat empat kotak itulah kita akhirnya bisa melihat jeroan kesalahan model secara jujur:

*   ***True Positive* (TP)**, yaitu kondisi saat model menebak sebuah unit masuk kategori target yang dicari (unit cepat tersewa) dan kenyataannya memang benar cepat laku.
*   ***True Negative* (TN)**, yaitu kondisi saat model menebak unit masuk kategori bukan target (lama kosong) dan di lapangan memang benar unit itu mangkrak lama.
*   ***False Positive* (FP)**, yaitu jebakan alarm palsu ketika model pede menebak sebuah unit bakal cepat tersewa padahal aslinya tetap nganggur berbulan-bulan.
*   ***False Negative* (FN)**, yaitu kejadian kecolongan saat unit yang aslinya punya potensi cepat laku malah divonis lama kosong oleh model sehingga dilewatkan oleh tim penjualan.

Di kasus platform vendor tadi, kotak *True Negative* terisi hampir penuh karena hampir semua unit memang lama kosong, sedangkan kotak *True Positive* nyaris kosong melompong karena semua unit langka yang dicari malah terbuang masuk ke kotak *False Negative*.

---

## Kenapa *Recall* Bolong dan Metrik Nggak Bisa Dipukul Rata

Begitu Aris menunjuk kotak *False Negative* yang membengkak di papan tulis, baru deh Vina ngeh kenapa tim *leasing* di lapangan ngeluh nggak pernah dapat rekomendasi unit potensial dari sistem baru itu. Di titik ini, obrolan kami langsung bergeser ke metrik bernama ***recall*** yang angkanya nyaris nol pada model vendor tersebut. *Recall* itu ukuran seberapa besar persentase kasus target yang berhasil ditangkap model dari seluruh target asli yang memang beneran ada di lapangan. Karena semua unit cepat tersewa malah ditebak lama kosong, daya tangkap model buat kelas yang paling dicari itu praktis mati total.

"Ya udah, suruh aja vendornya setel ulang biar sistemnya lebih berani nebak 'cepat tersewa', beres kan?" celetuk Vina waktu itu, masih mencoba mencari jalan pintas.

Aris langsung geleng kepala dan menjelaskan bahwa menaikkan daya tangkap sembarangan bakal menghancurkan metrik pasangannya, yaitu ***precision***. *Precision* itu ukuran seberapa jitu tebakan positif sebuah model, alias dari semua unit yang diklaim bakal cepat laku, berapa persen yang memang benar-benar laku. Kalau sistem dibikin terlalu gampang melabeli unit sebagai prospek panas, tim lapangan bakal kebanjiran alarm palsu dan buang-buang anggaran promosi untuk unit yang sebenarnya susah laku.

Di sinilah letak jebakan klasiknya yang disebut ***trade-off precision vs recall***. Kondisi tarik-ulur ini membuat kita nggak bisa memaksimalkan *precision* dan *recall* hingga seratus persen sekaligus, karena menaikkan daya tangkap model biasanya ikut menyeret lebih banyak tebakan yang meleset. Biar kedua ukuran ini nggak saling bunuh dan tetap seimbang saat dipakai menilai model, praktisi biasanya memakai satu angka penengah bernama ***F1-score***. *F1-score* ini adalah nilai rata-rata harmonis yang menggabungkan *precision* dan *recall*, sehingga skornya bakal langsung anjlok kalau salah satu dari keduanya jeblok. Selain itu, kalau tim mau menilai seberapa tajam kemampuan model memisahkan dua kategori di berbagai tingkat ambang kepercayaan, ada juga skor bernama ***ROC-AUC*** yang mengukur kerapian pemisahan kelas tersebut dengan nilai mendekati satu sebagai tanda performa paling tajam.

Sar, di bagian ini gue mendadak keinget materi kuliah minggu ini yang kebetulan banget lagi membahas hal yang sama persis. Lo inget nggak contoh kasus klasifikasi ujaran kebencian berbahasa Indonesia yang memakai ***IndoBERT***? Buat lo yang mungkin baru dengar istilahnya, *IndoBERT* itu model bahasa yang sudah dilatih khusus memahami konteks serta nuansa kalimat berbahasa Indonesia. Di studi kasus kuliah gue itu, modelnya mencatat *accuracy* 0,91 dan *F1-score* 0,90. Lihat deh betapa tipis selisih antara kedua angka itu, yang membuktikan kalau performanya memang merata di kedua kelas dan bukan hasil sulap *data imbalance* kayak dek vendor yang dibawa ke lantai 28.

Lagi asyik-asyiknya Aris membedah metrik kategori tadi, Pak Fajar yang dari tadi diam ikut nyeletuk menanyakan modul kedua dari platform vendor yang sama. Modul kedua ini tugasnya bukan menebak label kategori, melainkan menebak angka perkiraan harga sewa wajar per meter persegi dan estimasi jumlah hari kekosongan unit. Karena keluarannya berupa angka kontinu dan bukan pilihan label, alat ukurnya pindah ke ranah **metrik regresi** yang tugasnya menghitung seberapa jauh melesetnya tebakan angka model dari nilai kenyataan.

Pak Fajar jelas nggak butuh skor persenan menang-kalah, melainkan angka selisih yang langsung nyambung sama hitungan keuangan, dan di sinilah tiga metrik regresi utama dipakai:

1.  ***MAE* (*Mean Absolute Error*)**, yaitu rata-rata selisih absolut antara angka tebakan model dan angka asli di lapangan tanpa mempedulikan tebakannya kelebihan atau kekurangan.
2.  ***MSE* (*Mean Squared Error*)**, yaitu rata-rata selisih tebakan yang dikuadratkan terlebih dahulu supaya kesalahan tebak yang kelewat jauh langsung kena hukuman bobot jauh lebih berat.
3.  ***R-squared***, yaitu skor yang menunjukkan seberapa besar persentase variasi perubahan angka di dunia nyata yang berhasil dijelaskan oleh pola di dalam model.

Kalau *MAE* bilang tebakan meleset rata-rata sepuluh hari, mungkin tim keuangan masih bisa maklum, tapi kalau ada satu unit meleset sampai dua ratus hari, *MSE* bakal langsung teriak keras mengingatkan adanya kesalahan ekstrem.

---

## Jebakan Demo Cantik, *Overfitting*, dan Setelan Mesin

Satu pertanyaan besar yang sempat bikin gue heran di awal adalah gimana caranya platform vendor itu bisa lolos uji coba demo sebelum Aris membongkar pakai data internal. Waktu gue mengobrol berdua dengan Aris di *pantry* sambil nunggu seduhan kopi, ternyata jawabannya klasik banget: model vendor itu kena penyakit ***overfitting*** saat dilatih. *Overfitting* itu kondisi ketika model terlalu menghafal detail kecil beserta gangguan acak di data latihnya sampai gagal beradaptasi begitu ketemu data baru yang sedikit berbeda. Akibatnya, pas dipamerin pakai data sampel buatan vendor sendiri, nilainya melesat tinggi, tapi begitu disiram data riil gedung-gedung SCBD, modelnya langsung gagap.

Tentu saja kebalikannya juga sama bahayanya, yaitu penyakit ***underfitting*** yang terjadi saat model terlalu sederhana dan malas menangkap pola sehingga tebakannya ngawur baik di data latih maupun di data baru. Supaya kantor nggak ketipu lagi oleh hasil demo sekali jalan yang kebetulan bagus, Aris menjelaskan pentingnya ***cross-validation***. *Cross-validation* itu teknik menguji model berkali-kali dengan cara membagi data menjadi beberapa lipatan bergantian sehingga performanya terbukti konsisten di semua potongan data, bukan cuma hoki di satu pembagian saja.

Nggak berhenti di angka agregat, Aris juga membiasakan ***error analysis*** sebelum menandatangani laporan apa pun. *Error analysis* ini adalah kebiasaan membedah langsung baris-baris data yang gagal ditebak oleh model untuk mencari tahu pola kesalahan nyatanya di dunia nyata. Dari situ ketahuan bahwa model sering salah mengira unit podium ritel di lantai dasar punya pola sewa yang sama dengan lantai perkantoran tinggi, padahal perilaku penyewanya beda langit dan bumi.

Dari obrolan soal membedah mesin itulah gue jadi nyambung lagi sama catatan kuliah minggu ini tentang cara tim teknis mengoptimalkan model supaya nggak gampang *overfitting* atau mandek di performa pas-pasan. Sebelum proses latihan algoritma berjalan, tim teknis melakukan ***hyperparameter tuning***, yaitu proses menyetel setelan dasar mesin algoritma sebelum belajar, mirip seperti mengatur suspensi dan rasio gigi mobil sebelum turun ke lintasan balap. Ada tiga cara populer untuk mencari setelan dasar terbaik ini:

*   ***Grid search***, yaitu cara mencari setelan terbaik dengan menguji seluruh kombinasi angka setelan yang sudah didaftarkan satu per satu secara sistematis.
*   ***Random search***, yaitu teknik mencoba kombinasi setelan secara acak dalam jumlah tertentu yang sering kali jauh lebih hemat waktu tanpa harus mengetes semua kemungkinan.
*   ***Bayesian search***, yaitu metode pencarian setelan cerdas yang memanfaatkan hasil uji coba sebelumnya untuk menebak kombinasi mana lagi yang paling berpotensi unggul di percobaan berikutnya.

Selain mengutak-atik setelan awal, model yang terlalu liar menghafal data juga bisa dikekang memakai **regularisasi**, yaitu teknik memberi penalti atau batasan di dalam model supaya tidak nekat menciptakan pola rumit demi menghafal data latih. Ada pula jurus ***early stopping*** yang bertindak sebagai rem darurat dengan cara menghentikan proses latihan model lebih awal tepat di titik ketika performanya di data uji mulai menurun.

---

## Dipaksa Tayang, Lalu Basi dalam Tiga Bulan

Nah Sar, bagian paling menyakitkan dari rapat di lantai 28 hari ini bukan lagi soal temuan Aris di awal dulu, melainkan apa yang terjadi sesudahnya. Meskipun Aris sudah kasih peringatan soal *recall* dan *overfitting*, kontrak langganan platform terlanjur diteken dan manajemen telanjur malu kalau proyeknya dibatalkan sebelum tayang. Vendor akhirnya cuma diminta menambal aturan seadanya lalu platformnya dipaksa jalan di sistem kerja tim penjualan.

Masalahnya, setelah tombol tayang ditekan, nggak ada satu pun pihak yang memantau kesehatan modelnya, sementara kondisi pasar sewa perkantoran berubah drastis dalam tiga bulan terakhir. Ada dua menara perkantoran baru yang masuk ke pasar dengan tarif promo agresif, ditambah tren beberapa perusahaan penyewa yang memangkas luas ruangannya gara-gara pola kerja *hybrid*. Akibatnya, pola lama yang dihafal model langsung kedaluwarsa dan seluruh rekomendasi unitnya hari ini melenceng jauh dari kenyataan.

Melihat kekacauan merah di proyektor tadi, gue langsung kepikiran satu hal penting dari materi kuliah minggu ini: proyek AI bukan kayak beli meja kerja yang sekali ditaruh langsung beres selamanya. Seluruh rangkaian ini seharusnya dijalankan sebagai sebuah ***AI Project Lifecycle***, yaitu alur kerja menyeluruh proyek kecerdasan buatan yang berputar secara berulang (*iteratif*), bukan garis lurus sekali jadi. Kalau ditarik ke kekacauan di kantor gue tadi, alurnya sebenarnya punya delapan stasiun yang nggak boleh dilompati satu pun:

1.  ***Problem definition***, yaitu tahap merumuskan masalah bisnis yang beneran mau dipecahkan dan menyepakati ukuran suksesnya sebelum menyentuh data sama sekali.
2.  ***Data collection***, yaitu proses mengumpulkan bahan baku data yang relevan dan sah dari berbagai sumber internal maupun eksternal.
3.  ***Data preparation***, yaitu pekerjaan membereskan data kotor, menyamakan format yang berantakan, dan menangani kolom kosong supaya layak olah.
4.  ***EDA* (*Exploratory Data Analysis*)**, yaitu tahap mengintip isi data lewat ringkasan statistik dan grafik untuk mengenali pola serta kejanggalannya, persis seperti saat Aris memergoki ketimpangan 96 persen tadi.
5.  ***Modeling***, yaitu tahap melatih algoritma memakai data bersih untuk mempelajari pola hubungan di dalamnya.
6.  ***Evaluation***, yaitu tahap menguji model hasil latihan memakai kombinasi metrik yang tepat demi memastikan kelayakannya sebelum turun ke lapangan.
7.  ***Deployment***, yaitu tahap memasang model yang sudah lolos uji ke sistem nyata agar mulai bisa dipakai oleh tim operasional.
8.  ***Monitoring***, yaitu tahap mengawasi kinerja model secara berkala setelah tayang untuk mendeteksi kalau akurasinya melorot akibat perubahan kondisi dunia nyata.

Gara-gara tahap *monitoring* dan pengulangan siklus ke belakang diabaikan total, model yang tadinya dianggap pintar langsung membusuk pelan-pelan begitu pasar sewa bergeser.

Di atas kertas, delapan tahap itu terdengar rapi, tapi di praktik kantor gue, Aris masih harus mengunduh file manual dan menambal skrip lepas di laptopnya sendiri setiap kali diminta mengecek ulang. Padahal, di organisasi yang sudah matang, seluruh siklus hidup tadi diwujudkan secara teknis lewat ***ML Pipeline***. *ML Pipeline* itu adalah rangkaian alur kerja terprogram yang memindahkan data hingga menjadi model siap pakai secara terpecah per blok (**modular**), berjalan terjadwal tanpa klik manual (**otomatis**), dan bisa diulang kapan saja dengan hasil yang persis sama (***reproducible***).

Di dalam satu mesin otomatis itu, semua proses mengalir berurutan mulai dari ***data ingestion*** yang menarik data mentah secara otomatis dari berbagai sumber, lalu masuk ke ***preprocessing*** untuk pembersihan dan penyeragaman format secara terprogram. Setelah bersih, data melewati ***feature engineering***, yaitu tahap meracik atau memilih variabel petunjuk paling relevan agar algoritma lebih gampang menangkap pola, seperti memisahkan tipe gedung podium ritel dan menara perkantoran tadi. Dari situ, mesin otomatis menjalankan ***training*** untuk melatih ulang model, melemparnya ke tahap ***evaluation*** otomatis sebagai gerbang penyaring kualitas, meluncurkannya lewat proses ***deployment*** ke aplikasi pengguna, hingga menjaga napasnya lewat ***monitoring*** otomatis yang bakal membunyikan alarm kalau angka kesalahannya mulai melewati batas wajar.

Kalau saja kantor gue punya alur sebersih itu, atau minimal mewajibkan vendor membuka dapur evaluasinya sebelum kontrak diteken, rapat kuartalan siang ini nggak bakal berubah jadi sidang pemakaman anggaran proyek.

---

## Buat Bahan Mikir Lo Malam Ini, Sar 🤔

Sambil nunggu kopi kedua gue turun ke lambung buat menetralisir stres ruang rapat, ada tiga pertanyaan yang muncul di kepala gue dari drama lantai 28 ini buat bahan diskusi kita:

1.  Kalau lo jadi manajer bisnis yang harus menentukan arah pengembangan model prediksi unit potensial dengan anggaran promosi tim yang sangat terbatas, kesalahan mana yang lebih mahal buat perusahaan: *False Positive* atau *False Negative*, dan metrik mana yang bakal lo pasang jadi kompas utama?
2.  Melihat kasus model yang langsung melenceng setelah pasar sewa berubah dalam tiga bulan, menurut lo kegagalan terbesarnya sebenarnya terjadi di fase *problem definition* dan *EDA* pada awal proyek, atau murni karena ketiadaan *monitoring* sesudah *deployment*?
3.  Seandainya kuartal depan ada vendor baru lagi datang ke meja direksi membawa klaim *R-squared* atau *accuracy* setinggi langit, syarat verifikasi teknis apa saja dari konsep *cross-validation* hingga kesiapan *ML Pipeline* yang wajib lo jadikan syarat mutlak sebelum tanda tangan kontrak?

---

Lampu ruang rapat kaca akhirnya dimatikan oleh petugas gedung, menyisakan pantulan kota Jakarta yang mulai menyala di balik jendela lantai 28. Gue merapikan laptop ke dalam tas sambil melirik sekilas notifikasi tagihan kegiatan basket dari portal asrama Dylan di layar ponsel, lalu berjalan beriringan menuju lobi lift bersama Aris yang masih menenteng sisa es kopinya tanpa suara. Begitu pintu lift berdenting di lobi dasar, kami berdua cuma saling bertukar senyum lelah sebelum berpisah ke arah masing-masing.

Stay sharp and caffeinated from the 28th floor, ☕✨

Nik
