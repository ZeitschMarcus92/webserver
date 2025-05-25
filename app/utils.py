import pandas as pd                                                               # Importiert die Pandas-Bibliothek aus dem requirements.txt, die für die Datenanalyse und -manipulation verwendet wird
import os                                                                         # Importiert das OS-Modul für den Zugriff auf Betriebssystemfunktionen, die von der CSV-Datei benötigt werden

def input_with_choices(prompt, valid_options):                                    # (prompt ist die Eingabeaufforderung, valid_options sind die gültigen Optionen)
    while True:                                                                   # Schleife, die der Einagbeaufforderung folgt bis die Eingabe gültig ist 
        value = input(prompt).strip().capitalize()                                # strip() entfernt Leerzeichen am Anfang und Ende der Eingabe, capitalize() macht den ersten Buchstaben groß
        if value in valid_options:                                                # Überprüft, ob die Eingabe in den gültigen Optionen ist
            return value                                                          # Gibt die gültige Eingabe zurück
        print(f" Ungültige Eingabe. Bitte wähle: {', '.join(valid_options)}")     # Gibt eine Fehlermeldung aus, wenn die Eingabe ungültig ist und zeigt die gültigen Optionen an


tasks = []                                                                        # Initialisiert eine leere Liste für die Aufgaben
CSV_FILE = "tasks.csv"                                                            # Definiert den Dateinamen für die CSV

def load_from_csv():                                                               # definiert die Funktion zum Laden von Aufgaben aus der CSV-Datei
    global tasks                                                                   # Erlaubt den Zugriff auf die globale Variable tasks
    if os.path.exists(CSV_FILE):                                                   # Überprüft, ob die CSV-Datei existiert
        df = pd.read_csv(CSV_FILE)                                                 # Lädt die CSV-Datei in ein DataFrame
        tasks = df.to_dict(orient="records")                                       # Konvertiert das DataFrame in eine Liste von Dictionaries
        print(" Aufgaben aus 'tasks.csv' geladen.")                                # Gibt eine Bestätigung aus
    else:                                                                          # Wenn die CSV-Datei nicht existiert
        print("Noch keine gespeicherten Aufgaben gefunden.")                      # Gibt es eine Information aus

def save_to_csv():                                                                # definiert die Funktion zum Speichern von Aufgaben in die CSV-Datei
    if not tasks:                                                                 # Überprüft, ob die Liste der Aufgaben leer ist
        return
    df = pd.DataFrame(tasks)                                                      # pd.DataFrame() erstellt eine tabellenartige Datenstruktur, die du z. B. zum Speichern, Anzeigen oder Exportieren deiner Aufgabenliste verwendest
    df.to_csv(CSV_FILE, index=False)                                              # Speichert die Aufgaben in der CSV-Datei

def save_to_excel():                                                              # definiert die Funktion zum Speichern von Aufgaben in eine Excel-Datei
    if not tasks:
        print("Keine Aufgaben zum Speichern.")
        return
    df = pd.DataFrame(tasks)                                                      # Erstellt ein DataFrame aus der Liste der Aufgaben                                           
    df.to_excel("tasks.xlsx", index=False)
    print(" Aufgaben in 'tasks.xlsx' gespeichert.")


def add_task():                                                                    # definiert die Funktion zum Hinzufügen von Aufgaben
    print("\n Neue Aufgabe hinzufügen")
    title = input("Titel: ")
    description = input("Beschreibung: ")
    priority = input("Priorität (Hoch/Mittel/Niedrig): ")
    due_date = input("Fälligkeitsdatum (YYYY-MM-DD): ")
    status = input("Status (Offen/In Arbeit/Erledigt): ")
    if priority not in ["Hoch", "Mittel", "Niedrig"]:                               # Überprüft die Priorität
        print("Ungültige Priorität. Bitte Hoch, Mittel oder Niedrig eingeben.")     # Gibt eine Fehlermeldung aus
        return

    task = {                                                                        # Erstellt ein Dictionary für die Aufgabe (Dictionary ist eine Datentyp der Werte und Schlüssel in paare speichert)
        "title": title,
        "description": description,
        "priority": priority.capitalize(),                                          # capitalize() macht den ersten Buchstaben groß, falls nötig 
        "due_date": due_date,                                                       # Fälligkeitsdatum
        "status": status
    }

    tasks.append(task)                                                               # Fügt die Aufgabe zur Liste der Aufgaben hinzu
    save_to_csv()                                                                    # Automatisch speichern
    print(" Aufgabe hinzugefügt und gespeichert!\n")


def show_tasks():                                                                    # gibt die Funktion zum Anzeigen von Aufgaben an
    print("\n Deine Aufgaben:")
    if not tasks:
        print("Keine Aufgaben vorhanden.\n")
        return

    for i, task in enumerate(tasks, 1):                                                  # for (Start der Schleife ) i (Variable für die Aufgabe  z.bsp. tilte, usw.) enumerate() gibt den Index und das Element aus einer Liste (tasks 1 startet das Zählen bei 1 statt 0 )
        print(f"{i}. {task['title']} ({task['status']}) - Fällig: {task['due_date']} - Priorität: {task['priority']}") # Gibt die Aufgabe aus bzw. die Anzeige der Aufgaben 
    print("")


def change_status():                                                                  # gibt die Funktion zum Ändern des Status von Aufgaben an
    show_tasks()                                                                      # zeigt die Aufgaben an 
    if not tasks:
        return

    try:                                                                               # try bedeutet, dass der Code im try-Block ausgeführt wird, und wenn ein Fehler auftritt, wird der except-Block ausgeführt ( except-Block wird ausgeführt, wenn ein Fehler auftritt)
        number = int(input("Welche Aufgabe willst du ändern (Nummer)? "))              # Eingabeaufforderung für die Nummer der Aufgabe (int für gerade Zahlen bzw. Integer)(input ist ein String)
        if 1 <= number <= len(tasks):                                                  # Überprüft, ob die Nummer gültig ist
            new_status = input("Neuer Status (Offen/In Arbeit/Erledigt): ")            # Eingabeaufforderung für den neuen Status
            tasks[number - 1]["status"] = new_status                                   # Ändert den Status der Aufgabe
            save_to_csv() 
            print(" Status geändert und gespeichert!\n")
        else:
            print(" Ungültige Nummer.\n")                                              
    except ValueError:                                                                 # except ValueError bedeutet, dass ein Fehler aufgetreten ist, wenn der Benutzer eine ungültige Eingabe gemacht hat
        print(" Bitte gib eine gültige Zahl ein.\n") 
