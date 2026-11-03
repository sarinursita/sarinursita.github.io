---
title: 'Catatan Nik: Jira Board yang Meledak, Janji Manis Jam Sembilan Pagi, dan Pipa Rilis yang Macet'
subtitle: 'Gue duduk di depan papan Jira yang tiba-tiba penuh kartu HIGH PRIORITY, sementara rilis ke produksi masih bergantung pada satu orang dan satu malam panjang.'
type: blog
date: 2026-11-04T05:57:30+07:00
draft: true
ws_chat: 1668
ws_msg: 21752
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "software-design", "catatan-nik"]
summary: 'Materi pekan ini soal cara Agile dijalankan: peran dan artefak Scrum, lima event, Definition of Done, lalu DevOps dengan pipa CI/CD dan empat metrik DORA. Di kantor gue, papan Jira kebanjiran kartu baru dari sales di tengah Sprint, padahal "selesai" versi tim masih berarti kode jalan di laptop masing-masing.'
hook: 'Kalau kode cuma jalan di laptop sendiri, itu selesai versi siapa?'
---

Layar monitor gue jam sembilan pagi tadi mendadak berubah jadi arena adu ketangkasan mental. Di tab sebelah kiri, gue lagi nyiapin draf presentasi proyek mata kuliah gue yang bobotnya 15 persen itu. Di tab sebelah kanan, grup chat kantor lantai 28 mendadak heboh gara-gara Vina *drop* sepuluh kartu baru ke papan Jira tim valuasi, lengkap dengan label merah bertuliskan *HIGH PRIORITY*. 

Pas Aris dengan suara tercekat nanya di *thread* kenapa lingkup kerjaan minggu ini mendadak nambah dua kali lipat, Vina cuma balas santai dengan stiker kucing: *"Kan kita kerja pakai Agile, Ris! Harus adaptif dong sama dinamika pasar!"*

Gue yang lagi nyeruput *matcha* hangat hampir tersedak di depan laptop. Sar, lo pasti paham rasanya dengar kata *Agile* dipakai seenaknya di depan mata. Di dunia korporat, *Agile* sering banget dijadiin tameng sakti buat menutupi ketiadaan perencanaan, ketidakmampuan sales masang batasan ke klien, atau kemalasan berpikir terstruktur. 

Materi pertemuan lima pekan ini rasanya kayak tamparan realitas yang pas banget buat disodorin ke muka orang-orang yang hobi teriak *Agile* tapi kelakuannya masih feodal. Kita belajar soal bagaimana Agile diterjemahkan secara konkret lewat Scrum, lalu disambungin ke pipa DevOps biar hasilnya nggak cuma mandek jadi artefak di atas kertas. Duduk manis, siapin kopi lo, ini bedahan materi plus drama operasional yang bikin kepala gue berdenyut seharian.

---

## Agile Itu Payung, Scrum Kerangkanya: Jangan Dibalik-balik

Pekan lalu kita udah sepakat kalau *Agile* itu cara berpikir (filosofi yang isinya empat nilai dan 12 prinsip). Masalahnya, nilai luhur doang nggak bisa langsung dikerjain sama tim teknis. Lo nggak bisa datang ke meja Aris terus bilang, *"Ris, tolong dong hari ini lo bekerja secara lebih kolaboratif dan mengutamakan respon terhadap perubahan daripada mengikuti rencana."* Aris bakal bengong, terus buka LinkedIn nyari lowongan baru.

Nilai butuh wadah, dan wadah itu butuh mekanisme pengiriman. Hubungannya sesederhana ini:
* **Agile** adalah filosofi dan arah tujuannya.
* **Scrum** adalah kerangka kerja ringan berulang (*iterative framework*) buat menjalankan filosofi itu lewat aturan main, peran, dan artefak yang terukur.
* **DevOps** adalah budaya dan pipa otomasi (*pipeline*) yang memastikan hasil olahan Scrum lo beneran nyampe ke tangan pengguna secara cepat, aman, dan stabil.

Kalau dosennya nanya apa bedanya Agile dan Scrum di ujian nanti, jawaban paling elegannya adalah: Agile itu payungnya, Scrum adalah salah satu mobil yang berjalan di bawah payung itu. Lo bisa aja jalan pakai mobil lain kayak Kanban, Extreme Programming (XP), atau model *hybrid*. Tapi Scrum yang paling populer karena strukturnya pas buat menghadapi masalah yang kompleks.

