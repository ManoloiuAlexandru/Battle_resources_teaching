class Defence:
    def __init__(self, mana_cost, name, number_of_troops, nr_of_assaults, description, id):
        self.card_id = str(id)
        self.number_of_troops = number_of_troops
        self.nr_of_assaults = nr_of_assaults
        self.mana_cost = mana_cost
        self.original_mana_cost = mana_cost
        self.name = name
        self.card_type = "Defence"
        self.description = description
        self.img_url = self.name + ".png"
        self.empire_belonging = ""
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.card_id
        else:
            self.name_for_html = self.name + self.card_id

    def __str__(self):
        return f"MANA:{self.mana_cost} NAME:{self.name} {self.description}"
