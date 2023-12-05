from clases.Defence import Defence
from clases.creatures import Creature
from clases.spells import Spell

cards_that_are_in_the_game_for_all = [Creature(0, "Peasant", 1, 1, "", "worker", -1),
                                      Creature(6, 'Templar Knight', 7, 5, "Guard", "knight", -2),
                                      Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", "knight", -3),
                                      Creature(7, 'Teutonic Knight', 6, 5, "Guard Armored", "knight", -4),
                                      Spell(5, "Kill", "Kill an enemy minion", -7),
                                      Creature(5, "Mounted Knight", 4, 4, "Charge", "knight", -8),
                                      Creature(2, 'Squire', 2, 3, "", "knight", -9),
                                      Creature(2, 'Page', 1, 1, "Draw a card", "knight", -10),
                                      Creature(3, "Priest", 1, 1,
                                               "Restore a friendly minion to full HP and give it +1/+1", "worker",
                                               -15),
                                      Creature(2, "Guard Dog", 2, 2, "Guard", "animal", -18),
                                      Creature(8, "Richard the Lionheart", 6, 6, "Draw a Spell and a Creature Guard",
                                               "knight",
                                               - 21),
                                      Creature(3, "Miner", 1, 1, "At the end of your turn draw a card", "worker", -23),
                                      Creature(4, "City Guard", 5, 3, "Guard", "soldier", -24),
                                      Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", "worker", -31),
                                      Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", "worker",
                                               -33),
                                      Creature(1, "Church Scholar", 2, 1, "Evrey time a creature is healed gain +1/+1 ",
                                               "worker", -34),
                                      Creature(2, "Armorer", 2, 2, "Give a friendly minion armored", "worker", -39),
                                      Creature(1, "Wolf", 1, 1, "Charge", "animal", -49),
                                      Creature(1, "Archer", 1, 1, "Deal 1 damage", "soldier", -50),
                                      Creature(1, "Armored Page", 1, 1, "Armored", "knight", -51),
                                      Creature(1, "Scared Noble", 2, 1, "Give a friendly minion guard", "worker", -52),
                                      Creature(3, "Tournament Horserider", 1, 2, "Charge Armored", "knight", -53),
                                      Creature(3, "Personal instructor", 3, 2, "Give a friendly minion +1/+1", "worker",
                                               -54),
                                      Creature(4, "Last Defender", 6, 2,
                                               "If your hand is empty gain +2 attack and guard", "knight", -55),
                                      Creature(3, "Drummer", 2, 2, "Give your hand +1/+1", "soldier", -56),
                                      Creature(6, "War elephant", 5, 4,
                                               "While this is on the field your creatures have +1 attack", "animal",
                                               -20),
                                      Creature(5, "Army Champion", 4, 4,
                                               "While this is on the field friendly minions get +1/+1", "knight", -69),
                                      Creature(2, "Scribe of the Church", 1, 1, "Draw a spell", "worker", -73),
                                      Creature(12, "Trebuchet", 8, 8, "Cost 1 less for other each card in your hand",
                                               "machine ", -74),
                                      Creature(5, "Bishop", 2, 2, "Give a friendly minion +4/+4 and guard", "worker",
                                               -75),
                                      Creature(2, "Lost Scribe", 1, 2, "Desperate Draw a card", "worker", -80),
                                      Creature(2, "Lost Sheep", 1, 1, "Desperate Summon 2 1/1 Wild Wolf", "animal",
                                               -81),
                                      Creature(5, "Front Line Defender", 6, 3,
                                               "Desperate Summ a 1/2 Second Line Defender with Guard Guard", "soldier",
                                               2),
                                      Creature(6, "Joan of Arc", 2, 2,
                                               "Desperate Summ 7/8 Saint Joan of Arc with charge and armored",
                                               "worker",
                                               -90),
                                      Creature(11, "Covered Battering Ram", 8, 8,
                                               "Cost 1 less for each minion on the battlefield",
                                               "machine", -102),
                                      Creature(10, "Battering Ram", 8, 8,
                                               "Cost 1 less for each friendly minion on the battlefield",
                                               "machine", -103),
                                      Creature(8, "Carcassonne", 8, 8,
                                               "Can't attack. Deal 8 damage to a random enemy at the end of your turn",
                                               "building", -115),
                                      Creature(2, "Countryside Hunter", 3, 2, "Give a friendly worker +1/+1", "worker",
                                               -116),
                                      Creature(5, "Landlord", 3, 4, "Draw 3 workers", "worker", -117),
                                      Creature(2, "Shepherd", 2, 1, "Summon a 1/1 guard dog with guard", "worker",
                                               -118),
                                      Creature(2, "Peasant Fighter", 2, 3, "If you have another worker get +1/+1",
                                               "worker", -119),
                                      Creature(1, "New Recruit", 2, 1, "When you play a soldier give this +1 attack",
                                               "soldier", -120),
                                      Creature(7, "Wondering Scribe", 4, 4, "When you cast a spell draw a card",
                                               "worker", -121),
                                      Creature(2, "Armored Peasant", 2, 1, "Armored Guard", "soldier", -123),
                                      Creature(6, "Rich Peasant", 1, 2,
                                               "Summon 2 armored Peasant with guard and armored", "worker", -124),
                                      Creature(2, "Lost Shield", 2, 0, "Desperate Sumon a 4/4 City guard", "item", -82),
                                      Creature(9, "Wild Elephant", 7, 9, "Deal 4 damage", "animal", -142),
                                      Creature(4, "Local Healer", 4, 4, "Restore 4 health", "worker", -143),
                                      Creature(3, "Clergy", 3, 3, "Restore 3 health", "worker", -144),
                                      Creature(7, "Local Bodyguard", 8, 6, "Guard", "worker", -145),
                                      Creature(1, "Banner holder", 2, 1, "Give your hand +1 health", "soldier", -146),
                                      Creature(9, "Sleepy Guard", 12, 4, "Guard", "soldier", -147)
                                      ]