Scrum sendiri dibangun di atas **tiga pilar empirisisme**:
1. **Transparency:** Semua hal yang terjadi di dalam proses harus kelihatan jelas oleh semua orang yang terlibat. Nggak ada metrik tersembunyi, nggak ada masalah yang disapu ke bawah karpet.
2. **Inspection:** Artefak kerjaan dan progres diperiksa secara berkala tanpa bikin orang merasa diinterogasi.
3. **Adaptation:** Kalau pas inspeksi ketahuan ada penyimpangan dari jalur yang benar, proses atau rencananya langsung disesuaikan detik itu juga.

Siklus detak jantung Scrum ada di **Sprint**, siklus kerja pendek yang batas waktunya sebulan atau kurang (di kantor gue biasanya pakai ritme dua minggu). Kuncinya satu: di ujung Sprint, tim *wajib* menghasilkan **Increment**, yaitu potongan produk yang beneran berfungsi, memenuhi standar mutu (*Definition of Done*), dan siap dipakai kalau bisnis mau merilisnya.

---

## Tiga Akuntabilitas Scrum: Waktu Semua Orang Mau Jadi Bos tapi Ogah Komitmen

Scrum Guide edisi 2020 udah nggak pakai istilah *role* lagi, melainkan **akuntabilitas**. Ini penting banget, Sar. Kenapa? Karena kata *role* sering bikin orang terjebak kotak jabatan struktural. Di Scrum, cuma ada tiga akuntabilitas:

### 1. Product Owner (PO)
PO bertanggung jawab memaksimalkan nilai produk dan mengelola **Product Backlog**. PO adalah jembatan antara visi bisnis, celotehan klien, dan kapasitas tim. 
* *Yang BUKAN tugas PO:* PO bukan mandor proyek yang ngatur jam kerja harian, dan PO bukan penentu cara teknis arsitektur perangkat lunak.
* *Aturan besi:* Satu produk, satu Product Owner, satu Product Backlog. Kalau ada dua PO, proyek dijamin hancur karena dua kepala bakal rebutan narik prioritas ke arah yang beda.

### 2. Scrum Master (SM)
SM bertanggung jawab memastikan kerangka Scrum dipahami dan dijalankan sesuai panduan, melatih tim, serta menyingkirkan segala hambatan (*impediment*) yang mengganggu jalan tim pengembang.
* *Yang BUKAN tugas SM:* SM bukan sekretaris yang kerjaannya cuma nyatet notulen rapat, bukan juga manajer proyek yang kerjanya nagih tenggat waktu dengan muka galak. SM itu *servant leader*, pelayan yang memfasilitasi tim biar kerjanya mulus.

### 3. Developers (Tim Pengembang)
Orang-orang yang berkomitmen mengubah item backlog jadi Increment yang bernilai setiap Sprint.
* *Catatan kritis:* Kata *developers* di sini bukan cuma programmer yang ngetik kode. Di dalamnya termasuk desainer UI/UX, QA tester, analis data kayak Aris, sampai *security engineer*. Mereka yang megang kendali penuh soal **bagaimana** solusi teknis dibangun.

Kekacauan di kantor gue pagi ini terjadi karena Vina bertindak seolah-olah dia PO yang punya hak mutlak nambah kerjaan di tengah jalan, padahal dia *head of sales*. Dia nge-*bypass* fungsi PO resmi, mengabaikan kapasitas Aris dan tim teknis, lalu mendikte solusi teknisnya sekaligus. Itu bukan Scrum, itu anarki berbalut stiker Jira.

---

## Tiga Artefak dan Tiga Komitmen: Biar "Selesai" Nggak Jadi Debat Rasa

Di Scrum, setiap artefak punya pasangan komitmen yang mengikat secara moral dan operasional. Tujuannya transparan: biar tim punya jangkar yang jelas, bukan sekadar jalan tanpa arah.

