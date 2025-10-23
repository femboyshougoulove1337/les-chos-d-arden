import time
from player import Player
from saves import save_game, load_game
from world import forest, village
from story import first_encounter

def slow_print(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.02)
    print()

def start_game():
    slow_print("Bienvenue dans les Echos d'Arden...")
    data = load_game()
    if data:
        player = Player(data["name"])
        player.hp = data["hp"]
        player.attack = data["attack"]
        player.defense = data["defense"] 
        player.xp = data["xp"]
        player.gold = data["gold"]
        player.madness = data["madness"]
        player.items = data["items"]
        print(" Partie chargée !")
    else:    
        name = input("Quel est ton nom, voyageur ?")
        player = Player(name)
        slow_print(f"{name}, tu te réveille dans une forêt obscure...")
        first_encounter(player)

    game_loop(player)

def game_loop(player):
    while True:
        print("\n=== Que veux-tu faire ? ===")
        print("1. Explorer la forêt")
        print("2. Aller au village")
        print("3. Voir mes stats")
        print("4. Sauvegarder et quitter")

        choix = input("> ")
        if choix == "1":
            forest(player)
        elif choix == "2":
            village(player)
            player.show_stats()
        elif choix == "3":
            player.show_stats()
        elif choix == "4":
            save_game(player)
            slow_print("Partie sauvegardée. À bientôt, aventurier...")
            break    
        else:
            print("Choix invalide.")        

def main_menu():
    while True:
        print("\n=== les Echos d'Arden ===")
        print("1. Nouvelle partie / Continuer")
        print("2. Quiter")
        choix = input("> ")

        if choix == "1":
            player = start_game()
        elif choix == "2":
            slow_print("À bientôt, voyageur...")
            break
        else:
            print("Choix invalide.")

main_menu()