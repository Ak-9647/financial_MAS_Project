#!/usr/bin/env python3
"""
Test script to verify the Financial MAS analysis workflow
"""

import requests
import json

def test_analysis():
    """Test the analysis workflow"""
    print("🧪 Testing Financial MAS Analysis Workflow")
    print("=" * 50)
    
    # Test query
    query = "Analyze Apple (AAPL) stock performance"
    
    # Prepare the request
    url = "http://localhost:9000/"
    payload = {
        "message": {
            "role": "user",
            "parts": [{"text": json.dumps({"query": query})}]
        }
    }
    
    print(f"📊 Query: {query}")
    print("🚀 Sending request to orchestrator...")
    
    try:
        response = requests.post(url, json=payload, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Request successful!")
            print("\n📋 Response Structure:")
            print(f"   - State: {result.get('state', 'Unknown')}")
            print(f"   - Messages: {len(result.get('messages', []))} messages")
            
            if result.get('messages'):
                final_message = result['messages'][-1]
                if final_message.get('parts') and final_message['parts'][0].get('text'):
                    try:
                        analysis_result = json.loads(final_message['parts'][0]['text'])
                        print("\n🎯 Analysis Result Structure:")
                        print(f"   - Orchestrator: {analysis_result.get('orchestrator', 'N/A')}")
                        print(f"   - Workflow Completed: {analysis_result.get('workflow_completed', False)}")
                        print(f"   - Query: {analysis_result.get('query', 'N/A')}")
                        
                        if analysis_result.get('final_report'):
                            report = analysis_result['final_report']
                            print("\n📊 Final Report Contents:")
                            print(f"   - Executive Summary: {bool(report.get('executive_summary'))}")
                            print(f"   - Investment Recommendation: {bool(report.get('investment_recommendation'))}")
                            print(f"   - Key Findings: {len(report.get('key_findings', []))} items")
                            print(f"   - Financial Highlights: {bool(report.get('financial_highlights'))}")
                            
                            if report.get('investment_recommendation'):
                                rec = report['investment_recommendation']
                                print(f"\n💡 Investment Recommendation:")
                                print(f"   - Rating: {rec.get('rating', 'N/A')}")
                                print(f"   - Confidence: {rec.get('confidence', 'N/A')}")
                                print(f"   - Time Horizon: {rec.get('time_horizon', 'N/A')}")
                                print(f"   - Risk Level: {rec.get('risk_level', 'N/A')}")
                            
                            if report.get('financial_highlights'):
                                highlights = report['financial_highlights']
                                print(f"\n💰 Financial Highlights:")
                                for key, value in highlights.items():
                                    print(f"   - {key.replace('_', ' ').title()}: {value}")
                        
                        print("\n🔄 Workflow Steps:")
                        for step in analysis_result.get('workflow_steps', []):
                            print(f"   - Step {step.get('step')}: {step.get('agent')} - {step.get('status')}")
                        
                        print("\n✅ Analysis workflow completed successfully!")
                        return True
                        
                    except json.JSONDecodeError as e:
                        print(f"❌ Failed to parse analysis result: {e}")
                        print(f"Raw text: {final_message['parts'][0]['text'][:200]}...")
                        return False
                else:
                    print("❌ No analysis result found in response")
                    return False
            else:
                print("❌ No messages in response")
                return False
        else:
            print(f"❌ Request failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - is the orchestrator running?")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_analysis()
    if success:
        print("\n🎉 Test completed successfully!")
        print("Your Financial MAS system is working correctly!")
    else:
        print("\n❌ Test failed!")
        print("Please check the system logs for issues.") 