| Artefak | Isinya Apa? | Komitmen Pengikatnya |
|---|---|---|
| **Product Backlog** | Daftar hidup berisi semua fitur, perbaikan bug, dan kebutuhan yang mungkin dibangun buat produk. Urut dari nilai tertinggi ke terendah. | **Product Goal** (target jangka panjang produk yang mau dicapai). |
| **Sprint Backlog** | Kumpulan item dari Product Backlog yang dipilih buat dieksekusi di Sprint saat ini, plus rencana teknis mengerjakannya. | **Sprint Goal** (satu tujuan tunggal yang nggak boleh diganggu gugat selama Sprint berjalan). |
| **Increment** | Hasil kerja nyata yang sudah rampung di akhir Sprint dan bisa langsung difungsikan. | **Definition of Done (DoD)** (standar kualitas formal yang disepakati bersama). |

Poin soal **Definition of Done (DoD)** ini sering banget jadi bahan pembantaian dosen pas presentasi, Sar. 

Banyak tim pemula ngerasa kerjaannya udah *Done* cuma gara-gara kodenya jalan di laptop pribadinya si programmer. Begitu ditaruh di server kantor, sistemnya langsung mogok, databasenya meledak, terus mereka lempar-lemparan tanggung jawab. 

DoD yang sehat itu nggak kenal kata "kira-kira". DoD harus tertulis hitam di atas putih:
* Kode sudah di-*merge* ke cabang utama repositori.
* Lolos seluruh rangkaian *unit test* otomatis minimal 80 persen cakupan.
* Lolos uji keamanan (*vulnerability scan*).
* Dokumentasi API sudah diperbarui.
* Sudah berhasil di-*deploy* ke lingkungan *staging* dan lolos uji verifikasi.

Tanpa DoD yang tegas, Sprint Review cuma bakal jadi ajang halusinasi massal tempat tim memamerkan ilusi kemajuan.

---

## Lima Event dalam Scrum: Ritme Kerja, Bukan Pabrik Rapat

Banyak orang benci Scrum karena ngerasa kalendernya penuh rapat nggak berguna. Padahal Scrum cuma punya lima *event*, dan semuanya punya batas waktu ketat (*timebox*). Buat siklus Sprint dua mingguan, begini pembagian rasionalnya:

```
Sprint Planning
       |
       v
Sprint berjalan
  Daily Scrum 15 menit/hari
       |
       v
Sprint Review
       |
       v
Sprint Retrospective
```

1. **Sprint Planning (Maksimal 4 jam):** PO bawa prioritas teratas Product Backlog. Tim pengembang menilai kapasitasnya, memilih apa yang realistis dikerjakan, merumuskan *Sprint Goal*, lalu memecah item jadi tugas-tugas teknis.
2. **Daily Scrum (Tepat 15 menit, tiap hari di jam dan tempat yang sama):** Ini rapat tim pengembang buat tim pengembang, bukan ajang setor muka atau laporan pertanggungjawaban ke manajer! Tujuannya ngecek progres menuju *Sprint Goal* dan ngatur rencana harian. Ada ganjalan apa? Siapa butuh bantuan siapa? Selesai.
3. **Sprint Review (Maksimal 2 jam):** Digelar di akhir Sprint bareng para pemangku kepentingan (*stakeholders*). Tim mendemonstrasikan Increment yang beneran berfungsi. Ingat: tujuannya minta umpan balik langsung (*feedback*), bukan ajang jualan kecap atau presentasi slide PowerPoint penuh animasi.
4. **Sprint Retrospective (Maksimal 1,5 jam):** Dilakukan setelah Review dan sebelum Planning berikutnya. Ini beda krusial yang sering keluar di ujian! Sprint Review ngebahas **produknya** (apa yang kita bikin), sedangkan Retrospective ngebahas **proses dan manusianya** (gimana cara tim kerja selama Sprint, relasi antarorang, alat kerja, dan apa satu hal konkret yang mau kita perbaiki di Sprint depan).
5. **The Sprint Itself (Wadahnya):** Berjalan konsisten tanpa jeda. Begitu Sprint ini kelar, Sprint berikutnya langsung mulai besok paginya.

---

## Masuk ke Dunia DevOps: Jembatan Runtuhnya Tembok Silo

