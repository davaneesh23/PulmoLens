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
# GLOBAL DESIGN SYSTEM
# Light "plate" system for shared screens and projectors:
# bone-white ground, white panels with hairlines, ink-blue
# navigation rail, cobalt actions, rose estimate marker.
# Every page inherits these tokens and components.
# --------------------------------------------------

render("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700&display=swap');

:root {
    --ground: #F1F4F6;
    --surface: #FFFFFF;
    --surface-2: #E3E9EF;
    --line: #D3DCE4;
    --line-strong: #8797A6;
    --ink: #14202C;
    --ink-2: #3F4F5E;
    --ink-3: #566676;
    --rail: #13283E;
    --rail-2: #27476B;
    --rail-ink: #E6EDF4;
    --rail-ink-2: #A9BBCB;
    --action: #1F4F96;
    --action-hover: #173F7B;
    --pigment: #B02B45;
    --ochre-ink: #6B4500;
    --ochre-tint: #FBF1DC;
    --ochre-line: #E0C48A;
    --ok: #17694A;
    --font: "Source Sans 3", "Segoe UI", system-ui, -apple-system, Roboto, "Helvetica Neue", Arial, sans-serif;
    --ease: cubic-bezier(0.16, 1, 0.3, 1);
}

/* ---------- application ---------- */
html, body, .stApp { color-scheme: light; }
.stApp, [data-testid="stApp"] {
    background: var(--ground) !important;
    color: var(--ink) !important;
    font-family: var(--font);
    font-size: 15px;
}
.stApp *:not([class*="material"]):not([data-testid="stIconMaterial"]):not(code):not(pre) { font-family: var(--font); }
.stApp ::selection { background: #BFD3F0; color: var(--ink); }

[data-testid="stHeader"], header[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"], [data-testid="stToolbar"] * { color: var(--ink-2) !important; }
[data-testid="stDecoration"] { display: none !important; }

[data-testid="stMainBlockContainer"], .block-container {
    max-width: 1240px;
    padding: 2.25rem 2.5rem 4rem;
}
@media (max-width: 760px) {
    [data-testid="stMainBlockContainer"], .block-container { padding: 1.25rem 1rem 3rem; }
}

.stApp h1, .stApp h2, .stApp h3, .stApp h4 { color: var(--ink) !important; letter-spacing: -0.015em; }
.stApp p, .stApp li { line-height: 1.6; }
.stApp [data-testid="stMarkdownContainer"] p { color: var(--ink-2); }
.stApp [data-testid="stCaptionContainer"], .stApp [data-testid="stCaptionContainer"] * { color: var(--ink-3) !important; }
.stApp hr { border-color: var(--line) !important; }
.stApp a { text-underline-offset: 3px; }
.stApp :focus-visible { outline: 2px solid var(--action) !important; outline-offset: 2px; }
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-thumb { background: #B5C2CE; border-radius: 10px; border: 2px solid var(--ground); }

/* ---------- navigation rail ---------- */
[data-testid="stSidebar"] { background: var(--rail) !important; border-right: 0; }
[data-testid="stSidebar"] > div:first-child { background: transparent !important; }
[data-testid="stSidebarContent"] { display: flex; flex-direction: column; }
[data-testid="stSidebarHeader"] { order: -2; }
[data-testid="stSidebarUserContent"] { order: -1; padding-top: 0; padding-bottom: 0.5rem; }
[data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label { color: var(--rail-ink-2); }
[data-testid="stSidebar"] button { color: var(--rail-ink) !important; }
[data-testid="stSidebarNav"] { padding-top: 0.25rem; }
[data-testid="stSidebarNavLink"], [data-testid="stSidebarNav"] a {
    border-radius: 8px !important;
    margin: 2px 0.5rem !important;
    padding: 0.6rem 0.75rem !important;
    background: transparent !important;
    transition: background-color 160ms var(--ease);
}
[data-testid="stSidebarNavLink"] span, [data-testid="stSidebarNavLink"] p,
[data-testid="stSidebarNav"] a span, [data-testid="stSidebarNav"] a p {
    color: var(--rail-ink) !important;
    font-size: 15px;
    font-weight: 500;
}
[data-testid="stSidebarNavLink"]:hover, [data-testid="stSidebarNav"] a:hover { background: rgba(255,255,255,0.07) !important; }
[data-testid="stSidebarNavLink"][aria-current="page"], [data-testid="stSidebarNav"] a[aria-current="page"] {
    background: var(--rail-2) !important;
}
[data-testid="stSidebarNavLink"][aria-current="page"] span, [data-testid="stSidebarNavLink"][aria-current="page"] p,
[data-testid="stSidebarNav"] a[aria-current="page"] span, [data-testid="stSidebarNav"] a[aria-current="page"] p {
    color: #FFFFFF !important;
    font-weight: 600;
}
[data-testid="stSidebar"] :focus-visible { outline: 2px solid #9CC2F5 !important; }

.brand { display: flex; align-items: center; gap: 0.75rem; padding: 0.25rem 0.75rem 1.25rem; margin: 0 0 0.5rem; border-bottom: 1px solid rgba(255,255,255,0.12); }
.brand-mark { width: 34px; height: 34px; flex: none; }
.brand-name { color: #FFFFFF; font-size: 21px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; }
.brand-sub { color: var(--rail-ink-2); font-size: 13px; line-height: 1.35; margin-top: 2px; }

/* ---------- top bar ---------- */
.topbar { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 0 0 0.9rem; margin-bottom: 1.75rem; border-bottom: 1px solid var(--line); }
.topbar-title { color: var(--ink-2); font-size: 14px; font-weight: 500; }
.topbar-title strong { color: var(--ink); font-weight: 700; }
.topbar-status { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--ink-2); font-size: 13px; font-weight: 500; white-space: nowrap; }
.topbar-status::before { content: ""; width: 8px; height: 8px; border-radius: 50%; background: var(--ok); }
@media (max-width: 640px) { .topbar-title span { display: none; } }

/* ---------- page head ---------- */
.page-head { margin: 0 0 1.75rem; }
.page-title { color: var(--ink); font-size: clamp(30px, 3.6vw, 44px); font-weight: 700; line-height: 1.08; letter-spacing: -0.025em; margin: 0 0 0.75rem; text-wrap: balance; }
.lede { color: var(--ink-2); font-size: 18px; line-height: 1.6; max-width: 62ch; margin: 0; text-wrap: pretty; }
.section-title { color: var(--ink); font-size: 22px; font-weight: 650; letter-spacing: -0.015em; line-height: 1.2; margin: 3rem 0 0.35rem; }
.section-note { color: var(--ink-2); font-size: 15px; max-width: 62ch; margin: 0 0 1.25rem; }

/* ---------- panels, notes, status ---------- */
.panel { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 1.5rem 1.6rem; }
.panel-title { color: var(--ink); font-size: 17px; font-weight: 650; letter-spacing: -0.01em; margin: 0; }
.panel-sub { color: var(--ink-3); font-size: 13px; margin: 0.15rem 0 1.1rem; }
.note { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 0.85rem 1.1rem; color: var(--ink-2); font-size: 14px; line-height: 1.6; }
.note strong { color: var(--ink); }
.note-warn { background: var(--ochre-tint); border-color: var(--ochre-line); color: var(--ochre-ink); }
.note-warn strong { color: var(--ochre-ink); }
.disclaimer { background: var(--ochre-tint); border: 1px solid var(--ochre-line); border-radius: 10px; padding: 1.1rem 1.3rem; color: var(--ochre-ink); font-size: 14px; line-height: 1.65; max-width: 80ch; }
.disclaimer strong { color: var(--ochre-ink); font-weight: 700; }
.status { display: inline-flex; align-items: center; gap: 0.45rem; color: var(--ink-2); font-size: 13px; font-weight: 600; white-space: nowrap; }
.status::before { content: ""; width: 8px; height: 8px; border-radius: 50%; background: var(--ink-3); }
.status.is-ready::before { background: var(--ok); }
.status.is-ready { color: var(--ok); }
.status.is-wip::before { background: transparent; border: 2px solid var(--ochre-ink); }
.footer { color: var(--ink-3); font-size: 13px; line-height: 1.7; margin-top: 3rem; padding-top: 1.25rem; border-top: 1px solid var(--line); }
.footer strong { color: var(--ink-2); }

/* ---------- signature: the measurement scale ---------- */
.scale-grid { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1.3fr) 4.5rem; column-gap: 1.25rem; align-items: stretch; }
.scale-row { display: contents; }
.scale-row > * { padding: 0.8rem 0; background: linear-gradient(var(--line), var(--line)) top / 100% 1px no-repeat; }
.scale-row:first-of-type > * { background: none; padding-top: 0.2rem; }
.scale-name { color: var(--ink); font-size: 15px; font-weight: 650; line-height: 1.25; display: flex; flex-direction: column; justify-content: center; }
.scale-note { display: block; color: var(--ink-3); font-size: 13px; font-weight: 400; margin-top: 2px; }
.scale-value { color: var(--ink); font-size: 18px; font-weight: 700; text-align: right; font-variant-numeric: tabular-nums; display: flex; align-items: center; justify-content: flex-end; }
.scale-cell { display: flex; align-items: center; }
.scale { position: relative; height: 22px; width: 100%; }
.scale::before { content: ""; position: absolute; left: 0; right: 0; top: 0; height: 9px; border-radius: 3px; background: var(--surface-2); }
.scale-fill { position: absolute; left: 0; top: 0; height: 9px; width: var(--v); border-radius: 3px 0 0 3px; background: var(--action); transform-origin: left center; animation: plate-grow 900ms var(--ease) both; }
.scale-ticks { position: absolute; left: 0; right: 0; top: 12px; height: 6px; background-image: linear-gradient(to right, var(--line-strong) 1px, transparent 1px); background-size: 10% 100%; border-right: 1px solid var(--line-strong); }
.scale-axis-gap { background: none !important; padding: 0.15rem 0 0 !important; }
.scale-axis { display: flex; justify-content: space-between; color: var(--ink-3); font-size: 12px; font-variant-numeric: tabular-nums; background: none !important; padding: 0.15rem 0 0 !important; }
@keyframes plate-grow { from { transform: scaleX(0); } }
@media (max-width: 640px) {
    .scale-grid { grid-template-columns: minmax(0, 1fr); }
    .scale-row { display: grid; grid-template-columns: minmax(0, 1fr) auto; column-gap: 1rem; row-gap: 0.55rem; padding: 0.8rem 0; background: linear-gradient(var(--line), var(--line)) top / 100% 1px no-repeat; }
    .scale-row:first-of-type { background: none; padding-top: 0.2rem; }
    .scale-row > * { background: none; padding: 0; }
    .scale-row .scale-name { grid-column: 1; grid-row: 1; }
    .scale-row .scale-value { grid-column: 2; grid-row: 1; }
    .scale-row .scale-cell { grid-column: 1 / -1; grid-row: 2; }
    .scale-axis-gap { display: none; }
}

/* ---------- forms and controls ---------- */
.stApp [data-testid="stWidgetLabel"], .stApp [data-testid="stWidgetLabel"] p, .stApp [data-testid="stWidgetLabel"] label {
    color: var(--ink) !important; font-size: 14px !important; font-weight: 600 !important; line-height: 1.3;
}
.stApp [data-testid="stWidgetLabel"] svg { color: var(--ink-3) !important; fill: var(--ink-3) !important; }
.stApp [data-baseweb="input"], .stApp [data-baseweb="base-input"], .stApp [data-baseweb="select"] > div {
    background: var(--surface) !important;
    border-color: var(--line-strong) !important;
    border-radius: 8px !important;
    min-height: 44px;
}
.stApp [data-baseweb="input"] input, .stApp [data-baseweb="base-input"] input, .stApp [data-baseweb="select"] input,
.stApp [data-baseweb="select"] [class*="singleValue"], .stApp [data-baseweb="select"] div[value] {
    color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important; background: transparent !important;
    font-size: 15px; font-variant-numeric: tabular-nums;
}
.stApp [data-baseweb="select"] svg { fill: var(--ink-2) !important; }
.stApp [data-baseweb="input"]:focus-within, .stApp [data-baseweb="select"] > div:focus-within { border-color: var(--action) !important; }
.stApp [data-testid="stNumberInputContainer"] button { background: transparent !important; color: var(--ink-2) !important; }
.stApp [data-testid="stNumberInputContainer"] button:hover { background: var(--surface-2) !important; }
div[data-baseweb="popover"] [data-baseweb="menu"], div[data-baseweb="popover"] ul {
    background: var(--surface) !important; border: 1px solid var(--line-strong); border-radius: 8px;
}
div[data-baseweb="popover"] li, div[data-baseweb="popover"] [role="option"] { background: var(--surface) !important; color: var(--ink) !important; }
div[data-baseweb="popover"] li:hover, div[data-baseweb="popover"] [role="option"]:hover, div[data-baseweb="popover"] [aria-selected="true"] { background: var(--surface-2) !important; }
div[data-baseweb="tooltip"] > div, div[data-baseweb="popover"] [data-testid="stTooltipContent"] { background: var(--ink) !important; color: #FFFFFF !important; border-radius: 8px; }

.stApp [data-testid="stForm"] { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 1.5rem 1.6rem 1.4rem; }
.stApp [data-testid="stVerticalBlockBorderWrapper"] { border-color: var(--line) !important; }

.stApp button[data-testid="stBaseButton-primary"], .stApp [data-testid="stFormSubmitButton"] button[kind="primary"],
.stApp button[kind="primary"] {
    background: var(--action) !important; color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important;
    border: 1px solid var(--action) !important; border-radius: 8px !important;
    min-height: 46px; padding: 0.55rem 1.4rem; font-size: 15px !important; font-weight: 600 !important;
    transition: background-color 160ms var(--ease), transform 160ms var(--ease);
}
.stApp button[kind="primary"] *, .stApp button[data-testid="stBaseButton-primary"] * { color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important; }
.stApp button[kind="primary"]:hover, .stApp button[data-testid="stBaseButton-primary"]:hover { background: var(--action-hover) !important; border-color: var(--action-hover) !important; }
.stApp button[kind="primary"]:active { transform: translateY(1px); }
.stApp button[data-testid="stBaseButton-secondary"], .stApp button[kind="secondary"] {
    background: var(--surface) !important; color: var(--ink) !important; border: 1px solid var(--line-strong) !important; border-radius: 8px !important;
    min-height: 44px; font-weight: 600 !important;
}
.stApp button[kind="secondary"] * { color: var(--ink) !important; }
.stApp button[kind="secondary"]:hover { background: var(--surface-2) !important; }
.stApp button:disabled { opacity: 0.55 !important; cursor: not-allowed; }

.stApp [data-testid="stPageLink"] a, .stApp [data-testid="stPageLink-NavLink"] {
    background: transparent !important; border: 1px solid var(--line-strong); border-radius: 8px; padding: 0.5rem 0.9rem;
    color: var(--action) !important; font-weight: 600; text-decoration: none; transition: background-color 160ms var(--ease);
}
.stApp [data-testid="stPageLink"] a *, .stApp [data-testid="stPageLink-NavLink"] * { color: var(--action) !important; font-weight: 600; }
.stApp [data-testid="stPageLink"] a:hover, .stApp [data-testid="stPageLink-NavLink"]:hover { background: #E8EFFA !important; }

.stApp [data-testid="stExpander"] { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; }
.stApp [data-testid="stExpander"] summary, .stApp [data-testid="stExpander"] summary * { color: var(--ink) !important; font-weight: 600; }
.stApp [data-testid="stExpander"] summary:hover { background: var(--ground); }
.stApp [data-testid="stJson"], .stApp [data-testid="stJson"] * { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace !important; font-size: 13px; }

.stApp [data-testid="stAlert"] { border-radius: 10px; }
.stApp [data-testid="stAlert"] p, .stApp [data-testid="stAlert"] div { color: inherit; }
.stApp [data-testid="stAlertContainer"][data-baseweb="notification"], .stApp [data-testid="stAlert"] [data-baseweb="notification"] { border-radius: 10px; }

@media (prefers-reduced-motion: reduce) {
    .scale-fill { animation: none !important; }
    * { transition-duration: 0.01ms !important; }
}
</style>
""")


# --------------------------------------------------
# NAVIGATION RAIL BRANDING
# --------------------------------------------------

render("""
<div class="brand">
    <svg class="brand-mark" viewBox="0 0 34 34" fill="none" stroke="#E6EDF4" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M17 4v11"/>
        <path d="M17 13c-1.6 2.2-3 3.2-5.2 4.2"/>
        <path d="M17 13c1.6 2.2 3 3.2 5.2 4.2"/>
        <path d="M13.6 12.2C9.2 11.4 5 15.6 5 22.4c0 4 2.6 6.4 5.4 5.7 2.8-.7 3.3-3.6 3.3-7.4v-6.4c0-.9-.1-1.8-.1-2.1z"/>
        <path d="M20.4 12.2C24.8 11.4 29 15.6 29 22.4c0 4-2.6 6.4-5.4 5.7-2.8-.7-3.3-3.6-3.3-7.4v-6.4c0-.9.1-1.8.1-2.1z"/>
    </svg>
    <div>
        <div class="brand-name">PulmoLens</div>
        <div class="brand-sub">Respiratory health intelligence</div>
    </div>
</div>
""", container=st.sidebar)


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
# GLOBAL TOP BAR
# --------------------------------------------------

render("""
<div class="topbar">
    <div class="topbar-title"><strong>PulmoLens</strong> <span>&nbsp;·&nbsp; Explainable respiratory health research</span></div>
    <div class="topbar-status">Research system active</div>
</div>
""")


# --------------------------------------------------
# RUN SELECTED PAGE
# --------------------------------------------------

pg.run()