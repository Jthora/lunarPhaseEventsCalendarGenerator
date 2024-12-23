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

# Zodiac signs, emoji, and descriptions
ZODIAC_SIGNS = [
    ("Aries", "♈", "Fiery, passionate, and driven."),
    ("Taurus", "♉", "Grounded, practical, and loyal."),
    ("Gemini", "♊", "Curious, communicative, and versatile."),
    ("Cancer", "♋", "Emotional, nurturing, and protective."),
    ("Leo", "♌", "Confident, creative, and bold."),
    ("Virgo", "♍", "Detail-oriented, analytical, and helpful."),
    ("Libra", "♎", "Charming, harmonious, and diplomatic."),
    ("Scorpio", "♏", "Intense, transformative, and magnetic."),
    ("Sagittarius", "♐", "Adventurous, philosophical, and optimistic."),
    ("Capricorn", "♑", "Disciplined, ambitious, and practical."),
    ("Aquarius", "♒", "Innovative, independent, and humanitarian."),
    ("Pisces", "♓", "Dreamy, intuitive, and compassionate.")
]

# Constants
REFERENCE_POSITION = 26.854  # Galactic Center position in degrees (year 2000)
PRECESSION_RATE = 0.01397    # Degrees per year due to precession
REFERENCE_YEAR = 2000        # Base year for Galactic Center alignment

# Zodiac Signs and Degree Ranges
ZODIAC_SIGN_DEGREE_RANGES = [
    ('Aries', 0, 30), ('Taurus', 30, 60), ('Gemini', 60, 90),
    ('Cancer', 90, 120), ('Leo', 120, 150), ('Virgo', 150, 180),
    ('Libra', 180, 210), ('Scorpio', 210, 240), ('Sagittarius', 240, 270),
    ('Capricorn', 270, 300), ('Aquarius', 300, 330), ('Pisces', 330, 360)
]

# Functions
def fractional_year(date_str, time_str):
    date_time = datetime.strptime(f"{date_str} {time_str}", "%b %d, %Y %H:%M")
    year = date_time.year
    start_of_year = datetime(year, 1, 1)
    day_of_year = (date_time - start_of_year).total_seconds() / 86400
    return year + (day_of_year / 365.25)

def calculate_ayanamsa(fractional_year):
    return REFERENCE_POSITION - (fractional_year - REFERENCE_YEAR) * PRECESSION_RATE

def adjust_position(position, ayanamsa):
    corrected_position = position - ayanamsa
    return corrected_position % 360  # Wrap around 0-360

def calculate_zodiac(longitude):
    """
    Determine the zodiac sign based on the ecliptic longitude.
    """
    if longitude is None or not (0 <= longitude < 360):
        logging.error(f"Invalid longitude value: {longitude}")
        return "Unknown", "", "No description available."
    zodiac_index = int((longitude % 360) / 30)
    return ZODIAC_SIGNS[zodiac_index]

def calculate_lunar_phases(year, eph, timescale):
    """
    Calculate exact lunar phases for a given year using Skyfield.
    """
    try:
        # Define the time range for the year
        start_time = timescale.utc(year, 1, 1)
        end_time = timescale.utc(year + 1, 1, 1)

        # Calculate lunar phases
        try:
            times, phases = almanac.find_discrete(start_time, end_time, almanac.moon_phases(eph))
            if len(times) == 0:
                logging.warning(f"No lunar phases found for year {year}. Check ephemeris data and time range.")
        except Exception as e:
            logging.error(f"Error during lunar phase calculation for year {year}: {e}", exc_info=True)
            raise RuntimeError("Lunar phase calculation failed.") from e

        # Map phases to their names and emojis
        events = []
        earth = eph["earth"]
        moon = eph["moon"] 
        for t, phase in zip(times, phases):
            phase_name = MOON_PHASES.get(phase, "Unknown Phase")

            # Calculate Moon's position
            try:
                astrometric = earth.at(t).observe(moon)
                longitude = astrometric.apparent().ecliptic_latlon()[1].degrees

                # Calculate fractional year for Ayanamsa
                fractional_year_value = t.utc_datetime().year + (t.utc_datetime().timetuple().tm_yday / 365.25)
                ayanamsa = calculate_ayanamsa(fractional_year_value)

                # Adjust longitude with Ayanamsa
                corrected_longitude = adjust_position(longitude, ayanamsa)

            except NameError as e:
                logging.error(f"NameError: {e} - Ensure ephemeris objects are initialized correctly.")
                continue
            except UnboundLocalError as e:
                logging.error(f"UnboundLocalError: {e} - Issue with variable assignment.")
                continue
            try:
                longitude = astrometric.apparent().ecliptic_latlon()[1].degrees
                zodiac_name, zodiac_emoji, zodiac_description = calculate_zodiac(corrected_longitude)
            except Exception as e:
                logging.error(f"Error in zodiac calculation for longitude {longitude}: {e}", exc_info=True)
                zodiac_name, zodiac_emoji, zodiac_description = "Unknown", "❓", "Unknown significance."

            events.append({
                "datetime": t.utc_datetime(),
                "phase": phase_name,
                "zodiac_name": zodiac_name,
                "zodiac_emoji": zodiac_emoji,
                "zodiac_description": zodiac_description
            })

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
            zodiac_name = phase["zodiac_name"]
            zodiac_emoji = phase["zodiac_emoji"]
            zodiac_description = phase["zodiac_description"]
            try:
                localized_datetime = phase_datetime.astimezone(pytz.timezone(timezone))
            except pytz.UnknownTimeZoneError:
                logging.error(f"Invalid timezone: {timezone}")
                localized_datetime = phase_datetime

            # Determine cultural moon name for Full Moon
            cultural_title = ""
            if "Full Moon" in phase_name:
                month = localized_datetime.month
                cultural_title = CULTURAL_MOON_NAMES.get(month, "Full Moon")
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
                    + "Astrological Position: The Moon is in " + zodiac_name + " " + zodiac_emoji + ".\n"
                    + "Astrological Significance: " + zodiac_description + "\n"
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
            event.name = phase_name + cultural_title + " " + zodiac_emoji
            event.begin = localized_datetime.strftime('%Y-%m-%dT%H:%M:%S%z')
            event.description = description
            calendar.events.add(event)

        try:
            output_file = os.path.join(OUTPUT_DIR, f"lunar_phases_{year}.ics")
            if not calendar.events:
                logging.warning(f"No events generated for year {year}.")
            with open(output_file, 'w') as f:
                f.writelines(calendar)
            logging.info(f"Successfully created ICS file: {output_file}")
        except Exception as e:
            logging.error(f"Error writing ICS file for year {year}: {e}", exc_info=True)
            raise RuntimeError(f"Failed to write ICS file for year {year}.") from e

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

    if args.start_year > args.end_year:
        logging.error("Start year cannot be greater than end year.")
        raise ValueError("Invalid year range: Start year must be less than or equal to end year.")

    try:
        eph = load_file("de440s.bsp")
    except FileNotFoundError:
        logging.error("Ephemeris file 'de440s.bsp' not found.")
        print("Ephemeris file is missing. Please ensure 'de440s.bsp' is present in the working directory.")
        return

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