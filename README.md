# 📊 Bank Telemarketing Campaign – Prediksi Konversi Nasabah

Proyek ini merupakan **end-to-end machine learning project** untuk
memprediksi kemungkinan nasabah berlangganan produk **deposito berjangka**
berdasarkan data kampanye telemarketing bank.  
Solusi ini dilengkapi dengan **aplikasi Streamlit** untuk prediksi dan
**dashboard Tableau** untuk analisis bisnis.

---

## 🔗 Demo Aplikasi

- 🚀 **Aplikasi Streamlit (Prediksi Nasabah)**  
  https://final-project-bank-telemarketing-campaign-hjbtugbpsueu5yf6fzhf.streamlit.app/
  <img width="1886" height="849" alt="image" src="https://github.com/user-attachments/assets/58449fcb-5a8d-4b8b-86dd-8ca46965879b" />


- 📊 **Dashboard Tableau (Analisis Konversi)**  
  https://public.tableau.com/app/profile/ghofar.ismail8792/viz/BankMarketingCampaign_17638186946940/ConversionRate?publish=yes
  <img width="1811" height="816" alt="image" src="https://github.com/user-attachments/assets/2011cc9d-f540-47c1-9c1a-f35528d1bfab" />


---

## 🧠 Latar Belakang Bisnis

Model bisnis pemasaran deposito berjangka di Portugal sangat mengandalkan telemarketing sebagai kanal utama untuk menjangkau calon nasabah. Aktivitas ini membutuhkan sumber daya operasional yang besar mulai dari waktu agen, biaya telekomunikasi, hingga proses administratif dalam melakukan follow-up. Keberhasilan kampanye sangat ditentukan oleh kemampuan untuk memahami karakteristik nasabah yang cenderung merespons positif terhadap penawaran deposito.

Selain aspek operasional, kondisi ekonomi Portugal saat kampanye 2013–2014 turut memengaruhi perilaku nasabah terhadap produk deposito. Menurut Press Release Banco de Portugal, total simpanan sektor non-moneter mencapai €225,6 miliar, dan lebih dari 70% simpanan masyarakat berada dalam bentuk deposito berjangka atau tabungan. Dengan tingkat ketidakpastian ekonomi pascakrisis 2008–2010, bank-bank sangat bergantung pada deposito sebagai sumber pendanaan stabil. Karena itu, mereka menjalankan kampanye telemarketing intensif, seperti produk `Depósito a Prazo 12 Meses – Taxa Bónus Campanha Primavera 2014` yang memiliki fitur:

