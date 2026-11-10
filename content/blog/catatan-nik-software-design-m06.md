---
title: "Catatan Nik: Layar UAT yang Membisu, Jebakan Aplikasi Mobile, dan Misteri Harga Bersih"
subtitle: "Klien minta aplikasi mobile, kontrak jalan, arsitektur dikunci. Pas UAT, agen lapangan cuma butuh dua angka dalam sepuluh detik, dan orang keuangan yang punya definisi harga bersih nggak pernah diajak rapat."
type: blog
date: 2026-11-11T06:28:45.979546+07:00
draft: false
publish_from: file
ws_chat: 1702
ws_msg: 21870
category: "Collab Journal"
tags: ["study", "collab-journal", "MMSI", "software-design", "catatan-nik"]
summary: "Materi pekan ini soal requirement engineering: beda kebutuhan pengguna dan kebutuhan sistem, fungsional dan non-fungsional, model bawang stakeholder, sampai cara mengelola perubahan kebutuhan. Di kantor gue, satu aplikasi mobile hampir jadi roket untuk orang yang cuma butuh sepeda ontel."
hook: "Kebutuhan yang ditulis dalam bentuk solusi itu cara paling mahal buat salah dari awal."
---


Tiga puluh detik pertama di sesi *User Acceptance Testing* hari Selasa kemarin rasanya seperti uji nyali. Di layar proyektor ruang rapat lantai 28, kursor milik Mas Danu, salah satu agen senior dari tim sewa klien kami, berhenti bergerak di tengah-tengah formulir input beranak tujuh tab. 

Vina, yang duduk di sebelah gue dengan blazer andalannya dan senyum *pitching* paling prima, berdeham pelan. "Gimana, Mas Danu? Tampilan *mobile app*-nya sudah sangat *clean* dan modern, kan? Sudah siap *native* buat iOS dan Android."

Mas Danu meletakkan tablet uji coba ke atas meja kaca. Bunyinya agak keras. Dia menatap kami berdua, lalu menghela napas panjang. 

"Mbak Vina, Mbak Nik. Kami di lapangan itu kalau ketemu calon penyewa di lobi gedung perkantoran cuma butuh waktu sepuluh detik buat tahu dua hal: unit mana yang masih kosong, dan berapa harga bersih penawaran terakhir yang boleh kami lepas. Ini kenapa saya harus *login* dua faktor, pilih lima level hierarki properti, lalu disuruh unggah KTP penyewa cuma buat cek histori diskon? Kalau di basement sinyal hilang, aplikasinya malah muter-muter terus *crash*. Kalau begini, tim saya mendingan tetap pakai lembaran kertas cetak atau nanya grup chat kayak biasa."

Gue melirik Aris di sudut meja. Anak itu langsung menunduk, buru-buru mencatat di buku spiralnya dengan muka sepucat kertas HVS. Kontrak proyek ini sudah jalan tiga bulan, arsitektur teknis aplikasi *mobile* berbasis cloud sudah dikunci mati oleh tim pengembang pihak ketiga, dan sekarang, di ujung fase pengujian, kami baru sadar bahwa kami sedang membangun roket luar angkasa untuk orang yang cuma butuh sepeda ontel 🚀

Lebih parah lagi: pas Mas Danu iseng mengecek angka di kolom *net price*, dia langsung mengernyit. "Lho, rumus harga bersih ini kok belum dipotong biaya *service charge* sama komponen pajak sewa khusus kawasan berikat? Siapa yang ngasih rumus ini?"

Gue langsung tahu jawabannya. Rumus itu hasil asumsi tim teknis kami sendiri, karena orang bagian keuangan klien yang memegang definisi baku *harga bersih* sama sekali nggak pernah dilibatkan atau diundang rapat sejak hari pertama proposal diteken. 

Sore itu juga, gue sama Aris harus lembur menyeduh kopi kedua untuk membongkar ulang seluruh daftar kebutuhan dari nol. Pas banget malam ini materi kuliah gue masuk ke *Requirement Engineering*. Di dunia nyata, kalau salah eksekusi di tahap ini, harganya bisa ratusan juta rupiah plus muka tebal di depan dewan direksi.

---

## Fondasi yang Sering Disepelekan 🧱

