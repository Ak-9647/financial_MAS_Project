from agents.quantitative_analysis_agent import quantitative_analysis_agent
from utils.a2a_server import A2AServer
from utils.card_generator import generate_agent_card

HOST, PORT = "localhost", 9002
URL = f"http://{HOST}:{PORT}/"
SKILLS = [{"name": "perform_statistical_analysis", "description": "Performs statistical calculations on numerical data."}]

if __name__ == "__main__":
    card = generate_agent_card(quantitative_analysis_agent.name, quantitative_analysis_agent.description, URL, SKILLS)
    server = A2AServer(HOST, PORT, quantitative_analysis_agent, card)
    print(f"Starting Quantitative Analysis A2A Server at {URL}")
    server.run() 