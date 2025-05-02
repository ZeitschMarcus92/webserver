#!/bin/bash

# Apache Webserver installieren und starten
if [ -f /etc/debian_version ]; then
    sudo apt update && sudo apt install apache2 -y
    service_name="apache2"
elif [ -f /etc/redhat-release ]; then
    sudo yum install httpd -y
    service_name="httpd"
else
    echo "Nicht unterstütztes System." && exit 1
fi

# Webserver starten und aktivieren
sudo systemctl start $service_name
sudo systemctl enable $service_name

# Rechte auf Verzeichnisebene setzen (Suchrechte!)
sudo chmod +x /var
sudo chmod +x /var/www

# Webseite bereitstellen
sudo cp /mnt/c/Users/Marcus/Desktop/DevOps/Projekt1/index.html /var/www/html/
sudo cp /mnt/c/Users/Marcus/Desktop/DevOps/Projekt1/style.css /var/www/html/

# Eigentümer und Zugriffsrechte korrekt setzen
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html

# Erfolgsausgabe mit IP-Adresse
echo "Webserver läuft auf: http://$(hostname -I | awk '{print $1}')"
