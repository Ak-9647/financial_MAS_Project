#!/bin/bash

# Financial MAS Frontend Startup Script
echo "============================================================"
echo "Financial Multi-Agent System - Frontend Startup"
echo "============================================================"

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16+ first."
    echo "Visit: https://nodejs.org/"
    exit 1
fi

# Check Node.js version
NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 16 ]; then
    echo "❌ Node.js version 16+ is required. Current version: $(node -v)"
    exit 1
fi

echo "✅ Node.js version: $(node -v)"

# Navigate to frontend directory
cd frontend

# Check if package.json exists
if [ ! -f "package.json" ]; then
    echo "❌ package.json not found. Please ensure you're in the correct directory."
    exit 1
fi

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies"
        exit 1
    fi
    echo "✅ Dependencies installed successfully"
else
    echo "✅ Dependencies already installed"
fi

# Check if backend is running
echo "🔍 Checking backend status..."
BACKEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:9000/.well-known/agent.json 2>/dev/null)

if [ "$BACKEND_STATUS" = "200" ]; then
    echo "✅ Backend is running on port 9000"
else
    echo "⚠️  Backend not detected on port 9000"
    echo "   Please ensure the Financial MAS backend is running first:"
    echo "   python3 start_system.py"
    echo ""
    echo "   Continuing with frontend startup..."
fi

# Start the development server
echo ""
echo "🚀 Starting React development server..."
echo "   Frontend will be available at: http://localhost:3000"
echo "   Press Ctrl+C to stop the server"
echo ""

# Set environment variables
export REACT_APP_API_URL=http://localhost:9000
export BROWSER=none  # Prevent auto-opening browser

# Start the React app
npm start 