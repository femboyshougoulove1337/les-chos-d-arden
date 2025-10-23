import json
import os

SAVE_FILE = "data/saves.json"

def save_game(player):
    data = {
        "name": player.name,
        "hp": player.hp,
        "attack": player.attack,
        "defense": player.defense,
        "xp": player.xp,
        "gold": player.gold,
        "madness": player.madness,
        "items": player.items
    }
    # Crée le dossier datasi nécessaire
    os.makedirs("data", exist_ok=True)
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("Partie sauvegardé")

def load_game():
    if not os.path.exists(SAVE_FILE):
        print(" Aucune sauvegarde trouvée.")
        return None
    with open(SAVE_FILE, "r") as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError:
            print(" Fichier de sauvegarde corrompu.")
            return None