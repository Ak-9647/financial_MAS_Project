#!/usr/bin/env python3
"""
Financial MAS System Startup Script
This script starts all the agents in the correct order.
"""

import subprocess
import time
import sys
import os

def start_agent(script_name, port, description):
    """Start an agent server in a new process"""
    print(f"Starting {description} on port {port}...")
    try:
        process = subprocess.Popen([sys.executable, script_name])
        time.sleep(2)  # Give each agent time to start
        return process
    except Exception as e:
        print(f"Failed to start {description}: {e}")
        return None

def main():
    print("=" * 60)
    print("Financial Multi-Agent System Startup")
    print("=" * 60)
    
    processes = []
    
    # Start MCP servers first (if you implement them)
    # print("\n1. Starting MCP Tool Servers...")
    
    # Start A2A Agent Servers
    print("\n2. Starting A2A Agent Servers...")
    
    agents = [
        ("run_data_gathering_a2a_server.py", 9001, "Data Gathering Agent"),
        ("run_quantitative_analysis_a2a_server.py", 9002, "Quantitative Analysis Agent"),
        ("run_qualitative_analysis_a2a_server.py", 9003, "Qualitative Analysis Agent"),
        ("run_report_generation_a2a_server.py", 9004, "Report Generation Agent"),
        ("run_orchestrator_a2a_server.py", 9000, "Orchestrator Agent"),
    ]
    
    for script, port, description in agents:
        if os.path.exists(script):
            process = start_agent(script, port, description)
            if process:
                processes.append((process, description))
        else:
            print(f"Warning: {script} not found!")
    
    print(f"\n✅ Started {len(processes)} agents successfully!")
    print("\n3. System Status:")
    print("   - Orchestrator Agent: http://localhost:9000/")
    print("   - Data Gathering Agent: http://localhost:9001/")
    print("   - Quantitative Analysis Agent: http://localhost:9002/")
    print("   - Qualitative Analysis Agent: http://localhost:9003/")
    print("   - Report Generation Agent: http://localhost:9004/")
    
    print("\n4. To start the UI, run:")
    print("   streamlit run app.py")
    
    print("\n5. To stop all agents, press Ctrl+C")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nShutting down all agents...")
        for process, description in processes:
            print(f"Stopping {description}...")
            process.terminate()
        print("All agents stopped.")

if __name__ == "__main__":
    main() 