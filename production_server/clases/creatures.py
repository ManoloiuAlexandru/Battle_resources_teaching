list_of_creature_description = ["Two-handed Knight", "Hospitaller Knight", "Priest"]
list_of_creature_that_deal_dmg_to_enemies = {"Two-handed Knight": 99}
list_of_creature_that_heal = {"Hospitaller Knight": 2, "Priest": 99}


class Creature:
    def __init__(self, mana_cost, name, hp, attack, description, id):
        self.card_id = str(id)
        self.mana_cost = mana_cost
        self.original_mana_cost = mana_cost
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.description = description
        self.card_type = "Creature"
        self.exhausted = self.charge_check()
        self.can_be_target = True
        self.img_url = self.name + ".png"
        self.items = []
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.card_id
        else:
            self.name_for_html = self.name + self.card_id

    def __str__(self):
        return f"MANA:{self.mana_cost} {self.name} HP:{self.hp} ATTACK:{self.attack} {self.description} "

    def charge_check(self):
        if self.description == "Charge":
            return False
        return True

    def check_creature(self):
        if self.mana_cost < 0:
            self.mana_cost = 0
        elif self.mana_cost >= 10:
            self.mana_cost = 10
        if self.attack < 0:
            self.attack = 0
        if self.hp <= 0:
            self.hp = 1
