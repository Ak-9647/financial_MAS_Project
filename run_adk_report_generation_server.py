#!/usr/bin/env python3
"""
ADK-Powered Report Generation A2A Server
Enterprise-grade financial report synthesis using ADK framework
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.adk_report_generation_agent import ADKReportGenerationAgent
from utils.a2a_server import A2AServer

def main():
    # Initialize ADK Report Generation Agent
    adk_report_agent = ADKReportGenerationAgent()
    
    # Enhanced ADK agent card with enterprise metadata
    agent_card = {
        "name": "ADK Financial Report Generation Specialist",
        "description": "Enterprise-grade financial report synthesis using ADK framework",
        "version": "2.0",
        "adk_version": "1.0",
        "capabilities": adk_report_agent.get_capabilities(),
        "enterprise_features": [
            "Comprehensive report synthesis",
            "Investment recommendation engine",
            "Executive summary generation",
            "Risk assessment integration",
            "ADK-powered intelligence"
        ],
        "report_types": [
            "Executive Summary",
            "Investment Recommendation",
            "Financial Highlights",
            "Risk Assessment",
            "Company Analysis"
        ],
        "supported_protocols": ["A2A", "ADK"],
        "enterprise_grade": True
    }
    
    # Create ADK-enhanced A2A server
    server = A2AServer("localhost", 9004, adk_report_agent, agent_card)
    
    print("🚀 Starting ADK-Powered Report Generation A2A Server at http://localhost:9004/")
    print("📊 Enterprise Features: Comprehensive synthesis, Investment intelligence, Executive reporting")
    print("🔧 ADK Version:", adk_report_agent.adk_version)
    print("⚡ Capabilities:", ", ".join(adk_report_agent.get_capabilities()))
    
    server.run()

if __name__ == "__main__":
    main() 