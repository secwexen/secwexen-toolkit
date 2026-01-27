# Running the Tools

## Setup 

```bash
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

---

### OSINT Tools

```bash
python tools/osint/python/email_harvester.py
python tools/osint/python/subdomain_finder.py
python tools/osint/python/username_lookup.py
```

---

### Defensive Tools

```bash
python tools/defensive/python/firewall_watcher.py
python tools/defensive/python/log_monitor.py
python tools/defensive/python/malware_scanner.py
```

---

### Example Demos

```bash
python examples/osint_demo.py
python examples/defensive_demo.py
python examples/offensive_demo.py
```

---

## Bash Scripts (Linux / macOS)

Make scripts executable:

```bash
chmod +x tools/automation/bash/*.sh
```

Run:

```bash
./tools/automation/bash/auto_backup.sh
./tools/automation/bash/cleanup.sh
./tools/automation/bash/deploy_script.sh
```

---

## PowerShell Scripts (Windows)

Run PowerShell **as Administrator**.

Allow script execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Run scripts:

```powershell
.\tools\automation\powershell\Auto-Deploy.ps1
.\tools\automation\powershell\Backup-Files.ps1
.\tools\automation\powershell\Sync-Drives.ps1

.\tools\defensive\powershell\Check-DefenderStatus.ps1
.\tools\defensive\powershell\Get-EventLogs.ps1
.\tools\defensive\powershell\Monitor-Processes.ps1
```

---

## Rust Offensive Tool (Fast Port Scanner)

### Build

```bash
cd tools/offensive/rust/fast_port_scanner
cargo build --release
```

### Run

```bash
cargo run --release
```

Or run binary directly:

```bash
./target/release/fast_port_scanner
```

---

## Running Tests

```bash
pytest tests/
```

Or individually:

```bash
pytest tests/test_core.py
pytest tests/test_tools.py
pytest tests/test_utils.py
```

---

## Makefile  

```bash
make help
make install
make test
make run
```

---

## Notes

* Offensive tools must only be used in environments where you have explicit authorization.
* Some scripts may require **root / admin privileges**
* Defensive tools may need access to system logs or firewall APIs
