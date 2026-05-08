import streamlit as st

from utils.llm import (
    generate_founder_analysis,
    simulate_strategy,
    generate_investor_analysis,
    generate_vc_questions,
    generate_red_flags,
    generate_action_plan,
)

from utils.visualizations import (
    create_survival_gauge,
    create_pmf_gauge,
    create_risk_radar,
    create_runway_chart,
    create_runway_burn_chart,
    create_startup_dna_radar,
    create_investor_scorecard,
    create_vc_decision_meter,
    create_investor_heatmap,
    create_vc_funnel,
    create_strategy_comparison,
    create_founder_risk_timeline,
)

st.set_page_config(
    page_title="FounderSim AI",
    page_icon="🚀",
    layout="wide",
)

# ---------- SESSION STATE ----------

defaults = {
    "analysis_generated": False,
    "selected_strategy": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------- STYLING ----------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right,#020617,#0f172a,#111827);
    color: white;
}

.block-container {
    padding-top: 2rem;
    max-width: 1500px;
}

.section-title {
    font-size: 2rem;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 10px;
}

.section-subtitle {
    color: #94a3b8;
    margin-bottom: 20px;
}

.hero-card {
    background:
        linear-gradient(
            135deg,
            rgba(59,130,246,0.12),
            rgba(168,85,247,0.12)
        );

    border: 1px solid rgba(148,163,184,0.12);

    border-radius: 24px;

    padding: 35px;

    margin-bottom: 30px;
}

.alert-card {
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 12px;
    font-weight: 600;
}

.critical {
    background-color: rgba(127,29,29,0.35);
    border: 1px solid #ef4444;
}

.warning {
    background-color: rgba(146,64,14,0.35);
    border: 1px solid #f59e0b;
}

.success {
    background-color: rgba(22,101,52,0.35);
    border: 1px solid #22c55e;
}

