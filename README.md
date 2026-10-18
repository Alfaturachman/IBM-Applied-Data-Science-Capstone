# IBM Applied Data Science Capstone: SpaceX Falcon 9 Landing Prediction

Repositori ini memuat implementasi proyek akhir Applied Data Science Capstone dari IBM Data Science Professional Certificate oleh alfaturachman. Proyek ini mengintegrasikan seluruh siklus ilmu data end-to-end untuk memprediksi keberhasilan pendaratan pendorong roket tahap pertama (first stage booster) SpaceX Falcon 9, yang merupakan faktor kunci di balik keunggulan efisiensi biaya peluncuran roket komersial (62 juta dolar AS vs 165+ juta dolar AS dari kompetitor). Repositori ini memuat seluruh berkas notebook Jupyter yang telah dieksekusi lengkap, skrip aplikasi dasbor interaktif, basis data relasional SQLite, serta laporan presentasi final dalam format PDF dan PowerPoint.

---

## Bagian 1: Struktur Modul Kursus

1. **Module 1 - Introduction**: Pengumpulan data peluncuran roket melalui SpaceX REST API, perayapan web (web scraping) Wikipedia dengan BeautifulSoup, serta data wrangling dan imputasi nilai kosong.
2. **Module 2 - Exploratory Data Analysis (EDA)**: Investigasi data relasional menggunakan kueri SQL pada SQLite dan analisis eksplorasi visual data menggunakan Seaborn dan Matplotlib.
3. **Module 3 - Interactive Visual Analytics and Dashboard**: Analisis geospasial fasilitas peluncuran menggunakan Folium serta pembangunan aplikasi dasbor web interaktif berbasis Plotly Dash.
4. **Module 4 - Predictive Analysis (Classification)**: Prapemrosesan fitur dengan StandardScaler, validasi silang 10-lipatan, penyetelan hiperparameter GridSearchCV, serta evaluasi komparatif 4 model klasifikasi machine learning.
5. **Module 5 - Present Your Data-Driven Insights**: Penyusunan laporan presentasi eksekutif 17 slide (PDF dan PPTX) yang memenuhi seluruh 15 kriteria rubrik kelulusan Coursera, serta skrip otomatisasi generator presentasi berbasis Python.

---

## Bagian 2: Rangkuman Eksekutif per Modul

### Modul 1: Pengumpulan dan Pembersihan Data (Data Wrangling)
- **Ekstraksi Data Multi-Sumber:**
  - Mengambil data 90 catatan peluncuran Falcon 9 historis melalui endpoint SpaceX REST API (`/v4/launches/past`) dan melengkapi atribut pendukung (roket, muatan, landasan, dan inti pendorong).
  - Melakukan perayapan web (web scraping) pada tabel HTML Wikipedia untuk memvalidasi catatan manifest peluncuran pihak ketiga.
- **Data Wrangling dan Rekayasa Fitur:**
  - Menerapkan imputasi nilai rata-rata (mean imputation) untuk menangani nilai kosong pada kolom massa muatan (`PayloadMass`).
  - Mentransformasikan kolom hasil pendaratan mentah (`Outcome`) menjadi label target biner `Class`: nilai 1 untuk pendaratan sukses dan 0 untuk pendaratan gagal atau tidak dicoba.
  - Menerapkan One-Hot Encoding pada fitur kategorikal (`Orbit`, `LaunchSite`, `LandingPad`, `Serial`) untuk menghasilkan matriks masukan berdimensi 80 fitur numerik.

### Modul 2: Eksplorasi Data Berbasis SQL dan Visualisasi Grafis
- **Investigasi Basis Data Relasional SQLite:**
  - Membangun basis data SQLite (`my_data1.db`) dan mengeksekusi kueri agregasi SQL untuk mengidentifikasi 4 situs peluncuran unik (`CCAFS LC-40`, `CCAFS SLC-40`, `KSC LC-39A`, `VAFB SLC-4E`).
  - Menghitung total massa muatan misi NASA (45.596 kg) dan rata-rata massa muatan misi yang berhasil mendarat (5.408 kg).
  - Menemukan tanggal pendaratan darat pertama yang berhasil (22 Desember 2015 oleh pendorong B1019) serta pendorong pembawa muatan maksimum 15.600 kg untuk konstelasi Starlink.
- **Analisis Pola Visualisasi Seaborn:**
  - Menemukan korelasi positif antara nomor penerbangan (`FlightNumber`) dengan tingkat keberhasilan (peluncuran setelah nomor 40 mencatat rasio sukses di atas 80%).
  - Mengidentifikasi orbit dengan tingkat kesuksesan 100%: `ES-L1`, `GEO`, `HEO`, dan `SSO`, sedangkan orbit `GTO` memiliki tantangan pemulihan tertinggi (tingkat sukses ~52%) akibat beban termal re-entry yang ekstrem.
  - Membuktikan tren kenaikan kesuksesan tahunan dari 0% pada 2010 menjadi lebih dari 80% pada 2020.

