# medical_image_analysis/agent.py
from google.adk.agents import Agent

medical_image_analysis_agent = Agent(
    name="MedicalImageAnalysisAgent",
    model="gemini-1.5-flash",  # or gemini-1.5-pro if using image + text reasoning
    instruction=(
        "You're a helpful medical assistant capable of analyzing medical images "
        "(X-rays, scans, reports in image form). You describe key observations in a careful, "
        "non-diagnostic, professional tone. Avoid giving definitive conclusions. "
        "Always encourage the user to consult a doctor for final analysis."
    ),
    description="Analyzes medical images (X-rays, scans, photos of prescriptions, etc.)"
)
