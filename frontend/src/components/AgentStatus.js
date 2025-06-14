import React, { useState, useEffect } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  Grid,
  Chip,
  Avatar,
  Button,
  IconButton,
  LinearProgress,
  Tooltip,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
} from '@mui/material';
import {
  SmartToy,
  Refresh,
  PlayArrow,
  Stop,
  Info,
  CheckCircle,
  Error,
  Warning,
  Schedule,
} from '@mui/icons-material';
import { motion } from 'framer-motion';
import { checkAgentStatus } from '../services/api';

const AgentStatus = ({ agentStatus, setAgentStatus }) => {
  const [loading, setLoading] = useState(false);
  const [selectedAgent, setSelectedAgent] = useState(null);
  const [dialogOpen, setDialogOpen] = useState(false);

  const agentInfo = {
    orchestrator: {
      name: 'Orchestrator Agent',
      description: 'Coordinates the entire analysis workflow and manages task distribution',
      port: 9000,
      color: '#667eea',
      icon: '🎯',
    },
    dataGathering: {
      name: 'Data Gathering Agent',
      description: 'Retrieves financial data from APIs and performs web research',
      port: 9001,
      color: '#764ba2',
      icon: '📊',
    },
    quantitative: {
      name: 'Quantitative Analysis Agent',
      description: 'Performs statistical analysis and financial calculations',
      port: 9002,
      color: '#4caf50',
      icon: '📈',
    },
    qualitative: {
      name: 'Qualitative Analysis Agent',
      description: 'Analyzes sentiment, news, and market perception',
      port: 9003,
      color: '#ff9800',
      icon: '🧠',
    },
    reportGeneration: {
      name: 'Report Generation Agent',
      description: 'Synthesizes findings into comprehensive investment reports',
      port: 9004,
      color: '#f44336',
      icon: '📋',
    },
  };

  const refreshStatus = async () => {
    setLoading(true);
    try {
      const status = await checkAgentStatus();
      setAgentStatus(status);
    } catch (error) {
      console.error('Failed to refresh agent status:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleAgentClick = (agentKey) => {
    setSelectedAgent({ key: agentKey, ...agentInfo[agentKey], status: agentStatus[agentKey] });
    setDialogOpen(true);
  };

  const getStatusIcon = (status) => {
    if (!status) return <Warning color="disabled" />;
    if (status.online) return <CheckCircle color="success" />;
    return <Error color="error" />;
  };

  const getStatusColor = (status) => {
    if (!status) return 'default';
    if (status.online) return 'success';
    return 'error';
  };

  const getStatusText = (status) => {
    if (!status) return 'Unknown';
    if (status.online) return 'Online';
    return 'Offline';
  };

  const getUptime = (status) => {
    if (!status || !status.online) return 'N/A';
    const lastCheck = new Date(status.lastCheck);
    const now = new Date();
    const diff = now - lastCheck;
    const minutes = Math.floor(diff / 60000);
    if (minutes < 1) return 'Just now';
    if (minutes < 60) return `${minutes}m ago`;
    const hours = Math.floor(minutes / 60);
    return `${hours}h ${minutes % 60}m ago`;
  };

  useEffect(() => {
    // Auto-refresh every 30 seconds
    const interval = setInterval(refreshStatus, 30000);
    return () => clearInterval(interval);
  }, []);

  const onlineCount = Object.values(agentStatus).filter(agent => agent?.online).length;
  const totalCount = Object.keys(agentStatus).length;

  return (
    <Box sx={{ flexGrow: 1 }}>
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Box sx={{ mb: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Box>
            <Typography variant="h3" component="h1" sx={{ fontWeight: 700, mb: 1 }}>
              Agent Status
            </Typography>
            <Typography variant="h6" color="text.secondary">
              Monitor and manage your AI agents
            </Typography>
          </Box>
          <Button
            variant="contained"
            startIcon={<Refresh />}
            onClick={refreshStatus}
            disabled={loading}
          >
            Refresh Status
          </Button>
        </Box>
      </motion.div>

      {/* System Overview */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.1 }}
      >
        <Card sx={{ mb: 4, background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
          <CardContent>
            <Typography variant="h5" sx={{ mb: 3 }}>
              System Overview
            </Typography>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={6} md={3}>
                <Box sx={{ textAlign: 'center' }}>
                  <Typography variant="h3" sx={{ fontWeight: 700, color: 'primary.main' }}>
                    {onlineCount}/{totalCount}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Agents Online
                  </Typography>
                </Box>
              </Grid>
              <Grid item xs={12} sm={6} md={3}>
                <Box sx={{ textAlign: 'center' }}>
                  <Typography variant="h3" sx={{ fontWeight: 700, color: 'success.main' }}>
                    {onlineCount === totalCount ? '100%' : Math.round((onlineCount / totalCount) * 100) + '%'}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    System Health
                  </Typography>
                </Box>
              </Grid>
              <Grid item xs={12} sm={6} md={3}>
                <Box sx={{ textAlign: 'center' }}>
                  <Typography variant="h3" sx={{ fontWeight: 700, color: 'info.main' }}>
                    5
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Total Agents
                  </Typography>
                </Box>
              </Grid>
              <Grid item xs={12} sm={6} md={3}>
                <Box sx={{ textAlign: 'center' }}>
                  <Typography variant="h3" sx={{ fontWeight: 700, color: 'warning.main' }}>
                    24/7
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Monitoring
                  </Typography>
                </Box>
              </Grid>
            </Grid>
            {loading && <LinearProgress sx={{ mt: 2 }} />}
          </CardContent>
        </Card>
      </motion.div>

      {/* Agent Cards */}
      <Grid container spacing={3}>
        {Object.entries(agentInfo).map(([agentKey, info], index) => {
          const status = agentStatus[agentKey];
          return (
            <Grid item xs={12} md={6} lg={4} key={agentKey}>
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.2 + index * 0.1 }}
              >
                <Card
                  sx={{
                    height: '100%',
                    background: 'rgba(255, 255, 255, 0.05)',
                    backdropFilter: 'blur(20px)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    cursor: 'pointer',
                    transition: 'transform 0.3s ease',
                    '&:hover': {
                      transform: 'translateY(-4px)',
                    },
                  }}
                  onClick={() => handleAgentClick(agentKey)}
                >
                  <CardContent>
                    <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
                      <Avatar
                        sx={{
                          bgcolor: info.color,
                          width: 56,
                          height: 56,
                          fontSize: '1.5rem',
                        }}
                      >
                        {info.icon}
                      </Avatar>
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                        {getStatusIcon(status)}
                        <Chip
                          label={getStatusText(status)}
                          color={getStatusColor(status)}
                          size="small"
                        />
                      </Box>
                    </Box>

                    <Typography variant="h6" sx={{ fontWeight: 600, mb: 1 }}>
                      {info.name}
                    </Typography>
                    
                    <Typography variant="body2" color="text.secondary" sx={{ mb: 2, minHeight: 40 }}>
                      {info.description}
                    </Typography>

                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                      <Typography variant="caption" color="text.secondary">
                        Port: {info.port}
                      </Typography>
                      <Typography variant="caption" color="text.secondary">
                        Last Check: {getUptime(status)}
                      </Typography>
                    </Box>

                    <Box sx={{ display: 'flex', gap: 1 }}>
                      <Tooltip title="View Details">
                        <IconButton size="small" onClick={(e) => { e.stopPropagation(); handleAgentClick(agentKey); }}>
                          <Info />
                        </IconButton>
                      </Tooltip>
                      <Tooltip title="Restart Agent">
                        <IconButton size="small" disabled={!status?.online}>
                          <Refresh />
                        </IconButton>
                      </Tooltip>
                      <Tooltip title={status?.online ? 'Stop Agent' : 'Start Agent'}>
                        <IconButton size="small">
                          {status?.online ? <Stop /> : <PlayArrow />}
                        </IconButton>
                      </Tooltip>
                    </Box>
                  </CardContent>
                </Card>
              </motion.div>
            </Grid>
          );
        })}
      </Grid>

      {/* Agent Details Dialog */}
      <Dialog
        open={dialogOpen}
        onClose={() => setDialogOpen(false)}
        maxWidth="md"
        fullWidth
        PaperProps={{
          sx: {
            background: 'rgba(255, 255, 255, 0.05)',
            backdropFilter: 'blur(20px)',
            border: '1px solid rgba(255, 255, 255, 0.1)',
          },
        }}
      >
        {selectedAgent && (
          <>
            <DialogTitle>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                <Avatar sx={{ bgcolor: selectedAgent.color }}>
                  {selectedAgent.icon}
                </Avatar>
                <Box>
                  <Typography variant="h6">{selectedAgent.name}</Typography>
                  <Chip
                    label={getStatusText(selectedAgent.status)}
                    color={getStatusColor(selectedAgent.status)}
                    size="small"
                  />
                </Box>
              </Box>
            </DialogTitle>
            <DialogContent>
              <Typography variant="body1" sx={{ mb: 3 }}>
                {selectedAgent.description}
              </Typography>

              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <Typography variant="subtitle2" color="text.secondary">
                    Port
                  </Typography>
                  <Typography variant="body1">{selectedAgent.port}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="subtitle2" color="text.secondary">
                    Status
                  </Typography>
                  <Typography variant="body1">
                    {selectedAgent.status?.online ? 'Online' : 'Offline'}
                  </Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="subtitle2" color="text.secondary">
                    Last Check
                  </Typography>
                  <Typography variant="body1">
                    {selectedAgent.status?.lastCheck 
                      ? new Date(selectedAgent.status.lastCheck).toLocaleString()
                      : 'Never'
                    }
                  </Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="subtitle2" color="text.secondary">
                    Endpoint
                  </Typography>
                  <Typography variant="body1" sx={{ fontFamily: 'monospace', fontSize: '0.9rem' }}>
                    http://localhost:{selectedAgent.port}
                  </Typography>
                </Grid>
              </Grid>

              {selectedAgent.status?.error && (
                <Box sx={{ mt: 2, p: 2, bgcolor: 'error.dark', borderRadius: 1 }}>
                  <Typography variant="subtitle2" sx={{ mb: 1 }}>
                    Error Details:
                  </Typography>
                  <Typography variant="body2" sx={{ fontFamily: 'monospace' }}>
                    {selectedAgent.status.error}
                  </Typography>
                </Box>
              )}

              {selectedAgent.status?.info && (
                <Box sx={{ mt: 2, p: 2, bgcolor: 'rgba(255, 255, 255, 0.05)', borderRadius: 1 }}>
                  <Typography variant="subtitle2" sx={{ mb: 1 }}>
                    Agent Information:
                  </Typography>
                  <pre style={{ fontSize: '0.8rem', overflow: 'auto' }}>
                    {JSON.stringify(selectedAgent.status.info, null, 2)}
                  </pre>
                </Box>
              )}
            </DialogContent>
            <DialogActions>
              <Button onClick={() => setDialogOpen(false)}>Close</Button>
              <Button variant="contained" startIcon={<Refresh />}>
                Restart Agent
              </Button>
            </DialogActions>
          </>
        )}
      </Dialog>
    </Box>
  );
};

export default AgentStatus; 