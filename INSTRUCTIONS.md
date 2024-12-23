# Instructions

This guide will help you set up, generate, and manage lunar phase calendars. It is designed for beginners, with clear explanations of each step.

---

## **Step 1: Prepare Your Environment**

### 1. Install the Required Software
   - **Python 3.8 or newer**: [Download Python](https://www.python.org/downloads/) and install it. During installation, check the box that says "Add Python to PATH."
   - **Bash Shell**:  
     - Linux/macOS: Already installed.  
     - Windows: Install [Git for Windows](https://gitforwindows.org/), which includes Git Bash.

### 2. Verify the Installation
   Open a terminal (or Git Bash on Windows) and check the versions:
   ```bash
   python --version
   bash --version
   ```
   If these commands fail, ensure the software is installed and properly added to the system PATH.

---

## **Step 2: Download the Project**

Clone the repository from GitHub:
   ```bash
   git clone <repository_url>
   cd lunarPhaseEventsCalendarGenerator
   ```
   Alternatively, download the project as a ZIP file from GitHub and extract it to a folder.

---

## **Step 3: Set Up the Environment**

1. Run the `run.sh` script:
   ```bash
   ./run.sh
   ```
   - This script will:
     - Create a virtual environment.
     - Install required dependencies.
     - Download ephemeris data (`de440s.bsp`) if not already present.
   - **Windows Users**: Run this command in Git Bash.

2. If you encounter "Permission Denied," make the script executable:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

---

## **Step 4: Generate Lunar Phase Calendars**

1. Generate `.ics` files for a specific year range:
   ```bash
   ./run.sh --start_year 2024 --end_year 2048
   ```
   - Default values: Start year = 2024, End year = 2048.
   - The generated `.ics` files will be saved in the `output/` directory.

2. To disable Galactic Center correction, use:
   ```bash
   ./run.sh --disable_ayanamsa
   ```

---

## **Step 5: Merge `.ics` Files**

1. Run the merge script to combine all `.ics` files:
   ```bash
   ./run_merge.sh
   ```
   - The merged calendar will be saved as `output/merged_lunar_phases.ics`.

2. If you encounter "Permission Denied," make the script executable:
   ```bash
   chmod +x run_merge.sh
   ./run_merge.sh
   ```

---

## **Alternative: Run Python Scripts Manually**

### Generate Lunar Phase Calendars:
   ```bash
   python LunarPhaseEventsCalendarGenerator.py --start_year 2024 --end_year 2048
   ```

### Merge `.ics` Files:
   ```bash
   python merge_ics_files.py
   ```

---

## **Common Issues and Solutions**

1. **Permission Denied Errors**:  
   Make the `.sh` scripts executable:
   ```bash
   chmod +x run.sh
   chmod +x run_merge.sh
   ```

2. **Missing Ephemeris File**:  
   If `de440s.bsp` is missing, run `run.sh` to download it. Alternatively, download it manually from [NAIF Ephemeris Data](https://naif.jpl.nasa.gov/naif/data.html) and place it in the project directory.

3. **File Not Found**:  
   Ensure you're running the commands from the `lunarPhaseEventsCalendarGenerator` directory.

---

## **Logs and Debugging**

- Check the `output/lunar_phase_generator_error.log` file for error details.
- For merge errors, review `output/merge_ics_error.log`.

---

Congratulations! You’re now ready to generate and manage lunar phase calendars.
