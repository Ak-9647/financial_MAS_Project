#!/usr/bin/env python3
"""
ADK Financial MAS System Test Suite
Comprehensive testing of ADK framework implementation
"""
import requests
import json
import time

def test_adk_system():
    print("🧪 ADK FINANCIAL MAS SYSTEM TEST SUITE")
    print("=" * 60)
    
    # Test ADK agent endpoints
    adk_agents = [
        {"name": "ADK Orchestrator", "port": 9000},
        {"name": "ADK Data Gathering", "port": 9001},
        {"name": "ADK Quantitative Analysis", "port": 9002},
        {"name": "ADK Qualitative Analysis", "port": 9003},
        {"name": "ADK Report Generation", "port": 9004}
    ]
    
    print("🔍 Testing ADK Agent Availability...")
    print()
    
    for agent in adk_agents:
        print(f"Testing {agent['name']} Agent (Port {agent['port']}):")
        
        # Test agent card endpoint
        try:
            response = requests.get(f"http://localhost:{agent['port']}/.well-known/agent.json", timeout=5)
            if response.status_code == 200:
                agent_card = response.json()
                print(f"  ✅ Agent Card: {agent_card.get('name', 'Unknown')}")
                print(f"     🔧 ADK Version: {agent_card.get('adk_version', 'N/A')}")
                print(f"     ⚡ Enterprise: {agent_card.get('enterprise_grade', False)}")
                print(f"     📋 Capabilities: {len(agent_card.get('capabilities', []))}")
            else:
                print(f"  ❌ Agent Card: HTTP {response.status_code}")
        except Exception as e:
            print(f"  ❌ Agent Card: {str(e)}")
        
        # Test ADK info endpoint
        try:
            response = requests.get(f"http://localhost:{agent['port']}/adk/info", timeout=5)
            if response.status_code == 200:
                adk_info = response.json()
                print(f"  ✅ ADK Info: Agent ID {adk_info.get('agent_id', 'Unknown')[:8]}...")
                print(f"     📊 State: {adk_info.get('state', 'Unknown')}")
                print(f"     🕒 Executions: {adk_info.get('execution_count', 0)}")
            else:
                print(f"  ❌ ADK Info: HTTP {response.status_code}")
        except Exception as e:
            print(f"  ❌ ADK Info: {str(e)}")
        
        # Test ADK capabilities endpoint
        try:
            response = requests.get(f"http://localhost:{agent['port']}/adk/capabilities", timeout=5)
            if response.status_code == 200:
                capabilities = response.json()
                print(f"  ✅ ADK Capabilities: {len(capabilities.get('capabilities', []))} available")
            else:
                print(f"  ❌ ADK Capabilities: HTTP {response.status_code}")
        except Exception as e:
            print(f"  ❌ ADK Capabilities: {str(e)}")
        
        print()
    
    print("🚀 Testing ADK Financial Analysis Workflow...")
    print()
    
    # Test TTGT analysis with ADK orchestrator
    test_query = "Analyze TTGT stock performance using ADK framework"
    
    print(f"📊 Query: {test_query}")
    print("🤖 Sending to ADK Orchestrator...")
    
    try:
        payload = {
            "message": {
                "role": "user",
                "parts": [{"text": json.dumps({"query": test_query})}]
            }
        }
        
        response = requests.post("http://localhost:9000/", json=payload, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ ADK Analysis Complete!")
            print()
            
            # Check for ADK metadata
            if "adk_metadata" in result:
                adk_meta = result["adk_metadata"]
                print("🔧 ADK Metadata:")
                print(f"   Agent Name: {adk_meta.get('agent_name', 'Unknown')}")
                print(f"   Execution ID: {adk_meta.get('execution_id', 'Unknown')[:8]}...")
                print(f"   ADK Version: {adk_meta.get('adk_version', 'Unknown')}")
                print(f"   Execution Time: {adk_meta.get('execution_time', 0):.2f}s")
                print()
            
            # Check for workflow results
            if "messages" in result and len(result["messages"]) > 1:
                agent_response = result["messages"][-1]
                if "parts" in agent_response and agent_response["parts"]:
                    try:
                        analysis_result = json.loads(agent_response["parts"][0]["text"])
                        
                        print("📋 ADK Analysis Results:")
                        if "final_report" in analysis_result:
                            report = analysis_result["final_report"]
                            print(f"   Executive Summary: {report.get('executive_summary', 'N/A')[:100]}...")
                            print(f"   Investment Recommendation: {report.get('investment_recommendation', 'N/A')}")
                            print(f"   Confidence Level: {report.get('confidence_level', 'N/A')}")
                            print(f"   ADK Enhanced: {report.get('adk_synthesis', False)}")
                            print(f"   Enterprise Grade: {report.get('enterprise_grade', False)}")
                        
                        if "adk_capabilities_used" in analysis_result:
                            print(f"   ADK Capabilities Used: {len(analysis_result['adk_capabilities_used'])}")
                        
                        if "enterprise_features" in analysis_result:
                            features = analysis_result["enterprise_features"]
                            print(f"   Enterprise Features: {sum(features.values())} active")
                        
                    except json.JSONDecodeError:
                        print("   Raw Response: Analysis completed (JSON parse error)")
            
        else:
            print(f"❌ ADK Analysis Failed: HTTP {response.status_code}")
            print(f"   Response: {response.text[:200]}...")
    
    except Exception as e:
        print(f"❌ ADK Analysis Error: {str(e)}")
    
    print()
    print("=" * 60)
    print("🎉 ADK SYSTEM TEST COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    test_adk_system() 