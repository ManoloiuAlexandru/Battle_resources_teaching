import random

from clases.creatures import Creature


def generate_random_int():
    return random.randint(1, 1000000)


"""
Creatures
"""
list_of_creature_description = ["Two-handed Knight", "Hospitaller Knight", "Priest", "Lumberjack", "Armorer", "Archer",
                                "Personal instructor", "Scared Noble", "Bishop", "Protokentarchos"]
list_of_creature_that_deal_dmg_to_enemies = {"Two-handed Knight": 99, "Archer": 1}
list_of_creature_that_deal_dmg_to_players = {"Archer": 1}
list_of_creature_that_do_something_at_the_end_of_your_turn = {"Scribe": ("draw", 1), "Miner": ("draw", 1)}
list_of_creature_that_heal = {"Hospitaller Knight": 2, "Priest": 99}
list_of_creature_that_buff = {"Priest": (1, 1), "Lumberjack": (0, 1), "Armorer": (0, 0, "Armored"),
                              "Scared Noble": (0, 0, "Guard"), "Personal instructor": (1, 1),
                              "Watchtower": (2, 1, ""), "Drummer": (1, 1, ""), "Negotiator": (1, 1, ""),
                              "Last Defender": (0, 2, "Guard"), "Frederick Barbarossa": (1, 1, "Armored"),
                              "Bishop": (5, 5, "Guard"), "Protokentarchos": (3, 3, "")}
list_of_creature_that_buff_specific_cards = {"Frederick Barbarossa": ("Armored", 1, 1, "Armored")}
list_of_creature_with_on_going_effect = ["War elephant", "Army Champion"]
list_of_creature_with_negative_on_going_effect = {}
list_of_creature_with_positive_on_going_effect = {"Army Champion": (1, 1), "War elephant": (0, 1)}
list_of_creature_that_are_effected_by_action = {"Church Scholar": (1, 1, "", "heal")}
list_of_creature_that_draw_cards = {"Page": 1, "Wild Horse": 1, "Watchman": 1, "Negotiator": 1,
                                    "Richard the Lionheart": 2, "Scribe of the Church": 1}
list_of_creature_that_draw_specific_cards = {"Wild Horse": (["Creature"], ["Charge"]),
                                             "Scribe of the Church": (["Spell"], [""]),
                                             "Watchman": (["Creature"], ["Guard"]),
                                             "Richard the Lionheart": (
                                                 ["Creature", "Spell"], ["", ""])}
list_of_creature_that_add_mana = {"Farmer": 1}
list_of_creature_that_summon = {
    "Hunter": (1, [Creature(1, "Dog", 1, 1, "", generate_random_int()) for i in range(0, 4)])}
list_of_creature_that_are_affected_by_hand = {"Last Defender": ("empty hand", "buff"),
                                              "Drummer": ("affects hand", "buff", 1, 1, ""),
                                              "Negotiator": ("affects hand", "buff", 1, 1, ""),
                                              }
list_of_creature_that_summ_after_they_die = {
    "Lost Noble": (1, [Creature(4, "City Guard", 5, 3, "Guard", generate_random_int()) for i in range(0, 5)]),
    "Lost Sheep": (2, [Creature(1, "Wild Wolf", 1, 1, "", generate_random_int()) for i in range(0, 5)])}
list_of_creature_that_affect_all = {"Watchtower": "Guard"}
list_of_creature_that_affect_battle_field = {"Frederick Barbarossa": "Armored"}
list_of_creature_that_are_affected_in_hand = {"Trebuchet": ("reduce", "", 1)}
list_of_creature_that_do_somthing_when_die = {"Lost Sheep": "summ", "Lost Scribe": "draw", "Lost Shield": "draw",
                                              "Lost Noble": "summ"}
