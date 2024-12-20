import random

from production_server.clases.creatures import Creature

from production_server.clases.Defence import Defence

from production_server.clases.spells import Spell
from production_server.decks.all_cards_in_the_game import *


def generate_random_int():
    return random.randint(1, 1000000)


def get_list_of_all_war_animals(creature_list):
    animal1 = creature_list[0]
    animal2 = creature_list[1]
    animal3 = creature_list[2]
    creature_list = creature_list[:3]
    return [animal1, animal2, animal3]


list_of_bears = [Creature(3, "War Bear", 4, 4, "Guard", "animal", generate_random_int()) for i in range(0, 10)]
list_of_dogs = [Creature(3, "War Dog", 2, 4, "Charge", "animal", generate_random_int()) for i in range(0, 10)]
list_of_eagles = [Creature(3, "War Eagle", 4, 2, "Your minions get +1 attack", "animal", generate_random_int()) for i in
                  range(0, 10)]
list_of_animals = [Creature(3, "War Bear", 4, 4, "Guard", "animal", generate_random_int()) for i in range(0, 10)]
list_of_animals.extend([Creature(3, "War Dog", 2, 4, "Charge", "animal", generate_random_int()) for i in range(0, 10)])
list_of_animals.extend(
    [Creature(3, "War Eagle", 4, 2, "Your minions get +1 attack", "animal", generate_random_int()) for i in
     range(0, 10)])
war_pack = [[bear, eagle, dog] for (bear, eagle, dog) in zip(list_of_bears, list_of_eagles, list_of_dogs)]
"""
Creatures
"""
list_of_creature_description = ["Two-handed Knight", "Hospitaller Knight", "Priest", "Lumberjack", "Armorer", "Archer",
                                "Personal instructor", "Scared Noble", "Bishop", "Protokentarchos", "Animal Tamer",
                                "Church Builder", "Countryside Hunter", "Voice of the emperor", "Bailiff",
                                "Mercenary Herbalist", "Wild Elephant", "Local Healer", "Clergy", "Knight Arbalest",
                                "Knight Archer", "Heavy Armored Knight", "Motivated Squire", "Rogue Cleric",
                                "Harsh Trainer", "Heavy Arbalest", "Herbalist Guard", "Herbalist Knight",
                                "Full Armored Legionary", "Payed Scribe", "Veteran Tactician"]
list_of_creature_that_deal_dmg_to_enemies = {"Two-handed Knight": 99, "Archer": 1, "Wild Elephant": 4,
                                             "Knight Arbalest": 0, "Knight Archer": 0, "Heavy Armored Knight": 0,
                                             "Motivated Squire": 0, "Harsh Trainer": 1, "Heavy Arbalest": 4,
                                             "Full Armored Legionary": 0, "Limmu": 0, "Payed Scribe": 0,
                                             "Mercenary knight": 0, "Veteran Tactician": 0}
list_of_creature_that_can_target_yourself = {"Archer": 1, "Harsh Trainer": 1, "Heavy Arbalest": 4}
list_of_creature_that_deal_dmg_to_players = {"Archer": 1, "Wild Elephant": 4, "Knight Arbalest": 0, "Knight Archer": 0,
                                             "Motivated Squire": 0, "Heavy Arbalest": 4, "Payed Scribe": 0}
list_of_creature_that_do_something_at_the_end_of_your_turn = {"Scribe": ("draw", 1), "Miner": ("draw", 1),
                                                              "Carcassonne": ("damage 1 all enemies", 8)}
list_of_creature_that_heal = {"Hospitaller Knight": 2, "Priest": 99, "Church Builder": 8, "Mercenary Herbalist": 6,
                              "Local Healer": 4, "Clergy": 3, "Herbalist Guard": 3, "Herbalist Knight": 3}
list_of_creature_that_can_heal_players = {"Church Builder": 8, "Mercenary Herbalist": 6, "Local Healer": 4, "Clergy": 3,
                                          "Herbalist Guard": 3, "Herbalist Knight": 3}
list_of_creature_that_buff = {"Priest": (1, 1), "Lumberjack": (0, 1), "Armorer": (0, 0, "Armored"),
                              "Scared Noble": (0, 0, "Guard"), "Personal instructor": (1, 1),
                              "Watchtower": (2, 1, ""), "Drummer": (1, 1, ""), "Negotiator": (1, 1, ""),
                              "Last Defender": (0, 2, "Guard"), "Frederick Barbarossa": (1, 1, "Armored"),
                              "Bishop": (4, 4, "Guard"), "Protokentarchos": (3, 3, ""),
                              "Selfless Knight": (0, 0, "Armored"), "Animal Tamer": (2, 2, "Guard"),
                              "Countryside Hunter": (1, 1, ""), "Peasant Fighter": (1, 1, ""),
                              "Church Scholar": (1, 1, ""), "New Recruit": (0, 1, ""),
                              "Banner holder": (1, 0, ""), "Inspired soldier": (0, 0, "Guard Armored"),
                              "Knight's Trainee": (0, 1, "Guard"), "Mercenary Charger": (0, 1, "Charge"),
                              "Motivated Page": (1, 1, ""), "Honor Guard": (0, 1, "Guard"),
                              "Church Knight": (0, 0, "Guard Armored"), "Rogue Cleric": (1, 1, ""),
                              "Inspiring mercenary": (1, 1, ""), "Apollodorus of Damascus": (0, 1, ""),
                              "Harsh Trainer": (0, 2, ""), "Nero": (0, 6, ""), "Nero's Guard": (0, 3, ""),
                              "City Defender": (2, 2, ""), "Ancient Imperial Guard": (3, 3, "Guard"),
                              "Frenzied Mercenary": (0, 2, "Charge"), "Auxiliar Defender": (1, 1, ""),
                              "Charles V": (0, 0, "Rush Guard Armored Rebuilder"), "Scavenger Hyena": (1, 2, ""),
                              "Lndrau Aaurentis": (0, 0, "Guard"), "Ephix Maximus": (0, 2, "Charge"),
                              "Payed Guard": (3, 3, ""), "Veteran Knight": (1, 1, ""), "Henry III": (0, 0, "Armored"),
                              "Church Helper": (2, 1, ""), "Armored Librarian": (1, 1, "Armored"),
                              "Ancient Champion": (1, 1, ""), "Empire Believer": (1, 1, "")
                              }
