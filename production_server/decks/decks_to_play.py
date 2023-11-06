from clases.Item import Item
from clases.creatures import Creature
from clases.spells import Spell

bot_deck = [Creature(7, 'Templar Knight', 5, 5, "Guard", 3323),
            Creature(1, 'Page', 1, 1, "", 3324),
            Creature(2, 'Squire', 2, 2, "", 3325),
            Creature(4, "Mounted Knight", 4, 4, "Charge", 3326),
            Creature(7, 'Templar Knight', 5, 5, "Guard", 3328),
            Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 3329),
            Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 3330),
            Creature(7, 'Teutonic Knight', 6, 5, "", 3332),
            Item(5, "Knight's Equipment", "Give a creature +2/+2", 4443),
            Item(5, "Knight's Equipment", "Give a creature +2/+2", 4442),
            Spell(3, "Personal Guard", "Give a soldier guard", 3334),
            Spell(3, "Personal Guard", "Give a soldier guard", 3335),
            Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 3320),
            Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 3321),
            Spell(3, "Volley", "Deal 1 damage to all enemies", 3339),
            Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 3338),
            Spell(5, "Kill", "Kill an enemy soldier", 3337),
            Spell(5, "Kill", "Kill an enemy soldier", 3338),
            Spell(4, "Bandages", "Restore a friendly soldier to full HP", 3370),
            Spell(4, "Bandages", "Restore a friendly soldier to full HP", 3377),
            Spell(3, "Bandage", "Heal a friendly soldier for 4", 3355),
            Spell(3, "Bandage", "Heal a friendly soldier for 4", 3356),
            Item(3, "Shield", "Give a creature +0/+2 and Guard", 4445),
            Creature(3, "Priest", 1, 1, "Restore a friendly soldier to full HP", 4567),
            Creature(3, "Priest", 1, 1, "Restore a friendly soldier to full HP", 5678),
            Creature(3, "Guard Dog", 1, 1, "Guard Charge", 989),
            Creature(3, "Guard Dog", 1, 1, "Guard Charge", 900),
            ]
demo_deck = [Creature(3, "Guard Dog", 1, 1, "Guard Charge", 1),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 9),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 10),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 11),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 12),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 13),
             ]
test_deck = [Creature(3, "Guard Dog", 1, 1, "Guard Charge", 2),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 3),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 4),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 5),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 6),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 7),
             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 8),
             ]
integration_deck = [Creature(1, 'Templar Knight', 5, 1, "Guard", 23),
                    Creature(1, 'Page', 1, 1, "", 24),
                    Creature(1, 'Squire', 2, 1, "", 25),
                    Creature(1, "Mounted Knight", 4, 1, "Charge", 26),
                    Creature(1, 'Templar Knight', 5, 1, "", 28),
                    Creature(1, 'Hospitaller Knight', 5, 1, "Heal a friendly soldier for 2", 29),
                    Creature(1, 'Hospitaller Knight', 5, 1, "Heal a friendly soldier for 2", 30),
                    Creature(1, 'Teutonic Knight', 6, 1, "", 32),
                    Item(1, "Knight's Equipment", "Give a creature +2/+2", 43),
                    Item(1, "Knight's Equipment", "Give a creature +2/+2", 42),
                    Spell(1, "Personal Guard", "Give a soldier guard", 34),
                    Spell(1, "Personal Guard", "Give a soldier guard", 35),
                    Creature(1, "Priest", 1, 1, "Restore a friendly soldier to full HP", 36),
                    Creature(1, "Priest", 1, 1, "Restore a friendly soldier to full HP", 37),
                    Creature(1, "Two-handed Knight", 5, 1, "Kill an enemy soldier", 20),
                    Creature(1, "Two-handed Knight", 5, 1, "Kill an enemy soldier", 21),
                    Spell(1, "Volley", "Deal 1 damage to all enemies", 40),
                    Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 41),
                    Item(1, "Shield", "Give a creature +0/+2 and Guard", 43),
                    Item(1, "Shield", "Give a creature +0/+2 and Guard", 44),
                    Spell(1, "Kill", "Kill an enemy soldier", 37),
                    Spell(1, "Bandages", "Restore a friendly soldier to full HP", 38),
                    Spell(1, "Bandage", "Heal a friendly soldier for 4", 39),
                    ]
