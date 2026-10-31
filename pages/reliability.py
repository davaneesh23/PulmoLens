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
.reads { margin: 0; padding: 0; }
.reads dt { color: var(--ink); font-size: 15px; font-weight: 650; margin: 0; }
.reads dd { color: var(--ink-2); font-size: 15px; line-height: 1.55; margin: 0.15rem 0 1rem; max-width: 52ch; }
.reads dd:last-child { margin-bottom: 0; }
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
# PAGE INTRODUCTION
# --------------------------------------------------

render("""
<div class="page-head">
    <h1 class="page-title">Model Reliability</h1>
    <p class="lede">
        Explore probability calibration, model performance and prediction uncertainty.
    </p>
</div>
""")


# --------------------------------------------------
# HELD-OUT PERFORMANCE
# --------------------------------------------------

metrics = [
    ("ROC-AUC", 75.26, "75.26%", "Discrimination performance"),
    ("PR-AUC", 17.53, "17.53%", "Precision-recall performance"),
    ("Recall", 50.81, "50.81%", "At the selected threshold"),
    ("Precision", 16.34, "16.34%", "At the selected threshold"),
]

perf_col, read_col = st.columns([1.35, 1], gap="large")

with perf_col:
    render(f"""
    <div class="panel">
        <h2 class="panel-title">Model Performance</h2>
        <p class="panel-sub">Research evaluation metrics from the held-out test dataset.</p>
        {scale_rows(metrics)}
    </div>
    """)

with read_col:
    render("""
    <div class="panel">
        <h2 class="panel-title">How to read these values</h2>
        <p class="panel-sub">Plain-language meaning of each metric.</p>
        <dl class="reads">
            <dt>ROC-AUC</dt>
            <dd>How well the model ranks records that have the outcome above those that do not.</dd>
            <dt>PR-AUC</dt>
            <dd>The balance between precision and recall across thresholds. It depends on how common the outcome is, so it is not directly comparable with ROC-AUC.</dd>
            <dt>Recall</dt>
            <dd>At the selected threshold, the model flags about half of the records that have the outcome.</dd>
            <dt>Precision</dt>
            <dd>At the selected threshold, roughly 1 in 6 of the records the model flags has the outcome.</dd>
        </dl>
    </div>
    """)


# --------------------------------------------------
# CALIBRATION AND UNCERTAINTY
# --------------------------------------------------

render("""
<h2 class="section-title">Probability calibration and prediction uncertainty</h2>
<div class="panel">
    <p class="panel-sub" style="margin-top:0"><span class="status is-wip">In development</span></p>
    <p style="color:var(--ink-2); font-size:16px; line-height:1.6; margin:0; max-width:56ch">
        This PulmoLens module is under development. Sigmoid calibration is applied to the model's
        probabilities; the calibration and uncertainty views will appear here.
    </p>
</div>
""")


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