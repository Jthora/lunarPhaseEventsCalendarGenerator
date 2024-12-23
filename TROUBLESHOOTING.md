# Troubleshooting

## Common Issues

### 1. Missing Python Dependencies
   **Error**: `ModuleNotFoundError: No module named 'ics'`  
   **Solution**: Ensure you have run the setup script to install dependencies:
   ```bash
   ./run.sh
   ```

### 2. Ephemeris File Not Found
   **Error**: `FileNotFoundError: Ephemeris file 'de440s.bsp' not found.`  
   **Solution**: The setup script should automatically download the ephemeris data. If it fails, manually download it from [NAIF Ephemeris Data](https://naif.jpl.nasa.gov/naif/data.html) and place it in the repository directory.

### 3. Incorrect Timezone Handling
   **Error**: `Invalid timezone: <timezone>`  
   **Solution**: Ensure valid timezone strings are used. Default timezone is UTC.

### 4. Merge Script Fails
   **Error**: `No .ics files found in 'output/' directory.`  
   **Solution**: Verify `.ics` files exist in the `output/` directory before running `run_merge.sh`.

## Logging and Debugging
- Check the error log file for detailed information:
  ```bash
  output/lunar_phase_generator_error.log
  ```
