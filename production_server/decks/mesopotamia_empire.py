from clases.creatures import Creature
from clases.spells import Spell

mesopotamia_empire = [Spell(8, "Epidemic", "Destroy ALL minions", -32),
                      Creature(1, "City Gate Guard", 3, 1, "Guard", "ancient", -104),
                      Spell(3, "Ancient Tactics", "Draw 3 cards deal 3 damage to your kingdom", -105),
                      Creature(1, "Mesopotamia Scholar", 1, 2, "Draw a card Deal 2 damage to your kingdom", "ancient",
                               -106),
                      Creature(9, "King Saragon of Akkad", 7, 9,
                               "Give all ancients +2/+2 your knigdom can't take damage", "ancient", -107),
                      Creature(2, "Military Guard", 4, 2, "Guard Deal 2 damage to your kingdom", "ancient", -108),
                      Creature(1, "Lu", 2, 3, "Deal 2 damage to your kingdom", "ancient", -109),
                      Spell(4, "Mercenaries Reinforcements", "Deal 2-4 damage and summ that many Man at arms", -110),
                      Creature(5, "Assyrian Horserider", 7, 5, "Charge discard 2 cards from your hand", "ancient",
                               -111),
                      Spell(6, "Tactical Coordination", "When you discard or use this draw 3 cards", -112),
                      Creature(9, "Turtanu", 9, 3, "Guard Desperate Summon 3 City Gate Guards", "ancient", -113),
                      Creature(3, "Prisoner of War", 4, 3, "If you discard this summon it", "ancient", -114),
                      Spell(6, "Heat of the desert", "Deal 5 damage to all characters", -199),
                      Creature(6, "Limmu", 2, 3,
                               "Deal damage equal to the number of card in your hand to all other minions", "worker",
                               -200),
                      Creature(7, "Ancient Law Enforcer", 6, 6, "Deal 3 damage to all other characters", "ancient",
                               -201),
                      Creature(5, "Ancient Full Armored soldier", 5, 5,
                               "Deal 3 damage to all other characters if you hold a knight",
                               "knight", -202),
                      Creature(4, "Ancient Imperial Guard", 4, 4,
                               "If your kingdom has less then 15 HP gain +3/+3 and guard", "ancient",
                               -203),
                      Spell(3, "A day in the desert", "Deal 3 damage to all characters", -204),
                      Creature(3, "Ancient Army Guard", 5, 2, "Guard when you discard this summon it", "ancient", -205),
                      Creature(1, "Ancient Farmer", 3, 1, "Add 2 Resources to your deck", "ancient", -251),
                      Spell(3, "Ancient Arrow Volley", "Deal 2 damage to ALL minions add 2 Resources to your deck",
                            -252),
                      Spell(2, "Ancient Arrow Shot", "Deal 3 damage to a minion add 2 Resources to your deck", -253),
                      Creature(5, "Payed Guard", 5, 4, "Guard Consume a Resources from your deck to get a +3/+3",
                               "ancient", -254),
                      Creature(3, "Payed Scribe", 4, 3, "Consume a Resources from your deck to deal 3 damage", "worker",
                               -255),
                      Creature(7, "Hammurabi", 5, 5,
                               "For each Resources in your deck summon a 3/3 Man at Arms with Rush", "ancient", -256),
                      Spell(1, "Imperial Drama",
                            "Destory 4 of your minion in 1 turn without killing any enemy minions Reward: Lenxaadra, Queen of Drama",
                            -265),
                      ]
mesopotamia_show = [Spell(8, "Epidemic", "Destroy ALL minions", -32),
                    Creature(1, "City Gate Guard", 3, 1, "Guard", "ancient", -104),
                    Spell(3, "Ancient Tactics", "Draw 3 cards deal 3 damage to your kingdom", -105),
                    Creature(1, "Mesopotamia Scholar", 1, 2, "Draw a card Deal 2 damage to your kingdom", "ancient",
                             -106),
                    Creature(9, "King Saragon of Akkad", 7, 9, "Give all ancients +2/+2 your knigdom can't take damage",
                             "ancient", -107),
                    Creature(2, "Military Guard", 4, 2, "Guard Deal 2 damage to your kingdom", "ancient", -108),
                    Creature(1, "Lu", 2, 3, "Deal 2 damage to your kingdom", "ancient", -109),
                    Spell(4, "Mercenaries Reinforcements", "Deal 2-4 damage and summ that many Man at arms", -110),
                    Creature(5, "Assyrian Horserider", 7, 5, "Charge discard 2 cards from your hand", "ancient", -111),
                    Spell(6, "Tactical Coordination", "When you discard or use this draw 3 cards", -112),
                    Creature(9, "Turtanu", 9, 3, "Guard Desperate Summon 3 City Gate Guards", "ancient", -113),
                    Creature(3, "Prisoner of War", 4, 3, "If you discard this summon it", "ancient", -114),
                    Spell(6, "Heat of the desert", "Deal 5 damage to all characters", -199),
                    Creature(6, "Limmu", 2, 3,
                             "Deal damage equal to the number of card in your hand to all other minions", "worker",
                             -200),
                    Creature(7, "Ancient Law Enforcer", 6, 6, "Deal 3 damage to all other characters", "ancient",
                             -201),
                    Creature(5, "Ancient Full Armored soldier", 5, 5,
                             "Deal 3 damage to all other characters if you hold a knight",
                             "knight", -202),
                    Creature(4, "Ancient Imperial Guard", 4, 4,
                             "If your kingdom has less then 15 HP gain +3/+3 and guard", "ancient",
                             -203),
                    Spell(3, "A day in the desert", "Deal 3 damage to all characters", -204),
                    Creature(3, "Ancient Army Guard", 5, 2, "Guard when you discard this summon it", "ancient", -205),
                    Creature(1, "Ancient Farmer", 3, 1, "Add 2 Resources to your deck", "ancient", -251),
                    Spell(3, "Ancient Arrow Volley", "Deal 2 damage to ALL minions add 2 Resources to your deck",
                          -252),
                    Spell(2, "Ancient Arrow Shot", "Deal 3 damage to a minion add 2 Resources to your deck", -253),
                    Creature(5, "Payed Guard", 5, 4, "Guard Consume a Resources from your deck to get a +3/+3",
                             "ancient", -254),
                    Creature(3, "Payed Scribe", 4, 3, "Consume a Resources from your deck to deal 3 damage", "worker",
                             -255),
                    Creature(7, "Hammurabi", 5, 5,
                             "For each Resources in your deck summon a 3/3 Man at Arms with Rush", "ancient", -256),
                    Spell(1, "Imperial Drama",
                          "Destory 4 of your minion in 1 turn without killing any enemy minions Reward: Lenxaadra, Queen of Drama",
                          -265),
                    ]
