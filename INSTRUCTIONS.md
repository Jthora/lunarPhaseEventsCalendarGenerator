# Instructions for Using the Lunar Phase Events Calendar Generator

Follow these steps to set up and use the Lunar Phase Events Calendar Generator.

---

## **1. Prerequisites**
Ensure you have the following installed:
- Python 3.10+ with pip
- Git (for cloning the repository)

---

## **2. Setup**
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd lunar_phase_scripts
   ```

2. Set up the environment:
   ```bash
   ./setup_env.sh
   ```

   - This script creates a virtual environment, installs dependencies, and downloads the required Skyfield ephemeris data (`de440s.bsp`).

---

## **3. Running the Script**
To generate `.ics` files for 25 years:
```bash
./run.sh --timezone "America/New_York"
```

- The `--timezone` argument is optional; default is UTC.
- Replace `"America/New_York"` with your desired timezone (e.g., `"Europe/London"`).

---

## **4. Output**
- Generated `.ics` files will be saved in the `output/` directory.
- Each file corresponds to a year, named as `lunar_phases_<year>.ics`.

---

## **5. Example Calendar Entry**
**Summary**: `🌕 Full Moon (Wolf Moon)`  
**Description**:
```
The Full Moon occurs when the Moon is fully illuminated by the Sun, marking the midpoint of the lunar cycle.
This Full Moon is traditionally called the 'Wolf Moon' for the month of January.
Cultural Significance: Known for its role in agricultural and seasonal cycles.
Astrological Significance: A time of heightened emotions, clarity, and reflection.
```

---

## **6. Troubleshooting**
1. **Environment Issues**:
   - Ensure the virtual environment is activated:
     ```bash
     source myenv/bin/activate
     ```

2. **Dependency Issues**:
   - Manually install dependencies if required:
     ```bash
     pip install -r requirements.txt
     ```

3. **Log Files**:
   - Check `output/logs.txt` for details about any errors.
   - `lunar_phase_generator_error.log` contains critical error logs.

4. **Ephemeris File**:
   - Ensure the `de440s.bsp` file exists in the root directory. If not, re-run:
     ```bash
     ./setup_env.sh
     ```

---

## **7. Cleaning Up**
To clean up the environment:
- Deactivate the virtual environment:
  ```bash
  deactivate
  ```
- Remove the virtual environment directory:
  ```bash
  rm -rf myenv
  ```

---

## **8. Customization**
- Modify cultural moon names in the `CULTURAL_MOON_NAMES` dictionary inside `LunarPhaseEventsCalendarGenerator.py`.
- Adjust timezone via the `--timezone` option when running `./run.sh`.

---

## **9. Additional Resources**
- [Skyfield Documentation](https://rhodesmill.org/skyfield/)
- [List of Time Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

---

## **10. Support**
If you encounter issues, open an issue in the repository or contact the project maintainer.
