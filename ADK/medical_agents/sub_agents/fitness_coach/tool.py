from google.adk.tools import tool
from google.adk.types import FunctionCall

@tool()
def suggest_fitness_plan(goal: str) -> FunctionCall:
    """
    Transfer to Fitness Coach agent based on user's exercise goal.
    """
    return FunctionCall(name="transfer_to_agent", args={"agent_name": "FitnessCoachAgent"})
