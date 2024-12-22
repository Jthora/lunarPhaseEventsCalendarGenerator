import os
import logging
from datetime import datetime
import requests
from ics import Calendar, Event
import argparse

# Directory for output files
OUTPUT_DIR = "lunar_phase_generator_output"

# Logging setup
LOG_FILE = os.path.join(OUTPUT_DIR, "error.log")
os.makedirs(OUTPUT_DIR, exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.ERROR, format='%(asctime)s - %(message)s')

# Moon phases and emojis
MOON_PHASES = {
    "New Moon": "🌑",
    "First Quarter": "🌓",
    "Full Moon": "🌕",
    "Last Quarter": "🌗",
    "3rd Quarter": "🌗"
}

def fetch_lunar_phases(year):
    """
    Fetch lunar phase data from a public API and parse it.
    Adjusts for the actual API response format.
    """
    url = f"https://api.farmsense.net/v1/moonphases/?d={year}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Debugging: Print the raw API response
        print("API Response:", data)
        logging.info(f"Raw API response: {data}")
        
        # Parse and return the phases
        phases = []
        for item in data:
            target_date = item.get("TargetDate", "")
            phase = item.get("Phase", "Unknown")
            
            if target_date and phase:
                try:
                    # Convert TargetDate to a datetime object
                    date = datetime.strptime(target_date, "%Y")
                    phases.append({"date": date, "phase": phase})
                except ValueError as e:
                    logging.error(f"Error parsing date: {target_date}, error: {e}")
        
        return phases
    except requests.RequestException as e:
        logging.error(f"Error fetching lunar phases for {year}: {e}")
        print(f"Failed to fetch data for {year}. Please check your network or the API URL.")
        return []
    except (KeyError, ValueError) as e:
        logging.error(f"Error parsing API response: {e}")
        print(f"Unexpected data format from API. Check {LOG_FILE} for details.")
        return []

def create_ics_file(phases, year):
    """
    Create an ICS file from lunar phases and save it in the output directory.
    """
    try:
        calendar = Calendar()

        for phase in phases:
            date = phase["date"]
            phase_name = phase["phase"]
            emoji = MOON_PHASES.get(phase_name, "")
            
            event = Event()
            event.name = f"{emoji} {phase_name}".strip()
            event.begin = date.strftime('%Y-%m-%d')
            event.make_all_day()
            calendar.events.add(event)

        output_file = os.path.join(OUTPUT_DIR, f"lunar_phases_{year}.ics")
        with open(output_file, 'w') as f:
            f.writelines(calendar)

        print(f"ICS file created: {output_file}")
    except Exception as e:
        logging.error(f"Error creating ICS file for {year}: {e}")
        print(f"Failed to create the ICS file for {year}. Check {LOG_FILE} for details.")

def main():
    """
    Main function to handle argument parsing and process lunar phases.
    """
    parser = argparse.ArgumentParser(description="Generate a lunar phase calendar in ICS format.")
    parser.add_argument("--year", type=int, help="Year for the lunar phases (defaults to current year).")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging.")
    args = parser.parse_args()

    # Enable verbose logging if requested
    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)

    # Determine the year
    year = args.year if args.year else datetime.now().year

    # Fetch lunar phases and create ICS file
    print(f"Fetching lunar phases for the year {year}...")
    phases = fetch_lunar_phases(year)
    if phases:
        create_ics_file(phases, year)
    else:
        print(f"No lunar phases data available for {year}. Check {LOG_FILE} for details.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Error in script execution: {e}")
        print(f"An unexpected error occurred. Check {LOG_FILE} for details.")