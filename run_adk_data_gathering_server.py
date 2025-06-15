#!/usr/bin/env python3
"""
ADK-Powered Data Gathering A2A Server
Enterprise-grade financial data collection using ADK framework
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.adk_data_gathering_agent import ADKDataGatheringAgent
from utils.a2a_server import A2AServer

def main():
    # Initialize ADK Data Gathering Agent
    adk_data_agent = ADKDataGatheringAgent()
    
    # Enhanced ADK agent card with enterprise metadata
    agent_card = {
        "name": "ADK Financial Data Gathering Specialist",
        "description": "Enterprise-grade financial data collection using ADK framework",
        "version": "2.0",
        "adk_version": "1.0",
        "capabilities": adk_data_agent.get_capabilities(),
        "enterprise_features": [
            "Multi-source data integration",
            "Real-time financial data processing",
            "Enterprise symbol intelligence",
            "Market context analysis",
            "ADK-powered data validation"
        ],
        "data_sources": [
            "MCP Financial Server",
            "Market Data Providers",
            "Enterprise Data Registry",
            "Real-time APIs"
        ],
        "supported_protocols": ["A2A", "ADK", "MCP"],
        "enterprise_grade": True
    }
    
    # Create ADK-enhanced A2A server
    server = A2AServer("localhost", 9001, adk_data_agent, agent_card)
    
    print("🚀 Starting ADK-Powered Data Gathering A2A Server at http://localhost:9001/")
    print("📊 Enterprise Features: Multi-source integration, Symbol intelligence, Real-time processing")
    print("🔧 ADK Version:", adk_data_agent.adk_version)
    print("⚡ Capabilities:", ", ".join(adk_data_agent.get_capabilities()))
    
    server.run()

if __name__ == "__main__":
    main() 