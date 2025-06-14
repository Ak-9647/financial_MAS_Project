from agents.report_generation_agent import report_generation_agent
from utils.a2a_server import A2AServer
from utils.card_generator import generate_agent_card

HOST, PORT = "localhost", 9004
URL = f"http://{HOST}:{PORT}/"
SKILLS = [
    {"name": "synthesize_report", "description": "Compiles analyses into a final report."},
    {"name": "query_knowledge_base", "description": "Retrieves context from the vector DB."}
]

if __name__ == "__main__":
    card = generate_agent_card(report_generation_agent.name, report_generation_agent.description, URL, SKILLS)
    server = A2AServer(HOST, PORT, report_generation_agent, card)
    print(f"Starting Report Generation A2A Server at {URL}")
    server.run() 