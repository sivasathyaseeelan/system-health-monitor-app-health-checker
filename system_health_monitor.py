import psutil
import logging
from datetime import datetime

# Set thresholds in percentage
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_and_print(message):
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_and_print(f"ALERT: CPU usage is above threshold! Current usage: {cpu_usage}%")
    else:
        log_and_print(f"CPU usage is normal. Current usage: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_and_print(f"ALERT: Memory usage is above threshold! Current usage: {memory_usage}%")
    else:
        log_and_print(f"Memory usage is normal. Current usage: {memory_usage}%")

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_and_print(f"ALERT: Disk usage is above threshold! Current usage: {disk_usage}%")
    else:
        log_and_print(f"Disk usage is normal. Current usage: {disk_usage}%")

def check_running_processes():
    processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'username', 'cpu_percent'])]
    log_and_print(f"Running processes: {processes}")

def main():
    log_and_print(f"System Health Monitoring started at {datetime.now()}")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    log_and_print(f"System Health Monitoring ended at {datetime.now()}")

if __name__ == "__main__":
    main()
