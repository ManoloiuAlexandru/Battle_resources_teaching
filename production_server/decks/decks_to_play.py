from clases.Item import Item
from clases.creatures import Creature
from clases.spells import Spell

bot_deck = [Creature(7, 'Templar Knight', 7, 5, "Guard", 3323),
            Creature(2, 'Page', 1, 1, "Draw a card", 13324),
            Creature(2, 'Page', 1, 1, "Draw a card", 3324),
            Creature(2, "Hunting dog", 1, 2, "Charge", 89009),
            # Creature(2, "Hunting dog", 1, 2, "Charge", -30),
            # Creature(2, 'Squire', 2, 3, "", 3325),
            # Creature(2, 'Squire', 2, 3, "", 13325),
            Creature(5, "Mounted Knight", 4, 4, "Charge", 3326),
            # Creature(5, "Mounted Knight", 4, 4, "Charge", 13326),
            Creature(7, 'Templar Knight', 7, 5, "Guard", 3328),
            # Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2", 3329),
            # Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2", 3330),
            Creature(6, 'Teutonic Knight', 7, 6, "", 3332),
            # Creature(6, 'Teutonic Knight', 7, 6, "", 13332),
            # Item(2, "Knight's Equipment", "Give a creature +2/+2", 4443),
            Item(2, "Knight's Equipment", "Give a creature +2/+2", 4442),
            # Spell(1, "Personal Guard", "Give a minion guard and draw a card", 3334),
            Spell(1, "Personal Guard", "Give a minion guard and draw a card", 43334),
            Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", 7),
            # Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", 8),
            Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", 3320),
            Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", 3321),
            # Spell(3, "Volley", "Deal 2 damage to all enemies", 3339),
            Spell(3, "Volley", "Deal 2 damage to all enemies", 13339),
            # Spell(1, "Arrow shot", "Deal 2 damage to a enemy", 3338),
            Spell(1, "Arrow shot", "Deal 2 damage to a enemy", 13338),
            Spell(5, "Kill", "Kill an enemy minion", 3337),
            Spell(5, "Kill", "Kill an enemy minion", 3338),
            # Spell(2, "Bandages", "Restore a friendly minion to full HP", 3370),
            # Spell(2, "Bandages", "Restore a friendly minion to full HP", 3377),
            # Spell(1, "Bandage", "Heal a friendly minion for 4", 3355),
            # Spell(1, "Bandage", "Heal a friendly minion for 4", 3356),
            # Item(1, "Shield", "Give a creature +0/+2 and Guard", 4445),
            # Item(1, "Shield", "Give a creature +0/+2 and Guard", 14445),
            Creature(3, "Priest", 1, 1, "Restore a friendly minion to full HP and give it +1/+1", 4567),
            Creature(3, "Priest", 1, 1, "Restore a friendly minion to full HP and give it +1/+1", 5678),
            # Creature(2, "Guard Dog", 2, 2, "Guard", 989),
            # Creature(2, "Guard Dog", 2, 2, "Guard", 900),
            Spell(8, "Bodyguards", "Summon  2 Guards from your deck", 786781),
            # Spell(8, "Bodyguards", "Summon  2 Guards from your deck", 67861),
            # Spell(3, "Horse riding lessons",  "Give a friendly creature charge and +2 attack", 4281),
            Spell(3, "Horse riding lessons", "Give a friendly creature charge and +2 attack", 44281),
            Creature(8, "Frederick Barbarossa", 8, 8, "While Barbarossa is on the field enemy minions get -2/0",
                     99283),
            Creature(8, "Richard the Lionheart", 7, 7,
                     "While Richard the Lionheart is on the filed your minions get +1/+1", 98933),
            Spell(3, "Feudal Obligations", "Draw 2 cards", 65758),
            Spell(3, "Feudal Obligations", "Draw 2 cards", 123456),
            Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 4571),
            Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 2885),
            # Spell(8, "Black Death", "Destroy ALL minions", 14568),
            Spell(8, "Black Death", "Destroy ALL minions", 8924),
            # Item(2, "Leather Armor", "Give a creature +0/+3", 7474789),
            Item(2, "Leather Armor", "Give a creature +0/+3", 6474789),
            # Item(2, "Cloth Armor", "Give a creature +0/+1 and Charge", 957106),
            # Item(2, "Plate Armor", "Give a creature Armored", 1650267),
            # Item(1, "Dagger", "Give a creature +2/+0", 1876590),
            Creature(1, "Church Scholar", 2, 1, "Evrey time a creature is healed gain +1/+1 ", 54578),
            # Creature(1, "Church Scholar", 2, 1, "Evrey time a creature is healed gain +1/+1 ", 61290),
            # Spell(3, "Knight's training", "Give a minions +3/+3", 473561),
            Spell(3, "Knight's training", "Give a minions +3/+3", 878892),
            ]
