list_of_spells = ["Volley", "Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages"]
list_of_general_targets = {"Volley": 1}
list_of_self_target = ["Personal Guard", "Bandage", "Bandages"]
list_of_enemy_target = ["Kill"]
list_of_healing_spells = {"Bandage": 4, "Bandages": 99}
list_of_dmg_spells = ["Arrow shot"]
list_of_resetting_spells = ["Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages"]


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
            elif self.name in list_of_enemy_target:
                return "enemy"
        except Exception as e:
            print(e)
