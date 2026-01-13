#!/bin/bash

echo "[+] Starting system cleanup..."

# Remove Python cache files
echo "[+] Removing __pycache__ directories..."
find . -type d -name "__pycache__" -exec rm -rf {} +

# Remove temporary files
echo "[+] Removing temporary files..."
find . -type f -name "*.tmp" -delete

# Remove log files older than 10 days
echo "[+] Cleaning old logs..."
find /var/log -type f -mtime +10 -exec rm -f {} \;

# Clear system cache (Linux only)
if command -v sync >/dev/null 2>&1; then
    echo "[+] Clearing system cache..."
    sync; echo 3 > /proc/sys/vm/drop_caches 2>/dev/null
fi

echo "[+] Cleanup completed successfully."
