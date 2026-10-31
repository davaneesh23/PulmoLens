import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="PulmoLens | Respiratory Health Intelligence",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)


def render(html: str, container=st):
    """Render HTML safely: strip indentation and blank lines so Streamlit's
    Markdown parser never treats the HTML as a code block."""
    cleaned = "\n".join(line.strip() for line in html.splitlines() if line.strip())
    container.markdown(cleaned, unsafe_allow_html=True)


# --------------------------------------------------
# GLOBAL GLASSMORPHISM DESIGN SYSTEM
# --------------------------------------------------

render("""
<style>

/* =========================================
   GLOBAL APPLICATION
========================================= */

.stApp {
    background:
        radial-gradient(ellipse at 12% 15%, rgba(0, 190, 180, 0.13), transparent 38%),
        radial-gradient(ellipse at 85% 35%, rgba(34, 115, 180, 0.13), transparent 40%),
        linear-gradient(135deg, #071827 0%, #0B2638 50%, #102F43 100%) !important;
    color: #EAF5FA !important;
    font-family: "Inter", "Segoe UI", sans-serif;
}

/* Streamlit top bar (the white strip) */

[data-testid="stHeader"],
header[data-testid="stHeader"] {
    background: transparent !important;
    background-color: transparent !important;
}

[data-testid="stToolbar"],
[data-testid="stToolbar"] * {
    color: #C1D6E0 !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

.block-container {
    padding-top: 3.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Global typography */

h1, h2, h3, h4, h5 {
    color: #F1FAFC !important;
    font-weight: 650 !important;
    letter-spacing: -0.5px;
}

p, li, label {
    color: #B8CDD9;
    line-height: 1.65;
}

/* =========================================
   GLASSMORPHISM SIDEBAR
========================================= */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        rgba(7, 24, 39, 0.98),
        rgba(10, 39, 56, 0.98),
        rgba(14, 48, 66, 0.98)
    ) !important;
    border-right: 1px solid rgba(110, 220, 215, 0.18);
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
    padding-top: 1.5rem;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: #C1D6E0;
}

.brand-container {
    padding: 16px 12px 24px 12px;
    margin-bottom: 22px;
    border-bottom: 1px solid rgba(255,255,255,0.14);
}

.brand-name {
    color: #FFFFFF !important;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -1.2px;
}

.brand-name span {
    color: #55D9CF !important;
}

.brand-tagline {
    color: #91B0BF !important;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.7px;
    line-height: 1.8;
    margin-top: 7px;
}

[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #6EDDD1 !important;
    font-size: 10px;
    font-weight: 750;
    letter-spacing: 1.8px;
}

[data-testid="stSidebarNav"] {
    padding-top: 10px;
}

[data-testid="stSidebarNav"] a,
[data-testid="stSidebarNavLink"] {
    border-radius: 13px !important;
    margin: 6px 5px !important;
    padding: 12px 13px !important;
    background: transparent !important;
    transition: all 0.25s ease !important;
}

[data-testid="stSidebarNav"] a span,
[data-testid="stSidebarNav"] a svg,
[data-testid="stSidebarNavLink"] span,
[data-testid="stSidebarNavLink"] svg {
    color: #C3D8E2 !important;
    fill: #C3D8E2 !important;
}

[data-testid="stSidebarNav"] a:hover,
[data-testid="stSidebarNavLink"]:hover {
    background: rgba(255,255,255,0.08) !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"],
[data-testid="stSidebarNavLink"][aria-current="page"] {
    background: rgba(30, 190, 177, 0.16) !important;
    border: 1px solid rgba(80, 224, 207, 0.32) !important;
    box-shadow: 0 0 20px rgba(0, 210, 190, 0.08);
}

[data-testid="stSidebarNav"] a[aria-current="page"] span,
[data-testid="stSidebarNav"] a[aria-current="page"] svg,
[data-testid="stSidebarNavLink"][aria-current="page"] span,
[data-testid="stSidebarNavLink"][aria-current="page"] svg {
    color: #65E5D5 !important;
    fill: #65E5D5 !important;
}

[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.14) !important;
}

/* =========================================
   GLOBAL TOP HEADER
========================================= */

.top-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 23px;
    background: rgba(255,255,255,0.065);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 16px;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    margin-bottom: 28px;
}

.header-brand {
    color: #FFFFFF !important;
    font-size: 17px;
    font-weight: 750;
}

.header-label {
    color: #9EB9C7 !important;
    font-size: 10px;
    letter-spacing: 1.5px;
    font-weight: 650;
    margin-top: 4px;
}

.status-pill {
    background: rgba(0,210,170,0.10);
    border: 1px solid rgba(70,225,190,0.25);
    color: #70E4C9 !important;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 10px;
    font-weight: 750;
    letter-spacing: 1px;
}

/* =========================================
   GLASS METRIC CARDS
========================================= */

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.065) !important;
    padding: 21px;
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 15px;
    backdrop-filter: blur(15px);
    box-shadow: 0 5px 20px rgba(0,0,0,0.12);
}

[data-testid="stMetricLabel"] {
    color: #B4C9D5 !important;
    font-size: 13px;
}

[data-testid="stMetricValue"] {
    color: #5DE0D1 !important;
    font-weight: 750;
}

/* =========================================
   BUTTONS
========================================= */

.stApp button[kind="primary"],
.stApp button[kind="secondary"],
.stApp button[data-testid="stBaseButton-primary"],
.stApp button[data-testid="stBaseButton-secondary"],
.stApp [data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #087E8B, #10A99B) !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border: 1px solid rgba(100,230,215,0.3) !important;
    border-radius: 11px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}

.stApp button[kind] p,
.stApp button[kind] span,
.stApp button[kind] div,
.stApp [data-testid="stFormSubmitButton"] button * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

.stApp button[kind]:hover {
    background: #066773 !important;
    border-color: #60DCCF !important;
}

.stApp button:disabled {
    color: #FFFFFF !important;
    opacity: 0.75 !important;
}

/* =========================================
   INPUT FIELDS
========================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background: rgba(255,255,255,0.08) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255,255,255,0.20) !important;
    border-radius: 10px !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #91AAB8 !important;
}

/* =========================================
   ALERTS AND EXPANDERS
========================================= */

[data-testid="stAlert"] {
    border-radius: 13px;
}

[data-testid="stExpander"] {
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 12px;
}

[data-testid="stExpander"] summary {
    color: #EAF5FA !important;
}

/* =========================================
   DIVIDERS AND FOOTER
========================================= */

hr {
    border-color: rgba(255,255,255,0.15) !important;
}

.custom-footer {
    margin-top: 45px;
    padding-top: 18px;
    border-top: 1px solid rgba(255,255,255,0.14);
    color: #91AAB8;
    font-size: 11px;
    text-align: center;
}

/* =========================================
   SIDEBAR SCROLLBAR
========================================= */

[data-testid="stSidebar"] ::-webkit-scrollbar {
    width: 5px;
}

[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
    background: rgba(85,210,200,0.35);
    border-radius: 10px;
}

</style>
""")


