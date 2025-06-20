import os
from typing import Dict, List, Any
import requests


class PlacesService:
    """Wrapper to Google Places API for verifying or enriching medical data."""
    
    def __init__(self):
        self.places_api_key = os.getenv("GOOGLE_PLACES_API_KEY")

    def find_place_from_text(self, query: str) -> Dict[str, Any]:
        """Find place details using Google Places API."""
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        params = {
            "input": query,
            "inputtype": "textquery",
            "fields": "place_id,name,formatted_address,geometry",
            "key": self.places_api_key
        }

        try:
            res = requests.get(url, params=params)
            res.raise_for_status()
            data = res.json()

            if not data.get("candidates"):
                return {"error": "No match found for place query."}

            place = data["candidates"][0]
            return {
                "place_id": place.get("place_id"),
                "place_name": place.get("name"),
                "place_address": place.get("formatted_address"),
                "lat": place["geometry"]["location"]["lat"],
                "lng": place["geometry"]["location"]["lng"]
            }

        except Exception as e:
            return {"error": f"Google Places API Error: {e}"}
