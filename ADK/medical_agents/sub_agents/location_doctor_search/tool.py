def search_doctors_near_location(location: str, specialty: str = ""):
    if not specialty.strip():
        return {
            "__tool__": "transfer_to_agent",
            "agent_name": "GoogleSearchDoctorAgent"
        }

    # Otherwise proceed with actual API or DB logic
    ...
