#!/bin/bash

# Ziel für das Backup
Ziel="/mnt/c/Users/Marcus/Desktop/DevOps/Projekt1/backups/webserver_backup"

# Zielverzeichnis sicherstellen
mkdir -p "$(dirname "$Ziel")"
rm -rf "$Ziel"
mkdir -p "$Ziel"

# Backup erstellen
if cp -r /var/www/html "$Ziel"; then
    echo "✅ Backup wurde erfolgreich erstellt."
else
    echo "❌ FEHLER: Backup konnte nicht erstellt werden!"
    exit 1
fi

echo "Cronjob wurde auf jede Minute gestellt zur Sicherheit!"
