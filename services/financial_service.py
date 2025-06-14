import os
import finnhub
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class FinHubService:
    """A service to interact with the Finnhub API."""
    def __init__(self):
        self.api_key = os.getenv("FINNHUB_API_KEY")
        if not self.api_key:
            raise ValueError("FINNHUB_API_KEY environment variable not set.")
        self.client = finnhub.Client(api_key=self.api_key)

    def get_stock_price(self, symbol: str) -> Dict[str, Any]:
        try:
            resp = self.client.quote(symbol)
            # Check if we got a valid response
            if resp.get('c') is None:
                return {
                    "error": f"No data available for {symbol}. Check if API key is valid and symbol exists.",
                    "mock_data": {
                        'symbol': symbol,
                        'current_price': 150.0,
                        'change': 2.5,
                        'percentage_change': 1.69,
                        'day_high': 152.0,
                        'day_low': 148.0,
                        'previous_close_price': 147.5,
                        'note': 'Using mock data - check API key'
                    }
                }
            return {
                'current_price': resp.get('c'),
                'change': resp.get('d'),
                'percentage_change': resp.get('dp'),
                'day_high': resp.get('h'),
                'day_low': resp.get('l'),
                'previous_close_price': resp.get('pc'),
            }
        except Exception as e:
            return {
                "error": f"Failed to fetch stock price for {symbol}: {e}",
                "mock_data": {
                    'symbol': symbol,
                    'current_price': 150.0,
                    'change': 2.5,
                    'percentage_change': 1.69,
                    'day_high': 152.0,
                    'day_low': 148.0,
                    'previous_close_price': 147.5,
                    'note': 'Using mock data due to API error'
                }
            }

    def get_company_filings(self, symbol: str, limit: int = 5) -> list:
        try:
            filings = self.client.filings(symbol=symbol)
            return filings[:limit]
        except Exception as e:
            return [{"error": f"Failed to fetch filings for {symbol}: {e}"}] 