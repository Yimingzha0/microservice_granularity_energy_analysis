import csv
import re
import os
# This file is used to convert the Locust log processed_data to csv format and filter out the necessary information.
root_directory = '../train_system/results/fine/'
processed_directory = './train/fine/'

log_pattern = re.compile(
    r'\[(?P<timestamp>[\d\-:\s,]+)]\s+[^\]]+/INFO/locust:\s+(?P<status>SUCCESS|FAILURE):\s+(?P<method>\w+)\s+('
    r'?P<endpoint>[\S]+)\s+(?P<response_time>[\d.]+)ms\s+(?P<size>\d+)\s+bytes'
)
for subdir, _, files in os.walk(root_directory):
    for file in files:
        if file.endswith('.log'):
            log_filename = os.path.join(subdir, file)
            relative_path = os.path.relpath(subdir, root_directory)
            processed_subdir = os.path.join(processed_directory, relative_path)
            os.makedirs(processed_subdir, exist_ok=True)
            csv_filename = os.path.join(processed_subdir, file.replace('.log', '_requests.csv'))

            with open(log_filename, 'r') as file:
                log_lines = file.readlines()

            with open(csv_filename, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Timestamp', 'Method', 'Endpoint', 'Response Time (ms)', 'Size (bytes)'])
                for line in log_lines:
                    match = log_pattern.search(line)
                    if match:
                        timestamp = match.group('timestamp').strip()
                        method = match.group('method').strip()
                        endpoint = match.group('endpoint').strip()
                        response_time = match.group('response_time').strip()
                        size = match.group('size').strip()
                        csv_writer.writerow([timestamp, method, endpoint, response_time, size])

            print(f"Log data has been successfully converted to {csv_filename}")
