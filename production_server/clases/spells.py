from decks.lists_of_cards import *


class Spell:
    def __init__(self, mana_cost, name, description, id):
        self.card_id = str(id)
        self.mana_cost = mana_cost
        self.original_mana_cost = mana_cost
        self.name = name
        self.card_type = "Spell"
        self.description = description
        self.img_url = self.name + ".png"
        self.target = self.target_options()
        self.empire_belonging = ""
        self.category = ""
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.card_id
        else:
            self.name_for_html = self.name + self.card_id

    def __str__(self):
        return f"MANA:{self.mana_cost} NAME:{self.name} {self.description}"

    def deal_dmg_to_target(self):
        if "damage" in self.description.lower():
            for char in self.description:
                if char.isnumeric() is True:
                    return char

    def heal_to_target(self):
        if "heal" in self.description.lower():
            for char in self.description:
                if char.isnumeric() is True:
                    return char
        return "99"

    def target_options(self):
        try:
            if self.name in list_of_self_target:
                return "self"
            elif self.name in list_of_dmg_spells:
                return "enemy"
        except Exception as e:
            print(e)

    def mana_cost_reduction(self, amount):
        if self.mana_cost - amount < 0:
            self.mana_cost = 0
        else:
            self.mana_cost -= amount
