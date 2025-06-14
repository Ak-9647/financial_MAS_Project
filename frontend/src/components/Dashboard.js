import React, { useState, useEffect } from 'react';
import {
  Grid,
  Card,
  CardContent,
  Typography,
  Box,
  Button,
  TextField,
  IconButton,
  Chip,
  LinearProgress,
  Avatar,
  Divider,
} from '@mui/material';
import {
  TrendingUp,
  Speed,
  CheckCircle,
  Schedule,
  Analytics,
  SmartToy,
  Search,
  PlayArrow,
} from '@mui/icons-material';
import { motion } from 'framer-motion';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, AreaChart, Area } from 'recharts';

import { getSystemMetrics, submitAnalysisRequest, saveAnalysisToHistory } from '../services/api';

const Dashboard = ({ agentStatus, showNotification }) => {
  const [metrics, setMetrics] = useState({});
  const [quickQuery, setQuickQuery] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [recentAnalyses, setRecentAnalyses] = useState([]);

  // Mock data for charts
  const performanceData = [
    { name: 'Mon', analyses: 12, avgTime: 8.5 },
    { name: 'Tue', analyses: 19, avgTime: 9.2 },
    { name: 'Wed', analyses: 15, avgTime: 7.8 },
    { name: 'Thu', analyses: 22, avgTime: 10.1 },
    { name: 'Fri', analyses: 18, avgTime: 8.9 },
    { name: 'Sat', analyses: 8, avgTime: 7.2 },
    { name: 'Sun', analyses: 5, avgTime: 6.8 },
  ];

  const agentActivityData = [
    { name: '00:00', orchestrator: 2, dataGathering: 3, quantitative: 2, qualitative: 1, reportGeneration: 2 },
    { name: '04:00', orchestrator: 1, dataGathering: 2, quantitative: 1, qualitative: 1, reportGeneration: 1 },
    { name: '08:00', orchestrator: 8, dataGathering: 12, quantitative: 10, qualitative: 8, reportGeneration: 9 },
    { name: '12:00', orchestrator: 15, dataGathering: 18, quantitative: 16, qualitative: 14, reportGeneration: 15 },
    { name: '16:00', orchestrator: 12, dataGathering: 15, quantitative: 13, qualitative: 11, reportGeneration: 12 },
    { name: '20:00', orchestrator: 6, dataGathering: 8, quantitative: 7, qualitative: 5, reportGeneration: 6 },
  ];

  useEffect(() => {
    const loadMetrics = async () => {
      try {
        const data = await getSystemMetrics();
        setMetrics(data);
      } catch (error) {
        console.error('Failed to load metrics:', error);
      }
    };

    loadMetrics();
    
    // Mock recent analyses
    setRecentAnalyses([
      { id: 1, query: 'AAPL stock analysis', status: 'completed', time: '2 min ago' },
      { id: 2, query: 'Tesla earnings report', status: 'completed', time: '15 min ago' },
      { id: 3, query: 'NVIDIA vs AMD comparison', status: 'completed', time: '1 hour ago' },
    ]);
  }, []);

  const handleQuickAnalysis = async () => {
    if (!quickQuery.trim()) {
      showNotification('Please enter a query for analysis', 'warning');
      return;
    }

    setIsAnalyzing(true);
    const startTime = Date.now();

    try {
      const result = await submitAnalysisRequest(quickQuery);
      const duration = Date.now() - startTime;

      await saveAnalysisToHistory({
        query: quickQuery,
        result,
        duration: `${(duration / 1000).toFixed(1)}s`,
      });

      showNotification('Analysis completed successfully!', 'success');
      setQuickQuery('');
      
      // Add to recent analyses
      setRecentAnalyses(prev => [
        { id: Date.now(), query: quickQuery, status: 'completed', time: 'Just now' },
        ...prev.slice(0, 2)
      ]);
    } catch (error) {
      showNotification(error.message, 'error');
    } finally {
      setIsAnalyzing(false);
    }
  };

  const getOnlineAgentsCount = () => {
    return Object.values(agentStatus).filter(agent => agent.online).length;
  };

  const MetricCard = ({ title, value, subtitle, icon, color, trend }) => (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <Card
        sx={{
          height: '100%',
          background: 'rgba(255, 255, 255, 0.05)',
          backdropFilter: 'blur(20px)',
          border: '1px solid rgba(255, 255, 255, 0.1)',
          '&:hover': {
            transform: 'translateY(-4px)',
            transition: 'transform 0.3s ease',
          },
        }}
      >
        <CardContent>
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
            <Avatar sx={{ bgcolor: color, width: 48, height: 48 }}>
              {icon}
            </Avatar>
            {trend && (
              <Chip
                label={trend}
                size="small"
                color={trend.startsWith('+') ? 'success' : 'error'}
                sx={{ fontSize: '0.75rem' }}
              />
            )}
          </Box>
          <Typography variant="h4" component="div" sx={{ fontWeight: 700, mb: 1 }}>
            {value}
          </Typography>
          <Typography variant="h6" color="text.secondary" sx={{ mb: 0.5 }}>
            {title}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {subtitle}
          </Typography>
        </CardContent>
      </Card>
    </motion.div>
  );

  return (
    <Box sx={{ flexGrow: 1 }}>
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Box sx={{ mb: 4 }}>
          <Typography variant="h3" component="h1" sx={{ fontWeight: 700, mb: 1 }}>
            Financial MAS Dashboard
          </Typography>
          <Typography variant="h6" color="text.secondary">
            AI-powered financial analysis and investment insights
          </Typography>
        </Box>
      </motion.div>

      {/* Quick Analysis */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.1 }}
      >
        <Card sx={{ mb: 4, background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
          <CardContent>
            <Typography variant="h5" sx={{ mb: 2, display: 'flex', alignItems: 'center', gap: 1 }}>
              <Search />
              Quick Analysis
            </Typography>
            <Box sx={{ display: 'flex', gap: 2, alignItems: 'center' }}>
              <TextField
                fullWidth
                placeholder="Enter stock symbol or query (e.g., 'Analyze AAPL stock performance')"
                value={quickQuery}
                onChange={(e) => setQuickQuery(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleQuickAnalysis()}
                disabled={isAnalyzing}
                sx={{ flexGrow: 1 }}
              />
              <Button
                variant="contained"
                size="large"
                onClick={handleQuickAnalysis}
                disabled={isAnalyzing || !quickQuery.trim()}
                startIcon={isAnalyzing ? null : <PlayArrow />}
                sx={{ minWidth: 120 }}
              >
                {isAnalyzing ? 'Analyzing...' : 'Analyze'}
              </Button>
            </Box>
            {isAnalyzing && (
              <Box sx={{ mt: 2 }}>
                <LinearProgress />
                <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                  AI agents are processing your request...
                </Typography>
              </Box>
            )}
          </CardContent>
        </Card>
      </motion.div>

      {/* Metrics Cards */}
      <Grid container spacing={3} sx={{ mb: 4 }}>
        <Grid item xs={12} sm={6} md={3}>
          <MetricCard
            title="Total Analyses"
            value={metrics.totalAnalyses || '0'}
            subtitle="Completed this month"
            icon={<Analytics />}
            color="primary.main"
            trend="+12%"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <MetricCard
            title="Avg Response Time"
            value={metrics.avgResponseTime || '0s'}
            subtitle="System performance"
            icon={<Speed />}
            color="success.main"
            trend="-8%"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <MetricCard
            title="Success Rate"
            value={metrics.successRate || '0%'}
            subtitle="Analysis accuracy"
            icon={<CheckCircle />}
            color="info.main"
            trend="+2%"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <MetricCard
            title="Active Agents"
            value={`${getOnlineAgentsCount()}/5`}
            subtitle="System status"
            icon={<SmartToy />}
            color={getOnlineAgentsCount() === 5 ? 'success.main' : 'warning.main'}
          />
        </Grid>
      </Grid>

      {/* Charts and Recent Activity */}
      <Grid container spacing={3}>
        {/* Performance Chart */}
        <Grid item xs={12} lg={8}>
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <Card sx={{ height: 400, background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
              <CardContent>
                <Typography variant="h6" sx={{ mb: 2 }}>
                  Weekly Performance
                </Typography>
                <ResponsiveContainer width="100%" height={300}>
                  <AreaChart data={performanceData}>
                    <defs>
                      <linearGradient id="colorAnalyses" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#667eea" stopOpacity={0.8}/>
                        <stop offset="95%" stopColor="#667eea" stopOpacity={0.1}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                    <XAxis dataKey="name" stroke="rgba(255,255,255,0.7)" />
                    <YAxis stroke="rgba(255,255,255,0.7)" />
                    <Tooltip 
                      contentStyle={{ 
                        background: 'rgba(0,0,0,0.8)', 
                        border: '1px solid rgba(255,255,255,0.1)',
                        borderRadius: '8px'
                      }} 
                    />
                    <Area 
                      type="monotone" 
                      dataKey="analyses" 
                      stroke="#667eea" 
                      fillOpacity={1} 
                      fill="url(#colorAnalyses)" 
                    />
                  </AreaChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </motion.div>
        </Grid>

        {/* Recent Analyses */}
        <Grid item xs={12} lg={4}>
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.3 }}
          >
            <Card sx={{ height: 400, background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
              <CardContent>
                <Typography variant="h6" sx={{ mb: 2 }}>
                  Recent Analyses
                </Typography>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                  {recentAnalyses.map((analysis, index) => (
                    <motion.div
                      key={analysis.id}
                      initial={{ opacity: 0, x: 20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: index * 0.1 }}
                    >
                      <Box
                        sx={{
                          p: 2,
                          borderRadius: 2,
                          background: 'rgba(255, 255, 255, 0.05)',
                          border: '1px solid rgba(255, 255, 255, 0.1)',
                        }}
                      >
                        <Typography variant="body2" sx={{ fontWeight: 500, mb: 1 }}>
                          {analysis.query}
                        </Typography>
                        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                          <Chip
                            label={analysis.status}
                            size="small"
                            color="success"
                            sx={{ fontSize: '0.7rem' }}
                          />
                          <Typography variant="caption" color="text.secondary">
                            {analysis.time}
                          </Typography>
                        </Box>
                      </Box>
                    </motion.div>
                  ))}
                </Box>
              </CardContent>
            </Card>
          </motion.div>
        </Grid>

        {/* Agent Activity Chart */}
        <Grid item xs={12}>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
          >
            <Card sx={{ background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
              <CardContent>
                <Typography variant="h6" sx={{ mb: 2 }}>
                  Agent Activity (24h)
                </Typography>
                <ResponsiveContainer width="100%" height={300}>
                  <LineChart data={agentActivityData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                    <XAxis dataKey="name" stroke="rgba(255,255,255,0.7)" />
                    <YAxis stroke="rgba(255,255,255,0.7)" />
                    <Tooltip 
                      contentStyle={{ 
                        background: 'rgba(0,0,0,0.8)', 
                        border: '1px solid rgba(255,255,255,0.1)',
                        borderRadius: '8px'
                      }} 
                    />
                    <Line type="monotone" dataKey="orchestrator" stroke="#667eea" strokeWidth={2} />
                    <Line type="monotone" dataKey="dataGathering" stroke="#764ba2" strokeWidth={2} />
                    <Line type="monotone" dataKey="quantitative" stroke="#4caf50" strokeWidth={2} />
                    <Line type="monotone" dataKey="qualitative" stroke="#ff9800" strokeWidth={2} />
                    <Line type="monotone" dataKey="reportGeneration" stroke="#f44336" strokeWidth={2} />
                  </LineChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </motion.div>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Dashboard; 