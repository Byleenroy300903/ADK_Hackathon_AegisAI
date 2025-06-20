# consolidate/agent.py
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from medical_agents.sub_agents.consolidate.prompt import CONSOLIDATE_AGENT_INSTR
from medical_agents.sub_agents.diagnosis.agent import diagnosis_agent
from medical_agents.sub_agents.writer.agent import response_writer_agent
from medical_agents.sub_agents.location_doctor_search.agent import location_doctor_search_agent
from medical_agents.sub_agents.google_search_doctor.agent import google_search_doctor_agent
from medical_agents.sub_agents.addiction_support.agent import addiction_support_agent
from medical_agents.sub_agents.diet_nutrition.agent import diet_nutrition_agent  
from medical_agents.sub_agents.medical_image_analysis.agent import medical_image_analysis_agent

consolidate_agent = Agent(
    model="gemini-2.0-flash",
    name="consolidate_agent",
    description="Coordinates between diagnosis, writing, location search, addiction, and nutrition agents.",
    instruction=CONSOLIDATE_AGENT_INSTR,
    tools=[
        AgentTool(agent=diagnosis_agent),
        AgentTool(agent=response_writer_agent),
        AgentTool(agent=location_doctor_search_agent),
        AgentTool(agent=google_search_doctor_agent),
        AgentTool(agent=addiction_support_agent),
        AgentTool(agent=diet_nutrition_agent),
        AgentTool(agent=medical_image_analysis_agent)   
    ]
)