demo_deck = [
    Creature(0, "Andras", 99, 1, "Charge", 0),
    Creature(0, "Andras", 99, 1, "Charge", 1)

]
to_be_added_in_game = [Spell(5, "In the name of the king", "All friendly minions get +1/+1", 1002),
                       Spell(0, "Blood price", "Take 5 dmg and gaine 3 mana", 1004),
                       Spell(3, "Long march", "All enemies are exhausted", 1005),
                       Creature(9, "Heavy Cavalary", 9, 9, "Takes 2 less dmg from attacks", 1006),
                       Creature(2, "Bodyguard", 1, 1, "Guard", 1010),
                       Creature(4, "Bear", 4, 4, "", 1011),
                       Creature(3, "Woolf", 3, 3, "", 1012),
                       Item(4, "Banner", "While on a minion all minions get +1/+1", 1014),
                       Creature(4, "Merchant", 2, 4, "For the next 2 turns gain 1 mana each turn", 1014),
                       ]
cards_that_are_in_the_game_for_all = [Creature(0, "Peasant", 1, 1, "", -1),
                                      Creature(7, 'Templar Knight', 7, 5, "Guard", -2),
                                      Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", -3),
                                      Creature(6, 'Teutonic Knight', 7, 6, "", -4),
                                      Spell(5, "Kill", "Kill an enemy minion", -7),
                                      Creature(5, "Mounted Knight", 4, 4, "Charge", -8),
                                      Creature(2, 'Squire', 2, 3, "", -9),
                                      Creature(2, 'Page', 1, 1, "Draw a card", -10),
                                      Creature(3, "Priest", 1, 1,
                                               "Restore a friendly minion to full HP and give it +1/+1",
                                               -15),
                                      Creature(2, "Guard Dog", 2, 2, "Guard", -18),
                                      Creature(8, "Richard the Lionheart", 7, 7,
                                               "While Richard the Lionheart is on the filed your minions get +1/+1",
                                               -21),
                                      Creature(2, "Miner", 3, 2, "", -23),
                                      Creature(4, "City Guard", 6, 4, "Guard", -24),
                                      Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", -31),
                                      Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", -33),
                                      Creature(1, "Church Scholar", 2, 1, "Evrey time a creature is healed gain +1/+1 ",
                                               -34),
                                      Creature(2, "Armorer", 2, 2, "Give a friendly minion armored", -39),
                                      Creature(1, "Wolf", 1, 1, "Charge", -49),
                                      Creature(1, "Archer", 1, 1, "Deal 1 damage", -50)
                                      ]
