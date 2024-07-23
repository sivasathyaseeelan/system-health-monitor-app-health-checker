import requests
import logging
from datetime import datetime

logging.basicConfig(filename='application_health.log', level=logging.INFO)

def check_application_health(url, acceptable_statuses=[200]):
    try:
        response = requests.get(url)
        if response.status_code in acceptable_statuses:
            status = 'up'
        else:
            status = 'down'
        log_status(url, status, response.status_code)
        return status
    except requests.exceptions.RequestException as e:
        log_status(url, 'down', None, str(e))
        return 'down'

def log_status(url, status, status_code=None, error=None):
    timestamp = datetime.now().isoformat()
    if error:
        logging.error(f"{timestamp} - {url} - {status} - Error: {error}")
    else:
        logging.info(f"{timestamp} - {url} - {status} - Status Code: {status_code}")

if __name__ == "__main__":
    url = "http://ab4cee4aa148440dc9f61bc8ce46bf27-238763611.ap-south-1.elb.amazonaws.com"  # Replace with the URL of your application
    status = check_application_health(url)
    print(f"The application is {status}.")
