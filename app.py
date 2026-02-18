import streamlit as st
import numpy as np
import joblib

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Shadow Data Leak Detector",
    page_icon="🔐",
    layout="centered"
)

# ---------------- Load Model ----------------
@st.cache_resource
def load_model():
    return joblib.load("data_leak_model.pkl")

model = load_model()

# ---------------- UI ----------------
st.title("🔐 Shadow Data Leak Detector")
st.write("This application estimates the **risk of a potential data leak** based on password and login behavior.")

st.divider()

# ---------------- User Inputs ----------------
password_length = st.slider(
    "🔑 Password Length",
    min_value=4,
    max_value=30,
    value=12,
    help="Longer passwords generally reduce risk"
)

special_chars = st.slider(
    "✨ Number of Special Characters",
    min_value=0,
    max_value=10,
    value=2,
    help="Special characters increase password strength"
)

reuse_count = st.slider(
    "🔁 Password Reuse Count",
    min_value=0,
    max_value=10,
    value=0,
    help="Reusing passwords across platforms increases risk"
)

login_attempts = st.slider(
    "🚨 Failed Login Attempts",
    min_value=0,
    max_value=20,
    value=0,
    help="Multiple failed attempts may indicate attack activity"
)

st.divider()

# ---------------- Prediction ----------------
if st.button("🔍 Analyze Risk", use_container_width=True):

    input_data = np.array([[password_length, special_chars, reuse_count, login_attempts]])
    probability = model.predict_proba(input_data)[0][1] * 100

    st.subheader("📊 Risk Assessment")

    st.metric(
        label="Estimated Data Leak Probability",
        value=f"{probability:.2f} %"
    )

    # ---------- Risk Classification ----------
    if probability < 35:
        st.success("🟢 Low Risk")
        st.write("Your credentials appear secure with minimal exposure risk.")
    elif probability < 70:
        st.warning("🟠 Medium Risk")
        st.write("Some security improvements are recommended.")
    else:
        st.error("🔴 High Risk")
        st.write("Immediate action is advised to reduce potential data leakage.")

    st.divider()

    # ---------- Explainability ----------
    st.subheader("🧠 Why this result?")
    st.write(
        f"""
        - **Password Length:** {password_length}  
        - **Special Characters:** {special_chars}  
        - **Password Reuse Count:** {reuse_count}  
        - **Failed Login Attempts:** {login_attempts}  

        The machine learning model combines these factors to estimate overall risk.
        """
    )

# ---------------- Footer ----------------
st.caption("Built with Python, Streamlit & Machine Learning | Educational Project")
