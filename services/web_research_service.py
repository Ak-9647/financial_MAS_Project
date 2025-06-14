import os
import json
import requests
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SerperDevService:
    """A service to interact with the Serper.dev search API."""
    def __init__(self):
        self.api_key = os.getenv("SERPER_DEV_API_KEY")
        if not self.api_key:
            raise ValueError("SERPER_DEV_API_KEY environment variable not set.")
        self.search_url = "https://google.serper.dev/search"
        self.scraper_url = "https://scrape.serper.dev"

    def search_google(self, query: str, n_results: int = 5) -> List:
        payload = json.dumps({"q": query, "num": n_results})
        headers = {'X-API-KEY': self.api_key, 'Content-Type': 'application/json'}
        try:
            response = requests.post(self.search_url, headers=headers, data=payload)
            response.raise_for_status()
            return response.json().get('organic', [])
        except requests.RequestException as e:
            # Return mock search results when API fails
            return [
                {
                    "title": f"Mock Search Result for: {query}",
                    "link": "https://example.com/mock-result-1",
                    "snippet": f"This is a mock search result for '{query}'. Real search requires valid Serper.dev API key.",
                    "note": "Mock data - check API key"
                },
                {
                    "title": f"Financial Analysis: {query}",
                    "link": "https://example.com/mock-result-2", 
                    "snippet": f"Mock financial analysis content related to {query}.",
                    "note": "Mock data - check API key"
                },
                {
                    "error": f"API request failed: {e}",
                    "message": "Using mock data - please check your Serper.dev API key"
                }
            ]

    def get_text_from_page(self, url_to_scrape: str) -> str:
        payload = json.dumps({"url": url_to_scrape})
        headers = {'X-API-KEY': self.api_key, 'Content-Type': 'application/json'}
        try:
            response = requests.post(self.scraper_url, headers=headers, data=payload)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            return f"Error scraping page: {e}" 