Di materi minggu ini, dosen gue langsung menegaskan posisi topiknya: kelihatan sepele di atas kertas, tapi dampaknya paling mahal di lapangan. Analogi bangunan yang dikasih di kelas masuk akal banget di kepala gue. Minggu ini gue fokus ke *daftar apa yang sebenarnya diminta dan dibutuhkan penghuni rumah*, sedangkan minggu depan gue baru belajar teknik wawancaranya (*elicitation* dan *analysis*). Kalau daftar kebutuhannya saja sudah ngawur, tukang bangunan paling hebat sedunia pun cuma akan menghasilkan rumah yang salah kamar, salah pintu, dan roboh pas dihantam realitas operasional.

Secara formal, Ian Sommerville mendefinisikan *Requirement Engineering* (RE) sebagai proses menemukan, menganalisis, mendokumentasikan, dan memeriksa layanan serta batasan yang dibutuhkan sistem. 

Dua kata kuncinya sering banget dilupakan orang:

*   **Layanan (*services/what the system should do*)**: fungsi nyata apa yang harus dijalankan sistem untuk membantu pekerjaan manusia di dalamnya.
*   **Batasan (*constraints*)**: rambu-rambu yang membatasi cara fungsi itu berjalan. Batasannya bisa berupa aturan bisnis internal, regulasi pemerintah, batasan infrastruktur jaringan, sampai ketersediaan anggaran dan waktu rilis.

Kalau lo baca laporan legendaris dari Standish Group (*CHAOS Report*) yang sering dikutip dosen gue, tiga biang kerok utama kenapa proyek perangkat lunak gagal di tengah jalan itu hampir nggak pernah berakar dari kesalahan koding sintaks. Tiga penyebab teratasnya selalu sama: kebutuhan yang nggak lengkap, keterlibatan pengguna akhir yang minim, dan perubahan kebutuhan yang dibiarkan liar tanpa kendali. 

Kode yang *buggy* masih bisa ditambal lewat *hotfix* tengah malam. Tapi kalau dari awal kebutuhannya sudah salah arah, tim lo pada dasarnya lagi bikin solusi sempurna untuk masalah yang sama sekali nggak ada.

Di kantor, Vina terjebak pada tiga mitos klasik yang dibantai habis di materi minggu ini:

1.  **Mitos bahwa kebutuhan sama dengan apa yang diucapkan klien di awal.** Klien bilang, "Kami butuh aplikasi *mobile* yang canggih." Vina langsung mencatat kebutuhan sistem adalah "aplikasi *mobile*". Padahal itu solusi, bukan kebutuhan. Kebutuhan aslinya adalah akses data cepat saat berdiri di lobi gedung tanpa repot bawa laptop.
2.  **Mitos bahwa kebutuhan selesai dikunci di dokumen kontrak awal.** Kebutuhan pasti berubah begitu pengguna melihat bentuk nyata sistemnya, dan perubahan itu tanda sistem mulai menyentuh kenyataan. Yang salah bukan perubahannya, tapi ketiadaan mekanisme pengelolaannya.
3.  **Mitos bahwa urusan kebutuhan cuma tugas analis sistem.** Yang menanggung malu pas UAT hancur lebur bukan cuma Aris, tapi gue dari sisi pemasaran, Vina yang megang relasi klien, sampai manajemen yang harus menanggung pembengkakan biaya *rework*.

---

## Empat Roda Penggerak Kebutuhan ⚙️

Sommerville membagi siklus RE jadi empat aktivitas yang seharusnya berputar terus secara berulang (*iterative*), bukan dikerjakan sekali jalan kayak model air terjun kaku zaman dulu:

1.  ***Elicitation and Analysis***: menggali apa yang sebenarnya terjadi di lapangan lewat observasi, wawancara mendalam, sampai bongkar dokumen lama.
2.  ***Specification***: menuangkan hasil temuan itu ke dalam format dokumen yang rapi, terstruktur, dan bisa dipahami dua pihak (bahasa bisnis untuk klien, bahasa teknis untuk pengembang).
3.  ***Validation***: memverifikasi ulang apakah dokumen yang ditulis memang mencerminkan kebutuhan nyata, realistis dikerjakan, konsisten, dan punya tolak ukur pengujian.
4.  ***Requirements Management***: mengelola gelombang perubahan yang pasti datang di sepanjang umur proyek, mencatat siapa yang minta ubah, dan menakar konsekuensi biayanya.

