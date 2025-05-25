from setuptools import setup, find_packages                                                     # Importiert die benötigten Modulde von Setuptools (z.Bsp. main, utils)

setup(
    name="taskmanager",                                                                         # Name des Projekts
    version="0.1",                                                                              # Version des Projekts (Bsp.)
    description="Ein einfaches CLI-basiertes Task-Management-System",                           # Beschreibung 
    author="ZeitschMarcus92",                                                                   # z.Bsp. Github-Username
    packages=find_packages(where="app"),                                                        # Sucht nach Pakten im app-Ordner
    package_dir={"": "app"},                                                                    # Sucht alle Pakte im app-Ordner
    install_requires=[                                                                          # Installiert automatisch die notwendigen Pakete mit 
        "pandas"                                                                                # Panddas ist eine Bibliothek für Datenanalyse und -manipulation 
    ],
    entry_points={                                                                              # Definiert die Einstiegspunkte für das Projekt z.Bsp Konsolenbefehl ( taskmanager )
        "console_scripts": [                                                                    # Definiert die Kosolenbefehle
            "taskmanager=main:menu"                                                             # Definiert den Konsolenbefehl und die Funktion, die aufgerufen wird
        ]
    },
    python_requires=">=3.7",                                                                    # Mindestversion von Python, die benötigt wird zur Kompatilität bzw. der Version / Durchführung 
)

# das setup.py ist nicht zwingend notwendig, ist aber Sinnvoll wenn man z.Bsp. das Projekt auf PyPi veröffentlichen,installieren oder strukturierte Paketverwaltung machen möchte 