# 🚀 How to Run Your Financial Multi-Agent System

## Quick Start (3 Steps)

### 1. Start the System
```bash
python3 start_system.py
```
Wait for all agents to start (you'll see "✅ Started 5 agents successfully!")

### 2. Run Quick Test
```bash
python3 quick_test.py
```

### 3. Test Complete System
```bash
python3 test_system.py
```

---

## 📋 Available Test Commands

| Command | Purpose |
|---------|---------|
| `python3 quick_test.py` | Fast system check (30 seconds) |
| `python3 test_system.py` | Complete system test (2 minutes) |
| `python3 check_api_keys.py` | Verify API keys are working |

---

## 🔧 Manual Testing

### Test Individual Agents
```bash
# Check if all agents are running
curl http://localhost:9000/.well-known/agent.json  # Orchestrator
curl http://localhost:9001/.well-known/agent.json  # Data Gathering
curl http://localhost:9002/.well-known/agent.json  # Quantitative
curl http://localhost:9003/.well-known/agent.json  # Qualitative
curl http://localhost:9004/.well-known/agent.json  # Report Generation
```

### Test Financial Analysis
```bash
curl -X POST http://localhost:9000/ \
  -H "Content-Type: application/json" \
  -d '{"message": {"role": "user", "parts": [{"text": "{\"query\": \"Analyze Apple stock\"}"}]}}'
```

### Test Real Financial Data
```bash
curl -X POST http://localhost:8001/call \
  -H "Content-Type: application/json" \
  -d '{"tool": "get_stock_price", "params": {"symbol": "AAPL"}}'
```

---

## 🎯 What Should Work

✅ **Multi-Agent Workflow**: All 5 agents coordinate to analyze stocks  
✅ **Real Financial Data**: Live stock prices from Finnhub API  
✅ **Web Research**: Google search via Serper.dev API  
✅ **Agent Communication**: A2A protocol between agents  
✅ **Error Handling**: Graceful fallbacks when APIs fail  

---

## 🔍 System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Orchestrator  │────│ Data Gathering  │────│  Quantitative   │
│   (Port 9000)   │    │   (Port 9001)   │    │   (Port 9002)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
         ┌─────────────────┐    ┌─────────────────┐
         │   Qualitative   │────│ Report Generator│
         │   (Port 9003)   │    │   (Port 9004)   │
         └─────────────────┘    └─────────────────┘
```

---

## 🛠️ Troubleshooting

### System Won't Start
```bash
# Kill existing processes
pkill -f "python3.*start_system"
pkill -f "python3.*900"

# Restart
python3 start_system.py
```

### API Keys Not Working
```bash
python3 check_api_keys.py
```
Update your `.env` file with valid keys from:
- [Finnhub](https://finnhub.io/) (Free)
- [Serper.dev](https://serper.dev/) (Free)
- [OpenAI](https://platform.openai.com/) (Paid)

### Port Already in Use
```bash
# Check what's using the ports
lsof -i :9000
lsof -i :9001

# Kill specific processes
kill -9 <PID>
```

---

## 📊 Example Queries to Test

Try these queries with your system:

```bash
# Apple Stock Analysis
curl -X POST http://localhost:9000/ -H "Content-Type: application/json" \
  -d '{"message": {"role": "user", "parts": [{"text": "{\"query\": \"Analyze Apple (AAPL) stock performance and provide investment recommendation\"}"}]}}'

# Tesla Analysis
curl -X POST http://localhost:9000/ -H "Content-Type: application/json" \
  -d '{"message": {"role": "user", "parts": [{"text": "{\"query\": \"Analyze Tesla stock with current market data\"}"}]}}'

# Microsoft Analysis
curl -X POST http://localhost:9000/ -H "Content-Type: application/json" \
  -d '{"message": {"role": "user", "parts": [{"text": "{\"query\": \"Provide investment analysis for Microsoft\"}"}]}}'
```

---

## 🎉 Success Indicators

When everything is working, you should see:

✅ **All 5 agents responding** (ports 9000-9004)  
✅ **Real stock prices** (not mock data)  
✅ **4/4 workflow steps completed**  
✅ **JSON responses** with analysis results  
✅ **No connection errors** in tests  

---

## 🔗 Access Points

- **Main API**: http://localhost:9000/
- **Agent Discovery**: http://localhost:9001/.well-known/agent.json
- **Financial Data**: http://localhost:8001/tools
- **System Status**: Run `python3 quick_test.py`

---

## 📞 Need Help?

1. Run `python3 check_api_keys.py` to verify API setup
2. Run `python3 quick_test.py` for fast diagnosis
3. Check the terminal output for error messages
4. Ensure all required ports (8001, 9000-9004) are available

Your Financial Multi-Agent System is ready to analyze stocks! 🚀 