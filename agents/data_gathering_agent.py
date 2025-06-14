import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.financial_service import FinHubService
from services.web_research_service import SerperDevService
import json
import re

class DataGatheringAgent:
    def __init__(self):
        self.name = "data_gathering_agent"
        self.description = "Specialist in retrieving raw financial and web data"
        self.financial_service = FinHubService()
        self.web_service = SerperDevService()
    
    def extract_symbol_from_query(self, query):
        """Extract stock symbol from query"""
        # Common patterns for stock symbols
        patterns = [
            r'\b([A-Z]{1,5})\b',  # 1-5 uppercase letters
            r'\(([A-Z]{1,5})\)',  # Symbol in parentheses
        ]
        
        # Known company to symbol mappings
        company_symbols = {
            'apple': 'AAPL', 'tesla': 'TSLA', 'nvidia': 'NVDA', 
            'microsoft': 'MSFT', 'google': 'GOOGL', 'amazon': 'AMZN',
            'meta': 'META', 'netflix': 'NFLX'
        }
        
        query_lower = query.lower()
        for company, symbol in company_symbols.items():
            if company in query_lower:
                return symbol
        
        # Try to extract symbol patterns
        for pattern in patterns:
            matches = re.findall(pattern, query.upper())
            if matches:
                return matches[0]
        
        return 'AAPL'  # Default fallback
    
    async def execute(self, payload):
        """Execute data gathering with real API calls"""
        query = payload.get('query', '')
        task = payload.get('task', '')
        symbol = payload.get('symbol', '')
        
        # Extract symbol if not provided
        if not symbol:
            symbol = self.extract_symbol_from_query(query)
        
        result = {
            "agent": self.name,
            "task": "data_gathering",
            "query": query,
            "symbol": symbol
        }
        
        # Handle specific tasks
        if task == 'get_stock_price':
            stock_data = self.financial_service.get_stock_price(symbol)
            result["stock_data"] = stock_data
        else:
            # General data gathering
            # Get stock data
            stock_data = self.financial_service.get_stock_price(symbol)
            result["stock_data"] = stock_data
            
            # Get web search results
            search_query = f"{symbol} stock analysis financial performance"
            search_results = self.web_service.search_google(search_query, 3)
            result["web_research"] = search_results
            
            # Get company filings
            filings = self.financial_service.get_company_filings(symbol, 3)
            result["company_filings"] = filings
        
        return result

# Create instance
data_gathering_agent = DataGatheringAgent() 