Ada satu catatan penting yang gue garis bawahi tebal-tebal di buku catatan: *elicitation* itu nggak sama dengan *specification*. Menggali masalah lapangan butuh empati dan ketajaman mendengar, sementara menulis spesifikasi butuh presisi teknis dan ketelitian logika. 

Di proyek kami kemarin, Vina melakukan penggalian sambil langsung mengunci spesifikasi di kepalanya sendiri. Begitu dengar kata "lapangan", otak *sales*-nya langsung membayangkan aplikasi Android/iOS dengan visual mengkilap buat bahan portofolio akhir tahun. Nggak ada proses validasi balik ke Mas Danu dan kawan-kawannya. Akibatnya fatal: yang dispesifikasikan adalah apa yang ada di kepala Vina, bukan yang dibutuhkan agen di lapangan.

---

## Dua Tingkat Bahasa: Antara Bahasa Manusia dan Bahasa Mesin

Salah satu materi yang bikin gue melek adalah pemisahan tegas antara dua tingkatan kebutuhan:

### 1. *User Requirements*
Pernyataan kebutuhan tingkat tinggi yang ditulis pakai bahasa awam pengguna. Tujuannya supaya manajer, direktur, dan staf operasional bisa membaca dan sepakat pada tujuan besarnya. 
*Contoh di kantor:* "Sistem harus bisa menampilkan riwayat penawaran unit kantor secara cepat saat agen sedang mendampingi calon penyewa."

### 2. *System Requirements*
Pernyataan terinci yang membedah fungsi sistem sampai ke tingkat teknis tanpa meninggalkan celah multitafsir. Ini panduan kerja nyata buat tim pengembang dan tim penguji (*QA*).
*Contoh turunan teknisnya:* "Sistem harus menampilkan sepuluh riwayat penawaran harga terakhir untuk unit yang dipilih dalam waktu kurang dari dua detik pada koneksi seluler 3G/4G, dengan ukuran muatan data (*payload*) maksimal 150 KB."

Jebakan paling sering terjadi ketika analis berhenti di level *user requirement*, merasa dokumennya sudah selesai karena klien mengangguk paham, lalu langsung menyuruh *programmer* menulis kode. Kata "cepat", "mudah", atau "praktis" itu racun kalau nggak diubah jadi angka. Cepat versi Vina mungkin sepuluh detik masih oke sambil basa-basi, tapi cepat versi Mas Danu adalah maksimal dua detik sebelum calon penyewa mengalihkan pandangan ke layar ponselnya sendiri.

---

## Membedah Fungsi dan Menakar Kualitas 🔧

Di materi minggu ini, perbedaan antara *functional* dan *non-functional requirements* dijelaskan dengan sangat rapi, dan jujur ini bagian yang paling bikin gue tertampar pas inget proyek kami.

### *Functional Requirements* (FR)
FR bicara soal **apa yang harus bisa dikerjakan sistem**: layanan apa yang disediakan, bagaimana reaksi sistem terhadap input tertentu, dan perilaku sistem saat menghadapi kondisi khusus. Pola kalimat bakunya gampang dikenali: *"Sistem harus bisa..."*

Di atas kertas, menulis FR kedengarannya sepele. Tapi ada empat lubang jebakan yang kemarin sukses kami masuki semua:
*   **Hanya mencatat jalur bahagia (*happy path*).** Dokumen proyek cuma nulis "sistem harus bisa menampilkan daftar harga". Tim lupa mendefinisikan apa yang terjadi kalau jaringan internet mati total, kalau unit properti baru saja ditarik dari pasar lima menit lalu, atau kalau agen salah memasukkan kode promo sewa. Tujuh puluh persen logika perangkat lunak itu sebenarnya ada di penanganan kegagalan (*exception handling*), bukan di jalur normalnya.
*   **Ketidakkonsistenan antarpasal.** Di bab keamanan ditulis "semua data histori harga hanya bisa dibuka setelah otentikasi biometrik", tapi di bab pengalaman pengguna ditulis "agen harus bisa melihat ringkasan harga langsung dari layar kunci ponsel". Dua kebutuhan ini saling bertabrakan dan baru ketahuan pas demo.
*   **Ambigu.** Kalimat seperti "data penawaran harus akurat" itu nggak ada artinya tanpa parameter. Akurat menurut pembukuan akuntansi atau akurat menurut estimasi kasar tim pemasaran?
*   **Bercampur aduk dengan keputusan desain.** Menulis "sistem harus memakai menu tarik-turun (*dropdown*) warna biru untuk memilih luas gedung" itu keputusan antarmuka, bukan kebutuhan fungsional. Kebutuhan fungsionalnya murni: "pengguna harus bisa memfilter daftar unit berdasarkan rentang luas ruangan."

