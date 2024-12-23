import os
from ics import Calendar, Event
import logging

# Directory containing the .ics files
OUTPUT_DIR = "output"
MERGED_FILE = os.path.join(OUTPUT_DIR, "merged_lunar_phases.ics")

# Logging setup
LOG_FILE = os.path.join(OUTPUT_DIR, "merge_ics_error.log")
logging.basicConfig(filename=LOG_FILE, level=logging.ERROR, format='%(asctime)s - %(message)s')

def merge_ics_files(output_dir, merged_file):
    """
    Merge all .ics files in the specified directory into a single .ics file.
    """
    try:
        if not os.path.exists(output_dir):
            print(f"Output directory '{output_dir}' does not exist.")
            return

        merged_calendar = Calendar()
        event_ids = set()  # To track unique event IDs and avoid duplication

        # Find all .ics files in the directory
        ics_files = sorted([f for f in os.listdir(output_dir) if f.endswith('.ics')])
        if not ics_files:
            print("No .ics files found in the output directory.")
            return

        print(f"Found {len(ics_files)} .ics files to merge.")

        for ics_file in ics_files:
            file_path = os.path.join(output_dir, ics_file)
            try:
                with open(file_path, 'r') as f:
                    calendar = Calendar(f.read())
                    for event in calendar.events:
                        # Check for duplicate events by UID
                        if event.uid not in event_ids:
                            merged_calendar.events.add(event)
                            event_ids.add(event.uid)
                        else:
                            logging.warning(f"Duplicate event UID skipped: {event.uid}")
            except Exception as e:
                logging.error(f"Error reading file {ics_file}: {e}", exc_info=True)
                print(f"Warning: Could not read file '{ics_file}', check the logs for details.")

        # Write the merged calendar to a single file
        try:
            with open(merged_file, 'w') as f:
                f.writelines(merged_calendar)
            print(f"Merged .ics file created: {merged_file}")
        except Exception as e:
            logging.error(f"Error writing merged file: {e}", exc_info=True)
            print("Error: Failed to write the merged .ics file. Check the logs for details.")

    except Exception as e:
        logging.error(f"Critical error during merging: {e}", exc_info=True)
        print("Critical error occurred during merging. Check the logs for details.")

if __name__ == "__main__":
    merge_ics_files(OUTPUT_DIR, MERGED_FILE)