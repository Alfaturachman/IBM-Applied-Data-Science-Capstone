# Module 01: Introduction and Data Collection

Dokumen ini memuat panduan navigasi dan rangkuman komprehensif untuk Modul 01: Introduction and Data Collection pada kursus Applied Data Science Capstone. Modul pembuka ini menetapkan landasan proyek sains data menyeluruh untuk memprediksi keberhasilan pendaratan tahap pertama (*first stage booster*) roket Falcon 9 milik SpaceX guna mengestimasi efisiensi biaya peluncuran komersial. Pembahasan mencakup arsitektur teknis roket Falcon 9, skenario bisnis industri antariksa, pengumpulan data primer melalui *SpaceX REST API* dan teknik ekstraksi web (*Web Scraping* menggunakan *BeautifulSoup*), serta pra-pemrosesan awal (*Data Wrangling*) untuk menghasilkan dataset terstruktur dataset_part_2.csv.

---

## 1. Ikhtisar Modul dan Skenario Proyek Antariksa

### A. Konteks Bisnis dan Keunggulan Kompetitif SpaceX
- **Disrupsi Ekonomi Peluncuran Luar Angkasa:**
  - SpaceX mematok tarif peluncuran roket Falcon 9 sebesar 62 juta dolar AS per misi, jauh lebih murah dibandingkan tarif peluncuran roket konvensional kompetitor yang mencapai 165 juta dolar AS hingga lebih dari 200 juta dolar AS.
  - Penghematan signifikan ini tercapai berkat inovasi teknologi pemulihan dan penggunaan ulang tahap pertama (*first stage booster*), yang merupakan komponen fisik termahal pada sistem peluncuran antariksa.
- **Tujuan Analitis Data Scientist:**
  - Mengembangkan model pembelajaran mesin (*machine learning*) yang mampu memprediksi apakah tahap pertama roket Falcon 9 akan mendarat dengan selamat (*Class = 1*) atau tidak (*Class = 0*).
  - Prediksi probabilitas keberhasilan pendaratan ini dimanfaatkan oleh perusahaan peluncuran pesaing untuk menghitung struktur biaya penawaran lelang peluncuran satelit komersial secara kompetitif.

### B. Arsitektur Teknis Roket Falcon 9
- **Pelindung Muatan (Payload Fairing):** Cangkang pelindung satelit di puncak roket saat menembus atmosfer bawah bumi.
- **Tahap Kedua (Second Stage):** Ditenagai satu mesin *Merlin Vacuum* (MVac) untuk mendorong muatan ke orbit tujuan, beroperasi sekali pakai (*expendable*).
- **Tahap Pertama (First Stage / Booster):** Ditenagai sembilan mesin *Merlin 1D* dengan sirip kisi kendali (*grid fins*) dan kaki pendaratan hidrolik (*landing legs*). Tahap ini dirancang untuk mendarat kembali ke landasan darat (*Return to Launch Site* / RTLS) atau kapal nirawak (*Autonomous Spaceport Drone Ship* / ASDS).

---

## 2. Struktur Materi dan Kurikulum Modul

### A. Catatan Pembelajaran Konseptual (Study Notes)
- **01 Project Scenario.md**: Membahas latar belakang komersialisasi antariksa, arsitektur roket Falcon 9, variabilitas pendaratan booster, serta alur kerja metodologi sains data menyeluruh.
- **02 Data Collection.md**: Menguraikan metodologi pengumpulan data peluncuran melalui SpaceX REST API v4 dan ekstraksi halaman web Wikipedia menggunakan teknik *HTML parsing*.
- **03 Data Wrangling.md**: Mengkaji tahapan pra-pemrosesan data, eksplorasi sebaran pangkalan peluncuran, penanganan nilai hilang pada bobot kargo via imputasi rata-rata, dan pembentukan label target biner (*Class*).

### B. Evaluasi dan Tantangan Modul (Quizzes)
- **Quiz 01.md**: Evaluasi pemahaman awal terkait pemanggilan REST API, metode HTTP GET, fungsi `json_normalize()`, dan penguraian tabel HTML Wikipedia.
- **Quiz 02.md**: Evaluasi pemahaman rekayasa data, filter baris Falcon 9, imputasi nilai hilang, dan kalkulasi distribusi keberhasilan pendaratan.

---