### Modul 3: Analitik Visual Interaktif (Folium dan Plotly Dash)
- **Pemetaan Geospasial dengan Folium:**
  - Menandai pangkalan peluncuran dengan lingkaran zona keselamatan 1.000 meter dan mengelompokkan catatan peluncuran dengan plugin `MarkerCluster` berkode warna hijau (sukses) dan merah (gagal).
  - Menghitung jarak geodetik formula Haversine dari pangkalan CCAFS SLC-40 ke objek vital: garis pantai (0,90 km), jalan raya (0,58 km), jalur rel kereta api (1,28 km), dan pusat kota Titusville (23,19 km).
  - Membuktikan secara empiris bahwa pangkalan sengaja ditempatkan di bibir pantai menghadap samudra untuk keamanan publik, dekat infrastruktur logistik transportasi darat, dan menjaga jarak aman lebih dari 20 km dari pemukiman warga.
- **Aplikasi Dasbor Web Plotly Dash (`spacex_dash_app.py`):**
  - Mengembangkan antarmuka interaktif dengan kontrol `dcc.Dropdown` dan `dcc.RangeSlider` serta fungsi callback dinamis.
  - Membuktikan pangkalan KSC LC-39A sebagai fasilitas tersukses (10 pendaratan sukses, menyumbang 41,7% total sukses, dengan rasio keberhasilan tertinggi 76,92%).
  - Menemukan rentang muatan paling andal antara 2.000 kg hingga 4.000 kg (keberhasilan 72,7%), rentang paling rawan pada 6.000 kg hingga 8.000 kg (keberhasilan 0%), serta keandalan 100% pada varian Booster Block 5.

### Modul 4: Pemodelan Prediktif Klasifikasi Machine Learning
- **Pipeline dan Optimasi Hiperparameter:**
  - Menstandardisasi 80 fitur numerik menggunakan `StandardScaler` ($z = \frac{x - \mu}{\sigma}$) dan membagi data dengan rasio 80:20 (72 sampel latih dan 18 sampel uji independen).
  - Menerapkan validasi silang 10-lipatan (`cv=10`) dan `GridSearchCV` untuk menyetel 4 algoritma: Logistic Regression, Support Vector Machine (kernel sigmoid optimal), Decision Tree Classifier, dan K-Nearest Neighbors.
- **Hasil Evaluasi dan Matriks Konfusi:**
  - Keempat model klasifikasi mencapai akurasi data uji yang identik sebesar 83,33% (15 prediksi tepat dari 18 sampel uji).
  - Rincian matriks konfusi: 12 True Positives, 3 True Negatives, 3 False Positives, dan 0 False Negatives.
  - Model Logistic Regression direkomendasikan untuk implementasi produksi karena efisiensi komputasi, interpretabilitas tinggi, dan estimasi probabilitas yang halus.

### Modul 5: Laporan Presentasi dan Wawasan Bisnis Strategis
- **Laporan Salindia Portofolio Resmi:**
  - Dokumen presentasi teknis 17 slide yang memenuhi seluruh 15 kriteria rubrik evaluasi Coursera (`Data Science Capstone Project Report.pdf` dan `.pptx`).
  - Skrip otomatisasi Python mandiri untuk mereproduksi salindia dan grafik secara instan (`generate_presentation_pdf.py` dan `generate_presentation_pptx.py`).
- **Wawasan Inovatif Bisnis Antariksa:**
  - Menganalisis dampak finansial asimetris dari kesalahan klasifikasi: ketiadaan False Negative ($FN = 0$) menjamin armada pemulihan laut selalu disiagakan saat roket mendarat selamat, sedangkan False Positive ($FP = 3$) memicu pemborosan biaya mobilisasi kapal nirawak di laut sebesar 200.000 hingga 500.000 dolar AS per misi tanpa aset roket yang dapat dipulihkan.
  - Memberikan rekomendasi penyeimbangan data menggunakan SMOTE atau penyesuaian bobot kelas (`class_weight='balanced'`) untuk meminimalkan kerugian operasional.

---

## Bagian 3: Key Takeaways

- **Kelayakan Komersial Prediksi Machine Learning:**
  - Algoritma pembelajaran mesin mampu memprediksi pemulihan pendorong Falcon 9 dengan akurasi 83,33%, memberikan keunggulan kompetitif bagi entitas kedirgantaraan dalam memperkirakan struktur harga penawaran kontrak peluncuran satelit komersial.
- **Korelasi Muatan dan Orbit Terhadap Keberhasilan:**
  - Misi menuju orbit LEO dan SSO dengan muatan 2.000 hingga 4.000 kg memiliki probabilitas pemulihan pendorong yang sangat tinggi, memungkinkan penawaran agresif pada tingkat biaya 62 juta dolar AS. Sebaliknya, misi GTO berat di atas 6.000 kg memiliki risiko kegagalan pemulihan yang tinggi sehingga penawaran harus memperhitungkan biaya roket sekali pakai.
- **Reproduktifitas Penuh dan Otomatisasi Terpadu:**
  - Seluruh alur kerja dari penarikan data mentah, pembersihan, eksplorasi SQL, analitik spasial, dasbor interaktif, hingga pembentukan presentasi laporan PDF dikemas secara otomatis dan dapat direproduksi secara utuh melalui repositori ini.
