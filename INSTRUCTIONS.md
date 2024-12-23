# Instructions

## Step 1: Prepare Your Environment

### 1. Install the Required Software
- **Python 3.8 or newer**: [Download Python](https://www.python.org/downloads/) and install it. During installation, check the box that says "Add Python to PATH."
- **Bash Shell**:  
  - Linux/macOS: Already installed.  
  - Windows: Install [Git for Windows](https://gitforwindows.org/), which includes Git Bash.

### 2. Verify the Installation
Open a terminal (or Git Bash on Windows) and check the versions:
```bash
python3 --version
bash --version
```
If these commands fail, ensure the software is installed and properly added to the system PATH.

---

## Step 2: Download the Project

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

### 2. Generate Lunar Phase Calendars
To generate `.ics` files for a specific year range, provide optional arguments:
```bash
./run.sh 2024 2030
```
- If no arguments are provided, the default range is 2024–2048.

### 3. Check for Errors
- Logs are saved to `output/lunar_phase_generator_error.log` for troubleshooting.

---

## Step 4: Output Files

- Generated `.ics` files are saved in the `output/` directory.
- If no `.ics` files are generated, check the error log for details:
  ```bash
  output/lunar_phase_generator_error.log
  ```

---

## Notes

1. **Galactic Center Correction**:
   - The script enables Galactic Center correction by default. This is controlled by the internal `GALACTICCENTER` variable, which defaults to `on`.

2. **Dependencies**:
   - Ensure `requirements.txt` is present and contains the required Python libraries.

---

## Logs and Debugging

- Check `output/lunar_phase_generator_error.log` for errors.
- If `.ics` files are not generated, confirm that the Python script is running correctly and the ephemeris file (`de440s.bsp`) is downloaded successfully.

---

Follow these instructions carefully to set up and run the project.
