# dashboard/app.py
# Job Acceptance Prediction - Streamlit Dashboard

import streamlit as st
import pandas as pd
import pickle
import os

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Job Acceptance Predictor",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Job Acceptance Prediction System")
st.markdown("Predict whether a candidate will **accept or reject** a job offer")

# -------------------------------------------------
# Load Model & Features
# -------------------------------------------------
@st.cache_resource
def load_model_and_features():
    if not os.path.exists("models/best_model.pkl"):
        return None, None

    with open("models/best_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("models/model_features.pkl", "rb") as f:
        features = pickle.load(f)

    return model, features


model, feature_list = load_model_and_features()

# -------------------------------------------------
# Sidebar Inputs (IMPROVED)
# -------------------------------------------------
with st.sidebar:
    st.header("🧑 Candidate Profile")

    with st.expander("📚 Academic & Skills", expanded=True):
        skills_match = st.slider("Skills Match (%)", 0, 100, 80)
        academic_index = st.slider("Academic Index", 0, 100, 72)
        overall_assessment = st.slider("Overall Assessment", 0, 100, 75)

    with st.expander("🧪 Interview Performance", expanded=True):
        technical_score = st.slider("Technical Score", 0, 100, 75)
        aptitude_score = st.slider("Aptitude Score", 0, 100, 70)
        communication_score = st.slider("Communication Score", 0, 100, 70)

    with st.expander("💰 Compensation & Risk", expanded=True):
        ctc_gap_pct = st.slider("CTC Gap (%)", -50, 100, 20)
        risk_score = st.slider("Risk Score (0 = Low, 1 = High)", 0.0, 1.0, 0.3)

    st.markdown("---")
    predict_btn = st.button("🎯 Predict Job Acceptance", type="primary")

# -------------------------------------------------
# Prediction Logic
# -------------------------------------------------
if predict_btn:
    if model is None or feature_list is None:
        st.error("❌ Model not found. Please train the model first.")
    else:
        input_dict = {
            "technical_score": technical_score,
            "skills_match_percentage": skills_match,
            "aptitude_score": aptitude_score,
            "communication_score": communication_score,
            "academic_index": academic_index,
            "overall_assessment": overall_assessment,
            "ctc_gap_percentage": ctc_gap_pct,
            "risk_score": risk_score,
        }

        input_df = pd.DataFrame([input_dict])

        # Ensure feature alignment
        for col in feature_list:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[feature_list]

        # Prediction
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]

        # -------------------------------------------------
        # Display Results
        # -------------------------------------------------
        st.markdown("---")
        col1, col2, col3 = st.columns(3)

        with col1:
            if prediction == 1:
                st.success("✅ **WILL ACCEPT OFFER**")
            else:
                st.error("❌ **LIKELY TO REJECT**")

        with col2:
            st.metric("Acceptance Probability", f"{probability[1]*100:.1f}%")

        with col3:
            st.metric("Model Confidence", f"{max(probability)*100:.1f}%")

        st.markdown("### 📊 Probability Breakdown")
        st.progress(int(probability[1] * 100))
        st.write(f"✔ Accept: {probability[1]*100:.1f}%")
        st.write(f"✖ Reject: {probability[0]*100:.1f}%")

        # -------------------------------------------------
        # Recommendations
        # -------------------------------------------------
        st.markdown("### 💡 HR Recommendation")
        if prediction == 1:
            st.success("""
            **Low Dropout Risk Candidate**
            - Proceed with offer
            - Initiate onboarding
            - Strong acceptance confidence
            """)
        else:
            st.warning("""
            **High Dropout Risk Candidate**
            - Revisit compensation
            - Improve role alignment
            - Increase candidate engagement
            """)

# -------------------------------------------------
# Model Info
# -------------------------------------------------
with st.expander("ℹ️ Model Information"):
    st.write("""
    **Model Type:** Random Forest Classifier  
    **Problem Type:** Binary Classification  

    **Key Decision Factors:**
    - Skills match & interview performance
    - Academic strength
    - Compensation gap
    - Risk indicators
    """)

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.caption("Job Acceptance Prediction System | ML + HR Analytics")
