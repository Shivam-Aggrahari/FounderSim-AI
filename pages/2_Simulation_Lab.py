import streamlit as st

from utils.llm import (
    generate_scenario_simulation,
    generate_boardroom_simulation,
    generate_decision_tree,
)

from utils.visualizations import (
    create_survival_gauge,
    create_pmf_gauge,
    create_strategy_comparison,
    create_founder_risk_timeline,
)

st.set_page_config(
    page_title="Simulation Lab",
    page_icon="🧪",
    layout="wide",
)

# ---------- STYLING ----------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right,#020617,#0f172a,#111827);
    color: white;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
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

.sim-card {
    background: rgba(30,41,59,0.75);
    border: 1px solid rgba(148,163,184,0.15);
    border-radius: 18px;
    padding: 20px;
}

.persona-card {
    background: rgba(30,41,59,0.65);
    border: 1px solid rgba(148,163,184,0.12);
    border-radius: 16px;
    padding: 16px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown("""
<h1 style='text-align:center;font-size:3rem;'>
Simulation Lab
</h1>

<h4 style='text-align:center;color:#94a3b8;'>
Scenario Engine • AI Boardroom • Future Timeline Simulator
</h4>
""", unsafe_allow_html=True)

# ---------- STARTUP CONTEXT ----------

if "startup_data" not in st.session_state:

    st.warning(
        "Please run a startup simulation first in Command Center."
    )

    st.stop()

startup_data = st.session_state.startup_data

# ---------- TABS ----------

tabs = st.tabs([
    "Scenario Engine",
    "AI Boardroom",
    "Decision Tree Simulator",
])

# =========================================================
# SCENARIO ENGINE
# =========================================================

with tabs[0]:

    st.markdown("""
    <div class="section-title">
    Startup Scenario Engine
    </div>

    <div class="section-subtitle">
    Simulate market shocks, growth spikes, and startup crises
    </div>
    """, unsafe_allow_html=True)

    scenario_options = [
        "Recession Hits Market",
        "Competitor Raises $50M",
        "Viral Growth Spike",
        "AWS Outage",
        "Cofounder Leaves",
        "Failed Fundraising Round",
        "Major Enterprise Customer Signs",
    ]

    selected_scenario = st.selectbox(
        "Choose Scenario",
        scenario_options
    )

    if st.button(
        "Run Scenario Simulation",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("Simulating startup future..."):

            scenario_result = generate_scenario_simulation(
                startup_data,
                selected_scenario
            )

        base_survival = st.session_state.get(
            "survival_score",
            60
        )

        base_pmf = st.session_state.get(
            "market_score",
            60
        )

        impact_map = {

            "Recession Hits Market": -18,
            "Competitor Raises $50M": -12,
            "Viral Growth Spike": +25,
            "AWS Outage": -15,
            "Cofounder Leaves": -22,
            "Failed Fundraising Round": -28,
            "Major Enterprise Customer Signs": +18,
        }

        delta = impact_map[selected_scenario]

        adjusted_survival = max(
            0,
            min(
                100,
                base_survival + delta
            )
        )

        adjusted_pmf = max(
            0,
            min(
                100,
                base_pmf + delta * 0.6
            )
        )

        # ---------- KPI STRIP ----------

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric(
                "Survival Impact",
                f"{adjusted_survival}%",
                delta=delta
            )

        with m2:
            st.metric(
                "PMF Shift",
                f"{adjusted_pmf}%"
            )

        with m3:
            st.metric(
                "Scenario Severity",
                abs(delta)
            )

        # ---------- VISUALS ----------

        v1, v2 = st.columns(2)

        with v1:

            st.plotly_chart(
                create_survival_gauge(
                    adjusted_survival
                ),
                use_container_width=True
            )

        with v2:

            st.plotly_chart(
                create_pmf_gauge(
                    adjusted_pmf
                ),
                use_container_width=True
            )

        st.plotly_chart(
            create_founder_risk_timeline(),
            use_container_width=True
        )

        # ---------- AI OUTPUT ----------

        with st.container(border=True):

            st.write(scenario_result)

# =========================================================
# BOARDROOM
# =========================================================

with tabs[1]:

    st.markdown("""
    <div class="section-title">
    AI Boardroom Simulator
    </div>

    <div class="section-subtitle">
    Simulated investor conflict, pressure, and executive discussion
    </div>
    """, unsafe_allow_html=True)

    # ---------- PERSONAS ----------

    p1, p2, p3, p4, p5 = st.columns(5)

    personas = [
        ("Aggressive VC", "High Pressure"),
        ("YC Partner", "Strategic"),
        ("CFO", "Financial Risk"),
        ("CTO", "Execution"),
        ("Growth Lead", "Scaling"),
    ]

    cols = [p1, p2, p3, p4, p5]

    for col, persona in zip(cols, personas):

        with col:

            st.markdown(f"""
            <div class="persona-card">
            <h4>{persona[0]}</h4>
            <p>{persona[1]}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    boardroom_mode = st.selectbox(
        "Boardroom Scenario",
        [
            "Emergency Runway Meeting",
            "Series A Pitch",
            "Downround Discussion",
            "Founder Performance Review",
            "Growth Crisis",
        ]
    )

    if st.button(
        "Start Boardroom Simulation",
        use_container_width=True
    ):

        with st.spinner("Running boardroom simulation..."):

            boardroom_result = generate_boardroom_simulation(
                startup_data,
                boardroom_mode
            )

        with st.container(border=True):

            st.write(boardroom_result)

# =========================================================
# DECISION TREE
# =========================================================

with tabs[2]:

    st.markdown("""
    <div class="section-title">
    Decision Tree Simulator
    </div>

    <div class="section-subtitle">
    Explore branching startup futures and strategic outcomes
    </div>
    """, unsafe_allow_html=True)

    decision = st.selectbox(
        "Founder Decision",
        [
            "Raise Aggressive Round",
            "Cut Burn Immediately",
            "Pivot Product",
            "Expand Team Rapidly",
            "Focus on Enterprise",
            "Double Down on Growth",
        ]
    )

    if st.button(
        "Generate Future Timeline",
        use_container_width=True
    ):

        with st.spinner("Projecting startup future..."):

            decision_result = generate_decision_tree(
                startup_data,
                decision
            )

        # ---------- STRATEGY VISUAL ----------

        st.plotly_chart(
            create_strategy_comparison(),
            use_container_width=True
        )

        # ---------- TIMELINE ----------

        st.plotly_chart(
            create_founder_risk_timeline(),
            use_container_width=True
        )

        # ---------- AI OUTPUT ----------

        with st.container(border=True):

            st.write(decision_result)