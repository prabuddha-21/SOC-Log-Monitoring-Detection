# SOC Log Monitoring & Detection System

A Python-based Security Operations Center (SOC) project that analyzes Linux authentication logs and detects potentially suspicious security activities using rule-based detection techniques.

The project simulates basic SOC monitoring workflows, including authentication log analysis, suspicious login detection, privileged activity monitoring, and severity-based alert generation.

## Project Overview

The system currently implements three detection modules:

- SSH brute-force detection
- Successful login following multiple failed authentication attempts
- Privileged `sudo` activity monitoring

The project is developed and tested on Ubuntu Linux using Python 3 and sample authentication log files.

## Technologies Used

- **Programming Language:** Python 3
- **Operating System:** Ubuntu Linux
- **Log Analysis:** Linux authentication logs
- **Python Libraries:** `re`, `collections.Counter`, `pathlib`
- **Development Tools:** Terminal, Git, GitHub, VMware

## Detection Modules

### 1. SSH Brute-Force Detection

**Script:** `ssh_detector.py`

Detects repeated failed SSH authentication attempts by extracting source IP addresses and counting failed login events.

**Detection logic:**
- Parses log entries using regular expressions.
- Extracts the source IP address from failed SSH login events.
- Counts failed attempts for each source IP.
- Generates a HIGH severity alert when the configured threshold is reached.

**Configured threshold:** 3 failed attempts.

### 2. Successful Login After Multiple Failures

**Script:** `login_after_fail.py`

Identifies potentially suspicious SSH authentication activity when a successful login follows multiple failed attempts.

**Detection logic:**
- Analyzes failed and successful authentication events.
- Correlates activity using the source IP address.
- Generates a HIGH severity alert when the implemented detection conditions are met.

This behavior may indicate a potential account compromise, but the alert alone does not confirm that an account was compromised.

### 3. Privileged Activity Monitoring

**Script:** `sudo_detector.py`

Analyzes supplied log data to identify privileged commands and generate monitoring alerts.

**Detection logic:**
- Identifies privileged activity in the available log data.
- Reports the associated username and command.
- Displays the privilege level and alert severity when available.
- Assigns MEDIUM severity to the detected activity.

Privileged commands can be legitimate administrative operations. Further investigation is required to determine whether an event is suspicious.

## Project Structure

```text
soc-project/
├── ssh_detector.py
├── login_after_fail.py
├── sudo_detector.py
├── README.md
├── .gitignore
└── logs/
    ├── sample_auth.log
    └── ssh_failed.log
```

## Requirements

- Ubuntu or another Linux distribution
- Python 3
- Sample log files included in the project

The current scripts use Python standard-library modules and do not require third-party Python packages for the functionality described here.

## Installation and Execution

### 1. Clone the repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone <YOUR_REPOSITORY_URL>
cd soc-project
```

Alternatively, download the project and open a terminal in its directory.

### 2. Verify Python

```bash
python3 --version
```

### 3. Run SSH brute-force detection

```bash
python3 ssh_detector.py
```

### 4. Run successful-login-after-failures detection

```bash
python3 login_after_fail.py
```

### 5. Run privileged activity monitoring

```bash
python3 sudo_detector.py
```

Each script can be executed independently from the project directory.

## Testing and Sample Results

The following results were observed when running the scripts against the supplied sample data.

### SSH Brute-Force Detection

```text
=== SOC SSH Brute-Force Detection ===

Source IP : 192.168.56.10
Attempts  : 5
ALERT     : Possible SSH Brute-Force
Severity  : HIGH
```

**Result:** Five failed SSH login attempts were counted from the same source IP, exceeding the configured threshold of three.

### Successful Login After Multiple Failures

```text
=== Successful Login After Failed Attempts Detection ===

ALERT: Successful Login After Multiple Failures
Source IP       : 192.168.56.10
Failed Attempts : 5
Severity        : HIGH
Possible Account Compromise
```

**Result:** The detector generated an alert for a successful login following multiple failed attempts, according to its implemented detection logic.

### Privileged Activity Monitoring

```text
=== SOC Privileged Activity Monitoring ===

PRIVILEGED ACTIVITY
User      : testuser
Command   : /usr/bin/whoami
Privilege : ROOT
Severity  : MEDIUM

PRIVILEGED ACTIVITY
User      : testuser
Command   : /usr/bin/ls /root
Privilege : ROOT
Severity  : MEDIUM
```

**Result:** Two privileged activity alerts were generated for the commands shown in the sample data.

These results demonstrate execution against sample data. They do not establish that the host experienced a real attack or that an account was compromised.

## Key Learning Outcomes

- Linux authentication log analysis
- Python-based security detection
- Regular expressions and log parsing
- Threshold-based alert generation
- SSH brute-force detection
- Authentication event correlation
- Privileged activity monitoring
- Basic SOC alert investigation workflows
- Linux command-line operations

## Current Limitations

- The scripts process supplied log files rather than continuously monitoring a live system.
- Detection accuracy depends on log format and the implemented rules.
- The authentication correlation logic requires further testing against different event sequences and timestamps.
- The current project does not provide centralized alert storage or a graphical dashboard.
- Alerts require analyst validation to distinguish suspicious activity from legitimate behavior.

## Future Improvements

- Add timestamps and unique IDs to generated alerts.
- Export alerts to structured JSON or CSV files.
- Implement automated test cases for normal and suspicious authentication patterns.
- Improve event correlation using usernames, source IP addresses, and timestamps.
- Add centralized reporting for all detection modules.
- Integrate with Splunk for SIEM-based searching, investigation, and dashboard visualization.

## Disclaimer

This project is intended for educational purposes and authorized security testing in a controlled lab environment. Detection results should be validated before making incident-response decisions.

## Author

**Prabuddha Shankarrao Firange**

Aspiring SOC Analyst | Cybersecurity & Network Security

GitHub: [prabuddha-21](https://github.com/prabuddha-21)