cards_for_byzantine_empire = [
    Spell(6, "Peace Treaty", "Return all creature form the battlefield to their owners hands.", -36),
    Creature(4, "Pronoiar", 3, 3, "Charge", -37),
    Creature(2, "Akritoi", 3, 2, "Guard", -38),
    Creature(6, "Cataphract", 6, 6, "Guard Armored", -39),
    Spell(5, "Wealthy Empire", "Summon 2 random cards from your deck", -40),
    Item(1, "Shield", "Give a creature +0/+2 and Guard", -16),
    Spell(3, "Ancient Empire", "Draw 2 cards", -43),
]
cards_for_holy_roman_empire = [
    Creature(8, "Frederick Barbarossa", 8, 8,
             "While Barbarossa is on the field enemy minions get -2/0", -20),
    Creature(3, "Scribe", 3, 0, "At the end of your turn draw a card", -41),
    Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2 Armored",
             -11),
    Spell(1, "Bandage", "Heal a friendly minion for 4", -12),
    Spell(2, "Bandages", "Restore a friendly minion to full HP", -13),
    Spell(1, "Personal Guard", "Give a minion guard and draw a card", -14),
    Item(2, "Knight's Equipment", "Give a creature +2/+2", -17),
    Spell(3, "Knight's training", "Give a minions +3/+3", -35),
    Spell(8, "Black Death", "Destroy ALL minions", -32),
    Spell(3, "Feudal Obligations", "Draw 2 cards", -29),
    Item(2, "Plate Armor", "Give a creature Armored", -27),
    Item(1, "Dagger", "Give a creature +2/+0", -28),
    Spell(8, "Bodyguards", "Summon  2 Guards from your deck", -22),
    Creature(3, "Faithful Guard", 2, 2, "Guard Armored", -42),
    Spell(5, "Call of the Emperor", "Draw 3 cards and reduce there mana cost by 1", -47),
    Spell(4, "Arbalest Shot", "Deal 3 damage and draw a card", -48)
]
cards_for_mongol_empire = [Spell(3, "Volley", "Deal 2 damage to all enemies", -5),
                           Spell(1, "Arrow shot", "Deal 2 damage to a enemy", -6),
                           Creature(2, "Hunting dog", 1, 2, "Charge", -30),
                           Item(2, "Leather Armor", "Give a creature +0/+3 and draw a card", -25),
                           Item(2, "Cloth Armor", "Give a creature +0/+1 and Charge", -26),
                           Spell(3, "Horse riding lessons", "Give a friendly creature charge and +2 attack",
                                 -19),
                           Creature(3, "Hunter", 2, 2, "Summon a 1/1 Dog", -44),
                           Creature(3, "Rider", 2, 4, "Charge", -45),
                           Spell(2, "Call of the Khan", "Draw a card if it has Charge reduce the cost to 0", -46)
                           ]