Sekarang bayangin skenario ini: tim Scrum udah disiplin banget. Tiap dua minggu Increment selesai, DoD terpenuhi di lingkungan lokal. Tapi pas mau dirilis ke server produksi biar dipakai klien konsultan properti gue, tim IT operasional bilang: *"Wah, berkas instalasinya belum lolos form perizinan 12B, servernya belum siap, dan kami lagi fokus pemeliharaan rutin. Balik lagi bulan depan ya!"*

Bayangin betapa kacaunya. Janji adaptif di awal Sprint langsung musnah gara-gara rilisnya butuh birokrasi manual berminggu-minggu. Di sinilah **DevOps** masuk sebagai penyelamat.

DevOps itu bukan sekadar nama jabatan atau kumpulan aplikasi canggih, Sar. DevOps adalah gerakan budaya dan praktik teknis yang menyatukan tim pengembang (*Development*) dan tim pengelola operasi (*Operations*). Tujuannya biar jarak antara ide bisnis yang ditulis di kode sampai beneran dinikmati pengguna di lingkungan produksi bisa dipangkas jadi hitungan menit atau jam.

Ingat kerangka kerja **CALMS** yang disebut di buku ajar:
* **Culture:** Menghilangkan mentalitas silo lempar tanggung jawab. Prinsip intinya: *"You build it, you run it."* Siapa yang nulis kodenya, dia juga yang ikut bertanggung jawab kalau sistemnya mati di tengah malam.
* **Automation:** Hilangkan semua campur tangan manual yang rawan salah tik. Otomasi proses *build*, *testing*, konfigurasi server, sampai *deployment*.
* **Lean:** Bekerja dalam tumpukan kecil (*small batch sizes*), batasi kerjaan yang numpuk di tengah jalan (*limit WIP*), dan buang segala pemborosan proses.
* **Measurement:** Jangan pakai firasat. Ukur performa rilis, beban server, dan tingkat galat sistem pakai data telemetri yang valid.
* **Sharing:** Transparansi pengetahuan, bikin dokumentasi hidup, dan bedah insiden secara terbuka tanpa saling menyalahkan (*blameless post-mortem*).

---

## Pipa Pengiriman CI/CD: Jalur Bebas Hambatan Menuju Produksi

Biar CALMS nggak cuma jadi slogan motivasi di dinding kantor, kita butuh infrastruktur konkrit yang namanya pipa CI/CD (*Continuous Integration / Continuous Delivery / Continuous Deployment*). Ini konsep yang sering bikin mahasiswa S2 keseleo pas ujian lisan. Bedainnya harus tegas:

### 1. Continuous Integration (CI)
Tiap kali Aris atau tim teknis ngubah kode di komputernya, kode itu wajib langsung digabung (*commit and merge*) ke repositori utama sesering mungkin, minimal sekali sehari. 

Begitu kode masuk, server CI otomatis:
* Menjalankan proses kompilasi (*build*).
* Mengeksekusi ratusan pengujian unit (*automated unit test*).
* Menjalankan pemindai kualitas kode dan celah keamanan (*static code analysis/security gate*).

Kalau ada kode yang bikin sistem rusak (*broken build*), alarm langsung bunyi dan pengembangnya wajib benerin detik itu juga. Masalah integrasi diselesaikan dalam hitungan menit, bukan ditumpuk di akhir bulan!

### 2. Continuous Delivery (CDel)
Lanjutan dari CI. Setiap perubahan kode yang lolos pengujian otomatis bakal otomatis dipaketkan dan disiapkan ke lingkungan yang persis kayak lingkungan produksi (*staging*). Artefaknya selalu dalam kondisi stabil dan siap dirilis kapan saja. Tapi, **keputusan untuk rilis ke pengguna akhir tetap dipegang manusia** lewat penekanan satu tombol persetujuan bisnis.

### 3. Continuous Deployment (CDep)
Ini level tertingginya. Nggak ada tombol persetujuan manual dari manusia lagi. Begitu kode lolos seluruh rangkaian pengujian otomatis di pipa CI/CD, kode itu **otomatis meluncur langsung ke server produksi** dan live di depan pengguna. Perusahaan teknologi raksasa bisa melakukan puluhan sampai ratusan kali *deployment* per hari berkat pola ini.

```
Commit kode
       |
       v
Build + test otomatis   (CI)
       |
       v
Staging siap rilis (CDel)
       |
       v
Produksi otomatis (CDep)
       |
       v
Monitoring + umpan balik
```