list_of_creature_that_buff_specific_cards = {"Animal Tamer": "animal", "Countryside Hunter": "worker"}
list_of_creature_with_on_going_effect = ["War elephant", "Army Champion", "War Eagle", "King Saragon of Akkad"]
list_of_creature_with_negative_on_going_effect = {}
list_of_creature_with_positive_on_going_effect = {"Army Champion": (1, 1, ""), "War elephant": (0, 1, ""),
                                                  "War Eagle": (0, 1, ""),
                                                  "King Saragon of Akkad": (2, 2, "ancient")}
list_of_creature_that_are_effected_by_action = {"Church Scholar": ("self_buff", "heal creature"),
                                                "Enthusiastic Archer": ("damage:random:enemies:all:1", "summ all"),
                                                "New Recruit": ("self_buff", "summ soldier"),
                                                "Wondering Scribe": ("draw", "cast spell"),
                                                "Roman Architect": ("add_defence", "damage_taken"),
                                                "Scavenger Hyena": ("self_buff", "friendly_minion_dies:animal"),
                                                "Worker Recruiter": ("add_to_hand:workers", "summ worker"),
                                                "Soldier Architect": ("add_defence:self", "damage_taken"),
                                                "Claudius": ("add_defence", "kill_minion"),
                                                "Pyrrho of Elis": ("add_to_hand:Fire Arrow", "cast spell"),
                                                "Church Helper": ("buff new summ", "summ 1 hp minion"),
                                                "Tolui": ("damage:enemy_hero:spell_cost", "cast spell"),
                                                "Armored Librarian": ("self_buff", "cast spell:self"),
                                                "Tax collector": ("heal:empire:1", "summ all"),
                                                "Ancient Champion": ("self_buff", "summ ancient"),
                                                "Empire Believer": ("self_buff", "heal kingdom"),
                                                "Church Story Teller": (
                                                    "draw:heal:empire:1", "buff creature with spell"),
                                                "Knight of the Coin": ("draw", "attacking")
                                                }
list_of_creature_that_are_effected_by_action_once = {"Soldier Architect": 0}
list_of_creature_that_draw_card_on_action = {"Wondering Scribe": 1, "Knight of the Coin": 2, "Church Story Teller": 1}
list_of_creature_that_add_armor_on_action = {"Roman Architect": 1, "Soldier Architect": 2, "Claudius": 10}
list_of_creature_that_draw_cards = {"Page": 1, "Wild Horse": 1, "Watchman": 1, "Negotiator": 1,
                                    "Richard the Lionheart": 2, "Scribe of the Church": 1,
                                    "Mesopotamia Scholar": 1, "Landlord": 3, "Mercenary Recruiter": 1,
                                    "Byzantium Engineer": 1, "Tiberius": 3, "War Crier": 1, "Godfrey of Bouillon": 3,
                                    "Battle Tactician": 1, "Heraclius": 0, "Trained Dog": 1,
                                    "Wandering Bard": 1, "Selfish Soldier": 1}
list_of_creature_that_draw_specific_cards = {
    "Trained Dog": (["Creature"], ["Rush"], [""]),
    "Battle Tactician": (["Spell"], ["Tactic"], [""]),
    "Godfrey of Bouillon": (["Creature", "Creature", "Creature"], ["Rush", "Desperate", "Rebuilder"], ["", "", ""]),
    "War Crier": (["Creature"], ["Rush"], [""]),
    "Tiberius": (["Creature", "Creature", "Creature"], ["", "", ""], ["worker", "mercenary", "knight"]),
    "Byzantium Engineer": (["Defence"], [""], [""]),
    "Mercenary Recruiter": (["Creature"], [""], ["mercenary"]),
    "Landlord": (["Creature", "Creature", "Creature"], ["", "", ""], ["worker", "worker", "worker"]),
    "Negotiator": (["Creature"], [""], ["animal"]),
    "Wild Horse": (["Creature"], ["Charge"], [""]),
    "Scribe of the Church": (["Spell"], [""], [""]),
    "Watchman": (["Creature"], ["Guard"], [""]),
    "Richard the Lionheart": (
        ["Creature", "Spell"], ["", ""], ["", ""])}
list_of_creature_that_add_mana = {"Farmer": 1}
list_of_creature_that_summon = {
    "Work Friend": (1, [Creature(1, "Peasant", 1, 1, "", "worker", generate_random_int()) for i in range(0, 10)]),
    "Hammurabi": [0,
                  [Creature(3, "Man at Arms", 3, 3, "Rush", "ancient", generate_random_int()) for i in range(0, 40)]],
    "Snow Leopard": [0, [Creature(2, "Leopard", 2, 2, "", "animal", generate_random_int()) for i in range(0, 10)]],
    "Shepherd": (1, [Creature(1, "Guard Dog", 1, 1, "Guard", "animal", generate_random_int()) for i in range(0, 10)]),
    "Domestic cat": (1, [Creature(1, "Wild Cat", 1, 1, "", "animal", generate_random_int()) for i in range(0, 10)]),
    "Hunter": (1, [Creature(1, "Dog", 1, 1, "", "animal", generate_random_int()) for i in range(0, 10)]),
    "Rich Peasant": (
        2, [Creature(2, "Armored Peasant", 2, 1, "Armored Guard", "soldier", generate_random_int()) for i in
            range(0, 20)]),
    "Greek Peasant Recruiter": (
        1, [card for card in all_cards_in_game if card.card_type == "Creature" and card.mana_cost <= 3])}
