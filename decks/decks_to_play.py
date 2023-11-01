from clases.Item import Item
from clases.creatures import Creature
from clases.spells import Spell

starter_deck = [Creature(1, "Peasant", 1, 1, "", 1),
                Creature(1, "Peasant", 1, 1, "", 2),
                Creature(1, "Peasant", 1, 1, "", 3),
                Creature(1, "Peasant", 1, 1, "", 4),
                Creature(1, "Peasant", 1, 1, "", 5),
                Creature(1, "Peasant", 1, 1, "", 6),
                Creature(0, "Andras", 99, 99, "", 1000)]
bot_deck = [Creature(1, 'Templar Knight', 7, 1, "Guard", 261),
            Creature(1, 'Templar Knight', 7, 1, "Guard", 262),
            Creature(1, "Mounted Knight", 4, 1, "Charge", 263),
            Creature(1, "Mounted Knight", 4, 1, "Charge", 264),
            Creature(1, "Peasant", 1, 1, "", 264),
            Creature(1, "Peasant", 1, 1, "", 265),
            Creature(1, "Peasant", 2, 2, "", 266),
            Creature(1, "Peasant", 2, 2, "", 267),
            Creature(1, "Peasant", 3, 3, "", 268),
            Creature(1, "Peasant", 3, 3, "", 269),
            ]
demo_deck = [Creature(1, 'Hospitaller Knight', 5, 4, "Heal +2 a friendly soldier", 1),
             Creature(1, 'Hospitaller Knight', 5, 4, "Heal +2 a friendly soldier", 2),
             Creature(1, 'Hospitaller Knight', 5, 4, "Heal +2 a friendly soldier", 3),
             Creature(1, 'Hospitaller Knight', 5, 4, "Heal +2 a friendly soldier", 4),
             Creature(1, 'Hospitaller Knight', 5, 4, "Heal +2 a friendly soldier", 5),
             Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 10),
             Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 1),
             Creature(4, "Mounted Knight", 4, 4, "Charge", 15),
             Creature(4, "Mounted Knight", 4, 4, "Charge", 16),
             ]

test_deck = [Spell(3, "Personal Guard", "Give a soldier guard", 1),
             Creature(3, 'Squire', 1, 1, "", 2),
             Creature(3, 'Squire', 1, 1, "", 3),
             Spell(3, "Personal Guard", "Give a soldier guard", 4),
             Creature(1, 'Templar Knight', 7, 1, "Guard", 261),
             Creature(1, 'Templar Knight', 7, 1, "Guard", 262),
             Spell(3, "Personal Guard", "Give a soldier guard", 7),
             Creature(3, 'Squire', 1, 1, "", 8),
             Creature(3, 'Squire', 1, 1, "", 9),
             ]

integration_deck = [Creature(1, 'Templar Knight', 5, 5, "Guard", 23),
                    Creature(1, 'Page', 1, 1, "", 24),
                    Creature(1, 'Squire', 2, 2, "", 25),
                    Creature(1, "Mounted Knight", 4, 4, "Charge", 26),
                    Creature(1, 'Templar Knight', 5, 5, "", 28),
                    Creature(1, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 29),
                    Creature(1, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 30),
                    Creature(1, 'Teutonic Knight', 6, 5, "", 32),
                    Spell(1, "Personal Guard", "Give a soldier guard", 34),
                    Spell(1, "Personal Guard", "Give a soldier guard", 35),
                    Creature(1, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 20),
                    Creature(1, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 21),
                    Spell(1, "Volley", "Deal 1 damage to all enemies", 39),
                    Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 38),
                    Spell(1, "Kill", "Kill an enemy soldier", 37),
                    ]
integration_deck_opponent = [Creature(1, 'Templar Knight', 5, 5, "Guard", 3323),
                             Creature(1, 'Page', 1, 1, "", 3324),
                             Creature(1, 'Squire', 2, 2, "", 3325),
                             Creature(1, "Mounted Knight", 4, 4, "Charge", 3326),
                             Creature(1, 'Templar Knight', 5, 5, "", 3328),
                             Creature(1, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 3329),
                             Creature(1, 'Hospitaller Knight', 5, 4, "Heal a friendly soldier for 2", 3330),
                             Creature(1, 'Teutonic Knight', 6, 5, "", 3332),
                             Spell(1, "Personal Guard", "Give a soldier guard", 3334),
                             Spell(1, "Personal Guard", "Give a soldier guard", 3335),
                             Spell(1, "Personal Guard", "Give a soldier guard", 3341),
                             Spell(1, "Personal Guard", "Give a soldier guard", 3342),
                             Spell(1, "Personal Guard", "Give a soldier guard", 3343),
                             Creature(1, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 3320),
                             Creature(1, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 3321),
                             Spell(1, "Volley", "Deal 1 damage to all enemies", 3339),
                             Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 3338),
                             Spell(1, "Kill", "Kill an enemy soldier", 3337),
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

to_be_added_in_game = [Spell(3, "Bandage", "Heal a friendly soldier for 4", 1000),
                       Spell(4, "Bandages", "Restore a friendly soldier to full HP", 1001),
                       Spell(5, "In the name of the king", "All friendly soldiers get +1/+1", 1002),
                       Creature(3, "Priest", 1, 1, "Restore a friendly soldier to full HP", 1003),
                       Spell(0, "Blood price", "Take 5 dmg and gaine 3 mana", 1004),
                       Spell(3, "Long march", "All enemies are exhausted", 1005),
                       Spell(3, "Personal Guard", "Give a soldier guard", 1006),
                       Spell(4, "Bodyguards", "Summ 2 Guards from you deck", 1007),
                       Creature(9, "Heavy Cavalary", 9, 9, "Takes 2 less dmg from attacks", 1006),
                       Item(2, "Leather armor", "Give a friendly soldier +3 hp", 1007),
                       Creature(3, "Guard dog", 1, 1, "Guard,Charge", 1008),
                       Creature(5, "City Guard", 4, 5, "Guard", 1009),
                       Creature(2, "Bodyguard", 1, 1, "Guard", 1010),
                       Creature(4, "Bear", 4, 4, "", 1011),
                       Creature(3, "Woolf", 3, 3, "", 1012),
                       Creature(3, "Farmer", 1, 1, "Gain 1 mana", 1013),
                       Creature(4, "Merchant", 2, 4, "For the next 2 turns gain 1 mana each turn", 1014),
                       ]

guards_deck = [Creature(7, 'Templar Knight', 7, 5, "Guard", 111),
               Creature(7, 'Templar Knight', 7, 5, "Guard", 112),
               Creature(5, "City Guard", 4, 5, "Guard", 113),
               Creature(5, "City Guard", 4, 5, "Guard", 114),
               Creature(2, "Bodyguard", 1, 1, "Guard", 115),
               Creature(2, "Bodyguard", 1, 1, "Guard", 116), ]

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
                              ]
