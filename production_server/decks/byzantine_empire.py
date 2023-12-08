from clases.creatures import Creature
from clases.spells import Spell
from clases.Defence import Defence

cards_for_byzantine_empire = [
    Spell(6, "Peace Treaty", "Return all creature form the battlefield to their owners hands.", -36),
    Creature(4, "Pronoiar", 3, 3, "Charge", "soldier", -37),
    Creature(2, "Akritoi", 3, 2, "Guard", "soldier", -38),
    Creature(7, "Cataphract", 6, 6, "Guard Armored", "knight", -39),
    Spell(5, "Wealthy Empire", "Summon 2 random cards from your deck", -40),
    Spell(2, "Ancient Empire", "Draw 2 cards Debt(1)", -43),
    Creature(2, "Watchman", 2, 1, "Draw a guard card", "worker", -60),
    Creature(2, "Watchtower", 2, 1, "All your guards get +1/+2", "building", -61),
    Spell(7, "Landslide", "Deal 7 damage to ALL minions", -63),
    Spell(2, "Roman Formation Circular", "Give your minions on the filed Guard", -65),
    Spell(3, "Guard Duty", "Give a friendly minion +2/+2 if it is a Guard draw a card", -66),
    Spell(3, "Boarder Guards", "Summon 2 Akritoi Debt(1)", -68),
    Spell(1, "Roman Formation Phalanx", "Give your minions +1/+1 Debt(1)", -71),
    Creature(8, "Basil II", 6, 5, "Armored Charge Guard", "soldier", -76),
    Creature(5, "Protokentarchos", 4, 4, "Give a friendly minion +3/+3 Debt(1)", "soldier", -77),
    Spell(2, "Old Tactics", "Draw a card and reduce it is cost by 3", -79),
    Spell(1, "Pilum Throw", "Deal 3 damage Debt(1)", -83),
    Spell(3, "Fast Conscription", "Summon 4 1/1 Peasant", -84),
    Creature(4, "Lost Noble", 1, 1, "Desperate Summon a 3/5 City guard", "worker", -85),
    Spell(3, "Strength in numbers", "Give a minion +2/+3 and draw a creature", -91),
    Creature(4, "Mercenary Champion", 7, 7, "Debt(2)", "soldier", -135),
    Creature(2, "Mercenary soldier", 4, 3, "Debt(1)", "soldier", -136),
    Creature(5, "Mercenary elite Defender", 8, 7, "Guard Debt(2)", "soldier", -137),
    Creature(4, "Mercenary Herbalist", 6, 4, "Restore 6 health Debt(1)", "worker", -138),
    Defence(5, "Mercenary's Troops", 2, 8, "Debt(2)", -139),
    Creature(2, "Byzantium Engineer", 2, 2, "Draw a Defence", "worker", -140),
    Creature(2, "Wealthy Nobel", 2, 3, "Pays all debt", "worker", -141),
    Creature(1, "Mercenary emissary", 1, 2, "Add a random debt to your hand", "worker", -150),
    Creature(2, "Army Recruiter", 3, 2, "Add a random soldier to your hand", "soldier", -151),
    Creature(6, "Heavy Arbalest", 5, 6, "Deal 4 damage", "soldier", -186),
    Creature(3, "Herbalist Guard", 4, 2, "Guard Restore 3 health", "soldier", -187),
]
cards_byzantine_show = [
    Spell(6, "Peace Treaty", "Return all creature form the battlefield to their owners hands.", -36),
    Creature(4, "Pronoiar", 3, 3, "Charge", "soldier", -37),
    Creature(2, "Akritoi", 3, 2, "Guard", "soldier", -38),
    Creature(7, "Cataphract", 6, 6, "Guard Armored", "knight", -39),
    Spell(5, "Wealthy Empire", "Summon 2 random cards from your deck", -40),
    Spell(2, "Ancient Empire", "Draw 2 cards Debt(1)", -43),
    Creature(2, "Watchman", 2, 1, "Draw a guard card", "worker", -60),
    Creature(2, "Watchtower", 2, 1, "All your guards get +1/+2", "building", -61),
    Spell(7, "Landslide", "Deal 7 damage to ALL minions", -63),
    Spell(2, "Roman Formation Circular", "Give your minions on the filed Guard", -65),
    Spell(3, "Guard Duty", "Give a friendly minion +2/+2 if it is a Guard draw a card", -66),
    Spell(3, "Boarder Guards", "Summon 2 Akritoi Debt(1)", -68),
    Spell(1, "Roman Formation Phalanx", "Give your minions +1/+1 Debt(1)", -71),
    Creature(8, "Basil II", 6, 5, "Armored Charge Guard", "soldier", -76),
    Creature(5, "Protokentarchos", 4, 4, "Give a friendly minion +3/+3 Debt(1)", "soldier", -77),
    Spell(2, "Old Tactics", "Draw a card and reduce it is cost by 3", -79),
    Spell(1, "Pilum Throw", "Deal 3 damage Debt(1)", -83),
    Spell(3, "Fast Conscription", "Summon 4 1/1 Peasant", -84),
    Creature(4, "Lost Noble", 1, 1, "Desperate Summon a 3/5 City guard", "worker", -85),
    Spell(3, "Strength in numbers", "Give a minion +2/+3 and draw a creature", -91),
    Creature(4, "Mercenary Champion", 7, 7, "Debt(2)", "soldier", -135),
    Creature(2, "Mercenary soldier", 4, 3, "Debt(1)", "soldier", -136),
    Creature(5, "Mercenary elite Defender", 8, 7, "Guard Debt(2)", "soldier", -137),
    Creature(4, "Mercenary Herbalist", 6, 4, "Restore 6 health Debt(1)", "worker", -138),
    Defence(5, "Mercenary's Troops", 2, 8, "Debt(2)", -139),
    Creature(2, "Byzantium Engineer", 2, 2, "Draw a Defence", "worker", -140),
    Creature(2, "Wealthy Nobel", 2, 3, "Pays all debt", "worker", -141),
    Creature(1, "Mercenary emissary", 1, 2, "Add a random debt to your hand", "worker", -150),
    Creature(2, "Army Recruiter", 3, 2, "Add a random soldier to your hand", "soldier", -151),
    Creature(6, "Heavy Arbalest", 5, 6, "Deal 4 damage", "soldier", -186),
    Creature(3, "Herbalist Guard", 4, 2, "Guard Restore 3 health", "soldier", -187),
]