list_of_creature_that_summ_random = {"Greek Peasant Recruiter"}
list_of_creature_that_are_affected_by_hand = {"Last Defender": ("empty hand", "buff"),
                                              "Drummer": ("affects hand", "buff", 1, 1, ""),
                                              "Negotiator": ("affects hand", "buff", 1, 1, ""),
                                              "Veteran Knight": ("affects hand", "buff", 1, 1, ""),
                                              "Banner holder": ("affects hand", "buff", 1, 0, ""),
                                              "Inspired soldier": ("hand_check:Spell", "buff"),
                                              "Knight Arbalest": ("hand_check:knight", "change:dmg", 5),
                                              "Knight Archer": ("hand_check:knight", "change:dmg", 2),
                                              "Heavy Armored Knight": ("hand_check:knight", "change:dmg", 7),
                                              "Motivated Squire": ("hand_check:knight", "change:dmg", 3),
                                              "Knight's Trainee": ("hand_check:knight", "buff"),
                                              "Mercenary Charger": ("hand_check:knight", "buff"),
                                              "Motivated Page": ("hand_check:knight", "buff"),
                                              "Honor Guard": ("hand_check:knight", "buff"),
                                              "Church Knight": ("hand_check:knight", "buff"),
                                              "Limmu": ("hand_check:number", "change:all:dmg"),
                                              "Ancient Full Armored soldier": ("hand_check:knight", "change:dmg", 3),
                                              "Heavy Armored Mercenary": ("hand_check:knight", "change:armor:gain", 5),
                                              "Mercenary Defences": ("hand_check:knight", "change:armor:gain", 5),
                                              "Knight Recruiter": ("hand_check:knight", "change:discover", "knights"),
                                              "Mercenary knight": ("hand_check:knight", "change:dmg", 99),
                                              "Alexander I": (
                                                  "hand_check:knight", "change:discover", "advance greek spells")
                                              }
list_of_creature_that_reduce_mana_cost = {"Sir William Marshal": ("deck", "Creature", "knight", 2),
                                          "Mercenary Contractor": ("deck,hand", "Creature", "mercenary", 1),
                                          "Veteran Knight": ("hand", "Creature", "knight", 1),
                                          "Soldier Motivator": ("hand", "Creature", "soldier", 1),
                                          "Wandering Bard": ("last card draw", "Spell", "", 1)}
list_of_creature_that_summ_after_they_die = {
    "Lost Chicken": (
        1, [Creature(5, "Lynx", 5, 5, "", "animal", generate_random_int()) for i in range(0, 40)]),
    "Alpha Wolf": (
        7, [Creature(1, "Wolf", 1, 1, "", "animal", generate_random_int()) for i in range(0, 40)]),
    "Lost Shield": (
        1, [Creature(4, "City Guard", 4, 4, "Guard", "soldier", generate_random_int()) for i in range(0, 5)]),
    "Graf": (
        3, [Creature(2, "Armored Peasant", 2, 1, "Guard Armored", "soldier", generate_random_int()) for i in
            range(0, 50)]),
    "Turtanu": (
        3, [Creature(1, "City Gate Guard", 3, 1, "Guard", "ancient", generate_random_int()) for i in range(0, 50)]),
    "Goat": (1, [Creature(2, "Hungry Wolf", 2, 3, "", "animal", generate_random_int()) for i in range(0, 5)]),
    "Mother Wolf": (2, [Creature(1, "Wolf Pup", 1, 1, "", "animal", generate_random_int()) for i in range(0, 5)]),
    "Lost Noble": (
        1, [Creature(4, "City Guard", 5, 3, "Guard", "soldier", generate_random_int()) for i in range(0, 5)]),
    "Lost Sheep": (2, [Creature(1, "Wild Wolf", 1, 1, "", "animal", generate_random_int()) for i in range(0, 10)]),
    "Front Line Defender": (
        1, [Creature(1, "Second Line Defender", 2, 1, "Guard", "soldier", generate_random_int()) for i in range(0, 5)]),
    "Joan of Arc": (
        1,
        [Creature(9, "Saint Joan of Arc", 8, 7, "Armored Charge", "knight", generate_random_int()) for i in
         range(0, 3)]),
    "Khevtuul": (2, [Creature(1, "Night Watcher", 2, 2, "", "soldier", generate_random_int()) for i in range(0, 10)])}
list_of_creature_that_affect_all = {"Watchtower": ("Creature", "Guard"), "Inspiring mercenary": ("Creature", "Guard"),
                                    "Apollodorus of Damascus": ("Defence", ""), "Lndrau Aaurentis": ("Creature", ""),
                                    "Ephix Maximus": ("Creature", "")}
list_of_creature_that_affect_in_hand_specific = {"Veteran Knight": ("Creature", "", "knight")}
list_of_creature_that_affect_all_when_die = {"Inspiring mercenary": "Guard"}
list_of_creature_that_affect_battle_field = {"Frederick Barbarossa": "Armored"}
list_of_creature_that_do_damage_to_all = {"Louis the Pious": 1}
list_of_creature_that_are_affected_in_hand = {"Trebuchet": ("reduce", "", 1), "Margrave": ("reduce", "", 1),
                                              "Covered Battering Ram": ("reduce", "all_on_battle_field", 1),
                                              "Eager Fighter": ("reduce", "all_on_battle_field", 1),
                                              "Battering Ram": ("reduce", "allies_on_battle_field", 1),
                                              "Senatus Populusque Romanus": ("reduce", "armor", 1),
                                              "Siege Tower": ("reduce", "spells_casted", 1),
                                              "Church Chosen": ("reduce", "amount_of_mana_on_spells"),
                                              "Boarder Skirmishes": ("reduce", "armor", 1),
                                              "Catapult": ("reduce", "amount_of_mana_on_spells"),
                                              "Eager Mercenary": ("reduce", "", 1),
                                              "Soldier Commander": ("reduce", "total_summoned:soldier", 1),
                                              "Torsion Catapult": ("reduce", "total_summoned:soldier", 1),
                                              "Mercenary Battering Ram": ("reduce", "amount_of_debt_in_game"),
                                              "Quick Arrow": ("reduce", "any_dead_minion:this_turn", "cost_set", 1),
                                              "Opportunistic  Hoplite": ("reduce", "tactics:number", 3)}
