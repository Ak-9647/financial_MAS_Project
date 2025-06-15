#!/usr/bin/env python3
"""
ADK-Powered Orchestrator A2A Server
Enterprise-grade financial analysis orchestration using ADK framework
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.adk_orchestrator_agent import ADKOrchestratorAgent
from utils.a2a_server import A2AServer

def main():
    # Initialize ADK Orchestrator Agent
    adk_orchestrator = ADKOrchestratorAgent()
    
    # Enhanced ADK agent card with enterprise metadata
    agent_card = {
        "name": "ADK Financial Analysis Orchestrator",
        "description": "Enterprise-grade financial analysis coordination using ADK framework",
        "version": "2.0",
        "adk_version": "1.0",
        "capabilities": adk_orchestrator.get_capabilities(),
        "enterprise_features": [
            "Multi-agent workflow coordination",
            "Financial analysis orchestration", 
            "Enterprise data integration",
            "Real-time agent monitoring",
            "ADK-powered intelligence"
        ],
        "endpoints": {
            "analysis": "/",
            "agent_info": "/.well-known/agent.json",
            "adk_info": "/adk/info",
            "capabilities": "/adk/capabilities"
        },
        "supported_protocols": ["A2A", "ADK"],
        "enterprise_grade": True
    }
    
    # Create ADK-enhanced A2A server
    server = A2AServer("localhost", 9000, adk_orchestrator, agent_card)
    
    print("🚀 Starting ADK-Powered Orchestrator A2A Server at http://localhost:9000/")
    print("📊 Enterprise Features: Multi-agent coordination, ADK framework, Real-time monitoring")
    print("🔧 ADK Version:", adk_orchestrator.adk_version)
    print("⚡ Capabilities:", ", ".join(adk_orchestrator.get_capabilities()))
    
    server.run()

if __name__ == "__main__":
    main() 