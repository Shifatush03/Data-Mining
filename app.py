import streamlit as st
import pandas as pd
from catboost import CatBoostClassifier

# Load CatBoost Model
model = CatBoostClassifier()
model.load_model("catboost_model.cbm")

# Fungsi untuk prediksi
def predict_mental_health(input_data):
    # Konversi input menjadi DataFrame
    input_df = pd.DataFrame([input_data])
    # Prediksi menggunakan model CatBoost
    prediction = model.predict(input_df)
    return int(prediction[0])  # Pastikan hasil dalam bentuk integer

# Header aplikasi
st.title("Mental Health Prediction App")
st.write("Masukkan data untuk memprediksi kesehatan mental berdasarkan fitur berikut.")

# Input pengguna
Sadness = st.number_input("Sadness (0-3)", min_value=0, max_value=3, step=1)
Euphoric = st.number_input("Euphoric (0-3)", min_value=0, max_value=3, step=1)
Exhausted = st.number_input("Exhausted (0-3)", min_value=0, max_value=3, step=1)
Sleep_dissorder = st.number_input("Sleep Dissorder (0-3)", min_value=0, max_value=3, step=1)
Mood_Swing = st.number_input("Mood Swing (0-3)", min_value=0, max_value=3, step=1)
Suicidal_thoughts = st.number_input("Suicidal Thoughts (0-3)", min_value=0, max_value=3, step=1)
Anorxia = st.number_input("Anorxia (0-3)", min_value=0, max_value=3, step=1)
Authority_Respect = st.number_input("Authority Respect (0-3)", min_value=0, max_value=3, step=1)
Try_Explanation = st.number_input("Try Explanation (0-3)", min_value=0, max_value=3, step=1)
Aggressive_Response = st.number_input("Aggressive Response (0-3)", min_value=0, max_value=3, step=1)
Ignore_Move_On = st.number_input("Ignore & Move-On (0-3)", min_value=0, max_value=3, step=1)
Nervous_Break_down = st.number_input("Nervous Break-down (0-3)", min_value=0, max_value=3, step=1)
Admit_Mistakes = st.number_input("Admit Mistakes (0-3)", min_value=0, max_value=3, step=1)
Overthinking = st.number_input("Overthinking (0-3)", min_value=0, max_value=3, step=1)
Sexual_Activity = st.selectbox("Sexual Activity", ["Low", "Moderate", "High"])
Concentration = st.selectbox("Concentration", ["Low", "Moderate", "High"])
Optimisim = st.selectbox("Optimisim", ["Low", "Moderate", "High"])

# Map categorical inputs to numerical values
categorical_mapping = {"Low": 0, "Moderate": 1, "High": 2}
Sexual_Activity = categorical_mapping[Sexual_Activity]
Concentration = categorical_mapping[Concentration]
Optimisim = categorical_mapping[Optimisim]

# Tombol prediksi
if st.button("Predict"):
    # Data input
    input_data = {
        "Sadness": Sadness,
        "Euphoric": Euphoric,
        "Exhausted": Exhausted,
        "Sleep_dissorder": Sleep_dissorder,
        "Mood_Swing": Mood_Swing,
        "Suicidal_thoughts": Suicidal_thoughts,
        "Anorxia": Anorxia,
        "Authority_Respect": Authority_Respect,
        "Try-Explanation": Try_Explanation,
        "Aggressive_Response": Aggressive_Response,
        "Ignore_&_Move-On": Ignore_Move_On,
        "Nervous_Break-down": Nervous_Break_down,
        "Admit_Mistakes": Admit_Mistakes,
        "Overthinking": Overthinking,
        "Sexual_Activity": Sexual_Activity,
        "Concentration": Concentration,
        "Optimisim": Optimisim,
    }

    # Label diagnosis
    diagnosis_labels = ['Normal', 'Depression', 'Bipolar Type-1', 'Bipolar Type-2']

    # Prediksi
    prediction = predict_mental_health(input_data)
    predicted_diagnosis = diagnosis_labels[prediction]  # Mapping hasil prediksi ke label

    # Tampilkan hasil
    st.success(f"Hasil Diagnosis (Expert Diagnose): {predicted_diagnosis}")
