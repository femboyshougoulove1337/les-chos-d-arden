class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.xp = 0
        self.level = 1
        self.gold = 20
        self.madness = 0
        self.items = []
        self.skill_points = 0
        self.path = "Neutre" # "Chaos", "Clarté", ou "Neutre"
        self.skills = {
            "force_brutale": 0,
            "instinct": 0,
            "serenite": 0
        }

    def show_stats(self):
        print(f"\n=== {self.name} ===")
        print(f"PV : {self.hp}")
        print(f"Attaque : {self.attack}")
        print(f"Défense : {self.defense}")
        print(f"XP : {self.xp}")
        print(f"Niveau : {self.level}")
        print(f"Or : {self.gold}")
        print(f"Folie : {self.madness}")
        print(f"Objets : {self.items}")
        print(f"Voie: {self.path}")
        print(f"Points de compétence : {self.skill_points}")
        print(f"Compétences : {self.skills}")

    def add_xp(self, amount):
        self.xp += amount
        needed = self.level * 50
        if self.xp >= needed:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.skill_points += 1
        self.hp += 10
        print(f"\n Niveau {self.level} atteint ! Tu gagne 1 point de compétence.")