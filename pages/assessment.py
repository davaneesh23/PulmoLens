
import streamlit as st
from utils.prediction import predict_respiratory_probability

st.title("Respiratory Health Assessment")
st.caption("NHANES Research Record Evaluation")

st.info(
    "Enter a research record using the same coding "
    "and feature definitions used during model training. "
    "This tool is for research demonstration only."
)

with st.form("assessment_form"):

    st.subheader("1. Participant information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age (years)",
            min_value=20,
            max_value=80,
            value=45
        )

        gender = st.selectbox(
            "NHANES gender code",
            options=[1.0, 2.0],
            format_func=lambda x: (
                "1 – Male" if x == 1.0 else "2 – Female"
            )
        )

    with col2:
        race = st.selectbox(
            "NHANES race/ethnicity code",
            options=[1.0, 2.0, 3.0, 4.0, 5.0]
        )

        education = st.selectbox(
            "Education code",
            options=[1.0, 2.0, 3.0, 4.0, 5.0]
        )

    marital = st.selectbox(
        "Marital status code",
        options=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    )

    st.divider()
    st.subheader("2. Socioeconomic and survey information")

    income_ratio = st.number_input(
        "Income-to-poverty ratio (INDFMPIR)",
        min_value=0.0,
        max_value=5.0,
        value=2.5,
        step=0.1
    )

    cycle = st.selectbox(
        "NHANES survey cycle",
        options=["E", "F", "G"],
        format_func=lambda x: {
            "E": "2007–2008",
            "F": "2009–2010",
            "G": "2011–2012"
        }[x]
    )

    smoking = st.selectbox(
        "Smoking status",
        options=["Never", "Former", "Current", "Unknown"]
    )

    st.divider()

    submitted = st.form_submit_button(
        "Generate Research Prediction",
        use_container_width=True
    )

if submitted:

    input_data = {
        "RIDAGEYR": age,
        "RIAGENDR": gender,
        "RIDRETH1": race,
        "DMDEDUC2": education,
        "DMDMARTL": marital,
        "INDFMPIR": income_ratio,
        "CYCLE": cycle,
        "SMOKING_STATUS": smoking
    }

    try:
        probability = predict_respiratory_probability(
            input_data
        )

        st.divider()
        st.subheader("Model Output")

        st.metric(
            "Calibrated probability",
            f"{probability * 100:.2f}%"
        )

        st.progress(probability)

        st.caption(
            "This is a model-estimated probability for the "
            "self-reported respiratory outcome defined in "
            "the research dataset. It is not a diagnosis or "
            "a clinically validated individual risk estimate."
        )

        with st.expander("View submitted research record"):
            st.json(input_data)

    except Exception as e:
        st.error(f"Prediction error: {e}")
