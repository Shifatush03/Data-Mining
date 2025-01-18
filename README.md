# Prediksi Kesehatan Mental Berdasarkan Gaya Hidup

**SHIFATUSH SHAFWAH**

**NIM**: A11.2022.14078
        
 **Mata Kuliah** : DATA MINING [A11.4517]

STREAMLIT : [Prediksi Kesehatan Mental] (https://prediksi-mental-health-25.streamlit.app/)

DESKRIPSI PROYEK : 
Proyek ini bertujuan untuk mendeteksi prediksi kesehatan mental berdasarkan gaya hidup menggunakan model catboost. Proyek ini mencakup tahapan prepoccesing, oversampling, training model, dan deployment menggunakan **STREAMLIT** 

---

## **Tujuan Proyek**
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
- Hasil akhir : Model mencapai akurasi sebesar 96% pada data validasi.
  
![Screenshot 2025-01-17 231805](https://github.com/user-attachments/assets/137cd31c-5400-4850-93d0-13fa335fcc4f)
![confusionmatrixCatBoost](https://github.com/user-attachments/assets/da5d76cb-c189-445f-aab8-35ed65c2be66)

---

**Model atau Alur Penyelesaian (Bagan)**
![bagan1](https://github.com/user-attachments/assets/ac29a5b1-080a-49d9-842e-840ed41c9c29)


---
**PERFORMA MODEL**
Performa Model yang digunakan adalah CatBoost, yang dipilih karena performanya yang tinggi untuk data kategori. Evaluasi model dilakukan dengan menggunakan beberapa metrik, yaitu:
 - Akurasi: 96%
 - Precision: 97%
 - Recall: 96%
 - F1-Score: 96%

   ---
   
 # Diskusi Hasil dan Kesimpulan
- Model CatBoost menunjukkan performa yang sangat baik, dengan akurasi sebesar 96%. Hal ini menunjukkan bahwa model dapat mengklasifikasikan status kesehatan mental individu berdasarkan gaya hidup dengan tingkat keandalan yang tinggi.
- Teknik oversampling berhasil mengatasi masalah ketidakseimbangan data, yang terlihat dari peningkatan metrik seperti precision dan recall.
- Evaluasi melalui confusion matrix menunjukkan bahwa jumlah kesalahan prediksi pada kelas minoritas relatif rendah, membuktikan efektivitas preprocessing data.
- Model dapat lebih ditingkatkan dengan eksplorasi parameter tuning atau penggunaan ensemble model lainnya.

# Kesimpulan:
 - Proyek ini berhasil mencapai tujuan utamanya, yaitu memprediksi status kesehatan mental berdasarkan gaya hidup dengan menggunakan model CatBoost.
 - Model dapat digunakan sebagai alat bantu dalam mendeteksi risiko gangguan kesehatan mental, yang dapat memberikan insight awal bagi individu atau tenaga kesehatan.
 - Implementasi Streamlit memungkinkan akses yang mudah bagi pengguna akhir untuk memanfaatkan model ini dalam pengambilan keputusan.

# Saran:
 - Untuk pengembangan lebih lanjut, dataset yang lebih besar dan lebih beragam dapat digunakan untuk meningkatkan generalisasi model.
 - Penambahan fitur lain seperti riwayat kesehatan keluarga atau data genetik dapat meningkatkan akurasi prediksi.

   