all_cards_in_game = [Creature(0, "Peasant", 1, 1, "", "worker", -1),
                     Creature(6, 'Templar Knight', 7, 5, "Guard", "knight", -2),
                     Creature(9, "Two-handed Knight", 5, 5, "Kill an enemy minion", "knight", -3),
                     Creature(7, 'Teutonic Knight', 6, 5, "Guard Armored", "knight", -4),
                     Spell(3, "Volley", "Deal 2 damage to all enemies", -5),
                     Spell(1, "Arrow shot", "Deal 2 damage to a enemy", -6),
                     Spell(5, "Kill", "Kill an enemy minion", -7),
                     Creature(5, "Mounted Knight", 4, 4, "Charge", "knight", -8),
                     Creature(2, 'Squire', 2, 3, "", "knight", -9),
                     Creature(2, 'Page', 1, 1, "Draw a card", "knight", -10),
                     Creature(6, 'Hospitaller Knight', 5, 4, "Heal a friendly minion for 2 Armored", "knight", -11),
                     Spell(1, "Bandage", "Heal a friendly minion for 4", -12),
                     Spell(2, "Bandages", "Restore a friendly minion to full HP", -13),
                     Spell(1, "Personal Guard", "Give a minion guard and draw a card", -14),
                     Creature(3, "Priest", 1, 1,
                              "Restore a friendly minion to full HP and give it +1/+1", "worker",
                              -15),
                     Defence(1, "Empire Peasants", 1, 4, "", -16),
                     Creature(2, "Guard Dog", 2, 2, "Guard", "animal", -18),
                     Spell(3, "Horse riding lessons", "Give a friendly creature charge and +2 attack",
                           -19),
                     Creature(6, "War elephant", 5, 4,
                              "While this is on the field your creatures have +1 attack", "animal", -20),
                     Creature(8, "Richard the Lionheart", 6, 6, "Draw a Spell and a Creature Guard", "knight", -21),
                     Spell(8, "Bodyguards", "Summon  2 Guards from your deck", -22),
                     Creature(3, "Miner", 1, 1, "At the end of your turn draw a card", "worker", -23),
                     Creature(4, "City Guard", 5, 3, "Guard", "soldier", -24),
                     Spell(3, "Feudal Obligations", "Draw 2 cards", -29),
                     Creature(2, "Hunting dog", 1, 2, "Charge", "animal", -30),
                     Creature(3, "Farmer", 1, 1, "Gain 1 mana crystal", "worker", -31),
                     Creature(4, "Pronoiar", 3, 3, "Charge", "soldier", -37),
                     Creature(3, "Akritoi", 3, 2, "Guard", "soldier", -38),
                     Spell(8, "Epidemic", "Destroy ALL minions", -32),
                     Creature(2, "Lumberjack", 2, 2, "Give a friendly minion +1 attack", "worker", -33),
                     Creature(1, "Church Scholar", 2, 1, "Evrey time a creature is healed gain +1/+1 ", "worker", -34),
                     Spell(3, "Knight's training", "Give a minions +3/+3", -35),
                     Spell(6, "Peace Treaty", "Return all creature form the battlefield to their owners hands.", -36),
                     Creature(7, "Cataphract", 6, 6, "Guard Armored", "knight", -39),
                     Creature(2, "Armorer", 2, 2, "Give a friendly minion armored", "worker", -39),
                     Spell(5, "Wealthy Empire", "Summon 2 random cards from your deck", -40),
                     Creature(3, "Scribe", 3, 0, "At the end of your turn draw a card", "worker", -41),
                     Creature(3, "Faithful Guard", 2, 2, "Guard Armored", "soldier", -42),
                     Spell(2, "Ancient Empire", "Draw 2 cards Debt(1)", -43),
                     Creature(3, "Hunter", 3, 2, "Summon a 1/1 Dog", "worker", -44),
                     Creature(3, "Rider", 2, 3, "Charge", "soldier", -45),
                     Spell(2, "Call of the Khan", "Draw a card if it has Charge reduce the cost to 0", -46),
                     Spell(5, "Call of the Emperor", "Draw 3 cards and reduce there mana cost by 1", -47),
                     Spell(4, "Arbalest shot", "Deal 3 damage and draw a card", -48),
                     Creature(1, "Wolf", 1, 1, "Charge", "animal", -49),
                     Creature(1, "Archer", 1, 1, "Deal 1 damage", "soldier", -50),
                     Spell(2, "Chivalry and Honor", "Give a minion +2/+1 and draw a card", -51),
                     Creature(1, "Armored Page", 1, 1, "Armored", "knight", -51),
                     Creature(1, "Scared Noble", 2, 1, "Give a friendly minion guard", "worker", -52),
                     Creature(3, "Tournament Horserider", 1, 2, "Charge Armored", "knight", -53),
                     Creature(3, "Personal instructor", 3, 2, "Give a friendly minion +1/+1", "worker", -54),
                     Creature(4, "Last Defender", 6, 2, "If your hand is empty gain +2 attack and guard", "knight",
                              -55),
                     Creature(3, "Drummer", 2, 2, "Give your hand +1/+1", "soldier", -56),
                     Creature(3, "Negotiator", 1, 1, "Give your hand +1/+1 and draw a animal", "worker", -57),
                     Spell(3, "Horse raiding shot", "Deal 2 damage and draw a card", -58),
                     Creature(2, "Wild Horse", 2, 1, "Draw a charge card", "animal", -59),
                     Creature(2, "Watchman", 2, 1, "Draw a guard card", "worker", -60),
                     Creature(2, "Watchtower", 2, 1, "All your guards get +1/+2", "building", -61),
                     Creature(1, "Faithful Protector", 1, 1, "Guard Armored", "soldier", -62),
                     Spell(7, "Landslide", "Deal 7 damage to ALL minions", -63),
                     Spell(7, "Rain of Arrows", "Destroy ALL minions that are not Armored", -64),
                     Spell(2, "Roman Formation Circular", "Give your minions on the filed Guard", -65),
                     Spell(3, "Guard Duty", "Give a friendly minion +2/+2 if it is a Guard draw a card", -66),
                     Spell(3, "For the Khan", "Give all your minions +1/+0 and Charge", -67),
                     Spell(3, "Boarder Guards", "Summon 2 Akritoi Debt(1)", -68),
                     Creature(5, "Army Champion", 4, 4,
                              "While this is on the field friendly minions get +1/+1", "knight", -69),
                     Spell(2, "In the name of the king", "Give your minions +1/+1", -70),
                     Spell(1, "Roman Formation Phalanx", "Give your minions +1/+1 Debt(1)", -71),
                     Creature(8, "Frederick Barbarossa", 6, 6,
                              "Friendly minions get armored and +1/+1 Armored Guard", "knight", -72),
                     Creature(2, "Scribe of the Church", 1, 1, "Draw a spell", "worker", -73),
                     Creature(12, "Trebuchet", 8, 8, "Cost 1 less for each other card in your hand", "machine", -74),
                     Creature(5, "Bishop", 2, 2, "Give a friendly minion +4/+4 and guard", "worker", -75),
                     Creature(8, "Basil II", 6, 5, "Armored Charge Guard", "soldier", -76),
                     Creature(5, "Protokentarchos", 4, 4, "Give a friendly minion +3/+3 Debt(1)", "soldier", -77),
                     Creature(9, "Jochi", 8, 8, "Charge", "soldier", -78),
                     Spell(2, "Old Tactics", "Draw a card and reduce it is cost by 3", -79),
                     Creature(2, "Lost Scribe", 1, 2, "Desperate Draw a card", "worker", -80),
                     Creature(2, "Lost Sheep", 1, 1, "Desperate Summon 2 1/1 Wild Wolf", "animal", -81),
                     Creature(2, "Lost Shield", 2, 0, "Desperate Sumon a 4/4 City guard", "item", -82),
                     Spell(1, "Pilum Throw", "Deal 3 damage Debt(1)", -83),
                     Spell(3, "Fast Conscription", "Summon 4 1/1 Peasant", -84),
                     Creature(4, "Lost Noble", 1, 1, "Desperate Summon a 3/5 City guard", "worker", -85),
                     Creature(1, "Selfless Knight", 1, 2, "Desperate Give a friendly minion armored", "knight", -86),
                     Creature(2, "Armored Knight", 2, 2, "Armored", "knight", -87),
                     Creature(2, "Armored Horse", 1, 2, "Armored Desperate Draw a Spell", "animal", -88),
                     Creature(5, "Front Line Defender", 6, 3,
                              "Desperate Summ a 1/2 Second Line Defender with Guard Guard", "soldier", -89),
                     Creature(6, "Joan of Arc", 2, 2, "Desperate Summ 7/8 Saint Joan of Arc with charge and armored",
                              "soldier", -90),
                     Spell(3, "Strength in numbers", "Give a minion +2/+3 and draw a creature", -91),
                     Spell(3, "Animal Battle Companion", "Summon a random war animal", -92),
                     Creature(6, "Khevtuul", 5, 7, "Desperate summon 2 2/2 Night Watchers", "soldier", -93),
                     Spell(8, "War Pack", "Summon all war animals", -94),
                     Creature(4, "Animal Tamer", 3, 4, "Give a friendly animal +2/+2 and guard", "worker", -95),
                     Creature(4, "Mother Wolf", 3, 3, "Desperate summ 2 1/1 Wolf Pup", "animal", -96),
                     Creature(1, "Domestic cat", 1, 1, "Summon a 1/1 Wild Cat", "animal", -97),
                     Creature(2, "Goat", 1, 1, "Desperate summon a 3/2 Hungry Wolf", "animal", -98),
                     Spell(4, "Tag Team", "Dela 3 damage to a minion summ a 3/3 Hunting dog", -99),
                     Creature(5, "Church Builder", 6, 4, "Restore 8 health", "worker", -100),
                     Spell(9, "Call of God", "Heal for 8 and summon a 8/8 armored guard Crusader", -101),
                     Creature(11, "Covered Battering Ram", 8, 8, "Cost 1 less for each minion on the battlefield",
                              "machine", -102),
                     Creature(10, "Battering Ram", 8, 8, "Cost 1 less for each friendly minion on the battlefield",
                              "machine", -103),
                     Creature(1, "City Gate Guard", 3, 1, "Guard", "ancient", -104),
                     Spell(3, "Ancient Tactics", "Draw 3 cards deal 3 damage to your kingdom", -105),
                     Creature(1, "Mesopotamia Scholar", 1, 2, "Draw a card Deal 2 damage to your kingdom", "ancient",
                              -106),
                     Creature(9, "King Saragon of Akkad", 7, 9,
                              "Give all ancients +2/+2 your knigdom can't take damage", "ancient", -107),
                     Creature(2, "Military Guard", 4, 2, "Guard Deal 2 damage to your kingdom", "ancient", -108),
                     Creature(1, "Lu", 2, 3, "Deal 2 damage to your kingdom", "ancient", -109),
                     Spell(4, "Mercenaries Reinforcements", "Deal 2-4 damage and summ that many Man at arms", -110),
                     Creature(5, "Assyrian Horserider", 7, 5, "Charge discard 2 cards from your hand", "ancient", -111),
                     Spell(6, "Tactical Coordination", "When you discard or use this draw 3 cards", -112),
                     Creature(9, "Turtanu", 9, 3, "Guard Desperate Summon 3 City Gate Guards", "ancient", -113),
                     Creature(3, "Prisoner of War", 4, 3, "If you discard this summon it", "ancient", -114),
                     Creature(8, "Carcassonne", 8, 8,
                              "Can't attack. Deal 8 damage to a random enemy at the end of your turn", "building",
                              -115),
                     Creature(2, "Countryside Hunter", 3, 2, "Give a friendly worker +1/+1", "worker", -116),
                     Creature(5, "Landlord", 3, 4, "Draw 3 workers", "worker", -117),
                     Creature(2, "Shepherd", 2, 1, "Summon a 1/1 guard dog with guard", "worker", -118),
                     Creature(2, "Peasant Fighter", 2, 3, "If you have another worker get +1/+1", "worker", -119),
                     Creature(1, "New Recruit", 2, 1, "When you play a soldier give this +1 attack", "soldier", -120),
                     Creature(7, "Wondering Scribe", 4, 4, "When you cast a spell draw a card", "worker", -121),
                     Creature(1, "Heretic Knight", 1, 2, "Armored deal 2 damage to your kingdom", "knight", -122),
                     Creature(2, "Armored Peasant", 2, 1, "Armored Guard", "soldier", -123),
                     Creature(6, "Rich Peasant", 1, 2, "Summon 2 armored Peasant with guard and armored", "worker",
                              -124),
                     Creature(9, "Graf", 6, 3,
                              "Guard Armored Desperate Summon 3 Armored Peasant with guard and armored", "soldier",
                              -125),
                     Creature(10, "Margrave", 6, 4, "Guard Armored Cost 1 less for other each card in your hand",
                              "knight", -126),
                     Spell(2, "Warhammer", "Break an enemy armor making him lose all attributes", -127),
                     Creature(3, "Voice of the emperor", 4, 3, "Set a minion attack and health to 3", "soldier", -128),
                     Creature(3, "Bailiff", 3, 3, "Set a minion attack to 1", "soldier", -129),
                     Creature(3, "Big Game Beast", 3, 3, "Desperate draw an animal", "animal", -130),
                     Spell(3, "Defending  the empire", "Summon 3 Kaiserliche and put a 1/4 Defence", -131),
                     Creature(2, "Mercenary Recruiter", 2, 2, "Draw a mercenary", "mercenary", -132),
                     Creature(4, "Mercenary defender", 5, 2, "Guard put an 3/2 defence", "mercenary", -133),
                     Creature(5, "Architecti", 5, 5, "Add 5 Defenses to your kingdom", "worker", -134),
                     Creature(4, "Mercenary Champion", 7, 7, "Debt(2)", "soldier", -135),
                     Creature(2, "Mercenary soldier", 4, 3, "Debt(1)", "soldier", -136),
                     Creature(5, "Mercenary elite Defender", 8, 7, " Guard Debt(2)", "soldier", -137),
                     Creature(4, "Mercenary Herbalist", 6, 4, "Restore 6 health Debt(1)", "worker", -138),
                     Defence(5, "Mercenary's Troops", 2, 8, "Debt(2)", -139),
                     Creature(2, "Byzantium Engineer", 2, 2, "Draw a Defence", "worker", -140),
                     Creature(2, "Wealthy Nobel", 2, 3, "Pays all debt", "worker", -141),
                     Creature(9, "Wild Elephant", 7, 9, "Deal 4 damage", "animal", -142),
                     Creature(4, "Local Healer", 4, 4, "Restore 4 health", "worker", -143),
                     Creature(3, "Clergy", 3, 3, "Restore 3 health", "worker", -144),
                     Creature(7, "Local Bodyguard", 8, 6, "Guard", "worker", -145),
                     Creature(1, "Banner holder", 2, 1, "Give your hand +1 health", "soldier", -146),
                     Creature(9, "Sleepy Guard", 12, 4, "Guard", "soldier", -147),
                     Creature(1, "Mercenary employer", 2, 1, "Add a random mercenary to your hand", "mercenary", -148),
                     Creature(1, "Army Cook", 1, 2, "Add 2 Kaiserliche to your hand", "worker", -149),
                     Creature(1, "Mercenary emissary", 1, 2, "Add a random debt to your hand", "worker", -150),
                     Creature(2, "Army Recruiter", 3, 2, "Add a random soldier to your hand", "soldier", -151),
                     Creature(1, "Lure animal", 1, 1, "Desperate add a random animal to your hand", "animal", -152),
                     Creature(7, "Empire Crusader", 7, 7, "Add 5 Holy Roman Empire cards to your hand", "knight", -153),
                     Spell(2, "Build defences", "Gain 5 Defenses and draw a card", -154),
                     Spell(2, "Palisade Wall", "Deal 3 damage gain 3 defences", -155),
                     Spell(2, "Guard the Fort", "Gain 3 defences and summon a 2/3 Fort Guard", -156),
                     Creature(3, "Inspired soldier", 5, 2, "If you are holding a spell gain armored and guard",
                              "soldier", -157),
                     Spell(6, "Emperor's Hope", "Restore 8 health and draw 3 cards", -158),
                     Spell(1, "Emperor's Will", "Give a minion +1/+2 and Armored if you hold a knight", -159),
                     ]
