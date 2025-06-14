from agents.orchestrator_agent import orchestrator_agent
from utils.a2a_server import A2AServer
from utils.card_generator import generate_agent_card

HOST, PORT = "localhost", 9000
URL = f"http://{HOST}:{PORT}/"
SKILLS = [{"name": "financial_research", "description": "Conducts comprehensive financial research on companies by orchestrating a team of specialist agents."}]

if __name__ == "__main__":
    card = generate_agent_card(orchestrator_agent.name, orchestrator_agent.description, URL, SKILLS)
    server = A2AServer(HOST, PORT, orchestrator_agent, card)
    print(f"Starting Orchestrator A2A Server at {URL}")
    server.run() 