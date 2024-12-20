from production_server.clases.creatures import Creature
from production_server.clases.spells import Spell
from production_server.clases.Defence import Defence

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
    Creature(4, "Mercenary Builder", 4, 6, "Rush Rebuilder debt(1)", "mercenary", -224),
    Creature(6, "Religious Leader", 8, 5, "Rush Rebuilder", "worker", -226),
    Creature(8, "Mercenary Leader", 14, 5, "Rebuilder Rush debt(2)", "mercenary", -228),
    Spell(1, "We don't take it personally",
          "Don't take or do damage to the enemy kingdom for 8 turns Reward Lndrau Aaurentis", -246),
    Creature(9, "Eager Fighter", 4, 3, "Rush Cost 1 less for each minion on the field", "soldier", -272),
    Spell(1, "Knock down", "Knocks down a target, draw a card", -274),
    Creature(2, "Ball-headed Mace Soldier", 2, 3, "Add a Knock down to your hand", "soldier", -275),
    Spell(3, "Mercenary Arrow Volley", "Deal 3 damage to all enemies minions Debt(1)", -276),
    Spell(5, "Fast Mercenary Recruiting", "Summon 2 5/4 Man at Arms with Rush Debt(1)", -277),
    Creature(5, "General Belisarius", 5, 5, "Guard Desperate add Imperial Guard to your deck",
             "soldier", -278),
    Creature(2, "Worker Recruiter", 3, 2, "When you play a worker add a random worker to your hand",
             "worker", -279),
    Creature(1, "Work Friend", 2, 1, "Summon a 1/1 Peasant", "worker", -280),
    Creature(6, "Soldier Commander", 5, 5, "Guard Cost 1 less for each soldier you summoned this game",
             "soldier", -281),
    Creature(10, "Torsion Catapult", 8, 8, "Cost 1 less for each soldier you summoned this game",
             "machine", -282),
    Creature(3, "Heraclius", 3, 3, "Pays all your debt and draws that many cards", "worker", -283),
    Spell(2, "Sling shot", "Deal 3-6 damage Debt(1)", -284),
    Creature(11, "Mercenary Battering Ram", 8, 8,
             "Cost 1 less for each mana crystal you spent on Debt this game",
             "mechanical", -285),
    Spell(0, "Mercenary arrow shot", "Deal 2 damage to a minion Debt(1)", -286),
    Spell(2, "War Cry", "Give a friendly minion +3/+3 deal 1 damage to ALL other minions Debt(1)", -294),
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
    Creature(4, "Mercenary Builder", 4, 6, "Rush Rebuilder debt(1)", "mercenary", -224),
    Creature(6, "Religious Leader", 8, 5, "Rush Rebuilder", "worker", -226),
    Creature(8, "Mercenary Leader", 14, 5, "Rebuilder Rush debt(2)", "mercenary", -228),
    Spell(1, "We don't take it personally",
          "Don't take or do damage to the enemy kingdom for 8 turns Reward Lndrau Aaurentis", -246),
    Creature(9, "Eager Fighter", 4, 3, "Rush Cost 1 less for each minion on the field", "soldier", -272),
    Spell(1, "Knock down", "Knocks down a target, draw a card", -274),
    Creature(2, "Ball-headed Mace Soldier", 2, 3, "Add a Knock down to your hand", "soldier", -275),
    Spell(3, "Mercenary Arrow Volley", "Deal 3 damage to all enemies minions Debt(1)", -276),
    Spell(5, "Fast Mercenary Recruiting", "Summon 2 5/4 Man at Arms with Rush Debt(1)", -277),
    Creature(5, "General Belisarius", 5, 5, "Guard Desperate add Imperial Guard to your deck",
             "soldier", -278),
    Creature(2, "Worker Recruiter", 3, 2, "When you play a worker add a random worker to your hand",
             "worker", -279),
    Creature(1, "Work Friend", 2, 1, "Summon a 1/1 Peasant", "worker", -280),
    Creature(6, "Soldier Commander", 5, 5, "Guard Cost 1 less for each soldier you summoned this game",
             "soldier", -281),
    Creature(10, "Torsion Catapult", 8, 8, "Cost 1 less for each soldier you summoned this game",
             "machine", -282),
    Creature(3, "Heraclius", 3, 3, "Pays all your debt and draws that many cards", "worker", -283),
    Spell(2, "Sling shot", "Deal 3-6 damage Debt(1)", -284),
    Creature(11, "Mercenary Battering Ram", 8, 8,
             "Cost 1 less for each mana crystal you spent on Debt this game",
             "mechanical", -285),
    Spell(0, "Mercenary arrow shot", "Deal 2 damage to a minion Debt(1)", -286),
    Spell(2, "War Cry", "Give a friendly minion +3/+3 deal 1 damage to ALL other minions Debt(1)", -294),
]
