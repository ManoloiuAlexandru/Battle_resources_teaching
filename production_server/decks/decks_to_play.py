from clases.creatures import Creature
from clases.spells import Spell

from clases.Defence import Defence

from decks.byzantine_empire import cards_for_byzantine_empire

from decks.holy_roman_empire import list_of_holy_roman, cards_for_holy_roman_empire

from decks.mesopotamia_empire import mesopotamia_empire
from decks.mongols_empire import cards_for_mongol_empire, mongols_hordes

from decks.all_cards_in_the_game import cards_that_are_in_the_game_for_all

from decks.roman_empire import roman_empire

bot_deck = [
]
demo_deck = [
    Creature(0,"")
]

list_of_knights = [[Creature(3, "Motivated Squire", 3, 3, "Deal 3 damage if you are holding a knight", "knight", -168)],
                   [Creature(7, "Heavy Armored Knight", 4, 7, "If you're holding a knight deal 7 damage to a minion",
                             "knight",
                             -165)],
                   [Creature(3, "Motivated Page", 4, 2, "If you're holding a knight gain +1/+1", "knight",
                             -163)],
                   [Creature(4, "Knight's Trainee", 6, 2, "If you're holding a knight and gain +1 attack and guard",
                             "knight", -161)],
                   [Creature(7, "Empire Crusader", 7, 7, "Add 5 Holy Roman Empire cards to your hand", "knight", -153)],
                   [Creature(10, "Margrave", 6, 4, "Guard Armored Cost 1 less for other each card in your hand",
                             "knight", -126)],
                   [Creature(1, "Heretic Knight", 1, 2, "Armored deal 2 damage to your kingdom", "knight", -122)],
                   [Creature(2, "Armored Knight", 2, 2, "Armored", "knight", -87)],
                   [Creature(1, "Selfless Knight", 1, 2, "Desperate Give a friendly minion armored", "knight", -86)],
                   [Creature(8, "Frederick Barbarossa", 6, 6,
                             "Friendly minions get armored and +1/+1 Armored Guard", "knight", -72)],
                   [Creature(5, "Army Champion", 4, 4,
                             "While this is on the field friendly minions get +1/+1", "knight", -69)],
                   [Creature(4, "Last Defender", 6, 2, "If your hand is empty gain +2 attack and guard", "knight",
                             -55)],
                   [Creature(3, "Tournament Horserider", 1, 2, "Charge Armored", "knight", -53)],
                   [Creature(1, "Armored Page", 1, 1, "Armored", "knight", -51)],
                   [Creature(7, "Cataphract", 6, 6, "Guard Armored", "knight", -39)],
                   [Creature(8, "Richard the Lionheart", 6, 6, "Draw a Spell and a Creature Guard", "knight", -21)],
                   [Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2 Armored", "knight", -11)],
                   [Creature(2, 'Page', 1, 1, "Draw a card", "knight", -10)],
                   [Creature(2, 'Squire', 2, 3, "", "knight", -9)],
                   [Creature(5, "Mounted Knight", 4, 4, "Charge", "knight", -8)],
                   [Creature(7, 'Teutonic Knight', 6, 5, "Guard Armored", "knight", -4)],
                   [Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", "knight", -3)],
                   [Creature(6, 'Templar Knight', 7, 5, "Guard", "knight", -2)],
                   [Creature(6, "Inspiring knight", 5, 6,
                             "Desperate add a random knight to your hand", "knight",
                             -169)],
                   [Creature(8, "Snob Knight", 10, 6, "", "Knight", -170)]]
list_of_mercenary = [
    [Creature(2, "Mercenary Recruiter", 2, 2, "Draw a mercenary", "mercenary", -132)],
    [Creature(4, "Mercenary defender", 5, 2, "Guard put an 3/2 defence", "mercenary", -133)],
    [Creature(1, "Mercenary employer", 2, 1, "Add a random mercenary to your hand", "mercenary", -148)],
    [Creature(2, "Mercenary Charger", 3, 2,
              "If you're holding a knight and gain +1 attack and charge", "mercenary",
              -162)],
    [Creature(3, "Mercenary Lieutenant", 3, 3, "Desperate deal 1 damage to all minions", "mercenary",
              -177)],
    [Creature(2, "Inspiring mercenary", 2, 2, "Guard Desperate give all guards +1/+1", "mercenary", -178)]
]
list_of_debt_card = [[Spell(2, "Ancient Empire", "Draw 2 cards Debt(1)", -43)],
                     [Spell(3, "Boarder Guards", "Summon 2 Akritoi Debt(1)", -68)],
                     [Spell(1, "Roman Formation Phalanx", "Give your minions +1/+1 Debt(1)", -71)],
                     [Creature(5, "Protokentarchos", 4, 4, "Give a friendly minion +3/+3 Debt(1)", "soldier", -77)],
                     [Creature(4, "Mercenary Champion", 7, 7, "Debt(2)", "soldier", -135)],
                     [Creature(2, "Mercenary soldier", 4, 3, "Debt(1)", "soldier", -136)],
                     [Creature(5, "Mercenary elite Defender", 8, 7, "Guard Debt(2)", "soldier", -137)],
                     [Creature(4, "Mercenary Herbalist", 6, 4, "Restore 6 health Debt(1)", "worker", -138)],
                     [Defence(5, "Mercenary's Troops", 2, 8, "Debt(2)", -139)],
                     [Spell(1, "Pilum Throw", "Deal 3 damage Debt(1)", -83)]]
list_of_soldier = [[Creature(9, "Sleepy Guard", 12, 4, "Guard", "soldier", -147)],
                   [Creature(1, "Banner holder", 2, 1, "Give your hand +1 health", "soldier", -146)],
                   [Creature(5, "Mercenary elite Defender", 8, 7, " Guard Debt(2)", "soldier", -137)],
                   [Creature(2, "Mercenary soldier", 4, 3, "Debt(1)", "soldier", -136)],
                   [Creature(4, "Mercenary Champion", 7, 7, "Debt(2)", "soldier", -135)],
                   [Creature(3, "Bailiff", 3, 3, "Set a minion attack to 1", "soldier", -129)],
                   [Creature(3, "Voice of the emperor", 4, 3, "Set a minion attack and health to 3", "soldier", -128)],
                   [Creature(9, "Graf", 6, 3,
                             "Guard Armored Desperate Summon 3 Armored Peasant with guard and armored", "soldier",
                             -125)],
                   [Creature(2, "Armored Peasant", 2, 1, "Armored Guard", "soldier", -123)],
                   [Creature(1, "New Recruit", 2, 1, "When you play a soldier give this +1 attack", "soldier", -120)],
                   [Creature(6, "Khevtuul", 5, 7, "Desperate summon 2 2/2 Night Watchers", "soldier", -93)],
                   [Creature(6, "Joan of Arc", 2, 2, "Desperate Summ 7/8 Saint Joan of Arc with charge and armored",
                             "soldier", -90)],
                   [Creature(5, "Front Line Defender", 6, 3,
                             "Desperate Summ a 1/2 Second Line Defender with Guard Guard", "soldier", -89)],
                   [Creature(9, "Jochi", 8, 8, "Charge", "soldier", -78)],
                   [Creature(5, "Protokentarchos", 4, 4, "Give a friendly minion +3/+3 Debt(1)", "soldier", -77)],
                   [Creature(8, "Basil II", 6, 5, "Armored Charge Guard", "soldier", -76)],
                   [Creature(1, "Faithful Protector", 1, 1, "Guard Armored", "soldier", -62)],
                   [Creature(3, "Drummer", 2, 2, "Give your hand +1/+1", "soldier", -56)],
                   [Creature(1, "Archer", 1, 1, "Deal 1 damage", "soldier", -50)],
                   [Creature(3, "Rider", 2, 3, "Charge", "soldier", -45)],
                   [Creature(3, "Faithful Guard", 2, 2, "Guard Armored", "soldier", -42)],
                   [Creature(3, "Akritoi", 3, 2, "Guard", "soldier", -38)],
                   [Creature(4, "Pronoiar", 3, 3, "Charge", "soldier", -37)],
                   [Creature(4, "City Guard", 5, 3, "Guard", "soldier", -24)],
                   [Creature(2, "Army Recruiter", 3, 2, "Add a random soldier to your hand", "soldier", -151)]
                   ]
list_of_animals = [[Creature(9, "Wild Elephant", 7, 9, "Deal 4 damage", "animal", -142)],
                   [Creature(3, "Big Game Beast", 3, 3, "Desperate draw an animal", "animal", -130)],
                   [Creature(2, "Goat", 1, 1, "Desperate summon a 3/2 Hungry Wolf", "animal", -98)],
                   [Creature(1, "Domestic cat", 1, 1, "Summon a 1/1 Wild Cat", "animal", -97)],
                   [Creature(4, "Mother Wolf", 3, 3, "Desperate summ 2 1/1 Wolf Pup", "animal", -96)],
                   [Creature(2, "Armored Horse", 1, 2, "Armored Desperate Draw a Spell", "animal", -88)],
                   [Creature(2, "Lost Sheep", 1, 1, "Desperate Summon 2 1/1 Wild Wolf", "animal", -81)],
                   [Creature(2, "Wild Horse", 2, 1, "Draw a charge card", "animal", -59)],
                   [Creature(1, "Wolf", 1, 1, "Charge", "animal", -49)],
                   [Creature(2, "Hunting dog", 1, 2, "Charge", "animal", -30)],
                   [Creature(6, "War elephant", 5, 4,
                             "While this is on the field your creatures have +1 attack", "animal", -20)],
                   [Creature(2, "Guard Dog", 2, 2, "Guard", "animal", -18)],
                   [Creature(1, "Lure animal", 1, 1, "Desperate add a random animal to your hand", "animal", -152)],
                   [Creature(8, "Alpha Wolf", 7, 7, "Desperate summon 7 1/1 Wolf", "animal", -171)],
                   [Creature(3, "Lost Chicken", 3, 0, "Desperate summon a 5/5 Lynx", "animal", -172)],
                   ]
list_of_creatures_to_pick = {"mercenary": list_of_mercenary, "debt": list_of_debt_card, "soldier": list_of_soldier,
                             "animal": list_of_animals, "holy_roman": list_of_holy_roman, "knights": list_of_knights}
cards_for_byzantine_empire.extend(cards_that_are_in_the_game_for_all)
cards_for_holy_roman_empire.extend(cards_that_are_in_the_game_for_all)
cards_for_mongol_empire.extend(cards_that_are_in_the_game_for_all)
mesopotamia_empire.extend(cards_that_are_in_the_game_for_all)
roman_empire.extend(cards_that_are_in_the_game_for_all)
best_cards_so_far_deck = []
power_of_the_people = [Creature(8, "Frederick Barbarossa", 6, 6,
                                "Friendly minions get armored and +1/+1 Armored Guard", "knight", 911),
                       Creature(6, "Joan of Arc", 2, 2, "Desperate Summ 7/8 Saint Joan of Arc with charge and armored",
                                "worker", 912),
                       Creature(3, "Faithful Guard", 2, 2, "Guard Armored", "soldier", 913),
                       Creature(3, "Faithful Guard", 2, 2, "Guard Armored", "soldier", 914),
                       Creature(1, "Faithful Protector", 1, 1, "Guard Armored", "soldier", 915),
                       Creature(1, "Selfless Knight", 1, 2, "Desperate Give a friendly minion armored", "knight", 916),
                       Spell(4, "Arbalest Shot", "Deal 3 damage and draw a card", 917),
                       Creature(1, "Faithful Protector", 1, 1, "Guard Armored", "soldier", 918),
                       Creature(2, "Armored Horse", 1, 2, "Armored Desperate Draw a Spell", "animal", 919),
                       Creature(5, "Front Line Defender", 6, 3,
                                "Desperate Summ a 1/2 Second Line Defender with Guard Guard", "soldier", 920),
                       Creature(5, "Front Line Defender", 6, 3,
                                "Desperate Summ a 1/2 Second Line Defender with Guard Guard", "soldier", 921),
                       Creature(11, "Covered Battering Ram", 8, 8, "Cost 1 less for each minion on the battlefield",
                                "machine", 922),
                       Spell(9, "Call of God", "Heal for 8 and summon a 8/8 armored guard Crusader", 923),
                       Spell(4, "Arbalest Shot", "Deal 3 damage and draw a card", 924),
                       Creature(10, "Margrave", 6, 4, "Guard Armored Cost 1 less for other each card in your hand",
                                "knight", 925),
                       Creature(10, "Margrave", 6, 4, "Guard Armored Cost 1 less for other each card in your hand",
                                "knight", 926),
                       Creature(11, "Covered Battering Ram", 8, 8, "Cost 1 less for each minion on the battlefield",
                                "machine", 927),
                       Spell(2, "Warhammer", "Break an enemy armor making him lose all attributes", 928),
                       Creature(5, "Bishop", 2, 2, "Give a friendly minion +4/+4 and guard", "worker", 929),
                       Spell(5, "Call of the Emperor", "Draw 3 cards and reduce there mana cost by 1", 930),
                       Creature(6, "Rich Peasant", 1, 2, "Summon 2 armored Peasant with guard and armored", "worker",
                                931),
                       Spell(7, "Rain of Arrows", "Destroy ALL minions that are not Armored", 932),
                       Creature(9, "Graf", 6, 3,
                                "Guard Armored Desperate Summon 3 Armored Peasant with guard and armored", "soldier",
                                933),
                       Spell(9, "Call of God", "Heal for 8 and summon a 8/8 armored guard Crusader", 934),
                       Creature(6, "Rich Peasant", 1, 2, "Summon 2 armored Peasant with guard and armored", "worker",
                                935),
                       Creature(3, "Drummer", 2, 2, "Give your hand +1/+1", "soldier", 936),
                       Spell(7, "Rain of Arrows", "Destroy ALL minions that are not Armored", 937),
                       Creature(3, "Bailiff", 3, 3, "Set a minion attack to 1", "soldier", 938),
                       Creature(2, "Armored Knight", 2, 2, "Armored", "knight", 939),
                       Creature(9, "Graf", 6, 3,
                                "Guard Armored Desperate Summon 3 Armored Peasant with guard and armored", "soldier",
                                940),
                       ]
defenders = [Creature(5, "Mercenary elite Defender", 8, 7, "Guard Debt(2)", "soldier", 100),
             Creature(2, "Akritoi", 3, 2, "Guard", "soldier", 101),
             Creature(5, "Mercenary elite Defender", 8, 7, "Guard Debt(2)", "soldier", 102),
             Creature(2, "Watchtower", 2, 1, "All your guards get +1/+2", "building", 103),
             Creature(2, "Watchtower", 2, 1, "All your guards get +1/+2", "building", 104),
             Spell(2, "Ancient Empire", "Draw 2 cards Debt(1)", 105),
             Creature(1, "Mercenary emissary", 1, 2, "Add a random debt to your hand", "worker", 106),
             Creature(2, "Akritoi", 3, 2, "Guard", "soldier", 107),
             Creature(7, "Cataphract", 6, 6, "Guard Armored", "knight", 108),
             Creature(7, "Cataphract", 6, 6, "Guard Armored", "knight", 109),
             Spell(2, "Roman Formation Circular", "Give your minions on the filed Guard", 110),
             Creature(6, 'Templar Knight', 7, 5, "Guard", "knight", 111),
             Spell(2, "Ancient Empire", "Draw 2 cards Debt(1)", 112),
             Spell(3, "Strength in numbers", "Give a minion +2/+3 and draw a creature", 113),
             Creature(6, "Joan of Arc", 2, 2, "Desperate Summ 7/8 Saint Joan of Arc with charge and armored", "worker",
                      114),
             Creature(8, "Richard the Lionheart", 6, 6, "Draw a Spell and a Creature Guard", "knight", 115),
             Spell(7, "Landslide", "Deal 7 damage to ALL minions", 116),
             Spell(3, "Boarder Guards", "Summon 2 Akritoi Debt(1)", 117),
             Creature(5, "Mercenary elite Defender", 8, 7, "Guard Debt(2)", "soldier", 119),
             Creature(8, "Basil II", 6, 5, "Armored Charge Guard", "soldier", 120),
             Spell(5, "Kill", "Kill an enemy minion", 121),
             Creature(4, "Mercenary Herbalist", 6, 4, "Restore 6 health Debt(1)", "worker", 122),
             Creature(2, "Wealthy Nobel", 2, 3, "Pays all debt", "worker", 123),
             Creature(4, "Mercenary Champion", 7, 7, "Debt(2)", "soldier", 124),
             Creature(2, "Wealthy Nobel", 2, 3, "Pays all debt", "worker", 125),
             Creature(5, "Bishop", 2, 2, "Give a friendly minion +4/+4 and guard", "worker", 126),
             Creature(5, "Protokentarchos", 4, 4, "Give a friendly minion +3/+3 Debt(1)", "soldier", 127),
             Creature(5, "Front Line Defender", 6, 3,
                      "Desperate Summ a 1/2 Second Line Defender with Guard Guard", "soldier", 128),
             Creature(2, "Watchman", 2, 1, "Draw a guard card", "worker", 129),
             Spell(1, "Roman Formation Phalanx", "Give your minions +1/+1 Debt(1)", 130),
             ]
ancients = [Creature(1, "City Gate Guard", 3, 1, "Guard", "ancient", 150),
            Spell(3, "Ancient Tactics", "Draw 3 cards deal 3 damage to your kingdom", 151),
            Creature(1, "Mesopotamia Scholar", 1, 2, "Draw a card Deal 2 damage to your kingdom", "ancient", 152),
            Creature(1, "City Gate Guard", 3, 1, "Guard", "ancient", 153),
            Spell(3, "Ancient Tactics", "Draw 3 cards deal 3 damage to your kingdom", 154),
            Creature(1, "Mesopotamia Scholar", 1, 2, "Draw a card Deal 2 damage to your kingdom", "ancient", 155),
            Creature(5, "Front Line Defender", 6, 3,
                     "Desperate Summ a 1/2 Second Line Defender with Guard Guard", "soldier", 156),
            Creature(5, "Front Line Defender", 6, 3,
                     "Desperate Summ a 1/2 Second Line Defender with Guard Guard", "soldier", 157),
            Creature(11, "Covered Battering Ram", 8, 8, "Cost 1 less for each minion on the battlefield",
                     "machine", 158),
            Creature(10, "Battering Ram", 8, 8, "Cost 1 less for each friendly minion on the battlefield", "machine",
                     159),
            Creature(12, "Trebuchet", 8, 8, "Cost 1 less for each other card in your hand", "machine", 160),
            Creature(8, "Richard the Lionheart", 6, 6, "Draw a Spell and a Creature Guard", "knight", 161),
            Creature(12, "Trebuchet", 8, 8, "Cost 1 less for each other card in your hand", "machine", 162),
            Creature(2, "Goat", 1, 1, "Desperate summon a 3/2 Hungry Wolf", "animal", 163),
            Creature(3, "Tournament Horserider", 1, 2, "Charge Armored", "knight", 164),
            Creature(3, "Tournament Horserider", 1, 2, "Charge Armored", "knight", 165),
            Creature(6, "Joan of Arc", 2, 2, "Desperate Summ 7/8 Saint Joan of Arc with charge and armored",
                     "soldier", 166),
            Creature(9, "King Saragon of Akkad", 7, 9,
                     "Give all ancients +2/+2 your knigdom can't take damage", "ancient", 167),
            Creature(2, "Military Guard", 4, 2, "Guard Deal 2 damage to your kingdom", "ancient", 168),
            Creature(2, "Military Guard", 4, 2, "Guard Deal 2 damage to your kingdom", "ancient", 169),
            Creature(11, "Covered Battering Ram", 8, 8, "Cost 1 less for each minion on the battlefield",
                     "machine", 170),
            Creature(1, "Lu", 2, 3, "Deal 2 damage to your kingdom", "ancient", 171),
            Spell(4, "Mercenaries Reinforcements", "Deal 2-4 damage and summ that many Man at arms", 172),
            Spell(4, "Mercenaries Reinforcements", "Deal 2-4 damage and summ that many Man at arms", 173),
            Spell(8, "Epidemic", "Destroy ALL minions", 174),
            Creature(5, "Assyrian Horserider", 7, 5, "Charge discard 2 cards from your hand", "ancient", 175),
            Spell(6, "Tactical Coordination", "When you discard or use this draw 3 cards", 176),
            Creature(9, "Turtanu", 9, 3, "Guard Desperate Summon 3 City Gate Guards", "ancient", 177),
            Creature(3, "Prisoner of War", 4, 3, "If you discard this summon it", "ancient", 178),
            Creature(5, "Assyrian Horserider", 7, 5, "Charge discard 2 cards from your hand", "ancient", 179),
            Creature(1, "Lu", 2, 3, "Deal 2 damage to your kingdom", "ancient", 180),
            ]
insane_deck = [Creature(1, "Archer", 1, 1, "Deal 1 damage", "soldier", 9991),
               Creature(1, "Archer", 1, 1, "Deal 1 damage", "soldier", 9992),
               Creature(2, "Lost Shield", 2, 0, "Desperate Sumon a 4/4 City guard", "item", -82),
               Creature(2, "Lost Shield", 2, 0, "Desperate Sumon a 4/4 City guard", "item", -82),
               Creature(0, "Peasant", 1, 1, "", "worker", 9995),
               Creature(0, "Peasant", 1, 1, "", "worker", 9996),
               Creature(3, "Priest", 1, 1,
                        "Restore a friendly minion to full HP and give it +1/+1", "worker",
                        9997),
               Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", "knight", 9998),
               Creature(2, 'Squire', 2, 3, "", "knight", 9999),
               Creature(2, 'Page', 1, 1, "Draw a card", "knight", 10000),
               Creature(2, 'Squire', 2, 3, "", "knight", 10001),
               Creature(2, 'Page', 1, 1, "Draw a card", "knight", 10002),
               Defence(1, "Empire Peasants", 1, 4, "", 10003),
               Creature(2, "Guard Dog", 2, 2, "Guard", "animal", 10004),
               Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", "worker", 10006),
               Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", "worker", 10005),
               Creature(3, "Personal instructor", 3, 2, "Give a friendly minion +1/+1", "worker", 10006),
               Creature(4, "Last Defender", 6, 2, "If your hand is empty gain +2 attack and guard", "knight",
                        10007),
               Creature(3, "Personal instructor", 3, 2, "Give a friendly minion +1/+1", "worker", 10008),
               Creature(4, "Last Defender", 6, 2, "If your hand is empty gain +2 attack and guard", "knight",
                        10009),
               Spell(2, "Bandages", "Restore a friendly minion to full HP", 10011),
               Spell(1, "Personal Guard", "Give a minion guard and draw a card", 10012),
               Spell(2, "Bandages", "Restore a friendly minion to full HP", 10013),
               Spell(1, "Personal Guard", "Give a minion guard and draw a card", 10014),
               Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", "worker", 10015),
               Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", "worker", 10016),
               Creature(7, 'Teutonic Knight', 6, 5, "Guard Armored", "knight", 10017),
               Creature(7, 'Teutonic Knight', 6, 5, "Guard Armored", "knight", 10018),
               Spell(1, "Arrow shot", "Deal 2 damage to a enemy", 10019),
               Spell(5, "Kill", "Kill an enemy minion", 10020),
               ]

dict_of_decks = {"best_cards_so_far_deck": best_cards_so_far_deck, "demo_deck": demo_deck, "bot_deck": bot_deck,
                 "power_of_the_people": power_of_the_people, "cards_for_byzantine_empire": cards_for_byzantine_empire,
                 "cards_for_mongol_empire": cards_for_mongol_empire, "defenders": defenders,
                 "mongols_hordes": mongols_hordes, "ancients": ancients, "insane_deck": insane_deck,
                 }
empire_decks = {'Byzantine_Empire': cards_for_byzantine_empire,
                'Holy_Roman_Empire': cards_for_holy_roman_empire,
                'Mongol_Empire': cards_for_mongol_empire,
                "Mesopotamia_Empire": mesopotamia_empire,
                "Roman_Empire": roman_empire
                }