# --------------------------------------------------
# SIDEBAR BRANDING
# --------------------------------------------------

render("""
<div class="brand-container">
    <div class="brand-name">🫁 <span>PulmoLens</span></div>
    <div class="brand-tagline">
        RESPIRATORY HEALTH<br>
        INTELLIGENCE
    </div>
</div>
""", container=st.sidebar)

st.sidebar.caption("RESEARCH PLATFORM")


# --------------------------------------------------
# PAGE DEFINITIONS
# --------------------------------------------------

dashboard = st.Page(
    "pages/dashboard.py",
    title="Overview",
    icon=":material/dashboard:",
    default=True
)

assessment = st.Page(
    "pages/assessment.py",
    title="Health Assessment",
    icon=":material/assignment:"
)

explainability = st.Page(
    "pages/explainability.py",
    title="Explainable AI",
    icon=":material/psychology:"
)

reliability = st.Page(
    "pages/reliability.py",
    title="Model Reliability",
    icon=":material/verified_user:"
)


# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

pg = st.navigation([
    dashboard,
    assessment,
    explainability,
    reliability
])


# --------------------------------------------------
# GLOBAL HEADER
# --------------------------------------------------

render("""
<div class="top-header">
    <div>
        <div class="header-brand">PulmoLens</div>
        <div class="header-label">EXPLAINABLE RESPIRATORY HEALTH RESEARCH</div>
    </div>
    <div class="status-pill">● RESEARCH SYSTEM ACTIVE</div>
</div>
""")


# --------------------------------------------------
# RUN SELECTED PAGE
# --------------------------------------------------

pg.run()