list_of_creature_that_do_somthing_when_die = {"Lost Sheep": "summ", "Lost Scribe": "draw", "Lost Shield": "summ",
                                              "Lost Noble": "summ", "Selfless Knight": "buff",
                                              "Front Line Defender": "summ", "Armored Horse": "draw",
                                              "Joan of Arc": "summ", "Khevtuul": "summ", "Mother Wolf": "summ",
                                              "Goat": "summ", "Turtanu": "summ", "Graf": "summ",
                                              "Big Game Beast": "draw", "Lure animal": "add_to_hand",
                                              "Inspiring knight": "add_to_hand", "Alpha Wolf": "summ",
                                              "Lost Chicken": "summ", "Lost Builder": "add_armor",
                                              "Thief Camp Guard": "add_armor",
                                              "Inspiring mercenary": "buffall",
                                              "Julius Caesar": "resumm",
                                              "Charlemagne": "put_wepon",
                                              "Dog Pup": "add_to_deck",
                                              "Louis the Pious": "deal_damage:all",
                                              "General Belisarius": "add_to_deck",
                                              "Caligula": "add_to_deck", "Cow": "draw&heal:kingdom:1",
                                              "Lerima,Persistent One": "add_to_hand"}
list_of_creature_that_do_damage_when_die = {}
list_of_creature_that_add_to_hand_when_die = {"Lure animal": 1, "Inspiring knight": 1, "Lerima,Persistent One": 1}
list_of_creature_that_add_to_armor_when_die = {"Lost Builder": 3, "Thief Camp Guard": 8}
list_of_creature_that_draw_cards_when_die = {"Lost Scribe": 1, "Armored Horse": 1, "Big Game Beast": 1, "Cow": 1}
list_of_creature_that_draw_specific_cards_when_die = {"Armored Horse": (["Spell"], [""], [""]),
                                                      "Big Game Beast": (["Creature"], ["animal"], [""])}
list_of_creature_that_will_do_damage_to_your_kingdom = {"Mesopotamia Scholar": 2, "Military Guard": 2, "Lu": 2,
                                                        "Heretic Knight": 2}
list_of_creature_that_can_make_kingdom_immun = {"King Saragon of Akkad"}
list_of_cards_that_discard = {"Assyrian Horserider": 2, "Cataclysm": 2, "Assassin's payment": 1, "Selfish Soldier": 1}
list_of_cards_that_discard_after_effect = {"Cataclysm", "Selfish Soldier"}
list_of_creature_that_have_effect_when_discarded = {"Prisoner of War", "Ancient Army Guard"}
legendary_cards = ["Richard the Lionheart", "Frederick Barbarossa", "Basil II", "Jochi", "Joan of Arc",
                   "King Saragon of Akkad", "Carcassonne", "Apollodorus of Damascus", "Tiberius", "Nero", "Charles V",
                   "Julius Caesar", "Godfrey of Bouillon", "Charles IV", "Hammurabi", "Louis the Pious",
                   "Get back to work", "We don't take it personally", "Kublai", "Imperial Drama", "Sir William Marshal",
                   "General Belisarius", "Heraclius", "Caligula", "Alexander I", "Pyrrho of Elis", "Tolui",
                   "Baldwin of Antioch", "I want actions not words"]
list_of_creature_that_are_affected_by_battle_field = {"Peasant Fighter": ("buff", "worker on field")}
list_of_creature_that_debuff = {"Voice of the emperor": (3, 3, " "), "Bailiff": (-1, 1, " "),
                                "Louis the Pious": (1, -1, " "), "Kublai": (1, -1, " "),
                                "Lenxaadra, Queen of Drama": (0, 0, "")}
list_of_creature_that_debuff_all = {"Louis the Pious"}
list_of_creature_that_debuff_enemies = {"Kublai"}
list_of_creature_that_add_defence = {
    "Rusticus Recruiter": [Defence(1, "Peasant Troops", 1, 3, "", generate_random_int()) for i in range(0, 10)],
    "Mercenary defender": [Defence(3, "Mercenary's Troops", 3, 2, "", generate_random_int()) for i in range(0, 10)]}
list_of_creature_that_add_defence_when_die = {
    "Charlemagne": [Defence(5, "Peasant Troops", 5, 3, "", generate_random_int()) for i in range(0, 10)]
}
list_of_cards_that_give_armor = {"Architecti": 5, "Build defences": 5, "Palisade Wall": 3, "Guard the Fort": 3,
                                 "Heavy Armored Mercenary": 0, "Mercenary Defences": 0, "Fall Trap": 2,
                                 "Julius Caesar": 4}
list_of_card_that_add_debt = {"Mercenary Champion": 2, "Mercenary soldier": 1, "Boarder Guards": 1, "Pilum Throw": 1,
                              "Roman Formation Phalanx": 1, "Protokentarchos": 1, "Ancient Empire": 1,
                              "Mercenary elite Defender": 2, "Mercenary Herbalist": 1, "Mercenary's Troops": 2,
                              "Mercenary Builder": 1, "Mercenary Leader": 2, "Mercenary Arrow Volley": 1,
                              "Sling shot": 1, "Mercenary arrow shot": 1, "War Cry": 1}
list_of_card_that_pay_debt = {"Wealthy Nobel", "Heraclius"}
list_of_cards_that_add_cards_to_your_hand = {"Mercenary employer": (1, "mercenary"),
                                             "Mercenary emissary": (1, "debt"),
                                             "Army Recruiter": (1, "soldier"),
                                             "Army Cook": (2, ""),
                                             "Empire Crusader": (5, "holy_roman"),
                                             "Recruiting": (2, "knights"),
                                             "Friendly Dog": (1, "animal"),
                                             "Ball-headed Mace Soldier": (1, ""),
                                             "Sparatan Auxiliars": (2, "")
                                             }
