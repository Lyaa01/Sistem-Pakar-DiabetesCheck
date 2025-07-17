# Sistem-Pakar-DiabetesCheck
DiabetesCheck merupakan sistem pakar berbasis website yang dibangun menggunakan python dan streamlit untuk deteksi awal diabetes. Aplikasi ini merupakan sistem pakar berbasis aturan (rule-based expert system). Sistem ini dirancang untuk membantu mendeteksi risiko diabetes berdasarkan input data seperti kadar glukosa, usia, indeks massa tubuh (BMI), dan kadar insulin.

## 📋 Fitur

- Input nilai:
  - Glukosa
  - Usia
  - BMI (Indeks Massa Tubuh)
  - Insulin
- Analisis risiko berdasarkan logika aturan (rule-based)
- Output berupa tingkat risiko:
  - ✅ Risiko rendah
  - ⚠️ Risiko sedang
  - ⚠️ Risiko tinggi
  - 🚨 Risiko sangat tinggi
  - ℹ️ Data tidak cukup untuk diagnosis pasti

## ⚙️ Cara Menjalankan Aplikasi

1. Pastikan Python telah terinstall di komputer Anda.
2. Install Streamlit jika belum:
   ```bash
   pip install streamlit

3. Simpan kode aplikasi ke file, misalnya diabetes.py.

4. Jalankan aplikasi dengan perintah:
   ```bash
   streamlit run diabet.py

5. Aplikasi akan terbuka di browser secara otomatis.

## 🎯 Tujuan Pengembangan
Sistem ini dikembangkan untuk:
Membantu pengguna dalam mendeteksi dini risiko diabetes
Menjadi alat bantu bagi rumah sakit atau klinik dalam proses skrining awal
Memberikan edukasi kepada masyarakat mengenai pentingnya memantau kadar glukosa, BMI, dan insulin
