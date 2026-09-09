import re
from collections import Counter
from pathlib import Path

# Path to sample authentication log
LOG_FILE = Path(__file__).parent / "logs" / "sample_auth.log"

# Number of failed attempts required to trigger an alert
THRESHOLD = 3

failed_attempts = Counter()

# Detect failed SSH login attempts and extract source IP
pattern = re.compile(
    r"Failed password .* from (\d+\.\d+\.\d+\.\d+)"
)

print("\n=== SOC SSH Brute-Force Detection ===")

try:
    with open(LOG_FILE, "r", errors="ignore") as log:

        for line in log:
            match = pattern.search(line)

            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1

    if not failed_attempts:
        print("No failed SSH login attempts detected.")

    else:
        for ip, count in failed_attempts.items():

            print(f"\nSource IP : {ip}")
            print(f"Attempts  : {count}")

            if count >= THRESHOLD:
                print("ALERT     : Possible SSH Brute-Force")
                print("Severity  : HIGH")
            else:
                print("Status    : Below Detection Threshold")

except FileNotFoundError:
    print(f"ERROR: Log file not found: {LOG_FILE}")

except PermissionError:
    print(f"ERROR: Permission denied: {LOG_FILE}")
