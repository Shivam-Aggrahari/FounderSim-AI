import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# ---------- SURVIVAL GAUGE ----------

def create_survival_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Startup Survival"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 35], 'color': "#7f1d1d"},
                {'range': [35, 70], 'color': "#92400e"},
                {'range': [70, 100], 'color': "#166534"},
            ],
            'bar': {'color': "#60a5fa"}
        }
    ))

    fig.update_layout(
        paper_bgcolor="#0f172a",
        font_color="white",
        height=350,
    )

    return fig


# ---------- PMF GAUGE ----------

def create_pmf_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "PMF Probability"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 40], 'color': "#7f1d1d"},
                {'range': [40, 75], 'color': "#92400e"},
                {'range': [75, 100], 'color': "#166534"},
            ],
            'bar': {'color': "#818cf8"}
        }
    ))

    fig.update_layout(
        paper_bgcolor="#0f172a",
        font_color="white",
        height=350,
    )

    return fig


# ---------- STARTUP DNA RADAR ----------

def create_startup_dna_radar(
    growth_score,
    moat_score,
    execution_score,
    fundraising_score,
):

    categories = [
        "Growth",
        "Moat",
        "Execution",
        "Fundraising",
        "Distribution",
        "Product",
        "Speed",
    ]

    values = [
        growth_score,
        moat_score,
        execution_score,
        fundraising_score,
        growth_score * 0.9,
        moat_score * 0.8,
        execution_score * 1.1,
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Startup DNA'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=500,
    )

    return fig


# ---------- RISK RADAR ----------

def create_risk_radar(runway, growth):

    categories = [
        "Financial",
        "Hiring",
        "Operational",
        "Market",
        "Product",
        "Competition"
    ]

    financial_risk = max(15, 100 - runway * 4)

    market_risk = max(10, 100 - growth)

    competition_risk = 75

    values = [
        financial_risk,
        60,
        55,
        market_risk,
        35,
        competition_risk
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Risk Profile'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=500,
    )

    return fig


# ---------- RUNWAY CHART ----------

def create_runway_chart(runway):

    months = []
    cash = []

    remaining = 100

    for month in range(runway + 1):

        months.append(f"M{month}")

        cash.append(remaining)

        remaining -= int(100 / runway)

        if remaining < 0:
            remaining = 0

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=months,
        y=cash,
        mode='lines+markers',
        fill='tozeroy',
        name='Cash Remaining'
    ))

    fig.update_layout(
        title="Projected Runway",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=420,
    )

    return fig


# ---------- RUNWAY VS BURN ----------

def create_runway_burn_chart(runway):

    months = []
    runway_values = []
    burn_values = []

    runway_remaining = runway

    for month in range(12):

        months.append(f"Month {month+1}")

        runway_values.append(max(runway_remaining, 0))

        burn_values.append(100 - month * 6)

        runway_remaining -= 1

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=months,
        y=runway_values,
        mode='lines+markers',
        name='Runway'
    ))

    fig.add_trace(go.Scatter(
        x=months,
        y=burn_values,
        mode='lines+markers',
        name='Burn Pressure'
    ))

    fig.update_layout(
        title="Runway vs Burn Pressure",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=420,
    )

    return fig


# ---------- INVESTOR SCORECARD ----------

def create_investor_scorecard(
    market_score,
    moat_score,
    growth_score,
    execution_score,
    fundraising_score,
):

    categories = [
        "Market",
        "Moat",
        "Growth",
        "Execution",
        "Fundraising"
    ]

    values = [
        market_score,
        moat_score,
        growth_score,
        execution_score,
        fundraising_score
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Investor Evaluation'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=500,
    )

    return fig


# ---------- VC DECISION METER ----------

def create_vc_decision_meter(score):

    if score >= 75:
        verdict = "INVEST"

    elif score >= 50:
        verdict = "MAYBE"

    else:
        verdict = "PASS"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': f"VC Decision: {verdict}"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 50], 'color': "#7f1d1d"},
                {'range': [50, 75], 'color': "#92400e"},
                {'range': [75, 100], 'color': "#166534"},
            ],
            'bar': {'color': "#818cf8"}
        }
    ))

    fig.update_layout(
        paper_bgcolor="#0f172a",
        font_color="white",
        height=400,
    )

    return fig


# ---------- INVESTOR HEATMAP ----------

def create_investor_heatmap():

    data = pd.DataFrame({
        "Category": [
            "Market",
            "Moat",
            "Growth",
            "Execution",
            "Retention",
            "Fundraising"
        ],
        "Score": [
            75,
            62,
            81,
            68,
            55,
            73
        ]
    })

    fig = px.density_heatmap(
        data,
        x="Category",
        y="Score",
    )

    fig.update_layout(
        title="Investor Risk Heatmap",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=350,
    )

    return fig


# ---------- VC FUNNEL ----------

def create_vc_funnel():

    stages = [
        "VC Outreach",
        "Intro Calls",
        "Partner Meetings",
        "Due Diligence",
        "Term Sheets"
    ]

    values = [100, 30, 12, 5, 1]

    fig = go.Figure(go.Funnel(
        y=stages,
        x=values
    ))

    fig.update_layout(
        title="Fundraising Funnel",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=450,
    )

    return fig


# ---------- STRATEGY COMPARISON ----------

def create_strategy_comparison():

    strategies = [
        "Cut Costs",
        "Layoffs",
        "Raise Funding",
        "Pivot",
        "Aggressive Growth"
    ]

    survival = [72, 78, 88, 68, 52]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=strategies,
        y=survival,
        name="Survival Impact"
    ))

    fig.update_layout(
        title="Strategy Comparison",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=450,
    )

    return fig


# ---------- FOUNDER RISK TIMELINE ----------

def create_founder_risk_timeline():

    months = [
        "Month 1",
        "Month 2",
        "Month 3",
        "Month 4",
        "Month 5",
        "Month 6",
    ]

    burnout = [45, 52, 60, 68, 74, 81]

    execution = [80, 74, 69, 61, 55, 49]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=months,
        y=burnout,
        mode='lines+markers',
        name='Burnout Risk'
    ))

    fig.add_trace(go.Scatter(
        x=months,
        y=execution,
        mode='lines+markers',
        name='Execution Capacity'
    ))

    fig.update_layout(
        title="Founder Risk Timeline",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        height=450,
    )

    return fig