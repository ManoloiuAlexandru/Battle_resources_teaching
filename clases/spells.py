list_of_spells = ["Volley", "Kill", "Arrow shot", "Personal Guard"]
list_of_general_targets = ["Volley"]
list_of_self_target = ["Personal Guard"]
list_of_enemy_target = ["Kill"]


class Spell:
    def __init__(self, mana_cost, name, description, id):
        self.card_id = str(id)
        self.mana_cost = mana_cost
        self.name = name
        self.card_typ = "Spell"
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
        if "damage" in self.description:
            for char in self.description:
                if char.isnumeric() is True:
                    return char

    def target_options(self):
        try:
            if self.name in list_of_self_target:
                return "self"
            elif self.name in list_of_enemy_target:
                return "enemy"
        except Exception as e:
            print(e)
