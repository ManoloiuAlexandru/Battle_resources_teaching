from ITschool_projects.battle_resources.clases.creatures import Creature
from ITschool_projects.battle_resources.clases.spells import Spell

starter_deck = [Creature(1, "Peasant", 1, 1, "", 1),
                Creature(1, "Peasant", 1, 1, "", 2),
                Creature(1, "Peasant", 1, 1, "", 3),
                Creature(1, "Peasant", 1, 1, "", 4),
                Creature(1, "Peasant", 1, 1, "", 5),
                Creature(1, "Peasant", 1, 1, "", 6),
                Creature(0, "Andras", 99, 99, "", 1000)]

demo_deck = [Creature(2, "Archer", 1, 2, "", 7),
             Creature(7, 'Templar Knight', 5, 5, "", 8),
             Creature(3, "Spearmen", 3, 2, "", 9),
             Creature(2, "Militia", 2, 2, "", 10),
             Creature(5, "Crossbowmen", 4, 6, "", 11),
             Creature(1, "Peasant", 1, 1, "", 12),
             Creature(3, "Guard", 4, 1, "Guard", 13),
             Creature(8, 'Hospitaller Knight', 8, 3, "", 30),
             Creature(8, 'Hospitaller Knight', 8, 3, "", 31),
             Creature(7, 'Teutonic Knight', 6, 5, "", 32),
             Creature(7, 'Teutonic Knight', 6, 5, "", 33),
             Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 20),
             Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 21),
             Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 102),
             Spell(5, "Kill", "Kill an enemy soldier", 103),
             Spell(3, "Volley", "Deal 1 damage to all enemies", 103),
             Creature(4, "Mounted Knight", 4, 4, "Charge", 41)
             ]

test_deck = [Spell(3, "Volley", "Deal 1 damage to all enemies", 103),
             Spell(5, "Kill", "Kill an enemy soldier", 104),
             Spell(1, "Arrow shot", "Deal 1 damage to a enemy", 101),
             Creature(6, 'Templar Knight', 5, 5, "", 23),
             Creature(1, 'Page', 1, 1, "", 24),
             Creature(3, 'Squire', 1, 1, "", 25),
             Creature(3, 'Squire', 1, 1, "", 26),
             Creature(6, 'Templar Knight', 5, 5, "", 27),
             Creature(6, 'Templar Knight', 5, 5, "", 28),
             Creature(4, "Mounted Knight", 4, 4, "Charge", 40)
             ]

knight_deck = [Creature(6, 'Templar Knight', 5, 5, "", 23),
               Creature(1, 'Page', 1, 1, "", 24),
               Creature(3, 'Squire', 1, 1, "", 25),
               Creature(3, 'Squire', 1, 1, "", 26),
               Creature(6, 'Templar Knight', 5, 5, "", 27),
               Creature(6, 'Templar Knight', 5, 5, "", 28),
               Creature(8, 'Hospitaller Knight', 8, 3, "", 29),
               Creature(8, 'Hospitaller Knight', 8, 3, "", 30),
               Creature(8, 'Hospitaller Knight', 8, 3, "", 31),
               Creature(7, 'Teutonic Knight', 6, 5, "", 32),
               Creature(7, 'Teutonic Knight', 6, 5, "", 33),
               Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 20),
               Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 21),
               Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy soldier", 22),
               ]
