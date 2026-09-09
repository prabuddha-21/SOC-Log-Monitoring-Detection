# SOC Log Monitoring & Detection System

A beginner-friendly Security Operations Center (SOC) project that analyzes Linux authentication logs using Python to detect suspicious security activities.

## Project Overview

This project simulates basic SOC monitoring by analyzing Linux authentication logs and generating security alerts for suspicious events.

The system currently detects:

- SSH brute-force attempts
- Successful login after multiple failed attempts
- Privileged `sudo` activity

## Detection Modules

### 1. SSH Brute-Force Detection

**File:** `ssh_detector.py`

Counts failed SSH login attempts from source IP addresses.

If the number of failed attempts reaches the configured threshold, the system generates a **HIGH severity** alert.

### 2. Successful Login After Multiple Failures

**File:** `login_after_fail.py`

Correlates failed and successful SSH authentication attempts.

A successful login after multiple failed attempts from the same IP is flagged as potentially suspicious.

### 3. Privileged Activity Monitoring

**File:** `sudo_detector.py`

Analyzes `sudo` activity and identifies commands executed with root privileges.

These events are classified as **MEDIUM severity** for monitoring purposes.

## Project Structure

```text
SOC-Log-Monitoring-Detection/
│
├── ssh_detector.py
├── login_after_fail.py
├── sudo_detector.py
├── .gitignore
│
└── logs/
    └── sample_auth.log