integration_deck_official = [Creature(7, 'Templar Knight', 5, 5, "Guard", 23),
                             Creature(1, 'Page', 1, 1, "", 24),
                             Creature(1, 'Page', 1, 1, "", 124),
                             Creature(2, 'Squire', 2, 2, "", 25),
                             Creature(4, "Mounted Knight", 4, 4, "Charge", 26),
                             Creature(7, 'Templar Knight', 5, 5, "Guard", 28),
                             Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 29),
                             Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 30),
                             Creature(7, 'Teutonic Knight', 6, 5, "", 32),
                             Item(5, "Knight's Equipment", "Give a creature +2/+2", 43),
                             Item(5, "Knight's Equipment", "Give a creature +2/+2", 42),
                             Spell(3, "Personal Guard", "Give a soldier guard", 34),
                             Spell(3, "Personal Guard", "Give a soldier guard", 35),
                             Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 20),
                             Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 21),
                             Spell(3, "Volley", "Deal 1 damage to all enemies", 39),
                             Spell(3, "Volley", "Deal 1 damage to all enemies", 1139),
                             Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 138),
                             Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 139),
                             Spell(5, "Kill", "Kill an enemy soldier", 37),
                             Spell(5, "Kill", "Kill an enemy soldier", 38),
                             Spell(4, "Bandages", "Restore a friendly soldier to full HP", 70),
                             Spell(4, "Bandages", "Restore a friendly soldier to full HP", 77),
                             Spell(3, "Bandage", "Heal a friendly soldier for 4", 55),
                             Spell(3, "Bandage", "Heal a friendly soldier for 4", 56),
                             Item(3, "Shield", "Give a creature +0/+2 and Guard", 45),
                             Item(3, "Shield", "Give a creature +0/+2 and Guard", 46),
                             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 77),
                             Creature(3, "Guard Dog", 1, 1, "Guard Charge", 87),
                             ]
integration_deck_opponent = [Creature(1, 'Templar Knight', 5, 1, "Guard", 3323),
                             Creature(1, 'Page', 1, 1, "", 3324),
                             Creature(1, 'Squire', 2, 1, "", 3325),
                             Creature(1, "Mounted Knight", 4, 1, "Charge", 3326),
                             Creature(1, 'Templar Knight', 5, 1, "", 3328),
                             Creature(1, 'Hospitaller Knight', 5, 1, "Heal a friendly soldier for 2", 3329),
                             Creature(1, 'Hospitaller Knight', 5, 1, "Heal a friendly soldier for 2", 3330),
                             Creature(1, 'Teutonic Knight', 6, 1, "", 3332),
                             Spell(1, "Personal Guard", "Give a soldier guard", 3334),
                             Spell(1, "Personal Guard", "Give a soldier guard", 3335),
                             Creature(1, "Priest", 1, 1, "Restore a friendly soldier to full HP", 3336),
                             Creature(1, "Priest", 1, 1, "Restore a friendly soldier to full HP", 3337),
                             Item(1, "Knight's Equipment", "Give a creature +2/+2", 3343),
                             Item(1, "Knight's Equipment", "Give a creature +2/+2", 3342),
                             Creature(1, "Two-handed Knight", 5, 1, "Kill an enemy soldier", 3320),
                             Creature(1, "Two-handed Knight", 5, 1, "Kill an enemy soldier", 3321),
                             Spell(1, "Volley", "Deal 1 damage to all enemies", 3341),
                             Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 3340),
                             Spell(1, "Kill", "Kill an enemy soldier", 3337),
                             Item(1, "Shield", "Give a creature +0/+2 and Guard", 3343),
                             Item(1, "Shield", "Give a creature +0/+2 and Guard", 3344),
                             Spell(1, "Bandages", "Restore a friendly soldier to full HP", 3338),
                             Spell(1, "Bandage", "Heal a friendly soldier for 4", 3339),
                             ]
