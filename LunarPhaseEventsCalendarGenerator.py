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
    1: "🌓 1st Quarter Moon",
    2: "🌕 Full Moon",
    3: "🌗 3rd Quarter Moon"
}

# Cultural moon names for Full Moons
CULTURAL_MOON_NAMES = {
    1: "Wolf",
    2: "Snow",
    3: "Worm",
    4: "Pink",
    5: "Flower",
    6: "Strawberry",
    7: "Buck",
    8: "Sturgeon",
    9: "Harvest",
    10: "Hunter's",
    11: "Beaver",
    12: "Cold"
}

# Cultural significance for Full Moons
CULTURAL_SIGNIFICANCES = {
    "Wolf": "The Wolf Moon is deeply tied to the haunting howls of wolves that echo through the cold winter air, symbolizing survival and community in harsh conditions. It serves as a reminder of the strong bonds within wolf packs and the importance of perseverance. This moon has often inspired tales and myths of transformation and primal instincts.",
    "Snow": "The Snow Moon represents the heaviest snowfalls of the year, blanketing the earth in quiet stillness. It reflects the challenges of enduring the harshness of winter while finding beauty in the frozen landscapes. Many cultures see this moon as a time to gather together and share warmth and stories by the fire.",
    "Worm": "The Worm Moon signifies the thawing earth as spring approaches, with earthworms emerging to rejuvenate the soil. This moon celebrates the return of fertility and the cycles of renewal, marking a time for planting and new beginnings. Its name reflects a connection to the rhythms of nature and the changing of the seasons.",
    "Pink": "The Pink Moon gets its name from the first vibrant blooms of wild pink phlox, heralding the arrival of spring. It symbolizes renewal, growth, and the awakening of life after the cold winter months. This moon is often associated with hope, beauty, and the reemergence of color in the natural world.",
    "Flower": "The Flower Moon celebrates the abundance of blooming flowers in May, a time of lush growth and beauty. It embodies the energy of fertility, creativity, and the flourishing of life. Many cultures see this moon as a time to honor the earth’s generosity and participate in rituals of gratitude.",
    "Strawberry": "The Strawberry Moon marks the peak of the strawberry harvest, bringing sweetness and nourishment to summer. It symbolizes abundance, prosperity, and the rewards of hard work. This moon is often celebrated with gatherings and feasts, reflecting the joy of nature’s bounty.",
    "Buck": "The Buck Moon signifies the growth of antlers on young bucks, a powerful symbol of strength and vitality. It reflects a time of personal development, preparation, and stepping into one's power. This moon has long been associated with the wild energy of nature and the cycle of maturity.",
    "Sturgeon": "The Sturgeon Moon is named for the large sturgeon fish caught in abundance during August, a crucial time for survival in many communities. It highlights the relationship between humanity and water, symbolizing sustenance and the gifts of the rivers and lakes. This moon is often linked to themes of gratitude and interdependence.",
    "Harvest": "The Harvest Moon illuminates the fields during the critical time of reaping crops, allowing farmers to work late into the night. It symbolizes hard work, fulfillment, and the rewards of dedication. This moon is celebrated as a time of gathering and preparing for the winter ahead.",
    "Hunter's": "The Hunter's Moon marks the season of hunting game, providing resources for the harsh months of winter. It is a symbol of self-reliance, strategy, and the balance between giving and taking from nature. This moon has inspired many traditional rituals and celebrations of the hunt.",
    "Beaver": "The Beaver Moon reflects the industrious nature of beavers building their winter dams, a reminder of the importance of preparation and community. It symbolizes resilience, resourcefulness, and working together to create security for the future. This moon often carries a sense of determination and focus.",
    "Cold": "The Cold Moon marks the longest nights of the year and the deep chill of December, symbolizing endurance and reflection. It invites introspection and quiet moments to appreciate the stillness of winter. This moon is a time for rest and finding inner warmth amidst the season’s challenges."
}

