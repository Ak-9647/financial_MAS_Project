# 🤝 Contributing to Financial MAS

Thank you for your interest in contributing to the Financial Multi-Agent System! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Contributing Guidelines](#contributing-guidelines)
- [Code Style](#code-style)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Development Workflow](#development-workflow)

## 🤝 Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow:

- **Be respectful** and inclusive in all interactions
- **Be collaborative** and help others learn and grow
- **Be constructive** when providing feedback
- **Be patient** with newcomers and different skill levels
- **Focus on the code**, not the person

## 🚀 Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Python 3.8+** with pip
- **Node.js 16+** with npm
- **Git** for version control
- **Code editor** (VS Code, PyCharm, etc.)
- **Basic knowledge** of Python, React, and REST APIs

### First-Time Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/financial_mas_project.git
   cd financial_mas_project
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/originalowner/financial_mas_project.git
   ```
4. **Set up development environment** (see Development Setup below)

## 🛠️ Development Setup

### Backend Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# Set up environment variables
cp env.example .env
# Edit .env with your API keys (optional for development)

# Start the backend system
python start_system.py
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

### Development Tools

Install recommended development tools:

```bash
# Python formatting and linting
pip install black flake8 mypy pytest

# Pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install
```

## 📁 Project Structure

Understanding the project structure will help you contribute effectively:

```
financial_mas_project/
├── agents/                          # AI agent implementations
│   ├── base_agent.py               # Base agent class
│   ├── data_gathering_agent.py     # Data collection agent
│   ├── quantitative_analysis_agent.py
│   ├── qualitative_analysis_agent.py
│   ├── report_generation_agent.py
│   └── orchestrator_agent.py       # Main coordinator
├── frontend/                        # React frontend
│   ├── src/
│   │   ├── components/             # React components
│   │   ├── services/               # API integration
│   │   ├── utils/                  # Frontend utilities
│   │   └── __tests__/              # Frontend tests
│   ├── public/                     # Static assets
│   └── package.json                # Frontend dependencies
├── services/                        # Business logic
│   ├── financial_service.py        # Financial data handling
│   ├── web_research_service.py     # Web research logic
│   └── knowledge_service.py        # Knowledge management
├── mcp_servers/                     # MCP tool servers
├── utils/                           # Shared utilities
│   ├── a2a_server.py               # Agent-to-agent communication
│   ├── a2a_client.py               # A2A client
│   └── config.py                   # Configuration management
├── tests/                           # Test suite
│   ├── test_agents/                # Agent tests
│   ├── test_services/              # Service tests
│   └── test_integration/           # Integration tests
├── docs/                            # Documentation
├── scripts/                         # Utility scripts
└── requirements.txt                 # Python dependencies
```

## 📝 Contributing Guidelines

### Types of Contributions

We welcome various types of contributions:

1. **🐛 Bug Fixes** - Fix issues in existing code
2. **✨ New Features** - Add new functionality
3. **📚 Documentation** - Improve or add documentation
4. **🎨 UI/UX Improvements** - Enhance the frontend experience
5. **⚡ Performance Optimizations** - Improve system performance
6. **🧪 Tests** - Add or improve test coverage
7. **🔧 Refactoring** - Improve code structure and maintainability

### Contribution Areas

#### Backend (Python)
- **Agent Development**: Create new AI agents or improve existing ones
- **Service Layer**: Enhance business logic and data processing
- **API Endpoints**: Add new endpoints or improve existing ones
- **MCP Servers**: Develop new tool servers for external integrations
- **Performance**: Optimize agent communication and processing

#### Frontend (React)
- **Components**: Create reusable UI components
- **Pages**: Add new pages or improve existing ones
- **Animations**: Enhance user experience with smooth animations
- **Responsive Design**: Improve mobile and tablet experience
- **Accessibility**: Ensure the app is accessible to all users

#### Infrastructure
- **Testing**: Add unit, integration, and end-to-end tests
- **CI/CD**: Improve build and deployment processes
- **Documentation**: Write guides, tutorials, and API documentation
- **Performance**: Optimize build times and runtime performance

## 🎨 Code Style

### Python Code Style

We follow **PEP 8** with some modifications:

```python
# Use black formatter with line length 88
# Example of good Python code style

class DataGatheringAgent:
    """Agent responsible for gathering financial data."""
    
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config
        self.client = httpx.AsyncClient()
    
    async def gather_data(self, query: str) -> Dict[str, Any]:
        """Gather financial data based on the query."""
        try:
            # Implementation here
            return {"status": "success", "data": data}
        except Exception as e:
            logger.error(f"Data gathering failed: {e}")
            raise
```

**Python Guidelines:**
- Use **type hints** for all function parameters and return values
- Write **docstrings** for all classes and functions
- Use **async/await** for I/O operations
- Handle **exceptions** gracefully with proper logging
- Follow **SOLID principles** for class design

### JavaScript/React Code Style

We use **ESLint** and **Prettier** for consistent formatting:

```javascript
// Example of good React code style

import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Card, CardContent, Typography } from '@mui/material';

const MetricCard = ({ title, value, icon, color }) => {
  const [isHovered, setIsHovered] = useState(false);

  useEffect(() => {
    // Effect logic here
  }, []);

  return (
    <motion.div
      whileHover={{ scale: 1.05 }}
      onHoverStart={() => setIsHovered(true)}
      onHoverEnd={() => setIsHovered(false)}
    >
      <Card
        sx={{
          background: 'rgba(255, 255, 255, 0.08)',
          backdropFilter: 'blur(20px)',
          transition: 'all 0.3s ease',
        }}
      >
        <CardContent>
          <Typography variant="h6">{title}</Typography>
          <Typography variant="h4" color={color}>
            {value}
          </Typography>
        </CardContent>
      </Card>
    </motion.div>
  );
};

export default MetricCard;
```

**React Guidelines:**
- Use **functional components** with hooks
- Implement **proper prop types** or TypeScript
- Follow **component composition** patterns
- Use **meaningful variable names**
- Implement **proper error boundaries**

### Commit Message Format

Use **Conventional Commits** format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(frontend): add real-time agent status monitoring

fix(agents): resolve data gathering timeout issue

docs(readme): update installation instructions

style(frontend): improve glassmorphism effects

test(agents): add unit tests for orchestrator
```

## 🧪 Testing

### Running Tests

```bash
# Backend tests
python -m pytest tests/ -v

# Frontend tests
cd frontend
npm test

# Integration tests
python -m pytest tests/test_integration/ -v

# Test coverage
python -m pytest --cov=agents --cov=services tests/
```

### Writing Tests

#### Python Tests (pytest)

```python
import pytest
from agents.data_gathering_agent import DataGatheringAgent

class TestDataGatheringAgent:
    @pytest.fixture
    def agent(self):
        config = {"api_key": "test_key"}
        return DataGatheringAgent(config)
    
    @pytest.mark.asyncio
    async def test_gather_data_success(self, agent):
        result = await agent.gather_data("AAPL")
        assert result["status"] == "success"
        assert "data" in result
    
    @pytest.mark.asyncio
    async def test_gather_data_invalid_symbol(self, agent):
        with pytest.raises(ValueError):
            await agent.gather_data("")
```

#### React Tests (Jest + React Testing Library)

```javascript
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { ThemeProvider } from '@mui/material/styles';
import MetricCard from '../MetricCard';
import theme from '../../theme';

const renderWithTheme = (component) => {
  return render(
    <ThemeProvider theme={theme}>
      {component}
    </ThemeProvider>
  );
};

describe('MetricCard', () => {
  test('renders metric card with correct data', () => {
    renderWithTheme(
      <MetricCard 
        title="Test Metric" 
        value="100" 
        color="primary.main" 
      />
    );
    
    expect(screen.getByText('Test Metric')).toBeInTheDocument();
    expect(screen.getByText('100')).toBeInTheDocument();
  });

  test('handles hover interactions', () => {
    renderWithTheme(
      <MetricCard 
        title="Test Metric" 
        value="100" 
        color="primary.main" 
      />
    );
    
    const card = screen.getByText('Test Metric').closest('div');
    fireEvent.mouseEnter(card);
    // Assert hover state changes
  });
});
```

## 🔄 Pull Request Process

### Before Submitting

1. **Sync with upstream**:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** following the guidelines above

4. **Test thoroughly**:
   ```bash
   # Run all tests
   python -m pytest
   cd frontend && npm test
   ```

5. **Format code**:
   ```bash
   # Python
   black .
   flake8 .
   
   # JavaScript
   cd frontend
   npm run lint
   npm run format
   ```

### Submitting Pull Request

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request** on GitHub with:
   - **Clear title** describing the change
   - **Detailed description** of what was changed and why
   - **Screenshots** for UI changes
   - **Testing instructions** for reviewers
   - **Link to related issues**

3. **PR Template**:
   ```markdown
   ## Description
   Brief description of changes made.

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Performance improvement

   ## Testing
   - [ ] Unit tests pass
   - [ ] Integration tests pass
   - [ ] Manual testing completed

   ## Screenshots (if applicable)
   Add screenshots for UI changes.

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Tests added/updated
   - [ ] Documentation updated
   ```

### Review Process

1. **Automated checks** must pass (CI/CD, tests, linting)
2. **Code review** by maintainers
3. **Address feedback** if requested
4. **Final approval** and merge

## 🐛 Issue Reporting

### Bug Reports

Use the bug report template:

```markdown
**Bug Description**
Clear description of the bug.

**Steps to Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What should happen.

**Actual Behavior**
What actually happens.

**Environment**
- OS: [e.g., macOS 12.0]
- Python: [e.g., 3.9.0]
- Node.js: [e.g., 16.14.0]
- Browser: [e.g., Chrome 98.0]

**Screenshots**
Add screenshots if applicable.

**Additional Context**
Any other relevant information.
```

### Feature Requests

Use the feature request template:

```markdown
**Feature Description**
Clear description of the proposed feature.

**Problem Statement**
What problem does this solve?

**Proposed Solution**
How should this be implemented?

**Alternatives Considered**
Other solutions you've considered.

**Additional Context**
Mockups, examples, or references.
```

## 🔄 Development Workflow

### Daily Development

1. **Start with latest code**:
   ```bash
   git checkout main
   git pull upstream main
   ```

2. **Create feature branch**:
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Develop and test**:
   ```bash
   # Make changes
   # Run tests frequently
   python -m pytest
   cd frontend && npm test
   ```

4. **Commit regularly**:
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

5. **Push and create PR** when ready

### Working with Issues

1. **Comment on issues** you want to work on
2. **Get assignment** from maintainers
3. **Reference issues** in commits: `fixes #123`
4. **Update issue** with progress

### Communication

- **GitHub Discussions** for general questions
- **GitHub Issues** for bugs and features
- **Pull Request comments** for code-specific discussions
- **Be respectful** and constructive in all communications

## 🎯 Getting Help

### Resources

- **Documentation**: Check the `/docs` folder
- **Examples**: Look at existing code for patterns
- **Tests**: Existing tests show expected behavior
- **Issues**: Search existing issues for similar problems

### Asking Questions

When asking for help:

1. **Search existing issues** and discussions first
2. **Provide context** about what you're trying to do
3. **Include error messages** and relevant code
4. **Specify your environment** (OS, Python/Node versions)
5. **Be specific** about what you've already tried

## 🏆 Recognition

Contributors will be recognized in:

- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub contributors** page
- **Special mentions** for outstanding contributions

## 📞 Contact

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For general questions
- **Email**: [maintainer@example.com] for sensitive issues

---

Thank you for contributing to Financial MAS! Your efforts help make this project better for everyone. 🚀

*Happy coding!* 💻✨ 