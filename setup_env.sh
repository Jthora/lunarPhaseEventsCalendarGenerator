#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
  echo "Python 3 is not installed. Please install it and try again."
  exit 1
fi

# Set up a virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv myenv
source myenv/bin/activate

# Install dependencies
echo "Installing required Python libraries..."
pip install -r requirements.txt

echo "Environment setup complete. Run 'source myenv/bin/activate' to activate the environment."