all_cards_in_game = [Creature(0, "Peasant", 1, 1, "", -1),
                     Creature(7, 'Templar Knight', 7, 5, "Guard", -2),
                     Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", -3),
                     Creature(6, 'Teutonic Knight', 7, 6, "", -4),
                     Spell(3, "Volley", "Deal 2 damage to all enemies", -5),
                     Spell(1, "Arrow shot", "Deal 2 damage to a enemy", -6),
                     Spell(5, "Kill", "Kill an enemy minion", -7),
                     Creature(5, "Mounted Knight", 4, 4, "Charge", -8),
                     Creature(2, 'Squire', 2, 3, "", -9),
                     Creature(2, 'Page', 1, 1, "Draw a card", -10),
                     Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2 Armored", -11),
                     Spell(1, "Bandage", "Heal a friendly minion for 4", -12),
                     Spell(2, "Bandages", "Restore a friendly minion to full HP", -13),
                     Spell(1, "Personal Guard", "Give a minion guard and draw a card", -14),
                     Creature(3, "Priest", 1, 1,
                              "Restore a friendly minion to full HP and give it +1/+1",
                              -15),
                     Item(1, "Shield", "Give a creature +0/+2 and Guard", -16),
                     Item(2, "Knight's Equipment", "Give a creature +2/+2", -17),
                     Creature(2, "Guard Dog", 2, 2, "Guard", -18),
                     Spell(3, "Horse riding lessons", "Give a friendly creature charge and +2 attack",
                           -19),
                     Creature(8, "Frederick Barbarossa", 8, 8,
                              "While Barbarossa is on the field enemy minions get -2/0", -20),
                     Creature(8, "Richard the Lionheart", 7, 7,
                              "While Richard the Lionheart is on the filed your minions get +1/+1",
                              -21),
                     Spell(8, "Bodyguards", "Summon  2 Guards from your deck", -22),
                     Creature(2, "Miner", 3, 2, "", -23),
                     Creature(4, "City Guard", 6, 4, "Guard", -24),
                     Item(2, "Leather Armor", "Give a creature +0/+3 and draw a card", -25),
                     Item(2, "Cloth Armor", "Give a creature +0/+1 and Charge", -26),
                     Item(2, "Plate Armor", "Give a creature Armored", -27),
                     Item(1, "Dagger", "Give a creature +2/+0", -28),
                     Spell(3, "Feudal Obligations", "Draw 2 cards", -29),
                     Creature(2, "Hunting dog", 1, 2, "Charge", -30),
                     Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", -31),
                     Creature(4, "Pronoiar", 3, 3, "Charge", -37),
                     Creature(3, "Akritoi", 3, 2, "Guard", -38),
                     Spell(8, "Black Death", "Destroy ALL minions", -32),
                     Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", -33),
                     Creature(1, "Church Scholar", 2, 1, "Evrey time a creature is healed gain +1/+1 ",
                              -34),
                     Spell(3, "Knight's training", "Give a minions +3/+3", -35),
                     Spell(6, "Peace Treaty", "Return all creature form the battlefield to their owners hands.", -36),
                     Creature(6, "Cataphract", 6, 6, "Guard Armored", -39),
                     Creature(2, "Armorer", 2, 2, "Give a friendly minion armored", -39),
                     Spell(5, "Wealthy Empire", "Summon 2 random cards from your deck", -40),
                     Creature(3, "Scribe", 3, 0, "At the end of your turn draw a card", -41),
                     Creature(3, "Faithful Guard", 2, 2, "Guard Armored", -42),
                     Spell(3, "Ancient Empire", "Draw 2 cards", -43),
                     Creature(3, "Hunter", 2, 2, "Summon a 1/1 Dog", -44),
                     Creature(3, "Rider", 2, 4, "Charge", -45),
                     Spell(2, "Call of the Khan", "Draw a card if it has Charge reduce the cost to 0", -46),
                     Spell(5, "Call of the Emperor", "Draw 3 cards and reduce there mana cost by 1", -47),
                     Spell(4, "Arbalest shot", "Deal 3 damage and draw a card", -48),
                     Creature(1, "Wolf", 1, 1, "Charge", -49),
                     Creature(1, "Archer", 1, 1, "Deal 1 damage", -50)
                     ]
mongols_hordes = [Spell(3, "Volley", "Deal 2 damage to all enemies", 1900),
                  Spell(3, "Volley", "Deal 2 damage to all enemies", 1901),
                  Spell(1, "Arrow shot", "Deal 2 damage to a enemy", 1902),
                  Spell(1, "Arrow shot", "Deal 2 damage to a enemy", 1903),
                  Creature(2, "Hunting dog", 1, 2, "Charge", 1904),
                  Creature(2, "Hunting dog", 1, 2, "Charge", 1905),
                  Item(2, "Leather Armor", "Give a creature +0/+3 and draw a card", 1906),
                  Item(2, "Leather Armor", "Give a creature +0/+3 and draw a card", 1907),
                  Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 1908),
                  Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 1909),
                  Spell(3, "Horse riding lessons", "Give a friendly creature charge and +2 attack",
                        1910),
                  Spell(3, "Horse riding lessons", "Give a friendly creature charge and +2 attack",
                        1911),
                  Creature(3, "Rider", 2, 4, "Charge", 1912),
                  Creature(3, "Rider", 2, 4, "Charge", 1913),
                  Creature(5, "Mounted Knight", 4, 4, "Charge", 1914),
                  Creature(5, "Mounted Knight", 4, 4, "Charge", 1915),
                  Creature(2, "Guard Dog", 2, 2, "Guard", 1916),
                  Creature(2, "Guard Dog", 2, 2, "Guard", 1917),
                  Spell(5, "Kill", "Kill an enemy minion", 1918),
                  Spell(5, "Kill", "Kill an enemy minion", 1919),
                  Spell(2, "Call of the Khan", "Draw a card if it has Charge reduce the cost to 0", 1920),
                  Spell(2, "Call of the Khan", "Draw a card if it has Charge reduce the cost to 0", 1921),
                  Creature(3, "Hunter", 2, 2, "Summon a 1/1 Dog", 1922),
                  Creature(3, "Hunter", 2, 2, "Summon a 1/1 Dog", 1923),
                  Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", 1924),
                  Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", 1925),
                  Creature(2, 'Squire', 2, 3, "", 1926),
                  Creature(2, 'Squire', 2, 3, "", 1927),
                  Creature(2, 'Page', 1, 1, "Draw a card", 1928),
                  Creature(2, 'Page', 1, 1, "Draw a card", 1929),
                  ]
