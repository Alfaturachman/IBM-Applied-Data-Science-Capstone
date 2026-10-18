# Module 02: Exploratory Data Analysis (EDA)

Dokumen ini memuat panduan navigasi dan rangkuman komprehensif untuk Modul 02: Exploratory Data Analysis (EDA) pada kursus Applied Data Science Capstone. Modul ini berfokus pada tahapan investigasi mendalam terhadap data historis misi peluncuran SpaceX menggunakan dua pilar metodologi utama: kueri basis data relasional (*SQL*) dan visualisasi data statistik (*Python Matplotlib & Seaborn*). Pembahasan mencakup perumusan kueri analitis terstruktur, analisis korelasi multivariat, evaluasi tren keberhasilan tahunan, hingga rekayasa fitur (*feature engineering*) melalui teknik pengkodean *One-Hot Encoding* (*dummy variables*) yang menghasilkan matriks fitur berdimensi bersih dataset_part_3.csv.

---

## 1. Ikhtisar Modul dan Metodologi Eksplorasi Data

### A. Peran Strategis Analisis Eksploratif Data
- **Jembatan Antara Pembersihan Data dan Pemodelan:**
  - Analisis Eksploratif Data (*Exploratory Data Analysis* / EDA) memungkinkan ilmuwan data memahami karakteristik intrinsik kumpulan data sebelum melatih algoritma pembelajaran mesin.
  - Melalui EDA, anomali data terdeteksi, asumsi distribusi diuji, serta hubungan kausal dan korelasi antar-variabel penjelas dapat diidentifikasi secara kuantitatif dan visual.
- **Sasaran Analitis Utama Modul 2:**
  - Menemukan faktor-faktor teknis dan operasional yang menentukan keberhasilan pendaratan tahap pertama (*first stage booster*) roket Falcon 9.
  - Memeriksa disparitas tingkat keberhasilan lintas pangkalan peluncuran (*LaunchSite*), jenis orbit sasaran (*Orbit*), urutan nomor peluncuran (*FlightNumber*), dan bobot muatan kargo (*PayloadMass*).
  - Menyiapkan matriks fitur numerik penuh (*full numerical feature matrix*) melalui transformasi *One-Hot Encoding*.

### B. Arsitektur Dua Pendekatan EDA (SQL dan Visualisasi)
- **Eksplorasi Berbasis SQL (Database-Driven EDA):**
  - Memanfaatkan basis data relasional *serverless* SQLite dan ekstensi *IPython-SQL* di dalam Jupyter Notebook.
  - Menerapkan kueri deklaratif untuk pemfilteran string (*pattern matching*), fungsi agregasi (*SUM*, *AVG*, *MIN*, *MAX*), pengelompokan (*GROUP BY*), dan subkueri dinamis.
- **Eksplorasi Berbasis Visualisasi Statistik (Visualization-Driven EDA):**
  - Memanfaatkan pustaka *Pandas*, *Matplotlib*, dan *Seaborn*.
  - Menggunakan fungsi tingkat lanjut seperti `catplot` untuk diagram sebar kategorikal, `barplot` untuk agregasi per jenis orbit, dan `lineplot` untuk memetakan kurva tren keberhasilan tahunan.

---

## 2. Struktur Materi dan Kurikulum Modul

### A. Catatan Pembelajaran Konseptual (Study Notes)
- **01 Exploratory Analysis Using SQL.md**: Membahas konsep fundamental EDA, keunggulan pendekatan gabungan SQL dan visualisasi, analisis kurva pembelajaran operasional SpaceX sejak 2013, efek interaksi multivariat pangkalan dan bobot kargo, serta mekanisme *One-Hot Encoding*.

### B. Evaluasi dan Tantangan Modul (Quizzes)
- **Quiz 01.md**: Evaluasi pemahaman kueri SQL analitis, klausa `LIMIT`, fungsi agregasi `MIN()` dan `SUM()`, alias kolom `AS`, pengelompokan `GROUP BY`, serta identifikasi 4 lokasi peluncuran unik.
- **Quiz 02.md**: Evaluasi pemahaman representasi data diagram batang untuk data kategorikal, sintaks bawaan fungsi `catplot`, dan kalkulasi matematis jumlah kolom hasil *One-Hot Encoding* (80 kolom).

---

## 3. Rangkuman Pembelajaran dan Metodologi Lab Praktikum

### A. Lab 01: Analisis Eksploratif Data Berbasis SQL
- **Folder Lab:** `Lab 01 - EDA with SQL`
- **Dokumentasi Terperinci:** `EDA with SQL.md`
- **Berkas Terkait:**
  - `jupyter-labs-eda-sql-coursera_sqllite.ipynb`
  - `my_data1.db`
