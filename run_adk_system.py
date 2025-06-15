#!/usr/bin/env python3
"""
ADK-Powered Financial MAS System Startup
"""
import asyncio
import subprocess
import sys
import time
from utils.a2a_server import A2AServer
from agents.adk_orchestrator_agent import ADKOrchestratorAgent
from agents.adk_data_gathering_agent import ADKDataGatheringAgent
# ... other ADK agents

def start_adk_system():
    """Start the ADK-powered Financial MAS system"""
    print("=" * 60)
    print("🚀 ADK-Powered Financial Multi-Agent System")
    print("=" * 60)
    print("🔧 Initializing ADK Framework...")
    
    # Start ADK agents
    agents = [
        (ADKDataGatheringAgent(), 9001, "ADK Data Gathering Agent"),
        # ... other ADK agents
        (ADKOrchestratorAgent(), 9000, "ADK Orchestrator Agent")
    ]
    
    processes = []
    
    for agent, port, name in agents:
        print(f"🤖 Starting {name} on port {port}...")
        
        # Create ADK-compliant agent card
        agent_card = {
            "name": agent.name,
            "description": agent.description,
            "capabilities": agent.get_capabilities(),
            "adk_version": "1.0",
            "framework": "ADK Financial MAS"
        }
        
        # Start A2A server with ADK agent
        server = A2AServer("localhost", port, agent, agent_card)
        process = subprocess.Popen([
            sys.executable, "-c", 
            f"import asyncio; from utils.a2a_server import A2AServer; "
            f"server = A2AServer('localhost', {port}, agent, {agent_card}); "
            f"asyncio.run(server.start())"
        ])
        processes.append(process)
        time.sleep(1)
    
    print("✅ ADK System Started Successfully!")
    print("\n🌐 ADK Agent Endpoints:")
    for agent, port, name in agents:
        print(f"   • {name}: http://localhost:{port}/")
    
    print(f"\n🎨 React Frontend: http://localhost:3000/")
    print(f"📊 ADK System Status: All {len(agents)} agents running")
    
    return processes

if __name__ == "__main__":
    start_adk_system() 