cards_for_byzantine_empire.extend(cards_that_are_in_the_game_for_all)
cards_for_holy_roman_empire.extend(cards_that_are_in_the_game_for_all)
cards_for_mongol_empire.extend(cards_that_are_in_the_game_for_all)
best_cards_so_far_deck = [Creature(7, 'Templar Knight', 7, 5, "Guard", 991),
                          Creature(7, 'Templar Knight', 7, 5, "Guard", 992),
                          Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", 993),
                          Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", 994),
                          Spell(5, "Kill", "Kill an enemy minion", 995),
                          Spell(5, "Kill", "Kill an enemy minion", 996),
                          Creature(5, "Mounted Knight", 4, 4, "Charge", 997),
                          Creature(5, "Mounted Knight", 4, 4, "Charge", 998),
                          Creature(2, 'Page', 1, 1, "Draw a card", 999),
                          Creature(2, 'Page', 1, 1, "Draw a card", 9991),
                          Creature(8, "Frederick Barbarossa", 8, 8,
                                   "While Barbarossa is on the field enemy minions get -2/0", 9992),
                          Creature(8, "Richard the Lionheart", 7, 7,
                                   "While Richard the Lionheart is on the filed your minions get +1/+1", 9993),
                          Spell(8, "Bodyguards", "Summon  2 Guards from your deck", 9994),
                          Spell(8, "Bodyguards", "Summon  2 Guards from your deck", 9995),
                          Item(2, "Leather Armor", "Give a creature +0/+3 and draw a card", 9996),
                          Item(2, "Leather Armor", "Give a creature +0/+3 and draw a card", 9997),
                          Spell(3, "Feudal Obligations", "Draw 2 cards", 9998),
                          Spell(3, "Feudal Obligations", "Draw 2 cards", 9999),
                          Creature(2, "Hunting dog", 1, 2, "Charge", 99991),
                          Creature(2, "Hunting dog", 1, 2, "Charge", 99992),
                          Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 99993),
                          Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 99994),
                          Spell(8, "Black Death", "Destroy ALL minions", 99995),
                          Spell(8, "Black Death", "Destroy ALL minions", 99996),
                          Spell(1, "Personal Guard", "Give a minion guard and draw a card", 99997),
                          Spell(1, "Personal Guard", "Give a minion guard and draw a card", 99998),
                          Creature(2, "Guard Dog", 2, 2, "Guard", 9999991),
                          Creature(2, "Guard Dog", 2, 2, "Guard", 9999992),
                          Spell(3, "Volley", "Deal 2 damage to all enemies", 9999993),
                          Spell(1, "Arrow shot", "Deal 2 damage to a enemy", 9999994),
                          ]
