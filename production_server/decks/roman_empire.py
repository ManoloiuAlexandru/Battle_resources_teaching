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
                Creature(3, "Mercenary Lieutenant", 3, 3, "Desperate deal 1 damage to all minions", "mercenary",
                         -177),
                Creature(2, "Inspiring mercenary", 2, 2, "Guard Desperate give all guards +1/+1", "mercenary", -178),
                Creature(2, "Apollodorus of Damascus", 2, 2, "Give all defences +1 attack", "worker", -179),
                Defence(3, "Mercenary's Auxiliar", 3, 2, "", -180)
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
                     Creature(3, "Mercenary Lieutenant", 3, 3, "Desperate deal 1 damage to all minions", "mercenary",
                              -177),
                     Creature(2, "Inspiring mercenary", 2, 2, "Guard Desperate give all guards +1/+1", "mercenary",
                              -178),
                     Creature(0, "Apollodorus of Damascus", 2, 2, "Give all defences +1 attack", "worker", -179),
                     Defence(3, "Mercenary's Auxiliar", 3, 2, "", -180)
                     ]
