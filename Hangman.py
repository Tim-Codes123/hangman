import random
import os

woerter = ["python", "programmieren", "computer", "tastatur", "monitor", "vscode", "anaconda", "github", "hangman", "galgenmaennchen"]

wort = random.choice(woerter)
versteckt = ["_"] * len(wort)
versuche = 6
geraten = []

# Galgen-Stufen (0-6 Fehler)
stages = [
    """
     _____
    |     |
          |
          |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
          |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
    |     |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
   /|     |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
   /|\\    |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
   /|\\    |
   /      |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
   /|\\    |
   / \\    |
          |
    =========
    """
]

print("🎯 HANGMAN DELUXE - Rette das Männchen!")
print("Du hast 6 Versuche um das Wort zu erraten.")

while versuche > 0 and "_" in versteckt:
    os.system('cls' if os.name == 'nt' else 'clear')    # Bildschirm Löschen

    print(stages[6 - versuche])   #Zeigt die aktuelle Galgen-Stufe an
    print("   " + " ".join(versteckt))
    print(f"   Noch {versuche} Versuche übrig.")
    print(f"   Schon geraten: {', '.join(geraten) if geraten else '-'}")
    print()

    buchstabe = input("Dein Buchstabe: ").lower()

    if len(buchstabe) != 1 or not buchstabe.isalpha():
        print("Bitte gib einen einzelnen Buchstaben ein.")
        continue
    
    if buchstabe in geraten:
        print("Diesen Buchstaben hast du schon geraten.")
        continue
    
    geraten.append(buchstabe)

    if buchstabe in wort:
        for i in range(len(wort)):
            if wort[i] == buchstabe:
                versteckt[i] = buchstabe
        print("✅ Richtig geraten!")
    else:
        versuche -= 1
        print ("❌ Falsch geraten!")

# Spielende
os.system('cls' if os.name == 'nt' else 'clear')
print(stages[6 - versuche])
if "_" not in versteckt:
    print("🎉🎉🎉 GEWONNEN! 🎉🎉🎉")
    print(f"Das Wort war: {wort.upper()}")
else:
    print("💀💀💀 VERLOREN 💀💀💀")
    print(F"Das Wort war: {wort.upper()}")

input("\nDrücke Enter zum Beenden...")