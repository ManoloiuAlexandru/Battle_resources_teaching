import random

from clases.creatures import Creature

from clases.Defence import Defence


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
                                "Mercenary Herbalist", "Wild Elephant", "Local Healer", "Clergy"]
list_of_creature_that_deal_dmg_to_enemies = {"Two-handed Knight": 99, "Archer": 1, "Wild Elephant": 4}
list_of_creature_that_deal_dmg_to_players = {"Archer": 1, "Wild Elephant": 4}
list_of_creature_that_do_something_at_the_end_of_your_turn = {"Scribe": ("draw", 1), "Miner": ("draw", 1),
                                                              "Carcassonne": ("damage 1 all enemies", 8)}
list_of_creature_that_heal = {"Hospitaller Knight": 2, "Priest": 99, "Church Builder": 8, "Mercenary Herbalist": 6,
                              "Local Healer": 4, "Clergy": 3}
list_of_creature_that_can_heal_players = {"Church Builder": 8, "Mercenary Herbalist": 6, "Local Healer": 4, "Clergy": 3}
list_of_creature_that_buff = {"Priest": (1, 1), "Lumberjack": (0, 1), "Armorer": (0, 0, "Armored"),
                              "Scared Noble": (0, 0, "Guard"), "Personal instructor": (1, 1),
                              "Watchtower": (2, 1, ""), "Drummer": (1, 1, ""), "Negotiator": (1, 1, ""),
                              "Last Defender": (0, 2, "Guard"), "Frederick Barbarossa": (1, 1, "Armored"),
                              "Bishop": (5, 5, "Guard"), "Protokentarchos": (3, 3, ""),
                              "Selfless Knight": (0, 0, "Armored"), "Animal Tamer": (2, 2, "Guard"),
                              "Countryside Hunter": (1, 1, ""), "Peasant Fighter": (1, 1, ""),
                              "Church Scholar": (1, 1, ""), "New Recruit": (0, 1, ""),
                              "Banner holder": (1, 0, ""), "Inspired soldier": (0, 0, "Guard Armored")}
list_of_creature_that_buff_specific_cards = {"Animal Tamer": "animal", "Countryside Hunter": "worker"}
list_of_creature_with_on_going_effect = ["War elephant", "Army Champion", "War Eagle", "King Saragon of Akkad"]
list_of_creature_with_negative_on_going_effect = {}
list_of_creature_with_positive_on_going_effect = {"Army Champion": (1, 1, ""), "War elephant": (0, 1, ""),
                                                  "War Eagle": (0, 1, ""),
                                                  "King Saragon of Akkad": (2, 2, "ancient")}
list_of_creature_that_are_effected_by_action = {"Church Scholar": ("self_buff", "heal"),
                                                "New Recruit": ("self_buff", "summ soldier"),
                                                "Wondering Scribe": ("draw", "cast spell")}
list_of_creature_that_draw_card_on_action = {"Wondering Scribe": 1}
list_of_creature_that_draw_cards = {"Page": 1, "Wild Horse": 1, "Watchman": 1, "Negotiator": 1,
                                    "Richard the Lionheart": 2, "Scribe of the Church": 1,
                                    "Mesopotamia Scholar": 1, "Landlord": 3, "Mercenary Recruiter": 1,
                                    "Byzantium Engineer": 1}
list_of_creature_that_draw_specific_cards = {
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
    "Shepherd": (1, [Creature(1, "Guard Dog", 1, 1, "Guard", "animal", generate_random_int()) for i in range(0, 4)]),
    "Domestic cat": (1, [Creature(1, "Wild Cat", 1, 1, "", "animal", generate_random_int()) for i in range(0, 4)]),
    "Hunter": (1, [Creature(1, "Dog", 1, 1, "", "animal", generate_random_int()) for i in range(0, 4)]),
    "Rich Peasant": (
        2, [Creature(2, "Armored Peasant", 2, 1, "Armored Guard", "soldier", generate_random_int()) for i in
            range(0, 10)])}
list_of_creature_that_are_affected_by_hand = {"Last Defender": ("empty hand", "buff"),
                                              "Drummer": ("affects hand", "buff", 1, 1, ""),
                                              "Negotiator": ("affects hand", "buff", 1, 1, ""),
                                              "Banner holder": ("affects hand", "buff", 1, 0, ""),
                                              "Inspired soldier": ("hand_check:Spell", "buff")
                                              }
