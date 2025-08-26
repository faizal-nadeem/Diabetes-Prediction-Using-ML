import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🩺 Diabetes Prediction App (Demo)")

# ⚠️ Warning/Disclaimer
st.warning("⚠️ Disclaimer: This model is trained on a small dataset and is **NOT for real medical use**. "
           "It is created only for **practice and educational purposes** in healthcare-related machine learning.")

# Input fields
preg = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose Level", 0, 200, 100)
bp = st.number_input("Blood Pressure", 0, 150, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 1, 120, 30)

if st.button("Predict"):
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("High risk of Diabetes ❌ (Demo Prediction)")
    else:
        st.success("Low risk of Diabetes ✅ (Demo Prediction)")

# Small footer disclaimer
st.markdown(
    "<br><hr><p style='text-align: center; color: grey;'>⚠️ This application is for educational purposes only and should not be used for real medical decisions.</p>",
    unsafe_allow_html=True
)
