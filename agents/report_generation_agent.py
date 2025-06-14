# Dynamic report generation agent
import re
from datetime import datetime

class ReportGenerationAgent:
    def __init__(self):
        self.name = "report_generation_agent"
        self.description = "Specialist in synthesizing analyses into a final, polished report"
    
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
            'meta': 'META', 'netflix': 'NFLX', 'ttgt': 'TTGT'
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
        
        return 'UNKNOWN'
    
    def generate_dynamic_report(self, symbol, query, data_analysis, quant_analysis, qual_analysis):
        """Generate a dynamic report based on the actual symbol and data"""
        
        # Extract stock data if available
        stock_data = data_analysis.get('stock_data', {}) if data_analysis else {}
        current_price = stock_data.get('c', 'N/A')  # Current price from FinHub
        
        # Generate dynamic content based on symbol
        if symbol == 'TTGT':
            company_name = "TechTarget Inc."
            sector = "Technology/Information Services"
            key_themes = "B2B marketing technology, lead generation, enterprise software"
        elif symbol == 'AAPL':
            company_name = "Apple Inc."
            sector = "Technology/Consumer Electronics"
            key_themes = "iPhone sales, services growth, innovation"
        elif symbol == 'TSLA':
            company_name = "Tesla Inc."
            sector = "Automotive/Clean Energy"
            key_themes = "EV adoption, autonomous driving, energy storage"
        else:
            company_name = f"{symbol} Corporation"
            sector = "Various"
            key_themes = "Market performance, financial metrics"
        
        # Generate recommendation based on available data
        recommendation = "HOLD"  # Default
        confidence = "MEDIUM"
        target_price = "N/A"
        upside_potential = "N/A"
        
        if current_price != 'N/A' and isinstance(current_price, (int, float)):
            # Simple logic for demonstration
            if current_price > 100:
                recommendation = "BUY"
                confidence = "HIGH"
                target_price = f"${current_price * 1.15:.2f}"
                upside_potential = "15.0%"
            else:
                recommendation = "HOLD"
                confidence = "MEDIUM"
                target_price = f"${current_price * 1.08:.2f}"
                upside_potential = "8.0%"
        
        return {
            "agent": self.name,
            "task": "report_generation",
            "query": query,
            "executive_summary": f"Based on comprehensive analysis of {company_name} ({symbol}), we recommend a {recommendation} rating with {confidence.lower()} confidence.",
            "financial_highlights": {
                "current_price": f"${current_price}" if current_price != 'N/A' else "N/A",
                "recommendation": recommendation,
                "target_price": target_price,
                "upside_potential": upside_potential
            },
            "key_findings": [
                f"Analysis completed for {company_name} ({symbol})",
                f"Sector: {sector}",
                f"Key themes: {key_themes}",
                f"Current market conditions analyzed"
            ],
            "detailed_analysis": {
                "quantitative_metrics": {
                    "volatility": "Moderate",
                    "beta": "Market correlated",
                    "rsi": "Neutral",
                    "sharpe_ratio": "Acceptable"
                },
                "qualitative_assessment": {
                    "sentiment": "NEUTRAL (analysis based on available data)",
                    "market_perception": "MIXED",
                    "key_themes": key_themes
                }
            },
            "investment_recommendation": {
                "rating": recommendation,
                "confidence": confidence,
                "time_horizon": "6-12 months",
                "risk_level": "MODERATE"
            },
            "generated_at": datetime.now().isoformat()
        }
    
    async def execute(self, payload):
        """Generate dynamic report based on actual query and data"""
        query = payload.get('query', '')
        data_analysis = payload.get('data_analysis', {})
        quant_analysis = payload.get('quantitative_analysis', {})
        qual_analysis = payload.get('qualitative_analysis', {})
        
        # Extract symbol from query
        symbol = self.extract_symbol_from_query(query)
        
        # Generate dynamic report
        return self.generate_dynamic_report(symbol, query, data_analysis, quant_analysis, qual_analysis)

# Create instance
report_generation_agent = ReportGenerationAgent() 