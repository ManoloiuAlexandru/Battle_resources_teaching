from clases.Defence import Defence
from clases.creatures import Creature
from clases.spells import Spell

cards_holy_show = [Creature(8, "Frederick Barbarossa", 6, 6,
                            "Friendly minions get armored and +1/+1 Armored Guard", "knight", -72),
                   Creature(3, "Scribe", 3, 0, "At the end of your turn draw a card", "worker", -41),
                   Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2 Armored", "knight", -11),
                   Spell(1, "Bandage", "Heal a friendly minion for 4", -12),
                   Spell(2, "Bandages", "Restore a friendly minion to full HP", -13),
                   Spell(1, "Personal Guard", "Give a minion guard and draw a card", -14),
                   Defence(1, "Empire Peasants", 1, 4, "", -16),
                   Spell(3, "Knight's training", "Give a minions +3/+3", -35),
                   Spell(3, "Feudal Obligations", "Draw 2 cards", -29),
                   Spell(8, "Bodyguards", "Summon  2 Guards from your deck", -22),
                   Creature(3, "Faithful Guard", 2, 2, "Guard Armored", "soldier", -42),
                   Spell(5, "Call of the Emperor", "Draw 3 cards and reduce there mana cost by 1", -47),
                   Spell(4, "Arbalest Shot", "Deal 3 damage and draw a card", -48),
                   Spell(2, "Chivalry and Honor", "Give a minion +2/+1 and draw a card", -51),
                   Creature(1, "Faithful Protector", 1, 1, "Guard Armored", "soldier", -62),
                   Spell(7, "Rain of Arrows", "Destroy ALL minions that are not Armored", -64),
                   Spell(2, "In the name of the king", "Give your minions +1/+1", -70),
                   Creature(1, "Selfless Knight", 1, 2, "Desperate Give a friendly minion armored", "knight", -86),
                   Creature(2, "Armored Knight", 2, 2, "Armored", "knight", -87),
                   Creature(2, "Armored Horse", 1, 2, "Armored Desperate Draw a Spell", "animal", -88),
                   Creature(5, "Church Builder", 6, 4, "Restore 8 health", "worker", -100),
                   Spell(9, "Call of God", "Heal for 8 and summon a 8/8 armored guard Crusader", -101),
                   Creature(1, "Heretic Knight", 1, 2, "Armored deal 2 damage to your kingdom", "knight", -122),
                   Creature(9, "Graf", 6, 3,
                            "Guard Armored Desperate Summon 3 Armored Peasant with guard and armored", "soldier",
                            -125),
                   Creature(10, "Margrave", 6, 4, "Guard Armored Cost 1 less for other each card in your hand",
                            "knight", -126),
                   Spell(2, "Warhammer", "Break an enemy armor making him lose all attributes", -127),
                   Creature(3, "Voice of the emperor", 4, 3, "Set a minion attack and health to 3", "soldier", -128),
                   Creature(3, "Bailiff", 3, 3, "Set a minion attack to 1", "soldier", -129),
                   Spell(3, "Defending  the empire", "Summon 3 Kaiserliche and put a 1/4 Defence", -131),
                   Creature(1, "Army Cook", 1, 2, "Add 2 Kaiserliche to your hand", "worker", -149),
                   Creature(7, "Empire Crusader", 7, 7, "Add 5 Holy Roman Empire cards to your hand", "knight", -153),
                   Creature(3, "Inspired soldier", 5, 2, "If you are holding a spell gain armored and guard",
                            "soldier", -157),
                   Spell(6, "Emperor's Hope", "Restore 8 health and draw 3 cards", -158),
                   Spell(1, "Emperor's Will", "Give a minion +1/+2 and Armored if you hold a knight", -159),
                   Creature(2, "Church Knight", 2, 2, "If you are holding a knight get armored and guard", "worker",
                            -167),
                   Spell(7, "Crusade Calling", "Recruit a knight and summon a 5/5 Crusader with Guard", -216),
                   Spell(1, "Shield of Honor", "Give a damaged minion +3 attack and Armored", -222),
                   ]
