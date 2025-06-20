# main.py
from google.adk.agents import Agent
from medical_agents.sub_agents.consolidate.agent import consolidate_agent  # renamed for medical context
from medical_agents.prompt import ROOT_AGENT_INSTR  # your medical-specific root instruction
from medical_agents.sub_agents.location_doctor_search.agent import location_doctor_search_agent
from medical_agents.sub_agents.google_search_doctor import google_search_doctor_agent
from medical_agents.sub_agents.counseling.agent import counseling_agent
from medical_agents.sub_agents.fitness_coach.agent import fitness_coach_agent
from medical_agents.sub_agents.addiction_support.agent import addiction_support_agent
from medical_agents.sub_agents.diet_nutrition.agent import diet_nutrition_agent



root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="An AI-based medical assistant that collects symptoms, scans medical files, and helps route users to care",
    instruction=ROOT_AGENT_INSTR,
    sub_agents=[
        consolidate_agent,
        location_doctor_search_agent,google_search_doctor_agent,
        counseling_agent,
        fitness_coach_agent,
        addiction_support_agent,
        diet_nutrition_agent
    ]
)