### *Non-Functional Requirements* (NFR)
NFR nggak bicara soal fitur baru, melainkan **batasan pada layanan atau seberapa baik fitur tersebut bekerja**. Kalau fungsionalitas itu mesin mobilnya, NFR itu ketahanan suspensi, konsumsi bahan bakar, dan sistem pengeremannya. Sistem lo bisa saja punya sejuta fitur canggih, tapi kalau tiap kali klik tombol butuh waktu *loading* satu menit, sistem itu bakal dibuang ke tempat sampah.

Sommerville membagi NFR ke dalam tiga rumpun besar:

```
                      ┌─────────────────────────────────────────┐
                      │       NON-FUNCTIONAL REQUIREMENTS       │
                      └────────────────────┬────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         │                                 │                                 │
         ▼                                 ▼                                 ▼
┌──────────────────┐             ┌──────────────────┐             ┌──────────────────┐
│     PRODUCT      │             │  ORGANIZATIONAL  │             │     EXTERNAL     │
│   REQUIREMENTS   │             │   REQUIREMENTS   │             │   REQUIREMENTS   │
├──────────────────┤             ├──────────────────┤             ├──────────────────┤
│ • Performance    │             │ • Business Rules │             │ • Regulatory/Law │
│ • Usability      │             │ • Audit Policies │             │ • Data Privacy   │
│ • Reliability    │             │ • Tech Stack     │             │ • Partner APIs   │
│ • Security       │             │ • Data Retention │             │ • Hardware Limits│
└──────────────────┘             └──────────────────┘             └──────────────────┘
```

1.  **Product Requirements (Kualitas Sistem Itu Sendiri)**
    *   *Performance*: aplikasi harus memuat halaman katalog unit maksimal dalam 1,5 detik pada kondisi jaringan 10 Mbps.
    *   *Usability*: agen lapangan baru harus bisa mencari riwayat harga sebuah unit dalam waktu kurang dari tiga menit tanpa perlu membaca buku panduan tebal.
    *   *Reliability*: sistem punya tingkat ketersediaan (*uptime*) minimal 99,8% pada jam kerja operasional (pukul 08.00 sampai 20.00 WIB).
    *   *Security*: data penawaran harga tersimpan dalam bentuk terenkripsi dan riwayat perubahan tercatat permanen di log audit.
2.  **Organizational Requirements (Aturan Rumah Tangga Pemilik Sistem)**
    *   Sistem wajib mengikuti prosedur tata kelola data perusahaan konsultan kami, termasuk integrasi ke sistem otentikasi terpusat yang sudah ada.
    *   Arsitektur sistem harus bisa di-host di lingkungan cloud yang lolos sertifikasi kepatuhan internal, bukan di sembarang penyedia hosting murah.
3.  **External Requirements (Tekanan dari Luar Organisasi)**
    *   Kepatuhan terhadap Undang-Undang Perlindungan Data Pribadi (UU PDP) terkait penyimpanan data identitas calon penyewa korporat.
    *   Batasan perangkat keras: sistem harus bisa beroperasi stabil pada gawai standar inventaris kantor yang memorinya terbatas dan baterainya sudah mengalami degradasi performa.

Biar lo gampang membedakannya pas ngerjain tugas mandiri, dosen gue ngasih panduan matriks konversi dari kalimat kabur menjadi metrik terukur:

| Sifat Kabur (Harapan Hampa) | Metrik Terukur (Bisa Diuji) |
|---|---|
| Sistem harus responsif dan cepat | Halaman profil gedung tampil maksimal 2 detik untuk beban 300 pengguna serentak |
| Aplikasi harus aman dari peretasan | Sesi *login* otomatis kedaluwarsa setelah 15 menit tidak aktif; kata sandi disimpan sebagai hash, bukan teks asli |
| Tampilan harus ramah pengguna | Pengguna awam mampu menyelesaikan alur pencarian unit dalam maksimal 3 langkah navigasi |
| Layanan harus selalu siap pakai | Toleransi waktu henti (*downtime*) terencana maksimal 2 jam per bulan di luar jam operasional |

