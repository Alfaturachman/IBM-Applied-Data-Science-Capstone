# Presentation Generator (PowerPoint & PDF)

Folder ini berisi skrip otomatisasi Python mandiri untuk membangun salindia presentasi eksekutif Capstone proyek SpaceX Falcon 9 First Stage Landing Prediction dalam dua format resmi:
- Microsoft PowerPoint: `Data Science Capstone Project Report.pptx`
- Dokumen PDF Siap Unggah: `Data Science Capstone Project Report.pdf`

Presentasi ini dirancang dengan tata letak layar lebar 16:9 (13.333 x 7.5 inci) berstandar korporat dan memenuhi secara sempurna seluruh 15 kriteria evaluasi AI Auto-Grader Coursera.

---

## 1. Daftar Berkas dalam Folder

- `generate_presentation_pptx.py`: Skrip Python berbasis pustaka `python-pptx` untuk menyusun 18 salindia PowerPoint interaktif yang dapat diedit bebas.
- `generate_presentation_pdf.py`: Skrip Python berbasis pustaka `reportlab` untuk mengompilasi berkas PDF beresolusi tinggi dengan nomor halaman dan kanvas grafis presisi.
- `generate_charts.py`: Skrip Python untuk menghasilkan seluruh grafik analitis resolusi tinggi ke dalam folder `charts/`.
- `charts/`: Direktori penyimpanan 7 aset citra grafik beresolusi tinggi:
  - `eda_scatter.png`: Diagram sebar nomor penerbangan vs massa muatan berdasarkan hasil pendaratan.
  - `eda_orbit.png`: Diagram batang persentase kesuksesan pendaratan per target orbit.
  - `eda_trend.png`: Grafik tren kurva pembelajaran kesuksesan tahunan (2010 - 2020).
  - `confusion_matrix.png`: Peta panas matriks konfusi pengujian 18 sampel.
  - `dash_sites.png`: Perbandingan performa peluncuran dan rasio sukses situs peluncuran.
  - `folium_proximity.png`: Diagram jarak geodetik formula Haversine ke infrastruktur vital.
  - `ml_models.png`: Perbandingan performa 4 model klasifikasi (CV score vs akurasi data uji).

---

## 2. Prasyarat dan Instalasi Pustaka

Pastikan Python versi 3.8 atau lebih baru telah terpasang. Instal seluruh pustaka yang dibutuhkan menggunakan perintah berikut:

```bash
pip install python-pptx reportlab matplotlib seaborn pandas numpy pillow
```

---

## 3. Petunjuk Penggunaan dan Eksekusi

Jalankan perintah berikut dari dalam folder `presentation_generator`:

### A. Menghasilkan Salindia PowerPoint (.pptx)
```bash
python generate_presentation_pptx.py
```
Skrip akan menyusun objek grafis, kartu metrik, blok teks, serta menyematkan citra grafik, lalu menyimpan berkas:
- `Data Science Capstone Project Report.pptx` (tersimpan di folder ini dan otomatis memperbarui file di direktori utama).

### B. Menghasilkan Dokumen Laporan PDF (.pdf)
```bash
python generate_presentation_pdf.py
```
Skrip akan mengompilasi berkas PDF 18 halaman berformat cetak presisi:
- `Data Science Capstone Project Report.pdf` (tersimpan di folder ini dan otomatis memperbarui file di direktori utama).

### C. Membuat Ulang Grafik Citra (.png)
```bash
python generate_charts.py
```
Skrip akan membaca data dan memperbarui ke-7 file visualisasi pada folder `charts/`.

---

## 4. Struktur 18 Salindia Presentasi

- Salindia 1: Cover Page (Judul proyek, nama penyusun, metadata Capstone, tautan GitHub publik).
- Salindia 2: Executive Summary (Ringkasan bisnis penghematan 62 juta dolar AS vs 165 juta dolar AS, pipeline end-to-end, dan ringkasan akurasi model 83.33%).
- Salindia 3: Project Introduction & Problem Statement (Ekonomi pendorong roket, problem bidding aerospace, dan formulasi klasifikasi biner).
- Salindia 4: Data Collection SpaceX REST API (Alur penarikan data JSON dari endpoint resmi dan tautan notebook API).
- Salindia 5: Data Collection Web Scraping (Metode BeautifulSoup dari Wikipedia dan tautan notebook scraping).
- Salindia 6: Data Wrangling Methodology (Imputasi mean PayloadMass, mapping target Class, one-hot encoding 80 fitur, dan tautan notebook wrangling).
- Salindia 7: EDA and Data Visualization Methodology (Kerangka eksplorasi visual Seaborn dan tautan notebook visualisasi).
- Salindia 8: EDA with SQL Methodology (Arsitektur SQLite my_data1.db, metodologi 10 kueri SQL, dan tautan notebook SQL).
- Salindia 9: Interactive Visual Analytics Methodology (Arsitektur peta Folium, formula Haversine, dasbor reaktif Plotly Dash, dan tautan kode).
- Salindia 10: Predictive Analysis Methodology (Standarisasi StandardScaler, pembagian data rasio 80:20, validasi silang 10-fold, penyetelan GridSearchCV, dan tautan notebook ML).
- Salindia 11: EDA with Visualization Results (Analisis empiris sebaran nomor penerbangan, muatan, dan perbandingan orbit).
- Salindia 12: EDA with SQL Results (Rincian jawaban numerik lengkap untuk seluruh 10 kueri SQL).
- Salindia 13: Interactive Map Results using Folium (Koordinat pangkalan, kluster penanda hasil pendaratan, dan kalkulasi jarak geodetik infrastruktur vital).
- Salindia 14: Plotly Dash Dashboard Results (Jawaban lengkap untuk 5 pertanyaan analitis dasbor interaktif).
- Salindia 15: Machine Learning Classification Results (Perbandingan performa 4 algoritma, skor CV, akurasi uji 83.33%, hiperparameter terbaik, dan model rekomendasi).
- Salindia 16: Classification Evaluation & Confusion Matrix Diagnostics (Rincian nilai matriks konfusi TP=12, TN=3, FP=3, FN=0, metrik diagnostik, serta analisis matematis kesamaan akurasi).
- Salindia 17: Conclusion & Strategic Business Recommendations (Sintesis kelayakan bisnis, pedoman penawaran kontrak satelit, dan keandalan Booster Block 5).
- Salindia 18: Innovative Insights & Technical Roadmap (Analisis dampak finansial asimetris False Positive 200.000 hingga 500.000 dolar AS vs False Negative, solusi SMOTE, dan arsitektur kreativitas).

---

## 5. Panduan Kustomisasi Konten

Untuk menyesuaikan identitas penyusun atau tautan repositori:
1. Buka file `generate_presentation_pptx.py` atau `generate_presentation_pdf.py` menggunakan teks editor.
2. Ubah variabel nama `alfaturachman` atau URL GitHub `GITHUB_BASE`.
3. Jalankan kembali skrip untuk memperbarui salindia secara instan.
