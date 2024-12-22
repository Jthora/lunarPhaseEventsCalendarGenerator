# Lunar Phase Events Calendar Generator

This project generates `.ics` calendar files containing detailed lunar phase events for a 25-year period (2024–2048). The calendar includes all major moon phases (New Moon, First Quarter, Full Moon, Third Quarter) and appends culturally significant Full Moon names to the event summaries.

## Features
- Generates `.ics` files for 25 years of lunar phases.
- Includes detailed descriptions for each moon phase.
- Appends cultural names (e.g., "Wolf Moon") to Full Moon summaries.
- Supports timezone customization.
- Compatible with popular calendar applications like Google Calendar, Apple Calendar, and Outlook.

## Requirements
- Python 3.10+ with pip
- Dependencies:
  - `ics`
  - `requests`
  - `skyfield`
  - `pytz`

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd lunar_phase_scripts
   ```

2. Set up the environment and install dependencies:
   ```bash
   ./setup_env.sh
   ```

3. Run the script to generate `.ics` files:
   ```bash
   ./run.sh --timezone "America/New_York"
   ```

## Usage
- Generated `.ics` files will appear in the `output/` directory.
- Each file corresponds to a year, e.g., `lunar_phases_2024.ics`.

## Example Calendar Entry
**Summary**: `🌕 Full Moon (Wolf Moon)`  
**Description**:
```
The Full Moon occurs when the Moon is fully illuminated by the Sun, marking the midpoint of the lunar cycle.
This Full Moon is traditionally called the 'Wolf Moon' for the month of January.
Cultural Significance: Known for its role in agricultural and seasonal cycles.
Astrological Significance: A time of heightened emotions, clarity, and reflection.
```

## Customization
- Specify a timezone with the `--timezone` option:
  ```bash
  ./run.sh --timezone "Europe/London"
  ```

## Troubleshooting
- Ensure `pytz` and other dependencies are installed using the `setup_env.sh` script.
- Check `output/logs.txt` and `lunar_phase_generator_error.log` for errors.

## License
This project is licensed under the MIT License.
