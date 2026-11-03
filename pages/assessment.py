
import streamlit as st
from utils.prediction import predict_respiratory_probability


def render(html: str, container=st):
    """Render HTML safely: strip indentation and blank lines."""
    cleaned = "\n".join(
        line.strip() for line in html.splitlines() if line.strip()
    )
    container.markdown(cleaned, unsafe_allow_html=True)


# --------------------------------------------------
# NHANES CATEGORY MAPPINGS
# Display names are converted to original numeric codes
# before being passed to the trained model.
# --------------------------------------------------

race_options = {
    "Mexican American": 1.0,
    "Other Hispanic": 2.0,
    "Non-Hispanic White": 3.0,
    "Non-Hispanic Black": 4.0,
    "Other Race / Multiple Races": 5.0
}

education_options = {
    "Less than 9th grade": 1.0,
    "9th–11th grade": 2.0,
    "High school graduate / GED": 3.0,
    "Some college or Associate degree": 4.0,
    "College graduate or above": 5.0
}

marital_options = {
    "Married": 1.0,
    "Widowed": 2.0,
    "Divorced": 3.0,
    "Separated": 4.0,
    "Never married": 5.0,
    "Living with partner": 6.0
}


# --------------------------------------------------
# PAGE-SPECIFIC STYLES
# --------------------------------------------------

render("""
<style>
.form-sec { margin: 0 0 0.9rem; }
.form-sec-title { color: var(--ink); font-size: 18px; font-weight: 650; letter-spacing: -0.01em; }
.form-sec-cap { color: var(--ink-3); font-size: 13px; margin-top: 2px; }
.result-label { color: var(--ink-2); font-size: 14px; font-weight: 600; margin-top: 1.25rem; }
.result-value { color: var(--ink); font-size: 40px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; font-variant-numeric: tabular-nums; margin: 0.15rem 0 0; }
.plate { position: relative; padding: 2.6rem 2rem 0; margin-top: 0.5rem; }
.plate-track { position: relative; }
.plate-mark { position: absolute; left: var(--v); top: -8px; height: 28px; width: 0; border-left: 2px solid var(--pigment); transform: translateX(-1px); animation: plate-drop 700ms var(--ease) 500ms both; }
.plate-mark span { position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%); background: var(--pigment); color: #FFFFFF; font-size: 14px; font-weight: 700; padding: 0.2rem 0.55rem; border-radius: 6px; white-space: nowrap; font-variant-numeric: tabular-nums; }
.plate .scale { height: 24px; }
.plate .scale-axis { padding-top: 0.35rem !important; }
.plate.is-empty .plate-mark { display: none; }
@keyframes plate-drop { from { opacity: 0; transform: translate(-1px, 8px); } }
.result-copy { color: var(--ink-2); font-size: 15px; line-height: 1.6; margin: 1.25rem 0 1rem; max-width: 52ch; }
@media (prefers-reduced-motion: reduce) { .plate-mark { animation: none !important; } }
</style>
""")


def plate(pct=None, label=""):
    """Measurement scale for a single result."""
    if pct is None:
        return """
        <div class="plate is-empty">
            <div class="plate-track">
                <div class="scale" style="--v:0%">
                    <div class="scale-ticks"></div>
                </div>
                <div class="scale-axis">
                    <span>0%</span><span>50%</span><span>100%</span>
                </div>
            </div>
        </div>
        """

    return f"""
    <div class="plate">
        <div class="plate-track" style="--v:{pct:.2f}%">
            <div class="plate-mark"><span>{label}</span></div>
            <div class="scale">
                <div class="scale-fill"></div>
                <div class="scale-ticks"></div>
            </div>
            <div class="scale-axis">
                <span>0%</span><span>50%</span><span>100%</span>
            </div>
        </div>
    </div>
    """


# --------------------------------------------------
# PAGE INTRODUCTION
# --------------------------------------------------

render("""
<div class="page-head">
    <h1 class="page-title">Respiratory Health Assessment</h1>
    <p class="lede">
        Evaluate a structured NHANES research record using the trained,
        calibrated machine-learning pipeline. Enter participant information
        using understandable categories and survey details.
    </p>
    <div style="margin-top:0.9rem">
        <span class="status">Model-based research evaluation</span>
    </div>
</div>

<div class="note note-warn" style="margin-bottom:1.5rem">
    <strong>Before you begin:</strong> This assessment uses demographic,
    socioeconomic and smoking-related research variables. The selected
    categories are automatically converted into the original NHANES codes.
</div>
""")


