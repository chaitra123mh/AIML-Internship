import streamlit as st
import requests


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="HealthBridge | AI Disease Prediction",
    page_icon="🏥",
    layout="wide"
)


# ==========================================================
# PROFESSIONAL UI STYLE
# ==========================================================

st.markdown(
    """
<style>

/* ---------- Main application ---------- */

.stApp {
    background: #f4f8fb;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ---------- Text ---------- */

h1, h2, h3 {
    color: #073b4c !important;
}

p, label {
    color: #173f56 !important;
}


/* ---------- Main title ---------- */

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #073b4c;
    margin-bottom: 5px;
}

.main-subtitle {
    text-align: center;
    font-size: 20px;
    font-weight: 600;
    color: #087f8c;
    margin-bottom: 25px;
}


/* ---------- Top divider ---------- */

.top-line {
    width: 90px;
    height: 5px;
    margin: 0 auto 25px auto;
    background: #087f8c;
    border-radius: 10px;
}


/* ---------- Disclaimer ---------- */

div[data-testid="stAlert"] {
    border-radius: 12px;
}


/* ---------- Section headers ---------- */

.section-title {
    color: #073b4c !important;
    font-size: 25px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 12px;
}


/* ---------- Cards ---------- */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border: 1px solid #d5e3ea !important;
    border-radius: 16px !important;
    box-shadow: 0 5px 18px rgba(7, 59, 76, 0.08);
}


/* ---------- Input labels ---------- */

.stNumberInput label,
.stSelectbox label,
.stCheckbox label {
    color: #173f56 !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}


/* ---------- Input values ---------- */

input {
    color: #102a43 !important;
    background: #ffffff !important;
    font-weight: 600 !important;
}

div[data-baseweb="input"] {
    background: #ffffff !important;
    border-radius: 9px !important;
    border: 1px solid #b8ccd8 !important;
}

div[data-baseweb="select"] {
    background: #ffffff !important;
    border-radius: 9px !important;
}


/* ---------- Checkboxes ---------- */

.stCheckbox label p {
    color: #173f56 !important;
    font-weight: 600 !important;
}


/* ---------- Prediction button ---------- */

.stButton > button {
    width: 100%;
    height: 58px;
    border-radius: 13px;
    border: none;

    background: #087f8c;

    color: white !important;

    font-size: 18px !important;
    font-weight: 800 !important;

    box-shadow: 0 7px 20px rgba(8, 127, 140, 0.25);
}

.stButton > button:hover {
    background: #065f69;
    color: white !important;
}


/* ---------- Metrics ---------- */

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #cfe1e7;
    border-radius: 16px;
    padding: 20px;

    box-shadow: 0 5px 18px rgba(7, 59, 76, 0.08);
}

[data-testid="stMetricLabel"] {
    color: #47798d !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #073b4c !important;
    font-weight: 800 !important;
}


/* ---------- SHAP positive ---------- */

.shap-positive {
    background: #eaf8f2;
    border-left: 5px solid #159570;
    border-radius: 10px;
    padding: 13px 16px;
    margin-bottom: 10px;
    color: #075e46 !important;
    font-weight: 700;
}


/* ---------- SHAP negative ---------- */

.shap-negative {
    background: #fff0ef;
    border-left: 5px solid #d64545;
    border-radius: 10px;
    padding: 13px 16px;
    margin-bottom: 10px;
    color: #8b2020 !important;
    font-weight: 700;
}


/* ---------- Footer ---------- */

.footer-text {
    text-align: center;
    color: #496b7a;
    font-size: 13px;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #d5e2e8;
}

</style>
""",
    unsafe_allow_html=True
)


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="main-title">🏥 HealthBridge</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">AI-Based Disease Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="top-line"></div>',
    unsafe_allow_html=True
)

st.info(
    "⚕️ AI Decision Support: This application provides "
    "AI-based decision support for educational and demonstration "
    "purposes. It is not a substitute for professional medical "
    "diagnosis or treatment."
)


# ==========================================================
# PATIENT INFORMATION
# ==========================================================

st.markdown(
    '<div class="section-title">👤 Patient Information</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=30
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            ["M", "F"]
        )


# ==========================================================
# SYMPTOMS
# ==========================================================

