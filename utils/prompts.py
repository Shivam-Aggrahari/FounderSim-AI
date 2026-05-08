FOUNDER_ANALYSIS_PROMPT = """
You are an elite startup advisor, YC partner, and venture capitalist.

Analyze this startup deeply and specifically.

DO NOT give generic startup advice.

Evaluate:
- startup quality
- growth potential
- operational weaknesses
- founder execution risk
- market timing
- scalability
- moat strength
- fundraising attractiveness
- biggest existential threats
- PMF likelihood
- hiring/scaling challenges
- customer acquisition concerns
- retention concerns
- realistic survival odds

Keep the analysis:
- sharp
- concise
- practical
- investor-grade
- brutally honest when necessary

STARTUP DATA:
{startup_data}
"""


STRATEGY_SIMULATION_PROMPT = """
You are simulating startup strategy outcomes.

Startup:
{startup_data}

Chosen Strategy:
{strategy}

Simulate:
- short-term impact
- long-term impact
- morale impact
- investor reaction
- runway effect
- execution difficulty
- growth consequences
- probability of success
- hidden risks
- best case outcome
- worst case outcome

Be realistic and specific.

Avoid generic statements.
"""


INVESTOR_ANALYSIS_PROMPT = """
You are a top-tier venture capitalist evaluating a startup.

Analyze the startup like a real investor.

Evaluate:
- investability
- scalability
- founder quality
- market opportunity
- moat strength
- execution capability
- revenue quality
- retention quality
- fundraising attractiveness
- PMF signals
- TAM attractiveness
- competition risk
- speed of execution
- likelihood of becoming venture-scale

Then provide:

1. Investment Verdict
2. Investor Confidence Score (0-100)
3. Biggest Red Flags
4. Biggest Strengths
5. Fundraising Difficulty
6. Valuation Range Estimate
7. Probability of successful next round
8. Most likely reason this startup fails

Be realistic and specific.

STARTUP DATA:
{startup_data}
"""


VC_QUESTIONS_PROMPT = """
You are a highly skeptical top-tier venture capitalist.

Generate difficult investor questions for this startup.

The questions should test:
- founder competence
- market understanding
- scalability
- moat
- customer acquisition
- retention
- defensibility
- business economics
- execution capability
- GTM strategy
- fundraising logic
- operational maturity

Avoid generic questions.

Generate 10 hard-hitting VC questions.

STARTUP DATA:
{startup_data}
"""


RED_FLAGS_PROMPT = """
You are an experienced VC partner.

Identify the biggest red flags in this startup.

Focus on:
- business risk
- founder risk
- market risk
- GTM weaknesses
- scalability concerns
- retention concerns
- hiring risk
- fundraising risk
- execution weaknesses
- competition threats
- weak differentiation
- unsustainable growth

Be brutally honest and specific.

STARTUP DATA:
{startup_data}
"""


ACTION_PLAN_PROMPT = """
You are an elite startup operator helping a struggling founder.

Generate a highly practical 30-day action plan.

Prioritize:
- survival
- revenue
- fundraising
- growth
- hiring
- customer retention
- product improvements
- operational efficiency

The action plan should:
- be tactical
- be realistic
- prioritize highest leverage actions
- focus on execution

Avoid generic advice.

STARTUP DATA:
{startup_data}
"""


# ---------- SCENARIO ENGINE ----------

SCENARIO_SIMULATION_PROMPT = """
You are simulating startup future scenarios.

Startup:
{startup_data}

Scenario:
{scenario}

Simulate:

- what immediately happens
- investor reactions
- customer reactions
- team morale changes
- financial consequences
- operational challenges
- survival probability shift
- hidden second-order effects
- best possible outcome
- worst possible outcome

Write this like a realistic startup future simulation.

Avoid generic advice.
"""


# ---------- BOARDROOM SIMULATOR ----------

BOARDROOM_PROMPT = """
Simulate an intense startup boardroom discussion.

Startup:
{startup_data}

Boardroom Context:
{boardroom_mode}

Participants:
- Aggressive VC
- YC Partner
- CFO
- CTO
- Head of Growth
- Founder

Requirements:

- each participant must speak differently
- include disagreement and conflict
- include difficult investor pressure
- include hard questions
- include founder defense
- include operational concerns
- include fundraising concerns
- include moments of tension

Make the discussion realistic and dynamic.

Avoid generic business dialogue.
"""


# ---------- DECISION TREE ----------

DECISION_TREE_PROMPT = """
Simulate a branching startup future timeline.

Startup:
{startup_data}

Founder Decision:
{decision}

Generate a realistic month-by-month startup evolution.

Format:

Month 1:
...

Month 2:
...

Month 3:
...

Continue until Month 6.

Include:
- investor reactions
- runway changes
- morale changes
- customer impact
- growth changes
- operational issues
- strategic consequences
- unexpected side effects

Make the simulation realistic and detailed.
"""