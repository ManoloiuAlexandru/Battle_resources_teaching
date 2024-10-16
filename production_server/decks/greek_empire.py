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
                    Spell(6, "Ballestris Volly", "Deals 2 damage to all enemy minions and knocks them down", -303),
                    ]
cards_for_greek_empire = [Spell(2, "Greek Scrolls", "Discover a spell and reduce it is mana cost by 2", -296),
                          Spell(4, "Flaming arrow", "Deal 6 damage", -297),
                          Creature(5, "Veteran Tactician", 4, 4, "Deal 6 damage if you control a tactic", "soldier",
                                   -298),
                          Spell(3, "Cultural Empire", "Draw 2 cards", -299),
                          Spell(2, "Net Throw", "Deal 3 damage to creature and knocks it down", -300),
                          Spell(7, "Spartan Volley", "Deal 5 damage to all enemies", -301),
                          Creature(2, "Sparatan Auxiliars", 2, 3, "Add 2 1/2 Auxiliars to your hand", "soldier", -302),
                          Spell(6, "Ballestris Volly", "Deals 2 damage to all enemy minions and knocks them down",
                                -303),
                          ]
