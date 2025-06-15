#!/usr/bin/env python3
"""
ADK Financial Multi-Agent System Startup
Enterprise-grade financial analysis platform using ADK framework
"""
import subprocess
import time
import sys
import os

def start_adk_system():
    print("=" * 80)
    print("🚀 ADK FINANCIAL MULTI-AGENT SYSTEM STARTUP")
    print("=" * 80)
    print("🔧 Framework: Agent Development Kit (ADK) v1.0")
    print("📊 Platform: Enterprise Financial Analysis")
    print("⚡ Features: Multi-agent coordination, Real-time processing, Enterprise intelligence")
    print()
    
    # ADK agent configurations
    adk_agents = [
        {
            "name": "ADK Data Gathering Agent",
            "script": "run_adk_data_gathering_server.py",
            "port": 9001,
            "description": "Enterprise data collection with multi-source integration"
        },
        {
            "name": "ADK Quantitative Analysis Agent", 
            "script": "run_quantitative_analysis_a2a_server.py",
            "port": 9002,
            "description": "Advanced quantitative financial analysis"
        },
        {
            "name": "ADK Qualitative Analysis Agent",
            "script": "run_qualitative_analysis_a2a_server.py", 
            "port": 9003,
            "description": "Comprehensive qualitative market analysis"
        },
        {
            "name": "ADK Report Generation Agent",
            "script": "run_adk_report_generation_server.py",
            "port": 9004,
            "description": "Enterprise-grade report synthesis"
        },
        {
            "name": "ADK Orchestrator Agent",
            "script": "run_adk_orchestrator_server.py",
            "port": 9000,
            "description": "Multi-agent workflow coordination"
        }
    ]
    
    print("🤖 Starting ADK Agent Servers...")
    print()
    
    processes = []
    
    for agent in adk_agents:
        print(f"🚀 Starting {agent['name']} on port {agent['port']}...")
        print(f"   📋 {agent['description']}")
        
        try:
            process = subprocess.Popen([
                sys.executable, agent['script']
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            processes.append(process)
            time.sleep(2)  # Give each agent time to start
            print(f"   ✅ Started successfully")
        except Exception as e:
            print(f"   ❌ Failed to start: {e}")
        
        print()
    
    print("=" * 80)
    print("🎉 ADK FINANCIAL MAS SYSTEM READY!")
    print("=" * 80)
    print()
    print("📊 ADK Agent Endpoints:")
    print("   🎯 ADK Orchestrator Agent: http://localhost:9000/")
    print("   📈 ADK Data Gathering Agent: http://localhost:9001/")
    print("   🔢 ADK Quantitative Analysis Agent: http://localhost:9002/")
    print("   📝 ADK Qualitative Analysis Agent: http://localhost:9003/")
    print("   📋 ADK Report Generation Agent: http://localhost:9004/")
    print()
    print("🌐 Enterprise Features:")
    print("   ⚡ Real-time multi-agent coordination")
    print("   🔧 ADK framework with enterprise capabilities")
    print("   📊 Comprehensive financial analysis workflow")
    print("   🛡️ Enterprise-grade error handling and monitoring")
    print("   🔗 A2A protocol compliance with ADK enhancements")
    print()
    print("🎨 Ultra-Modern Frontend: http://localhost:3000")
    print("🔧 MCP Financial Server: http://localhost:8001")
    print()
    print("📚 ADK Documentation:")
    print("   📖 Agent Info: GET /{agent_port}/adk/info")
    print("   ⚡ Capabilities: GET /{agent_port}/adk/capabilities")
    print("   🔍 Agent Cards: GET /{agent_port}/.well-known/agent.json")
    print()
    print("🛑 To stop all ADK agents, press Ctrl+C")
    print("=" * 80)
    
    try:
        # Keep the main process running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down ADK Financial MAS System...")
        for process in processes:
            process.terminate()
        print("✅ All ADK agents stopped successfully!")

if __name__ == "__main__":
    start_adk_system() 