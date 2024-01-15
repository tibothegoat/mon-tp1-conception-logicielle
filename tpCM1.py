from datetime import datetime

import pytz # $ pip install pytz


timezone_paris = pytz.timezone('Europe/Paris')

current_time = datetime.now(timezone)

current_time_formatted = current_time.strftime("%H:%M:%S")

print(current_time_formatted))

"""

import datetime

def main():
    # Obtenir l'heure actuelle
    heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")

    # Afficher l'heure dans la console
    print(f"Heure actuelle : {heure_actuelle}")

    # Écrire l'heure dans le fichier main.py
    with open("main.py", "w") as fichier:
        fichier.write(f"# Fichier généré automatiquement\n")
        fichier.write(f"# Heure actuelle : {heure_actuelle}\n")

if __name__ == "__main__":
    main()

"""