st.markdown(
    '<div class="section-title">🩺 Symptoms</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        fever = st.checkbox("Fever")
        cough = st.checkbox("Cough")
        fatigue = st.checkbox("Fatigue")
        breathlessness = st.checkbox("Breathlessness")

    with col2:

        chest_pain = st.checkbox("Chest Pain")
        nausea = st.checkbox("Nausea")
        headache = st.checkbox("Headache")


# ==========================================================
# HEALTH MEASUREMENTS
# ==========================================================

st.markdown(
    '<div class="section-title">📊 Health Measurements</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=60.0,
            value=22.0,
            step=0.1
        )

        bp_systolic = st.number_input(
            "Systolic Blood Pressure",
            min_value=70,
            max_value=250,
            value=120
        )

        bp_diastolic = st.number_input(
            "Diastolic Blood Pressure",
            min_value=40,
            max_value=150,
            value=80
        )

    with col2:

        spo2 = st.number_input(
            "SpO2 (%)",
            min_value=50,
            max_value=100,
            value=98
        )

        glucose = st.number_input(
            "Glucose (mg/dL)",
            min_value=40,
            max_value=500,
            value=100
        )

        hba1c = st.number_input(
            "HbA1c",
            min_value=3.0,
            max_value=20.0,
            value=5.5,
            step=0.1
        )


# ==========================================================
# AI PREDICTION
# ==========================================================

st.markdown(
    '<div class="section-title">🤖 AI Prediction</div>',
    unsafe_allow_html=True
)

if st.button(
    "🔍  Analyze Patient & Predict Disease",
    type="primary"
):

    input_data = {
        "Age": age,
        "Gender": gender,
        "Fever": int(fever),
        "Cough": int(cough),
        "Fatigue": int(fatigue),
        "Breathlessness": int(breathlessness),
        "Chest_Pain": int(chest_pain),
        "Nausea": int(nausea),
        "Headache": int(headache),
        "BMI": bmi,
        "BP_Systolic": bp_systolic,
        "BP_Diastolic": bp_diastolic,
        "SpO2": spo2,
        "Glucose_mg_dL": glucose,
        "HbA1c": hba1c
    }

    try:

        with st.spinner(
            "🧠 Analyzing patient information..."
        ):

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"features": input_data},
                timeout=10
            )

        if response.status_code == 200:

            result = response.json()

            st.success(
                "✅ Prediction completed successfully!"
            )

            # ==================================================
            # RESULT
            # ==================================================

            st.markdown(
                '<div class="section-title">🎯 Prediction Result</div>',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Predicted Disease",
                    result["predicted_disease"]
                )

            with col2:

                st.metric(
                    "Prediction Confidence",
                    result["confidence_percentage"]
                )

            st.warning(
                result["message"]
            )


            # ==================================================
            # SHAP EXPLANATION
            # ==================================================

            st.markdown(
                '<div class="section-title">🔎 Explainable AI — SHAP</div>',
                unsafe_allow_html=True
            )

            st.write(
                "Top features influencing this prediction:"
            )

            shap_data = result.get(
                "shap_explanation",
                []
            )

            if shap_data:

                for item in shap_data:

                    feature = item["feature"]
                    impact = item["impact"]

                    if impact >= 0:

                        st.markdown(
                            f'<div class="shap-positive">'
                            f'⬆️ {feature}: +{impact:.4f}'
                            f'</div>',
                            unsafe_allow_html=True
                        )

                    else:

                        st.markdown(
                            f'<div class="shap-negative">'
                            f'⬇️ {feature}: {impact:.4f}'
                            f'</div>',
                            unsafe_allow_html=True
                        )

            else:

                st.info(
                    "SHAP explanation is not available."
                )

        else:

            st.error(
                f"API Error: {response.text}"
            )

    except requests.exceptions.RequestException:

        st.error(
            "Unable to connect to the HealthBridge API. "
            "Please make sure the FastAPI server is running."
        )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    '<div class="footer-text">'
    '<b>🏥 HealthBridge</b><br>'
    'AI-Based Disease Prediction & Explainable AI System<br><br>'
    'Streamlit • FastAPI • Machine Learning • SHAP • MLflow'
    '</div>',
    unsafe_allow_html=True
)