power_of_the_people = [Creature(0, "Peasant", 1, 1, "", 911),
                       Creature(0, "Peasant", 1, 1, "", 912),
                       Creature(3, "Faithful Guard", 2, 2, "Guard Armored", 913),
                       Creature(3, "Faithful Guard", 2, 2, "Guard Armored", 914),
                       Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2 Armored", 915),
                       Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2 Armored", 916),
                       Spell(4, "Arbalest Shot", "Deal 3 damage and draw a card", 917),
                       Spell(5, "Call of the Emperor", "Draw 3 cards and reduce there mana cost by 1", 918),
                       Creature(2, 'Squire', 2, 3, "", 919),
                       Creature(2, 'Squire', 2, 3, "", 920),
                       Creature(2, 'Page', 1, 1, "Draw a card", 921),
                       Creature(2, 'Page', 1, 1, "Draw a card", 922),
                       Creature(3, "Priest", 1, 1,
                                "Restore a friendly minion to full HP and give it +1/+1",
                                923),
                       Spell(4, "Arbalest Shot", "Deal 3 damage and draw a card", 924),
                       Item(2, "Knight's Equipment", "Give a creature +2/+2", 925),
                       Creature(2, "Guard Dog", 2, 2, "Guard", 926),
                       Spell(8, "Black Death", "Destroy ALL minions", 927),
                       Item(2, "Knight's Equipment", "Give a creature +2/+2", 928),
                       Creature(2, "Guard Dog", 2, 2, "Guard", 929),
                       Spell(5, "Call of the Emperor", "Draw 3 cards and reduce there mana cost by 1", 930),
                       Creature(4, "City Guard", 6, 4, "Guard", 931),
                       Creature(4, "City Guard", 6, 4, "Guard", 932),
                       Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 933),
                       Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 934),
                       Spell(8, "Black Death", "Destroy ALL minions", 935),
                       Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", 936),
                       Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", 937),
                       Item(1, "Dagger", "Give a creature +2/+0", 938),
                       Item(1, "Dagger", "Give a creature +2/+0", 939),
                       Spell(3, "Feudal Obligations", "Draw 2 cards", 940),
                       ]
defenders = [Creature(4, "Pronoiar", 3, 3, "Charge", 100),
             Creature(2, "Akritoi", 3, 2, "Guard", 101),
             Creature(6, "Cataphract", 6, 6, "Guard Armored", 102),
             Spell(5, "Wealthy Empire", "Summon 2 random cards from your deck", 103),
             Item(1, "Shield", "Give a creature +0/+2 and Guard", 104),
             Spell(3, "Ancient Empire", "Draw 2 cards", 105),
             Creature(4, "Pronoiar", 3, 3, "Charge", 106),
             Creature(2, "Akritoi", 3, 2, "Guard", 107),
             Creature(6, "Cataphract", 6, 6, "Guard Armored", 108),
             Spell(5, "Wealthy Empire", "Summon 2 random cards from your deck", 109),
             Creature(7, 'Templar Knight', 7, 5, "Guard", 110),
             Creature(7, 'Templar Knight', 7, 5, "Guard", 111),
             Spell(3, "Ancient Empire", "Draw 2 cards", 112),
             Creature(2, "Guard Dog", 2, 2, "Guard", 113),
             Creature(2, "Guard Dog", 2, 2, "Guard", 114),
             Creature(2, 'Page', 1, 1, "Draw a card", 115),
             Creature(2, 'Page', 1, 1, "Draw a card", 116),
             Creature(2, "Armorer", 2, 2, "Give a friendly minion armored", 117),
             Creature(2, "Armorer", 2, 2, "Give a friendly minion armored", 118),
             Creature(4, "City Guard", 6, 4, "Guard", 119),
             Creature(4, "City Guard", 6, 4, "Guard", 120),
             Spell(5, "Kill", "Kill an enemy minion", 121),
             Spell(5, "Kill", "Kill an enemy minion", 122),
             Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 123),
             Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", 124),
             Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", 125),
             Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", 126),
             Creature(5, "Mounted Knight", 4, 4, "Charge", 127),
             Creature(5, "Mounted Knight", 4, 4, "Charge", 128),
             Creature(3, "Priest", 1, 1, "Restore a friendly minion to full HP and give it +1/+1", 129),
             ]
dict_of_decks = {"best_cards_so_far_deck": best_cards_so_far_deck, "demo_deck": demo_deck, "bot_deck": bot_deck,
                 "power_of_the_people": power_of_the_people, "cards_for_byzantine_empire": cards_for_byzantine_empire,
                 "cards_for_mongol_empire": cards_for_mongol_empire, "defenders": defenders,
                 "mongols_hordes": mongols_hordes}
empire_decks = {'Byzantine_Empire': cards_for_byzantine_empire,
                'Holy_Roman_Empire': cards_for_holy_roman_empire,
                'Mongol_Empire': cards_for_mongol_empire
                }