# Zodiac signs, emoji, and descriptions
ZODIAC_SIGNS = [
    ("Aries", "♈ <🜂>", 
     "Cardinal Fire ▲ 🔥\nWhen the Moon is in Aries, its energy is bold, impulsive, and action-oriented. This is a time for initiating projects, taking risks, and embracing dynamic energy. The fiery influence of Aries enhances courage and determination but may also heighten impatience or restlessness."),
    ("Taurus", "♉ [🜃]", 
     "Fixed Earth ■ ⛰️\nThe Moon in Taurus brings a grounded, steady, and sensual energy. It is a time to focus on comfort, stability, and enjoying the pleasures of life. Taurus' connection to the Earth helps anchor emotions, encouraging patience and long-term planning."),
    ("Gemini", "♊ (🜁)", 
     "Mutable Air ● 💨\nWhen the Moon is in Gemini, communication, curiosity, and mental agility are heightened. This is an excellent time for gathering information, exploring new ideas, and socializing. The adaptable energy of Gemini can bring variety and excitement, though it may scatter focus."),
    ("Cancer", "♋ <🜄>", 
     "Cardinal Water ▲ 💧\nThe Moon feels at home in Cancer, amplifying emotions, intuition, and the need for nurturing. This is a time for focusing on home, family, and emotional well-being. Cancer’s protective energy encourages self-care and deep connections, but it may also bring sensitivity or moodiness."),
    ("Leo", "♌ [🜂]", 
     "Fixed Fire ■ 🔥\nWhen the Moon is in Leo, creativity, self-expression, and confidence are emphasized. It’s a time for shining brightly, taking pride in achievements, and seeking recognition. Leo’s influence inspires warmth and generosity, but it may also amplify a need for attention."),
    ("Virgo", "♍ (🜃)", 
     "Mutable Earth ● ⛰️\nThe Moon in Virgo enhances focus on details, organization, and practical solutions. This is a time for analyzing emotions and finding ways to be of service to others. Virgo’s grounded energy promotes self-improvement and mindfulness, though it may also bring self-criticism."),
    ("Libra", "♎ <🜁>", 
     "Cardinal Air ▲ 💨\nWhen the Moon is in Libra, balance, harmony, and relationships take center stage. This is an ideal time for diplomacy, collaboration, and creating beauty in one’s environment. Libra’s airy energy fosters a desire for fairness and connection, though it may also lead to indecisiveness."),
    ("Scorpio", "♏ [🜄]", 
     "Fixed Water ■ 💧\nThe Moon in Scorpio brings intense, transformative, and deeply emotional energy. This is a time for diving into hidden truths, exploring passions, and embracing change. Scorpio’s influence encourages emotional depth and resilience but may also amplify secrecy or possessiveness."),
    ("Sagittarius", "♐ (🜂)", 
     "Mutable Fire ● 🔥\nWhen the Moon is in Sagittarius, optimism, adventure, and philosophical exploration are highlighted. It’s a time for expanding horizons, seeking knowledge, and embracing freedom. Sagittarius’ fiery energy inspires enthusiasm and growth, though it may also bring restlessness."),
    ("Capricorn", "♑ <🜃>", 
     "Cardinal Earth ▲ ⛰️\nThe Moon in Capricorn emphasizes discipline, ambition, and responsibility. This is a time for setting long-term goals, focusing on work, and achieving practical results. Capricorn’s grounded energy supports perseverance and structure but may also feel emotionally reserved."),
    ("Aquarius", "♒ [🜁]", 
     "Fixed Air ■ 💨\nWhen the Moon is in Aquarius, innovation, independence, and humanitarian ideals are amplified. This is a time for thinking outside the box, exploring unconventional ideas, and fostering community. Aquarius’ influence encourages intellectual curiosity and progressive thinking, though it may also feel detached emotionally."),
    ("Pisces", "♓ (🜄)", 
     "Mutable Water ● 💧\nThe Moon in Pisces enhances intuition, dreaminess, and compassion. This is a time for creativity, spiritual exploration, and connecting with the deeper currents of emotion. Pisces’ watery energy promotes empathy and imagination but may also bring escapism or confusion.")
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

# Fractional Year
def fractional_year(date_str, time_str):
    date_time = datetime.strptime(f"{date_str} {time_str}", "%b %d, %Y %H:%M")
    year = date_time.year
    start_of_year = datetime(year, 1, 1)
    day_of_year = (date_time - start_of_year).total_seconds() / 86400
    return year + (day_of_year / 365.25)

# Galactic Center Sag 0º Ayanamsa Calculation
def calculate_ayanamsa(fractional_year):
    return REFERENCE_POSITION - (fractional_year - REFERENCE_YEAR) * PRECESSION_RATE

def adjust_position(position, ayanamsa):
    corrected_position = position - ayanamsa
    return corrected_position % 360  # Wrap around 0-360

# Zodiac Calculation
def calculate_zodiac(longitude):
    """
    Determine the zodiac sign based on the ecliptic longitude.
    """
    if longitude is None or not (0 <= longitude < 360):
        logging.error(f"Invalid longitude value: {longitude}")
        return "Unknown", "", "No description available."
    zodiac_index = int((longitude % 360) / 30)
    return ZODIAC_SIGNS[zodiac_index]

def calculate_lunar_phases(year, eph, timescale, galacticCenter_on=True):
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

                if galacticCenter_on:
                    # Calculate fractional year for Galactic Center
                    fractional_year_value = t.utc_datetime().year + (t.utc_datetime().timetuple().tm_yday / 365.25)
                    galacticCenter = calculate_ayanamsa(fractional_year_value)

                    # Adjust longitude with Galactic Center
                    corrected_longitude = adjust_position(longitude, galacticCenter)
                else:
                    corrected_longitude = longitude

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

def create_ics_file(phases, year, timezone, galacticCenter_on=True):
    """
    Create an ICS file from lunar phases and save it in the output directory.
    """
    try:
        calendar = Calendar()

        alignment = "Galactic Center"
        if galacticCenter_on!=True:
            alignment = "Western Occult"


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
                    "The Full Moon occurs when the Moon is fully illuminated by the Sun, marking the midpoint of the lunar cycle.\n\n"
                    + "This Full Moon is traditionally called the '" + cultural_name + " Moon' for the month of "
                    + localized_datetime.strftime('%B') + ". " + cultural_significance + "\n\n"
                    + "Significance: A time of culmination, celebration, and achieving clarity.\n\n"
                    + "Meaning: A time of heightened emotions, clarity, and reflection.\n\n"
                    + "Zodiac: " + zodiac_name + " " + zodiac_emoji + "\n"
                    + "Alignment: " + alignment + "\n\n"
                    + "Description: " + zodiac_description
                )
            elif "New Moon" in phase_name:
                description = (
                    "The New Moon marks the beginning of the lunar cycle.\n\n"
                    + "The Moon is positioned between the Earth and the Sun, making it invisible from Earth.\n\n"
                    + "Significance: A time for setting intentions and new beginnings.\n\n"
                    + "Meaning: Represents a fresh start, reflection, and inward focus.\n\n"
                    + "Zodiac: " + zodiac_name + " " + zodiac_emoji + "\n"
                    + "Alignment: " + alignment + "\n\n"
                    + "Description: " + zodiac_description
                )
            elif "1st Quarter" in phase_name:
                description = (
                    "The First Quarter Moon occurs when half the Moon is illuminated, and the other half remains dark.\n\n"
                    + "This phase is a time of action, decisions, and challenges as you work toward your goals.\n\n"
                    + "Significance: Represents a period of growth and progress in many traditions.\n\n"
                    + "Meaning: A time to confront obstacles and make important choices, paving the way for success.\n\n"
                    + "Zodiac: " + zodiac_name + " " + zodiac_emoji + "\n"
                    + "Alignment: " + alignment + "\n\n"
                    + "Description: " + zodiac_description
                )
            elif "3rd Quarter" in phase_name:
                description = (
                    "The Third Quarter Moon occurs when half the Moon is illuminated as it wanes toward the New Moon.\n\n"
                    + "This phase symbolizes release, reflection, and preparation for the next cycle.\n\n"
                    + "Significance: Often associated with closure and letting go of what no longer serves you.\n\n"
                    + "Meaning: A period of introspection, evaluation, and setting the stage for new beginnings.\n\n"
                    + "Zodiac: " + zodiac_name + " " + zodiac_emoji + "\n"
                    + "Alignment: " + alignment + "\n\n"
                    + "Description: " + zodiac_description
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
    parser.add_argument("--galactic_center", type=str, choices=["on", "off"], default="on", help="Toggle ayanamsa Galactic Center correction (default: on).")
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
        galacticCenter_on = (args.galactic_center == "on")
        phases = calculate_lunar_phases(year, eph, timescale, galacticCenter_on)
        if phases:
            create_ics_file(phases, year, "UTC", galacticCenter_on)
        else:
            print(f"Failed to generate calendar for year {year}. Check {LOG_FILE} for details.")

if __name__ == "__main__":
    main()