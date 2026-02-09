import streamlit as st
import numpy as np
import joblib

# Load trained ML model
model = joblib.load("data_leak_model.pkl")

st.set_page_config(page_title="Shadow Data Leak Detector", layout="centered")

st.title("🔐 Shadow Data Leak Detector")
st.write("Predict the probability of a data leak using ML")

st.divider()

# ---- User Inputs ----
password_length = st.slider("Password Length", 4, 30, 8)
special_chars = st.slider("Number of Special Characters", 0, 10, 1)
reuse_count = st.slider("Password Reuse Count", 0, 10, 0)
login_attempts = st.slider("Failed Login Attempts", 0, 20, 0)

st.divider()

if st.button("🔍 Analyze Risk"):
    input_data = np.array([[password_length, special_chars, reuse_count, login_attempts]])
    probability = model.predict_proba(input_data)[0][1] * 100

    st.subheader("📊 Result")
    st.metric("Data Leak Probability", f"{probability:.2f} %")

    if probability < 40:
        st.success("Low Risk 🟢")
    elif probability < 70:
        st.warning("Medium Risk 🟠")
    else:
        st.error("High Risk 🔴")

st.caption("Built using Python, Streamlit & Machine Learning")
