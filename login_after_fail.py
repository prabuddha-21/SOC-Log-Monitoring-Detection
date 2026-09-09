import re
from collections import defaultdict
from pathlib import Path

# Path to sample authentication log
LOG_FILE = Path(__file__).parent / "logs" / "sample_auth.log"

# Number of failed attempts before considering a login suspicious
THRESHOLD = 3

failed_attempts = defaultdict(int)

# Detect failed SSH logins
failed_pattern = re.compile(
    r"Failed password .* from (\d+\.\d+\.\d+\.\d+)"
)

# Detect successful SSH logins
success_pattern = re.compile(
    r"Accepted password .* from (\d+\.\d+\.\d+\.\d+)"
)

print("\n=== Successful Login After Failed Attempts Detection ===")

try:
    with open(LOG_FILE, "r", errors="ignore") as log:

        for line in log:

            # Check for failed login
            failed_match = failed_pattern.search(line)

            if failed_match:
                ip = failed_match.group(1)
                failed_attempts[ip] += 1

            # Check for successful login
            success_match = success_pattern.search(line)

            if success_match:
                ip = success_match.group(1)

                if failed_attempts[ip] >= THRESHOLD:
                    print("\nALERT: Successful Login After Multiple Failures")
                    print(f"Source IP       : {ip}")
                    print(
                        f"Failed Attempts : "
                        f"{failed_attempts[ip]}"
                    )
                    print("Severity        : HIGH")
                    print("Possible Account Compromise")

                    # Reset counter after generating alert
                    failed_attempts[ip] = 0

except FileNotFoundError:
    print(f"ERROR: Log file not found: {LOG_FILE}")

except PermissionError:
    print(f"ERROR: Permission denied: {LOG_FILE}")
