#!/bin/bash

# ==========================================
#  Secwexen - File Integrity Checker (Linux)
#  Compares current file hashes with a stored
#  baseline to detect tampering or corruption.
# ==========================================

TARGET_DIR="/opt/secwexen"
HASH_DB="/var/secwexen/hash_db.txt"
LOG_FILE="/var/log/secwexen_integrity.log"

mkdir -p "$(dirname "$HASH_DB")"
mkdir -p "$(dirname "$LOG_FILE")"

log() {
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] $1" | tee -a "$LOG_FILE"
}

generate_hashes() {
    find "$TARGET_DIR" -type f -exec sha256sum {} \; | sort > "$HASH_DB"
}

log "[+] Starting integrity check..."
log "    Target directory: $TARGET_DIR"
log "    Hash database: $HASH_DB"

# If no baseline exists, create one
if [ ! -f "$HASH_DB" ]; then
    log "[!] No hash database found. Creating baseline..."
    generate_hashes
    log "[✓] Baseline created. Integrity check completed."
    exit 0
fi

# Generate current hash list
CURRENT_HASHES=$(mktemp)
find "$TARGET_DIR" -type f -exec sha256sum {} \; | sort > "$CURRENT_HASHES"

log "[+] Comparing current state with baseline..."

# Detect modified files
MODIFIED=$(comm -12 <(cut -d' ' -f3- "$HASH_DB") <(cut -d' ' -f3- "$CURRENT_HASHES") | while read file; do
    old_hash=$(grep " $file$" "$HASH_DB" | cut -d' ' -f1)
    new_hash=$(grep " $file$" "$CURRENT_HASHES" | cut -d' ' -f1)
    if [ "$old_hash" != "$new_hash" ]; then
        echo "$file"
    fi
done)

# Detect new files
NEW_FILES=$(comm -13 "$HASH_DB" "$CURRENT_HASHES" | cut -d' ' -f3-)

# Detect deleted files
DELETED_FILES=$(comm -23 "$HASH_DB" "$CURRENT_HASHES" | cut -d' ' -f3-)

# Report results
if [ -n "$MODIFIED" ]; then
    log "[!] Modified files detected:"
    echo "$MODIFIED" | while read f; do log "    ~ $f"; done
else
    log "[✓] No modified files."
fi

if [ -n "$NEW_FILES" ]; then
    log "[!] New files detected:"
    echo "$NEW_FILES" | while read f; do log "    + $f"; done
else
    log "[✓] No new files."
fi

if [ -n "$DELETED_FILES" ]; then
    log "[!] Deleted files detected:"
    echo "$DELETED_FILES" | while read f; do log "    - $f"; done
else
    log "[✓] No deleted files."
fi

log "[+] Integrity check completed."

rm "$CURRENT_HASHES"
