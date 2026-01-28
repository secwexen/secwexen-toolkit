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
├── docs/                        # Project documentation
├── examples/                    # Example and demo scripts
├── tests/                       # Test suite
├── tools/                       # Core security toolkit
│   │
│   ├── automation/              # Automation and DevOps scripts
│   │   ├── bash/
│   │   └── powershell/
│   │
│   ├── defensive/               # Defensive (Blue Team) tools
│   │   ├── bash/
│   │   ├── powershell/
│   │   └── python/
│   │
│   ├── offensive/               # Offensive (Red Team) tools
│   │   └── rust/
│   │       └── fast_port_scanner/
│   │           └── src/
│   │
│   └── osint/                   # OSINT tools
│       └── python/
│
├── utils/                       # Shared utility modules
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

## Installation

### Requirements

- Python 3.9+
- Rust (cargo)
- Linux / Windows
- PowerShell 5+

### Setup

```bash
# 1. Clone repository
git clone https://github.com/secwexen/secwexen-arsenal.git
cd aappmart

# 2. (Optional but recommended) Create a virtual environment 
# Linux / macOS
python3 -m venv venv  
source venv/bin/activate  

# Windows (PowerShell)
python -m venv venv  
venv\Scripts\activate  

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Documentation

- Detailed usage guide: [basic_usage.md](docs/basic_usage.md)

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

Secwexen Arsenal is under active development.  
Some files are placeholders and will be filled soon. 

---

## Author  

**Secwexen** – Project Author & Maintainer   
**GitHub:** [github.com/secwexen](https://github.com/secwexen)  
