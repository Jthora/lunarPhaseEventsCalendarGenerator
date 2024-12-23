# Instructions

Follow these steps to generate and manage lunar phase calendars.

## Setup

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd lunarPhaseEventsCalendarGenerator
   ```
2. Ensure Python 3.8+ and Bash are installed on your system.
3. Run the setup script to initialize the environment:
   ```bash
   ./run.sh
   ```

## Generating Lunar Phase Calendars
1. Generate .ics files for a specific year range:
   ```bash
   ./run.sh --start_year 2024 --end_year 2048
   ```
2. The .ics files will be saved in the `output/` directory.

## Merging .ics Files
1. Run the merge script to combine all .ics files in the `output/` directory:
   ```bash
   ./run_merge.sh
   ```
2. The merged .ics file will be saved as `output/merged_lunar_phases.ics`.

## Customization
- **Ayanamsa Correction**: By default, ayanamsa correction for Galactic Center Sagittarius 0º is enabled.
Disable it with the `--disable_ayanamsa` flag:
   ```bash
   ./run.sh --disable_ayanamsa
   ```
