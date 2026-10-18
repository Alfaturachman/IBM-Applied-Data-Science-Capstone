# IBM Applied Data Science Capstone: SpaceX Falcon 9 Landing Prediction

Repositori ini memuat implementasi proyek akhir Applied Data Science Capstone dari IBM Data Science Professional Certificate oleh alfaturachman. Proyek ini mengintegrasikan seluruh siklus ilmu data end-to-end untuk memprediksi keberhasilan pendaratan pendorong roket tahap pertama (first stage booster) SpaceX Falcon 9, yang merupakan faktor kunci di balik efisiensi biaya peluncuran roket komersial (62 juta dolar AS vs 165+ juta dolar AS dari kompetitor). Repositori ini memuat seluruh berkas notebook Jupyter yang telah dieksekusi lengkap, skrip aplikasi dasbor interaktif, basis data relasional SQLite, serta laporan presentasi final dalam format PDF dan PowerPoint.

---

## Bagian 1: Struktur Berkas Repositori

1. **jupyter-labs-spacex-data-collection-api-v2.ipynb**: Ekstraksi 90 catatan peluncuran melalui SpaceX REST API dan penguraian atribut penunjang.
2. **jupyter-labs-webscraping.ipynb**: Perayapan web (web scraping) pada tabel HTML Wikipedia menggunakan BeautifulSoup untuk memvalidasi catatan peluncuran historis.
3. **labs-jupyter-spacex-Data-wrangling-v2.ipynb**: Penanganan nilai kosong massa muatan dengan imputasi nilai rata-rata, rekayasa variabel target biner `Class` (1 = sukses, 0 = gagal), dan pembentukan matriks fitur.
4. **jupyter-labs-eda-sql-coursera_sqllite.ipynb**: Investigasi relasional SQLite untuk 10 kueri analitik (total muatan NASA, rata-rata muatan sukses, pendaratan pertama, dan ranking pendorong).
5. **my_data1.db**: Basis data relasional SQLite lokal berisi tabel `SPACEXTBL`.
6. **jupyter-labs-eda-dataviz-v2.ipynb**: Analisis visualisasi data menggunakan Seaborn dan Matplotlib untuk menguji korelasi muatan, orbit, dan tren tahunan.
7. **dataset_part_3.csv**: Matriks masukan hasil One-Hot Encoding berdimensi 80 fitur numerik.
8. **lab-jupyter-launch-site-location-v2.ipynb**: Pemetaan geospasial interaktif Folium, penandaan fasilitas, pengelompokan MarkerCluster, dan kalkulasi jarak geodetik Haversine.
9. **spacex_launch_geo.csv**: Set data koordinat lintang dan bujur fasilitas peluncuran.
10. **jupyter-labs-spacex-plotly-dash.ipynb**: Notebook pengujian fungsi callback reaktif Plotly Dash.
11. **spacex_dash_app.py**: Skrip mandiri aplikasi web dasbor interaktif berbasis Plotly Dash dengan kontrol menu tarik-turun dan penggeser rentang muatan.
12. **spacex_launch_dash.csv**: Set data terstruktur pendukung aplikasi dasbor Plotly Dash.
13. **SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb**: Pipeline klasifikasi machine learning (StandardScaler, train-test split 80:20, validasi silang 10-lipatan, penyetelan GridSearchCV pada Logistic Regression, SVM, Decision Tree, dan KNN).
14. **Data Science Capstone Project Report.pdf**: Laporan presentasi teknis eksekutif 18 slide berformat PDF yang memenuhi seluruh kriteria rubrik evaluasi Coursera.
15. **Data Science Capstone Project Report.pptx**: Salindia presentasi Microsoft PowerPoint rasio layar lebar 16:9 yang dapat disunting bebas.

---

## Bagian 2: Rangkuman Eksekutif per Tahapan Proyek

### 1. Pengumpulan dan Pembersihan Data (Data Wrangling)
- **Ekstraksi Data:** Mengambil 90 rekaman peluncuran roket Falcon 9 dari endpoint REST API SpaceX (`/v4/launches/past`) dan menyelaraskannya dengan data hasil web scraping tabel Wikipedia menggunakan BeautifulSoup.
- **Wrangling dan Rekayasa Fitur:** Menerapkan imputasi nilai rata-rata pada kolom `PayloadMass` yang kosong; mentransformasikan hasil pendaratan pendorong roket menjadi target biner `Class` (1 untuk pendaratan sukses dan 0 untuk pendaratan gagal/tidak dicoba); menerapkan One-Hot Encoding pada fitur kategorikal (`Orbit`, `LaunchSite`, `LandingPad`, `Serial`) sehingga menghasilkan 80 fitur numerik.

