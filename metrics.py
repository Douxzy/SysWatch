# Import necessary modules
import time  # Provides time-related functions
from prometheus_client import start_http_server, Gauge  # Prometheus client library for exposing metrics
import psutil  # Library for retrieving system information (e.g., CPU, memory, disk usage)

# Define Prometheus metrics for system monitoring
cpu_usage = Gauge('cpu_usage_percent', 'CPU usage percentage', ['cpu'])  # CPU usage metric labeled by individual CPUs
mem_usage = Gauge('memory_usage_percent', 'Memory usage percentage')  # Overall memory usage metric
disk_usage = Gauge('disk_usage_percent', 'Disk usage percentage', ['mountpoint'])  # Disk usage metric labeled by mountpoints

def record_metrics():
    """
    Collect and record system metrics.

    This function gathers the following system metrics:
    
    - **CPU usage** for each core (in percentage).
    - **Memory usage** (overall, in percentage).
    - **Disk usage** (for the root directory, in percentage).

    Each metric is updated in Prometheus to be accessible for monitoring.

    :return: None
    """
    # Collect CPU usage for each core and update the Prometheus metric
    cpu_stats = psutil.cpu_percent(interval=1, percpu=True)
    for i, perc in enumerate(cpu_stats):  # Loop through each CPU core
        cpu_usage.labels(cpu=f"cpu{i}").set(perc)  # Update metric with percentage usage

    # Collect memory usage and update the Prometheus metric
    mem = psutil.virtual_memory()
    mem_usage.set(mem.percent)  # Update metric with memory usage percentage

    # Collect disk usage for the root directory and update the Prometheus metric
    disk_stats = psutil.disk_usage('/')
    disk_usage.labels(mountpoint='/').set(disk_stats.percent)  # Update metric with disk usage percentage

def expose_metrics():
    """
    Expose system metrics through an HTTP server.

    This function:
    - Starts an HTTP server at port 8080 to expose the metrics at the `/metrics` endpoint.
    - Periodically collects and updates system metrics every 5 seconds.

    :return: None
    """
    # Start the HTTP server to expose metrics at port 8080
    start_http_server(8080)

    # Continuously collect and update metrics
    while True:
        record_metrics()  # Record the latest system metrics
        time.sleep(5)  # Wait for 5 seconds before collecting metrics again

if __name__ == "__main__":
    """
    Entry point of the script.

    When this script is run, it will start exposing metrics at port 8080 and
    continuously update them.
    """
    expose_metrics()
