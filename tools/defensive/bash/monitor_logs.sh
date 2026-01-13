#!/bin/bash

# ==========================================
#  Secwexen - Log Monitoring Script (Linux)
#  Monitors system logs in real-time and
#  alerts on suspicious or critical events.
# ==========================================

LOG_FILE="/var/log/syslog"
ALERT_LOG="/var/log/secwexen_log_monitor.log"

mkdir -p "$(dirname "$ALERT_LOG")"

log_alert() {
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] $1" | tee -a "$ALERT_LOG"
}

if [ ! -f "$LOG_FILE" ]; then
    log_alert "[!] System log file not found: $LOG_FILE"
    exit 1
fi

log_alert "[+] Starting log monitor..."
log_alert "    Monitoring: $LOG_FILE"

# Keywords to watch for
KEYWORDS=(
    "failed"
    "unauthorized"
    "denied"
    "segfault"
    "panic"
    "error"
    "attack"
    "malware"
    "ssh"
)

# Build grep pattern
PATTERN=$(printf "|%s" "${KEYWORDS[@]}")
PATTERN=${PATTERN:1}

# Monitor logs in real-time
tail -Fn0 "$LOG_FILE" | while read line; do
    if echo "$line" | grep -Ei "$PATTERN" >/dev/null; then
        log_alert "[!] Suspicious event detected:"
        log_alert "    $line"
    fi
done