### 2. Eksplorasi Data Berbasis SQL dan Visualisasi Grafis
- **Analisis Kueri SQL SQLite:** Mengeksekusi 10 kueri terstruktur pada basis data `my_data1.db`: mengidentifikasi 4 situs peluncuran unik (`CCAFS LC-40`, `CCAFS SLC-40`, `KSC LC-39A`, `VAFB SLC-4E`), menghitung akumulasi muatan misi NASA (45.596 kg), rata-rata muatan sukses (5.408 kg), pendaratan darat sukses pertama pada 22 Desember 2015 oleh pendorong B1019, serta kapasitas muatan maksimum 15.600 kg pada pendorong Block 5.
- **Visualisasi Seaborn:** Menemukan korelasi positif nomor penerbangan terhadap keberhasilan misi (penerbangan setelah nomor 40 mencatat rasio kesuksesan di atas 80%); orbit ES-L1, GEO, HEO, dan SSO memiliki tingkat kesuksesan 100%, sedangkan orbit GTO mencatat tingkat kesuksesan terendah (~52%) akibat kecepatan re-entry yang sangat tinggi; tren kesuksesan tahunan meningkat pesat dari 0% pada 2010 menjadi lebih dari 80% pada 2020.

### 3. Analitik Visual Interaktif (Folium dan Plotly Dash)
- **Peta Geospasial Folium:** Menandai pangkalan peluncuran dengan lingkaran zona keamanan 1.000 meter dan mengelompokkan catatan peluncuran dengan plugin `MarkerCluster` hijau/merah. Menghitung jarak geodetik formula Haversine dari pangkalan CCAFS SLC-40 ke garis pantai (0,90 km), jalan raya (0,58 km), jalur rel kereta api (1,28 km), dan pusat kota Titusville (23,19 km).
- **Dasbor Web Plotly Dash (`spacex_dash_app.py`):** Pangkalan KSC LC-39A memimpin dengan jumlah sukses terbanyak (10 pendaratan) dan rasio keberhasilan tertinggi (76,92%); rentang muatan paling andal berada pada 2.000 kg hingga 4.000 kg (keberhasilan 72,7%); rentang muatan paling rawan berada pada 6.000 kg hingga 8.000 kg (keberhasilan 0%); Booster Block 5 mencatat keandalan pendaratan sempurna 100%.

### 4. Pemodelan Prediktif Klasifikasi Machine Learning
- **Pipeline dan Optimasi:** Menstandardisasi matriks 80 fitur numerik dengan `StandardScaler` ($z = \frac{x - \mu}{\sigma}$); mempartisi data latih dan uji secara independen rasio 80:20 (72 sampel latih, 18 sampel uji); menerapkan validasi silang 10-lipatan (`cv=10`) dan `GridSearchCV` untuk menyetel hiperparameter optimal pada 4 algoritma klasifikasi.
- **Hasil Evaluasi dan Matriks Konfusi:** Keempat model (Logistic Regression, Support Vector Machine dengan kernel sigmoid, Decision Tree, dan K-Nearest Neighbors) mencapai akurasi data uji yang identik sebesar 83,33% (15 prediksi benar dari 18 sampel uji). Matriks konfusi mencatat 12 True Positives, 3 True Negatives, 3 False Positives, dan 0 False Negatives. Logistic Regression direkomendasikan untuk implementasi produksi karena efisiensi komputasi dan kalibrasi probabilitas yang halus.

### 5. Laporan Presentasi dan Wawasan Bisnis Strategis
- **Salindia Portofolio Resmi:** Menyusun 18 slide presentasi eksekutif (`Data Science Capstone Project Report.pdf` dan `.pptx`) yang secara spesifik memuat tautan langsung ke setiap notebook komputasi, rincian hasil SQL, koordinat Folium, jawaban analitik Dash, serta diagram matriks konfusi.
- **Wawasan Inovatif Bisnis:** Ketiadaan False Negative ($FN = 0$) memastikan armada pemulihan kapal nirawak di laut selalu disiagakan ketika pendorong berhasil mendarat. Sebaliknya, kesalahan False Positive ($FP = 3$) menimbulkan kerugian finansial sekitar 200.000 hingga 500.000 dolar AS per misi untuk pengerahan kapal laut tanpa roket yang dapat dipulihkan. Penggunaan teknik penyeimbangan kelas seperti SMOTE direkomendasikan untuk pengembangan lanjutan.

---

## Bagian 3: Key Takeaways

- **Kelayakan Komersial Prediksi Machine Learning:** Pembelajaran mesin mampu memprediksi keberhasilan pemulihan pendorong Falcon 9 dengan akurasi 83,33%, memungkinkan kompetitor kedirgantaraan memperkirakan struktur biaya marginal SpaceX secara akurat.
- **Korelasi Muatan dan Orbit:** Misi muatan menengah (2.000 hingga 4.000 kg) menuju orbit LEO/SSO memiliki probabilitas sukses pendaratan tinggi (>72%), sedangkan misi muatan berat di atas 6.000 kg menuju orbit GTO memiliki risiko kehilangan pendorong yang tinggi sehingga penawaran harga harus memperhitungkan biaya roket sekali pakai.
- **Kesiapan dan Reproduktifitas Penuh:** Seluruh artefak kode komputasi, basis data, dasbor interaktif, serta berkas presentasi PDF/PPTX tersimpan secara rapi dan siap diverifikasi secara publik.