Dosa terbesar kami kemarin: NFR baru disinggung pas pengujian. Masalah performa di *basement* gedung dianggap cuma "urusan teknis kecil yang bisa diatur belakangan". Padahal begitu arsitektur sistem sudah dikunci ke model yang rakus transfer data konstan ke server induk, bikin aplikasi itu bisa jalan luring (*offline-first*) butuh perombakan total dari struktur basis datanya. NFR bukan kosmetik, NFR adalah keputusan arsitektur.

---

## Siapa yang Duduk di Bawang Itu? 🧅

Pelajaran paling berharga dari materi ini adalah analisis pemangku kepentingan (*stakeholder*). Siapa pun yang memengaruhi atau dipengaruhi oleh keberadaan sistem adalah *stakeholder*.

Model mental yang paling gampang dipakai adalah **Model Bawang (*Onion Model*)**:

```
                  ┌──────────────────────────────────────────────┐
                  │                 LAPISAN LUAR                 │
                  │   Regulator (UU PDP), Pemilik Gedung Mitra   │
                  │   ┌──────────────────────────────────────┐   │
                  │   │            LAPISAN BISNIS            │   │
                  │   │   Tim Keuangan, VP Sales, Direktur   │   │
                  │   │   ┌──────────────────────────────┐   │   │
                  │   │   │     LAPISAN OPERASIONAL      │   │   │
                  │   │   │   Admin Database, Tim IT Ops │   │   │
                  │   │   │   ┌──────────────────────┐   │   │   │
                  │   │   │   │     LAPISAN INTI     │   │   │   │
                  │   │   │   │    Pengguna Akhir    │   │   │   │
                  │   │   │   │     (Mas Danu &      │   │   │   │
                  │   │   │   │    Agen Lapangan)    │   │   │   │
                  │   │   │   │   ┌──────────────┐   │   │   │   │
                  │   │   │   │   │    SISTEM    │   │   │   │   │
                  │   │   │   │   └──────────────┘   │   │   │   │
                  │   │   │   └──────────────────────┘   │   │   │
                  │   │   └──────────────────────────────┘   │   │
                  │   └──────────────────────────────────────┘   │
                  └──────────────────────────────────────────────┘
```

1.  **Lapisan Inti (Pengguna Langsung):** Orang yang tangannya menyentuh sistem tiap hari. Dalam kasus kami, Mas Danu dan tim agen penyewaan properti komersial.
2.  **Lapisan Operasional:** Tim IT klien yang bakal pusing mengurus pemeliharaan rutin, admin hak akses, dan tim meja bantuan (*helpdesk*).
3.  **Lapisan Bisnis:** Manajemen yang melihat hasil akhir lewat laporan pendapatan, termasuk tim keuangan yang menentukan apakah penawaran diskon sewa masih menguntungkan perusahaan.
4.  **Lapisan Luar:** Pihak yang nggak pernah melihat sistemnya sama sekali tapi kena dampak regulasinya, seperti auditor eksternal, pemilik gedung mitra yang menitipkan asetnya, atau lembaga pengawas perlindungan data.

Kesalahan fatal kami kemarin adalah jatuh ke jebakan nomor satu: **cuma mendengarkan atasan yang punya anggaran**. Vina rapat intensif berbulan-bulan dengan Head of Business Development klien. Proposal diteken, anggaran cair, arsitektur jalan. Tapi Mas Danu yang ada di lapisan inti nggak pernah ditanya rutinitas fisiknya di lapangan, dan tim keuangan klien yang ada di lapisan bisnis sama sekali nggak pernah dimintai konfirmasi soal formula bisnis.

Padahal di kantor konsultan gue sendiri, aturan mainnya jelas: Pak Fajar di ujung koridor lantai 28 adalah pemegang otoritas tunggal alur penagihan dan pengakuan pendapatan proyek ke klien. Kalau tim valuasi coba-coba bikin definisi hitungan termin sendiri tanpa restu Pak Fajar, tagihan pasti mandek di meja kasir. Di sisi klien, fungsi Pak Fajar ini dipegang oleh manajer keuangan mereka yang namanya Bu Retno. Tapi Bu Retno nggak diundang ke rapat awal karena dianggap "terlalu teknis dan birokratis". 

