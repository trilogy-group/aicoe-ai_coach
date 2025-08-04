#!/bin/bash

# AI Coach POC Demo Runner

echo "🚀 AI Coach Proof-of-Concept System"
echo "===================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Check for API keys
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  Warning: ANTHROPIC_API_KEY not set"
    echo "   Please set: export ANTHROPIC_API_KEY='your-key'"
    exit 1
fi

# Create outputs directory if it doesn't exist
mkdir -p outputs

# Parse command line arguments
MODE=${1:-inference}
DURATION=${2:-60}
USERS=${3:-50}

echo ""
echo "🎯 Running in $MODE mode"
echo "   Duration: $DURATION minutes"
echo "   Users: $USERS"
echo ""

# Run the main program
if [ "$MODE" == "training" ]; then
    if [ -z "$OPENAI_API_KEY" ]; then
        echo "⚠️  Error: OPENAI_API_KEY required for training mode"
        echo "   Please set: export OPENAI_API_KEY='your-key'"
        exit 1
    fi
    echo "🧬 Starting prompt evolution training..."
    python main.py --mode training --users $USERS
else
    echo "💡 Starting real-time coaching simulation..."
    python main.py --mode inference --duration $DURATION --users $USERS
fi

echo ""
echo "✅ Demo completed! Check outputs/ directory for results."