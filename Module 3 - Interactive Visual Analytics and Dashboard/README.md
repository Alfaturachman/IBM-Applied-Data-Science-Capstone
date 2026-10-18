# Module 03: Interactive Visual Analytics and Dashboard

Dokumen ini memuat panduan navigasi dan rangkuman komprehensif untuk Modul 03: Interactive Visual Analytics and Dashboard pada kursus Applied Data Science Capstone. Modul ini berfokus pada penerapan teknik analitik visual interaktif berbasis web untuk menginvestigasi data spasial dan performa peluncuran roket SpaceX secara *real-time*. Dua pilar teknologi utama yang diintegrasikan mencakup *Folium* berbasis *Leaflet.js* untuk analisis geospasial dan kedekatan wilayah fasilitas peluncuran (*proximity analysis*), serta kerangka kerja *Plotly Dash* untuk membangun aplikasi dasbor terpadu dengan kontrol menu tarik-turun (*dropdown*) dan penggeser rentang (*range slider*) yang mengendalikan visualisasi dinamis.

---

## 1. Ikhtisar Modul dan Metodologi Visual Analitik Interaktif

### A. Paradigma Analisis Visual Interaktif vs Statis
- **Keterbatasan Grafik Statis:**
  - Representasi grafis statis tidak mampu memberikan fleksibilitas saat analis atau pemangku kepentingan (*stakeholders*) ingin meneliti kombinasi parameter spesifik secara dinamis tanpa mengubah kode komputasi.
- **Kekuatan Visual Analitik Interaktif:**
  - Memfasilitasi interaksi langsung pengguna melalui operasi *zoom-in/zoom-out*, penggeseran kanvas (*pan*), penyaringan (*filter*), dan penelusuran (*search*).
  - Menyajikan cerita data (*data storytelling*) yang persuasif, memungkinkan identifikasi kluster keberhasilan dan isolasi faktor risiko secara cepat.

### B. Dua Pilar Teknologi Modul 3 (Folium dan Plotly Dash)
- **Folium (Geospatial Mapping):**
  - Mengonversi data koordinat garis lintang (*Lat*) dan bujur (*Long*) menjadi representasi visual peta interaktif.
  - Memanfaatkan *MarkerCluster* untuk mereduksi kepadatan titik peluncuran yang bertumpuk pada koordinat yang sama serta menghitung jarak geodetik bola bumi (*Haversine*).
- **Plotly Dash (Web Analytic Dashboard):**
  - Kerangka kerja aplikasi web murni berbasis Python untuk membangun antarmuka dasbor responsif.
  - Menggunakan fungsi panggilan balik (*callbacks*) reaktif untuk memperbarui grafik diagram lingkaran (*pie chart*) dan diagram sebar (*scatter plot*) secara instan berdasarkan masukan pengguna.

---

## 2. Struktur Materi dan Kurikulum Modul

### A. Catatan Pembelajaran Konseptual (Study Notes)
- **01 Interactive Visual Analytics and Dashboards.md**: Membahas konsep dasar analitik visual interaktif, arsitektur pemetaan *Folium*, kriteria pemilihan lokasi pangkalan peluncuran optimal, struktur komponen antarmuka *Plotly Dash*, serta alur komunikasi fungsi panggilan balik (*callbacks*).

### B. Evaluasi dan Tantangan Modul (Quizzes)
- **Quiz.md**: Evaluasi pemahaman sintaks *Folium* (`map.add_child` dan `object.add_to`), plugin `MarkerCluster` untuk penanganan penanda bertumpuk, konfigurasi atribut `options` pada `dcc.Dropdown`, pengikatan elemen tata letak melalui `component_id` unik pada dekorator `@app.callback`, serta dukungan multi-input pada fungsi panggilan balik *Dash*.

---

## 3. Rangkuman Pembelajaran dan Metodologi Lab Praktikum

### A. Lab 01: Analisis Geospasial Fasilitas Peluncuran dengan Folium
- **Folder Lab:** `Lab 01 - Interactive Visual Analytics with Folium`
- **Dokumentasi Terperinci:** `Interactive Visual Analytics with Folium.md`
- **Berkas Terkait:**
  - `lab-jupyter-launch-site-location-v2.ipynb`
  - `spacex_launch_geo.csv`
