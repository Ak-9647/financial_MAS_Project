# 🚀 Financial MAS Complete Setup Guide

This guide will help you set up the complete Financial Multi-Agent System with the beautiful modern React frontend.

## 📋 Prerequisites

### Required Software
- **Python 3.8+** - [Download here](https://python.org/downloads/)
- **Node.js 16+** - [Download here](https://nodejs.org/)
- **Git** - [Download here](https://git-scm.com/)

### API Keys (Optional but Recommended)
- **Finnhub API** - [Get free key](https://finnhub.io/)
- **Serper.dev API** - [Get free key](https://serper.dev/)
- **OpenAI API** - [Get key](https://platform.openai.com/api-keys)

## 🛠️ Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/Ak-9647/financial_MAS_Project.git
cd financial_MAS_Project
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Set Up Frontend Dependencies
```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Return to project root
cd ..
```

### 4. Configure Environment Variables
```bash
# Create environment file
cp env.example .env

# Edit the .env file with your API keys
nano .env  # or use your preferred editor
```

**Example .env file:**
```env
# Financial Data API
FINNHUB_API_KEY=your_finnhub_api_key_here

# Web Search API
SERPER_API_KEY=your_serper_api_key_here

# AI Model API
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Custom API endpoints
FINANCIAL_API_BASE_URL=https://finnhub.io/api/v1
SEARCH_API_BASE_URL=https://google.serper.dev
```

## 🚀 Running the System

### Quick Start (Recommended)

**Terminal 1: Start Backend Agents**
```bash
# Make sure you're in the project root and virtual environment is activated
python3 start_system.py
```

**Terminal 2: Start Modern Frontend**
```bash
# Make script executable (first time only)
chmod +x start_frontend.sh

# Start the React frontend
./start_frontend.sh
```

### Manual Start (Alternative)

**Backend Agents (5 terminals):**
```bash
# Terminal 1: Data Gathering Agent
python3 run_data_gathering_a2a_server.py

# Terminal 2: Quantitative Analysis Agent
python3 run_quantitative_analysis_a2a_server.py

# Terminal 3: Qualitative Analysis Agent
python3 run_qualitative_analysis_a2a_server.py

# Terminal 4: Report Generation Agent
python3 run_report_generation_a2a_server.py

# Terminal 5: Orchestrator Agent
python3 run_orchestrator_a2a_server.py
```

**Frontend:**
```bash
# Terminal 6: React Frontend
cd frontend
npm start
```

## 🌐 Access Points

Once everything is running, you can access:

### 🎨 Modern React Frontend (Primary)
- **URL**: http://localhost:3000
- **Features**: 
  - Beautiful glassmorphism design
  - Real-time agent monitoring
  - Interactive charts and analytics
  - Comprehensive analysis interface
  - Analysis history management

### 📊 Streamlit UI (Alternative)
```bash
# In a new terminal
streamlit run app.py
```
- **URL**: http://localhost:8501
- **Features**: Simple interface for basic functionality

### 🔧 Backend APIs
- **Orchestrator**: http://localhost:9000
- **Data Gathering**: http://localhost:9001
- **Quantitative Analysis**: http://localhost:9002
- **Qualitative Analysis**: http://localhost:9003
- **Report Generation**: http://localhost:9004

## 🎯 Using the System

### React Frontend Workflow

1. **Dashboard** (http://localhost:3000)
   - View system metrics and status
   - Quick analysis with the search bar
   - Monitor agent activity in real-time

2. **Analysis Page** (/analysis)
   - Enter detailed financial queries
   - Watch real-time progress through analysis steps
   - View comprehensive results with expandable sections

3. **Agent Status** (/agents)
   - Monitor all 5 agents in real-time
   - View detailed agent information
   - System health overview

4. **History** (/history)
   - Browse past analyses
   - Search and filter results
   - Export and share reports

### Example Queries

Try these sample queries in either interface:

```
Analyze Apple (AAPL) stock performance and provide investment recommendation

Compare Tesla vs Ford stock performance over the last quarter

Analyze NVIDIA earnings report and market sentiment

Provide technical analysis for Bitcoin price trends

Evaluate Microsoft Azure vs AWS market position
```

## 🔍 Verification Steps

### 1. Check Backend Status
```bash
# Test orchestrator
curl http://localhost:9000/.well-known/agent.json

# Should return agent information
```

### 2. Test Analysis Request
```bash
curl -X POST http://localhost:9000/ \
  -H "Content-Type: application/json" \
  -d '{
    "message": {
      "role": "user",
      "parts": [{"text": "{\"query\": \"Analyze AAPL stock\"}"}]
    }
  }'
```

### 3. Frontend Health Check
- Navigate to http://localhost:3000
- Check that agent status shows "5/5 Agents" in the navigation
- Try a quick analysis from the dashboard

## 🐛 Troubleshooting

### Common Issues

**Port Conflicts**
```bash
# Check what's using the ports
lsof -i :3000  # Frontend
lsof -i :9000  # Orchestrator
lsof -i :9001  # Data Gathering
# etc.

# Kill processes if needed
kill -9 <PID>
```

**Python Dependencies**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**Node.js Dependencies**
```bash
# Clear cache and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**API Key Issues**
- Verify your .env file is in the project root
- Check that API keys are valid and have sufficient quota
- The system works with mock data if no API keys are provided

### Debug Mode

**Backend Verbose Logging:**
```bash
# Set debug environment variable
export DEBUG=1
python3 start_system.py
```

**Frontend Development Mode:**
```bash
cd frontend
npm start  # Automatically includes hot reload and error overlay
```

## 📊 System Architecture

```
┌─────────────────┐    ┌─────────────────┐
│   React Frontend │    │  Streamlit UI   │
│   (Port 3000)   │    │   (Port 8501)   │
└─────────┬───────┘    └─────────┬───────┘
          │                      │
          └──────────┬───────────┘
                     │
         ┌───────────▼───────────┐
         │   Orchestrator Agent  │
         │     (Port 9000)       │
         └───────────┬───────────┘
                     │
    ┌────────────────┼────────────────┐
    │                │                │
┌───▼───┐    ┌───▼───┐    ┌───▼───┐    ┌───▼───┐
│ Data  │    │ Quant │    │ Qual  │    │Report │
│ Agent │    │ Agent │    │ Agent │    │ Agent │
│ 9001  │    │ 9002  │    │ 9003  │    │ 9004  │
└───────┘    └───────┘    └───────┘    └───────┘
```

## 🎨 Frontend Features

### Design Highlights
- **Glassmorphism Effects**: Semi-transparent cards with backdrop blur
- **Smooth Animations**: Framer Motion powered transitions
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dark Theme**: Elegant dark theme with gradient accents
- **Real-time Updates**: Live agent status and notifications

### Technical Features
- **React 18**: Latest React with concurrent features
- **Material-UI v5**: Comprehensive component library
- **TypeScript Ready**: Easy to migrate to TypeScript
- **PWA Ready**: Progressive Web App capabilities
- **Performance Optimized**: Code splitting and lazy loading

## 🚀 Production Deployment

### Frontend Deployment
```bash
# Build for production
cd frontend
npm run build

# Deploy to Netlify, Vercel, or your preferred platform
```

### Backend Deployment
```bash
# Use Docker or your preferred deployment method
# Ensure all environment variables are set
# Configure reverse proxy for production
```

## 📈 Next Steps

1. **Customize the Theme**: Modify colors and styling in `frontend/src/index.js`
2. **Add New Features**: Extend the React components for additional functionality
3. **Integrate More APIs**: Add new data sources to the backend agents
4. **Deploy to Production**: Set up CI/CD pipeline for automated deployment

## 🤝 Support

If you encounter any issues:

1. Check this troubleshooting guide
2. Review the logs in the terminal windows
3. Create an issue on GitHub with detailed error information
4. Check the individual README files in each directory

---

**🎉 Congratulations! You now have a fully functional Financial Multi-Agent System with a beautiful modern frontend!** 