*	Bunga promo 3% untuk 12 bulan pertama (lebih tinggi dari rata-rata bunga deposito pada umumnya 1,3–2%) (https://www.theglobaleconomy.com/Portugal/deposit_interest_rate/#:~:text=The%20most%20recent%20value%20is,1%202%203%204%205)
*	Minimum setoran €5.000, maksimum sekitar €60.000 (dengan bunga deposito spesial selama 3 tahun).
*	Dijamin penuh oleh Fundo de Garantia de Depósitos?Lembaga Penjamin Simpanan Portugal (tanpa risiko).
*	Tanpa penalti bila tarik dana lebih awal.
*	Bonus ekstra untuk nasabah baru (voucher, bebas biaya admin).

Namun, meskipun produk menarik, tingkat konversi tetap rendah, dan terjadi ketidakseimbangan besar antara jumlah nasabah yang dihubungi dan yang benar-benar membuka deposito. Data historis menunjukkan bahwa tingkat konversi kampanye telemarketing cenderung rendah. Dari lebih dari 40 ribu percobaan kontak, hanya sekitar 11% nasabah yang akhirnya menyetujui penempatan deposito. Angka ini mengindikasikan adanya ketidakefisienan dalam strategi targeting, sehingga banyak panggilan tidak menghasilkan nilai tambah. Situasi ini memperlihatkan perlunya pendekatan analitis untuk memahami lebih dalam pola respons nasabah.

Hal ini menunjukkan adanya masalah dalam strategi targeting, tingginya biaya per kontak (Cost per Acquisition/CPA), dan ketidakefisienan dalam pemanfaatan data. Dengan volume data besar dan hubungan antar variabel yang kompleks (demografi, riwayat kontak, kondisi makro, dan channel komunikasi), pendekatan analitik yang sistematis menjadi kebutuhan untuk meningkatkan efektivitas kampanye dan menurunkan pemborosan operasional..

Proyek ini bertujuan untuk:
- Mengidentifikasi nasabah dengan **potensi konversi tinggi**
- Membantu tim marketing memprioritaskan nasabah yang layak dihubungi
- Meningkatkan efisiensi dan efektivitas kampanye

---
## 🧠 Problem Statement
Meskipun Bank Portugal menawarkan produk deposito dengan suku bunga kompetitif di tengah iklim ekonomi yang tidak pasti, realisasi konversi nasabah masih jauh dari target yang diharapkan. Strategi "spray and pray" dalam telemarketing—di mana agen menghubungi ribuan nasabah tanpa prioritas yang jelas—telah menyebabkan pembengkakan biaya operasional yang signifikan. Dengan rata-rata durasi panggilan yang memakan waktu (mean: ~258 detik) dan beberapa nasabah dihubungi berulang kali (hingga 56 kali dalam satu kampanye), sumber daya bank terkuras untuk melayani 88,7% nasabah yang pada akhirnya menolak penawaran. Ketidakefisienan ini bukan hanya membuang anggaran pemasaran, tetapi juga meningkatkan risiko brand fatigue di mata nasabah akibat kontak yang tidak relevan.

*Masalah Utama*

`Tingginya Cost per Acquisition (CPA) dan inefisiensi operasional telemarketing akibat ketidakmampuan bank dalam mengidentifikasi prospek berkualitas tinggi (High-Value Leads) sebelum panggilan dilakukan, yang mengakibatkan 89% upaya kontak menjadi beban biaya tanpa menghasilkan pendapatan (revenue).`

Untuk membedah masalah inefisiensi biaya dan targeting tersebut, masalah-masalah yang harus diselesaikan adalah :

1. *Analisis Cost vs. Duration:* Bagaimana hubungan antara durasi panggilan (duration) dengan keberhasilan konversi? Pada titik durasi berapakah sebuah panggilan mulai dianggap "membuang biaya" (diminishing return) jika tidak terjadi penutupan penjualan?
2. *Efektivitas Frekuensi Kontak:* Apakah meningkatkan jumlah panggilan (campaign) kepada nasabah yang sama benar-benar meningkatkan peluang konversi, atau justru hanya menambah biaya telekomunikasi dan operasional agen secara sia-sia?
3. *Profil Demografi Risiko Rendah:* Dari segi Job dan Education, segmen nasabah manakah (misal: retired vs blue-collar) yang memiliki conversion rate tertinggi sehingga layak diprioritaskan untuk mengurangi waktu prospeksi?
4. *Optimasi Waktu Kontak:* Pada bulan (month) dan hari apa (day_of_week) tingkat keberhasilan tertinggi tercatat? Apakah ada pola waktu tertentu di mana operasional telemarketing justru merugi?
5. Bagaimana kita dapat membangun model klasifikasi yang mampu memprediksi probabilitas seorang nasabah akan berlangganan deposito ("yes") berdasarkan fitur demografi dan riwayat kontaknya, sehingga tim marketing hanya perlu menghubungi 20-30% nasabah teratas namun tetap menangkap mayoritas potensi konversi?

## 🧠 Evaluation Metric

Sebagai tim Data Scientist, kami memprioritaskan pengurangan *False Negative (FN)* untuk memastikan bahwa tidak ada calon nasabah potensial yang terlewat oleh sistem prediksi. False Negative terjadi ketika model memprediksi seorang nasabah tidak akan menaruh uang di deposito, padahal sebenarnya mereka berminat. Kesalahan ini berdampak langsung pada hilangnya peluang pendapatan dan menurunkan tingkat konversi kampanye.

Untuk itu, metrik utama yang menjadi fokus adalah *Recall*, yaitu kemampuan model dalam menangkap seluruh nasabah yang benar-benar berminat. Recall yang tinggi menunjukkan bahwa model berhasil meminimalkan FN, sehingga lebih banyak calon nasabah bernilai tinggi dapat dihubungi oleh agen telemarketing. Pendekatan ini memastikan bahwa kampanye berjalan lebih efektif, peluang penjualan meningkat, dan potensi pendapatan tidak terbuang.

1. DESKRIPSI DATASET**

-	[Sumber dataset: UCI Machine Learning Repository (Sergio Moro, Paulo Cortez, Paulo Rita).](https://www.kaggle.com/datasets/volodymyrgavrysh/bank-marketing-campaigns-dataset)
-	Jumlah Baris: 41.188 
-	Jumlah Kolom: 20 
-	Periode: 2014
-	Tipe Problem: Binary classification —> target y (yes/no) apakah convert ke term deposit.

Note :
- Sebagian besar fitur bersifat numerikal.
- Terdapat inkonsistensi penulisan pada fitur kategorikal.
- Setiap baris data merepresentasikan informasi seorang pelanggan yang deposit atau tidak.

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| *age* | Numerik | Usia nasabah. |
| *job* | Kategorikal | Jenis pekerjaan nasabah (misal: admin, blue-collar, entrepreneur, dll). |
| *marital* | Kategorikal | Status pernikahan nasabah (married, single, divorced, unknown). |
| *education* | Kategorikal | Tingkat pendidikan nasabah. |
| *default* | Binary | Apakah nasabah memiliki kredit macet? (yes/no). |
| *housing* | Binary | Apakah nasabah memiliki cicilan rumah? (yes/no). |
| *loan* | Binary | Apakah nasabah memiliki pinjaman pribadi? (yes/no). |
| *contact* | Kategorikal | Jenis alat komunikasi yang digunakan (cellular/telephone). |
| *month* | Kategorikal | Bulan kontak terakhir dalam tahun (jan, feb, mar, ..., nov, dec). |
| *day_of_week* | Kategorikal | Hari kontak terakhir dalam seminggu (mon, tue, wed, thu, fri). |
| *duration* | Numerik | Durasi panggilan kontak terakhir dalam detik. |
| *campaign* | Numerik | Jumlah kontak yang dilakukan selama kampanye ini untuk nasabah tersebut. |
| *pdays* | Numerik | Jumlah hari yang berlalu setelah nasabah terakhir dihubungi dari kampanye sebelumnya (999 berarti belum pernah dihubungi). |
| *previous* | Numerik | Jumlah kontak yang dilakukan sebelum kampanye ini untuk nasabah tersebut. |
| *poutcome* | Kategorikal | Hasil dari kampanye pemasaran sebelumnya (failure, nonexistent, success). |
| *emp.var.rate* | Numerik | Employment Variation Rate - Indikator makroekonomi (variasi tingkat kerja kuartalan). |
| *cons.price.idx* | Numerik | Consumer Price Index - Indikator harga konsumen bulanan. |
| *cons.conf.idx* | Numerik | Consumer Confidence Index - Indikator kepercayaan konsumen bulanan. |
| *euribor3m* | Numerik | Euribor 3 month rate - Tingkat suku bunga harian. |
| *nr.employed* | Numerik | Number of employees - Indikator jumlah karyawan kuartalan. |
| *y* | Binary (Target) | Target variabel: apakah nasabah berlangganan deposito berjangka? (yes/no). |


## 🛠 Gambaran Solusi

Tahapan yang dilakukan dalam proyek ini meliputi:

1. Exploratory Data Analysis (EDA) untuk memahami perilaku nasabah
2. Feature engineering dan encoding data kategorikal
3. Penanganan data tidak seimbang menggunakan SMOTE
4. Pelatihan model machine learning (Random Forest)
5. Cost benefit calculation 
6. Penyimpanan model ke dalam file `.pkl`
7. Deployment model menggunakan Streamlit
8. Visualisasi dan insight bisnis menggunakan Tableau

---

## 🚀 Fitur Aplikasi Streamlit

Aplikasi Streamlit digunakan sebagai **alat prediksi operasional**.

### 🔹 Prediksi Satu Nasabah
- Input data sederhana (mode simulasi)
- Field lain diisi otomatis
- Menampilkan hasil prediksi dan probabilitas konversi (%)

### 🔹 Prediksi Massal (Bulk)
- Upload file CSV atau Excel
- Mendukung kolom nama nasabah dan nomor telepon
- Menghasilkan:
  - Hasil prediksi
  - Probabilitas konversi (%)
  - File hasil yang bisa diunduh

Fitur ini memungkinkan tim marketing **langsung mengetahui nasabah
mana yang berpotensi untuk dihubungi**.

---

## 📊 Dashboard Tableau

Dashboard Tableau digunakan untuk analisis strategis, antara lain:
- Tingkat konversi kampanye
- Analisis profil nasabah
- Pengaruh status pinjaman (loan & housing)
- Insight perilaku nasabah terhadap keberhasilan kampanye

Dashboard ini berfungsi sebagai **pendukung pengambilan keputusan bisnis**.

---

## ⚙️ Teknologi yang Digunakan

- **Python** (pandas, numpy)
- **Machine Learning**: scikit-learn, imbalanced-learn, category-encoders
- **Deployment**: Streamlit
- **Visualisasi Data**: Tableau Public
- **Model**: Random Forest Classifier

