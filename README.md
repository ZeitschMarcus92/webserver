# Projektbericht: Aufbau & Funktionen

Task-Management-System (CLI-basiert)Version: 0.1Archiv-Datei: Taskmanager
- (CLI steht für Command Line Interface    ( Kommandozeilen-Benutzeroberfläche))

# Funktionen im Überblick

# requirements.txt

Externe Bibliothek, die installiert werden muss:

pandas ( bedeutet quasi das Paket, was ohne das nicht funktionieren würde )

Wird mehr installiert als nötig dann : 

-  kann das zu Konflikten, längeren Installationszeiten oder unnötiger Komplexität führe und 

-  manche Pakete könnten veraltete oder inkompatible Versionen mitbringen.


# Hinweise

tasks.csv wird automatisch erstellt, sobald Aufgaben vorhanden sind

Daten bleiben auch nach dem Beenden des Programms erhalten


# 1. Einleitung

Dieses Projekt ist ein einfaches Aufgabenverwaltungsprogramm, das komplett über die Kommandozeile gesteuert wird. Es wurde in Python geschrieben und erlaubt das Erstellen, Anzeigen und Verwalten von Aufgaben – ganz ohne grafische Oberfläche.

Ziel war es, ein übersichtliches, funktionales und lokales lauffähiges Tool zu entwickeln, das auch für Einsteiger verständlich und erweiterbar ist ( mit Kommentaren dazu )

# 2. Was kann das Tool?

 Neue Aufgaben erfassen mit Titel, Beschreibung, Priorität, Fälligkeitsdatum und Status
 
 Aufgaben als Liste anzeigen
 
 Aufgabenstatus ändern (z.Bsp. von "Offen" zu "Erledigt")
 
 Automatische Speicherung als CSV-Datei
 
 Export der Daten als Excel-Datei
 
 Funktioniert komplett offline

# 3. Start & Installation

Voraussetzungen

Python ab Version 3.7

# Anleitung

- Projektordner öffnen 

Terminal oder Konsole öffnen

- cd /Pfad/zum/Projekt etc. ...

Abhängigkeiten installieren: wenn nötig

- pip install -r requirements.txt

Programm starten: nach Eingaben der Referenzen 

- python app/main.py

 Menü (nach dem Start) im Terminal ( POWERSHELL )

1. Aufgaben anzeigen
2. Neue Aufgabe hinzufügen
3. Status ändern
4. Als Excel speichern
0. Beenden

Eingaben erfolgen über einfache Nummern.

5. So funktioniert die Datenspeicherung

tasks.csv: Enthält alle Aufgaben im Klartext, gut lesbar mit Excel

tasks.xlsx: Optionaler Export für besseres Layout in Excel

Alle Daten bleiben auf deinem Computer – keine Cloud, keine Abhängigkeit.

6. Verzeichnisaufbau (von mir) :

/Projekt Python
│
├── app/
│   ├── __init__.py      # Leer, markiert das Verzeichnis als Python-Modul
│   ├── main.py          # Einstiegspunkt: Menü und Benutzerführung
│   └── utils.py         # Aufgabenfunktionen (Hinzufügen, Anzeigen, Status ändern, usw. ...)
│
├── tasks.csv            # CSV-Datei mit gespeicherten Aufgaben
├── tasks.xlsx           # Optionaler Excel-Export der Aufgaben
├── requirements.txt     # Enthält: pandas (Paket)
├── setup.py             # Paket-Setup für pip-Installation ( nicht zwingend )
└── README.md            # Projektdokumentation
