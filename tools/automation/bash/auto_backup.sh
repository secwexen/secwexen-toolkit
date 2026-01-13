#!/bin/bash

BACKUP_DIR="/var/backups/secwexen"
SOURCE_DIR="/opt/secwexen"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
ARCHIVE_NAME="backup_$TIMESTAMP.tar.gz"

echo "[+] Starting automated backup..."

# Create backup directory if missing
mkdir -p "$BACKUP_DIR"

# Create compressed archive
tar -czf "$BACKUP_DIR/$ARCHIVE_NAME" "$SOURCE_DIR"

if [ $? -eq 0 ]; then
    echo "[+] Backup completed successfully."
    echo "    File: $BACKUP_DIR/$ARCHIVE_NAME"
else
    echo "[!] Backup failed."
    exit 1
fi

# Optional: delete backups older than 7 days
find "$BACKUP_DIR" -type f -mtime +7 -exec rm -f {} \;

echo "[+] Old backups cleaned."
echo "[+] Backup process finished."
