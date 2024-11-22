#!/bin/bash
# Conway's Game of Life Setup Script

# Ensure Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Ensure pip is installed
if ! command -v pip3 &>/dev/null; then
    echo "pip3 is not installed. Please install pip3 and try again."
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Success message
echo "Setup complete! Run 'python main.py' to start the simulation."
