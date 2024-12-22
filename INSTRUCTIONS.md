
# Instructions: Lunar Phase Events Calendar Generator

## Overview
This project provides tools to generate ICS calendar files for lunar phases (e.g., New Moon, Full Moon) for any given year or the next 25 years automatically. It includes Python scripts and Bash scripts for easy setup and automation, making it beginner-friendly.

---

## Contents
1. `LunarPhaseEventsCalendarGenerator.py` - The main Python script for generating ICS files for a specified year.
2. `setup_env.sh` - A Bash script to prepare the Python environment and install dependencies.
3. `generate_calendars.sh` - A Bash script to generate ICS files for the next 25 years.
4. `run.sh` - A master Bash script that runs everything in sequence.

---

## Prerequisites

### Requirements
- **Python 3.7 or later**:
  - Check your Python version:
    ```bash
    python3 --version
    ```
  - If not installed:
    - **macOS**: Install with Homebrew:
      ```bash
      brew install python
      ```
    - **Linux**:
      ```bash
      sudo apt update
      sudo apt install python3 python3-pip
      ```
    - **Windows**: Download Python 3 from [python.org](https://www.python.org/).
- **Bash Shell**:
  - Required to run the Bash scripts.
  - Included by default on Linux and macOS.
  - On Windows, use WSL (Windows Subsystem for Linux) or Git Bash.

---

## How to Use

### Step 1: Download the Repository
Clone the repository or download the ZIP file containing all the scripts.

```bash
git clone https://github.com/yourusername/LunarPhaseEventsCalendarGenerator.git
cd LunarPhaseEventsCalendarGenerator
```

Alternatively, extract the ZIP file into a folder and navigate to it.

---

### Step 2: Run the Master Script
To automate the entire process (setup and generation):
```bash
./run.sh
```

The `run.sh` script will:
1. Prepare the Python environment by running `setup_env.sh`.
2. Generate ICS files for the next 25 years by running `generate_calendars.sh`.

---

### Step 3: Check the Output
- Generated `.ics` files will be in the `output` directory.
- Logs for errors or additional information will be in `output/logs.txt`.

---

## Manual Usage

### Setting Up the Environment
If you want to prepare the environment manually:
1. Run the `setup_env.sh` script:
   ```bash
   ./setup_env.sh
   ```

2. Activate the virtual environment:
   ```bash
   source myenv/bin/activate  # On Linux/macOS
   myenv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Generating ICS Files for a Specific Year
To generate a calendar for a specific year:
```bash
python3 LunarPhaseEventsCalendarGenerator.py --year 2025
```

---

### Automating 25 Years of Calendars
Run the `generate_calendars.sh` script to generate ICS files for the next 25 years:
```bash
./generate_calendars.sh
```

---

## Troubleshooting

### Common Issues
1. **Command Not Found**:
   - Ensure you’re using `python3` instead of `python`.
   - Verify that Bash is available on your system.

2. **Permission Denied**:
   - Make scripts executable:
     ```bash
     chmod +x *.sh
     ```
   - Re-run the script with elevated privileges:
     ```bash
     sudo ./run.sh
     ```

3. **Python Dependencies Not Installed**:
   - Ensure `setup_env.sh` was run successfully and the environment is activated.

4. **Missing `.ics` Files**:
   - Check the log file:
     ```bash
     cat output/logs.txt
     ```

---

## Notes
- **Re-running Scripts**:
  - If the environment is already set up, you can skip `setup_env.sh` and directly run:
    ```bash
    ./generate_calendars.sh
    ```

- **Cleaning Up**:
  - To reset and remove the virtual environment:
    ```bash
    rm -rf myenv
    ```

---

## Example Workflow
1. Download the repository or extract the ZIP.
2. Navigate to the directory:
   ```bash
   cd LunarPhaseEventsCalendarGenerator
   ```
3. Run the master script:
   ```bash
   ./run.sh
   ```
4. Check the `output` directory for generated `.ics` files.

---

Enjoy your lunar phase calendars! 🌑🌓🌕🌗
