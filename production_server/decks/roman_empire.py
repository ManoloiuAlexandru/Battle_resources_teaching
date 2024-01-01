from clases.creatures import Creature
from clases.spells import Spell

from clases.Defence import Defence

roman_empire = [Creature(2, "Mercenary Recruiter", 2, 2, "Draw a mercenary", "mercenary", -132),
                Creature(4, "Mercenary defender", 5, 2, "Guard put an 3/2 defence", "mercenary", -133),
                Creature(5, "Architecti", 5, 5, "Add 5 Defenses to your kingdom", "worker", -134),
                Creature(1, "Mercenary employer", 2, 1, "Add a random mercenary to your hand", "mercenary", -148),
                Spell(2, "Build defences", "Gain 5 Defenses and draw a card", -154),
                Spell(2, "Palisade Wall", "Deal 3 damage gain 3 defences", -155),
                Spell(2, "Guard the Fort", "Gain 3 defences and summon a 2/3 Fort Guard", -156),
                Creature(2, "Mercenary Charger", 3, 2,
                         "If you're holding a knight and gain +1 attack and charge", "mercenary",
                         -162),
                Creature(3, "Mercenary Lieutenant", 3, 3, "Deal 1 damage to all other minions", "mercenary",
                         -177),
                Creature(2, "Inspiring mercenary", 2, 2, "Guard Desperate give all guards +1/+1", "mercenary", -178),
                Creature(2, "Apollodorus of Damascus", 2, 2, "Give all defences +1 attack", "worker", -179),
                Defence(3, "Mercenary's Auxiliar", 3, 2, "", -180),
                Creature(2, "Roman Architect", 4, 1, "Gain 1 defence when a friendly mininon takes damage",
                         "worker", -181),
                Spell(1, "Pilum Volley", "Deal 1 damage to ALL minions", -182),
                Creature(1, "Rusticus Recruiter", 1, 1, "Put an 1/3 defence", "worker", -183),
                Creature(2, "Aedile", 7, 0, "Guard", "soldier", -184),
                Creature(2, "Harsh Trainer", 3, 2, "Deal 1 damage to a minion and give it +2 attack", "worker", -185),
                Creature(5, "Tiberius", 5, 3, "Draw a mercenary,knight and worker", "worker", -189),
                Creature(8, "Nero", 9, 4, "Charge +6 attack while damaged", "worker", -190),
                Creature(4, "Nero's Guard", 6, 2, "Guard +3 attack while damaged", "soldier", -191),
                Spell(2, "Recruiting", "Add 2 random knights", -192),
                Creature(3, "Roman Guard", 4, 3, "Guard", "soldier", -193),
                Spell(3, "Unknown Territory", "Spend all your defences to deal that much damage to ALL minions",
                      -194),
                Creature(4, "Full Armored Legionary", 5, 4,
                         "Guard Deal damage equal to your defences to an enemy minion", "knight",
                         -195),
                Spell(10, "Senatus Populusque Romanus",
                      "Deal 2 damage to ALL minions cost 1 less for each defences you have", -196),
                Spell(1, "Known Territory", "Deal 1 damage to a minion for each defence you have", -197),
                Creature(3, "City Defender", 4, 2, "If you kingdom has defences gain +2/+2", "soldier", -198),
                Creature(2, "Frenzied Mercenary", 4, 2, "Has charge and +2 attack while damaged", "mercenary",
                         -207),
                Creature(5, "Heavy Armored Mercenary", 5, 5, "If you are holding a knight get 5 defence", "knight",
                         -208),
                Spell(4, "Mercenary Defences",
                      "Deal 5 damage to a minion if you are holding a knight gain 5 defences", -209),
                Spell(2, "Commander Desperation", "Deal 1 damage to ALL minions, if you have 13 or less hp deal 3",
                      -210),
                Spell(4, "Commander's last charge", "Deal 4 damage if you have less then 12 health deal 6", -211),
                Spell(0, "Whip hit", "Deal 1 damage to a minion and give it +2 attack", -212),
                Creature(2, "Auxiliar Defender", 3, 2, "If you have a defence gain +1/+1", "mercenary", -213),
                Spell(1, "Fall Trap", "Deal 2 damage to a minion gain 2 defence", -214),
                Spell(1, "Vast Empire", "Recruit a mercenary if you have 10 mana keep all 3 cards", -215),
                Creature(2, "Frightened Girl", 3, 2, "Guard Recruit a guard", "worker", -217),
                Creature(1, "War Crier", 2, 1, "Draw a rush card from your deck", "worker", -218),
                Creature(7, "Julius Caesar", 6, 7,
                         "Rush Gain 4 defences desperate Lose 4 defences to resummon this", "mercenary",
                         -219),
                Spell(5, "Tavern Fight", "Destroy all creatures except one", -220),
                Spell(1, "Execute", "Destroy a damaged minion", -221),
                Spell(1, "Shield of Honor", "Give a damaged minion +3 attack and Armored", -222),
                Spell(1, "Get back to work",
                      "Deal 6 damage to a friendly minion in one turn without killing it Reward Ephix Maximus",
                      -247),
                Creature(3, "Louis the Pious", 2, 3,
                         "Set The health of all other minions to 1 Desperate deal 1 damage to all",
                         "knight", -250),
                Spell(10, "Boarder Skirmishes", "Deal 5 damage to ALL minions cost 1 less for each defence you have",
                      -269),
                Creature(4, "Caligula", 4, 4, "Rush Desperate add Claudius to your deck", "soldier", -292),
                Spell(3, "Swamped", "Destroy a damaged minion and knock down all minions", -293),
                Spell(2, "War Cry", "Give a friendly minion +3/+3 deal 1 damage to ALL other minions Debt(1)", -294),
                ]
