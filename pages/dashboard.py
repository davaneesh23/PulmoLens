
import streamlit as st

st.title("🫁 PulmoLens")
st.caption(
    "Explainable and Calibrated Machine Learning "
    "for Respiratory Health Research"
)

st.divider()

st.subheader("Project Overview")

st.write("""
PulmoLens is an educational machine learning research
framework that analyses structured health and behavioural
data to investigate patterns associated with reported
respiratory health conditions.

It combines machine learning, probability calibration,
explainable AI and prediction uncertainty analysis.
""")

# Performance metrics from your previous test evaluation
col1, col2, col3, col4 = st.columns(4)

col1.metric("ROC-AUC", "0.7526")
col2.metric("PR-AUC", "0.1753")
col3.metric("Recall", "50.81%")
col4.metric("Precision", "16.34%")

st.caption(
    "Reported evaluation results from the earlier "
    "test experiment. Metrics are not clinical validation."
)

st.divider()

st.subheader("Research Modules")

c1, c2 = st.columns(2)

with c1:
    st.info("**Machine Learning**\n\n"
            "Gradient Boosting and model comparison.")

    st.info("**Explainable AI**\n\n"
            "SHAP feature importance and explanations.")

with c2:
    st.info("**Probability Calibration**\n\n"
            "Sigmoid calibration and reliability analysis.")

    st.info("**Uncertainty Analysis**\n\n"
            "Bootstrap model stability experiments.")

st.divider()

st.warning(
    "PulmoLens is a research prototype, not a "
    "medical diagnostic or clinical decision system."
)
