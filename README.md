# System Health Monitoring Script & Application Health Checker

## Requirements

- Python 3.6+
- `psutil` library

## Installation

1. **Clone the repository** (or download the script):
    ```bash
    git clone https://github.com/sivasathyaseeelan/system-health-monitor-app-health-checker.git
    cd system-health-monitor-app-health-checker
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

# System Health Monitoring Script

This project provides a script to monitor the health of a Linux system. The script checks CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds, the script sends an alert to the console and logs the alert to a log file.

## Features

- Monitors CPU usage
- Monitors memory usage
- Monitors disk space usage
- Lists running processes
- Logs alerts and information to both console and log file


## Usage

1. **Configure the script**:

    Open the `system_health_monitor.py` file and Set thresholds in percentage:

    ```python
    # Set thresholds in percentage
    CPU_THRESHOLD = 80
    MEMORY_THRESHOLD = 80
    DISK_THRESHOLD = 80
    ```

2. **Run the script**:

```bash
python system_health_monitor.py
```
The script will print the CPU usage, memory usage, disk space, and running processes and log the results to `system_health.log`.

# Application Health Checker

## Overview

The Application Health Checker is a Python script designed to monitor the uptime and health of web applications. It checks the availability of an application by sending HTTP requests and evaluating the response status codes. The script determines if the application is 'up' (functioning correctly) or 'down' (unavailable or not responding).

## Features

- Checks the health of a web application by making HTTP GET requests.
- Logs the status of the application to a file.
- Configurable to specify acceptable HTTP status codes.

## Usage

1. **Configure the script**:

    Open the `application_health_checker.py` file and set the URL of the application you want to monitor:

    ```python
    url = "http://example.com"  # Replace with the URL of your application
    ```

2. **Run the script**:

    ```bash
    python application_health_checker.py
    ```

    The script will print the status of the application and log the results to `application_health.log`.

## Configuration

- **`url`**: Update this variable in `application_health_checker.py` to point to the URL of the application you want to monitor.
- **`acceptable_statuses`**: Modify the `acceptable_statuses` list in the script if you want to allow different HTTP status codes for a healthy application.

## Logging

The script logs health check results to `application_health.log`. Logs include timestamps, URLs, status codes, and any errors encountered.