list_of_creature_that_summ_after_they_die = {
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
list_of_creature_that_affect_all = {"Watchtower": "Guard"}
list_of_creature_that_affect_battle_field = {"Frederick Barbarossa": "Armored"}
list_of_creature_that_are_affected_in_hand = {"Trebuchet": ("reduce", "", 1), "Margrave": ("reduce", "", 1),
                                              "Covered Battering Ram": ("reduce", "all_on_battle_field", 1),
                                              "Battering Ram": ("reduce", "allies_on_battle_field", 1)}
list_of_creature_that_do_somthing_when_die = {"Lost Sheep": "summ", "Lost Scribe": "draw", "Lost Shield": "summ",
                                              "Lost Noble": "summ", "Selfless Knight": "buff",
                                              "Front Line Defender": "summ", "Armored Horse": "draw",
                                              "Joan of Arc": "summ", "Khevtuul": "summ", "Mother Wolf": "summ",
                                              "Goat": "summ", "Turtanu": "summ", "Graf": "summ",
                                              "Big Game Beast": "draw", "Lure animal": "add_to_hand"}
list_of_creature_that_add_to_hand_when_die = {"Lure animal": 1}
list_of_creature_that_draw_cards_when_die = {"Lost Scribe": 1, "Armored Horse": 1, "Big Game Beast": 1}
list_of_creature_that_draw_specific_cards_when_die = {"Armored Horse": (["Spell"], [""], [""]),
                                                      "Big Game Beast": (["Creature"], ["animal"], [""])}
list_of_creature_that_will_do_damage_to_your_kingdom = {"Mesopotamia Scholar": 2, "Military Guard": 2, "Lu": 2,
                                                        "Heretic Knight": 2}
list_of_creature_that_can_make_kingdom_immun = {"King Saragon of Akkad"}
list_of_cards_that_discard = {"Assyrian Horserider": 2, "Cataclysm": 2}
list_of_creature_that_have_effect_when_discarded = {"Prisoner of War"}
legendary_cards = ["Richard the Lionheart", "Frederick Barbarossa", "Basil II", "Jochi", "Joan of Arc",
                   "King Saragon of Akkad", "Carcassonne"]
list_of_creature_that_are_affected_by_battle_field = {"Peasant Fighter": ("buff", "worker on field")}
list_of_creature_that_debuff = {"Voice of the emperor": (3, 3, " "), "Bailiff": (-1, 1, " ")}
list_of_creature_that_add_defence = {
    "Mercenary defender": Defence(3, "Mercenary's Troops", 3, 2, "", generate_random_int()) for i in range(0, 10)}
list_of_cards_that_give_armor = {"Architecti": 5, "Build defences": 5, "Palisade Wall": 3, "Guard the Fort": 3}
list_of_card_that_add_debt = {"Mercenary Champion": 2, "Mercenary soldier": 1, "Boarder Guards": 1, "Pilum Throw": 1,
                              "Roman Formation Phalanx": 1, "Protokentarchos": 1, "Ancient Empire": 1,
                              "Mercenary elite Defender": 2, "Mercenary Herbalist": 1, "Mercenary's Troops": 2}
list_of_card_that_pay_debt = {"Wealthy Nobel"}
list_of_creature_that_add_cards_to_your_hand = {"Mercenary employer": (1, "mercenary"),
                                                "Mercenary emissary": (1, "debt"),
                                                "Army Recruiter": (1, "soldier"),
                                                "Army Cook": (2, ""),
                                                "Empire Crusader": (5, "holy_roman")
                                                }
list_of_creature_that_add_cards_to_your_hand_when_die = {"Lure animal": (1, "animal")}
list_of_creature_that_add_specific_card_to_your_hand = {
    "Army Cook": [Creature(1, "Kaiserliche", 1, 1, "", "soldier", generate_random_int()) for i in range(0, 40)], }
"""
Spells
"""
list_of_spells_that_have_a_range = {"Mercenaries Reinforcements": random.randint(2, 4)}
list_of_spells = ["Volley", "Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages", "Horse riding lessons",
                  "Bodyguards", "Feudal Obligations", "Epidemic", "Knight's training", "Peace Treaty",
                  "Wealthy Empire", "Ancient Empire", "Call of the Khan", "Call of the Emperor", "Arbalest Shot",
                  "Chivalry and Honor", "Horse raiding shot", "Landslide", "Rain of Arrows", "Roman Formation Circular",
                  "Guard Duty", "For the Khan", "Boarder Guards", "In the name of the king", "Roman Formation Phalanx",
                  "Old Tactics", "Pilum Throw", "Fast Conscription", "Strength in numbers", "Animal Battle Companion",
                  "War Pack", "Tag Team", "Call of God", "Ancient Tactics", "Mercenaries Reinforcements",
                  "Tactical Coordination", "Cataclysm", "Warhammer", "Trapped path", "Defending  the empire",
                  "Build defences", "Palisade Wall", "Guard the Fort", "Emperor's Hope", "Emperor's Will"]
list_of_self_target = {"Personal Guard": "Guard", "Bandage": "", "Bandages": "", "Horse riding lessons": "Charge",
                       "Knight's training": "", "Chivalry and Honor": "", "Guard Duty": "", "For the Khan": "Charge",
                       "Strength in numbers": "", "Call of God": "", "Emperor's Hope": "", "Emperor's Will": ""}
list_of_healing_spells = {"Bandage": 4, "Bandages": 99, "Call of God": 8, "Emperor's Hope": 8}
list_of_dmg_spells = {"Arrow shot": 2, "Epidemic": 100, "Volley": 2, "Kill": 100, "Arbalest Shot": 3,
                      "Horse raiding shot": 2, "Landslide": 7, "Rain of Arrows": 100, "Pilum Throw": 3, "Tag Team": 3,
                      "Mercenaries Reinforcements": list_of_spells_that_have_a_range.get("Mercenaries Reinforcements"),
                      "Cataclysm": 99, "Palisade Wall": 3}
list_of_dmg_spells_but_not_to_player = {"Tag team"}
list_of_resetting_spells = ["Kill", "Arrow shot", "Personal Guard", "Bandage", "Bandages", "Horse riding lessons",
                            "Knight's training", "Arbalest Shot", "Chivalry and Honor", "Pilum Throw",
                            "Strength in numbers", "Tag Team", "Emperor's Will"]
list_of_spells_with_no_target = ["Bodyguards", "Feudal Obligations", "Epidemic", "Volley", "Peace Treaty",
                                 "Wealthy Empire", "Ancient Empire", "Call of the Khan", "Call of the Emperor",
                                 "Landslide", "Rain of Arrows", "Roman Formation Circular", "For the Khan",
                                 "Boarder Guards", "In the name of the king", "Roman Formation Phalanx",
                                 "Old Tactics", "Fast Conscription", "Animal Battle Companion", "War Pack",
                                 "Ancient Tactics", "Tactical Coordination", "Cataclysm", "Trapped path",
                                 "Defending  the empire", "Build defences", "Guard the Fort"]
list_of_spells_that_summon = {"Wealthy Empire": ("", 2), "Bodyguards": ("Guard", 2), "Boarder Guards": ("", 0),
                              "Fast Conscription": ("", 0), "Animal Battle Companion": ("", 0), "War Pack": ("", 0),
                              "Tag Team": ("", 0), "Call of God": ("", 0), "Mercenaries Reinforcements": ("", 0),
                              "Defending  the empire": ("", 0), "Guard the Fort": ("", 0)}
list_of_spells_that_draw_cards = {"Feudal Obligations": 2, "Personal Guard": 1, "Ancient Empire": 2,
                                  "Call of the Khan": 1, "Call of the Emperor": 3, "Arbalest Shot": 1,
                                  "Chivalry and Honor": 1, "Horse raiding shot": 1, "Old Tactics": 1,
                                  "Ancient Tactics": 3, "Tactical Coordination": 3, "Build defences": 1,
                                  "Emperor's Hope": 3
                                  }
list_of_buff_spells = {"Bandage": (0, 0, ""), "Bandages": (0, 0, ""), "Horse riding lessons": (0, 2, "Charge"),
                       "Personal Guard": (0, 0, "Guard"),
                       "Roman Formation Circular": (0, 0, "Guard"),
                       "Knight's training": (3, 3, ""), "Chivalry and Honor": (1, 2, ""), "Guard Duty": (2, 2, ""),
                       "For the Khan": (0, 1, "Charge"), "In the name of the king": (1, 1, ""),
                       "Roman Formation Phalanx": (1, 1, ""), "Strength in numbers": (3, 2, ""),
                       "Call of God": (0, 0, ""), "Emperor's Hope": (0, 0, ""), "Emperor's Will": (2, 1, "")}
list_of_spells_that_reduce_mana = {"Call of the Khan": ("Charge", 100), "Call of the Emperor": ("", 1),
                                   "Old Tactics": ("", 3)}
list_of_spells_that_buff_conditional = {"Emperor's Will": ("hand:knight", (3, 2, "Armored"))}
list_of_spells_with_specific_targets = {"Rain of Arrows": ("Non Armored", "ALL")}
list_of_spells_that_affect_the_battlefield = {"Roman Formation Circular": "self", "For the Khan": "self",
                                              "In the name of the king": "self", "Roman Formation Phalanx": "self"}
list_of_spells_that_buff_specific_targets = {"Guard Duty": ("Guard", "draw"), "Strength in numbers": ("", "draw")}
list_of_spells_that_draw_cards_conditional = {"Guard Duty": 1, "Strength in numbers": 1}
list_of_spells_that_summon_specific_cards = {
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
        1, [Creature(8, "Crusader", 8, 8, "Guard Armored", "knight", generate_random_int()) for i in range(0, 10)])}
list_of_spells_that_draw_specific_cards = {"Strength in numbers": (["Creature"], [""])}
list_of_spells_that_can_heal_player = {"Call of God": 8, "Emperor's Hope": 8}
list_of_spells_that_do_damage_to_your_kingdom = {"Ancient Tactics": 3}
list_of_spells_that_have_effect_when_discarded = {"Tactical Coordination"}
list_of_spells_that_debuff = {"Warhammer": (0, 0, "")}
list_of_spells_that_add_traps = {"Trapped path": 4}
list_of_spells_that_add_defences = {
    "Defending  the empire": Defence(1, "Empire Peasants", 1, 4, "", generate_random_int())
    for
    i in range(0, 10)}
"""
Defence
"""
list_of_defences = ["Empire Peasants", "Mercenary's Troops"]
