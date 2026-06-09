#!/usr/bin/env python3
"""
Hackathon Harvester - Quick Start Script
This script provides an easy way to run the application with proper checks.
"""

import os
import sys
import subprocess
from pathlib import Path

# Add project root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def check_virtual_environment():
    """Check if virtual environment is activated."""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment is activated")
        return True
    else:
        print("⚠️  Virtual environment not detected")
        print("Consider running: python -m venv venv && source venv/bin/activate")
        return False

def check_dependencies():
    """Check if required dependencies are installed."""
    import importlib
    required_packages = {
        'flask': 'flask',
        'pymongo': 'pymongo',
        'python-dotenv': 'dotenv',
        'llama-index': 'llama_index',
        'google-generativeai': 'google.generativeai'
    }
    
    missing_packages = []
    for package, import_name in required_packages.items():
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed")
    return True

def check_env_file():
    """Check if .env file exists and has required variables."""
    env_path = Path('.env')
    if not env_path.exists():
        print("❌ .env file not found!")
        print("Create .env file with your API keys")
        return False
    
    with open(env_path, 'r') as f:
        env_content = f.read()
    
    required_vars = ['GEMINI_API_KEY', 'MONGODB_URI']
    missing_vars = []
    
    for var in required_vars:
        if var not in env_content or f"{var}=your_" in env_content:
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Missing or placeholder values in .env: {', '.join(missing_vars)}")
        return False
    
    print("✅ .env file configured")
    return True

def main():
    """Main function to run the application with checks."""
    print("🏆 Hackathon Harvester - Starting Application")
    print("=" * 50)
    
    # Perform checks
    checks = [
        check_python_version(),
        check_virtual_environment(),
        check_dependencies(),
        check_env_file()
    ]
    
    if not all(checks):
        print("\n❌ Some checks failed. Please fix the issues above before running.")
        sys.exit(1)
    
    print("\n🚀 All checks passed! Starting the application...")
    print("🌐 Open http://localhost:5000 in your browser")
    print("📋 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Import and run the Flask app
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