knight_deck_official = [Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 251),
                        Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 252),
                        Creature(7, 'Teutonic Knight', 6, 5, "", 253),
                        Creature(7, 'Teutonic Knight', 6, 5, "", 254),
                        Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 255),
                        Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 256),
                        Creature(2, 'Squire', 2, 2, "", 257),
                        Creature(2, 'Squire', 2, 2, "", 258),
                        Creature(1, 'Page', 1, 1, "", 259),
                        Creature(1, 'Page', 1, 1, "", 260),
                        Creature(7, 'Templar Knight', 7, 5, "Guard", 261),
                        Creature(7, 'Templar Knight', 7, 5, "Guard", 262),
                        Creature(4, "Mounted Knight", 4, 4, "Charge", 263),
                        Creature(4, "Mounted Knight", 4, 4, "Charge", 264),
                        Spell(3, "Volley", "Deal 1 damage to all enemies", 265),
                        Spell(3, "Volley", "Deal 1 damage to all enemies", 266),
                        Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 267),
                        Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 268),
                        Spell(5, "Kill", "Kill an enemy soldier", 269),
                        Spell(5, "Kill", "Kill an enemy soldier", 270),
                        ]
to_be_added_in_game = [Spell(5, "In the name of the king", "All friendly soldiers get +1/+1", 1002),
                       Spell(0, "Blood price", "Take 5 dmg and gaine 3 mana", 1004),
                       Spell(3, "Long march", "All enemies are exhausted", 1005),
                       Spell(4, "Bodyguards", "Summ 2 Guards from you deck", 1007),
                       Creature(9, "Heavy Cavalary", 9, 9, "Takes 2 less dmg from attacks", 1006),
                       Item(2, "Leather armor", "Give a friendly soldier +3 hp", 1007),
                       Creature(5, "City Guard", 4, 5, "Guard", 1009),
                       Creature(2, "Bodyguard", 1, 1, "Guard", 1010),
                       Creature(4, "Bear", 4, 4, "", 1011),
                       Creature(3, "Woolf", 3, 3, "", 1012),
                       Creature(3, "Farmer", 1, 1, "Gain 1 mana", 1013),
                       Creature(4, "Merchant", 2, 4, "For the next 2 turns gain 1 mana each turn", 1014),
                       ]
cards_that_are_in_the_game = [Creature(1, "Peasant", 1, 1, "", -1),
                              Creature(7, 'Templar Knight', 7, 5, "Guard", -2),
                              Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", -3),
                              Creature(7, 'Teutonic Knight', 6, 5, "", -4),
                              Spell(3, "Volley", "Deal 1 damage to all enemies", -5),
                              Spell(1, "Arrow shot", "Deal 1 damage to a enemy", -6),
                              Spell(5, "Kill", "Kill an enemy soldier", -7),
                              Creature(4, "Mounted Knight", 4, 4, "Charge", -8),
                              Creature(2, 'Squire', 2, 2, "", -9),
                              Creature(1, 'Page', 1, 1, "", -10),
                              Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", -11),
                              Spell(3, "Bandage", "Heal a friendly soldier for 4", -12),
                              Spell(4, "Bandages", "Restore a friendly soldier to full HP", -13),
                              Spell(3, "Personal Guard", "Give a soldier guard", -14),
                              Creature(3, "Priest", 1, 1, "Restore a friendly soldier to full HP", -15),
                              Item(3, "Shield", "Give a creature +0/+2 and Guard", -16),
                              Item(5, "Knight's Equipment", "Give a creature +2/+2", -17),
                              Creature(3, "Guard Dog", 1, 1, "Guard Charge", -18),
                              ]
dict_of_decks = {"demo_deck": demo_deck, "bot_deck": bot_deck, "test_deck": test_deck,
                 "integration_deck": integration_deck, "integration_deck_opponent": integration_deck_opponent,
                 "knight_deck_official": knight_deck_official, "integration_deck_official": integration_deck_official
                 }
