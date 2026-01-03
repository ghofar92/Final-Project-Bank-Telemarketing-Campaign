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

- 📊 **Dashboard Tableau (Analisis Konversi)**  
  https://public.tableau.com/app/profile/ghofar.ismail8792/viz/BankMarketingCampaign_17638186946940/ConversionRate

---

## 🧠 Latar Belakang Bisnis

Dalam kampanye telemarketing, bank menghubungi banyak nasabah untuk
menawarkan produk deposito. Namun, tingkat konversi cenderung rendah
dan memakan banyak sumber daya.

Proyek ini bertujuan untuk:
- Mengidentifikasi nasabah dengan **potensi konversi tinggi**
- Membantu tim marketing memprioritaskan nasabah yang layak dihubungi
- Meningkatkan efisiensi dan efektivitas kampanye

---

## 🛠 Gambaran Solusi

Tahapan yang dilakukan dalam proyek ini meliputi:

1. Exploratory Data Analysis (EDA) untuk memahami perilaku nasabah
2. Feature engineering dan encoding data kategorikal
3. Penanganan data tidak seimbang menggunakan SMOTE
4. Pelatihan model machine learning (Random Forest)
5. Penyimpanan model ke dalam file `.pkl`
6. Deployment model menggunakan Streamlit
7. Visualisasi dan insight bisnis menggunakan Tableau

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

