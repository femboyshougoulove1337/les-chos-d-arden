def show_skill_tree(player):
    print("\n Arbre de compétence :")
    print("1. Force brutale (+5 ATQ, +2 DEF)")
    print("2. Instinct (+3 ATQ, +10 Folie)")
    print("3. Sérénité (+15 PV, -5 Folie)")
    print("4. Retour")

    if player.skill_points <+ 0:
        print("Tu n'as pas de points disponibles.")
        return
    
    choice = input("> ")
    if choice == "1":
        player.attack += 5
        player.defense += 2
        player.skills["force_brutale"] += 1
    elif choice == "2":
        player.attack += 3
        player.madness += 10
        player.skills["instinct"] += 1
    elif choice == "3":
        player.hp += 15
        player.madness = max(0, player.madness - 5)
        player.skils["serenite"] += 1
    elif choice == "4":
        return
    else:
        print("Choix invalide.")

    player.skill_points -= 1
    print("Compétence améliorée !")                