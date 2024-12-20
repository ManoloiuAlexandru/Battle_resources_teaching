from clases.spells import Spell

from clases.creatures import Creature

from clases.Defence import Defence


def save_your_deck(deck, empire):
    with open("my_deck.txt", "w") as file:
        file.write("empire:" + empire)
        file.write("\n")
        for card in deck:
            for card_attr, value in card.__dict__.items():
                file.write(card_attr + ":" + str(value))
                file.write("\n")
            file.write("--------------------------------")
            file.write("\n")


def get_old_deck():
    old_deck = []
    empire = ""
    file = open("my_deck.txt", "r")
    file_line = file.readline()

    while file_line:
        card_id = ""
        mana_cost = ""
        name = ""
        card_type = ""
        description = ""
        hp = ""
        attack = ""
        category = ""
        number_of_def = ""
        duration = ""
        file_line = file_line.strip()
        while file_line != "--------------------------------":
            if "empire" in file_line.split(":"):
                empire = file_line.split(":")[1]
            if "card_id" in file_line.split(":"):
                card_id = file_line.split(":")[1]
            elif "mana_cost" in file_line.split(":"):
                mana_cost = int(file_line.split(":")[1])
            elif "name" in file_line.split(":"):
                name = file_line.split(":")[1]
            elif "card_type" in file_line.split(":"):
                card_type = file_line.split(":")[1]
            elif "description" in file_line.split(":"):
                description = file_line.split(":")[1]
            elif "hp" in file_line.split(":"):
                hp = int(file_line.split(":")[1])
            elif "attack" in file_line.split(":"):
                attack = int(file_line.split(":")[1])
            elif "category" in file_line.split(":"):
                category = file_line.split(":")[1]
            elif "number_of_troops" in file_line.split(":"):
                number_of_def = int(file_line.split(":")[1])
            elif "nr_of_assaults" in file_line.split(":"):
                duration = int(file_line.split(":")[1])
            file_line = file.readline()
            file_line = file_line.strip()
        if card_type == "Spell":
            old_deck.append(Spell(mana_cost, name, description, card_id))
        elif card_type == "Creature":
            old_deck.append(Creature(mana_cost, name, hp, attack, description, category, card_id))
        elif card_type == "Defence":
            old_deck.append(Defence(mana_cost, name, number_of_def, duration, description, card_id))
        file_line = file.readline()
    return old_deck, empire


def return_list_of_filtered_library(library, filters):
    results = []
    for card in library:
        if card.mana_cost == filters["mana"] and filters["mana"] < 99:
            results.append(card)
        if filters["attrib"].lower() in card.description.lower() and card.card_type == "Creature" and filters[
            "attrib"] != "":
            results.append(card)
    return results
