#!/bin/bash

# Variablen
GRUPPE="webgroup"
ADMIN="webadmin"
USER="webuser"
VERZEICHNIS="/var/www/html"

# Gruppe und Benutzer erstellen
sudo groupadd $GRUPPE
sudo useradd -m -G $GRUPPE $ADMIN
sudo useradd -m -G $GRUPPE $USER

# Eigentümer und Berechtigungen setzen
sudo chown -R $ADMIN:$GRUPPE $VERZEICHNIS
sudo chmod -R 754 $VERZEICHNIS

# Ausgabe
ls -ld $VERZEICHNIS
id $ADMIN
id $USER
getent group $GRUPPE 