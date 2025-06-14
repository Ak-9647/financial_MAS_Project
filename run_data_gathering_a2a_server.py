from agents.data_gathering_agent import data_gathering_agent
from utils.a2a_server import A2AServer
from utils.card_generator import generate_agent_card

HOST, PORT = "localhost", 9001
URL = f"http://{HOST}:{PORT}/"
SKILLS = [
    {"name": "get_stock_price", "description": "Fetches stock price for a symbol."},
    {"name": "get_company_filings", "description": "Fetches SEC filings for a symbol."},
    {"name": "search_google", "description": "Searches Google for a query."},
    {"name": "get_text_from_page", "description": "Scrapes text from a URL."},
]

if __name__ == "__main__":
    card = generate_agent_card(data_gathering_agent.name, data_gathering_agent.description, URL, SKILLS)
    server = A2AServer(HOST, PORT, data_gathering_agent, card)
    print(f"Starting Data Gathering A2A Server at {URL}")
    server.run() 