- **Metodologi dan Temuan Utama:**
  - Mengimpor data CSV SpaceX ke dalam tabel SQLite `SPACEXTBL` dan membuat tabel bersih `SPACEXTABLE` bebas baris kosong.
  - Mengeksekusi 10 tugas kueri analitis terstruktur:
    - Task 1: Menemukan 4 lokasi peluncuran unik (`CCAFS LC-40`, `VAFB SLC-4E`, `KSC LC-39A`, `CCAFS SLC-40`).
    - Task 2: Menyaring 5 baris pertama peluncuran dari pangkalan berawalan `'CCA'`.
    - Task 3: Menghitung total akumulasi massa muatan kargo misi NASA CRS sebesar **45.596 kg**.
    - Task 4: Menghitung rata-rata massa muatan pendorong Falcon 9 varian v1.1 sebesar **2.534,67 kg**.
    - Task 5: Menemukan tanggal pendaratan sukses perdana di landasan darat pada **2015-12-22**.
    - Task 6: Mengidentifikasi pendorong roket sukses di kapal nirawak dengan bobot 4.000 kg hingga 6.000 kg (`B1022`, `B1026`, `B1021.2`, `B1031.2`).
    - Task 7: Menghitung frekuensi status hasil misi (tingkat keberhasilan misi peluncuran di atas 98%).
    - Task 8: Mengidentifikasi seluruh pendorong roket Falcon 9 Block 5 pengangkut satelit Starlink berbobot maksimum **15.600 kg** via subkueri.
    - Task 9: Menganalisis kegagalan pendaratan drone ship tahun 2015 pada bulan 01 (Januari) dan bulan 04 (April).
    - Task 10: Memeringkat frekuensi hasil pendaratan historis periode 2010 s.d. 2017 secara menurun (*descending order*).

### B. Lab 02: Analisis Eksploratif Data Berbasis Visualisasi
- **Folder Lab:** `Lab 02 - EDA with Visualization`
- **Dokumentasi Terperinci:** `EDA with Visualization.md`
- **Berkas Terkait:**
  - `jupyter-labs-eda-dataviz-v2.ipynb`
  - `dataset_part_3.csv`
- **Metodologi dan Temuan Utama:**
  - Menganalisis korelasi visual multivariat:
    - Task 1 & 2: Memetakan hubungan `FlightNumber` dan `PayloadMass` terhadap `LaunchSite`, memperlihatkan konsentrasi uji coba awal di Florida dan pembatasan bobot di pangkalan pesisir barat.
    - Task 3: Menghitung tingkat keberhasilan pendaratan per orbit via diagram batang, di mana orbit `ES-L1`, `GEO`, `HEO`, dan `SSO` mencapai 100%, `VLEO` mencapai 85,7%, sedangkan `GTO` hanya mencapai 51,9%.
    - Task 4 & 5: Memeriksa interaksi nomor penerbangan dan bobot muatan terhadap jenis orbit, mengungkap dominasi keberhasilan muatan berat 15.600 kg pada orbit VLEO.
    - Task 6: Memvisualisasikan tren tahunan menggunakan diagram garis, memperlihatkan lonjakan keberhasilan pendaratan dari 0% (2010 hingga 2013) menjadi di atas 84% hingga 90% (2019 dan 2020).
  - Melakukan rekayasa fitur (*Feature Engineering*):
    - Task 7: Menerapkan fungsi `pd.get_dummies()` pada kolom kategorikal `Orbit`, `LaunchSite`, `LandingPad`, dan `Serial`, memperluas matriks fitur menjadi **80 kolom biner dan numerik**.
    - Task 8: Mengonversi seluruh kolom matriks fitur ke tipe homogen `float64` dan mengekspor hasilnya ke berkas `dataset_part_3.csv` berdimensi (90 baris, 80 kolom).

---

## 4. Key Takeaways dan Implikasi Terhadap Rekayasa Fitur

### A. Pola Kunci Keberhasilan Pendaratan Falcon 9
- **Kematangan Desain dan Sistem Kendali:**
  - Kurva pembelajaran operasional SpaceX terbukti meningkat tajam seiring akumulasi nomor penerbangan, dipicu oleh penyempurnaan desain pendorong roket Falcon 9 Block 5, sirip kemudi titanium tahan panas ekstrem, dan keandalan sistem pembakaran pendaratan (*landing burn*).
- **Pengaruh Energi Orbit Sasaran:**
  - Misi dengan kebutuhan energi tinggi menuju orbit transfer geostasioner (GTO) memiliki batas toleransi propelan cadangan yang lebih tipis dibandingkan misi orbit rendah bumi (LEO/VLEO), sehingga memerlukan strategi pemulihan berbasis kapal nirawak ASDS dengan tingkat risiko lebih tinggi.

### B. Kesiapan Matriks Fitur untuk Pemodelan Machine Learning
- Matriks fitur `dataset_part_3.csv` menyediakan 80 prediktor numerik berkualitas tinggi yang sepenuhnya terstandarisasi.
- Dataset ini siap diintegrasikan langsung ke dalam tahapan pemodelan klasifikasi prediktif (*Classification Algorithms*) pada modul berikutnya, meliputi *Logistic Regression*, *Support Vector Machines* (SVM), *Decision Tree*, dan *K-Nearest Neighbors* (KNN).
