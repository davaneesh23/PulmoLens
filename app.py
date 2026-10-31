
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="PulmoLens",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional healthcare dashboard styling
st.markdown("""
<style>

/* Main application */
.stApp {
    background-color: #F5F8FC;
    color: #173B57;
}

/* Headings */
h1, h2, h3, h4 {
    color: #173B57 !important;
}

/* Normal text */
p, label, li {
    color: #34495E;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #EAF1F7;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] p {
    color: #173B57 !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #DCE6EF;
}

[data-testid="stMetricLabel"] {
    color: #526779 !important;
}

[data-testid="stMetricValue"] {
    color: #087E8B !important;
}

/* Buttons */
.stButton > button {
    background-color: #087E8B;
    color: white !important;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #066773;
    color: white !important;
}

/* Alerts */
[data-testid="stAlert"] p {
    color: #173B57 !important;
}

/* Dividers */
hr {
    border-color: #DCE6EF;
}

</style>
""", unsafe_allow_html=True)

# Sidebar branding
st.sidebar.title("🫁 PulmoLens")
st.sidebar.caption("RESPIRATORY HEALTH ANALYTICS")
st.sidebar.divider()

# Dashboard page
dashboard = st.Page(
    "pages/dashboard.py",
    title="Overview",
    icon=":material/dashboard:",
    default=True
)

# Assessment page
assessment = st.Page(
    "pages/assessment.py",
    title="Health Assessment",
    icon=":material/assignment:"
)

# Explainability page
explainability = st.Page(
    "pages/explainability.py",
    title="Explainable AI",
    icon=":material/psychology:"
)

# Reliability page
reliability = st.Page(
    "pages/reliability.py",
    title="Model Reliability",
    icon=":material/verified_user:"
)

# Navigation
pg = st.navigation([
    dashboard,
    assessment,
    explainability,
    reliability
])

pg.run()