list_of_cards_that_add_cards_to_your_hand_by_action = {"Worker Recruiter": (1, "workers"),
                                                       "Pyrrho of Elis": (1, "spells")}
list_of_creature_that_add_cards_to_your_hand_when_die = {"Lure animal": (1, "animal"),
                                                         "Inspiring knight": (1, "knights"),
                                                         "Lerima,Persistent One": (1, "Lerima_self")}
list_of_creature_that_add_specific_card_to_your_hand = {
    "Army Cook": [Creature(1, "Kaiserliche", 1, 1, "", "soldier", generate_random_int()) for i in range(0, 40)],
    "Sparatan Auxiliars": [Creature(1, "Auxiliars", 2, 1, "", "soldier", generate_random_int()) for i in
                           range(0, 40)],
    "Ball-headed Mace Soldier": [Spell(1, "Knock down", "Knocks down a target, draw a card", generate_random_int()) for
                                 i in range(0, 40)]}
list_of_creature_that_have_other_stat_while_damaged = {"Nero": "damaged", "Nero's Guard": "damaged",
                                                       "Frenzied Mercenary": "damaged"}
list_of_cards_that_check_your_kingdom = {"Unknown Territory": ("armor", "spend:all", "buff"),
                                         "Full Armored Legionary": ("armor", "check:all", "change:dmg"),
                                         "Known Territory": ("armor", "check:all", "buff"),
                                         "City Defender": ("armor", "check:1", "buff"),
                                         "Ancient Imperial Guard": ("health", "check:15", "buff"),
                                         "Auxiliar Defender": ("defence", "check:1", "buff"),
                                         "Commander Desperation": ("health", "check:12", 3),
                                         "Commander's last charge": ("health", "check:12", 6),
                                         "Charles V": ("deck", "check:holy", "buff"),
                                         "Novice Tactician": ("tactic", "check:1", "draw:1"),
                                         "Snow Leopard": ("tactic", "check:1", "summ:2"),
                                         "Payed Guard": ("deck", "check:Resources", "buff"),
                                         "Payed Scribe": ("deck", "check:Resources", 3),
                                         "Hammurabi": ("deck", "check:Resources", "summ"),
                                         "Heraclius": ("debt", "check:1", "draw:all"),
                                         "Veteran Tactician": ("tactic", "check:1", "change:dmg:6"),
                                         "Last Empire Believer": ("health", "check:-X", "buff")
                                         }
list_of_creature_that_do_damage_to_all_other_creatures = {"Limmu": 0, "Mercenary Lieutenant": 1}
list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms = {"Ancient Law Enforcer": 3,
                                                                       "Ancient Full Armored soldier": 0}
list_of_cards_that_discover = {"Vast Empire": "mercenary", "Crusade Calling": "knights", "Frightened Girl": "guards",
                               "Jaffa Merchant": "knights", "Knight Recruiter": "", "Chinese Tactician": "tactics",
                               "Greek Scrolls": "spells",
                               "Scrolls of war": "spells",
                               "Alexander I": "advance greek spells"}
list_of_creature_that_plays_a_card_from_your_deck = {"Battle Tactician"}
list_of_creature_that_add_cards_to_your_deck_when_die = {"Dog Pup": (
    1, [Creature(1, "Big Dog", 5, 4, "", "animal", generate_random_int()) for i in range(0, 20)]),
    "General Belisarius": (
        1, [Creature(5, "Imperial Guard", 10, 10, "Guard", "soldier", generate_random_int()) for i in range(0, 10)]),
    "Caligula": (
        1, [Creature(10, "Claudius", 10, 10, "Rush When this minion kills and enemy add 10 defences", "soldier",
                     generate_random_int()) for i in range(0, 10)]), }
list_of_cards_that_add_cards_to_your_deck = {"Ancient Farmer":
                                                 (2, [Spell(0, "Resources",
                                                            "Restore 2 health to your kingdom when drawn",
                                                            generate_random_int()) for i in range(0, 40)]),
                                             "Ancient Arrow Volley": (2, [Spell(0, "Resources",
                                                                                "Restore 2 health to your kingdom when drawn",
                                                                                generate_random_int()) for i in
                                                                          range(0, 40)]),
                                             "Ancient Arrow Shot": (2, [Spell(0, "Resources",
                                                                              "Restore 2 health to your kingdom when drawn",
                                                                              generate_random_int()) for i in
                                                                        range(0, 40)])}
list_of_creature_that_damage_a_random_creature = {"Mercenary knight": 1}
list_of_creature_that_affect_all_enemy_minions = {"Lenxaadra, Queen of Drama": "debuff"}
list_of_creature_that_freeze_on_attack = {"Sling Shooter"}
"""
Spells
"""
list_of_cards_that_reset_at_the_end_of_turn_in_hand = {"Quick Arrow"}
list_of_spells_that_have_a_range = {"Mercenaries Reinforcements": random.randint(2, 4),
                                    "Sling shot": random.randint(3, 6)}
