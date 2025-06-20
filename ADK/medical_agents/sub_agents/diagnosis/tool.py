# diagnosis/tool.py
from typing import Dict
from google.adk.tools import ToolContext

from medical_agents.sub_agents.diagnosis.places_wrapper import PlacesService


# Wrapper to Google Places API to simulate location-based health lookups
places_service = PlacesService()

def analyze_symptoms_or_location(symptom_text: str) -> str:
    """
    Analyzes the user's symptoms and gives a general overview.
    """
    print(f"[TOOL CALL] analyze_symptoms_or_location called with: {symptom_text}")

    text = symptom_text.lower()

    if "fever" in text and "throat" in text:
        return "The symptoms suggest a possible viral or bacterial infection such as flu or strep throat. Please consult a physician for accurate diagnosis."
    elif "rash" in text or "skin" in text:
        return "This may be a dermatological issue. Consider uploading a skin photo for more insights or consult a dermatologist."
    else:
        return "The symptoms are unclear. Could you provide more details or specify affected areas?"
