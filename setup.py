#!/usr/bin/env python3
"""
Advanced Sentiment Analysis System - Setup Script
==================================================

This script helps you set up the Advanced Sentiment Analysis System
with proper environment configuration and security measures.

Usage:
    python setup.py
"""

import os
import sys
import subprocess
import getpass
from pathlib import Path

def print_banner():
    """Print setup banner"""
    print("=" * 70)
    print("🚀 Advanced Sentiment Analysis System - Setup")
    print("=" * 70)
    print("Setting up your production-ready sentiment analysis platform...")
    print()

def check_python_version():
    """Check Python version compatibility"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    
    requirements = [
        "dspy-ai>=2.4.0",
        "openai>=1.0.0",
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.1.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "plotly>=5.0.0",
        "openpyxl>=3.0.0",
        "jupyter>=1.0.0",
        "ipykernel>=6.0.0",
        "ipywidgets>=7.0.0",
        "python-dotenv>=0.19.0",
        "requests>=2.28.0"
    ]
    
    for package in requirements:
        try:
            print(f"   Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])
        except subprocess.CalledProcessError:
            print(f"   ⚠️  Warning: Failed to install {package}")
    
    print("✅ Dependencies installation completed")

def setup_environment():
    """Setup environment configuration"""
    print("\n🔧 Setting up environment configuration...")
    
    env_file = Path(".env")
    
    if env_file.exists():
        print("   .env file already exists")
        overwrite = input("   Do you want to overwrite it? (y/N): ").lower()
        if overwrite != 'y':
            print("   Keeping existing .env file")
            return
    
    # Get OpenAI API key
    print("\n🔑 OpenAI API Key Configuration")
    print("   You need an OpenAI API key to use this system.")
    print("   Get one at: https://platform.openai.com/api-keys")
    
    api_key = getpass.getpass("   Enter your OpenAI API key (input hidden): ").strip()
    
    if not api_key:
        print("   ⚠️  No API key provided. You can set it later.")
        api_key = "your_openai_api_key_here"
    elif not api_key.startswith("sk-"):
        print("   ⚠️  Warning: API key should start with 'sk-'")
    
    # Create .env file
    env_content = f"""# Advanced Sentiment Analysis System - Environment Configuration
# Created by setup.py

# OpenAI API Configuration (REQUIRED)
OPENAI_API_KEY={api_key}

# Sentiment Analysis Thresholds (Optional - defaults provided)
SENTIMENT_CONFIDENCE_THRESHOLD=0.7
ESCALATION_RATE_THRESHOLD=0.15
PROCESSING_TIME_THRESHOLD=5.0
ERROR_RATE_THRESHOLD=0.05

# Production Configuration (Optional)
ENVIRONMENT=development
MAX_CONCURRENT_REQUESTS=100
RATE_LIMIT_REQUESTS_PER_MINUTE=1000
RATE_LIMIT_BURST_CAPACITY=50

# Monitoring Configuration (Optional)
METRICS_COLLECTION_ENABLED=true

# Logging Configuration (Optional)
LOG_LEVEL=INFO
LOG_FORMAT=json

# Cache Configuration (Optional)
CACHE_ENABLED=true
CACHE_TTL_SECONDS=300

# Performance Configuration (Optional)
BATCH_SIZE_DEFAULT=100
MAX_WORKERS_DEFAULT=10
PROCESSING_TIMEOUT_SECONDS=30
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("✅ Environment configuration created (.env)")

def setup_jupyter():
    """Setup Jupyter environment"""
    print("\n📚 Setting up Jupyter environment...")
    
    try:
        # Install Jupyter extensions
        subprocess.check_call([sys.executable, "-m", "pip", "install", "jupyter_contrib_nbextensions", "-q"])
        print("✅ Jupyter extensions installed")
        
        # Enable widgets
        subprocess.check_call([sys.executable, "-m", "jupyter", "nbextension", "enable", "--py", "widgetsnbextension", "--sys-prefix"])
        print("✅ Jupyter widgets enabled")
        
    except subprocess.CalledProcessError:
        print("   ⚠️  Warning: Some Jupyter setup steps failed")

def verify_installation():
    """Verify the installation"""
    print("\n🔍 Verifying installation...")
    
    try:
        # Test imports
        import pandas
        import numpy
        import matplotlib
        import seaborn
        import plotly
        import sklearn
        import dspy
        import openai
        
        print("✅ All core packages imported successfully")
        
        # Check environment
        if os.path.exists(".env"):
            print("✅ Environment configuration found")
        else:
            print("⚠️  Environment configuration not found")
        
        # Check notebook
        if os.path.exists("advanced_sentiment_analysis.ipynb"):
            print("✅ Main notebook found")
        else:
            print("⚠️  Main notebook not found")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    return True

def print_next_steps():
    """Print next steps for the user"""
    print("\n" + "=" * 70)
    print("🎉 Setup completed successfully!")
    print("=" * 70)
    print("\n📋 Next Steps:")
    print("   1. Start Jupyter Notebook:")
    print("      jupyter notebook advanced_sentiment_analysis.ipynb")
    print("\n   2. Run all cells in the notebook to initialize the system")
    print("\n   3. The system will automatically use your configured API key")
    print("\n   4. Check the README.md for detailed usage examples")
    print("\n🔗 Useful Links:")
    print("   • Documentation: README.md")
    print("   • Contributing: CONTRIBUTING.md")
    print("   • License: LICENSE")
    print("\n💡 Tips:")
    print("   • Keep your .env file secure and never commit it to git")
    print("   • Monitor your OpenAI API usage at platform.openai.com")
    print("   • Check CHANGELOG.md for updates and new features")
    print("\n" + "=" * 70)

def main():
    """Main setup function"""
    try:
        print_banner()
        check_python_version()
        install_dependencies()
        setup_environment()
        setup_jupyter()
        
        if verify_installation():
            print_next_steps()
        else:
            print("\n❌ Setup completed with errors. Please check the output above.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()