# 🚀 Financial Multi-Agent System (MAS)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![React 18](https://img.shields.io/badge/react-18.0+-61dafb.svg)](https://reactjs.org/)
[![Node.js 16+](https://img.shields.io/badge/node.js-16.0+-green.svg)](https://nodejs.org/)

A sophisticated financial research system built with **multi-agent architecture**, featuring distributed AI agents that collaborate through A2A (Agent-to-Agent) protocol and an **ultra-modern React frontend** that rivals the best fintech applications.

## ✨ What's New - Ultra-Modern Frontend

🎨 **Cutting-edge React frontend** with advanced glassmorphism effects  
🎭 **Sophisticated animations** powered by Framer Motion  
📱 **Mobile-first responsive design** that works beautifully on all devices  
⚡ **Real-time agent monitoring** with live status updates  
🔮 **Interactive data visualization** with custom charts and metrics  

![Financial MAS Dashboard](https://via.placeholder.com/800x400/667eea/ffffff?text=Ultra-Modern+Financial+MAS+Dashboard)

## 🏗️ System Architecture

### 🤖 Agent Layer (A2A Servers)
- **Orchestrator Agent** (Port 9000) - Coordinates the entire workflow
- **Data Gathering Agent** (Port 9001) - Retrieves financial data and web research
- **Quantitative Analysis Agent** (Port 9002) - Performs statistical analysis
- **Qualitative Analysis Agent** (Port 9003) - Analyzes sentiment and themes
- **Report Generation Agent** (Port 9004) - Synthesizes final reports

### 🎨 Frontend Layer
- **Ultra-Modern React Frontend** (Port 3000) - Primary interface with advanced features
- **Streamlit UI** (Port 8501) - Alternative simple interface for quick access

### 🔧 Data Layer (Optional MCP Tool Servers)
- **Financial Data Server** (Port 8001) - Finnhub API integration
- **Web Research Server** (Port 8002) - Serper.dev search API
- **Knowledge Base Server** (Port 8003) - ChromaDB vector database

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** with pip
- **Node.js 16+** with npm
- **Git** for version control

### 1. Clone & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/financial_mas_project.git
cd financial_mas_project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
# Run the setup script to create your .env file
python3 setup_env.py

# Edit with your API keys (optional for demo mode)
nano .env  # or use your preferred editor
```

**API Keys (Optional):**
- **Finnhub**: https://finnhub.io/ (Financial data)
- **Serper.dev**: https://serper.dev/ (Web search)
- **OpenAI**: https://platform.openai.com/api-keys (AI processing)

### 3. Start the Backend System

```bash
# Start all AI agents
python start_system.py
```

This will start all 5 agents on ports 9000-9004. You should see:
```
✅ Started 5 agents successfully!
- Orchestrator Agent: http://localhost:9000/
- Data Gathering Agent: http://localhost:9001/
- Quantitative Analysis Agent: http://localhost:9002/
- Qualitative Analysis Agent: http://localhost:9003/
- Report Generation Agent: http://localhost:9004/
```

### 4. Launch the Ultra-Modern Frontend

```bash
# Option A: Use the startup script (Recommended)
chmod +x start_frontend.sh
./start_frontend.sh

# Option B: Manual startup
cd frontend
npm install
npm start
```

### 5. Access the Application

🎯 **Primary Interface**: http://localhost:3000 (Ultra-Modern React Frontend)  
🔧 **Alternative Interface**: http://localhost:8501 (Streamlit UI)

## 🎨 Frontend Features

### Ultra-Modern Design System
- **Advanced Glassmorphism** with 24px backdrop blur effects
- **Gradient Color Palette** with professional fintech aesthetics
- **Premium Typography** using Inter and JetBrains Mono fonts
- **Responsive Design** that adapts from mobile to desktop

### Interactive Components
- **Real-time Agent Monitoring** with health indicators
- **Interactive Dashboard** with metrics and charts
- **Advanced Analysis Interface** with progress tracking
- **Mobile-Responsive Navigation** with smooth animations

### Technical Excellence
- **React 18** with modern hooks and patterns
- **Material-UI v5** with custom theming
- **Framer Motion** for sophisticated animations
- **Recharts** for beautiful data visualization

## 📱 Usage Examples

### Quick Analysis
1. Open http://localhost:3000
2. Use the quick analysis box on the dashboard
3. Enter queries like:
   - "Analyze NVIDIA's stock performance"
   - "Compare AMD vs Intel financial metrics"
   - "Research Tesla's latest earnings"

### Detailed Analysis
1. Navigate to the Analysis page
2. Enter comprehensive queries
3. Watch real-time progress through all 4 agent steps
4. View expandable results with detailed insights

### System Monitoring
1. Check the navbar for real-time agent status
2. Visit the Agents page for detailed system health
3. Monitor performance metrics and connectivity

## 🛠️ Development

### Project Structure

```
financial_mas_project/
├── agents/                          # AI agent implementations
│   ├── data_gathering_agent.py
│   ├── quantitative_analysis_agent.py
│   ├── qualitative_analysis_agent.py
│   ├── report_generation_agent.py
│   └── orchestrator_agent.py
├── frontend/                        # Ultra-modern React frontend
│   ├── src/
│   │   ├── components/              # React components
│   │   │   ├── Navbar.js           # Navigation with glassmorphism
│   │   │   ├── Dashboard.js        # Main dashboard
│   │   │   ├── AnalysisPage.js     # Analysis interface
│   │   │   ├── AgentStatus.js      # System monitoring
│   │   │   └── HistoryPage.js      # Analysis history
│   │   ├── services/               # API services
│   │   │   └── api.js              # Backend integration
│   │   ├── App.js                  # Main app component
│   │   └── index.js                # Theme and setup
│   ├── public/                     # Static assets
│   ├── package.json                # Dependencies
│   └── README.md                   # Frontend documentation
├── services/                       # Business logic services
├── mcp_servers/                    # MCP tool servers (optional)
├── utils/                          # Utility modules
├── requirements.txt                # Python dependencies
├── start_system.py                 # Backend startup script
├── start_frontend.sh               # Frontend startup script
└── app.py                         # Streamlit UI (alternative)
```

### Adding New Features

#### Backend (Python)
1. Create new agent in `agents/` directory
2. Add A2A server runner: `run_new_agent_a2a_server.py`
3. Update orchestrator to include new agent
4. Add to startup script

#### Frontend (React)
1. Create components in `frontend/src/components/`
2. Add routes in `App.js`
3. Update navigation in `Navbar.js`
4. Integrate with API in `services/api.js`

### Testing

```bash
# Test backend agents
python test_system.py

# Test individual agents
curl http://localhost:9000/.well-known/agent.json

# Test frontend
cd frontend
npm test
```

## 🔧 Configuration

### Agent Ports
- **Orchestrator**: 9000
- **Data Gathering**: 9001
- **Quantitative Analysis**: 9002
- **Qualitative Analysis**: 9003
- **Report Generation**: 9004

### MCP Tool Server Ports (Optional)
- **Financial Data**: 8001
- **Web Research**: 8002
- **Knowledge Base**: 8003

### Frontend Configuration
- **Development Server**: 3000
- **Build Output**: `frontend/build/`
- **API Proxy**: Configured to backend on port 9000

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Code Style

- **Python**: Follow PEP 8, use black formatter
- **JavaScript/React**: Use ESLint and Prettier
- **Commits**: Use conventional commit messages

## 📊 Performance

- **Backend Response Time**: ~8-15 seconds for full analysis
- **Frontend Load Time**: <2 seconds on modern browsers
- **Memory Usage**: ~200MB for full system
- **Concurrent Users**: Supports multiple simultaneous analyses

## 🔒 Security

- **API Keys**: Stored in `.env` file (never committed)
- **CORS**: Configured for local development
- **Input Validation**: Implemented on both frontend and backend
- **Error Handling**: Graceful degradation with user feedback

## 📈 Roadmap

- [ ] **Real-time WebSocket updates** for live analysis progress
- [ ] **User authentication** and personalized dashboards
- [ ] **Portfolio tracking** with historical performance
- [ ] **Advanced charting** with technical indicators
- [ ] **Export functionality** for reports and data
- [ ] **Dark/Light theme** toggle
- [ ] **Mobile app** using React Native

## 🐛 Troubleshooting

### Common Issues

**Backend agents not starting:**
```bash
# Check if ports are in use
lsof -i :9000-9004

# Kill existing processes if needed
pkill -f "python.*run_.*_a2a_server.py"
```

**Frontend not loading:**
```bash
# Clear npm cache and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
npm start
```

**API connection errors:**
- Ensure all backend agents are running
- Check firewall settings
- Verify `.env` file configuration

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for AI capabilities
- **Material-UI** for React components
- **Framer Motion** for animations
- **Recharts** for data visualization
- **FastAPI** for backend framework

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/financial_mas_project/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/financial_mas_project/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/financial_mas_project/wiki)

---

**⭐ Star this repository if you find it useful!**

*Built with ❤️ using Python, React, and modern AI technologies* 