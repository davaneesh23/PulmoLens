
import streamlit as st

st.set_page_config(
    page_title="PulmoLens | Respiratory Intelligence",
    page_icon="🫁",
    layout="wide"
)


def render(html: str):
    """Render HTML safely: strip indentation and blank lines so Streamlit's
    Markdown parser never treats the HTML as a code block."""
    cleaned = "\n".join(line.strip() for line in html.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


# --------------------------------------------------
# PREMIUM GLASSMORPHISM DASHBOARD DESIGN
# --------------------------------------------------

render("""
<style>

.stApp {
    background:
        radial-gradient(ellipse at 15% 15%, rgba(0, 190, 180, 0.16), transparent 38%),
        radial-gradient(ellipse at 85% 35%, rgba(34, 115, 180, 0.18), transparent 40%),
        linear-gradient(135deg, #071827 0%, #0B2638 50%, #102F43 100%);
    color: #EAF5FA;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1450px;
}

h1, h2, h3, p, label {
    color: #EAF5FA;
}

.glass-card {
    background: rgba(255, 255, 255, 0.075);
    border: 1px solid rgba(255, 255, 255, 0.17);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.18);
}

.hero {
    min-height: 470px;
    padding: 48px;
    border-radius: 28px;
    background:
        linear-gradient(110deg, rgba(7, 24, 39, 0.96), rgba(9, 51, 68, 0.72)),
        radial-gradient(circle at 80% 50%, rgba(0, 220, 200, 0.2), transparent 40%);
    border: 1px solid rgba(151, 226, 232, 0.2);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
    display: flex;
    align-items: center;
    overflow: hidden;
    position: relative;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 650px;
}

.hero-kicker {
    color: #55D9CF;
    letter-spacing: 3px;
    font-size: 12px;
    font-weight: 700;
}

.hero-title {
    font-size: clamp(36px, 5vw, 60px);
    line-height: 1.08;
    font-weight: 750;
    color: #FFFFFF;
    margin: 20px 0;
}

.hero-description {
    color: #C0D5E1;
    font-size: 17px;
    line-height: 1.8;
    max-width: 570px;
}

.hero-status {
    display: inline-block;
    margin-top: 20px;
    padding: 9px 16px;
    border-radius: 30px;
    background: rgba(0, 210, 180, 0.12);
    border: 1px solid rgba(0, 220, 190, 0.3);
    color: #69E8D6;
    font-size: 12px;
    letter-spacing: 1px;
}

.lungs-area {
    position: absolute;
    right: 4%;
    top: 5%;
    width: 39%;
    height: 90%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.lungs-svg {
    width: 100%;
    max-height: 420px;
    overflow: visible;
    animation: breathe 4s ease-in-out infinite;
    transform-origin: center center;
    filter: drop-shadow(0 0 22px rgba(48, 226, 210, 0.32));
}

@keyframes breathe {
    0%, 100% { transform: scale(0.96); }
    50% { transform: scale(1.045); }
}

.lung-glow {
    animation: glow 4s ease-in-out infinite;
}

@keyframes glow {
    0%, 100% { opacity: 0.55; }
    50% { opacity: 1; }
}

.metric-glass {
    background: rgba(255,255,255,0.075);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 18px;
    padding: 22px;
    min-height: 145px;
    backdrop-filter: blur(15px);
}

.metric-label {
    color: #B7CDD9;
    font-size: 13px;
    letter-spacing: 1px;
}

.metric-value {
    color: #5DE0D1;
    font-size: 34px;
    font-weight: 750;
    margin: 10px 0 4px;
}

.metric-description {
    color: #A9C2D0;
    font-size: 12px;
}

.section-heading {
    color: #FFFFFF;
    font-size: 27px;
    font-weight: 700;
    margin-top: 45px;
}

.section-subheading {
    color: #AFC6D4;
    font-size: 14px;
    margin-bottom: 22px;
}

.module-card {
    background: rgba(255,255,255,0.065);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 18px;
    padding: 23px;
    min-height: 215px;
    backdrop-filter: blur(16px);
    transition: all 0.3s ease;
}

.module-card:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.11);
    border-color: rgba(75,220,205,0.45);
}

.module-icon {
    font-size: 30px;
}

.module-title {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 700;
    margin: 13px 0;
}

.module-description {
    color: #B4C9D5;
    font-size: 13px;
    line-height: 1.7;
}

.module-status {
    color: #62DCCB;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-top: 15px;
}

.info-card {
    background: rgba(255,255,255,0.065);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 17px;
    padding: 23px;
    min-height: 170px;
}

.info-title {
    color: #FFFFFF;
    font-size: 17px;
    font-weight: 700;
}

.info-description {
    color: #B4C9D5;
    font-size: 13px;
    line-height: 1.7;
}

.disclaimer {
    background: rgba(255, 184, 77, 0.08);
    border: 1px solid rgba(255, 184, 77, 0.25);
    border-radius: 16px;
    padding: 20px;
    color: #E8D9B8;
    font-size: 13px;
    line-height: 1.8;
}

.footer {
    text-align: center;
    color: #8FAAB9;
    font-size: 12px;
    padding: 35px 0 10px;
    border-top: 1px solid rgba(255,255,255,0.12);
    margin-top: 45px;
}

.stButton > button {
    background: linear-gradient(90deg, #087E8B, #10A99B);
    color: white !important;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 12px;
    padding: 12px 25px;
    font-weight: 700;
}

.stButton > button:hover {
    background: #10A99B;
    border-color: #6DE8DA;
}

[data-testid="stMetricValue"] {
    color: #5DE0D1;
}

[data-testid="stMetricLabel"] {
    color: #B7CDD9;
}

</style>
""")


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

render("""
<div class="hero">

    <div class="hero-content">

        <div class="hero-kicker">
            PULMOLENS · INTELLIGENT HEALTH RESEARCH
        </div>

        <div class="hero-title">
            Understand<br>
            Respiratory Health.
        </div>

        <div class="hero-description">
            An explainable and calibrated machine learning
            framework designed to explore respiratory health
            risk using structured population health data.
        </div>

        <div class="hero-status">
            ● RESEARCH PLATFORM ACTIVE
        </div>

    </div>

    <div class="lungs-area">
        <svg class="lungs-svg" viewBox="0 0 500 540"
             xmlns="http://www.w3.org/2000/svg">

            <defs>
                <linearGradient id="lungGradient" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#8FFFF0"/>
                    <stop offset="50%" stop-color="#19BEB8"/>
                    <stop offset="100%" stop-color="#087E9A"/>
                </linearGradient>

                <linearGradient id="tubeGradient" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#B6FFF4"/>
                    <stop offset="100%" stop-color="#16AFAE"/>
                </linearGradient>

                <filter id="softGlow">
                    <feGaussianBlur stdDeviation="8" result="blur"/>
                    <feMerge>
                        <feMergeNode in="blur"/>
                        <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                </filter>
            </defs>

            <path d="M250 45 L250 215"
                  stroke="url(#tubeGradient)"
                  stroke-width="29"
                  stroke-linecap="round"
                  fill="none"/>

            <g stroke="#C1FFF4" stroke-width="3" opacity="0.6">
                <path d="M237 72 H263 M237 91 H263 M237 110 H263 M237 129 H263 M237 148 H263 M237 167 H263"/>
            </g>

            <g fill="none" stroke="url(#tubeGradient)"
               stroke-width="20" stroke-linecap="round">
                <path d="M250 190 C220 225 185 235 160 270"/>
                <path d="M250 190 C280 225 315 235 340 270"/>
            </g>

            <path class="lung-glow"
                  d="M205 205 C165 200 115 220 90 270 C55 345 68 440 115 472 C155 500 204 468 215 420 C227 370 220 300 220 250 C220 225 216 211 205 205Z"
                  fill="url(#lungGradient)"
                  opacity="0.86"
                  filter="url(#softGlow)"/>

            <path class="lung-glow"
                  d="M295 205 C335 200 385 220 410 270 C445 345 432 440 385 472 C345 500 296 468 285 420 C273 370 280 300 280 250 C280 225 284 211 295 205Z"
                  fill="url(#lungGradient)"
                  opacity="0.86"
                  filter="url(#softGlow)"/>

            <g stroke="#D2FFF6" stroke-width="6"
               fill="none" stroke-linecap="round" opacity="0.7">
                <path d="M160 270 L125 310 L115 360"/>
                <path d="M160 270 L180 320 L175 390"/>
                <path d="M125 310 L95 335"/>
                <path d="M180 320 L205 350"/>
                <path d="M340 270 L375 310 L385 360"/>
                <path d="M340 270 L320 320 L325 390"/>
                <path d="M375 310 L405 335"/>
                <path d="M320 320 L295 350"/>
            </g>

            <path d="M250 205 L250 430"
                  stroke="#D6FFF7"
                  stroke-width="3"
                  opacity="0.35"
                  fill="none"/>

            <g fill="#9CFFF0" opacity="0.8">
                <circle cx="75" cy="180" r="4"/>
                <circle cx="420" cy="170" r="5"/>
                <circle cx="440" cy="390" r="3"/>
                <circle cx="60" cy="400" r="3"/>
                <circle cx="250" cy="25" r="4"/>
            </g>
        </svg>
    </div>

</div>
""")


# --------------------------------------------------
# PERFORMANCE METRICS
# --------------------------------------------------

render("""
<div class="section-heading">Model Performance</div>
<div class="section-subheading">
Research evaluation metrics from the held-out test dataset.
</div>
""")

metrics = [
    ("ROC-AUC", "75.26%", "Discrimination performance"),
    ("PR-AUC", "17.53%", "Precision-recall performance"),
    ("RECALL", "50.81%", "At the selected threshold"),
    ("PRECISION", "16.34%", "At the selected threshold"),
]

cols = st.columns(4)

for col, (label, value, description) in zip(cols, metrics):
    with col:
        render(f"""
        <div class="metric-glass">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-description">{description}</div>
        </div>
        """)


# --------------------------------------------------
# MODEL INFORMATION
# --------------------------------------------------

render("""
<div class="section-heading">Inside the PulmoLens Framework</div>
<div class="section-subheading">
The machine learning components behind the research platform.
</div>
""")

model_info = [
    ("🧠", "Gradient Boosting",
     "The selected machine learning algorithm used to estimate respiratory outcome probabilities."),
    ("⚖️", "Sigmoid Calibration",
     "A probability calibration technique applied to improve the reliability of model probability estimates."),
    ("🌍", "NHANES Dataset",
     "Publicly available National Health and Nutrition Examination Survey data from three survey cycles."),
]

cols = st.columns(3)

for col, (icon, title, description) in zip(cols, model_info):
    with col:
        render(f"""
        <div class="info-card">
            <div style="font-size:30px">{icon}</div>
            <div class="info-title">{title}</div>
            <p class="info-description">{description}</p>
        </div>
        """)


# --------------------------------------------------
# RESEARCH MODULES
# --------------------------------------------------

render("""
<div class="section-heading">Explore Research Modules</div>
<div class="section-subheading">
Explore the different components of the PulmoLens platform.
</div>
""")

modules = [
    ("📊", "Health Assessment",
     "Enter structured research data and generate a model-based respiratory risk estimate.",
     "AVAILABLE"),
    ("🔍", "Explainable AI",
     "Explore feature contributions and understand how model predictions are influenced.",
     "AVAILABLE IN NAVIGATION"),
    ("📈", "Model Reliability",
     "Explore probability calibration, model performance and prediction uncertainty.",
     "AVAILABLE IN NAVIGATION"),
]

cols = st.columns(3)

for col, (icon, title, description, status) in zip(cols, modules):
    with col:
        render(f"""
        <div class="module-card">
            <div class="module-icon">{icon}</div>
            <div class="module-title">{title}</div>
            <div class="module-description">{description}</div>
            <div class="module-status">● {status}</div>
        </div>
        """)


# --------------------------------------------------
# RESEARCH DISCLAIMER
# --------------------------------------------------

render("""
<div class="section-heading">Important Research Disclaimer</div>
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
    Explainable and Calibrated Machine Learning for Respiratory Health Research<br><br>
    Academic Research Prototype · Built with Python and Streamlit
</div>
""")
