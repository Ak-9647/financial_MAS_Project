from agents.qualitative_analysis_agent import qualitative_analysis_agent
from utils.a2a_server import A2AServer
from utils.card_generator import generate_agent_card

HOST, PORT = "localhost", 9003
URL = f"http://{HOST}:{PORT}/"
SKILLS = [{"name": "analyze_sentiment_and_themes", "description": "Analyzes text for sentiment and summarizes key topics."}]

if __name__ == "__main__":
    card = generate_agent_card(qualitative_analysis_agent.name, qualitative_analysis_agent.description, URL, SKILLS)
    server = A2AServer(HOST, PORT, qualitative_analysis_agent, card)
    print(f"Starting Qualitative Analysis A2A Server at {URL}")
    server.run() 