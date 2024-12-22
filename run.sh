#!/bin/bash

# Step 1: Run the setup script
echo "Preparing environment..."
bash setup_env.sh
if [[ $? -ne 0 ]]; then
  echo "Environment setup failed. Please check the output and try again."
  exit 1
fi

# Step 2: Generate calendars
echo "Generating 25 years of lunar phase calendars..."
bash generate_calendars.sh
