# Prediksi Kesehatan Mental Berdasarkan Gaya Hidup

**SHIFATUSH SHAFWAH**

**NIM**: A11.2022.14078
        
 **Mata Kuliah** : DATA MINING A11.4517

STREAMLIT : [Prediksi Kesehatan Mental] (https://prediksi-mental-health-25.streamlit.app/)

Tujuan PROYEK : 
Proyek ini bertujuan untuk mendeteksi prediksi kesehatan mental berdasarkan gaya hidup menggunakan model catboost. Proyek ini mencakup tahapan prepoccesing, oversampling, training model, dan deployment menggunakan **STREAMLIT** 

---

## **Deskripsi Proyek**
proyek ini bertujuan untuk mendeteksi prediksi kesehatan mental menggunakan dataset gaya hidup. Dataset telah melalui beberapa tahap :
1. Prepocessing untuk membersihkan data.
2. oversampling untuk menangani ketidakseimbangan data.
3. Training menggunakan algoritma CatBoost.
4. Deployment menggunakan Streamlit untuk kemudahan akses.

---

## **Struktur File**
Berikut adalah struktur file dalam repository dan penjelasannya :
1. **'Dataset-Mental-Disorders.csv'**
   Dataset utama yang digunakan untuk melatih model prediksi. Dataset ini berisi informasi gaya hidup dan kesehatan mental individu.
2. **'dataKasus-1.xlsx'**
   Dataset tambahan atau uji coba untuk validasi model.
3. **'Latihan.ipynb'**
   Notebook ini digunakan untuk tahapan eksperimen awal dalam memahami dataset, eksplorasi data, dan prepocessing.
4. **'mental.ipynb'**
   Notebook utama untuk training model CatBoost, evaluasi performa, dan anlisis hasil.
5. **'app.py'**
   File Phyton yang digunakan untuk membuat aplikasi web dengan **Streamlit**. File ini memuat logika deployment model.
6. **'catboost_model.cbm'**
   Model yang telah dilatih menggunakan algoritma CatBoost dan disimpan dalam format '.cbm'.
7. **'requirements.txt'**
   File yang berisi daftar library pyhton yang dibutuhkan oleh proyek ini, seperti :
   - pandas
   - numpy
   - streamlit
   - catboost
8. **'testing.ipynb'**
   Notebook yang digunakan untuk menguji performa model dengan data baru atau dataset validasi.

---

## **CARA MENJALANKAN PROYEK**
Berikut adalah langkah-langkah untuk menjalankan proyek :
1. Clone repository :
        '''bash
           git clone https://github.com/username/repository-name.git
2. INSTALL DEPENDENCIES :
        pip install -r requirements.txt
3. Jalankan Aplikasi Streamlit :
        streamlit run app.py
4. Akses aplikasi di browser melalui URL :
        http://localhost:8501

   ---

# PENJELASAN DATASET
Dataset-Mental-Disorders.csv :
- kolom-kolom penting :
- Lifestyle_Habits : kebiasaan gaya hidup (misalnya olahraga, pola makan).
- Stress_Level : Tingkat stres individu.
- Mental_Health_Status : Status kesehatah mental (Target prediksi, seperti sehat atau gangguan).
- Kolom lainnya berisi informasi tembahan seperti usia, jenis kelamin, dll.
Dataset diproses untuk memastikan kebersihan data sebelum digunakan dalam moodel.

---

# MODEL DAN EVALUASI 
- Model : CatBoost dipilih karena performanya yang tinggi untuk dataset kategori.
- Evaluasi : Model dilatih dan diuji menggunakan metrik seperti akurasi, precision, recall,dan F1-score.
- Hasil akhir : Model mencapai akurasi sebesar 90% pada data validasi.
   

