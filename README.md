# Lunar Phase Events Calendar Generator
A script that produces an .ics file of Lunar Phases for any particular year (defaults to current year)

![Lunar Phase Events](./lunarPhaseEventsCalendarGenerator-small.png)

# Lunar Phase Events Calendar Generator

## Description
The **Lunar Phase Events Calendar Generator** is a Python script that creates an ICS calendar file containing lunar phases (e.g., Full Moon, New Moon) for a specified year. The script fetches data from a public API and generates events with moon emojis for visualization in popular calendar applications.

---

## Features
- Generates ICS files with lunar phases and corresponding emojis.
- Fetches lunar data dynamically from a public API.
- Handles errors gracefully with detailed logs.
- Compatible with calendar apps like Google Calendar and Apple Calendar.
- Easy to use, even for Python beginners.

---

## Prerequisites

### Python
- Requires Python 3.7 or later.
- Check if Python 3 is installed:
  ```bash
  python3 --version
  ```
- If not installed:
  - **macOS**: Install via Homebrew:
    ```bash
    brew install python
    ```
  - **Linux**: Install Python 3:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
  - **Windows**: Download Python 3 from the official website: [https://www.python.org/](https://www.python.org/).

### Pip
- Ensure `pip` (Python's package installer) is installed:
  ```bash
  python3 -m ensurepip --upgrade
  ```

### Git
- Install Git to clone the repository:
  ```bash
  sudo apt install git  # On Linux
  brew install git      # On macOS
  ```

### Calendar Application
- Any calendar app that supports ICS files (e.g., Google Calendar, Apple Calendar).

---

## Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/LunarPhaseEventsCalendarGenerator.git
cd LunarPhaseEventsCalendarGenerator
```

### Step 2: Set Up a Virtual Environment
```bash
python3 -m venv myenv
source myenv/bin/activate  # On Linux/macOS
myenv\Scripts\activate     # On Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
- Test the script by running:
  ```bash
  python3 LunarPhaseEventsCalendarGenerator.py --year 2025
  ```

---

## Usage

### Basic Usage
- Generate an ICS file for the current year:
  ```bash
  python3 LunarPhaseEventsCalendarGenerator.py
  ```

### Specify a Year
- Generate an ICS file for a specific year (e.g., 2025):
  ```bash
  python3 LunarPhaseEventsCalendarGenerator.py --year 2025
  ```

### Enable Verbose Mode
- Display detailed logs for debugging:
  ```bash
  python3 LunarPhaseEventsCalendarGenerator.py --year 2025 --verbose
  ```

---

## Output
- The ICS file is saved in the `lunar_phase_generator_output` directory.
- Example: `lunar_phase_generator_output/lunar_phases_2025.ics`.
- Error logs are saved as `lunar_phase_generator_output/lunar_phase_generator_error.log`.

---

## Troubleshooting

### Common Issues

- **Command Not Found**:
  - Ensure you're using `python3` instead of `python`.
  - Verify that Python 3 is installed:
    ```bash
    python3 --version
    ```

- **Missing `requests` or `ics` Module**:
  - Install missing dependencies:
    ```bash
    pip install -r requirements.txt
    ```

- **Permission Denied**:
  - Run the command with elevated privileges:
    ```bash
    sudo python3 LunarPhaseEventsCalendarGenerator.py
    ```

- **ICS File Not Generated**:
  - Check the `lunar_phase_generator_output/lunar_phase_generator_error.log` file for details:
    ```bash
    cat lunar_phase_generator_output/lunar_phase_generator_error.log
    ```

### Advanced Debugging
- Enable verbose mode:
  ```bash
  python3 LunarPhaseEventsCalendarGenerator.py --year 2025 --verbose
  ```
- Inspect raw API responses for unexpected formats.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Additional Notes

### Virtual Environment Best Practices
- Always activate your virtual environment before running the script to ensure proper dependency management:
  ```bash
  source myenv/bin/activate  # On Linux/macOS
  myenv\Scripts\activate     # On Windows
  ```

### Setting Up Python 3
- **macOS**: Install via Homebrew:
  ```bash
  brew install python
  ```
- **Linux**:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```
- **Windows**: Download Python 3 from the official website: [https://www.python.org/](https://www.python.org/).

---

Enjoy your lunar phase calendar! 🌑🌓🌕🌗
