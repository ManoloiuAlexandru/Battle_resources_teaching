list_of_creature_description = ["Two-handed Knight"]


class Creature:
    def __init__(self, mana_cost, name, hp, attack, description, id):
        self.id = str(id)
        self.mana_cost = mana_cost
        self.name = name
        self.hp = hp
        self.attack = attack
        self.description = description
        self.exhausted = self.charge_check()
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.id
        else:
            self.name_for_html = self.name + self.id

    def __str__(self):
        return f"MANA:{self.mana_cost} {self.name} HP:{self.hp} ATTACK:{self.attack} {self.description} "

    def charge_check(self):
        if self.description == "Charge":
            return False
        return True
