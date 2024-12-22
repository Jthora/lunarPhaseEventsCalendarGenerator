import os
import logging
from datetime import datetime
from skyfield.api import load_file, load
from skyfield import almanac
from ics import Calendar, Event
import argparse
import pytz

# Directory for output files
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Logging setup
LOG_FILE = os.path.join(OUTPUT_DIR, "lunar_phase_generator_error.log")
logging.basicConfig(filename=LOG_FILE, level=logging.ERROR, format='%(asctime)s - %(message)s')

# Moon phases and emojis
MOON_PHASES = {
    0: "🌑 New Moon",
    1: "🌓 First Quarter Moon",
    2: "🌕 Full Moon",
    3: "🌗 Third Quarter Moon"
}

# Cultural moon names for Full Moons
CULTURAL_MOON_NAMES = {
    1: "Wolf Moon",
    2: "Snow Moon",
    3: "Worm Moon",
    4: "Pink Moon",
    5: "Flower Moon",
    6: "Strawberry Moon",
    7: "Buck Moon",
    8: "Sturgeon Moon",
    9: "Harvest Moon",
    10: "Hunter's Moon",
    11: "Beaver Moon",
    12: "Cold Moon"
}

# Cultural significance for Full Moons
CULTURAL_SIGNIFICANCES = {
    "Wolf Moon": "Often associated with howling wolves during the cold winter months.",
    "Snow Moon": "Reflects the heavy snowfalls typically experienced in February.",
    "Worm Moon": "Named for the reappearance of earthworms as the ground thaws in spring.",
    "Pink Moon": "Named after pink wildflowers, signaling spring blooms.",
    "Flower Moon": "Marks the abundance of blooming flowers in May.",
    "Strawberry Moon": "Named for the strawberry harvest season.",
    "Buck Moon": "Represents the time when antlers of young bucks are in full growth.",
    "Sturgeon Moon": "Named for the large sturgeon fish caught in August.",
    "Harvest Moon": "Associated with the time of harvesting crops in early autumn.",
    "Hunter's Moon": "Traditionally marks the time for hunting game before winter.",
    "Beaver Moon": "Named for the time beavers build their winter dams.",
    "Cold Moon": "Reflects the cold, long nights of December."
}

def calculate_lunar_phases(year, eph, timescale):
    """
    Calculate exact lunar phases for a given year using Skyfield.
    """
    try:
        # Define the time range for the year
        start_time = timescale.utc(year, 1, 1)
        end_time = timescale.utc(year + 1, 1, 1)

        # Calculate lunar phases
        times, phases = almanac.find_discrete(start_time, end_time, almanac.moon_phases(eph))

        # Map phases to their names and emojis
        events = []
        for t, phase in zip(times, phases):
            phase_name = MOON_PHASES.get(phase, "Unknown Phase")
            events.append({"datetime": t.utc_datetime(), "phase": phase_name})

        return events
    except Exception as e:
        logging.error(f"Error calculating lunar phases for year {year}: {e}", exc_info=True)
        return []

def create_ics_file(phases, year, timezone):
    """
    Create an ICS file from lunar phases and save it in the output directory.
    """
    try:
        calendar = Calendar()

        for phase in phases:
            phase_datetime = phase["datetime"]
            phase_name = phase["phase"]
            localized_datetime = phase_datetime.astimezone(pytz.timezone(timezone))

            # Determine cultural moon name for Full Moon
            cultural_title = ""
            if "Full Moon" in phase_name:
                month = localized_datetime.month
                cultural_title = CULTURAL_MOON_NAMES.get(month, "")
                if cultural_title:
                    cultural_title = f" ({cultural_title})"

            # Determine cultural moon name for Full Moon
            cultural_name = ""
            cultural_significance = CULTURAL_SIGNIFICANCES.get(cultural_name, "No cultural significance available.")
            if "Full Moon" in phase_name:
                month = localized_datetime.month
                cultural_name = CULTURAL_MOON_NAMES.get(month, "")
                if cultural_name:
                    cultural_name = f"{cultural_name}"
                    cultural_significance = CULTURAL_SIGNIFICANCES.get(cultural_name, "No cultural significance available.")

            # Enhanced descriptions
            if "Full Moon" in phase_name:
                description = (
                    "The Full Moon occurs when the Moon is fully illuminated by the Sun, marking the midpoint of the lunar cycle.\n"
                    + "This Full Moon is traditionally called the '" + cultural_name + "' for the month of "
                    + localized_datetime.strftime('%B') + ".\n"
                    + "Cultural Significance: " + cultural_significance + "\n"
                    + "Astrological Significance: A time of heightened emotions, clarity, and reflection."
                )
            elif "New Moon" in phase_name:
                description = (
                    "The New Moon marks the beginning of the lunar cycle. "
                    + "The Moon is positioned between the Earth and the Sun, making it invisible from Earth.\n"
                    + "Cultural Significance: A time for setting intentions and new beginnings.\n"
                    + "Astrological Significance: Represents a fresh start, reflection, and inward focus."
                )
            elif "First Quarter" in phase_name:
                description = (
                    "The First Quarter Moon occurs when half the Moon is illuminated, and the other half remains dark.\n"
                    + "This phase is a time of action, decisions, and challenges as you work toward your goals.\n"
                    + "Cultural Significance: Represents a period of growth and progress in many traditions.\n"
                    + "Astrological Significance: A time to confront obstacles and make important choices, paving the way for success."
                )
            elif "Third Quarter" in phase_name:
                description = (
                    "The Third Quarter Moon occurs when half the Moon is illuminated as it wanes toward the New Moon.\n"
                    + "This phase symbolizes release, reflection, and preparation for the next cycle.\n"
                    + "Cultural Significance: Often associated with closure and letting go of what no longer serves you.\n"
                    + "Astrological Significance: A period of introspection, evaluation, and setting the stage for new beginnings."
                )
            else:
                description = (
                    "The " + phase_name + " occurs as part of the lunar cycle. "
                    + "It represents a transition toward the next phase of the Moon."
                )

            # Create the event
            event = Event()
            event.name = phase_name + cultural_title
            event.begin = localized_datetime.strftime('%Y-%m-%dT%H:%M:%S%z')
            event.description = description
            calendar.events.add(event)

        output_file = os.path.join(OUTPUT_DIR, f"lunar_phases_{year}.ics")
        with open(output_file, 'w') as f:
            f.writelines(calendar)

        print(f"ICS file created: {output_file}")
    except Exception as e:
        logging.error(f"Error creating ICS file for year {year}: {e}", exc_info=True)

def main():
    """
    Main function to handle lunar phase generation.
    """
    parser = argparse.ArgumentParser(description="Generate lunar phase calendar ICS files.")
    parser.add_argument("--start_year", type=int, default=2024, help="Start year for calendar generation (default: 2024).")
    parser.add_argument("--end_year", type=int, default=2048, help="End year for calendar generation (default: 2048).")
    args = parser.parse_args()

    eph = load_file("de440s.bsp")
    timescale = load.timescale()

    for year in range(args.start_year, args.end_year + 1):
        print(f"Generating lunar phase calendar for year {year}...")
        phases = calculate_lunar_phases(year, eph, timescale)
        if phases:
            create_ics_file(phases, year, "UTC")
        else:
            print(f"Failed to generate calendar for year {year}. Check {LOG_FILE} for details.")

if __name__ == "__main__":
    main()