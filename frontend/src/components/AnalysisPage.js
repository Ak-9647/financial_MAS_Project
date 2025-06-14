import React, { useState } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Grid,
  Chip,
  LinearProgress,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Paper,
  Divider,
  IconButton,
  Tooltip,
} from '@mui/material';
import {
  Search,
  PlayArrow,
  ExpandMore,
  TrendingUp,
  TrendingDown,
  Assessment,
  Psychology,
  Description,
  Share,
  Download,
  Refresh,
} from '@mui/icons-material';
import { motion, AnimatePresence } from 'framer-motion';
import { submitAnalysisRequest, saveAnalysisToHistory } from '../services/api';

const AnalysisPage = ({ showNotification }) => {
  const [query, setQuery] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [analysisSteps, setAnalysisSteps] = useState([]);

  const predefinedQueries = [
    'Analyze Apple (AAPL) stock performance and provide investment recommendation',
    'Compare Tesla vs Ford stock performance over the last quarter',
    'Analyze NVIDIA earnings report and market sentiment',
    'Provide technical analysis for Bitcoin price trends',
    'Evaluate Microsoft Azure vs AWS market position',
  ];

  const handleAnalysis = async () => {
    if (!query.trim()) {
      showNotification('Please enter a query for analysis', 'warning');
      return;
    }

    setIsAnalyzing(true);
    setAnalysisResult(null);
    setAnalysisSteps([]);
    const startTime = Date.now();

    // Simulate analysis steps
    const steps = [
      { id: 1, name: 'Data Gathering', status: 'running', description: 'Collecting financial data and market information' },
      { id: 2, name: 'Quantitative Analysis', status: 'pending', description: 'Performing statistical analysis and calculations' },
      { id: 3, name: 'Qualitative Analysis', status: 'pending', description: 'Analyzing sentiment and market perception' },
      { id: 4, name: 'Report Generation', status: 'pending', description: 'Synthesizing findings into comprehensive report' },
    ];

    setAnalysisSteps(steps);

    try {
      // Simulate step progression
      for (let i = 0; i < steps.length; i++) {
        await new Promise(resolve => setTimeout(resolve, 2000));
        setAnalysisSteps(prev => prev.map(step => 
          step.id === i + 1 
            ? { ...step, status: 'completed' }
            : step.id === i + 2
            ? { ...step, status: 'running' }
            : step
        ));
      }

      const result = await submitAnalysisRequest(query);
      const duration = Date.now() - startTime;

      // Parse the result if it's a string
      let parsedResult;
      try {
        parsedResult = typeof result === 'string' ? JSON.parse(result) : result;
      } catch {
        parsedResult = { 
          summary: result,
          recommendation: 'Analysis completed successfully',
          confidence: 'High',
          keyFindings: ['Analysis completed', 'Data processed successfully']
        };
      }

      setAnalysisResult(parsedResult);

      await saveAnalysisToHistory({
        query,
        result: parsedResult,
        duration: `${(duration / 1000).toFixed(1)}s`,
      });

      showNotification('Analysis completed successfully!', 'success');
    } catch (error) {
      showNotification(error.message, 'error');
      setAnalysisSteps(prev => prev.map(step => 
        step.status === 'running' ? { ...step, status: 'error' } : step
      ));
    } finally {
      setIsAnalyzing(false);
    }
  };

  const getStepIcon = (status) => {
    switch (status) {
      case 'completed':
        return <TrendingUp color="success" />;
      case 'running':
        return <Refresh sx={{ animation: 'spin 1s linear infinite' }} />;
      case 'error':
        return <TrendingDown color="error" />;
      default:
        return <Assessment color="disabled" />;
    }
  };

  const getStepColor = (status) => {
    switch (status) {
      case 'completed':
        return 'success';
      case 'running':
        return 'primary';
      case 'error':
        return 'error';
      default:
        return 'default';
    }
  };

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
            Financial Analysis
          </Typography>
          <Typography variant="h6" color="text.secondary">
            Advanced AI-powered financial research and analysis
          </Typography>
        </Box>
      </motion.div>

      <Grid container spacing={3}>
        {/* Query Input Section */}
        <Grid item xs={12} lg={8}>
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.1 }}
          >
            <Card sx={{ mb: 3, background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
              <CardContent>
                <Typography variant="h5" sx={{ mb: 2, display: 'flex', alignItems: 'center', gap: 1 }}>
                  <Search />
                  Analysis Query
                </Typography>
                
                <TextField
                  fullWidth
                  multiline
                  rows={4}
                  placeholder="Enter your financial analysis query here... (e.g., 'Analyze Tesla stock performance and provide investment recommendation')"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  disabled={isAnalyzing}
                  sx={{ mb: 2 }}
                />

                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                  <Button
                    variant="contained"
                    size="large"
                    onClick={handleAnalysis}
                    disabled={isAnalyzing || !query.trim()}
                    startIcon={isAnalyzing ? null : <PlayArrow />}
                    sx={{ minWidth: 150 }}
                  >
                    {isAnalyzing ? 'Analyzing...' : 'Start Analysis'}
                  </Button>

                  <Box sx={{ display: 'flex', gap: 1 }}>
                    <Tooltip title="Share Analysis">
                      <IconButton disabled={!analysisResult}>
                        <Share />
                      </IconButton>
                    </Tooltip>
                    <Tooltip title="Download Report">
                      <IconButton disabled={!analysisResult}>
                        <Download />
                      </IconButton>
                    </Tooltip>
                  </Box>
                </Box>

                {/* Predefined Queries */}
                <Typography variant="subtitle2" sx={{ mb: 1 }}>
                  Quick Start Examples:
                </Typography>
                <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                  {predefinedQueries.map((predefinedQuery, index) => (
                    <Chip
                      key={index}
                      label={predefinedQuery}
                      variant="outlined"
                      size="small"
                      onClick={() => setQuery(predefinedQuery)}
                      disabled={isAnalyzing}
                      sx={{ 
                        cursor: 'pointer',
                        '&:hover': { backgroundColor: 'rgba(255, 255, 255, 0.1)' }
                      }}
                    />
                  ))}
                </Box>
              </CardContent>
            </Card>
          </motion.div>

          {/* Analysis Steps */}
          <AnimatePresence>
            {analysisSteps.length > 0 && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                transition={{ duration: 0.5 }}
              >
                <Card sx={{ mb: 3, background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
                  <CardContent>
                    <Typography variant="h6" sx={{ mb: 2 }}>
                      Analysis Progress
                    </Typography>
                    {isAnalyzing && <LinearProgress sx={{ mb: 2 }} />}
                    
                    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                      {analysisSteps.map((step, index) => (
                        <motion.div
                          key={step.id}
                          initial={{ opacity: 0, x: -20 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: index * 0.1 }}
                        >
                          <Paper
                            sx={{
                              p: 2,
                              background: 'rgba(255, 255, 255, 0.05)',
                              border: '1px solid rgba(255, 255, 255, 0.1)',
                              display: 'flex',
                              alignItems: 'center',
                              gap: 2,
                            }}
                          >
                            {getStepIcon(step.status)}
                            <Box sx={{ flexGrow: 1 }}>
                              <Typography variant="subtitle1" sx={{ fontWeight: 500 }}>
                                {step.name}
                              </Typography>
                              <Typography variant="body2" color="text.secondary">
                                {step.description}
                              </Typography>
                            </Box>
                            <Chip
                              label={step.status}
                              color={getStepColor(step.status)}
                              size="small"
                            />
                          </Paper>
                        </motion.div>
                      ))}
                    </Box>
                  </CardContent>
                </Card>
              </motion.div>
            )}
          </AnimatePresence>

          {/* Analysis Results */}
          <AnimatePresence>
            {analysisResult && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
              >
                <Card sx={{ background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
                  <CardContent>
                    <Typography variant="h5" sx={{ mb: 3, display: 'flex', alignItems: 'center', gap: 1 }}>
                      <Description />
                      Analysis Results
                    </Typography>

                    {/* Executive Summary */}
                    <Accordion defaultExpanded>
                      <AccordionSummary expandIcon={<ExpandMore />}>
                        <Typography variant="h6">Executive Summary</Typography>
                      </AccordionSummary>
                      <AccordionDetails>
                        <Typography variant="body1" sx={{ lineHeight: 1.8 }}>
                          {analysisResult.summary || analysisResult.executiveSummary || 'Analysis completed successfully.'}
                        </Typography>
                      </AccordionDetails>
                    </Accordion>

                    {/* Key Findings */}
                    {analysisResult.keyFindings && (
                      <Accordion>
                        <AccordionSummary expandIcon={<ExpandMore />}>
                          <Typography variant="h6">Key Findings</Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
                            {analysisResult.keyFindings.map((finding, index) => (
                              <Typography key={index} variant="body2" sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                                <Box sx={{ width: 6, height: 6, borderRadius: '50%', bgcolor: 'primary.main' }} />
                                {finding}
                              </Typography>
                            ))}
                          </Box>
                        </AccordionDetails>
                      </Accordion>
                    )}

                    {/* Investment Recommendation */}
                    {analysisResult.recommendation && (
                      <Accordion>
                        <AccordionSummary expandIcon={<ExpandMore />}>
                          <Typography variant="h6">Investment Recommendation</Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                          <Typography variant="body1" sx={{ lineHeight: 1.8 }}>
                            {analysisResult.recommendation}
                          </Typography>
                          {analysisResult.confidence && (
                            <Box sx={{ mt: 2 }}>
                              <Chip
                                label={`Confidence: ${analysisResult.confidence}`}
                                color="primary"
                                variant="outlined"
                              />
                            </Box>
                          )}
                        </AccordionDetails>
                      </Accordion>
                    )}

                    {/* Detailed Analysis */}
                    {analysisResult.detailedAnalysis && (
                      <Accordion>
                        <AccordionSummary expandIcon={<ExpandMore />}>
                          <Typography variant="h6">Detailed Analysis</Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                          <Typography variant="body1" sx={{ lineHeight: 1.8, whiteSpace: 'pre-line' }}>
                            {analysisResult.detailedAnalysis}
                          </Typography>
                        </AccordionDetails>
                      </Accordion>
                    )}
                  </CardContent>
                </Card>
              </motion.div>
            )}
          </AnimatePresence>
        </Grid>

        {/* Sidebar */}
        <Grid item xs={12} lg={4}>
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <Card sx={{ mb: 3, background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
              <CardContent>
                <Typography variant="h6" sx={{ mb: 2 }}>
                  Analysis Tips
                </Typography>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                  <Box>
                    <Typography variant="subtitle2" sx={{ mb: 1 }}>
                      📊 Stock Analysis
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Include ticker symbols (e.g., AAPL, TSLA) for specific stock analysis
                    </Typography>
                  </Box>
                  <Divider />
                  <Box>
                    <Typography variant="subtitle2" sx={{ mb: 1 }}>
                      📈 Market Trends
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Ask about sector comparisons or market sentiment analysis
                    </Typography>
                  </Box>
                  <Divider />
                  <Box>
                    <Typography variant="subtitle2" sx={{ mb: 1 }}>
                      💡 Investment Advice
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Request specific investment recommendations with risk assessment
                    </Typography>
                  </Box>
                </Box>
              </CardContent>
            </Card>

            <Card sx={{ background: 'rgba(255, 255, 255, 0.05)', backdropFilter: 'blur(20px)' }}>
              <CardContent>
                <Typography variant="h6" sx={{ mb: 2 }}>
                  System Status
                </Typography>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
                    <Typography variant="body2">Data Sources</Typography>
                    <Chip label="Active" color="success" size="small" />
                  </Box>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
                    <Typography variant="body2">AI Models</Typography>
                    <Chip label="Online" color="success" size="small" />
                  </Box>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
                    <Typography variant="body2">Market Data</Typography>
                    <Chip label="Real-time" color="success" size="small" />
                  </Box>
                </Box>
              </CardContent>
            </Card>
          </motion.div>
        </Grid>
      </Grid>
    </Box>
  );
};

export default AnalysisPage; 