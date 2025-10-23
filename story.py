def first_encounter(player):
    print("\nUne silhouette encapuchonnée t'aborde.")
    print("1. L'aider")
    print("2. L'ignorer")
    print("3. La menacer")

    choice = input("> ")
    if choice == "1":
        print("La figure te remercie. Tu sens ton âme s'éclaircir.")
        player.madness = max(0, player.madness - 5)
        player.xp += 10
    elif choice == "2":
        print("Tu passes ton chemin, rien ne se passe.")
    else:
        print("Elle te maudit... ta tête bourdonne.")
        player.madness += 10

def villager_dialogue(player):
    print("\n Un villageois à moitié fou t'interpelle :")
    print("\"Ils viennent la nuit... Les ombres... Tu veut savoir ?\"")
    print("1. L'écouter")
    print("2. Le repousser")
    print("3. Le menacer")

    choice = input("> ")
    if choice == "1":
        print("Tu écoute avec empathie. Tu sens ton esprit s'apaiser.")
        player.path = "Clarté"
        player.add_xp(10)
        player.madness = max(0, player.madness - 5)
    elif choice == "2":
        print("Tu t'éloignes, son rire résonne dans ton dos...")
        player.path = "Neutre"
        player.madness += 3
    elif choice == "3":
        print("Il sort un couteau !")
        from combat import combat
        enemy = {"nom": "Villageois fou", "pv": 25, "attaque": 7, "defense": 1, "xp": 20, "gold": 3}
        combat(player, enemy)                  