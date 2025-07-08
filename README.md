# 🔐 Linux Log Analyzer (CentOS 7)

A simple Python 2.7 script that parses Linux SSH authentication logs from /var/log/secure, extracts failed login attempts, and generates a CSV report of suspicious IP addresses.

This tool was built on *CentOS 7* using *Python 2.7*, designed for system administrators and security students who want to analyze login failures.

---

## 📂 Features

- Parses /var/log/secure for:
  - Invalid users
  - Failed SSH login attempts
- Extracts:
  - Username
  - IP address
- Counts failed attempts per IP
- Generates CSV report:
  - failed_ssh_report_<timestamp>.csv

---

## 🛠 Requirements

- CentOS 7
- Python 2.7 (preinstalled)
- rsyslog enabled to generate /var/log/secure

---

## 🧪 Sample Run

```bash
$ sudo python analyser.py
Report saved to /home/<user>/log-analyser/reports/failed_ssh_report_2025-07-08_18-22.csv