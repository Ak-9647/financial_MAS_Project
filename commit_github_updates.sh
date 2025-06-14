#!/bin/bash

# GitHub Repository Update Script
# This script commits all the new documentation and GitHub configuration files

echo "🚀 Financial MAS - GitHub Repository Update Script"
echo "=================================================="

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository. Please run this script from the project root."
    exit 1
fi

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "📋 Found uncommitted changes. Proceeding with commit..."
else
    echo "✅ No changes to commit."
    exit 0
fi

# Add all new and modified files
echo "📁 Adding files to git..."

# Documentation files
git add README.md
git add CONTRIBUTING.md
git add LICENSE
git add DEPLOYMENT.md
git add requirements-dev.txt

# Frontend showcase (if exists)
if [ -f "FRONTEND_SHOWCASE.md" ]; then
    git add FRONTEND_SHOWCASE.md
fi

# Setup guide (if exists)
if [ -f "SETUP_GUIDE.md" ]; then
    git add SETUP_GUIDE.md
fi

# GitHub configuration
git add .github/

# Frontend files (if they exist and have changes)
if [ -d "frontend" ]; then
    git add frontend/package.json
    git add frontend/public/index.html
    git add frontend/src/
    git add frontend/README.md
fi

# Startup script
if [ -f "start_frontend.sh" ]; then
    git add start_frontend.sh
fi

# Check what's being committed
echo ""
echo "📋 Files to be committed:"
git status --short

echo ""
read -p "🤔 Do you want to proceed with the commit? (y/N): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Commit cancelled."
    exit 1
fi

# Create comprehensive commit message
COMMIT_MESSAGE="feat: add comprehensive GitHub documentation and ultra-modern frontend

🎨 Ultra-Modern Frontend Enhancements:
- Advanced glassmorphism effects with 24px backdrop blur
- Sophisticated animations powered by Framer Motion
- Mobile-first responsive design for all devices
- Real-time agent monitoring with live status updates
- Interactive data visualization with custom charts

📚 Documentation Updates:
- Comprehensive README with installation and usage guides
- Detailed CONTRIBUTING guidelines for developers
- Complete DEPLOYMENT guide for all environments
- MIT License for open source compliance
- Development requirements for testing and linting

🔧 GitHub Configuration:
- CI/CD pipeline with automated testing and deployment
- Issue templates for bugs and feature requests
- Pull request template with comprehensive checklist
- Security scanning and dependency checks

🚀 Frontend Architecture:
- React 18 with Material-UI v5 and modern hooks
- Advanced theming with custom color palette
- Component-based architecture with reusable elements
- API integration with comprehensive error handling
- Performance optimizations and code splitting

🛠️ Development Tools:
- ESLint and Prettier for code formatting
- Jest and React Testing Library for testing
- GitHub Actions for automated CI/CD
- Docker configuration for containerized deployment

This update transforms the project into a production-ready,
enterprise-grade financial analysis platform with modern
development practices and comprehensive documentation."

# Commit the changes
echo "💾 Committing changes..."
git commit -m "$COMMIT_MESSAGE"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully committed all changes!"
    echo ""
    echo "📋 Summary of changes:"
    echo "  • Updated README.md with comprehensive documentation"
    echo "  • Added CONTRIBUTING.md with development guidelines"
    echo "  • Created DEPLOYMENT.md with deployment instructions"
    echo "  • Added LICENSE file (MIT License)"
    echo "  • Created requirements-dev.txt for development dependencies"
    echo "  • Added GitHub Actions CI/CD pipeline"
    echo "  • Created issue and PR templates"
    echo "  • Enhanced frontend with ultra-modern design"
    echo ""
    echo "🚀 Next steps:"
    echo "  1. Push to GitHub: git push origin main"
    echo "  2. Create a new release tag if desired"
    echo "  3. Update GitHub repository settings"
    echo "  4. Configure GitHub Actions secrets if needed"
    echo ""
    echo "🔗 GitHub Repository Features Now Available:"
    echo "  • Automated testing and deployment"
    echo "  • Issue tracking with templates"
    echo "  • Pull request reviews with checklists"
    echo "  • Security scanning and dependency checks"
    echo "  • Comprehensive documentation"
    echo ""
else
    echo "❌ Error: Failed to commit changes."
    exit 1
fi

# Ask if user wants to push to GitHub
echo ""
read -p "🌐 Do you want to push these changes to GitHub now? (y/N): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 Pushing to GitHub..."
    
    # Check if we have a remote origin
    if git remote get-url origin > /dev/null 2>&1; then
        git push origin main
        
        if [ $? -eq 0 ]; then
            echo "✅ Successfully pushed to GitHub!"
            echo ""
            echo "🎉 Your Financial MAS project is now updated on GitHub with:"
            echo "  • Ultra-modern React frontend"
            echo "  • Comprehensive documentation"
            echo "  • Professional development workflow"
            echo "  • Automated CI/CD pipeline"
            echo ""
            echo "🔗 Visit your GitHub repository to see the changes!"
        else
            echo "❌ Error: Failed to push to GitHub."
            echo "💡 You can push manually later with: git push origin main"
        fi
    else
        echo "❌ Error: No remote origin configured."
        echo "💡 Configure your GitHub remote with:"
        echo "    git remote add origin https://github.com/yourusername/financial_mas_project.git"
    fi
else
    echo "📝 Changes committed locally. Push to GitHub when ready with:"
    echo "    git push origin main"
fi

echo ""
echo "🎊 GitHub repository update complete!"
echo "Thank you for using Financial MAS! 🚀" 