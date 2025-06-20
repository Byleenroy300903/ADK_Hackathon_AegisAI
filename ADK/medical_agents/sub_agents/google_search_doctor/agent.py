from google.adk.agents import Agent
from google.adk.tools import google_search

google_search_doctor_agent = Agent(
    name="GoogleSearchDoctorAgent",
    model="gemini-2.0-flash",  # ✅ This supports tools
    instruction=(
        "Use the Google Search tool to find doctors when a specific specialty is not found in our database. "
        "Search for 'verified mental health professionals near <location>'"
    ),
    description="Agent to fallback using Google Search for doctor lookup.",
    tools=[google_search]  # ✅ tool is enabled
)
