list_of_creature_description = ["Two-handed Knight", "Hospitaller Knight", "Priest"]
list_of_creature_that_deal_dmg_to_enemies = {"Two-handed Knight": 99}
list_of_creature_that_heal = {"Hospitaller Knight": 2, "Priest": 99}
list_of_creature_with_on_going_effect = ["Frederick Barbarossa", "Richard the Lionheart"]
list_of_creature_with_negative_on_going_effect = ["Frederick Barbarossa"]
list_of_creature_with_positive_on_going_effect = ["Richard the Lionheart"]
list_of_creature_that_draw_cards = {"Page": 1}


class Creature:
    def __init__(self, mana_cost, name, hp, attack, description, id):
        self.card_id = str(id)
        self.mana_cost = mana_cost
        self.original_mana_cost = mana_cost
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.original_attack = attack
        self.active_effects = []
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
        if "Charge" in self.description.split():
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

    def negative_effects_from_creatures(self, card):
        if card.name == "Frederick Barbarossa":
            if card.name not in self.active_effects:
                self.active_effects.append(card.name)
                self.attack -= 1
                if self.attack < 0:
                    self.attack = 0

    def positive_effects_from_creatures(self, card):
        if card.name == "Richard the Lionheart":
            if card.name not in self.active_effects:
                self.active_effects.append(card.name)
                self.attack += 1
                self.hp += 1

    def reverse_effect_creature(self, card):
        try:
            if card.name == "Frederick Barbarossa" and card.name in self.active_effects:
                self.attack += 1
                self.active_effects.remove(card.name)
                if self.original_attack == 0:
                    self.attack = 0
            elif card.name == "Richard the Lionheart" and card.name in self.active_effects:
                self.attack -= 1
                self.hp -= 1
                self.active_effects.remove(card.name)
        except Exception as e:
            print(e)