---

## Metrik Pengukuran: Velocity Cuma Pemanis, DORA Itu Ujian Kejujuran

Di Scrum, kita kenal metrik internal kayak **Velocity** (berapa rata-rata poin kerjaan yang bisa diselesaikan tim per Sprint) dan grafik **Burndown/Burnup**. Tapi hati-hati, Sar! Dosennya wanti-wanti banget: Velocity itu alat bantu internal tim buat ngukur kapasitas rencana, bukan rapor buat ngebandingin tim mana yang lebih hebat atau alat manajemen buat nakut-nakutin karyawan.

Kalau mau ngukur kesehatan ekosistem rekayasa perangkat lunak modern secara obyektif, kiblat industri sekarang pakai **DORA Metrics** (*DevOps Research and Assessment*). Ada empat metrik kunci:

1. **Deployment Frequency:** Seberapa sering organisasi lo berhasil merilis kode ke lingkungan produksi? (Tim elit bisa berkali-kali sehari, tim medioker mungkin cuma sekali sebulan).
2. **Lead Time for Changes:** Berapa lama waktu yang dibutuhkan dari satu baris kode dikomit pertama kali sampai beneran jalan di server produksi?
3. **Change Failure Rate (CFR):** Berapa persentase dari rilis lo yang berujung kegagalan, bikin sistem *down*, atau butuh tambalan darurat (*hotfix*)?
4. **Mean Time to Restore (MTTR):** Kalau terjadi insiden di server produksi, berapa lama waktu rata-rata yang lo butuhkan buat memulihkan layanan ke kondisi normal?

Metrik DORA ini jenius banget karena mengunci keseimbangan antara kecepatan dan keandalan. Lo nggak bisa pamer frekuensi rilis 20 kali sehari kalau ternyata *Change Failure Rate* lo menyentuh angka 60 persen dan bikin pengguna ngamuk. Kecepatan tanpa kestabilan itu namanya sabotase diri.

---

## Skala Enterprise: Waktu Satu Tim Kecil Beranak Jadi Puluhan

Scrum itu gampang kalau tim lo cuma tujuh orang yang duduk melingkar di satu ruangan. Tapi gimana ceritanya kalau di level enterprise ada 25 tim yang harus barengan ngerjain satu ekosistem sistem valuasi properti regional?

Ini yang bikin pusing:
* **Arsitektur Monolit yang Kaku:** Kalau arsitektur sistem lo monolitik warisan masa lalu (kayak sistem basis data kantor gue yang separuh kodenya nggak ada dokumentasinya gara-gara ditinggal *resign* sama orang lama), perubahan kecil dari satu tim bisa bikin fungsi tim lain berantakan.
* **Ketergantungan Antar-Tim (*Dependencies*):** Tim A mau ngerilis fitur valuasi tanah, tapi nunggu tim B bikin API autentikasi, yang ternyata nunggu tim C beresin skema basis data. Ujungnya Sprint Goal ketiga tim gagal barengan.
* **Birokrasi Kontrak dan Kepatuhan:** Sistem enterprise selalu kebentur audit legal, sertifikasi ISO, dan kepatuhan finansial yang menuntut dokumentasi berlapis, padahal tim maunya serba cepat.

Buku referensinya nyebut beberapa kerangka *scaling*:
* **Scrum of Scrums:** Paling simpel, cuma pertemuan berkala antar-duta dari masing-masing tim Scrum buat koordinasi dependensi.
* **Nexus & LeSS (Large-Scale Scrum):** Tetap setia pada aturan Scrum murni, mempertahankan satu Product Backlog bersama buat banyak tim.
* **SAFe (Scaled Agile Framework):** Pendekatan berlapis yang sangat terstruktur (tim, program, portofolio). Populer di korporasi besar tapi sering dikritik karena terlalu berat, birokratis, dan mirip Waterfall yang dikasih baju baru.
* **Platform Team Approach:** Ini solusi paling elegan zaman sekarang. Organisasi bikin satu tim internal khusus (*Platform Team*) yang tugasnya bukan bikin fitur bisnis, melainkan nyediain infrastruktur pipa CI/CD otomatis, manajemen server, dan *observability* sebagai layanan mandiri (*self-service*) buat tim-tim pengembang lainnya.

