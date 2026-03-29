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
    return joblib.load("model.pkl")  # make sure this matches your trained model name

model = load_model()

# ---------------- UI Header ----------------
st.title("🔐 Shadow Data Leak Detector")
st.markdown(
    "Analyze your **password strength & login behavior** to detect potential **data leak risks**."
)

st.divider()

# ---------------- User Inputs ----------------
st.subheader("🧾 Enter Security Details")

col1, col2 = st.columns(2)

with col1:
    password_length = st.slider("🔑 Password Length", 4, 30, 12)
    special_chars = st.slider("✨ Special Characters", 0, 10, 2)

with col2:
    reuse_count = st.slider("🔁 Password Reuse Count", 0, 10, 0)
    login_attempts = st.slider("🚨 Failed Login Attempts", 0, 20, 0)

st.divider()

# ---------------- Prediction ----------------
if st.button("🔍 Analyze Risk", use_container_width=True):

    input_data = np.array([[password_length, special_chars, reuse_count, login_attempts]])

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    risk_prob = probabilities[1] * 100
    confidence = max(probabilities) * 100

    st.subheader("📊 Risk Assessment")

    # ----------- Progress Bar -----------
    st.progress(int(risk_prob))

    st.metric(
        label="Estimated Data Leak Probability",
        value=f"{risk_prob:.2f}%"
    )

    st.caption(f"Model Confidence: {confidence:.2f}%")

    # ---------- Risk Classification ----------
    if risk_prob < 35:
        st.success("🟢 Low Risk")
        risk_level = "Low"
    elif risk_prob < 70:
        st.warning("🟠 Medium Risk")
        risk_level = "Medium"
    else:
        st.error("🔴 High Risk")
        risk_level = "High"

    # ---------------- Explainability ----------------
    st.divider()
    st.subheader("🧠 Why this result?")

    reasons = []
    improvements = []

    # Logic explanations
    if password_length < 10:
        reasons.append("🔑 Password is shorter than recommended")
        improvements.append("Use at least 12–16 characters")

    if special_chars < 2:
        reasons.append("✨ Not enough special characters")
        improvements.append("Include symbols like @, #, $, %")

    if reuse_count > 2:
        reasons.append("🔁 Password reused across multiple platforms")
        improvements.append("Use unique passwords for each account")

    if login_attempts > 5:
        reasons.append("🚨 High number of failed login attempts detected")
        improvements.append("Enable account lockout or 2FA")

    # Display reasons
    if reasons:
        st.write("⚠️ **Risk Factors Detected:**")
        for r in reasons:
            st.write(f"- {r}")
    else:
        st.success("✅ No major risk factors detected")

    # Display improvements
    if improvements:
        st.write("💡 **Recommended Actions:**")
        for tip in improvements:
            st.write(f"- {tip}")

    # ---------------- Summary Box ----------------
    st.divider()
    st.subheader("📌 Summary")

    st.info(
        f"Risk Level: **{risk_level}** | Probability: **{risk_prob:.2f}%** | Confidence: **{confidence:.2f}%**"
    )

# ---------------- Footer ----------------
st.divider()
st.caption("🚀 Built with Streamlit, Machine Learning & Explainable AI")