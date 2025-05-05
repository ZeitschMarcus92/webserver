# Aufgabe 3: Schleifen

# 1. for-Schleife: Zahlen von 1 bis 10
print("Zahlen von 1 bis 10:")
for i in range(1, 11):
    print(i)

# 2. while-Schleife: Zahl 5 solange Benutzer 'Ja' eingibt
antwort = input("Möchtest du die Zahl 5 sehen? (Ja/Nein): ")

while antwort.strip().lower() == "ja":
    print(5)
    antwort = input("Noch einmal? (Ja/Nein): ")

print("Programm beendet.")
