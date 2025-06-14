#!/bin/bash

# Financial MAS Project - Git Repository Setup
echo "🚀 Setting up Git repository for Financial MAS Project..."

# Initialize git repository
echo "📁 Initializing Git repository..."
git init

# Add all files (respecting .gitignore)
echo "📋 Adding files to Git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Financial Multi-Agent System

- Complete multi-agent architecture with 5 specialized agents
- A2A (Agent-to-Agent) communication protocol
- Real-time financial data integration (Finnhub API)
- Web research capabilities (Serper.dev API)
- Streamlit UI for system monitoring and interaction
- MCP (Model Context Protocol) tool servers
- Comprehensive testing suite
- Docker support and deployment scripts

Features:
✅ Orchestrator Agent (workflow coordination)
✅ Data Gathering Agent (financial data & web research)
✅ Quantitative Analysis Agent (statistical analysis)
✅ Qualitative Analysis Agent (sentiment analysis)
✅ Report Generation Agent (final synthesis)
✅ Real API integrations with error handling
✅ Distributed microservices architecture
✅ Production-ready deployment"

# Set main branch
echo "🌿 Setting main branch..."
git branch -M main

# Add remote origin
echo "🔗 Adding remote repository..."
git remote add origin https://github.com/Ak-9647/financial_MAS_Project.git

# Push to GitHub
echo "⬆️ Pushing to GitHub..."
git push -u origin main

echo "✅ Git repository setup complete!"
echo "🔗 Repository URL: https://github.com/Ak-9647/financial_MAS_Project.git" 