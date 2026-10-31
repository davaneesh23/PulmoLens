import streamlit as st


def render(html: str, container=st):
    """Render HTML safely: strip indentation and blank lines so Streamlit's
    Markdown parser never treats the HTML as a code block."""
    cleaned = "\n".join(line.strip() for line in html.splitlines() if line.strip())
    container.markdown(cleaned, unsafe_allow_html=True)


# --------------------------------------------------
# PAGE INTRODUCTION
# --------------------------------------------------

render("""
<div class="page-head">
    <h1 class="page-title">Explainable AI</h1>
    <p class="lede">
        Explore feature contributions and understand how model predictions are influenced.
    </p>
</div>
""")


# --------------------------------------------------
# MODULE STATUS
# --------------------------------------------------

status_col, next_col = st.columns([1.4, 1], gap="large")

with status_col:
    render("""
    <div class="panel">
        <h2 class="panel-title">Module status</h2>
        <p class="panel-sub"><span class="status is-wip">In development</span></p>
        <p class="def-text" style="max-width:52ch; color:var(--ink-2); font-size:16px; line-height:1.6; margin:0">
            This PulmoLens module is under development.
        </p>
    </div>
    """)

with next_col:
    render("""
    <h2 class="panel-title">Available now</h2>
    <p class="panel-sub">Open another part of the platform.</p>
    """)
    st.page_link("pages/assessment.py", label="Open Health Assessment")
    st.page_link("pages/dashboard.py", label="Back to Overview")


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