---

## Bedah Proyek Pekan Ini: Racikan Buat Dapet Nilai A

Mengingat proyek pertemuan lima ini bobotnya 15 persen dan bentuknya studi kasus plus presentasi, gue bakal pakai studi kasus sistem yang beneran gue pahami celah penyakitnya. Jangan bikin kasus fiktif toko roti atau perpustakaan kampus yang terlalu klise, Sar. Dosennya bakal bosan setengah mati.

Gue kepikiran kita bikin rancangan arsitektur proses buat: **"Modernisasi Sistem Valuasi Properti Komersial Skala Enterprise Berbasis Scrum dan Integrasi Pipeline CI/CD."**

Struktur laporannya kita kunci dengan alur logis begini:
1. **Analisis Konteks & Masalah:** Paparkan sistem legasi monolitik yang sering jebol pas sinkronisasi data antar-cabang, plus ketergantungan fatal pada proses manual tanpa SOP.
2. **Desain Scrum yang Taat Asas:** 
   * Definisikan satu Product Owner pemegang mandat tunggal (biar nggak ada figur kayak Vina yang bisa seenaknya intervensi).
   * Bentuk tim lintas fungsi (analis, desainer, *developer*, QA).
   * Rancang satu Product Backlog awal (5 sampai 8 *user stories* yang realistis).
   * Rumuskan *Definition of Done* yang ketat (wajib lolos *automated testing* dan pemindaian celah keamanan).
3. **Simulasi Satu Sprint Penuh:** Ceritakan alur dari Sprint Planning penentuan Sprint Goal, dinamika Daily Scrum, demonstrasi fitur operasional di Sprint Review, sampai rencana adaptasi proses di Sprint Retrospective.
4. **Desain Pipa DevOps Terintegrasi:** Gambarkan diagram alur dari *git commit* Aris, proses kompilasi otomatis, eksekusi tes unit, pemindaian SonarQube, *containerization* via Docker, sampai rilis bertahap (*canary deployment*) ke server aktif.
5. **Mitigasi Skalabilitas & Metrik Keberhasilan:** Tunjukkan pemisahan peran via *Platform Team*, plus komitmen pemantauan pakai empat pilar metrik DORA.

Gue yakin kalau alurnya runtut dan berakar dari realitas lapangan yang tajam, rubrik analitik dosennya bakal gue libas habis.

---

## Umpan Balik Buat Sari: Asah Analisis Lo!

Biar persiapan presentasi gue minggu depan makin matang dan gue nggak kagok pas sesi tanya jawab dosen, coba lo bedah beberapa pertanyaan konseptual ini di catatan lo berikutnya:

1. **Tentang Otomasi vs Otorisasi:** Di industri properti dan perbankan yang regulasinya luar biasa ketat soal audit kepatuhan finansial, apakah implementasi *Continuous Deployment* (yang rilis otomatis tanpa persetujuan manusia) beneran realistis buat diterapkan? Atau batas maksimal yang masuk akal sebenarnya cuma mandek di *Continuous Delivery*? Kasih argumen berbasis manajemen risiko.
2. **Kekacauan Akuntabilitas:** Kalau di lapangan lo ketemu situasi di mana manajemen puncak (*C-level*) sering banget nge-*bypass* Product Owner dan nodong tim pengembang buat ngerjain fitur dadakan di tengah Sprint yang lagi jalan, langkah diplomatis dan struktural apa yang harus diambil oleh seorang Scrum Master tanpa harus bikin perang terbuka di kantor?
3. **Ilusi Metrik:** Banyak manajer proyek memakai *Velocity* tim buat dasar pemberian bonus tahunan karyawan. Menurut pemahaman lo soal nilai-nilai Scrum dan metrik DORA, kenapa kebijakan manajemen kayak gitu justru bakal merusak kualitas perangkat lunak dalam jangka panjang? Perilaku manipulatif apa yang bakal muncul di tim pengembang?



*Matcha* gue udah dingin dari tadi gara-gara keasyikan nulis catatan ini di sela-sela ngecek kerjaan. Gue mau jalan keluar sebentar cari udara segar sebelum lanjut ngerapihin draf laporan kita.

Menyeruput sisa matcha yang udah kemanisan,

Nik
