# Lunar Phase Events Calendar Generator
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14545444.svg)](https://doi.org/10.5281/zenodo.14545444) - [Defensive Publication Declaration](https://en.wikipedia.org/wiki/Defensive_publication)

![Lunar Phase Events Calendar Generator](lunarPhaseEventsCalendarGenerator-small.png)

This repository contains tools to generate and manage `.ics` calendar files for lunar phase events. The generator includes options for cultural and astrological details for each lunar phase, making it useful for educational, astrological, or personal planning purposes.

## Features

- Generates `.ics` files for lunar phases between a specified year range.
- Includes cultural names for Full Moons and astrological zodiac signs for lunar phases.
- Supports ayanamsa correction for Galactic Center Sagittarius 0º.
- Merges multiple `.ics` files into a single comprehensive calendar.

## Scripts

1. **`LunarPhaseEventsCalendarGenerator.py`**  
   Generates lunar phase `.ics` files with cultural and astrological details.

2. **`merge_ics_files.py`**  
   Merges multiple `.ics` files into a single file.

3. **`run.sh`**  
   Automates the setup and generation of `.ics` files.

4. **`run_merge.sh`**  
   Automates the merging of `.ics` files in the output directory.

## Requirements

- Python 3.8+
- Required Python libraries (installed via `requirements.txt`).
- Bash shell for executing `.sh` scripts.

