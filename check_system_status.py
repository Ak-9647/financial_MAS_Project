#!/usr/bin/env python3
"""
System Status Checker for Financial MAS
Verifies all services are running and accessible
"""

import requests
import json
from typing import Dict, List

def check_service(name: str, url: str, timeout: int = 5) -> Dict:
    """Check if a service is running and accessible"""
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return {
                "name": name,
                "status": "✅ RUNNING",
                "url": url,
                "response_time": f"{response.elapsed.total_seconds():.3f}s"
            }
        else:
            return {
                "name": name,
                "status": f"❌ ERROR ({response.status_code})",
                "url": url,
                "response_time": f"{response.elapsed.total_seconds():.3f}s"
            }
    except requests.exceptions.ConnectionError:
        return {
            "name": name,
            "status": "❌ CONNECTION REFUSED",
            "url": url,
            "response_time": "N/A"
        }
    except requests.exceptions.Timeout:
        return {
            "name": name,
            "status": "❌ TIMEOUT",
            "url": url,
            "response_time": "N/A"
        }
    except Exception as e:
        return {
            "name": name,
            "status": f"❌ ERROR: {str(e)}",
            "url": url,
            "response_time": "N/A"
        }

def main():
    print("🔍 Financial MAS System Status Check")
    print("=" * 50)
    
    # Define services to check
    services = [
        ("Orchestrator Agent", "http://localhost:9000/.well-known/agent.json"),
        ("Data Gathering Agent", "http://localhost:9001/.well-known/agent.json"),
        ("Quantitative Analysis Agent", "http://localhost:9002/.well-known/agent.json"),
        ("Qualitative Analysis Agent", "http://localhost:9003/.well-known/agent.json"),
        ("Report Generation Agent", "http://localhost:9004/.well-known/agent.json"),
        ("React Frontend", "http://localhost:3000"),
        ("Financial Data MCP Server", "http://localhost:8001/tools"),
    ]
    
    results = []
    for name, url in services:
        result = check_service(name, url)
        results.append(result)
        print(f"{result['status']:<25} {result['name']:<30} ({result['response_time']})")
    
    print("\n" + "=" * 50)
    
    # Summary
    running_count = sum(1 for r in results if "✅" in r['status'])
    total_count = len(results)
    
    if running_count == total_count:
        print(f"🎉 ALL SERVICES RUNNING ({running_count}/{total_count})")
        print("\n🌐 Access URLs:")
        print("   • React Frontend: http://localhost:3000")
        print("   • Orchestrator API: http://localhost:9000")
        print("   • System is ready for financial analysis!")
    else:
        print(f"⚠️  SOME SERVICES DOWN ({running_count}/{total_count})")
        print("\n❌ Failed Services:")
        for result in results:
            if "❌" in result['status']:
                print(f"   • {result['name']}: {result['status']}")

if __name__ == "__main__":
    main() 