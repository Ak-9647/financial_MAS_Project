#!/usr/bin/env python3

import requests
import json

def quick_test():
    print("🚀 Financial MAS - Quick Test")
    print("=" * 40)
    
    # Test 1: Check if orchestrator is running
    try:
        response = requests.get("http://localhost:9000/.well-known/agent.json", timeout=5)
        if response.status_code == 200:
            print("✅ System is running")
        else:
            print("❌ System not running - start with: python3 start_system.py")
            return
    except:
        print("❌ System not running - start with: python3 start_system.py")
        return
    
    # Test 2: Run a quick analysis
    print("\n📈 Running stock analysis...")
    payload = {
        "message": {
            "role": "user",
            "parts": [{"text": '{"query": "Quick analysis of Apple stock"}'}]
        }
    }
    
    try:
        response = requests.post("http://localhost:9000/", json=payload, timeout=20)
        if response.status_code == 200:
            data = response.json()
            if data.get('state') == 'COMPLETED':
                print("✅ Analysis completed successfully")
                response_data = json.loads(data['messages'][1]['parts'][0]['text'])
                if response_data.get('workflow_completed'):
                    print("✅ All 4 agents worked together")
                else:
                    print("⚠️  Partial completion")
            else:
                print(f"❌ Analysis failed - Status: {data.get('state')}")
        else:
            print(f"❌ Request failed - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Analysis error: {e}")
    
    # Test 3: Check real data
    print("\n💰 Testing real financial data...")
    try:
        response = requests.post(
            "http://localhost:8001/call",
            json={"tool": "get_stock_price", "params": {"symbol": "TSLA"}},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            result = data['result']
            price = result.get('current_price')
            if price:
                print(f"✅ Tesla (TSLA): ${price}")
            else:
                print("⚠️  No price data available")
        else:
            print("❌ Financial data server not responding")
    except Exception as e:
        print(f"❌ Financial data error: {e}")
    
    print("\n" + "=" * 40)
    print("🎉 Quick test completed!")
    print("\n📖 Available commands:")
    print("   python3 start_system.py    # Start all agents")
    print("   python3 quick_test.py      # Run this test")
    print("   python3 test_system.py     # Full system test")
    print("   python3 check_api_keys.py  # Check API keys")

if __name__ == "__main__":
    quick_test() 