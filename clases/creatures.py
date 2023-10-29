class Creature:
    def __init__(self, mana_cost, name, hp, attack, description, id):
        self.id = str(id)
        self.mana_cost = mana_cost
        self.name = name
        self.hp = hp
        self.attack = attack
        self.description = description
        self.exhausted = True

    def __str__(self):
        return f"MANA:{self.mana_cost} {self.name} HP:{self.hp} ATTACK:{self.attack} "