list_of_holy_roman = [[Creature(8, "Frederick Barbarossa", 6, 6,
                                "Friendly minions get armored and +1/+1 Armored Guard", "knight", -72)],
                      [Creature(3, "Scribe", 3, 0, "At the end of your turn draw a card", "worker", -41)],
                      [Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2 Armored", "knight", -11)],
                      [Spell(1, "Bandage", "Heal a friendly minion for 4", -12)],
                      [Spell(2, "Bandages", "Restore a friendly minion to full HP", -13)],
                      [Spell(1, "Personal Guard", "Give a minion guard and draw a card", -14)],
                      [Defence(1, "Empire Peasants", 1, 4, "", -16)],
                      [Spell(3, "Knight's training", "Give a minions +3/+3", -35)],
                      [Spell(3, "Feudal Obligations", "Draw 2 cards", -29)],
                      [Spell(8, "Bodyguards", "Summon  2 Guards from your deck", -22)],
                      [Creature(3, "Faithful Guard", 2, 2, "Guard Armored", "soldier", -42)],
                      [Spell(5, "Call of the Emperor", "Draw 3 cards and reduce there mana cost by 1", -47)],
                      [Spell(4, "Arbalest Shot", "Deal 3 damage and draw a card", -48)],
                      [Spell(2, "Chivalry and Honor", "Give a minion +2/+1 and draw a card", -51)],
                      [Creature(1, "Faithful Protector", 1, 1, "Guard Armored", "soldier", -62)],
                      [Spell(7, "Rain of Arrows", "Destroy ALL minions that are not Armored", -64)],
                      [Spell(2, "In the name of the king", "Give your minions +1/+1", -70)],
                      [Creature(1, "Selfless Knight", 1, 2, "Desperate Give a friendly minion armored", "knight", -86)],
                      [Creature(2, "Armored Knight", 2, 2, "Armored", "knight", -87)],
                      [Creature(2, "Armored Horse", 1, 2, "Armored Desperate Draw a Spell", "animal", -88)],
                      [Creature(5, "Church Builder", 6, 4, "Restore 8 health", "worker", -100)],
                      [Spell(9, "Call of God", "Heal for 8 and summon a 8/8 armored guard Crusader", -101)],
                      [Creature(1, "Heretic Knight", 1, 2, "Armored deal 2 damage to your kingdom", "knight", -122)],
                      [Creature(9, "Graf", 6, 3,
                                "Guard Armored Desperate Summon 3 Armored Peasant with guard and armored", "soldier",
                                -125)],
                      [Creature(10, "Margrave", 6, 4, "Guard Armored Cost 1 less for other each card in your hand",
                                "knight", -126)],
                      [Spell(2, "Warhammer", "Break an enemy armor making him lose all attributes", -127)],
                      [Creature(3, "Voice of the emperor", 4, 3, "Set a minion attack and health to 3", "soldier",
                                -128)],
                      [Creature(3, "Bailiff", 3, 3, "Set a minion attack to 1", "soldier", -129)],
                      [Spell(3, "Defending  the empire", "Summon 3 Kaiserliche and put a 1/4 Defence", -131)],
                      [Creature(1, "Army Cook", 1, 2, "Add 2 Kaiserliche to your hand", "worker", -149)],
                      [Creature(7, "Empire Crusader", 7, 7, "Add 5 Holy Roman Empire cards to your hand", "knight",
                                -153)],
                      [Creature(3, "Inspired soldier", 5, 2, "If you are holding a spell gain armored and guard",
                                "soldier", -157)],
                      [Spell(6, "Emperor's Hope", "Restore 8 health and draw 3 cards", -158)],
                      [Spell(1, "Emperor's Will", "Give a minion +1/+2 and Armored if you hold a knight", -159)],
                      [Creature(2, "Church Knight", 2, 2, "If you are holding a knight get armored and guard", "worker",
                                -167)],
                      [Spell(7, "Crusade Calling", "Recruit a knight and summon a 5/5 Crusader with Guard", -216)],
                      [Spell(1, "Shield of Honor", "Give a damaged minion +3 attack and Armored", -222)]
                      ]
cards_for_holy_roman_empire = [
    Creature(8, "Frederick Barbarossa", 6, 6,
             "Friendly minions get armored and +1/+1 Armored Guard", "knight", -72),
    Creature(3, "Scribe", 3, 0, "At the end of your turn draw a card", "worker", -41),
    Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2 Armored", "knight", -11),
    Spell(1, "Bandage", "Heal a friendly minion for 4", -12),
    Spell(2, "Bandages", "Restore a friendly minion to full HP", -13),
    Spell(1, "Personal Guard", "Give a minion guard and draw a card", -14),
    Defence(1, "Empire Peasants", 1, 4, "", -16),
    Spell(3, "Knight's training", "Give a minions +3/+3", -35),
    Spell(3, "Feudal Obligations", "Draw 2 cards", -29),
    Spell(8, "Bodyguards", "Summon  2 Guards from your deck", -22),
    Creature(3, "Faithful Guard", 2, 2, "Guard Armored", "soldier", -42),
    Spell(5, "Call of the Emperor", "Draw 3 cards and reduce there mana cost by 1", -47),
    Spell(4, "Arbalest Shot", "Deal 3 damage and draw a card", -48),
    Spell(2, "Chivalry and Honor", "Give a minion +2/+1 and draw a card", -51),
    Creature(1, "Faithful Protector", 1, 1, "Guard Armored", "soldier", -62),
    Spell(7, "Rain of Arrows", "Destroy ALL minions that are not Armored", -64),
    Spell(2, "In the name of the king", "Give your minions +1/+1", -70),
    Creature(1, "Selfless Knight", 1, 2, "Desperate Give a friendly minion armored", "knight", -86),
    Creature(2, "Armored Knight", 2, 2, "Armored", "knight", -87),
    Creature(2, "Armored Horse", 1, 2, "Armored Desperate Draw a Spell", "animal", -88),
    Creature(5, "Church Builder", 6, 4, "Restore 8 health", "worker", -100),
    Spell(9, "Call of God", "Heal for 8 and summon a 8/8 armored guard Crusader", -101),
    Creature(1, "Heretic Knight", 1, 2, "Armored deal 2 damage to your kingdom", "knight", -122),
    Creature(9, "Graf", 6, 3,
             "Guard Armored Desperate Summon 3 Armored Peasant with guard and armored", "soldier",
             -125),
    Creature(10, "Margrave", 6, 4, "Guard Armored Cost 1 less for other each card in your hand", "knight", -126),
    Spell(2, "Warhammer", "Break an enemy armor making him lose all attributes", -127),
    Creature(3, "Voice of the emperor", 4, 3, "Set a minion attack and health to 3", "soldier", -128),
    Creature(3, "Bailiff", 3, 3, "Set a minion attack to 1", "soldier", -129),
    Spell(3, "Defending  the empire", "Summon 3 Kaiserliche and put a 1/4 Defence", -131),
    Creature(1, "Army Cook", 1, 2, "Add 2 Kaiserliche to your hand", "worker", -149),
    Creature(7, "Empire Crusader", 7, 7, "Add 5 Holy Roman Empire cards to your hand", "knight", -153),
    Creature(3, "Inspired soldier", 5, 2, "If you are holding a spell gain armored and guard",
             "soldier", -157),
    Spell(6, "Emperor's Hope", "Restore 8 health and draw 3 cards", -158),
    Spell(1, "Emperor's Will", "Give a minion +1/+2 and Armored if you hold a knight", -159),
    Creature(2, "Church Knight", 2, 2, "If you are holding a knight get armored and guard", "worker",
             -167),
    Spell(7, "Crusade Calling", "Recruit a knight and summon a 5/5 Crusader with Guard", -216),
    Spell(1, "Shield of Honor", "Give a damaged minion +3 attack and Armored", -222),
]
