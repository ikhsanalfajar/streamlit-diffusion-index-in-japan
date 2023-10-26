# Laporan Proyek Machine Learning

### Nama : Ikhsan Al Fajar

### Nim : 211351062

### Kelas : Pagi B

## Domain Proyek

Pada bagian ini, kamu perlu menuliskan latar belakang yang relevan dengan proyek yang diangkat.

Permainan video atau yang lebih dikenal sebagai "video game" adalah permainan yang menggunakan interaksi dengan antarmuka (User Interface) melalui gambar yang dihasilkan oleh peranti video. Dalam perkembangan zaman, video game sudah menjadi bagian yang tidak terpisahkan dari kebudayaan kita dan bahkan melahirkan industri yang bernilai jutaan dollar. Berbagai jenis perangkat diciptakan seiring dengan perkembangan tersebut. Genre dari video game juga mengalami perkembangan yang pesat bersamaan dengan berkembanganya video game itu sendiri. Maka dari itu dilakukanlah analisis data guna mendapatkan informasi mengenai popularitas dari video game dengan genre paling sukses dan platform yang digunakannya. Selain itu, guna mendapatkan informasi mengenai penerbit mana yang telah mencapai kesuksesannya dilihat dari banyaknya seri judul yang keluar serta angka penjualannya.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Jelaskan mengapa dan bagaimana masalah tersebut harus diselesaikan
- Adapun alasan survei data analisis ini dilakukan guna mengetahui perkembangan dari video game itu sendiri guna mengetahui bagaimana genre dan platform dari video game itu berkembang diberbagai negara, sehingga dari pihak penerbit maupun pembuat game dapat memikirkan serta memproduksi produk-produk video game baru yang sesuai dengan target pasar berdasarkan minat genre maupun platform dari video game itu sendiri.

- Menyertakan hasil riset terkait atau referensi. Referensi yang diberikan harus berasal dari sumber yang kredibel dan author yang jelas.

  Format Referensi: [Judul Referensi](https://scholar.google.com/)

## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:

- Pernyataan Masalah 1
- Pernyataan Masalah 2
- Pernyataan Masalah n

### Goals

Menjelaskan tujuan dari pernyataan masalah:

- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut:

  ### Solution statements

  - Mengajukan 2 atau lebih solution statement. Misalnya, menggunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan atau melakukan improvement pada baseline model dengan hyperparameter tuning.
  - Solusi yang diberikan harus dapat terukur dengan metrik evaluasi.

## Data Understanding

Paragraf awal bagian ini menjelaskan informasi mengenai data yang Anda gunakan dalam proyek. dataset wajib menggunakan [kaggle](https://www.kaggle.com/) dan **atribut yang digunakan minimal 8 atribut**. Sertakan juga sumber atau tautan untuk mengunduh dataset.<br>

Contoh: [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction).

Kumpulan dataset ini, saya mengambil dari website kaggle yang bersumber dari vgchartz.com, menawarkan banyak wawasan tentang dinamika antara platform dan genre untuk 100 video game teratas di seluruh dunia. Amati platform mana yang mendorong penjualan global, genre apa yang paling sukses di berbagai wilayah di seluruh dunia, dan bagaimana kedua faktor ini berubah seiring berjalannya waktu. Analisis data ini untuk menginformasikan pemahaman Anda tentang industri game dan temukan tren yang mendorong pengembang game menuju kesuksesan!

[Global Video Game Sales](https://www.kaggle.com/datasets/thedevastator/global-video-game-sales)

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:

### Variabel-variabel pada Global Video Game Sales adalah sebagai berikut:

- Rank : Peringkat game berdasarkan penjualan global. (int64)
- Name : Nama permainan.
- Platform : Nama permainan.
- Year : Tahun game ini dirilis.
- Genre : Genre Permainan.
- Publisher : Penerbit permainan.
- NA_Sales : Penjualan game di Amerika Utara.
- EU_Sales : Penjualan game di Eropa.
- JP_Sales : Penjualan game di Jepang.
- Other_Sales : Penjualan game di Wilayah lain.
- Global_Sales : Total penjualan game di seluruh dunia.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation

Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling

Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation

Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:

- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

## Deployment

pada bagian ini anda memberikan link project yang diupload melalui streamlit share. boleh ditambahkan screen shoot halaman webnya.

**---Ini adalah bagian akhir laporan---**

_Catatan:_

- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

san mengenai metrik yang digunakan

- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

##
