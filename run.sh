#!/bin/bash

# Ensure the script stops on errors
set -e

# Define variables
ENV_DIR="myenv"
EPHEMERIS_FILE="de440s.bsp"
DEFAULT_START_YEAR=2024
DEFAULT_END_YEAR=2048
GALACTICCENTER="on"  # Default galactic center adjustment is "on"
LOG_FILE="output/lunar_phase_generator_error.log"

# Create the output directory if it doesn't exist
OUTPUT_DIR="output"
mkdir -p "$OUTPUT_DIR"

# Check for custom year range arguments
START_YEAR=${1:-$DEFAULT_START_YEAR}
END_YEAR=${2:-$DEFAULT_END_YEAR}

# Function to handle errors and log them
handle_error() {
    echo "An error occurred. Check the log file: $LOG_FILE"
    echo "$(date) - ERROR: $1" >> "$LOG_FILE"
    exit 1
}

# Step 1: Set up the environment
echo "Setting up the environment..."

# Check if the virtual environment already exists
if [ ! -d "$ENV_DIR" ]; then
    echo "Creating a new virtual environment in $ENV_DIR..."
    python3 -m venv "$ENV_DIR" || handle_error "Failed to create virtual environment."
else
    echo "Virtual environment already exists in $ENV_DIR."
fi

# Activate the virtual environment
source "$ENV_DIR/bin/activate" || handle_error "Failed to activate virtual environment."

# Upgrade pip and install dependencies
echo "Upgrading pip and installing required dependencies..."
pip install --upgrade pip || handle_error "Failed to upgrade pip."
pip install -r requirements.txt || handle_error "Failed to install dependencies from requirements.txt."

# Download ephemeris data if not already present
if [ ! -f "$EPHEMERIS_FILE" ]; then
    echo "Downloading ephemeris data..."
    wget -q https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440s.bsp -O "$EPHEMERIS_FILE" || handle_error "Failed to download ephemeris data."
    echo "Ephemeris data downloaded: $EPHEMERIS_FILE"
else
    echo "Ephemeris data already present: $EPHEMERIS_FILE"
fi

echo "Environment setup complete!"

# Step 2: Generate lunar phase calendars
echo "Generating lunar phase calendars for years $START_YEAR to $END_YEAR with galacticCenter=$GALACTICCENTER..."

# Run the Python script and capture errors
python3 LunarPhaseEventsCalendarGenerator.py --start_year "$START_YEAR" --end_year "$END_YEAR" --galactic_center "$GALACTICCENTER" || handle_error "Python script failed during execution."

# Check if output files were generated
if [ "$(ls -A $OUTPUT_DIR/*.ics 2>/dev/null)" ]; then
    echo "Calendars successfully generated. Check the 'output/' directory."
else
    handle_error "No .ics files were generated. Check the Python script and logs."
fi

echo "All done!"