#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

def check_finnhub_api():
    """Check if Finnhub API key is valid"""
    api_key = os.getenv("FINNHUB_API_KEY")
    if not api_key:
        return "❌ FINNHUB_API_KEY not found in .env file"
    
    try:
        import finnhub
        client = finnhub.Client(api_key=api_key)
        # Test with a simple quote request
        resp = client.quote("AAPL")
        if resp.get('c') is not None:
            return f"✅ Finnhub API key is valid (AAPL: ${resp.get('c')})"
        else:
            return "❌ Finnhub API key invalid or rate limited"
    except Exception as e:
        return f"❌ Finnhub API error: {e}"

def check_serper_api():
    """Check if Serper.dev API key is valid"""
    api_key = os.getenv("SERPER_DEV_API_KEY")
    if not api_key:
        return "❌ SERPER_DEV_API_KEY not found in .env file"
    
    try:
        headers = {'X-API-KEY': api_key, 'Content-Type': 'application/json'}
        payload = json.dumps({"q": "test", "num": 1})
        response = requests.post("https://google.serper.dev/search", headers=headers, data=payload)
        
        if response.status_code == 200:
            return "✅ Serper.dev API key is valid"
        elif response.status_code == 403:
            return "❌ Serper.dev API key invalid or expired"
        else:
            return f"❌ Serper.dev API error: {response.status_code}"
    except Exception as e:
        return f"❌ Serper.dev API error: {e}"

def check_openai_api():
    """Check if OpenAI API key is valid"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "❌ OPENAI_API_KEY not found in .env file"
    
    try:
        headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
        response = requests.get("https://api.openai.com/v1/models", headers=headers)
        
        if response.status_code == 200:
            return "✅ OpenAI API key is valid"
        elif response.status_code == 401:
            return "❌ OpenAI API key invalid"
        else:
            return f"❌ OpenAI API error: {response.status_code}"
    except Exception as e:
        return f"❌ OpenAI API error: {e}"

def main():
    print("🔍 Checking API Keys Configuration...")
    print("=" * 50)
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("❌ .env file not found!")
        print("\n📝 To fix:")
        print("1. Copy env.example to .env: cp env.example .env")
        print("2. Edit .env and add your API keys")
        return
    
    print("✅ .env file found")
    print("\n🔍 Testing API Keys:")
    print("-" * 30)
    
    # Test each API
    print("Finnhub:", check_finnhub_api())
    print("Serper.dev:", check_serper_api())
    print("OpenAI:", check_openai_api())
    
    print("\n" + "=" * 50)
    print("📖 How to get API keys:")
    print("-" * 30)
    print("🔸 Finnhub (Free): https://finnhub.io/")
    print("   - Sign up and get free API key")
    print("   - 60 API calls/minute limit")
    
    print("\n🔸 Serper.dev (Free): https://serper.dev/")
    print("   - Sign up with Google")
    print("   - Get 2,500 free searches")
    
    print("\n🔸 OpenAI: https://platform.openai.com/")
    print("   - Create account and add payment method")
    print("   - Generate API key")
    
    print("\n" + "=" * 50)
    print("🚀 Next steps:")
    print("1. Get valid API keys from the services above")
    print("2. Update your .env file with the keys")
    print("3. Run this script again to verify")
    print("4. Start the system with: python3 start_system.py")

if __name__ == "__main__":
    main() 