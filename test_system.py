#!/usr/bin/env python3

import requests
import json
import time
import sys

def test_api_keys():
    """Test API keys"""
    print("🔍 Testing API Keys...")
    try:
        from services.financial_service import FinHubService
        from services.web_research_service import SerperDevService
        
        # Test Finnhub
        financial = FinHubService()
        stock_data = financial.get_stock_price("AAPL")
        if stock_data.get('current_price'):
            print("✅ Finnhub API working - AAPL:", stock_data['current_price'])
        else:
            print("❌ Finnhub API issue:", stock_data.get('error', 'Unknown error'))
        
        # Test Serper
        web = SerperDevService()
        search_results = web.search_google("test", 1)
        if search_results and not search_results[0].get('error'):
            print("✅ Serper.dev API working")
        else:
            print("❌ Serper.dev API issue:", search_results[0].get('error', 'Unknown error') if search_results else 'No results')
            
    except Exception as e:
        print(f"❌ API test error: {e}")

def test_agents():
    """Test all A2A agents"""
    print("\n🤖 Testing A2A Agents...")
    agents = [
        ("Orchestrator", 9000),
        ("Data Gathering", 9001),
        ("Quantitative", 9002),
        ("Qualitative", 9003),
        ("Report Generation", 9004)
    ]
    
    for name, port in agents:
        try:
            response = requests.get(f"http://localhost:{port}/.well-known/agent.json", timeout=5)
            if response.status_code == 200:
                print(f"✅ {name} Agent (port {port})")
            else:
                print(f"❌ {name} Agent (port {port}) - Status: {response.status_code}")
        except Exception as e:
            print(f"❌ {name} Agent (port {port}) - Error: {e}")

def test_mcp_servers():
    """Test MCP servers"""
    print("\n🔧 Testing MCP Servers...")
    servers = [
        ("Financial Data", 8001),
        ("Web Research", 8002),
        ("Knowledge Base", 8003)
    ]
    
    for name, port in servers:
        try:
            response = requests.get(f"http://localhost:{port}/tools", timeout=5)
            if response.status_code == 200:
                tools = response.json().get('tools', [])
                print(f"✅ {name} MCP Server (port {port}) - {len(tools)} tools")
            else:
                print(f"❌ {name} MCP Server (port {port}) - Status: {response.status_code}")
        except Exception as e:
            print(f"❌ {name} MCP Server (port {port}) - Error: {e}")

def test_workflow():
    """Test complete workflow"""
    print("\n🔄 Testing Complete Workflow...")
    try:
        payload = {
            "message": {
                "role": "user",
                "parts": [{"text": '{"query": "Analyze Microsoft (MSFT) stock performance"}'}]
            }
        }
        
        response = requests.post("http://localhost:9000/", json=payload, timeout=30)
        if response.status_code == 200:
            data = response.json()
            if data.get('state') == 'COMPLETED':
                response_data = json.loads(data['messages'][1]['parts'][0]['text'])
                if response_data.get('workflow_completed'):
                    steps = response_data.get('workflow_steps', [])
                    completed_steps = [s for s in steps if s['status'] == 'completed']
                    print(f"✅ Workflow completed - {len(completed_steps)}/4 steps successful")
                    return True
                else:
                    print("❌ Workflow not completed")
            else:
                print(f"❌ Workflow failed - State: {data.get('state')}")
        else:
            print(f"❌ Workflow request failed - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Workflow test error: {e}")
    return False

def test_real_data():
    """Test if agents are using real API data"""
    print("\n📊 Testing Real Data Usage...")
    try:
        payload = {
            "message": {
                "role": "user", 
                "parts": [{"text": '{"task": "get_stock_price", "symbol": "GOOGL"}'}]
            }
        }
        
        response = requests.post("http://localhost:9001/", json=payload, timeout=10)
        if response.status_code == 200:
            data = response.json()
            response_data = json.loads(data['messages'][1]['parts'][0]['text'])
            stock_data = response_data.get('stock_data', {})
            
            if stock_data.get('current_price') and isinstance(stock_data['current_price'], (int, float)):
                print(f"✅ Real data - GOOGL: ${stock_data['current_price']}")
                return True
            else:
                print("❌ Using mock data or no price data")
        else:
            print(f"❌ Data gathering test failed - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Real data test error: {e}")
    return False

def test_ui():
    """Test Streamlit UI"""
    print("\n🖥️  Testing Streamlit UI...")
    try:
        response = requests.get("http://localhost:8501/", timeout=5)
        if response.status_code == 200:
            print("✅ Streamlit UI accessible at http://localhost:8501")
            return True
        else:
            print(f"❌ Streamlit UI not accessible - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Streamlit UI test error: {e}")
    return False

def main():
    print("=" * 60)
    print("🚀 Financial Multi-Agent System - Comprehensive Test")
    print("=" * 60)
    
    # Run all tests
    test_api_keys()
    test_agents()
    test_mcp_servers()
    workflow_success = test_workflow()
    real_data_success = test_real_data()
    ui_success = test_ui()
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 Test Summary:")
    print("=" * 60)
    print(f"✅ Workflow: {'PASS' if workflow_success else 'FAIL'}")
    print(f"✅ Real Data: {'PASS' if real_data_success else 'FAIL'}")
    print(f"✅ UI: {'PASS' if ui_success else 'FAIL'}")
    
    if workflow_success and real_data_success:
        print("\n🎉 System is fully functional with real API data!")
        print("\n🔗 Access points:")
        print("   • Streamlit UI: http://localhost:8501")
        print("   • Orchestrator API: http://localhost:9000")
        print("   • Agent Discovery: http://localhost:9001/.well-known/agent.json")
    else:
        print("\n⚠️  Some components need attention. Check the logs above.")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main() 