# Instructions

Follow these steps to generate and manage lunar phase calendars. These instructions are beginner-friendly, guiding you through every step in detail.

---

## **Step 1: Prepare Your Environment**

### 1. Install the Required Software
   You’ll need the following installed on your computer:
   - **Python 3.8 or newer**: [Download Python](https://www.python.org/downloads/) and install it. During installation, make sure to check the box that says "Add Python to PATH."
   - **Bash Shell**: If you're using Linux or macOS, Bash is pre-installed. If you're using Windows:
     - Install [Git for Windows](https://gitforwindows.org/). This includes Bash as part of the Git Bash tool.

### 2. Verify the Installation
   Open a terminal (or Git Bash on Windows) and type the following commands to ensure everything is set up:
   ```bash
   python --version
   ```
   This should display the Python version. If it doesn't, double-check that Python is installed correctly and added to your system PATH.

   For Bash, simply type:
   ```bash
   bash --version
   ```
   This should display the Bash version.

---

## **Step 2: Download the Project**

1. Clone this repository from GitHub:
   ```bash
   git clone <repository_url>
   cd lunarPhaseEventsCalendarGenerator
   ```
   - If you're unfamiliar with Git, you can download the project as a ZIP file from GitHub, then extract it to a folder on your computer.

---

## **Step 3: Install Python Dependencies**

1. Install the required Python libraries using the `requirements.txt` file:
   ```bash
   python -m pip install -r requirements.txt
   ```
   - This command downloads and installs all necessary libraries for the script to work.

   If you encounter any errors, ensure that `pip` (Python's package manager) is installed and updated:
   ```bash
   python -m ensurepip
   python -m pip install --upgrade pip
   ```

---

## **Step 4: Generate Lunar Phase Calendars**

### Generate `.ics` Files for a Specific Year Range:
1. Run the `run.sh` script to create `.ics` calendar files:
   ```bash
   ./run.sh --start_year 2024 --end_year 2048
   ```
   - **Windows Users**: Run this command in Git Bash, as `.sh` scripts may not work in Command Prompt or PowerShell.

2. Once completed, the `.ics` files will be saved in the `output/` directory.

---

## **Step 5: Merge `.ics` Files**

1. Combine all generated `.ics` files into a single calendar file:
   ```bash
   ./run_merge.sh
   ```
   - The merged file will be saved as `output/merged_lunar_phases.ics`.

---

## **Additional Options**

### Disable Ayanamsa Correction:
If you want to disable the ayanamsa correction for Galactic Center Sagittarius 0º:
   ```bash
   ./run.sh --disable_ayanamsa
   ```

### Run Scripts Manually:
If you prefer to run the Python scripts directly instead of using `.sh` files:
1. Generate `.ics` files:
   ```bash
   python LunarPhaseEventsCalendarGenerator.py --start_year 2024 --end_year 2048
   ```
2. Merge `.ics` files:
   ```bash
   python merge_ics_files.py
   ```

---

## **Common Issues for Beginners**

1. **Permission Denied Errors**:  
   If you see `Permission Denied` when trying to run `.sh` scripts, make them executable:
   ```bash
   chmod +x run.sh
   chmod +x run_merge.sh
   ```

2. **File Not Found Errors**:  
   Double-check that you're in the correct directory (`lunarPhaseEventsCalendarGenerator`).

3. **Can't Find Python or Bash**:  
   Ensure both are correctly installed and added to your PATH environment variable. Restart your computer if necessary.

---

Congratulations! You’re now ready to generate and manage lunar phase calendars.