list_of_spells = ["Volley", "Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages", "Horse riding lessons",
                  "Bodyguards", "Feudal Obligations", "Epidemic", "Knight's training", "Peace Treaty",
                  "Wealthy Empire", "Ancient Empire", "Call of the Khan", "Call of the Emperor", "Arbalest Shot",
                  "Chivalry and Honor", "Horse raiding shot", "Landslide", "Rain of Arrows", "Roman Formation Circular",
                  "Guard Duty", "For the Khan", "Boarder Guards", "In the name of the king", "Roman Formation Phalanx",
                  "Old Tactics", "Pilum Throw", "Fast Conscription", "Strength in numbers", "Animal Battle Companion",
                  "War Pack", "Tag Team", "Call of God", "Ancient Tactics", "Mercenaries Reinforcements",
                  "Tactical Coordination", "Cataclysm", "Warhammer", "Trapped path", "Defending  the empire",
                  "Build defences", "Palisade Wall", "Guard the Fort", "Emperor's Hope", "Emperor's Will",
                  "Pilum Volley", "Recruiting", "Unknown Territory", "Senatus Populusque Romanus", "Known Territory",
                  "Heat of the desert", "A day in the desert", "Fast Auxiliars", "Mercenary Defences",
                  "Commander Desperation", "Commander's last charge", "Whip hit", "Fall Trap", "Vast Empire",
                  "Crusade Calling", "Tavern Fight", "Execute", "Shield of Honor", "Priority Target", "Avenge",
                  "You don't scare me", "Hidden Armor", "Arbalets Volley", "Church Chosen", "Wild Bear",
                  "We don't take it personally", "Get back to work", "Resources", "Ancient Arrow Volley",
                  "Ancient Arrow Shot", "Snare Trap", "Fire Trap", "Deadly Shot", "Quick Shot", "Hit and Run",
                  "Imperial Drama", "Boarder Skirmishes", "Knock down", "Mercenary Arrow Volley",
                  "Fast Mercenary Recruiting", "Sling shot", "Mercenary arrow shot", "Quick Arrow", "Well Trained Pet",
                  "Second Charge", "Swamped", "War Cry", "Flaming arrow", "Greek Scrolls", "Spartan Volley",
                  "Cultural Empire", "Net Throw", "Ballestris Volly", "Elephants stampede", "Catapult Shot",
                  "Lagoras discovery", "Scrolls of war", "Arbalest Flame Shot", "Gladiator Net Throw",
                  "King Recruiting", "Catapult Volley", "The Kings Charge", "Kings Guard Volley", "Auxiliar Volley",
                  "Wild Training", "Savage Empire", "Light of Hope", "Assassin's payment", "Will of God",
                  "Collateral Victim", "I want actions not words"]
list_of_self_target = {"Personal Guard": "Guard", "Bandage": "", "Bandages": "", "Horse riding lessons": "Charge",
                       "Knight's training": "", "Chivalry and Honor": "", "Guard Duty": "", "For the Khan": "Charge",
                       "Strength in numbers": "", "Call of God": "", "Emperor's Hope": "", "Emperor's Will": "",
                       "Whip hit": "", "Fall Trap": "", "Shield of Honor": "", "Church Chosen": "", "War Cry": "",
                       "Savage Empire": "", "Light of Hope": "", "Will of God": "", "Collateral Victim": ""}
list_of_healing_spells = {"Bandage": 4, "Bandages": 99, "Call of God": 8, "Emperor's Hope": 8}
list_of_dmg_spells = {"Arrow shot": 2, "Epidemic": 100, "Volley": 2, "Kill": 100, "Arbalest Shot": 3,
                      "Horse raiding shot": 2, "Landslide": 7, "Rain of Arrows": 100, "Pilum Throw": 3, "Tag Team": 3,
                      "Mercenaries Reinforcements": list_of_spells_that_have_a_range.get("Mercenaries Reinforcements"),
                      "Cataclysm": 100, "Palisade Wall": 3, "Pilum Volley": 1, "Unknown Territory": 0,
                      "Senatus Populusque Romanus": 2, "Known Territory": 0, "Heat of the desert": 5,
                      "A day in the desert": 3, "Mercenary Defences": 5, "Commander Desperation": 1,
                      "Commander's last charge": 4, "Whip hit": 1, "Fall Trap": 2, "Tavern Fight": 99, "Execute": 99,
                      "Arbalets Volley": 2, "Ancient Arrow Volley": 2, "Ancient Arrow Shot": 3, "Deadly Shot": 99,
                      "Quick Shot": 3, "Hit and Run": 1, "Boarder Skirmishes": 5, "Knock down": 0,
                      "Mercenary Arrow Volley": 3, "Sling shot": list_of_spells_that_have_a_range.get("Sling shot"),
                      "Mercenary arrow shot": 2, "Quick Arrow": 4, "Well Trained Pet": 3, "Swamped": 99, "War Cry": 1,
                      "Flaming arrow": 6, "Spartan Volley": 5, "Net Throw": 3, "Ballestris Volly": 2,
                      "Catapult Shot": 10, "Scrolls of war": 2, "Arbalest Flame Shot": 8, "Gladiator Net Throw": 3,
                      "Catapult Volley": 8, "Kings Guard Volley": 2, "Auxiliar Volley": 1, "Assassin's payment": 100,
                      "Collateral Victim": 100
                      }
list_of_dmg_spells_but_not_to_player = {"Tag team", "Mercenary Defences", "Whip hit", "Ancient Arrow Shot",
                                        "Mercenary arrow shot", "Quick Arrow", "Kill", "Assassin's payment",
                                        "Collateral Victim"}
list_of_spells_that_kill_the_target = {"Kill", "Assassin's payment", "Collateral Victim"}
list_of_resetting_spells = ["Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages", "Horse riding lessons",
                            "Knight's training", "Arbalest Shot", "Chivalry and Honor", "Pilum Throw",
                            "Strength in numbers", "Tag Team", "Emperor's Will", "Execute", "Shield of Honor",
                            "Ancient Arrow Shot", "Mercenary arrow shot", "Quick Arrow", "Swamped", "War Cry",
                            "Flaming arrow", "Net Throw", "Catapult Shot", "Arbalest Flame Shot", "Gladiator Net Throw",
                            "Savage Empire", "Light of Hope", "Assassin's payment", "Collateral Victim"]
