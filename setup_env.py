#!/usr/bin/env python3
"""
Environment Setup Script for Financial MAS
This script helps you create your .env file with API keys
"""

import os
import shutil

def create_env_file():
    """Create a .env file from the example template"""
    
    # Check if .env already exists
    if os.path.exists('.env'):
        response = input(".env file already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Keeping existing .env file.")
            return
    
    # Copy example file to .env
    if os.path.exists('env.example'):
        shutil.copy('env.example', '.env')
        print("✅ Created .env file from template!")
        print("\n📝 Next steps:")
        print("1. Edit .env file with your actual API keys")
        print("2. Get API keys from:")
        print("   - Finnhub: https://finnhub.io/")
        print("   - Serper.dev: https://serper.dev/")
        print("   - OpenAI: https://platform.openai.com/api-keys")
        print("\n🚀 After adding API keys, you can run:")
        print("   python3 start_system.py")
    else:
        print("❌ env.example file not found!")

def check_requirements():
    """Check if all required packages are installed"""
    try:
        import dotenv
        print("✅ python-dotenv is installed")
    except ImportError:
        print("❌ python-dotenv not installed. Run: pip install python-dotenv")

def main():
    print("🔧 Financial MAS Environment Setup")
    print("=" * 40)
    
    check_requirements()
    create_env_file()
    
    print("\n✨ Setup complete!")

if __name__ == "__main__":
    main() 