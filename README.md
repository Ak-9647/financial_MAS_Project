# Financial Multi-Agent System (MAS)

A sophisticated financial research system built with multi-agent architecture, featuring distributed agents that collaborate through A2A (Agent-to-Agent) protocol.

## 🏗️ Architecture

### Agent Layer (A2A Servers)
- **Orchestrator Agent** (Port 9000) - Coordinates the entire workflow
- **Data Gathering Agent** (Port 9001) - Retrieves financial data and web research
- **Quantitative Analysis Agent** (Port 9002) - Performs statistical analysis
- **Qualitative Analysis Agent** (Port 9003) - Analyzes sentiment and themes
- **Report Generation Agent** (Port 9004) - Synthesizes final reports

### Data Layer (MCP Tool Servers) - Optional
- **Financial Data Server** (Port 8001) - Finnhub API integration
- **Web Research Server** (Port 8002) - Serper.dev search API
- **Knowledge Base Server** (Port 8003) - ChromaDB vector database

### UI Layer
- **Streamlit Control Room** - Web interface for interacting with the system

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Variables (Required for Real API Features)

**Easy Setup:**
```bash
# Run the setup script to create your .env file
python3 setup_env.py

# Then edit .env with your actual API keys
nano .env  # or use your preferred editor
```

**Manual Setup:**
```bash
# Copy the example file
cp env.example .env

# Edit with your API keys
# Get your keys from:
# - Finnhub: https://finnhub.io/
# - Serper.dev: https://serper.dev/
# - OpenAI: https://platform.openai.com/api-keys
```

### 3. Start the System

**Option A: Use the startup script (Recommended)**
```bash
python start_system.py
```

**Option B: Start agents manually**
```bash
# Terminal 1
python run_data_gathering_a2a_server.py

# Terminal 2
python run_quantitative_analysis_a2a_server.py

# Terminal 3
python run_qualitative_analysis_a2a_server.py

# Terminal 4
python run_report_generation_a2a_server.py

# Terminal 5
python run_orchestrator_a2a_server.py
```

### 4. Launch the UI

```bash
streamlit run app.py
```

## 🎯 Usage

1. Open the Streamlit interface in your browser
2. Check the sidebar to ensure all agents are running (green checkmarks)
3. Enter a financial research query, such as:
   - "Analyze NVIDIA's stock performance and recent news"
   - "Compare AMD vs Intel financial metrics"
   - "Research Tesla's latest earnings and market sentiment"

## 📁 Project Structure

```
financial_mas_project/
├── agents/                          # Agent implementations
│   ├── data_gathering_agent.py
│   ├── quantitative_analysis_agent.py
│   ├── qualitative_analysis_agent.py
│   ├── report_generation_agent.py
│   └── orchestrator_agent.py
├── services/                        # Business logic services
│   ├── financial_service.py
│   ├── web_research_service.py
│   └── knowledge_service.py
├── mcp_servers/                     # MCP tool servers
│   ├── financial_data_server.py
│   ├── web_research_server.py
│   └── knowledge_base_server.py
├── utils/                           # Utility modules
│   ├── sse_server_wrapper.py
│   ├── a2a_server.py
│   ├── a2a_client.py
│   └── card_generator.py
├── db/                              # Database files
├── run_*_a2a_server.py             # Agent server runners
├── start_system.py                  # System startup script
├── app.py                          # Streamlit UI
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🔧 Configuration

### Agent Ports
- Orchestrator: 9000
- Data Gathering: 9001
- Quantitative Analysis: 9002
- Qualitative Analysis: 9003
- Report Generation: 9004

### MCP Tool Server Ports (Optional)
- Financial Data: 8001
- Web Research: 8002
- Knowledge Base: 8003

## 🧪 Testing the System

### Test Individual Agents

```bash
# Test agent discovery
curl http://localhost:9000/.well-known/agent.json

# Test task submission
curl -X POST http://localhost:9000/ \
  -H "Content-Type: application/json" \
  -d '{
    "message": {
      "role": "user",
      "parts": [{"text": "{\"query\": \"Analyze NVIDIA stock\"}"}]
    }
  }'
```

### Test Full Workflow

Use the Streamlit interface or send requests directly to the orchestrator.

## 🛠️ Development

### Adding New Agents

1. Create agent class in `agents/`
2. Create A2A server runner: `run_new_agent_a2a_server.py`
3. Update orchestrator to include new agent
4. Add to startup script

### Extending Functionality

- Add new MCP tools in `mcp_servers/`
- Extend services in `services/`
- Add utilities in `utils/`

## 🐛 Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure no other processes are using ports 9000-9004
2. **Agent not starting**: Check console output for detailed error messages
3. **Connection timeouts**: Verify all agents are running before testing
4. **Import errors**: Ensure all dependencies are installed

### Debugging

- Check individual agent logs in their terminal windows
- Use the system status in the Streamlit sidebar
- Test agent endpoints directly with curl

## 📦 Dependencies

- `starlette` - Web framework for A2A servers
- `uvicorn` - ASGI server
- `httpx` - HTTP client for A2A communication
- `streamlit` - Web UI framework
- `finnhub-python` - Financial data API (optional)
- `requests` - HTTP requests
- `chromadb` - Vector database (optional)
- `sentence-transformers` - Text embeddings (optional)

## 🚧 Current Implementation

This system currently uses **mock agents** that simulate financial analysis. To enable real functionality:

1. Set up API keys for external services
2. Implement actual MCP tool servers
3. Replace mock agent logic with real analysis

## 🎯 Future Enhancements

- Real-time data streaming
- Advanced ML models for analysis
- Portfolio management capabilities
- Risk assessment modules
- Multi-language support
- Enhanced visualization

## 📄 License

This project is for educational and demonstration purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Built with ❤️ using Multi-Agent Architecture** 