list_of_spells_with_no_target = ["Bodyguards", "Feudal Obligations", "Epidemic", "Volley", "Peace Treaty",
                                 "Wealthy Empire", "Ancient Empire", "Call of the Khan", "Call of the Emperor",
                                 "Landslide", "Rain of Arrows", "Roman Formation Circular", "For the Khan",
                                 "Boarder Guards", "In the name of the king", "Roman Formation Phalanx",
                                 "Old Tactics", "Fast Conscription", "Animal Battle Companion", "War Pack",
                                 "Ancient Tactics", "Tactical Coordination", "Cataclysm", "Trapped path",
                                 "Defending  the empire", "Build defences", "Guard the Fort", "Pilum Volley",
                                 "Recruiting", "Unknown Territory", "Senatus Populusque Romanus", "Heat of the desert",
                                 "A day in the desert", "Fast Auxiliars", "Commander Desperation", "Vast Empire",
                                 "Crusade Calling", "Tavern Fight", "Priority Target", "Avenge", "You don't scare me",
                                 "Hidden Armor", "Arbalets Volley", "Wild Bear", "We don't take it personally",
                                 "Get back to work", "Ancient Arrow Volley", "Snare Trap", "Fire Trap", "Deadly Shot",
                                 "Hit and Run", "Imperial Drama", "Boarder Skirmishes", "Mercenary Arrow Volley",
                                 "Fast Mercenary Recruiting", "Second Charge", "Greek Scrolls", "Spartan Volley",
                                 "Cultural Empire", "Ballestris Volly", "Elephants stampede", "Lagoras discovery",
                                 "King Recruiting", "Catapult Volley", "The Kings Charge", "Kings Guard Volley",
                                 "Auxiliar Volley", "Wild Training", "I want actions not words"]
list_of_spells_that_summon = {"Wealthy Empire": ("", 2), "Bodyguards": ("Guard", 2), "Boarder Guards": ("", 0),
                              "Fast Conscription": ("", 0), "Animal Battle Companion": ("", 0), "War Pack": ("", 0),
                              "Tag Team": ("", 0), "Call of God": ("", 0), "Mercenaries Reinforcements": ("", 0),
                              "Defending  the empire": ("", 0), "Guard the Fort": ("", 0), "Crusade Calling": ("", 0),
                              "Fast Mercenary Recruiting": ("", 0), "Second Charge": ("", 0), "Savage Empire": ("", 0)}
list_of_spells_that_draw_cards = {"Feudal Obligations": 2, "Personal Guard": 1, "Ancient Empire": 2,
                                  "Call of the Khan": 1, "Call of the Emperor": 3, "Arbalest Shot": 1,
                                  "Chivalry and Honor": 1, "Horse raiding shot": 1, "Old Tactics": 1,
                                  "Ancient Tactics": 3, "Tactical Coordination": 3, "Build defences": 1,
                                  "Emperor's Hope": 3, "Fast Auxiliars": 2, "Knock down": 1, "Cultural Empire": 2,
                                  "King Recruiting": 4, "Wild Training": 1}
list_of_buff_spells = {"Bandage": (0, 0, ""), "Bandages": (0, 0, ""), "Horse riding lessons": (0, 2, "Charge"),
                       "Personal Guard": (0, 0, "Guard"),
                       "Roman Formation Circular": (0, 0, "Guard"),
                       "Knight's training": (3, 3, ""), "Chivalry and Honor": (1, 2, ""), "Guard Duty": (2, 2, ""),
                       "For the Khan": (0, 1, "Charge"), "In the name of the king": (1, 1, ""),
                       "Roman Formation Phalanx": (1, 1, ""), "Strength in numbers": (3, 2, ""),
                       "Call of God": (0, 0, ""), "Emperor's Hope": (0, 0, ""), "Emperor's Will": (2, 1, ""),
                       "Whip hit": (0, 2, ""), "Shield of Honor": (0, 3, "Armored"), "Avenge": (2, 3, ""),
                       "Hidden Armor": (0, 0, "Armored"), "Church Chosen": (5, 5, "Armored"), "Knock down": (0, 0, ""),
                       "War Cry": (3, 3, ""), "Net Throw": (0, 0, ""), "Gladiator Net Throw": (0, 0, ""),
                       "Wild Training": (3, 3, ""), "Savage Empire": (0, 2, ""), "Light of Hope": (2, 2, ""),
                       "Will of God": (1, 1, " Can't be blocked ")
                       }
list_of_spells_that_reduce_mana = {"Call of the Khan": ("Charge", 100), "Call of the Emperor": ("", 1),
                                   "Old Tactics": ("", 3), "Greek Scrolls": ("", 2)}
list_of_spells_that_buff_conditional = {"Emperor's Will": ("hand:knight", (2, 1, "Armored")),
                                        "Quick Shot": ("hand:empty", "draw", 1),
                                        "Well Trained Pet": ("battle:animal", "change:damage:3", 5),
                                        }
list_of_spells_with_specific_targets = {"Rain of Arrows": ("Non Armored", "ALL")}
list_of_spells_that_affect_the_battlefield = {"Roman Formation Circular": "self", "For the Khan": "self",
                                              "In the name of the king": "self", "Roman Formation Phalanx": "self"}
list_of_spells_that_buff_specific_targets = {"Guard Duty": ("Guard", "draw"), "Strength in numbers": ("", "draw")}
list_of_spells_that_draw_cards_conditional = {"Guard Duty": 1, "Strength in numbers": 1, "Wild Training": 1}
list_of_spells_that_summon_specific_cards = {
    "Fast Mercenary Recruiting": (
        2, [Creature(4, "Man at Arms", 4, 5, "Rush", "soldier", generate_random_int()) for i in range(0, 50)]),
    "Wild Bear": [
        0, [Creature(3, "War Bear", 3, 3, "Guard", "animal", generate_random_int()) for i in range(0, 50)]],
    "Guard the Fort": (
        1, [Creature(2, "Fort Guard", 3, 2, "Guard", "soldier", generate_random_int()) for i in range(0, 50)]),
    "Defending  the empire": (
        3, [Creature(1, "Kaiserliche", 1, 1, "", "soldier", generate_random_int()) for i in range(0, 50)]),
    "Mercenaries Reinforcements": (list_of_spells_that_have_a_range.get("Mercenaries Reinforcements"),
                                   [Creature(1, "Man at arms", 1, 1, "", "ancient", generate_random_int()) for i in
                                    range(0, 40)]),
    "Tag Team": (1, [Creature(3, "Hunting dog", 3, 3, "", "animal", generate_random_int()) for i in range(0, 50)]),
    "Boarder Guards": (
        2, [Creature(2, "Akritoi", 3, 2, "Guard", "soldier", generate_random_int()) for i in range(0, 10)]),
    "Fast Conscription": (4, [Creature(1, "Peasant", 1, 1, "", "worker", generate_random_int()) for i in range(0, 40)]),
    "Animal Battle Companion": (1, [random.choice(list_of_animals) for i in range(0, 10)]),
    "War Pack": (3, get_list_of_all_war_animals(war_pack)),
    "Call of God": (
        1, [Creature(8, "Crusader", 8, 8, "Guard Armored", "knight", generate_random_int()) for i in range(0, 10)]),
    "Crusade Calling": (
        1, [Creature(5, "Crusader", 5, 5, "Guard", "knight", generate_random_int()) for i in range(0, 10)]),
    "Savage Empire": (
        2, [Creature(1, "Dog", 1, 1, "", "animal", generate_random_int()) for i in range(0, 50)])}
