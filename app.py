import streamlit as st

st.set_page_config(
    page_title="FounderSim AI",
    page_icon="🚀",
    layout="wide",
)

# ---------- STYLING ----------

st.markdown("""
<style>

.stApp {
    background:
        linear-gradient(
            to bottom right,
            #020617,
            #0f172a,
            #111827
        );

    color: white;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
}

.hero-title {
    text-align: center;
    font-size: 5rem;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero-subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1.5rem;
    margin-bottom: 50px;
}

.hero-card {
    background:
        linear-gradient(
            135deg,
            rgba(59,130,246,0.12),
            rgba(168,85,247,0.12)
        );

    border: 1px solid rgba(148,163,184,0.15);

    border-radius: 28px;

    padding: 50px;

    margin-bottom: 50px;
}

.metric-card {
    background: rgba(30,41,59,0.72);

    border:
        1px solid rgba(148,163,184,0.12);

    border-radius: 22px;

    padding: 30px;

    text-align: center;
}

.metric-number {
    font-size: 3rem;
    font-weight: 800;
}

.metric-label {
    color: #94a3b8;
    margin-top: 10px;
}

.feature-card {

    background:
        rgba(30,41,59,0.7);

    border:
        1px solid rgba(148,163,184,0.12);

    border-radius: 22px;

    padding: 30px;

    min-height: 300px;
}

.feature-title {
    font-size: 1.6rem;
    font-weight: 700;
    margin-bottom: 18px;
}

.feature-text {
    color: #cbd5e1;
    line-height: 1.8;
}

.section-title {
    font-size: 2.5rem;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 20px;
    text-align: center;
}

.big-banner {

    background:
        linear-gradient(
            135deg,
            rgba(59,130,246,0.16),
            rgba(168,85,247,0.16)
        );

    border-radius: 30px;

    padding: 60px;

    text-align: center;

    margin-top: 60px;
}

.footer {
    text-align:center;
    color:#94a3b8;
    margin-top:50px;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------

st.markdown("""
<div class="hero-title">
FounderSim AI
</div>

<div class="hero-subtitle">
AI Startup Operating System
</div>
""", unsafe_allow_html=True)

# ---------- MAIN HERO ----------

st.markdown("""
<div class="hero-card">

<h1>
Simulate Startup Survival Before Reality Does.
</h1>

<br>

<p style="font-size:1.15rem;color:#cbd5e1;line-height:1.9;">

FounderSim AI is an AI-powered startup simulation platform that helps founders:

• predict startup survivability

• simulate investor pressure

• stress-test strategic decisions

• model fundraising outcomes

• forecast operational risk

• analyze PMF strength

• explore branching startup futures

<br>

Built for:
founders,
accelerators,
VCs,
startup operators,
and startup analysts.

</p>

</div>
""", unsafe_allow_html=True)

# ---------- METRICS ----------

m1, m2, m3, m4 = st.columns(4)

metrics = [
    ("25+", "Startup Signals"),
    ("7", "Scenario Engines"),
    ("5", "Boardroom Personas"),
    ("AI", "Strategic Intelligence"),
]

cols = [m1, m2, m3, m4]

for col, metric in zip(cols, metrics):

    with col:

        st.markdown(f"""
        <div class="metric-card">

        <div class="metric-number">
        {metric[0]}
        </div>

        <div class="metric-label">
        {metric[1]}
        </div>

        </div>
        """, unsafe_allow_html=True)

# ---------- FEATURES ----------

st.markdown("""
<div class="section-title">
Core Systems
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    🧠 Command Center
    </div>

    <div class="feature-text">

    Advanced startup diagnostics dashboard.

    Analyze:

    • startup survivability

    • PMF strength

    • investor confidence

    • founder burnout risk

    • fundraising readiness

    • runway sustainability

    • operational weaknesses

    • growth scalability

    </div>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    🧪 Simulation Lab
    </div>

    <div class="feature-text">

    AI-powered startup future simulator.

    Run simulations for:

    • recessions

    • failed fundraising rounds

    • cofounder departures

    • viral growth spikes

    • enterprise expansion

    • competitor funding events

    • aggressive scaling strategies

    </div>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

c3, c4 = st.columns(2)

with c3:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    🏛 AI Boardroom
    </div>

    <div class="feature-text">

    Experience realistic investor pressure.

    Includes:

    • hostile VC questioning

    • YC-style discussions

    • emergency runway meetings

    • founder defense simulation

    • investor skepticism analysis

    • executive pressure dynamics

    </div>

    </div>
    """, unsafe_allow_html=True)

with c4:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    🌳 Decision Tree Engine
    </div>

    <div class="feature-text">

    Explore branching startup futures.

    Simulate:

    • growth vs profitability

    • hiring expansion

    • burn reduction

    • pivots

    • fundraising choices

    • enterprise transition

    • long-term startup evolution

    </div>

    </div>
    """, unsafe_allow_html=True)

# ---------- BIG CTA ----------

st.markdown("""
<div class="big-banner">

<h1>
Navigate using the sidebar →
</h1>

<br>

<h3 style="color:#cbd5e1;">

Open:
• Command Center
• Simulation Lab

to begin startup simulation.

</h3>

</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------

st.markdown("""
<div class="footer">

Built with Streamlit • OpenRouter • Plotly • LLMs

</div>
""", unsafe_allow_html=True)