list_of_creature_that_draw_cards_when_die = {"Lost Scribe": 1, "Lost Shield": 1}
list_of_creature_that_draw_specific_cards_when_die = {"Lost Shield": (["Creature"], ["Guard"])}
"""
Spells
"""
list_of_spells = ["Volley", "Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages", "Horse riding lessons",
                  "Bodyguards", "Feudal Obligations", "Black Death", "Knight's training", "Peace Treaty",
                  "Wealthy Empire", "Ancient Empire", "Call of the Khan", "Call of the Emperor", "Arbalest Shot",
                  "Chivalry and Honor", "Horse raiding shot", "Landslide", "Rain of Arrows", "Roman Formation Circular",
                  "Guard Duty", "For the Khan", "Boarder Guards", "In the name of the king", "Roman Formation Phalanx",
                  "Old Tactics", "Pilum Throw", "Fast Conscription"]
list_of_self_target = {"Personal Guard": "Guard", "Bandage": "", "Bandages": "", "Horse riding lessons": "Charge",
                       "Knight's training": "", "Chivalry and Honor": "", "Guard Duty": "", "For the Khan": "Charge"}
list_of_healing_spells = {"Bandage": 4, "Bandages": 99}
list_of_dmg_spells = {"Arrow shot": 2, "Black Death": 100, "Volley": 2, "Kill": 100, "Arbalest Shot": 3,
                      "Horse raiding shot": 2, "Landslide": 7, "Rain of Arrows": 100, "Pilum Throw": 3}
list_of_resetting_spells = ["Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages", "Horse riding lessons",
                            "Knight's training", "Arbalest Shot", "Chivalry and Honor", "Pilum Throw"]
list_of_spells_with_no_target = ["Bodyguards", "Feudal Obligations", "Black Death", "Volley", "Peace Treaty",
                                 "Wealthy Empire", "Ancient Empire", "Call of the Khan", "Call of the Emperor",
                                 "Landslide", "Rain of Arrows", "Roman Formation Circular", "For the Khan",
                                 "Boarder Guards", "In the name of the king", "Roman Formation Phalanx",
                                 "Old Tactics", "Fast Conscription"]
list_of_spells_that_summon = {"Wealthy Empire": ("", 2), "Bodyguards": ("Guard", 2), "Boarder Guards": ("", 0),
                              "Fast Conscription": ("", 0)}
list_of_spells_that_draw_cards = {"Feudal Obligations": 2, "Personal Guard": 1, "Ancient Empire": 2,
                                  "Call of the Khan": 1, "Call of the Emperor": 3, "Arbalest Shot": 1,
                                  "Chivalry and Honor": 1, "Horse raiding shot": 1, "Old Tactics": 1
                                  }
list_of_buff_spells = {"Bandage": (0, 0, ""), "Bandages": (0, 0, ""), "Horse riding lessons": (0, 2, "Charge"),
                       "Personal Guard": (0, 0, "Guard"),
                       "Roman Formation Circular": (0, 0, "Guard"),
                       "Knight's training": (3, 3, ""), "Chivalry and Honor": (1, 2, ""), "Guard Duty": (2, 2, ""),
                       "For the Khan": (0, 1, "Charge"), "In the name of the king": (1, 1, ""),
                       "Roman Formation Phalanx": (1, 1, "")}
list_of_spells_that_reduce_mana = {"Call of the Khan": ("Charge", 100), "Call of the Emperor": ("", 1),
                                   "Old Tactics": ("", 3)}
list_of_spells_with_specific_targets = {"Rain of Arrows": ("Non Armored", "ALL")}
list_of_spells_that_affect_the_battlefield = {"Roman Formation Circular": "self", "For the Khan": "self",
                                              "In the name of the king": "self", "Roman Formation Phalanx": "self"}
list_of_spells_that_buff_specific_targets = {"Guard Duty": ("Guard", "draw")}
list_of_spells_that_draw_cards_conditional = {"Guard Duty": 1}
list_of_spells_that_summon_specific_cards = {
    "Boarder Guards": (2, [Creature(2, "Akritoi", 3, 2, "Guard", generate_random_int()) for i in range(0, 10)]),
    "Fast Conscription": (4, [Creature(1, "Peasant", 1, 1, "", generate_random_int()) for i in range(0, 40)])}
