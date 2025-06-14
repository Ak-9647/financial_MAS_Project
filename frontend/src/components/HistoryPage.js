import React, { useState, useEffect } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Grid,
  Chip,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TablePagination,
  InputAdornment,
  Menu,
  MenuItem,
  Accordion,
  AccordionSummary,
  AccordionDetails,
} from '@mui/material';
import {
  History,
  Search,
  FilterList,
  Delete,
  Visibility,
  Download,
  Share,
  ExpandMore,
  DateRange,
  TrendingUp,
  Assessment,
} from '@mui/icons-material';
import { motion, AnimatePresence } from 'framer-motion';
import { getAnalysisHistory, deleteAnalysisFromHistory } from '../services/api';

const HistoryPage = () => {
  const [history, setHistory] = useState([]);
  const [filteredHistory, setFilteredHistory] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedAnalysis, setSelectedAnalysis] = useState(null);
  const [dialogOpen, setDialogOpen] = useState(false);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [filterAnchor, setFilterAnchor] = useState(null);
  const [dateFilter, setDateFilter] = useState('all');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadHistory();
  }, []);

  useEffect(() => {
    filterHistory();
  }, [history, searchTerm, dateFilter]);

  const loadHistory = async () => {
    try {
      const data = await getAnalysisHistory();
      setHistory(data);
    } catch (error) {
      console.error('Failed to load history:', error);
    } finally {
      setLoading(false);
    }
  };

  const filterHistory = () => {
    let filtered = [...history];

    // Search filter
    if (searchTerm) {
      filtered = filtered.filter(item =>
        item.query.toLowerCase().includes(searchTerm.toLowerCase()) ||
        (typeof item.result === 'string' && item.result.toLowerCase().includes(searchTerm.toLowerCase()))
      );
    }

    // Date filter
    const now = new Date();
    if (dateFilter !== 'all') {
      filtered = filtered.filter(item => {
        const itemDate = new Date(item.timestamp);
        const diffTime = now - itemDate;
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

        switch (dateFilter) {
          case 'today':
            return diffDays <= 1;
          case 'week':
            return diffDays <= 7;
          case 'month':
            return diffDays <= 30;
          default:
            return true;
        }
      });
    }

    setFilteredHistory(filtered);
    setPage(0);
  };

  const handleViewAnalysis = (analysis) => {
    setSelectedAnalysis(analysis);
    setDialogOpen(true);
  };

  const handleDeleteAnalysis = async (id) => {
    try {
      await deleteAnalysisFromHistory(id);
      await loadHistory();
    } catch (error) {
      console.error('Failed to delete analysis:', error);
    }
  };

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  const formatDate = (timestamp) => {
    return new Date(timestamp).toLocaleString();
  };

  const getResultSummary = (result) => {
    if (typeof result === 'string') {
      return result.substring(0, 100) + (result.length > 100 ? '...' : '');
    }
    if (result && result.summary) {
      return result.summary.substring(0, 100) + (result.summary.length > 100 ? '...' : '');
    }
    return 'Analysis completed';
  };

  const paginatedHistory = filteredHistory.slice(
    page * rowsPerPage,
    page * rowsPerPage + rowsPerPage
  );

  return (
    <Box>
      <Typography variant="h3">Analysis History</Typography>
      <Typography variant="body1">View your past analyses here.</Typography>
    </Box>
  );
};

export default HistoryPage; 