## 3. Rangkuman Pembelajaran dan Metodologi Lab Praktikum

### A. Lab 01: Pengumpulan Data via SpaceX REST API
- **Folder Lab:** `Lab 01 - Data Collection API`
- **Dokumentasi Terperinci:** `Data Collection API.md`
- **Metodologi dan Temuan Utama:**
  - Mengirimkan permintaan HTTP GET ke *endpoint* `/launches/past` dan mengurai data bersarang (*nested JSON*) ke format tabular dua dimensi menggunakan *Pandas*.
  - Melakukan pemanggilan API berantai (*chained API calls*) untuk menerjemahkan data identitas sekunder: nama roket (`/rockets`), fasilitas pangkalan (`/launchpads`), bobot muatan (`/payloads`), dan modul booster (`/cores`).
  - Menyaring baris data roket khusus Falcon 9 (mengabaikan Falcon 1 awal) dan melakukan imputasi *mean* pada kolom bobot muatan (`PayloadMass`).
  - Menghasilkan berkas luaran `dataset_part_1.csv` berdimensi (90 baris, 17 kolom).

### B. Lab 02: Pengumpulan Data via Web Scraping
- **Folder Lab:** `Lab 02 - Data Collection with Web Scraping`
- **Dokumentasi Terperinci:** `Data Collection with Web Scraping.md`
- **Metodologi dan Temuan Utama:**
  - Mengunduh dokumen HTML halaman Wikipedia *"List of Falcon 9 and Falcon Heavy launches"* menggunakan pustaka *Requests*.
  - Mengurai struktur pohon *Document Object Model* (DOM) menggunakan *BeautifulSoup* dan menyaring tabel HTML berkelas target `wikitable`.
  - Mengekstrak data penerbangan dari baris `<tr>` dan sel `<td>`, membersihkan catatan kaki referensi (seperti `[1]`), dan menstandarisasi kolom ke kamus Python.
  - Menghasilkan berkas luaran `spacex_web_scraped.csv` berdimensi (121 baris, 11 kolom).

### C. Lab 03: Pembersihan dan Rekayasa Awal Data (Data Wrangling)
- **Folder Lab:** `Lab 03 - Data Wrangling`
- **Dokumentasi Terperinci:** `Data Wrangling.md`
- **Metodologi dan Temuan Utama:**
  - Menganalisis sebaran amatan pada setiap pangkalan peluncuran: Cape Canaveral `CCAFS SLC-40` (55 misi), Kennedy Space Center `KSC LC-39A` (22 misi), dan Vandenberg `VAFB SLC-4E` (13 misi).
  - Mengidentifikasi 8 klasifikasi luaran pendaratan (*Landing Outcomes*) dan memetakannya ke dalam label biner klasifikasi:
    - Nilai `1` (Pendaratan Sukses): mencakup hasil `True Ocean`, `True RTLS`, dan `True ASDS` (total 60 peluncuran atau 66,7%).
    - Nilai `0` (Pendaratan Gagal): mencakup hasil `False Ocean`, `False RTLS`, `False ASDS`, `None ASDS`, dan `None None` (total 30 peluncuran atau 33,3%).
  - Menghasilkan berkas dataset bersih `dataset_part_2.csv` berdimensi (90 baris, 18 kolom) yang siap digunakan pada Modul 2.

---

## 4. Key Takeaways dan Implikasi Terhadap Pipeline Capstone

### A. Fondasi Integritas Data
- **Kualitas Masukan Menentukan Kualitas Model (Garbage In, Garbage Out):**
  - Pembersihan menyeluruh pada Modul 1 menjamin tidak ada nilai kosong yang tertinggal pada variabel prediktor kuantitatif utama (`PayloadMass`) dan label target biner (`Class`) telah terstandarisasi dengan benar.
- **Konsistensi Skema Dataset:**
  - Standardisasi skema data Falcon 9 memastikan seluruh baris mewakili unit amatan yang homogen dan relevan dengan pertanyaan bisnis utama proyek.

### B. Kesiapan Menuju Tahapan Eksplorasi (Modul 2)
- Dataset `dataset_part_2.csv` menjadi input langsung untuk Modul 02 (*Exploratory Data Analysis*), di mana data akan diinvestigasi lebih lanjut melalui kueri basis data SQL serta visualisasi statistik untuk mengungkap korelasi multivariat.
