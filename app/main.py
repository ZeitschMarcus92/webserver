from utils import (                                           # Importiert die benötigten Funktion aus utils.py
   
    add_task,                                                 # Funktion zum Hinzufügen von Aufgaben
    show_tasks,                                               # - " -     zum Anzeigen von Aufgaben 
    change_status,                                            # - " -     zum ändern des Status von Aufgaben 
    save_to_excel,                                            # - " -     zum Speichern von Aufgaben in Excel
    load_from_csv,                                            # - " -     zum Laden von Aufgaben aus CSV 
    tasks                                                     # wichtig, um die Anzahl an Aufgaben zu prüfen
)

def menu():                                                  # Funktion für das Hauptmenu 
    load_from_csv()                                          # Lädt die Aufgaben aus der CSV-Datei 
    print(f"\n Es wurden {len(tasks)} Aufgaben geladen.\n")  # Gibt die Anzahl der geladenen Aufgaben an (falls vorhanden) 

    while True:                                              # Endlosschleife für das Hauptmenü   
        print("==== Task-Manager ====")
        print("[1] Aufgabe hinzufügen")
        print("[2] Aufgaben anzeigen")
        print("[3] Aufgabenstatus ändern")
        print("[4] Aufgaben als Excel speichern")
        print("[0] Beenden")

        choice = input("Was möchtest du tun? ")              # Eingabeaanfrage 

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            change_status()
        elif choice == "4":
            save_to_excel()
        elif choice == "0":
            if tasks:
                save_to_excel()
                print(" Aufgaben automatisch als Excel gespeichert (tasks.xlsx).")
            print("Auf Wiedersehen!")
            break                                           # Bei Eingabe 0 wird die Schleife beendet 
        else:
            print(" Ungültige Eingabe!\n")

if __name__ == "__main__":                                 # Kehrt nach der Ausführung des Skripts zurück und beendet das Programm
    menu()
