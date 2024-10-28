from production_server.clases.Defence import Defence
from production_server.clases.creatures import Creature
from production_server.clases.spells import Spell

cards_greek_show = [Spell(2, "Greek Scrolls", "Discover a spell and reduce it is mana cost by 2", -296),
                    Spell(4, "Flaming arrow", "Deal 6 damage", -297),
                    Creature(5, "Veteran Tactician", 4, 4, "Deal 6 damage if you control a tactic", "soldier", -298),
                    Spell(3, "Cultural Empire", "Draw 2 cards", -299),
                    Spell(2, "Net Throw", "Deal 3 damage to creature and knocks it down", -300),
                    Spell(7, "Spartan Volley", "Deal 5 damage to all enemies", -301),
                    Creature(2, "Sparatan Auxiliars", 2, 3, "Add 2 1/2 Auxiliars to your hand", "soldier", -302),
                    Spell(6, "Ballestris Volly", "Deals 2 damage to all enemies and knocks them down", -303),
                    Spell(3, "Elephants stampede", "Knocks down all enemies", -304),
                    Spell(10, "Catapult Shot", "Deal 10 damage", -305),
                    Spell(3, "Lagoras discovery",
                          "Tactic After your opponent plays a minion deal 6 damage to it and the rest to the kingdom",
                          -306),
                    Spell(2, "Scrolls of war", "Deal 2 damage and discover a spell", -307),
                    Creature(6, "Opportunistic  Hoplite", 6, 6, "Cost 3 less for each tactic", "soldier", -308),
                    Creature(4, "Sling Shooter", 6, 3, "Knock down any character damaged by this", "soldier", -309),
                    Creature(6, "Greek Peasant Recruiter", 5, 5, "Summon a random 3 cost minion", "soldier", -310),
                    Creature(7, "Pyrrho of Elis", 7, 5, "When you cast a spell add a Flaming arrow to your hand",
                             "worker", -311),
                    Creature(5, "Alexander I", 8, 2, "If you are holding a knight discover a powerful Greek attack",
                             "knight", -312),
                    Spell(2, "Auxiliar Volley", "Deal 1 damage to all enemies", -313)
                    ]
cards_for_greek_empire = [Spell(2, "Greek Scrolls", "Discover a spell and reduce it is mana cost by 2", -296),
                          Spell(4, "Flaming arrow", "Deal 6 damage", -297),
                          Creature(5, "Veteran Tactician", 4, 4, "Deal 6 damage if you control a tactic", "soldier",
                                   -298),
                          Spell(3, "Cultural Empire", "Draw 2 cards", -299),
                          Spell(2, "Net Throw", "Deal 3 damage to creature and knocks it down", -300),
                          Spell(7, "Spartan Volley", "Deal 5 damage to all enemies", -301),
                          Creature(2, "Sparatan Auxiliars", 2, 3, "Add 2 1/2 Auxiliars to your hand", "soldier", -302),
                          Spell(6, "Ballestris Volly", "Deals 2 damage to all enemies and knocks them down",
                                -303),
                          Spell(3, "Elephants stampede", "Knocks down all enemies", -304),
                          Spell(10, "Catapult Shot", "Deal 10 damage", -305),
                          Spell(3, "Lagoras discovery",
                                "Tactic After your opponent plays a minion deal 6 damage to it and the rest to the kingdom",
                                -306),
                          Spell(2, "Scrolls of war", "Deal 2 damage and discover a spell", -307),
                          Creature(6, "Opportunistic  Hoplite", 6, 6, "Cost 3 less for each tactic", "soldier", -308),
                          Creature(4, "Sling Shooter", 6, 3, "Knock down any character damaged by this", "soldier",
                                   -309),
                          Creature(6, "Greek Peasant Recruiter", 5, 5, "Summon a random 3 cost minion", "soldier",
                                   -310),
                          Creature(7, "Pyrrho of Elis", 7, 5, "When you cast a spell add a Flaming arrow to your hand",
                                   "worker", -311),
                          Creature(5, "Alexander I", 8, 2,
                                   "If you are holding a knight discover a powerful Greek attack",
                                   "knight", -312),
                          Spell(2, "Auxiliar Volley", "Deal 1 damage to all enemies", -313)
                          ]
