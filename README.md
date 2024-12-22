# Lunar Phase Events Calendar Generator
A script that produces an .ics file of Lunar Phases for any particular year (defaults to current year)

![Lunar Phase Events](./lunarPhaseEventsCalendarGenerator-small.png)

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

	•	If not installed:
	•	macOS: Install via Homebrew:

brew install python


	•	Linux: Install Python 3:

sudo apt update
sudo apt install python3 python3-pip


	•	Windows: Download Python 3 from the official website: https://www.python.org/.

Pip
	•	Ensure pip (Python’s package installer) is installed:

python3 -m ensurepip --upgrade



Git
	•	Install Git to clone the repository:

sudo apt install git  # On Linux
brew install git      # On macOS



Calendar Application
	•	Any calendar app that supports ICS files (e.g., Google Calendar, Apple Calendar).

Installation Guide

Step 1: Clone the Repository

git clone https://github.com/yourusername/LunarPhaseEventsCalendarGenerator.git
cd LunarPhaseEventsCalendarGenerator

Step 2: Set Up a Virtual Environment

python3 -m venv myenv
source myenv/bin/activate  # On Linux/macOS
myenv\Scripts\activate     # On Windows

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Verify Installation
	•	Test the script by running:

python3 LunarPhaseEventsCalendarGenerator.py --year 2025

Usage

Basic Usage
	•	Generate an ICS file for the current year:

python3 LunarPhaseEventsCalendarGenerator.py



Specify a Year
	•	Generate an ICS file for a specific year (e.g., 2025):

python3 LunarPhaseEventsCalendarGenerator.py --year 2025



Enable Verbose Mode
	•	Display detailed logs for debugging:

python3 LunarPhaseEventsCalendarGenerator.py --year 2025 --verbose

Output
	•	The ICS file is saved in the lunarPhases directory.
	•	Example: lunarPhases/lunar_phases_2025.ics.
	•	Import the file into your calendar application to view the lunar phases.

Troubleshooting

Common Issues
	•	Command Not Found:
	•	Ensure you’re using python3 instead of python.
	•	Verify that Python 3 is installed:

python3 --version


	•	Missing requests or ics Module:
	•	Install missing dependencies:

pip install -r requirements.txt


	•	Permission Denied:
	•	Run the command with elevated privileges:

sudo python3 LunarPhaseEventsCalendarGenerator.py


	•	ICS File Not Generated:
	•	Check the error.log file for details:

cat error.log



Advanced Debugging
	•	Enable verbose mode:

python3 LunarPhaseEventsCalendarGenerator.py --year 2025 --verbose


	•	Inspect raw API responses for unexpected formats.

Contributing

Contributions are welcome! To contribute:
	1.	Fork the repository.
	2.	Create a feature branch.
	3.	Submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Additional Notes

Virtual Environment Best Practices
	•	Always activate your virtual environment before running the script to ensure proper dependency management:

source myenv/bin/activate  # On Linux/macOS
myenv\Scripts\activate     # On Windows



Setting Up Python 3
	•	macOS: Install via Homebrew:

brew install python


	•	Linux:

sudo apt update
sudo apt install python3 python3-pip


	•	Windows: Download Python 3 from the official website: https://www.python.org/.

Example API Response and Script Behavior
	•	Sample API response:

[
  {
    "Error": 0,
    "ErrorMsg": "success",
    "TargetDate": "2025",
    "Moon": ["Moon before Yule"],
    "Index": 21,
    "Age": 22.231409255177535,
    "Phase": "3rd Quarter",
    "Distance": 391120.6,
    "Illumination": 0.49,
    "AngularDiameter": 0.5091988491989435,
    "DistanceToSun": 147099665.8828856,
    "SunAngularDiameter": 0.542184434133913
  }
]


	•	Resulting ICS file:

BEGIN:VEVENT
SUMMARY:🌗 3rd Quarter
DTSTART;VALUE=DATE:20250101
DTEND;VALUE=DATE:20250102
END:VEVENT

Credits

Special thanks to:
	•	FarmSense API for providing lunar phase data.
	•	Contributors and community feedback.

Enjoy your lunar phase calendar! 🌑🌓🌕🌗

---

### Next Steps
1. Copy and paste the above code into your `README.md`.
2. Replace `yourusername` with your actual GitHub username in the repository URL.
3. Test the steps in a clean environment to confirm accuracy.

Let me know if you'd like help setting up the GitHub repository! 🚀
