#!/bin/bash

# Variablen
LOGDATEI="/var/log/webserver.log"
SERVICE="apache2"

# Log-Funktion
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | sudo tee -a "$LOGDATEI" > /dev/null
}

# Logdatei sicherstellen
sudo touch "$LOGDATEI"
sudo chmod 666 "$LOGDATEI"

log "Skript gestartet."

# Webserver starten
if sudo systemctl start "$SERVICE" && systemctl is-active --quiet "$SERVICE"; then
    log "Webserver ist aktiv."
else
    log "FEHLER: Webserver konnte nicht gestartet werden."
fi

# Datei kopieren
if [ -f /var/www/html/index.html ]; then
    cp /var/www/html/index.html /var/www/html/index_backup.html && \
    log "Datei kopiert: index.html -> index_backup.html" || \
    log "FEHLER beim Kopieren der Datei."
else
    log "index.html nicht gefunden – Kopie übersprungen."
fi

# Letzte 5 Logeinträge anzeigen
echo -e "\nLetzte 5 Log-Einträge:"
tail -n 5 "$LOGDATEI"
