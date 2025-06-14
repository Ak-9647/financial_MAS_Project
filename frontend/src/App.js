import React, { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import { Box, Container, Alert, Snackbar, Backdrop } from '@mui/material';
import { motion, AnimatePresence } from 'framer-motion';

// Components
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import AnalysisPage from './components/AnalysisPage';
import AgentStatus from './components/AgentStatus';
import HistoryPage from './components/HistoryPage';

// Services
import { checkAgentStatus } from './services/api';

function App() {
  const [agentStatus, setAgentStatus] = useState({});
  const [notification, setNotification] = useState({ open: false, message: '', severity: 'info' });
  const [loading, setLoading] = useState(true);

  // Check agent status on mount
  useEffect(() => {
    const checkStatus = async () => {
      try {
        const status = await checkAgentStatus();
        setAgentStatus(status);
      } catch (error) {
        console.error('Failed to check agent status:', error);
        setNotification({
          open: true,
          message: 'Failed to connect to agents. Please ensure the system is running.',
          severity: 'error'
        });
      } finally {
        setLoading(false);
      }
    };

    checkStatus();
    
    // Check status every 30 seconds
    const interval = setInterval(checkStatus, 30000);
    return () => clearInterval(interval);
  }, []);

  const showNotification = (message, severity = 'info') => {
    setNotification({ open: true, message, severity });
  };

  const handleCloseNotification = () => {
    setNotification({ ...notification, open: false });
  };

  // Ultra-modern loading screen
  if (loading) {
    return (
      <Backdrop
        open={loading}
        sx={{
          background: 'linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%)',
          zIndex: 9999,
        }}
      >
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
            height: '100vh',
            position: 'relative',
          }}
        >
          {/* Animated background particles */}
          {[...Array(30)].map((_, i) => (
            <motion.div
              key={i}
              style={{
                position: 'absolute',
                width: Math.random() * 6 + 2,
                height: Math.random() * 6 + 2,
                background: `linear-gradient(45deg, #667eea, #764ba2)`,
                borderRadius: '50%',
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
              }}
              animate={{
                y: [0, -50, 0],
                opacity: [0.2, 1, 0.2],
                scale: [1, 1.2, 1],
              }}
              transition={{
                duration: Math.random() * 4 + 3,
                repeat: Infinity,
                delay: Math.random() * 2,
                ease: "easeInOut",
              }}
            />
          ))}
          
          {/* Main loading animation */}
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              zIndex: 1,
            }}
          >
            {/* Spinning loader */}
            <motion.div
              animate={{ rotate: 360 }}
              transition={{ duration: 2, repeat: Infinity, ease: 'linear' }}
              style={{
                width: 80,
                height: 80,
                border: '4px solid rgba(255, 255, 255, 0.1)',
                borderTop: '4px solid #667eea',
                borderRight: '4px solid #764ba2',
                borderRadius: '50%',
                marginBottom: 24,
              }}
            />
            
            {/* Loading text */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3, duration: 0.6 }}
              style={{
                fontSize: '1.5rem',
                fontWeight: 600,
                color: '#ffffff',
                textAlign: 'center',
                marginBottom: 8,
              }}
            >
              Financial MAS
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.6, duration: 0.6 }}
              style={{
                fontSize: '1rem',
                color: 'rgba(255, 255, 255, 0.7)',
                textAlign: 'center',
              }}
            >
              Initializing AI Agents...
            </motion.div>
          </motion.div>
        </Box>
      </Backdrop>
    );
  }

  return (
    <Box
      sx={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%)',
        position: 'relative',
        overflow: 'hidden',
      }}
    >
      {/* Enhanced animated background elements */}
      <Box
        sx={{
          position: 'fixed',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          zIndex: -2,
          opacity: 0.15,
        }}
      >
        {/* Floating particles */}
        {[...Array(25)].map((_, i) => (
          <motion.div
            key={`particle-${i}`}
            style={{
              position: 'absolute',
              width: Math.random() * 4 + 1,
              height: Math.random() * 4 + 1,
              background: i % 3 === 0 ? '#667eea' : i % 3 === 1 ? '#764ba2' : '#ff6b6b',
              borderRadius: '50%',
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              y: [0, -40, 0],
              x: [0, Math.random() * 20 - 10, 0],
              opacity: [0.3, 1, 0.3],
              scale: [1, 1.2, 1],
            }}
            transition={{
              duration: Math.random() * 4 + 3,
              repeat: Infinity,
              delay: Math.random() * 2,
              ease: "easeInOut",
            }}
          />
        ))}
        
        {/* Geometric shapes */}
        {[...Array(8)].map((_, i) => (
          <motion.div
            key={`shape-${i}`}
            style={{
              position: 'absolute',
              width: Math.random() * 60 + 40,
              height: Math.random() * 60 + 40,
              background: `linear-gradient(45deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1))`,
              borderRadius: i % 2 === 0 ? '50%' : '20%',
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              backdropFilter: 'blur(1px)',
            }}
            animate={{
              rotate: [0, 360],
              scale: [1, 1.1, 1],
              opacity: [0.1, 0.3, 0.1],
            }}
            transition={{
              duration: Math.random() * 20 + 15,
              repeat: Infinity,
              delay: Math.random() * 5,
              ease: "linear",
            }}
          />
        ))}
      </Box>

      {/* Gradient overlay */}
      <Box
        sx={{
          position: 'fixed',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          zIndex: -1,
          background: 'radial-gradient(circle at 20% 80%, rgba(102, 126, 234, 0.1) 0%, transparent 50%), radial-gradient(circle at 80% 20%, rgba(118, 75, 162, 0.1) 0%, transparent 50%)',
        }}
      />

      <Navbar agentStatus={agentStatus} />
      
      <Container maxWidth="xl" sx={{ py: 3 }}>
        <AnimatePresence mode="wait">
          <Routes>
            <Route 
              path="/" 
              element={
                <motion.div
                  key="dashboard"
                  initial={{ opacity: 0, y: 30, scale: 0.95 }}
                  animate={{ opacity: 1, y: 0, scale: 1 }}
                  exit={{ opacity: 0, y: -30, scale: 0.95 }}
                  transition={{ 
                    duration: 0.4,
                    ease: [0.4, 0, 0.2, 1]
                  }}
                >
                  <Dashboard 
                    agentStatus={agentStatus} 
                    showNotification={showNotification}
                  />
                </motion.div>
              } 
            />
            <Route 
              path="/analysis" 
              element={
                <motion.div
                  key="analysis"
                  initial={{ opacity: 0, y: 30, scale: 0.95 }}
                  animate={{ opacity: 1, y: 0, scale: 1 }}
                  exit={{ opacity: 0, y: -30, scale: 0.95 }}
                  transition={{ 
                    duration: 0.4,
                    ease: [0.4, 0, 0.2, 1]
                  }}
                >
                  <AnalysisPage showNotification={showNotification} />
                </motion.div>
              } 
            />
            <Route 
              path="/agents" 
              element={
                <motion.div
                  key="agents"
                  initial={{ opacity: 0, y: 30, scale: 0.95 }}
                  animate={{ opacity: 1, y: 0, scale: 1 }}
                  exit={{ opacity: 0, y: -30, scale: 0.95 }}
                  transition={{ 
                    duration: 0.4,
                    ease: [0.4, 0, 0.2, 1]
                  }}
                >
                  <AgentStatus 
                    agentStatus={agentStatus} 
                    setAgentStatus={setAgentStatus}
                  />
                </motion.div>
              } 
            />
            <Route 
              path="/history" 
              element={
                <motion.div
                  key="history"
                  initial={{ opacity: 0, y: 30, scale: 0.95 }}
                  animate={{ opacity: 1, y: 0, scale: 1 }}
                  exit={{ opacity: 0, y: -30, scale: 0.95 }}
                  transition={{ 
                    duration: 0.4,
                    ease: [0.4, 0, 0.2, 1]
                  }}
                >
                  <HistoryPage />
                </motion.div>
              } 
            />
          </Routes>
        </AnimatePresence>
      </Container>

      {/* Enhanced Notification Snackbar */}
      <Snackbar
        open={notification.open}
        autoHideDuration={6000}
        onClose={handleCloseNotification}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
      >
        <Alert 
          onClose={handleCloseNotification}
          severity={notification.severity}
          variant="filled"
          sx={{
            background: notification.severity === 'success' 
              ? 'linear-gradient(135deg, #00e676 0%, #00c853 100%)'
              : notification.severity === 'error'
              ? 'linear-gradient(135deg, #ff5252 0%, #c50e29 100%)'
              : notification.severity === 'warning'
              ? 'linear-gradient(135deg, #ffab00 0%, #c77800 100%)'
              : 'linear-gradient(135deg, #40c4ff 0%, #0094cc 100%)',
            backdropFilter: 'blur(20px)',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            borderRadius: 2,
            boxShadow: '0 8px 32px rgba(0, 0, 0, 0.3)',
          }}
        >
          {notification.message}
        </Alert>
      </Snackbar>
    </Box>
  );
}

export default App; 