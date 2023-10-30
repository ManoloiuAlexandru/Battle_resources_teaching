from ITschool_projects.battle_resources.clases.creatures import Creature


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 30
        self.mana = 0
        self.hand = []
        self.deck = []
        self.battle_field = []
        self.turn = 0
        self.problem = ""
        self.incoming_action = 0
        self.incoming_spell = None

    def mana_increase(self, amount):
        self.mana += amount
        if self.mana > 10:
            self.mana = 10

    def check_player(self):
        if self.hp <= 0:
            return 0
        return 1

    def __str__(self):
        return f"{self.name}"

    def put_card_on_field(self, card_picked):
        for card in self.hand:
            if card_picked.get(card.name_for_html) is not None and card.mana_cost <= self.mana:
                if card.name == "Two-handed Knight":
                    self.hand.remove(card)
                    self.battle_field.append(card)
                    self.mana_increase(-card.mana_cost)
                    self.incoming_action = 2
                    return 2
                elif card.name == "Arrow shot":
                    self.hand.remove(card)
                    self.mana_increase(-card.mana_cost)
                    self.incoming_action = 3
                    self.incoming_spell = card
                    return 3
                self.hand.remove(card)
                self.battle_field.append(card)
                self.mana_increase(-card.mana_cost)
                return 1
        return 0

    def check_battlefield(self):
        for card in self.battle_field:
            if card.hp <= 0:
                self.battle_field.remove(card)
