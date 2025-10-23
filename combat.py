import random

def combat(player, enemy):
    print(f"Un {enemy['nom']} t'attaque !")

    while player.hp > 0 and enemy['pv'] > 0:
        print(f"\n{player.name} : {player.hp} PV")
        print(f"{enemy['nom']} : {enemy['pv']} PV")
        action = input("1. Attaquer | 2. Fuir > ")

        if action == "1":
            dmg = max(player.attack - enemy['defense'], 0)
            enemy['pv'] -= dmg
            print(f"Tu inflige {dmg} dégâts.")

            if enemy['pv'] <= 0:
                print(f"Tu as vaincu {enemy['nom']} !")
                player.xp += enemy['xp']
                player.gold += enemy['gold']
                if "folie" in enemy:
                    player.madness += enemy["folie"]
                break

        # tour de l'ennemi
            enemy_dmg = max(enemy['attaque'] - player.defense, 0)
            player.hp -= enemy_dmg
            print(f"{enemy['nom']} te frappe pour {enemy_dmg} dégâts.")
            
        else:
            print("Tu fuis le combat...")
            break       