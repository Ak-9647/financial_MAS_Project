import axios from 'axios';

// Base API configuration
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:9000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Agent endpoints
const AGENT_ENDPOINTS = {
  orchestrator: 'http://localhost:9000',
  dataGathering: 'http://localhost:9001',
  quantitative: 'http://localhost:9002',
  qualitative: 'http://localhost:9003',
  reportGeneration: 'http://localhost:9004',
};

// Check if all agents are running
export const checkAgentStatus = async () => {
  const status = {};
  
  for (const [agentName, endpoint] of Object.entries(AGENT_ENDPOINTS)) {
    try {
      const response = await axios.get(`${endpoint}/.well-known/agent.json`, {
        timeout: 5000,
      });
      status[agentName] = {
        online: true,
        lastCheck: new Date().toISOString(),
        info: response.data,
      };
    } catch (error) {
      status[agentName] = {
        online: false,
        lastCheck: new Date().toISOString(),
        error: error.message,
      };
    }
  }
  
  return status;
};

// Submit analysis request
export const submitAnalysisRequest = async (query) => {
  try {
    const response = await api.post('/', {
      message: {
        role: 'user',
        parts: [{ text: JSON.stringify({ query }) }],
      },
    });
    
    return response.data;
  } catch (error) {
    console.error('Analysis request failed:', error);
    throw new Error(
      error.response?.data?.message || 
      'Failed to submit analysis request. Please check if the system is running.'
    );
  }
};

// Get analysis history (mock for now - you can implement storage later)
export const getAnalysisHistory = async () => {
  // This would typically fetch from a database or local storage
  const history = JSON.parse(localStorage.getItem('analysisHistory') || '[]');
  return history.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
};

// Save analysis to history
export const saveAnalysisToHistory = async (analysis) => {
  const history = JSON.parse(localStorage.getItem('analysisHistory') || '[]');
  const newEntry = {
    id: Date.now().toString(),
    timestamp: new Date().toISOString(),
    query: analysis.query,
    result: analysis.result,
    duration: analysis.duration,
  };
  
  history.unshift(newEntry);
  
  // Keep only last 50 analyses
  if (history.length > 50) {
    history.splice(50);
  }
  
  localStorage.setItem('analysisHistory', JSON.stringify(history));
  return newEntry;
};

// Delete analysis from history
export const deleteAnalysisFromHistory = async (id) => {
  const history = JSON.parse(localStorage.getItem('analysisHistory') || '[]');
  const filtered = history.filter(item => item.id !== id);
  localStorage.setItem('analysisHistory', JSON.stringify(filtered));
  return filtered;
};

// Get system metrics (mock data for demo)
export const getSystemMetrics = async () => {
  return {
    totalAnalyses: JSON.parse(localStorage.getItem('analysisHistory') || '[]').length,
    avgResponseTime: '12.3s',
    successRate: '98.5%',
    uptime: '99.2%',
    activeAgents: 5,
    lastUpdate: new Date().toISOString(),
  };
};

// WebSocket connection for real-time updates (optional)
export const connectWebSocket = (onMessage) => {
  // This would connect to a WebSocket endpoint for real-time updates
  // For now, we'll use polling
  const interval = setInterval(async () => {
    try {
      const status = await checkAgentStatus();
      onMessage({ type: 'agent_status', data: status });
    } catch (error) {
      console.error('WebSocket polling error:', error);
    }
  }, 10000);
  
  return () => clearInterval(interval);
};

export default api; 