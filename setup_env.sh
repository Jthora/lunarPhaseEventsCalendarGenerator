#!/bin/bash

# Setup Python virtual environment
if [ ! -d "myenv" ]; then
  echo "Creating Python virtual environment..."
  python3 -m venv myenv
fi

source myenv/bin/activate

# Install required Python libraries
echo "Installing required Python libraries..."
pip install --upgrade pip
pip install -r requirements.txt || pip install skyfield ics requests

# Download the ephemeris file if it doesn't exist
if [ ! -f "de440s.bsp" ]; then
  echo "Downloading Skyfield ephemeris data..."
  wget https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440s.bsp -O de440s.bsp
fi

echo "Environment setup complete. Run 'source myenv/bin/activate' to activate the environment."