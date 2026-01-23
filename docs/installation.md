# Installation Guide

This document explains how to install and run the Secwexen Toolkit on your system.

---

## Requirements

- Python 3.8+
- Git
- Bash (Linux/macOS) or PowerShell (Windows)
- Recommended: virtual environment for Python tools

---

## 1. Clone the Repository

```
git clone https://github.com/secwexen/secwexen-toolkit.git
```

---

## 2. Install Python Dependencies

If tools require Python packages in the future:

```
pip install -r requirements.txt
```

(Current version does not require external packages.)

---

## 3. Running Tools

### Offensive Tools
```
python tools/offensive/port_scanner.py
```

### Defensive Tools
```
python tools/defensive/log_monitor.py
```

### OSINT Tools
```
python tools/osint/username_checker.py
```

### Automation Scripts
```
bash tools/automation/cleanup_temp.sh
```

or on Windows:

```
powershell tools/automation/system_info.ps1
```

---

## 4. Running Tests

```
pytest tests/
```

---

## 5. Updating the Toolkit

```
git pull origin main
```

---

## Notes
This project is under active development. Some tools are placeholders and will be expanded in future releases.
