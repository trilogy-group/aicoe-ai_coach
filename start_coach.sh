#!/bin/bash

# AI Coach Startup Script

echo "🤖 AI COACH - Personal Productivity System"
echo "=========================================="
echo ""
echo "Checking dependencies..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import pynput" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo "✅ All dependencies ready!"
echo ""
echo "Starting AI Coach..."
echo ""

# Run the coach
python ai_coach.py