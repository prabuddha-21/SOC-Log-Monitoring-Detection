import re
from pathlib import Path

# Path to sample authentication log
LOG_FILE = Path(__file__).parent / "logs" / "sample_auth.log"

# Detect sudo commands and the user executing them
pattern = re.compile(
    r"sudo: (\w+) : .*USER=root ; COMMAND=(.*)"
)

sudo_events = []

print("\n=== SOC Privileged Activity Monitoring ===")

try:
    with open(LOG_FILE, "r", errors="ignore") as log:

        for line in log:
            match = pattern.search(line)

            if match:
                user = match.group(1)
                command = match.group(2)

                sudo_events.append((user, command))

    if not sudo_events:
        print("No privileged activity detected.")

    else:
        # Display the latest 10 sudo events
        for user, command in sudo_events[-10:]:

            print("\nPRIVILEGED ACTIVITY")
            print(f"User      : {user}")
            print(f"Command   : {command}")
            print("Privilege : ROOT")
            print("Severity  : MEDIUM")

except FileNotFoundError:
    print(f"ERROR: Log file not found: {LOG_FILE}")

except PermissionError:
    print(f"ERROR: Permission denied: {LOG_FILE}")
