import random

from clases.creatures import *
from decks.lists_of_cards import *
from clases.Item import list_of_item
from clases.game_logics import *


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
        self.empire = ""
        self.used_power = 0

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
                if card.name in list_of_creature_that_are_affected_by_hand and len(self.battle_field) < 7:
                    self.hand_check(card)
                if card.name in list_of_creature_description and len(self.battle_field) < 7:
                    self.mana_pay(card)
                    self.battle_field.append(card)
                    self.incoming_action = 2
                    self.active_minion = card
                    return 2
                elif card.name in list_of_creature_that_draw_cards and len(self.battle_field) < 7:
                    for nr_cards in range(list_of_creature_that_draw_cards.get(card.name)):
                        if card.name in list_of_creature_that_draw_specific_cards:
                            try:
                                random_card = self.get_random_card(card)
                                if random_card is not None:
                                    self.hand.append(random_card)
                                    self.deck.remove(random_card)
                            except Exception as e:
                                print(e)
                        else:
                            self.draw_card()
                elif card.name in list_of_creature_that_add_mana and len(self.battle_field) < 7:
                    self.mana_increase(list_of_creature_that_add_mana.get(card.name))
                    if self.empty_mana + list_of_creature_that_add_mana.get(card.name) > 10:
                        self.empty_mana = 10
                    else:
                        self.empty_mana += list_of_creature_that_add_mana.get(card.name)
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
                elif card.name in list_of_creature_with_on_going_effect and len(self.battle_field) < 7:
                    self.ongoing_effects.append(card)
                elif card.name in list_of_creature_that_summon and len(self.battle_field) < 7:
                    self.battle_field.append(card)
                    self.mana_pay(card)
                    if len(self.battle_field) < 7:
                        for i in range(list_of_creature_that_summon.get(card.name)[0]):
                            if len(self.battle_field) < 7:
                                self.battle_field.append(list_of_creature_that_summon.get(card.name)[1][i])
                                list_of_creature_that_summon.get(card.name)[1].remove(
                                    list_of_creature_that_summon.get(card.name)[1][i])
                    return 1
                elif card.name in list_of_creature_that_affect_all and len(self.battle_field) < 7:
                    self.buff_all_cards(card)
                elif card.name in list_of_creature_that_affect_battle_field and len(self.battle_field) < 7:
                    self.buff_all_in_battle(card)
                elif len(self.battle_field) == 7:
                    return 0
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
            self.card_in_hand_effect()
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
        self.deck = []
        for card in deck:
            self.deck.append(card)

    def get_random_card(self, card):
        try:
            random_card = random.choice(self.deck)
            nr_try = 0
            type_of_card = list_of_creature_that_draw_specific_cards.get(card.name)[0][0]
            list_of_creature_that_draw_specific_cards.get(card.name)[0].pop(0)
            type_of_description = list_of_creature_that_draw_specific_cards.get(card.name)[1][0]
            list_of_creature_that_draw_specific_cards.get(card.name)[1].pop(0)
            if type_of_description == "":
                while type_of_card != random_card.card_type and nr_try < 30:
                    random_card = random.choice(self.deck)
                    nr_try += 1
                if nr_try == 30:
                    for charge in self.deck:
                        if type_of_description in charge.description.split():
                            random_card = charge
                if type_of_card == random_card.card_type:
                    return random_card
            else:
                if any(type_of_description in obj.description.split() for obj in self.deck):
                    while (
                            type_of_card != random_card.card_type or type_of_description not in random_card.description.split()) and nr_try < 30:
                        random_card = random.choice(self.deck)
                        nr_try += 1
                    if nr_try == 30:
                        for charge in self.deck:
                            if type_of_description in charge.description.split():
                                random_card = charge
                    if type_of_card == random_card.card_type and type_of_description in random_card.description.split():
                        return random_card
        except Exception as e:
            print(e)

    @staticmethod
    def battle_fields_effects(player, enemy_player):
        Player.check_for_active_effects(player, enemy_player)
        if len(player.ongoing_effects) > 0:
            for effect in player.ongoing_effects:
                if effect.name in list_of_creature_with_negative_on_going_effect:
                    for creature in enemy_player.battle_field:
                        creature.negative_effects_from_creatures(effect,
                                                                 list_of_creature_with_negative_on_going_effect.get(
                                                                     effect.name), player)
                elif effect.name in list_of_creature_with_positive_on_going_effect:
                    for creature in player.battle_field:
                        creature.positive_effects_from_creatures(effect,
                                                                 list_of_creature_with_positive_on_going_effect.get(
                                                                     effect.name), player)
        if len(enemy_player.ongoing_effects) > 0:
            for effect in enemy_player.ongoing_effects:
                if effect.name in list_of_creature_with_negative_on_going_effect:
                    for creature in player.battle_field:
                        creature.negative_effects_from_creatures(effect,
                                                                 list_of_creature_with_negative_on_going_effect.get(
                                                                     effect.name), player)
                elif effect.name in list_of_creature_with_positive_on_going_effect:
                    for creature in enemy_player.battle_field:
                        creature.positive_effects_from_creatures(effect,
                                                                 list_of_creature_with_positive_on_going_effect.get(
                                                                     effect.name), player)

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
        Player.clean_board(player, enemy_player)
        return effect_got_removed

    def effect_lost(self, card, enemy_player):
        if card.name in list_of_creature_with_negative_on_going_effect:
            for creature in enemy_player.battle_field:
                creature.reverse_effect_creature(card, list_of_creature_with_negative_on_going_effect.get(card.name), 1,
                                                 self)
        elif card.name in list_of_creature_with_positive_on_going_effect:
            for creature in self.battle_field:
                creature.reverse_effect_creature(card, list_of_creature_with_positive_on_going_effect.get(card.name),
                                                 -1,
                                                 self)
        else:
            for creature in self.battle_field:
                creature.reverse_effect_creature(card.name)

    @staticmethod
    def clean_board(player, enemy_player):
        try:
            for card in player.battle_field[:]:
                if card.hp <= 0 and card.card_type == "Creature":
                    player.battle_field.remove(card)
            for card in enemy_player.battle_field[:]:
                if card.hp <= 0 and card.card_type == "Creature":
                    enemy_player.battle_field.remove(card)
        except Exception as e:
            print(e)

    def buff_card_from_hand(self, card, buffing_card):
        card.hp += list_of_creature_that_buff.get(buffing_card.name)[0]
        card.max_hp += list_of_creature_that_buff.get(buffing_card.name)[0]
        card.attack += list_of_creature_that_buff.get(buffing_card.name)[1]
        if list_of_creature_that_buff.get(buffing_card.name)[2] not in card.description:
            card.description += " " + list_of_creature_that_buff.get(buffing_card.name)[2]
        card.check_creature()

    def hand_check(self, card):
        if "empty hand" in list_of_creature_that_are_affected_by_hand.get(card.name)[0] and len(self.hand) == 1 and \
                list_of_creature_that_are_affected_by_hand.get(card.name)[1] == "buff":
            self.buff_card_from_hand(card, card)

        elif "affects hand" in list_of_creature_that_are_affected_by_hand.get(card.name)[0] and len(self.hand) > 1 and \
                list_of_creature_that_are_affected_by_hand.get(card.name)[1] == "buff":
            for creature in self.hand:
                if creature != card and creature.card_type == "Creature":
                    self.buff_card_from_hand(creature, card)

    def buff_all_cards(self, card):
        for creature in self.hand:
            if creature.card_type == "Creature" and list_of_creature_that_affect_all.get(
                    card.name) in creature.description.split():
                self.buff_card_from_hand(creature, card)
        for creature in self.battle_field:
            if creature.card_type == "Creature" and list_of_creature_that_affect_all.get(
                    card.name) in creature.description.split():
                self.buff_card_from_hand(creature, card)
        for creature in self.deck:
            if creature.card_type == "Creature" and list_of_creature_that_affect_all.get(
                    card.name) in creature.description.split():
                self.buff_card_from_hand(creature, card)

    def buff_all_in_battle(self, card):
        for creature in self.battle_field:
            if creature.card_type == "Creature":
                self.buff_card_from_hand(creature, card)

    def card_in_hand_effect(self):
        for creature in self.hand:
            if creature.name in list_of_creature_that_are_affected_in_hand:
                if list_of_creature_that_are_affected_in_hand.get(creature.name)[0] == "reduce":
                    if list_of_creature_that_are_affected_in_hand.get(creature.name)[1] != "":
                        pass
                    else:
                        self.hand[self.hand.index(creature)].mana_cost = self.hand[
                            self.hand.index(creature)].original_mana_cost
                        self.hand[self.hand.index(creature)].mana_cost -= len(self.hand) * \
                                                                     list_of_creature_that_are_affected_in_hand.get(
                                                                         creature.name)[2] - 1