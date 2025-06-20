# diagnosis/agent.py
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from medical_agents.sub_agents.diagnosis.tool import analyze_symptoms_or_location


diagnosis_agent = Agent(
    name="diagnosis_agent",
    model="gemini-2.0-flash",
    description="Analyzes symptoms or locations to simulate a health insight for the user.",
    instruction="""
    You are a medical diagnosis assistant. When a user provides symptoms (e.g., 'fever and cough') or a context (e.g., 'pharmacy near Guindy'),
    use the analyze_symptoms_or_location tool to simulate a health check and return a diagnosis or helpful suggestion.
    Always include a disclaimer stating that this is not a medical diagnosis and users should consult a certified doctor.
    """,
    tools=[FunctionTool(func=analyze_symptoms_or_location)]
)