roman_empire_show = [Creature(2, "Mercenary Recruiter", 2, 2, "Draw a mercenary", "mercenary", -132),
                     Creature(4, "Mercenary defender", 5, 2, "Guard put an 3/2 defence", "mercenary", -133),
                     Creature(5, "Architecti", 5, 5, "Add 5 Defenses to your kingdom", "worker", -134),
                     Creature(1, "Mercenary employer", 2, 1, "Add a random mercenary to your hand", "mercenary", -148),
                     Spell(2, "Build defences", "Gain 5 Defenses and draw a card", -154),
                     Spell(2, "Palisade Wall", "Deal 3 damage gain 3 defences", -155),
                     Spell(2, "Guard the Fort", "Gain 3 defences and summon a 2/3 Fort Guard", -156),
                     Creature(2, "Mercenary Charger", 3, 2,
                              "If you're holding a knight and gain +1 attack and charge", "mercenary",
                              -162),
                     Creature(3, "Mercenary Lieutenant", 3, 3, "Deal 1 damage to all other minions", "mercenary",
                              -177),
                     Creature(2, "Inspiring mercenary", 2, 2, "Guard Desperate give all guards +1/+1", "mercenary",
                              -178),
                     Creature(2, "Apollodorus of Damascus", 2, 2, "Give all defences +1 attack", "worker", -179),
                     Defence(3, "Mercenary's Auxiliar", 3, 2, "", -180),
                     Creature(2, "Roman Architect", 4, 1, "Gain 1 defence when a friendly mininon takes damage",
                              "worker", -181),
                     Spell(1, "Pilum Volley", "Deal 1 damage to ALL minions", -182),
                     Creature(1, "Rusticus Recruiter", 1, 1, "Put an 1/3 defence", "worker", -183),
                     Creature(2, "Aedile", 7, 0, "Guard", "soldier", -184),
                     Creature(2, "Harsh Trainer", 3, 2, "Deal 1 damage to a minion and give it +2 attack", "worker",
                              -185),
                     Creature(5, "Tiberius", 5, 3, "Draw a mercenary,knight and worker", "worker", -189),
                     Creature(8, "Nero", 9, 4, "Charge +6 attack while damaged", "worker", -190),
                     Creature(4, "Nero's Guard", 6, 2, "Guard +3 attack while damaged", "soldier", -191),
                     Spell(2, "Recruiting", "Add 2 random knights", -192),
                     Creature(3, "Roman Guard", 4, 3, "Guard", "soldier", -193),
                     Spell(3, "Unknown Territory", "Spend all your defences to deal that much damage to ALL minions",
                           -194),
                     Creature(4, "Full Armored Legionary", 5, 4,
                              "Guard Deal damage equal to your defences to an enemy minion", "knight",
                              -195),
                     Spell(10, "Senatus Populusque Romanus",
                           "Deal 2 damage to ALL minions cost 1 less for each defences you have", -196),
                     Spell(1, "Known Territory", "Deal 1 damage to a minion for each defence you have", -197),
                     Creature(3, "City Defender", 4, 2, "If you kingdom has defences gain +2/+2", "soldier", -198),
                     Creature(2, "Frenzied Mercenary", 4, 2, "Has charge and +2 attack while damaged", "mercenary",
                              -207),
                     Creature(5, "Heavy Armored Mercenary", 5, 5, "If you are holding a knight get 5 defence", "knight",
                              -208),
                     Spell(4, "Mercenary Defences",
                           "Deal 5 damage to a minion if you are holding a knight gain 5 defences", -209),
                     Spell(2, "Commander Desperation", "Deal 1 damage to ALL minions, if you have 13 or less hp deal 3",
                           -210),
                     Spell(4, "Commander's last charge", "Deal 4 damage if you have less then 12 health deal 6", -211),
                     Spell(0, "Whip hit", "Deal 1 damage to a minion and give it +2 attack", -212),
                     Creature(2, "Auxiliar Defender", 3, 2, "If you have a defence gain +1/+1", "mercenary", -213),
                     Spell(1, "Fall Trap", "Deal 2 damage to a minion gain 2 defence", -214),
                     Spell(1, "Vast Empire", "Recruit a mercenary if you have 10 mana keep all 3 cards", -215),
                     Creature(2, "Frightened Girl", 3, 2, "Guard Recruit a guard", "worker", -217),
                     Creature(1, "War Crier", 2, 1, "Draw a rush card from your deck", "worker", -218),
                     Creature(7, "Julius Caesar", 6, 7,
                              "Rush Gain 4 defences desperate Lose 4 defences to resummon this", "mercenary",
                              -219),
                     Spell(5, "Tavern Fight", "Destroy all creatures except one", -220),
                     Spell(1, "Execute", "Destroy a damaged minion", -221),
                     Spell(1, "Shield of Honor", "Give a damaged minion +3 attack and Armored", -222),
                     Spell(1, "Get back to work",
                           "Deal 6 damage to a friendly minion in one turn without killing it Reward Ephix Maximus",
                           -247),
                     Creature(3, "Louis the Pious", 2, 3,
                              "Set The health of all other minions to 1 Desperate deal 1 damage to all",
                              "knight", -250),
                     Spell(10, "Boarder Skirmishes",
                           "Deal 5 damage to ALL minions cost 1 less for each defence you have", -269),
                     Creature(4, "Caligula", 4, 4, "Rush Desperate add Claudius to your deck", "soldier", -292),
                     Spell(3, "Swamped", "Destroy a damaged minion and knock down all minions", -293),
                     Spell(2, "War Cry", "Give a friendly minion +3/+3 deal 1 damage to ALL other minions Debt(1)", -294),
                     ]