form_col, result_col = st.columns([1.15, 1], gap="large")


# --------------------------------------------------
# RESEARCH RECORD FORM
# --------------------------------------------------

with form_col:

    with st.form("assessment_form"):

        render("""
        <div class="form-sec">
            <div class="form-sec-title">Participant information</div>
            <div class="form-sec-cap">
                Demographic and participant-level variables
            </div>
        </div>
        """)

        col1, col2 = st.columns(2)

        with col1:

            age = st.number_input(
                "Age (years)",
                min_value=20,
                max_value=80,
                value=45,
                help="Accepted model input range: 20–80 years."
            )

            gender = st.selectbox(
                "Gender",
                options=[1.0, 2.0],
                format_func=lambda x: (
                    "Male" if x == 1.0 else "Female"
                ),
                help="NHANES variable: RIAGENDR."
            )

        with col2:

            race_label = st.selectbox(
                "Race / Ethnicity",
                options=list(race_options.keys()),
                help="Select the appropriate NHANES race/ethnicity category."
            )

            education_label = st.selectbox(
                "Education Level",
                options=list(education_options.keys()),
                help="Select the participant's highest education category."
            )

        marital_label = st.selectbox(
            "Marital Status",
            options=list(marital_options.keys()),
            help="Select the participant's marital status."
        )

        st.markdown("---")

        render("""
        <div class="form-sec">
            <div class="form-sec-title">
                Socioeconomic and survey information
            </div>
            <div class="form-sec-cap">
                Income-to-poverty ratio, survey cycle and smoking category
            </div>
        </div>
        """)

        col3, col4 = st.columns(2)

        with col3:

            income_ratio = st.number_input(
                "Income-to-poverty ratio",
                min_value=0.0,
                max_value=5.0,
                value=2.5,
                step=0.1,
                help="NHANES variable: INDFMPIR."
            )

            cycle = st.selectbox(
                "NHANES survey cycle",
                options=["E", "F", "G"],
                format_func=lambda x: {
                    "E": "2007–2008 (Cycle E)",
                    "F": "2009–2010 (Cycle F)",
                    "G": "2011–2012 (Cycle G)"
                }[x],
                help="Select the cycle associated with the research record."
            )

        with col4:

            smoking = st.selectbox(
                "Smoking Status",
                options=["Never", "Former", "Current", "Unknown"],
                help="Use the same category definitions used during preprocessing."
            )

        st.markdown("---")

        render("""
        <div class="note">
            <strong>Input check:</strong> Selected categories are automatically
            converted into their original NHANES numeric codes before being
            passed to the existing calibrated prediction pipeline.
        </div>
        """)

        submitted = st.form_submit_button(
            "Generate research prediction  →",
            use_container_width=True,
            type="primary"
        )


# --------------------------------------------------
# MODEL OUTPUT
# --------------------------------------------------

with result_col:

    if not submitted:

        render(f"""
        <div class="panel">
            <h2 class="panel-title">Model output</h2>
            <p class="panel-sub">No assessment has been run yet.</p>
            <p class="result-copy" style="margin-top:0">
                Complete the research record and select Generate research
                prediction. The calibrated probability appears here
                on a 0–100% scale.
            </p>
            {plate(None)}
        </div>
        """)

    else:

        # Convert displayed category names to original NHANES codes.
        race = race_options[race_label]
        education = education_options[education_label]
        marital = marital_options[marital_label]

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

            probability = predict_respiratory_probability(input_data)

            shown = f"{probability * 100:.2f}%"
            position = max(
                0.0,
                min(float(probability), 1.0)
            ) * 100

            render(f"""
            <div class="panel">
                <h2 class="panel-title">Model output</h2>
                <p class="panel-sub">
                    <span class="status is-ready">Assessment complete</span>
                </p>
                <div class="result-label">Calibrated probability</div>
                <div class="result-value">{shown}</div>
                {plate(position, shown)}
                <p class="result-copy">
                    The calibrated model returned an estimated probability
                    for the dataset-defined self-reported respiratory outcome.
                    The marker shows the model output on a 0–100% scale.
                </p>
            </div>
            """)

            st.warning(
                "Research use only. This value is a model-estimated probability "
                "for the self-reported respiratory outcome defined in the "
                "research dataset. It is not a diagnosis or a clinically "
                "validated individual risk estimate."
            )

            with st.expander("Review submitted research record"):
                st.json(input_data)

        except Exception as e:
            st.error(f"Prediction error: {e}")
