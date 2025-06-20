from google.adk.agents import Agent
from medical_agents.sub_agents.location_doctor_search.tool import search_doctors_near_location
from google.adk.tools import FunctionTool


location_doctor_search_agent = Agent(
    name="LocationDoctorSearchAgent",
    model="gemini-2.0-flash",
    description="Handles user queries related to doctors near a location.",
    instruction="""
        The user might provide a location and an optional specialty.
        Use the `search_doctors_near_location` tool to find doctors.
        If results are not found, gracefully handle and suggest alternatives.
    """,
    tools=[FunctionTool(func=search_doctors_near_location)]
)
