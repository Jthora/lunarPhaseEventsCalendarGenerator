#!/bin/bash

# Set variables
VENV_DIR="myenv"
PYTHON_SCRIPT="merge_ics_files.py"

# Check for Python installation
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed. Please install Python3 to continue."
    exit 1
fi

# Check for pip installation
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed. Please install pip3 to continue."
    exit 1
fi

# Check for the virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Setting up..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment."
        exit 1
    fi
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment."
    exit 1
fi

# Upgrade pip and install required packages
echo "Upgrading pip and installing required packages..."
pip install --upgrade pip
pip install ics
if [ $? -ne 0 ]; then
    echo "Error: Failed to install required packages."
    deactivate
    exit 1
fi

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: $PYTHON_SCRIPT not found in the current directory."
    deactivate
    exit 1
fi

# Run the Python script
echo "Running $PYTHON_SCRIPT..."
python3 "$PYTHON_SCRIPT"
if [ $? -ne 0 ]; then
    echo "Error: An error occurred while running $PYTHON_SCRIPT."
    deactivate
    exit 1
fi

# Deactivate the virtual environment
echo "Deactivating the virtual environment..."
deactivate

# Completion message
echo "ICS files merged successfully! Check the output directory for the merged file."