list_of_spells_that_draw_specific_cards = {"Strength in numbers": (["Creature"], [""]),
                                           "Fast Auxiliars": (["Defence", "Defence"], ["", ""]),
                                           "Wild Training": (["Creature"], ["animal"])}
list_of_spells_that_can_heal_player = {"Call of God": 8, "Emperor's Hope": 8, "Resources": 2}
list_of_spells_that_do_damage_to_your_kingdom = {"Ancient Tactics": 3}
list_of_spells_that_have_effect_when_discarded = {"Tactical Coordination"}
list_of_spells_that_debuff = {"Warhammer": (0, 0, ""), "You don't scare me": (1, 1, " ")}
list_of_spells_that_add_traps = {"Trapped path": 4}
list_of_spells_that_add_defences = {
    "Defending  the empire": Defence(1, "Empire Peasants", 1, 4, "", generate_random_int())
    for
    i in range(0, 10)}
list_of_spells_that_target_random_creatures = {"Tavern Fight": 13, "Deadly Shot": 1, "Hit and Run": 3}
list_of_spells_that_target_random_enemy_creature = {"Deadly Shot": 1, "Hit and Run": 3}
list_of_spells_that_do_something_conditional = {"Execute": "damaged", "Shield of Honor": "damaged",
                                                "Swamped": "damaged"}
list_of_spells_that_affect_one_target_and_then_the_rest = {"Swamped", "War Cry"}
list_of_tactics = {"Priority Target": "dmg_delt>3=>deal_dmg:99",
                   "Avenge": "friendly_minion_dies=>buff:random",
                   "You don't scare me": "attacking=>debuff",
                   "Hidden Armor": "attacking=>buff:target",
                   "Wild Bear": "attacking:kingdom=>summon:1",
                   "Snare Trap": "attacking=>send_to_hand",
                   "Fire Trap": "attacking:minion=>deal_dmg:2:enemies",
                   "Lagoras discovery": "summ=>deal_dmg:6:minion:rest_to_kingdom"}
list_of_quests = {"We don't take it personally": {"damage:taken_and_done:kingdom:0:8:add_to_hand": {
    1: Creature(5, "Lndrau Aaurentis", 8, 8, "Armored Guard All your cards get guard", "legend",
                generate_random_int()) for i in range(0, 10)}},
    "Get back to work": {"damage:taken_and_done:kingdom:0:6:add_to_hand": {
        1: Creature(5, "Ephix Maximus", 6, 6, "Charge Give all your cards Charge and +2 attack", "legend",
                    generate_random_int()) for i in range(0, 10)}},
    "Imperial Drama": {"damage:taken_and_done:kingdom:0:4:add_to_hand": {
        1: Creature(5, "Lenxaadra, Queen of Drama", 5, 5, "Silence all enemy minions from deck,hand and battlefield",
                    "legend",
                    generate_random_int()) for i in range(0, 10)}},
    "I want actions not words": {"damage:taken_and_done:kingdom:0:2:add_to_hand": {
        1: Creature(5, "Lerima,Persistent One", 10, 10,
                    "Charge Desperate return this to your hand",
                    "legend",
                    generate_random_int()) for i in range(0, 10)}},
}
list_of_spells_that_add_mana_cost = {"Snare Trap": 2}
list_of_cards_that_send_back_to_hand = {"Snare Trap": 1}
list_of_spells_that_auto_cast = {"Resources": "heal_player"}
list_of_spells_that_freeze = {"Knock down", "Swamped", "Net Throw", "Gladiator Net Throw", "The Kings Charge"}
list_of_spells_that_freeze_all_enemies = {"Ballestris Volly", "Elephants stampede", "The Kings Charge"}
list_of_spells_that_resummon = {"Second Charge": ("died:this_turn", "animal", 7)}
list_of_cards_that_change_hero_power = {"Baldwin of Antioch": {"Holy Roman Empire": "Order of the Church",
                                                               "Mongol Empire": "Mongol Hordes",
                                                               "Mesopotamia Empire": "Test of Time",
                                                               "Roman empire": "Fortifications!",
                                                               "Greek empire": "Macedonian Empire",
                                                               "Byzantine Empire": "Mercenary Empire"}}
list_of_permanent_effect = {"Henry III": {"Kaiserliche": "Armored"}}
list_of_spells_that_buff_drawn_cards = {"Wild Training"}
list_of_spells_that_only_heal_player = {"Savage Empire": 2, "Light of Hope": 3}
list_of_spells_that_target_multiple_targets = {"Collateral Victim": 2}
list_of_spells_that_do_damage_to_your_minion_then_the_enemy = {
    "Collateral Victim": {"own_minion_picked": False, "enemy_minion_picked": False}}
"""
Defence
"""
list_of_defences = ["Empire Peasants", "Mercenary's Troops", "Mercenary's Auxiliar"]
