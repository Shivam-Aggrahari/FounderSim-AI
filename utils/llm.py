import os

from dotenv import load_dotenv
from openai import OpenAI

from utils.prompts import (
    FOUNDER_ANALYSIS_PROMPT,
    STRATEGY_SIMULATION_PROMPT,
    INVESTOR_ANALYSIS_PROMPT,
    VC_QUESTIONS_PROMPT,
    RED_FLAGS_PROMPT,
    ACTION_PLAN_PROMPT,
    SCENARIO_SIMULATION_PROMPT,
    BOARDROOM_PROMPT,
    DECISION_TREE_PROMPT,
)

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL_NAME = "openai/gpt-3.5-turbo"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

# ---------- CORE RESPONSE ----------

def generate_response(prompt: str):

    try:

        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1400,
        )

        return completion.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"

# ---------- FOUNDER ANALYSIS ----------

def generate_founder_analysis(
    startup_data: str
):

    prompt = FOUNDER_ANALYSIS_PROMPT.format(
        startup_data=startup_data
    )

    return generate_response(prompt)

# ---------- STRATEGY SIMULATION ----------

def simulate_strategy(
    startup_data: str,
    strategy: str
):

    prompt = STRATEGY_SIMULATION_PROMPT.format(
        startup_data=startup_data,
        strategy=strategy
    )

    return generate_response(prompt)

# ---------- INVESTOR ANALYSIS ----------

def generate_investor_analysis(
    startup_data: str
):

    prompt = INVESTOR_ANALYSIS_PROMPT.format(
        startup_data=startup_data
    )

    return generate_response(prompt)

# ---------- VC QUESTIONS ----------

def generate_vc_questions(
    startup_data: str
):

    prompt = VC_QUESTIONS_PROMPT.format(
        startup_data=startup_data
    )

    return generate_response(prompt)

# ---------- RED FLAGS ----------

def generate_red_flags(
    startup_data: str
):

    prompt = RED_FLAGS_PROMPT.format(
        startup_data=startup_data
    )

    return generate_response(prompt)

# ---------- ACTION PLAN ----------

def generate_action_plan(
    startup_data: str
):

    prompt = ACTION_PLAN_PROMPT.format(
        startup_data=startup_data
    )

    return generate_response(prompt)

# ---------- SCENARIO ENGINE ----------

def generate_scenario_simulation(
    startup_data: str,
    scenario: str
):

    prompt = SCENARIO_SIMULATION_PROMPT.format(
        startup_data=startup_data,
        scenario=scenario
    )

    return generate_response(prompt)

# ---------- BOARDROOM SIMULATOR ----------

def generate_boardroom_simulation(
    startup_data: str,
    boardroom_mode: str
):

    prompt = BOARDROOM_PROMPT.format(
        startup_data=startup_data,
        boardroom_mode=boardroom_mode
    )

    return generate_response(prompt)

# ---------- DECISION TREE ----------

def generate_decision_tree(
    startup_data: str,
    decision: str
):

    prompt = DECISION_TREE_PROMPT.format(
        startup_data=startup_data,
        decision=decision
    )

    return generate_response(prompt)