Hasilnya? Aplikasi kami menampilkan angka harga sewa bersih yang melanggar standar akuntansi internal klien sendiri. Indah di mata Vina, tapi haram dipakai menurut pembukuan klien.

---

## Menyelamatkan Kapal yang Miring: Mengelola Perubahan Kebutuhan 🚢

Pas sesi istirahat sore kemarin, Aris duduk lemas sambil memandangi tumpukan dokumen spesifikasi setebal 80 halaman yang mendadak nggak berguna. Dosen gue sempat bilang: *kebutuhan yang baik itu harus lengkap, konsisten, tidak ambigu, bisa diuji, bisa dilacak, realistis, dan punya skala prioritas yang tegas.* Dokumen kami tebalnya minta ampun, tapi gagal di poin paling krusial: nggak bisa diuji karena tolak ukur keberhasilannya kabur, dan nggak realistis buat kondisi operasional lapangan.

Biar lo nggak ikut stres, ini langkah darurat yang gue dan Aris ambil tadi malam buat menyusun ulang kebutuhan:

1.  **Pemberian Nomor Unik (*Requirement Traceability Matrix*).** Semua kebutuhan kami bongkar ulang dan diberi kode unik bertingkat (misalnya `FR-PRC-001` untuk fungsi harga, `NFR-PRF-002` untuk performa). Tanpa nomor identitas, mustahil melacak apakah sebuah fungsi berasal dari permintaan Mas Danu atau hasil karangan tim teknis di tengah jalan.
2.  **Klasifikasi Prioritas yang Kejam (Wajib vs Nanti).** Kami membuang separuh fitur pemanis yang dijanjikan Vina di proposal awal. Fitur pemindai kartu nama otomatis dan analisis sentimen calon penyewa kami lempar ke tumpukan daftar tunggu (*backlog*). Kami kunci tiga hal yang wajib hidup: pencarian ketersediaan unit secara luring, histori penawaran tiga bulan terakhir, dan kalkulator harga bersih yang rumusnya sudah divalidasi Bu Retno.
3.  **Satu Pintu Perubahan.** Nggak ada lagi obrolan santai di lobi atau instruksi lewat pesan singkat yang langsung dieksekusi tim pengembang. Setiap permintaan penyesuaian harus melalui formulir dampak: berapa hari penambahan waktu koding, berapa biaya revisi arsitektur, dan siapa penanggung jawab di pihak klien yang berani tanda tangan.

Perubahan kebutuhan itu keniscayaan. Yang bikin proyek hancur berantakan bukan fakta bahwa kebutuhan itu berubah, melainkan kepanikan tim yang membiarkan semua pihak memasukkan daftar keinginan baru tanpa pernah menghitung ulang kapasitas muatan kapalnya.

---

## Bahan Diskusi Kita Selanjutnya

Melihat kekacauan minggu ini, gue makin sadar kalau materi minggu ini bukan cuma hafalan ujian teori di kampus. Ini tameng paling ampuh buat melindungi akal sehat kita dari janji-janji manis presentasi penjualan yang nggak napak tanah.

Minggu depan gue bakal masuk ke teknik penggalian yang lebih dalam (*elicitation* dan *analysis*). Sebelum kelas dibuka, coba lo bantu bedah situasi ini pakai kacamata analis lo, Sar:

1.  Kalau lo diposisikan sebagai analis sistem yang masuk ke proyek di tengah kekacauan seperti kasus kantor gue kemarin, langkah pertama apa yang bakal lo lakukan untuk menyelaraskan Mas Danu (yang frustrasi karena sistemnya ribet) dan Bu Retno (yang murka karena formula keuangannya dilewati), tanpa membuat Vina kehilangan muka di hadapan manajemen puncak klien?
2.  Pilih satu sistem nyata yang paling lo pahami di lingkungan kerja atau organisasi lo sekarang. Coba petakan *stakeholder*-nya ke dalam empat lapisan Model Bawang, lalu turunkan **tiga kebutuhan fungsional** yang punya penanganan jalur gagal (*exception path*), plus **dua kebutuhan non-fungsional** yang parameternya benar-benar bisa diuji secara objektif.

Gue mau lanjut bantu Aris merapikan draf kamus data dan matriks pelacakan kebutuhan sebelum rapat penentuan nasib proyek bareng direksi besok siang.

Dari remah biskuit di atas keyboard,

Nik
