list_of_item = ["Shield", "Knight's Equipment"]
list_of_good_items = ["Shield", "Knight's Equipment"]


class Item:
    def __init__(self, mana_cost, name, description, id):
        self.card_id = str(id)
        self.mana_cost = mana_cost
        self.original_mana_cost = mana_cost
        self.name = name
        self.card_type = "Item"
        self.description = description
        self.img_url = self.name + ".png"
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.card_id
        else:
            self.name_for_html = self.name + self.card_id

    def __str__(self):
        return f"MANA:{self.mana_cost} NAME:{self.name} {self.description}"

    def status_update(self, creature):
        if self.name in list_of_good_items:
            if "Guard" in self.description.split() and "Guard" not in creature.description.split():
                creature.description += " Guard"
            for hp in self.description.split("/")[1]:
                if hp.isnumeric():
                    creature.hp += int(hp)
                    creature.max_hp += int(hp)
            for attack in self.description.split("/")[0]:
                if attack.isnumeric():
                    creature.attack += int(attack)
