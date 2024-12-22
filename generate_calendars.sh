#!/bin/bash

# Activate the Python environment
if [[ ! -d "myenv" ]]; then
  echo "Python virtual environment not found. Run 'setup_env.sh' first."
  exit 1
fi
source myenv/bin/activate

# Define output directory
OUTPUT_DIR="output"
mkdir -p "$OUTPUT_DIR"

# Get the current year
CURRENT_YEAR=$(date +"%Y")

# Loop through the next 25 years
for ((i=0; i<25; i++)); do
  YEAR=$((CURRENT_YEAR + i))
  echo "Generating lunar phase calendar for year $YEAR..."
  python3 LunarPhaseEventsCalendarGenerator.py --year "$YEAR" >> "$OUTPUT_DIR/logs.txt" 2>&1
  if [[ $? -eq 0 ]]; then
    echo "Successfully generated calendar for year $YEAR."
  else
    echo "Failed to generate calendar for year $YEAR. Check '$OUTPUT_DIR/logs.txt' for details."
  fi
done

echo "All calendars generated. Check the '$OUTPUT_DIR' directory."
