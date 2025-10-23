import random
from combat import combat
from story import villager_dialogue

def forest(player):
    print("\n Tu entre dans la Forêt des Murmures.")
    event = random.choice(["combat", "treasure", "npc"])

    if event == "combat":
        enemy = {"nom": "Loup affamé", "pv": 30, "attaque": 8, "defense": 2, "xp": 10, "gold": 5}
        combat(player, enemy)
    elif event == "treasure":
        print("Tu trouve une potion et regagnes 20 PV !")
        player.hp += 20
    else:
        print("Un vieil ermite te donne un conseil mystérieux...")
        player.madness += 2  

def village(player):
    print("\n Tu arrives dans le Village Dévasté.")
    print("Des maisons calcinées, un silence lourd... mais une silhouette bouge.")
    villager_dialogue(player)
    # event aléatoire
    event = random.choice(["combat", "loot", "rien"])
    if event == "combat":
        enemy = {"nom": "Bandit masqué", "pv": 40, "attaque": 9, "defense": 3, "xp": 15, "gold": 10}
        combat(player, enemy)
    elif event == "loot":
        print("Tu trouve une bourse d'or ! (+15 or)")
        player.gold += 15
    else:
        print("Il ne se passe rien... le vent hurle entre les ruines.")                      