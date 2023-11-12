import random

from clases.creatures import *
from clases.spells import list_of_spells

from clases.Item import list_of_item


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 30
        self.mana = 0
        self.empty_mana = 1
        self.hand = []
        self.deck = []
        self.battle_field = []
        self.turn = 0
        self.problem = ""
        self.incoming_action = 0
        self.incoming_spell = None
        self.active_minion = None
        self.active_item = None
        self.ongoing_effects = []
        self.logs = ""
        self.playing_deck_name = ""

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
                self.logs += "Playing:" + card.name + "\n"
                if card.name in list_of_creature_description:
                    self.mana_pay(card)
                    self.battle_field.append(card)
                    self.incoming_action = 2
                    self.active_minion = card
                    return 2
                elif card.name in list_of_creature_that_draw_cards:
                    for nr_cards in range(list_of_creature_that_draw_cards.get(card.name)):
                        self.draw_card()
                elif card.name in list_of_spells:
                    self.mana_pay(card)
                    self.incoming_action = 3
                    self.incoming_spell = card
                    return 3
                elif card.name in list_of_item:
                    self.mana_pay(card)
                    self.incoming_action = 4
                    self.active_item = card
                    return 4
                elif card.name in list_of_creature_with_on_going_effect:
                    self.ongoing_effects.append(card)
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

    def make_deck(self, deck):
        for card in deck:
            self.deck.append(card)

    @staticmethod
    def battle_fields_effects(player, enemy_player):
        Player.check_for_active_effects(player, enemy_player)
        if len(player.ongoing_effects) > 0:
            for effect in player.ongoing_effects:
                if effect.name in list_of_creature_with_negative_on_going_effect:
                    for creature in enemy_player.battle_field:
                        creature.negative_effects_from_creatures(effect)
                elif effect.name in list_of_creature_with_positive_on_going_effect:
                    for creature in player.battle_field:
                        creature.positive_effects_from_creatures(effect)
        if len(enemy_player.ongoing_effects) > 0:
            for effect in enemy_player.ongoing_effects:
                if effect.name in list_of_creature_with_negative_on_going_effect:
                    for creature in player.battle_field:
                        creature.negative_effects_from_creatures(effect)
                elif effect.name in list_of_creature_with_positive_on_going_effect:
                    for creature in enemy_player.battle_field:
                        creature.positive_effects_from_creatures(effect)

    @staticmethod
    def check_for_active_effects(player, enemy_player):
        effect_got_removed = 0
        for card in player.ongoing_effects:
            if card not in player.battle_field and card.card_type == "Creature":
                player.ongoing_effects.remove(card)
                player.effect_lost(card, enemy_player)
                effect_got_removed = 1
        for card in enemy_player.ongoing_effects:
            if card not in enemy_player.battle_field and card.card_type == "Creature":
                enemy_player.ongoing_effects.remove(card)
                enemy_player.effect_lost(card, player)
                effect_got_removed = 1
        return effect_got_removed

    def effect_lost(self, card, enemy_player):
        if card.name in list_of_creature_with_negative_on_going_effect:
            for creature in enemy_player.battle_field:
                creature.reverse_effect_creature(card)
        elif card.name in list_of_creature_with_positive_on_going_effect:
            for creature in self.battle_field:
                creature.reverse_effect_creature(card)
        else:
            for creature in self.battle_field:
                creature.reverse_effect_creature(card.name)