div[data-testid="stMetric"] {
    background-color: rgba(30,41,59,0.75);
    border: 1px solid rgba(148,163,184,0.15);
    padding: 18px;
    border-radius: 16px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown("""
<h1 style='text-align:center;font-size:4rem;font-weight:800;'>
FounderSim AI
</h1>

<h4 style='text-align:center;color:#94a3b8;font-size:1.4rem;'>
AI Startup Operating System
</h4>
""", unsafe_allow_html=True)

# ---------- HERO ----------

st.markdown("""
<div class="hero-card">

<h2 style="margin-top:0px;">
Founder Intelligence Dashboard
</h2>

<p style="font-size:1.05rem;color:#cbd5e1;line-height:1.8;">

Analyze startup survivability, investor attractiveness,
operational weaknesses, fundraising readiness,
PMF strength, founder risk, and strategic scalability
using AI-powered startup diagnostics.

</p>

</div>
""", unsafe_allow_html=True)

# ---------- INPUT ----------

with st.expander("Founder Intake", expanded=True):

    c1, c2, c3 = st.columns(3)

    with c1:

        startup_name = st.text_input("Startup Name")

        stage = st.selectbox(
            "Startup Stage",
            ["Idea", "MVP", "Seed", "Series A", "Growth"]
        )

        business_model = st.selectbox(
            "Business Model",
            ["B2B", "B2C", "Marketplace", "SaaS", "AI Product"]
        )

        sector = st.text_input("Sector")

    with c2:

        monthly_revenue = st.number_input(
            "Monthly Revenue ($)",
            min_value=0,
            value=10000
        )

        monthly_burn = st.number_input(
            "Monthly Burn ($)",
            min_value=0,
            value=25000
        )

        runway = st.slider(
            "Runway Remaining",
            1,
            36,
            6
        )

        funding_raised = st.number_input(
            "Funding Raised ($)",
            min_value=0,
            value=0
        )

    with c3:

        team_size = st.slider(
            "Team Size",
            1,
            500,
            10
        )

        growth_rate = st.slider(
            "Growth Rate (%)",
            -20,
            150,
            5
        )

        churn = st.slider(
            "Monthly Churn (%)",
            0,
            100,
            5
        )

        competition = st.selectbox(
            "Competition",
            ["Low", "Moderate", "High", "Extreme"]
        )

    st.markdown("## Go-To-Market")

    g1, g2 = st.columns(2)

    with g1:

        acquisition_channel = st.text_input(
            "Acquisition Channel"
        )

        customer_type = st.selectbox(
            "Primary Customer",
            ["SMB", "Enterprise", "Consumer", "Developers"]
        )

    with g2:

        moat = st.text_input(
            "Competitive Advantage"
        )

        competitors = st.text_input(
            "Competitors"
        )

    scenario = st.text_area(
        "Describe your startup situation",
        height=180
    )

# ---------- ANALYZE ----------

if st.button(
    "Run Founder Simulation",
    type="primary",
    use_container_width=True
):

    startup_data = f"""
    Startup: {startup_name}
    Stage: {stage}
    Business Model: {business_model}
    Sector: {sector}
    Revenue: ${monthly_revenue}
    Burn: ${monthly_burn}
    Runway: {runway}
    Funding Raised: ${funding_raised}
    Team Size: {team_size}
    Growth Rate: {growth_rate}
    Churn: {churn}
    Competition: {competition}
    Acquisition: {acquisition_channel}
    Customer: {customer_type}
    Moat: {moat}
    Competitors: {competitors}

    Scenario:
    {scenario}
    """

    st.session_state.startup_data = startup_data

    with st.spinner("Running AI Startup Simulation..."):

        st.session_state.analysis = generate_founder_analysis(
            startup_data
        )

        st.session_state.investor_analysis = generate_investor_analysis(
            startup_data
        )

        st.session_state.red_flags = generate_red_flags(
            startup_data
        )

        st.session_state.vc_questions = generate_vc_questions(
            startup_data
        )

        st.session_state.action_plan = generate_action_plan(
            startup_data
        )

    revenue_burn_ratio = monthly_revenue / max(monthly_burn, 1)

    st.session_state.survival_score = int(
        max(
            5,
            min(
                95,
                runway * 3.5
                + growth_rate * 0.9
                + revenue_burn_ratio * 30
                - churn * 0.7
            )
        )
    )

    st.session_state.investor_score = int(
        max(
            5,
            min(
                95,
                growth_rate * 1.0
                + revenue_burn_ratio * 40
                + runway * 2
                - churn * 0.8
            )
        )
    )

    st.session_state.burnout_score = int(
        max(
            5,
            min(
                95,
                85
                - runway * 2.5
                + (monthly_burn / max(monthly_revenue, 1)) * 12
            )
        )
    )

    st.session_state.market_score = int(
        max(
            10,
            min(
                95,
                growth_rate * 0.9 + 40
            )
        )
    )

    st.session_state.moat_score = int(
        max(
            10,
            min(
                95,
                70 if moat else 35
            )
        )
    )

    st.session_state.execution_score = int(
        max(
            10,
            min(
                95,
                growth_rate * 0.7 + runway * 2
            )
        )
    )

    st.session_state.fundraising_score = int(
        max(
            10,
            min(
                95,
                st.session_state.investor_score + runway
            )
        )
    )

    st.session_state.analysis_generated = True

# ---------- DASHBOARD ----------

if st.session_state.analysis_generated:

    # ---------- KPI STRIP ----------

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric(
            "Survival",
            f"{st.session_state.survival_score}%"
        )

    with m2:
        st.metric(
            "Investor Confidence",
            f"{st.session_state.investor_score}%"
        )

    with m3:
        st.metric(
            "Burnout Risk",
            f"{st.session_state.burnout_score}%"
        )

    with m4:
        st.metric(
            "Fundraising",
            f"{st.session_state.fundraising_score}%"
        )

    # ---------- ALERTS ----------

    st.markdown("""
    <div class="section-subtitle">
    Operational Alerts
    </div>
    """, unsafe_allow_html=True)

    if runway <= 6:

        st.markdown("""
        <div class="alert-card critical">
        ⚠ Runway critically low.
        </div>
        """, unsafe_allow_html=True)

    if churn >= 15:

        st.markdown("""
        <div class="alert-card warning">
        ⚠ Churn threatens PMF stability.
        </div>
        """, unsafe_allow_html=True)

    if st.session_state.investor_score >= 75:

        st.markdown("""
        <div class="alert-card success">
        ✓ Strong investor interest detected.
        </div>
        """, unsafe_allow_html=True)

    # ---------- STARTUP HEALTH ----------

    st.markdown("""
    <div class="section-title">
    Startup Health
    </div>
    <div class="section-subtitle">
    Core startup viability and scalability indicators
    </div>
    """, unsafe_allow_html=True)

    h1, h2, h3 = st.columns(3)

    with h1:

        st.plotly_chart(
            create_survival_gauge(
                st.session_state.survival_score
            ),
            use_container_width=True
        )

    with h2:

        st.plotly_chart(
            create_pmf_gauge(
                st.session_state.market_score
            ),
            use_container_width=True
        )

    with h3:

        st.plotly_chart(
            create_startup_dna_radar(
                st.session_state.market_score,
                st.session_state.moat_score,
                st.session_state.execution_score,
                st.session_state.fundraising_score,
            ),
            use_container_width=True
        )

    # ---------- FINANCIAL STABILITY ----------

    st.markdown("""
    <div class="section-title">
    Financial Stability
    </div>
    """, unsafe_allow_html=True)

    f1, f2 = st.columns(2)

    with f1:

        st.plotly_chart(
            create_runway_chart(
                runway
            ),
            use_container_width=True
        )

    with f2:

        st.plotly_chart(
            create_runway_burn_chart(
                runway
            ),
            use_container_width=True
        )

    # ---------- INVESTOR MODE ----------

    st.markdown("""
    <div class="section-title">
    Investor Mode
    </div>
    """, unsafe_allow_html=True)

    i1, i2 = st.columns(2)

    with i1:

        st.plotly_chart(
            create_vc_decision_meter(
                st.session_state.investor_score
            ),
            use_container_width=True
        )

    with i2:

        st.plotly_chart(
            create_investor_scorecard(
                st.session_state.market_score,
                st.session_state.moat_score,
                st.session_state.survival_score,
                st.session_state.execution_score,
                st.session_state.fundraising_score,
            ),
            use_container_width=True
        )

    i3, i4 = st.columns(2)

    with i3:

        st.plotly_chart(
            create_investor_heatmap(),
            use_container_width=True
        )

    with i4:

        st.plotly_chart(
            create_vc_funnel(),
            use_container_width=True
        )

    # ---------- OPERATIONAL RISK ----------

    st.markdown("""
    <div class="section-title">
    Operational Risk
    </div>
    """, unsafe_allow_html=True)

    o1, o2 = st.columns(2)

    with o1:

        st.plotly_chart(
            create_risk_radar(
                runway,
                growth_rate
            ),
            use_container_width=True
        )

    with o2:

        st.plotly_chart(
            create_founder_risk_timeline(),
            use_container_width=True
        )

    # ---------- STRATEGY LAB ----------

    st.markdown("""
    <div class="section-title">
    Strategy Lab
    </div>
    """, unsafe_allow_html=True)

    st.plotly_chart(
        create_strategy_comparison(),
        use_container_width=True
    )

    # ---------- REPORTS ----------

    st.markdown("""
    <div class="section-title">
    Startup Intelligence Reports
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "Founder Analysis",
        "Investor Analysis",
        "Red Flags",
        "VC Questions",
        "30-Day Action Plan",
    ])

    with tabs[0]:

        with st.container(border=True):
            st.write(st.session_state.analysis)

    with tabs[1]:

        with st.container(border=True):
            st.write(st.session_state.investor_analysis)

    with tabs[2]:

        with st.container(border=True):
            st.write(st.session_state.red_flags)

    with tabs[3]:

        with st.container(border=True):
            st.write(st.session_state.vc_questions)

    with tabs[4]:

        with st.container(border=True):
            st.write(st.session_state.action_plan)