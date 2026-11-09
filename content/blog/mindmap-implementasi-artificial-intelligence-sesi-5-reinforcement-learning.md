---
title: "Mindmap - Implementasi Artificial Intelligence - Sesi 5 - Reinforcement Learning"
type: blog
date: 2026-11-09T23:24:00+07:00
draft: false
category: "Kuliah"
tags: ["Mindmap", "Implementasi Artificial Intelligence"]
summary: "Mindmap reinforcement learning sesi 5: karakteristik dan bedanya dengan supervised, lima komponen formulasi masalah, proses Markov Decision Process, algoritma, aplikasi, sampai tantangannya."
cover: "/images/mindmap/implementasi-artificial-intelligence-sesi-5-reinforcement-learning.png"
---

Ini peta kedua dari sesi 5, bagian reinforcement learning. Sengaja aku pisah dari peta unsupervised, karena kalau digabung pohonnya jadi terlalu lebar dan aku malah bingung sendiri waktu membacanya. Dua topik, dua peta, dan dua-duanya aku gambar sendiri setelah menonton video dan membaca modulnya.

Isi petanya begini:

- **Karakteristik**: reinforcement learning itu belajar apa yang harus dilakukan, memetakan situasi ke tindakan supaya reward-nya paling besar. Aksinya dipandu tujuan dan kondisi saat itu, prosesnya iteratif, dan di awal sama sekali tidak ada label. Dosen juga menyebut bidang ini gabungan banyak ilmu, bukan cuma ilmu komputer.
- **Bedanya dengan supervised**: informasinya hanya sebagian, bukan penuh. Konsekuensi dari tindakan datang tertunda, bukan langsung. Dan yang paling beda, keputusan agent ikut mempengaruhi data yang akan diterima berikutnya, jadi datanya tidak diam seperti di supervised.
- **Kenapa penting**: karena yang dilatih adalah mengambil keputusan dalam ketidakpastian, dan itu bagian dari otonomi serta kecerdasan. Relevan di robotika, model konsumen, industri kesehatan, dan sistem tutor untuk pendidikan.
- **Lima komponen formulasi masalah**: environment sebagai dunia tempat agent beroperasi, state sebagai kondisi agent saat ini, reward sebagai umpan balik dari lingkungan, policy sebagai aturan memetakan kondisi ke tindakan, dan value sebagai perkiraan reward ke depan dari kondisi itu.
- **Proses Markov Decision Process**: agent berada di satu kondisi, memilih aksi, lingkungan pindah ke kondisi baru, agent menerima reward, lalu diulang dari awal. Sifat Markov-nya satu: kondisi berikutnya cukup ditentukan kondisi sekarang dan aksi yang diambil.
- **Algoritma**: dynamic programming yang menghitung dari peta yang sudah ada, Q-Learning yang membuat tabel nilai keadaan dan tindakan, DQN yang versi jaringan saraf dari Q-Learning, SARSA yang memakai urutan state, action, reward, state, action, dan DDPG untuk tindakan yang nilainya tak terbatas.
- **Aplikasi dan tantangan**: aplikasinya ada di robotik, otomasi industri, data processing, dan sistem pelatihan yang menyesuaikan kebutuhan siswa. Tantangannya ruang pencarian yang sangat besar dan tidak diketahui, biaya eksplorasi yang mahal, serta batas eksplorasi soal keselamatan, privasi, dan etika.

Dari dua peta sesi ini, bagian yang paling mengubah cara aku melihat justru baris "keputusan agent mempengaruhi data berikutnya". Selama ini aku membayangkan model itu belajar dari data yang sudah ada, selesai. Di reinforcement learning, modelnya ikut mengubah kenyataan yang nanti dia hadapi sendiri.

Sama seperti peta lainnya, ini versi yang aku pakai untuk belajar, jadi kalau ada cabang yang menurutmu kurang tepat, aku senang kalau dikoreksi.