- **Metodologi dan Temuan Utama:**
  - Menandai 4 pangkalan peluncuran utama (`CCAFS LC-40`, `CCAFS SLC-40`, `KSC LC-39A`, `VAFB SLC-4E`) menggunakan lingkaran radius 1.000 meter `folium.Circle` dan penanda label `folium.Marker`.
  - Mengelompokkan amatan peluncuran menggunakan plugin `MarkerCluster` dengan kode warna hijau untuk pendaratan sukses (`class = 1`) dan merah untuk kegagalan (`class = 0`).
  - Mengimplementasikan perhitungan jarak geodetik formula *Haversine* dan menarik garis visual `folium.PolyLine` dari pangkalan `CCAFS SLC-40` ke objek vital di sekitarnya:
    - *Garis Pantai Terdekat (Coastline):* **0,90 km**
    - *Jalan Raya Terdekat (Highway):* **0,58 km**
    - *Jalur Rel Kereta Api (Railway):* **1,28 km**
    - *Pusat Kota Terdekat (City - Titusville):* **23,19 km**
  - Membuktikan secara empiris bahwa pangkalan sengaja ditempatkan di dekat garis pantai samudra demi keselamatan publik, dekat dengan infrastruktur transportasi logistik, dan menjaga zona aman di atas 20 km dari pemukiman warga.

### B. Lab 02: Pembangunan Aplikasi Dasbor Real-Time dengan Plotly Dash
- **Folder Lab:** `Lab 02 - Build an Interactive Dashboard with Plotly Dash`
- **Dokumentasi Terperinci:** `Build an Interactive Dashboard with Plotly Dash.md`
- **Berkas Terkait:**
  - `jupyter-labs-spacex-plotly-dash.ipynb`
  - `spacex_dash_app.py`
  - `spacex_launch_dash.csv`
- **Metodologi dan Temuan Utama:**
  - Merancang tata letak dasbor web menggunakan `dcc.Dropdown` untuk pemilihan pangkalan (`ALL` vs lokasi spesifik) dan `dcc.RangeSlider` untuk filter massa muatan (0 kg s.d. 10.000 kg).
  - Mengonfigurasi callback pertama untuk merender diagram lingkaran (`px.pie`): menampilkan kontribusi pendaratan sukses per pangkalan jika `ALL` dipilih, atau rasio sukses vs gagal jika pangkalan spesifik dipilih.
  - Mengonfigurasi callback kedua untuk merender diagram sebar (`px.scatter`): menampilkan korelasi bobot muatan terhadap keberhasilan misi dengan pembedaan warna kategori varian pendorong roket (*Booster Version Category*).
  - Menuntaskan visualisasi analitik untuk menjawab 5 pertanyaan kunci bisnis:
    - *Pangkalan dengan peluncuran sukses terbanyak:* `KSC LC-39A` (**10 peluncuran sukses**, menyumbang 41,7% total sukses).
    - *Pangkalan dengan rasio keberhasilan tertinggi:* `KSC LC-39A` (**76,92%**).
    - *Rentang muatan paling andal:* **2.000 kg hingga 4.000 kg** (puncak pada interval **3.000 kg s.d. 4.000 kg** dengan keberhasilan **72,7%**).
    - *Rentang muatan paling rawan:* **6.000 kg hingga 8.000 kg** (**0%** keberhasilan / 0 dari 4 sukses).
    - *Varian booster terunggul:* `B5` (Block 5) dengan kesuksesan **100%**, disusul `FT` (*Full Thrust*) dengan kesuksesan **66,67%**.

---

## 4. Key Takeaways dan Implikasi Terhadap Pipeline Capstone

### A. Wawasan Spasial dan Keamanan Operasional
- **Mitigasi Bahaya Penerbangan Antariksa:**
  - Penempatan landasan peluncuran di bibir pantai menghadap samudra lepas meminimalkan risiko terhadap keselamatan jiwa manusia jika terjadi anomali saat fase pembakaran awal.
- **Dukungan Logistik Terintegrasi:**
  - Akses rel kereta api dan jalan raya berjarak sekitar 0,6 km hingga 1,3 km dari landasan mutlak diperlukan untuk mobilisasi komponen roket Falcon 9 berdimensi besar dan bahan bakar propelan cair.

### B. Kesiapan Menuju Pemodelan Prediktif Klasifikasi (Modul 4)
- **Seleksi Fitur Berbobot Tinggi:**
  - Temuan pada Modul 3 memperkuat bukti bahwa lokasi pangkalan (`LaunchSite`), bobot muatan (`PayloadMass`), dan nomor seri/blok pendorong roket memiliki korelasi kausalitas kuat terhadap probabilitas pendaratan sukses.
- **Pondasi Matriks Masukan Model Machine Learning:**
  - Seluruh wawasan analitik interaktif ini mengonfirmasi relevansi 80 fitur numerik hasil *One-Hot Encoding* dari Modul 2 untuk diolah lebih lanjut pada algoritma klasifikasi (*Logistic Regression*, *SVM*, *Decision Tree*, dan *KNN*) pada Modul 4 (*Predictive Analysis*).
