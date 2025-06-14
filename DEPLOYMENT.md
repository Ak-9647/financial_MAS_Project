# 🚀 Deployment Guide - Financial MAS

This guide covers deploying the Financial Multi-Agent System to various environments, from local development to production cloud deployments.

## 📋 Table of Contents

- [Overview](#overview)
- [Local Development](#local-development)
- [Production Deployment](#production-deployment)
- [Docker Deployment](#docker-deployment)
- [Cloud Deployment](#cloud-deployment)
- [Environment Configuration](#environment-configuration)
- [Monitoring & Logging](#monitoring--logging)
- [Security Considerations](#security-considerations)
- [Troubleshooting](#troubleshooting)

## 🏗️ Overview

The Financial MAS consists of multiple components that need to be deployed:

### Backend Components
- **5 AI Agents** (Orchestrator, Data Gathering, Quantitative, Qualitative, Report Generation)
- **3 MCP Tool Servers** (Optional: Financial Data, Web Research, Knowledge Base)
- **Python Dependencies** and environment configuration

### Frontend Components
- **React Application** (Primary UI)
- **Streamlit Application** (Alternative UI)
- **Static Assets** and build artifacts

## 💻 Local Development

### Quick Start (Recommended)

```bash
# Clone and setup
git clone https://github.com/yourusername/financial_mas_project.git
cd financial_mas_project

# Backend setup
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Environment configuration
python3 setup_env.py
# Edit .env with your API keys

# Start backend
python start_system.py

# Start frontend (new terminal)
cd frontend
npm install
npm start
```

### Manual Development Setup

```bash
# Backend - Start each agent manually
python run_orchestrator_a2a_server.py          # Port 9000
python run_data_gathering_a2a_server.py        # Port 9001
python run_quantitative_analysis_a2a_server.py # Port 9002
python run_qualitative_analysis_a2a_server.py  # Port 9003
python run_report_generation_a2a_server.py     # Port 9004

# Optional MCP Servers
python mcp_servers/financial_data_server.py     # Port 8001
python mcp_servers/web_research_server.py       # Port 8002
python mcp_servers/knowledge_base_server.py     # Port 8003

# Frontend
cd frontend
npm run build  # For production build
npm start      # For development
```

## 🏭 Production Deployment

### System Requirements

**Minimum Requirements:**
- **CPU**: 2 cores
- **RAM**: 4GB
- **Storage**: 10GB
- **OS**: Ubuntu 20.04+, CentOS 8+, or macOS 10.15+

**Recommended for Production:**
- **CPU**: 4+ cores
- **RAM**: 8GB+
- **Storage**: 50GB+ SSD
- **OS**: Ubuntu 22.04 LTS

### Production Setup

#### 1. Server Preparation

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.8+
sudo apt install python3 python3-pip python3-venv -y

# Install Node.js 16+
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install process manager
sudo npm install -g pm2

# Install reverse proxy
sudo apt install nginx -y
```

#### 2. Application Deployment

```bash
# Clone repository
git clone https://github.com/yourusername/financial_mas_project.git
cd financial_mas_project

# Create production user
sudo useradd -m -s /bin/bash financial-mas
sudo chown -R financial-mas:financial-mas /opt/financial-mas

# Setup Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Build frontend
cd frontend
npm ci --production
npm run build
cd ..

# Setup environment
cp env.example .env
# Configure production environment variables
```

#### 3. Process Management with PM2

Create `ecosystem.config.js`:

```javascript
module.exports = {
  apps: [
    {
      name: 'orchestrator',
      script: 'run_orchestrator_a2a_server.py',
      interpreter: 'python3',
      cwd: '/opt/financial-mas',
      env: {
        PORT: 9000,
        NODE_ENV: 'production'
      }
    },
    {
      name: 'data-gathering',
      script: 'run_data_gathering_a2a_server.py',
      interpreter: 'python3',
      cwd: '/opt/financial-mas',
      env: { PORT: 9001 }
    },
    {
      name: 'quantitative',
      script: 'run_quantitative_analysis_a2a_server.py',
      interpreter: 'python3',
      cwd: '/opt/financial-mas',
      env: { PORT: 9002 }
    },
    {
      name: 'qualitative',
      script: 'run_qualitative_analysis_a2a_server.py',
      interpreter: 'python3',
      cwd: '/opt/financial-mas',
      env: { PORT: 9003 }
    },
    {
      name: 'report-generation',
      script: 'run_report_generation_a2a_server.py',
      interpreter: 'python3',
      cwd: '/opt/financial-mas',
      env: { PORT: 9004 }
    }
  ]
};
```

Start services:

```bash
# Start all services
pm2 start ecosystem.config.js

# Save PM2 configuration
pm2 save
pm2 startup

# Monitor services
pm2 monit
```

#### 4. Nginx Configuration

Create `/etc/nginx/sites-available/financial-mas`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    # Frontend (React build)
    location / {
        root /opt/financial-mas/frontend/build;
        index index.html index.htm;
        try_files $uri $uri/ /index.html;
    }

    # API endpoints
    location /api/ {
        proxy_pass http://localhost:9000/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }

    # Streamlit alternative UI
    location /streamlit/ {
        proxy_pass http://localhost:8501/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Enable site:

```bash
sudo ln -s /etc/nginx/sites-available/financial-mas /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 🐳 Docker Deployment

### Docker Compose Setup

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  # Backend Services
  orchestrator:
    build: .
    command: python run_orchestrator_a2a_server.py
    ports:
      - "9000:9000"
    environment:
      - PORT=9000
    env_file:
      - .env
    restart: unless-stopped

  data-gathering:
    build: .
    command: python run_data_gathering_a2a_server.py
    ports:
      - "9001:9001"
    environment:
      - PORT=9001
    env_file:
      - .env
    restart: unless-stopped

  quantitative:
    build: .
    command: python run_quantitative_analysis_a2a_server.py
    ports:
      - "9002:9002"
    environment:
      - PORT=9002
    env_file:
      - .env
    restart: unless-stopped

  qualitative:
    build: .
    command: python run_qualitative_analysis_a2a_server.py
    ports:
      - "9003:9003"
    environment:
      - PORT=9003
    env_file:
      - .env
    restart: unless-stopped

  report-generation:
    build: .
    command: python run_report_generation_a2a_server.py
    ports:
      - "9004:9004"
    environment:
      - PORT=9004
    env_file:
      - .env
    restart: unless-stopped

  # Frontend
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    depends_on:
      - orchestrator
    restart: unless-stopped

  # Reverse Proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - frontend
      - orchestrator
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

### Dockerfile for Backend

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "run_orchestrator_a2a_server.py"]
```

### Frontend Dockerfile

Create `frontend/Dockerfile`:

```dockerfile
# Build stage
FROM node:18-alpine as build

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Deploy with Docker

```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f

# Scale services
docker-compose up -d --scale quantitative=2

# Stop services
docker-compose down
```

## ☁️ Cloud Deployment

### AWS Deployment

#### Using AWS ECS (Recommended)

1. **Create ECS Cluster**:
```bash
aws ecs create-cluster --cluster-name financial-mas-cluster
```

2. **Build and Push Images**:
```bash
# Build images
docker build -t financial-mas-backend .
docker build -t financial-mas-frontend ./frontend

# Tag for ECR
docker tag financial-mas-backend:latest 123456789012.dkr.ecr.us-west-2.amazonaws.com/financial-mas-backend:latest
docker tag financial-mas-frontend:latest 123456789012.dkr.ecr.us-west-2.amazonaws.com/financial-mas-frontend:latest

# Push to ECR
docker push 123456789012.dkr.ecr.us-west-2.amazonaws.com/financial-mas-backend:latest
docker push 123456789012.dkr.ecr.us-west-2.amazonaws.com/financial-mas-frontend:latest
```

3. **Create Task Definitions** and **Services** via AWS Console or CLI

#### Using AWS Lambda (Serverless)

For serverless deployment, create individual Lambda functions for each agent:

```python
# lambda_handler.py for each agent
import json
from agents.orchestrator_agent import OrchestratorAgent

def lambda_handler(event, context):
    agent = OrchestratorAgent()
    result = agent.process_request(event['body'])
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(result)
    }
```

### Google Cloud Platform

#### Using Cloud Run

```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT_ID/financial-mas-backend
gcloud run deploy financial-mas-backend \
  --image gcr.io/PROJECT_ID/financial-mas-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Microsoft Azure

#### Using Container Instances

```bash
# Create resource group
az group create --name financial-mas-rg --location eastus

# Deploy container
az container create \
  --resource-group financial-mas-rg \
  --name financial-mas-backend \
  --image your-registry/financial-mas-backend:latest \
  --ports 9000 \
  --environment-variables PORT=9000
```

## ⚙️ Environment Configuration

### Production Environment Variables

Create `.env.production`:

```bash
# Application
NODE_ENV=production
DEBUG=false
LOG_LEVEL=info

# API Keys (Required for full functionality)
FINNHUB_API_KEY=your_finnhub_api_key
SERPER_API_KEY=your_serper_api_key
OPENAI_API_KEY=your_openai_api_key

# Database (if using)
DATABASE_URL=postgresql://user:password@localhost:5432/financial_mas
REDIS_URL=redis://localhost:6379

# Security
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=your-domain.com,www.your-domain.com

# CORS
CORS_ALLOWED_ORIGINS=https://your-domain.com,https://www.your-domain.com

# Monitoring
SENTRY_DSN=your_sentry_dsn_here
```

### SSL/TLS Configuration

For production, enable HTTPS:

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 📊 Monitoring & Logging

### Application Monitoring

#### Using PM2 Monitoring

```bash
# Install PM2 monitoring
pm2 install pm2-server-monit

# View real-time monitoring
pm2 monit

# View logs
pm2 logs
pm2 logs orchestrator
```

#### Health Check Endpoints

Add health checks to each agent:

```python
# In each agent server
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }
```

### Logging Configuration

Create `logging.conf`:

```ini
[loggers]
keys=root,financial_mas

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=INFO
handlers=consoleHandler

[logger_financial_mas]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=financial_mas
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('/var/log/financial-mas/app.log',)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

## 🔒 Security Considerations

### Production Security Checklist

- [ ] **Environment Variables**: Store sensitive data in environment variables, not code
- [ ] **HTTPS**: Enable SSL/TLS for all communications
- [ ] **API Keys**: Rotate API keys regularly
- [ ] **Access Control**: Implement proper authentication and authorization
- [ ] **Rate Limiting**: Add rate limiting to prevent abuse
- [ ] **Input Validation**: Validate all user inputs
- [ ] **CORS**: Configure CORS properly for production domains
- [ ] **Security Headers**: Add security headers (HSTS, CSP, etc.)
- [ ] **Updates**: Keep all dependencies updated
- [ ] **Monitoring**: Monitor for security incidents

### Firewall Configuration

```bash
# Ubuntu UFW
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw --force enable

# Block direct access to backend ports
sudo ufw deny 9000:9004/tcp
```

## 🐛 Troubleshooting

### Common Issues

#### Backend Services Not Starting

```bash
# Check port availability
sudo netstat -tlnp | grep :9000

# Check logs
pm2 logs orchestrator

# Restart service
pm2 restart orchestrator
```

#### Frontend Build Issues

```bash
# Clear cache and rebuild
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run build
```

#### Database Connection Issues

```bash
# Check database status
sudo systemctl status postgresql

# Test connection
psql -h localhost -U username -d financial_mas
```

### Performance Optimization

#### Backend Optimization

```python
# Use connection pooling
import asyncio
import aiohttp

class OptimizedAgent:
    def __init__(self):
        self.session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(limit=100)
        )
```

#### Frontend Optimization

```javascript
// Code splitting
const AnalysisPage = lazy(() => import('./components/AnalysisPage'));

// Memoization
const MemoizedComponent = React.memo(ExpensiveComponent);
```

### Monitoring Commands

```bash
# System resources
htop
df -h
free -h

# Application processes
pm2 status
pm2 monit

# Network connections
sudo netstat -tlnp
sudo ss -tlnp

# Logs
tail -f /var/log/financial-mas/app.log
journalctl -u nginx -f
```

## 📞 Support

For deployment issues:

- **Documentation**: Check this guide and README.md
- **GitHub Issues**: Report deployment-specific issues
- **Community**: Join discussions for deployment help

---

**🚀 Happy Deploying!**

*This guide covers most deployment scenarios. For specific cloud providers or custom setups, refer to their documentation and adapt these instructions accordingly.* 