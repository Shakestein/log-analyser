import re
from collections import defaultdict
import csv
import os
from datetime import datetime

log_file_path = "/var/log/secure"  # CentOS uses /var/log/secure: Varies based on the type of Linux used.
pattern = re.compile(r"Failed password for(?: invalid user)? (\w+) from ([\d.]+)")

failed_logins = defaultdict(int)

with open(log_file_path, "r", encoding="utf-8", errors="ignore") as logfile:
    for line in logfile:
        match = pattern.search(line)
        if match:
            username, ip = match.groups()
            failed_logins[ip] += 1

# Timestamped output
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
output_dir = os.path.join(os.path.expanduser("~"), "log-analyzer", "reports")
output_file = os.path.join(output_dir, f"failed_ssh_report_{timestamp}.csv")

with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP Address", "Failed Attempts"])
    for ip, count in sorted(failed_logins.items(), key=lambda x: -x[1]):
        writer.writerow([ip, count])

print(f"Report saved to {output_file}")