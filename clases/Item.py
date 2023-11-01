class Item:
    def __init__(self, mana_cost, name, description, id):
        self.card_id = str(id)
        self.mana_cost = mana_cost
        self.name = name
        self.card_typ = "Item"
        self.description = description
        self.img_url = self.name + ".png"
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.card_id
        else:
            self.name_for_html = self.name + self.card_id

    def __str__(self):
        return f"MANA:{self.mana_cost} NAME:{self.name} {self.description}"
