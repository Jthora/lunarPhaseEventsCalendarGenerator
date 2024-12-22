#!/bin/bash

# Activate the Python environment
if [ ! -d "myenv" ]; then
  echo "Error: Python virtual environment not found. Run 'setup_env.sh' first." >&2
  exit 1
fi
source myenv/bin/activate

# Define output directory
OUTPUT_DIR="output"
mkdir -p "$OUTPUT_DIR"

# Initialize counters
FAILURE_COUNT=0
SUCCESS_COUNT=0

# Generate calendars for 25 years
for YEAR in {2024..2048}; do
  echo "Generating lunar phase calendar for year $YEAR..."
  python3 LunarPhaseEventsCalendarGenerator.py >> "$OUTPUT_DIR/logs.txt" 2>&1

  if [ $? -eq 0 ] && [ -f "$OUTPUT_DIR/lunar_phases_${YEAR}.ics" ]; then
    echo "Successfully generated calendar for year $YEAR."
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
  else
    echo "Failed to generate calendar for year $YEAR. Check '$OUTPUT_DIR/logs.txt' for details." >&2
    FAILURE_COUNT=$((FAILURE_COUNT + 1))
  fi
done

# Report summary
echo "====================================="
echo "Generation Summary:"
echo "  Successful Years: $SUCCESS_COUNT"
echo "  Failed Years: $FAILURE_COUNT"
if [ $FAILURE_COUNT -gt 0 ]; then
  echo "Some calendars failed to generate. Check logs for details." >&2
else
  echo "All calendars generated successfully!"
fi
echo "====================================="