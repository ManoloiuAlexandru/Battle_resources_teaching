from clases.creatures import Creature

"""
Creatures
"""
list_of_creature_description = ["Two-handed Knight", "Hospitaller Knight", "Priest", "Lumberjack", "Armorer"]
list_of_creature_that_deal_dmg_to_enemies = {"Two-handed Knight": 99}
list_of_creature_that_do_something_at_the_end_of_your_turn = {"Scribe": ("draw", 1), "Veteran": ("buff", 1, 1)}
list_of_creature_that_heal = {"Hospitaller Knight": 2, "Priest": 99}
list_of_creature_that_buff = {"Priest": (1, 1), "Lumberjack": (0, 1), "Armorer": (0, 0, "Armored")}
list_of_creature_with_on_going_effect = ["Frederick Barbarossa", "Richard the Lionheart"]
list_of_creature_with_negative_on_going_effect = ["Frederick Barbarossa"]
list_of_creature_with_positive_on_going_effect = ["Richard the Lionheart"]
list_of_creature_that_are_effected_by_action = {"Church Scholar": (1, 1, "", "heal")}
list_of_creature_that_draw_cards = {"Page": 1}
list_of_creature_that_add_mana = {"Farmer": 1}
list_of_creature_that_summon = {"Hunter": Creature(1, "Dog", 1, 1, "", len("hunter") + 11)}

"""
Spells
"""
list_of_spells = ["Volley", "Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages", "Horse riding lessons",
                  "Bodyguards", "Feudal Obligations", "Black Death", "Knight's training", "Peace Treaty",
                  "Wealthy Empire", "Ancient Empire", "Call of the Khan", "Call of the Emperor", "Arbalest Shot"]
list_of_self_target = {"Personal Guard": "Guard", "Bandage": "", "Bandages": "", "Horse riding lessons": "Charge",
                       "Knight's training": ""}
list_of_enemy_target = []
list_of_healing_spells = {"Bandage": 4, "Bandages": 99}
list_of_dmg_spells = {"Arrow shot": 2, "Black Death": 100, "Volley": 2, "Kill": 100, "Arbalest Shot": 3}
list_of_resetting_spells = ["Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages", "Horse riding lessons",
                            "Knight's training", "Arbalest Shot"]
list_of_spells_with_no_target = ["Bodyguards", "Feudal Obligations", "Black Death", "Volley", "Peace Treaty",
                                 "Wealthy Empire", "Ancient Empire", "Call of the Khan", "Call of the Emperor"]
list_of_spells_that_summon = {"Wealthy Empire": ("", 2), "Bodyguards": ("Guard", 2)}
list_of_spells_that_draw_cards = {"Feudal Obligations": 2, "Personal Guard": 1, "Ancient Empire": 2,
                                  "Call of the Khan": 1, "Call of the Emperor": 3, "Arbalest Shot": 1}
list_of_buff_spells = {"Bandage": (0, 0, ""), "Bandages": (0, 0, ""), "Horse riding lessons": (0, 2, "Charge"),
                       "Personal Guard": (0, 0, "Guard"),
                       "Knight's training": (3, 3, "")}
list_of_spells_that_reduce_mana = {"Call of the Khan": ("Charge", 100), "Call of the Emperor": ("", 1)}
