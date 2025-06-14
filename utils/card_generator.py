# Simple card generator since we'll use basic dict instead of complex types
def generate_agent_card(name, description, url, skills_list):
    """Generates an agent card dict for A2A discovery."""
    skills = [{"name": s['name'], "description": s['description']} for s in skills_list]
    
    return {
        "name": name,
        "description": description,
        "url": url,
        "version": "1.0.0",
        "defaultInputModes": ["application/json"],
        "defaultOutputModes": ["application/json"],
        "capabilities": {
            "can_stream": False,
            "can_push_notifications": False,
            "can_state_transition_history": True
        },
        "skills": skills
    } 