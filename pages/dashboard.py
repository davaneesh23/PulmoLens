import streamlit as st


def render(html: str, container=st):
    """Render HTML safely: strip indentation and blank lines so Streamlit's
    Markdown parser never treats the HTML as a code block."""
    cleaned = "\n".join(line.strip() for line in html.splitlines() if line.strip())
    container.markdown(cleaned, unsafe_allow_html=True)


# --------------------------------------------------
# PAGE-SPECIFIC STYLES (global tokens come from app.py)
# --------------------------------------------------

render("""
<style>
.defs { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2rem; }
.def { border-top: 2px solid var(--ink); padding-top: 0.9rem; }
.def-term { color: var(--ink); font-size: 19px; font-weight: 650; letter-spacing: -0.01em; margin-bottom: 0.4rem; }
.def-text { color: var(--ink-2); font-size: 15px; line-height: 1.6; margin: 0; max-width: 40ch; }
.rule { border-top: 1px solid var(--line); margin: 0.9rem 0 0.9rem; }
.mod-title { color: var(--ink); font-size: 18px; font-weight: 650; letter-spacing: -0.01em; margin: 0 0 0.2rem; }
.mod-text { color: var(--ink-2); font-size: 15px; line-height: 1.55; margin: 0 0 0.45rem; max-width: 58ch; }
@media (max-width: 860px) { .defs { grid-template-columns: minmax(0, 1fr); gap: 1.5rem; } }
</style>
""")


def scale_rows(items):
    """items: (name, percent, display value, note). Draws the shared measurement scale."""
    rows = ""
    for name, pct, value, note in items:
        rows += f"""
        <div class="scale-row">
            <div class="scale-name">{name}<span class="scale-note">{note}</span></div>
            <div class="scale-cell"><div class="scale" style="--v:{pct}%"><div class="scale-fill"></div><div class="scale-ticks"></div></div></div>
            <div class="scale-value">{value}</div>
        </div>
        """
    axis = """
    <div class="scale-axis-gap"></div>
    <div class="scale-axis"><span>0%</span><span>50%</span><span>100%</span></div>
    <div class="scale-axis-gap"></div>
    """
    return f'<div class="scale-grid">{rows}{axis}</div>'


# --------------------------------------------------
# FIRST VIEWPORT: WHAT THIS IS + HOW WELL IT PERFORMS
# --------------------------------------------------

left, right = st.columns([1, 1.05], gap="large")

with left:
    render("""
    <div class="page-head">
        <h1 class="page-title">Understand<br>Respiratory Health.</h1>
        <p class="lede">
            An explainable and calibrated machine learning framework designed to explore
            respiratory health risk using structured population health data.
        </p>
    </div>
    """)

    if st.button("Start an assessment", type="primary", key="overview_start_assessment"):
        st.switch_page("pages/assessment.py")

    render("""
    <p class="section-note" style="margin-top:1.1rem">
        Research and educational use only. Outputs are statistical estimates, not medical diagnoses.
    </p>
    """)

metrics = [
    ("ROC-AUC", 75.26, "75.26%", "Discrimination performance"),
    ("PR-AUC", 17.53, "17.53%", "Precision-recall performance"),
    ("Recall", 50.81, "50.81%", "At the selected threshold"),
    ("Precision", 16.34, "16.34%", "At the selected threshold"),
]

with right:
    render(f"""
    <div class="panel">
        <h2 class="panel-title">Model Performance</h2>
        <p class="panel-sub">Research evaluation metrics from the held-out test dataset.</p>
        {scale_rows(metrics)}
    </div>
    """)


# --------------------------------------------------
# FRAMEWORK COMPONENTS
# --------------------------------------------------

render("""
<h2 class="section-title">Inside the PulmoLens Framework</h2>
<p class="section-note">The machine learning components behind the research platform.</p>
<div class="defs">
    <div class="def">
        <div class="def-term">Gradient Boosting</div>
        <p class="def-text">The selected machine learning algorithm used to estimate respiratory outcome probabilities.</p>
    </div>
    <div class="def">
        <div class="def-term">Sigmoid Calibration</div>
        <p class="def-text">A probability calibration technique applied to improve the reliability of model probability estimates.</p>
    </div>
    <div class="def">
        <div class="def-term">NHANES Dataset</div>
        <p class="def-text">Publicly available National Health and Nutrition Examination Survey data from three survey cycles.</p>
    </div>
</div>
""")


# --------------------------------------------------
# RESEARCH MODULES
# --------------------------------------------------

render("""
<h2 class="section-title">Explore Research Modules</h2>
<p class="section-note">Explore the different components of the PulmoLens platform.</p>
""")

modules = [
    ("Health Assessment",
     "Enter structured research data and generate a model-based respiratory risk estimate.",
     "pages/assessment.py", "Available", "is-ready"),
    ("Explainable AI",
     "Explore feature contributions and understand how model predictions are influenced.",
     "pages/explainability.py", "In development", "is-wip"),
    ("Model Reliability",
     "Explore probability calibration, model performance and prediction uncertainty.",
     "pages/reliability.py", "In development", "is-wip"),
]

for title, text, page, status, state in modules:
    render('<div class="rule"></div>')
    text_col, link_col = st.columns([3, 1], vertical_alignment="center")
    with text_col:
        render(f"""
        <div class="mod-title">{title}</div>
        <p class="mod-text">{text}</p>
        <span class="status {state}">{status}</span>
        """)
    with link_col:
        st.page_link(page, label=f"Open {title}")


# --------------------------------------------------
# RESEARCH DISCLAIMER
# --------------------------------------------------

render("""
<h2 class="section-title">Important Research Disclaimer</h2>
<div class="disclaimer">
    <strong>Research and educational use only.</strong><br>
    PulmoLens is an academic machine learning research prototype.
    Its outputs are statistical estimates based on structured
    NHANES survey data and are not medical diagnoses or
    individual clinical assessments. The model should not be
    used to make medical decisions. Consult a qualified
    healthcare professional for medical advice.
</div>
""")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

render("""
<div class="footer">
    <strong>PULMOLENS</strong><br>
    Explainable and Calibrated Machine Learning for Respiratory Health Research<br>
    Academic Research Prototype · Built with Python and Streamlit
</div>
""")