# secwexen-arsenal  

![Build Status](https://img.shields.io/github/actions/workflow/status/secwexen/secwexen-arsenal/build.yml?label=Build)
![Lint](https://img.shields.io/github/actions/workflow/status/secwexen/secwexen-arsenal/lint.yml?label=Lint)
![Python Lint](https://img.shields.io/github/actions/workflow/status/secwexen/secwexen-arsenal/pylint.yml?label=PyLint)
![CodeQL](https://img.shields.io/github/actions/workflow/status/secwexen/secwexen-arsenal/codeql.yml?label=CodeQL)
![Release](https://img.shields.io/github/v/release/secwexen/secwexen-arsenal)
![License](https://img.shields.io/github/license/secwexen/secwexen-arsenal)
![Repo Size](https://img.shields.io/github/repo-size/secwexen/secwexen-arsenal)
![Last Commit](https://img.shields.io/github/last-commit/secwexen/secwexen-arsenal)
![Python Versions](https://img.shields.io/pypi/pyversions/secwexen-arsenal)
![Coverage](https://img.shields.io/codecov/c/github/secwexen/secwexen-arsenal)

**A curated collection of offensive, defensive, and automation tools developed for cybersecurity research, penetration testing, and threat analysis.**

This repository serves as a central hub for my custom-built security utilities, written in **Python**, **Rust**, **Bash**, and **PowerShell**.  
Each tool is designed for real-world workflows, focusing on efficiency, clarity, and practical use in controlled environments.

---

## Features 

- Offensive security scripts for recon, enumeration, and exploitation  
- Defensive utilities for log analysis, threat hunting, and incident response  
- OSINT automation tools for intelligence gathering  
- Rust-based CLI tools for performance-critical tasks  
- Python-based automation for SIEM, parsing, and data processing  
- Bash & PowerShell helpers for system diagnostics and workflow optimization  

---

## Technologies 

- **Python** — automation, parsing, threat intel  
- **Rust** — high-performance security tooling  
- **Bash** — Linux workflow automation  
- **PowerShell** — Windows diagnostics & IR  
- **Linux** — primary development environment  

---

## Project Structure

```
secwexen-arsenal
├── .github/                     
│
├── docs/                        # Project documentation
│   └── basic_usage.md           # Basic usage guide
│
├── examples/                    # Example and demo scripts
│   ├── defensive_demo.py
│   ├── offensive_demo.py
│   └── osint_demo.py
│
├── tests/                       # Test suite
│   ├── test_core.py
│   ├── test_tools.py
│   └── test_utils.py
│
├── tools/                       # Core security toolkit
│   │
│   ├── automation/              # Automation and DevOps scripts
│   │   ├── bash/
│   │   │   ├── auto_backup.sh
│   │   │   ├── cleanup.sh
│   │   │   └── deploy_script.sh
│   │   └── powershell/
│   │       ├── Auto-Deploy.ps1
│   │       ├── Backup-Files.ps1
│   │       └── Sync-Drives.ps1
│   │
│   ├── defensive/               # Defensive (Blue Team) tools
│   │   ├── bash/
│   │   ├── powershell/
│   │   │   ├── Check-DefenderStatus.ps1
│   │   │   ├── Get-EventLogs.ps1
│   │   │   └── Monitor-Processes.ps1
│   │   └── python/
│   │       ├── firewall_watcher.py
│   │       ├── log_monitor.py
│   │       └── malware_scanner.py
│   │
│   ├── offensive/               # Offensive (Red Team) tools
│   │   └── rust/
│   │       └── fast_port_scanner/
│   │           ├── Cargo.toml
│   │           └── src/
│   │               └── main.rs
│   │
│   └── osint/                   # OSINT tools
│       └── python/
│           ├── email_harvester.py
│           ├── subdomain_finder.py
│           └── username_lookup.py
│
├── utils/                       # Shared utility modules
│   ├── __init__.py
│   ├── file_ops.py              # File operations
│   ├── logger.py                # Logging utilities
│   └── validators.py            # Input validation helpers
│
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DISCLAIMER.md
├── LICENSE
├── Makefile                     
├── README.md                    
├── SECURITY.md                  
├── pyproject.toml               
└── requirements.txt             
```

---

## Ethical Use  

All tools in this repository are developed **strictly for educational and ethical purposes**.  
They are intended for use in:

- Controlled lab environments  
- Authorized penetration tests  
- Research and learning  

I do **not** endorse or support illegal activity of any kind.

---

## License  

This project is licensed under the **Apache-2.0 License**.  
See the [LICENSE](LICENSE) file for full details.

---

## Development Status

Secwexen Toolkit is under active development.  
Some files are placeholders and will be filled soon.  

---

## Author  

**Secwexen** – Cybersecurity & Ethical Hacker Expert   
**GitHub:** [github.com/secwexen](https://github.com/secwexen)  
