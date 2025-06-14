import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  IconButton,
  Badge,
  Menu,
  MenuItem,
  Chip,
  useMediaQuery,
  useTheme,
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Avatar,
  Divider,
} from '@mui/material';
import {
  Dashboard as DashboardIcon,
  Analytics as AnalyticsIcon,
  SmartToy as AgentsIcon,
  History as HistoryIcon,
  Menu as MenuIcon,
  Notifications as NotificationsIcon,
  Settings as SettingsIcon,
  TrendingUp,
  Speed,
  CheckCircle,
} from '@mui/icons-material';
import { motion, AnimatePresence } from 'framer-motion';

const Navbar = ({ agentStatus }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  
  const [mobileOpen, setMobileOpen] = useState(false);
  const [notificationAnchor, setNotificationAnchor] = useState(null);

  const navigationItems = [
    { path: '/', label: 'Dashboard', icon: <DashboardIcon />, color: '#667eea' },
    { path: '/analysis', label: 'Analysis', icon: <AnalyticsIcon />, color: '#764ba2' },
    { path: '/agents', label: 'Agents', icon: <AgentsIcon />, color: '#00e676' },
    { path: '/history', label: 'History', icon: <HistoryIcon />, color: '#ff6b6b' },
  ];

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const handleNotificationClick = (event) => {
    setNotificationAnchor(event.currentTarget);
  };

  const handleNotificationClose = () => {
    setNotificationAnchor(null);
  };

  const getOnlineAgentsCount = () => {
    return Object.values(agentStatus).filter(agent => agent.online).length;
  };

  const getTotalAgentsCount = () => {
    return Object.keys(agentStatus).length || 5;
  };

  const getSystemHealth = () => {
    const onlineCount = getOnlineAgentsCount();
    const totalCount = getTotalAgentsCount();
    const percentage = totalCount > 0 ? (onlineCount / totalCount) * 100 : 0;
    
    if (percentage === 100) return { status: 'Excellent', color: 'success', icon: <CheckCircle /> };
    if (percentage >= 80) return { status: 'Good', color: 'warning', icon: <Speed /> };
    return { status: 'Issues', color: 'error', icon: <TrendingUp /> };
  };

  const drawer = (
    <Box 
      sx={{ 
        width: 280, 
        height: '100%',
        background: 'rgba(10, 14, 39, 0.95)',
        backdropFilter: 'blur(20px)',
        borderRight: '1px solid rgba(255, 255, 255, 0.1)',
      }}
    >
      {/* Drawer Header */}
      <Box sx={{ p: 3, borderBottom: '1px solid rgba(255, 255, 255, 0.1)' }}>
        <motion.div
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <Typography 
            variant="h5" 
            sx={{ 
              fontWeight: 700,
              background: 'linear-gradient(45deg, #667eea 30%, #764ba2 90%)',
              backgroundClip: 'text',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              mb: 1,
            }}
          >
            Financial MAS
          </Typography>
          <Typography variant="body2" color="text.secondary">
            AI-Powered Financial Analysis
          </Typography>
        </motion.div>
      </Box>

      {/* System Status */}
      <Box sx={{ p: 2 }}>
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.2 }}
        >
          <Box
            sx={{
              p: 2,
              borderRadius: 2,
              background: 'rgba(255, 255, 255, 0.05)',
              border: '1px solid rgba(255, 255, 255, 0.1)',
              mb: 2,
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
              {getSystemHealth().icon}
              <Typography variant="body2" fontWeight={600}>
                System Health: {getSystemHealth().status}
              </Typography>
            </Box>
            <Chip
              label={`${getOnlineAgentsCount()}/${getTotalAgentsCount()} Agents Online`}
              color={getSystemHealth().color}
              size="small"
              sx={{ fontSize: '0.75rem' }}
            />
          </Box>
        </motion.div>
      </Box>

      {/* Navigation Items */}
      <List sx={{ px: 2 }}>
        {navigationItems.map((item, index) => (
          <motion.div
            key={item.path}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.1 * (index + 1) }}
          >
            <ListItem
              button
              onClick={() => {
                navigate(item.path);
                setMobileOpen(false);
              }}
              sx={{
                borderRadius: 2,
                mb: 1,
                background: location.pathname === item.path 
                  ? `linear-gradient(135deg, ${item.color}20, ${item.color}10)`
                  : 'transparent',
                border: location.pathname === item.path 
                  ? `1px solid ${item.color}40`
                  : '1px solid transparent',
                transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
                '&:hover': {
                  background: location.pathname === item.path 
                    ? `linear-gradient(135deg, ${item.color}30, ${item.color}15)`
                    : 'rgba(255, 255, 255, 0.05)',
                  transform: 'translateX(4px)',
                },
              }}
            >
              <ListItemIcon 
                sx={{ 
                  color: location.pathname === item.path ? item.color : 'text.secondary',
                  minWidth: 40,
                }}
              >
                {item.icon}
              </ListItemIcon>
              <ListItemText 
                primary={item.label}
                sx={{ 
                  color: location.pathname === item.path ? item.color : 'text.primary',
                  '& .MuiListItemText-primary': {
                    fontWeight: location.pathname === item.path ? 600 : 400,
                  }
                }}
              />
            </ListItem>
          </motion.div>
        ))}
      </List>
    </Box>
  );

  return (
    <>
      <AppBar
        position="sticky"
        elevation={0}
        sx={{
          background: 'rgba(255, 255, 255, 0.08)',
          backdropFilter: 'blur(24px)',
          borderBottom: '1px solid rgba(255, 255, 255, 0.12)',
          '&::before': {
            content: '""',
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            height: '1px',
            background: 'linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent)',
          },
        }}
      >
        <Toolbar sx={{ minHeight: { xs: 64, sm: 70 } }}>
          {isMobile && (
            <motion.div
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.9 }}
            >
              <IconButton
                color="inherit"
                aria-label="open drawer"
                edge="start"
                onClick={handleDrawerToggle}
                sx={{ 
                  mr: 2,
                  background: 'rgba(255, 255, 255, 0.05)',
                  '&:hover': {
                    background: 'rgba(255, 255, 255, 0.1)',
                  },
                }}
              >
                <MenuIcon />
              </IconButton>
            </motion.div>
          )}

          {/* Logo */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5 }}
            style={{ cursor: 'pointer' }}
            onClick={() => navigate('/')}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
              <Avatar
                sx={{
                  width: 40,
                  height: 40,
                  background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                  fontSize: '1.2rem',
                  fontWeight: 700,
                }}
              >
                FM
              </Avatar>
              <Box>
                <Typography
                  variant="h6"
                  component="div"
                  sx={{
                    fontWeight: 700,
                    background: 'linear-gradient(45deg, #667eea 30%, #764ba2 90%)',
                    backgroundClip: 'text',
                    WebkitBackgroundClip: 'text',
                    WebkitTextFillColor: 'transparent',
                    lineHeight: 1,
                  }}
                >
                  Financial MAS
                </Typography>
                {!isMobile && (
                  <Typography variant="caption" color="text.secondary" sx={{ lineHeight: 1 }}>
                    AI-Powered Analysis
                  </Typography>
                )}
              </Box>
            </Box>
          </motion.div>

          <Box sx={{ flexGrow: 1 }} />

          {/* Desktop Navigation */}
          {!isMobile && (
            <Box sx={{ display: 'flex', gap: 1, mr: 3 }}>
              {navigationItems.map((item, index) => (
                <motion.div
                  key={item.path}
                  initial={{ opacity: 0, y: -10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.1 * index }}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Button
                    color="inherit"
                    startIcon={item.icon}
                    onClick={() => navigate(item.path)}
                    sx={{
                      borderRadius: 2,
                      px: 3,
                      py: 1,
                      background: location.pathname === item.path 
                        ? `linear-gradient(135deg, ${item.color}20, ${item.color}10)`
                        : 'rgba(255, 255, 255, 0.05)',
                      border: location.pathname === item.path 
                        ? `1px solid ${item.color}40`
                        : '1px solid rgba(255, 255, 255, 0.1)',
                      color: location.pathname === item.path ? item.color : 'text.primary',
                      fontWeight: location.pathname === item.path ? 600 : 400,
                      transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
                      '&:hover': {
                        background: location.pathname === item.path 
                          ? `linear-gradient(135deg, ${item.color}30, ${item.color}15)`
                          : 'rgba(255, 255, 255, 0.1)',
                        transform: 'translateY(-1px)',
                        boxShadow: `0 4px 20px ${item.color}30`,
                      },
                    }}
                  >
                    {item.label}
                  </Button>
                </motion.div>
              ))}
            </Box>
          )}

          {/* System Status & Notifications */}
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
            {/* Agent Status Indicator */}
            <motion.div
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.3 }}
            >
              <Chip
                label={`${getOnlineAgentsCount()}/${getTotalAgentsCount()}`}
                color={getSystemHealth().color}
                size="small"
                icon={getSystemHealth().icon}
                sx={{ 
                  fontWeight: 600,
                  background: getSystemHealth().color === 'success' 
                    ? 'linear-gradient(135deg, #00e676 0%, #00c853 100%)'
                    : getSystemHealth().color === 'warning'
                    ? 'linear-gradient(135deg, #ffab00 0%, #c77800 100%)'
                    : 'linear-gradient(135deg, #ff5252 0%, #c50e29 100%)',
                  '& .MuiChip-icon': {
                    color: 'white',
                  },
                }}
              />
            </motion.div>

            {/* Notifications */}
            <motion.div
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.9 }}
            >
              <IconButton
                color="inherit"
                onClick={handleNotificationClick}
                sx={{
                  background: 'rgba(255, 255, 255, 0.05)',
                  '&:hover': {
                    background: 'rgba(255, 255, 255, 0.1)',
                  },
                }}
              >
                <Badge badgeContent={2} color="error">
                  <NotificationsIcon />
                </Badge>
              </IconButton>
            </motion.div>
          </Box>
        </Toolbar>
      </AppBar>

      {/* Mobile Drawer */}
      <Drawer
        variant="temporary"
        open={mobileOpen}
        onClose={handleDrawerToggle}
        ModalProps={{
          keepMounted: true,
        }}
        sx={{
          display: { xs: 'block', md: 'none' },
          '& .MuiDrawer-paper': {
            boxSizing: 'border-box',
            width: 280,
            background: 'rgba(10, 14, 39, 0.95)',
            backdropFilter: 'blur(20px)',
            border: 'none',
          },
        }}
      >
        {drawer}
      </Drawer>

      {/* Notifications Menu */}
      <Menu
        anchorEl={notificationAnchor}
        open={Boolean(notificationAnchor)}
        onClose={handleNotificationClose}
        PaperProps={{
          sx: {
            background: 'rgba(255, 255, 255, 0.08)',
            backdropFilter: 'blur(20px)',
            border: '1px solid rgba(255, 255, 255, 0.12)',
            borderRadius: 2,
            minWidth: 300,
          },
        }}
      >
        <MenuItem onClick={handleNotificationClose}>
          <Box>
            <Typography variant="body2" fontWeight={600}>
              System Status Update
            </Typography>
            <Typography variant="caption" color="text.secondary">
              All agents are running smoothly
            </Typography>
          </Box>
        </MenuItem>
        <MenuItem onClick={handleNotificationClose}>
          <Box>
            <Typography variant="body2" fontWeight={600}>
              Analysis Complete
            </Typography>
            <Typography variant="caption" color="text.secondary">
              AAPL stock analysis finished
            </Typography>
          </Box>
        </MenuItem>
      </Menu>
    </>
  );
};

export default Navbar; 