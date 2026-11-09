---
title: "Mindmap - Implementasi Artificial Intelligence - Sesi 5 - Unsupervised Learning"
type: blog
date: 2026-11-09T23:20:00+07:00
draft: false
category: "Kuliah"
tags: ["Mindmap", "Implementasi Artificial Intelligence"]
summary: "Mindmap unsupervised learning sesi 5: cara mesin belajar tanpa label, empat tipe clustering beserta algoritmanya, association rules dengan support-confidence-lift, sampai reduksi dimensi."
cover: "/images/mindmap/implementasi-artificial-intelligence-sesi-5-unsupervised-learning.png"
---

Sesi 5 mata kuliah Implementasi Artificial Intelligence isinya dua topik sekaligus, unsupervised learning dan reinforcement learning, jadi aku bikin dua peta terpisah. Yang ini bagian unsupervised. Alasannya tetap sama seperti sesi sebelumnya: kalau cuma baca modul, materinya lewat begitu saja. Baru nempel kalau aku gambar ulang dan memutuskan sendiri mana yang jadi cabang, mana yang jadi anak cabang.

Di peta ini alurnya begini:

- **Definisi**: unsupervised learning dipakai untuk analisa dan menemukan pola dari data yang tidak berlabel, tanpa intervensi manusia. Inti kerjanya mengelompokkan data berdasarkan persamaan atau perbedaan di antara data itu sendiri.
- **Empat tipe clustering**: eksklusif menempatkan satu data di satu kelompok saja, contohnya K-Means dengan langkah menentukan jumlah kelompok, menaruh titik pusat, memasukkan data ke pusat terdekat, lalu memindahkan pusat ke rata-rata anggotanya. Overlap atau soft clustering mengizinkan satu data masuk beberapa kelompok dengan bobot, misalnya 30 persen di kelompok A dan 70 persen di kelompok B, dan di situ Fuzzy K-Means masuk. Hirarkis dipakai kalau yang dicari letak bertingkatnya, dengan dua arah kerja, aglomeratif dari spesifik ke umum dan divisif dari umum ke spesifik, hasilnya dibaca lewat dendrogram. Probabilistik memakai sebaran, dan GMM bekerja dengan mean sebagai puncak lonceng serta variance sebagai lebarnya.
- **Kegunaan clustering**: market segmentation, document clustering, image segmentation, dan image compression untuk K-Means. Untuk fuzzy, aku catat penentuan segmen properti, kategori produk di marketplace, dan pasien dengan beberapa penyakit sekaligus. Untuk hirarkis, taksonomi makhluk hidup, struktur folder dokumen, silsilah bahasa, dan wilayah bertingkat. Untuk GMM, pengenalan suara, deteksi anomali, dan segmentasi citra medis.
- **Association**: bukan clustering, karena yang dicari relasi antar variabel, misalnya hubungan antar produk yang berujung pada cross selling dan mesin rekomendasi. Tiga algoritmanya Apriori yang membuang kombinasi jarang, Eclat yang memakai irisan daftar transaksi, dan FP-Growth yang menyusun pohon frekuensi. Cara mengukurnya lewat support, confidence, dan lift, dan ketiga rumusnya aku tulis lengkap di peta.
- **Reduksi dimensi**: mengurangi jumlah fitur tanpa merusak integritas data, gunanya mencegah model overfitting, memudahkan visualisasi, menyiapkan data sebelum training, dan menyederhanakan data survei. Metodenya PCA yang membuat kolom baru pada arah sebaran terlebar, SVD yang memecah tabel besar, dan autoencoder.

Peta ini yang aku buka terakhir sebelum kuis, karena di situ semua istilahnya sudah aku susun sendiri, jadi kalau ada yang ketuker tinggal lihat posisinya. Kalau kamu menemukan cabang yang menurutmu perlu ditambah atau ada istilah yang salah tempat, aku terbuka untuk masukan.
