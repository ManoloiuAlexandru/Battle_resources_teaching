import random

from clases.creatures import list_of_creature_description
from clases.spells import list_of_spells


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
        self.active_minion = None
        self.attacking_minion = None

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
                if card.name in list_of_creature_description:
                    self.mana_pay(card)
                    self.battle_field.append(card)
                    self.incoming_action = 2
                    self.active_minion = card
                    return 2
                elif card.name in list_of_spells:
                    self.mana_pay(card)
                    self.incoming_action = 3
                    self.incoming_spell = card
                    return 3
                self.battle_field.append(card)
                self.mana_pay(card)
                return 1
        return 0

    def check_battlefield(self):
        for card in self.battle_field[:]:
            if card.hp <= 0:
                self.battle_field.remove(card)

    def mana_pay(self, card):
        self.hand.remove(card)
        self.mana_increase(-card.mana_cost)

    def draw_card(self):
        try:
            pick_card = random.choice(self.deck)
            if len(self.hand) < 10:
                self.hand.append(pick_card)
            self.deck.remove(pick_card)
        except Exception as e:
            print(e)
            if len(self.deck) == 0:
                self.hp -= 1

    def start_game(self):
        try:
            for i in range(0, 5):
                self.draw_card()
        except Exception as e:
            print(e)
