list_of_spells = ["Volley", "Kill", "Arrow shot"]


class Spell:
    def __init__(self, mana_cost, name, description, id):
        self.id = str(id)
        self.mana_cost = mana_cost
        self.name = name
        self.description = description
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.id
        else:
            self.name_for_html = self.name + self.id

    def __str__(self):
        return f"MANA:{self.mana_cost} NAME:{self.name} {self.description}"

    def deal_dmg_to_target(self):
        if "damage" in self.description:
            for char in self.description:
                if char.isnumeric() is True:
                    return char
