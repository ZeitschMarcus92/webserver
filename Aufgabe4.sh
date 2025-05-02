#!/bin/bash

# Webserver-Verzeichnis
VERZEICHNIS="/var/www/html"

# Zähler für gefundene HTML-Dateien
gefunden=0

# Ausgabe
echo "Suche nach HTML-Dateien in $VERZEICHNIS ..."

# Durch alle Dateien im Verzeichnis loopen
for datei in "$VERZEICHNIS"/*; do
    if [[ -f "$datei" && "$datei" =~ \.html$ ]]; then
        echo "Gefunden: $(basename "$datei")"
        gefunden=$((gefunden + 1))
    fi
done

# Prüfen, ob etwas gefunden wurde
if [[ $gefunden -eq 0 ]]; then
    echo "Keine HTML-Dateien gefunden."
else
    echo "$gefunden HTML-Datei(en) gefunden."
fi