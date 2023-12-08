import random

from clases.creatures import *
from decks.lists_of_cards import *
from clases.game_logics import *
from decks.lists_of_cards import *

from decks.decks_to_play import *


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
        self.active_defence = None
        self.ongoing_effects = []
        self.logs = ""
        self.playing_deck_name = ""
        self.empire = ""
        self.used_power = 0
        self.enemy_player = None
        self.immunity = False
        self.armor = 0
        self.fatigue = 1
        self.number_of_troops = 0
        self.nr_of_assaults = 0
        self.debt = 0
        self.last_debt = 0
        self.number_of_assaults = 1

    def mana_increase(self, amount):
        self.mana += amount
        if self.mana > 10:
            self.mana = 10

    def check_player(self):
        if self.hp <= 0:
            self.mana = 0
            self.battle_field.clear()
            self.deck.clear()
            self.hand.clear()
            return 0
        return 1

    def heal_player(self, amount):
        if self.hp + amount > 30:
            self.hp = 30
        else:
            self.hp += amount

    def __str__(self):
        return f"{self.name}"

    def put_card_on_field(self, card_picked):
        for card in self.hand[:]:
            if card_picked.get(card.name_for_html) is not None and card.mana_cost <= self.mana:
                self.check_for_creature_with_effect_on("summ", card)
                if card.name in list_of_cards_that_add_cards_to_your_hand:
                    self.add_random_card_to_hand(card)
                if card.name in list_of_card_that_pay_debt:
                    if self.last_debt > self.mana:
                        self.mana = self.empty_mana
                    else:
                        self.mana += self.last_debt
                    self.last_debt = 0
                if card.name in list_of_card_that_add_debt:
                    self.debt += list_of_card_that_add_debt.get(card.name)
                    self.last_debt = list_of_card_that_add_debt.get(card.name)
                if card.name in list_of_cards_that_give_armor:
                    self.armor += list_of_cards_that_give_armor.get(card.name)
                if card.name in list_of_cards_that_discard:
                    self.card_discard(list_of_cards_that_discard.get(card.name), card)
                    if self.incoming_spell is not None:
                        self.incoming_action = 3
                if card.name in list_of_creature_that_will_do_damage_to_your_kingdom:
                    self.hp -= list_of_creature_that_will_do_damage_to_your_kingdom.get(card.name)
                elif card.name in list_of_spells_that_do_damage_to_your_kingdom:
                    self.hp -= list_of_spells_that_do_damage_to_your_kingdom.get(card.name)
                self.logs += "Playing:" + card.name + "\n"
                if card.name in list_of_creature_that_can_make_kingdom_immun:
                    self.immunity = True
                if card.name in list_of_creature_that_are_affected_by_hand and len(self.battle_field) < 7:
                    self.hand_check(card)
                if card.name in list_of_creature_description and len(self.battle_field) < 7:
                    self.mana_pay(card)
                    self.battle_field.append(card)
                    self.incoming_action = 2
                    self.active_minion = card
                    return 2
                if card.name in list_of_creature_that_add_defence:
                    self.put_item_on(self.enemy_player, card)
                elif card.name in list_of_creature_that_draw_cards and len(self.battle_field) < 7:
                    for nr_cards in range(list_of_creature_that_draw_cards.get(card.name)):
                        if card.name in list_of_creature_that_draw_specific_cards:
                            try:
                                random_card = self.get_random_card(card, nr_cards)
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
                    self.check_for_creature_with_effect_on("cast spell", card)
                    self.check_spell(card)
                    self.mana_pay(card)
                    self.incoming_action = 3
                    self.incoming_spell = card
                    return 3
                elif card.name in list_of_defences:
                    self.mana_pay(card)
                    self.incoming_action = 4
                    self.active_defence = card
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
                    if card.name in list_of_creature_that_affect_all_when_die:
                        pass
                    else:
                        self.buff_all_cards(card)
                elif card.name in list_of_creature_that_affect_battle_field and len(self.battle_field) < 7:
                    self.buff_all_in_battle(card)
                elif len(self.battle_field) == 7:
                    return 0
                if card.name in list_of_creature_that_are_affected_by_battle_field:
                    self.buff_card_from_battle(card)
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
            if len(self.deck) == 0 and self.immunity is False:
                if self.armor == 0:
                    self.hp -= self.fatigue
                else:
                    self.armor -= self.fatigue
                self.fatigue += 1

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

    def get_random_card(self, card, index_of_card):
        try:
            random_card = random.choice(self.deck)
            nr_try = 0
            if self.incoming_spell is None:
                type_of_card, type_of_description, category = Player.card_to_draw_type(card, index_of_card)
            else:
                type_of_card = list_of_spells_that_draw_specific_cards.get(self.incoming_spell.name)[0][index_of_card]
                type_of_description = list_of_spells_that_draw_specific_cards.get(self.incoming_spell.name)[1][
                    index_of_card]
                category = None
            if type_of_description == "" and category == "":
                while type_of_card != random_card.card_type and nr_try < len(self.deck) + 1:
                    random_card = random.choice(self.deck)
                    nr_try += 1
                if nr_try == len(self.deck) + 1:
                    for charge in self.deck:
                        if type_of_description in charge.description.split():
                            random_card = charge
                if type_of_card == random_card.card_type:
                    return random_card
            elif category != "" and type_of_description == "":
                while category != random_card.category and nr_try < len(self.deck) + 1:
                    random_card = random.choice(self.deck)
                    nr_try += 1
                if nr_try == len(self.deck) + 1:
                    for charge in self.deck:
                        if category == charge.category:
                            random_card = charge
                if category == random_card.category:
                    return random_card
            else:
                if any(type_of_description in obj.description.split() for obj in self.deck):
                    while (
                            type_of_card != random_card.card_type or type_of_description not in random_card.description.split()) and nr_try < len(
                        self.deck) + 1:
                        random_card = random.choice(self.deck)
                        nr_try += 1
                    if nr_try == len(self.deck) + 1:
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
                                                                 list_of_creature_with_negative_on_going_effect, player)
                elif effect.name in list_of_creature_with_positive_on_going_effect:
                    for creature in player.battle_field:
                        creature.positive_effects_from_creatures(effect,
                                                                 list_of_creature_with_positive_on_going_effect, player)
        if len(enemy_player.ongoing_effects) > 0:
            for effect in enemy_player.ongoing_effects:
                if effect.name in list_of_creature_with_negative_on_going_effect:
                    for creature in player.battle_field:
                        creature.negative_effects_from_creatures(effect,
                                                                 list_of_creature_with_negative_on_going_effect, player)
                elif effect.name in list_of_creature_with_positive_on_going_effect:
                    for creature in enemy_player.battle_field:
                        creature.positive_effects_from_creatures(effect,
                                                                 list_of_creature_with_positive_on_going_effect, player)

    @staticmethod
    def check_for_active_effects(player, enemy_player):
        effect_got_removed = 0
        for card in player.ongoing_effects:
            if card.original_description in card.description.split("  "):
                if card not in player.battle_field and card.card_type == "Creature" and card.name in list_of_creature_that_can_make_kingdom_immun:
                    player.immunity = False
                if card not in player.battle_field and card.card_type == "Creature":
                    player.ongoing_effects.remove(card)
                    player.effect_lost(card, enemy_player)
                    effect_got_removed = 1
            else:
                player.ongoing_effects.remove(card)
                player.effect_lost(card, player)
                effect_got_removed = 1
        for card in enemy_player.ongoing_effects:
            if card.original_description in card.description.split("  "):
                if card not in enemy_player.battle_field and card.card_type == "Creature" and card.name in list_of_creature_that_can_make_kingdom_immun:
                    enemy_player.immunity = False
                if card not in enemy_player.battle_field and card.card_type == "Creature":
                    enemy_player.ongoing_effects.remove(card)
                    enemy_player.effect_lost(card, player)
                    effect_got_removed = 1
            else:
                enemy_player.ongoing_effects.remove(card)
                enemy_player.effect_lost(card, enemy_player)
                effect_got_removed = 1
        Player.clean_board(player, enemy_player)
        return effect_got_removed

    def effect_lost(self, card, enemy_player):
        if card.name in list_of_creature_with_negative_on_going_effect:
            for creature in enemy_player.battle_field:
                creature.reverse_effect_creature(card, list_of_creature_with_negative_on_going_effect, 1,
                                                 self)
        elif card.name in list_of_creature_with_positive_on_going_effect:
            for creature in self.battle_field:
                creature.reverse_effect_creature(card, list_of_creature_with_positive_on_going_effect,
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
                    if card.name in list_of_creature_that_do_somthing_when_die:
                        Player.action_when_die(player, card)
            for card in enemy_player.battle_field[:]:
                if card.hp <= 0 and card.card_type == "Creature":
                    enemy_player.battle_field.remove(card)
                    if card.name in list_of_creature_that_do_somthing_when_die:
                        Player.action_when_die(enemy_player, card)
        except Exception as e:
            print(e)

    @staticmethod
    def action_when_die(player, card):
        if card.original_description in card.description.split("  "):
            if list_of_creature_that_do_somthing_when_die.get(card.name) == "summ":
                if len(player.battle_field) < 7:
                    for i in range(list_of_creature_that_summ_after_they_die.get(card.name)[0]):
                        if len(player.battle_field) < 7:
                            player.battle_field.append(list_of_creature_that_summ_after_they_die.get(card.name)[1][i])
                            list_of_creature_that_summ_after_they_die.get(card.name)[1].remove(
                                list_of_creature_that_summ_after_they_die.get(card.name)[1][i])
            elif list_of_creature_that_do_somthing_when_die.get(card.name) == "draw":
                for nr_cards in range(list_of_creature_that_draw_cards_when_die.get(card.name)):
                    if card.name in list_of_creature_that_draw_specific_cards_when_die:
                        try:
                            random_card = player.get_random_card(card, nr_cards)
                            if random_card is not None:
                                player.hand.append(random_card)
                                player.deck.remove(random_card)
                        except Exception as e:
                            print(e)
                    else:
                        player.draw_card()
            elif list_of_creature_that_do_somthing_when_die.get(card.name) == "buff":
                random_minion = random.choice(player.battle_field)
                player.buff_card_from_hand(random_minion, card)
            elif list_of_creature_that_do_somthing_when_die.get(card.name) == "add_to_hand":
                player.add_random_card_to_hand(card)
            elif list_of_creature_that_do_somthing_when_die.get(card.name) == "add_armor":
                player.armor += list_of_creature_that_add_to_armor_when_die.get(card.name)
            elif "deal_damage" in list_of_creature_that_do_somthing_when_die.get(card.name).split(":"):
                if "all" in list_of_creature_that_do_somthing_when_die.get(card.name).split(":"):
                    player.deal_damage_to_all_creatures(card.name)
            elif list_of_creature_that_do_somthing_when_die.get(card.name) == "buffall":
                player.buff_all_cards(card)

    def deal_damage_to_all_creatures(self, name):
        for creature in self.battle_field:
            creature.hp -= list_of_creature_that_do_damage_to_all.get(name)
        for creature in self.enemy_player.battle_field:
            creature.hp -= list_of_creature_that_do_damage_to_all.get(name)

    def buff_card_from_hand(self, card, buffing_card):
        buff = list_of_creature_that_buff.get(buffing_card.name)
        if card.card_type == "Creature":
            card.hp += buff[0]
            card.max_hp += buff[0]
            card.attack += buff[1]
            if buff[2] not in card.description:
                card.description += "  " + buff[2]
            card.check_creature(buff[2])
        else:
            card.nr_of_assaults += buff[0]
            card.number_of_troops += buff[1]

    def hand_check(self, card):
        incoming_card = list_of_creature_that_are_affected_by_hand.get(card.name)
        if "empty hand" in incoming_card[0] and len(self.hand) == 1 and incoming_card[1] == "buff":
            self.buff_card_from_hand(card, card)

        elif "affects hand" in incoming_card[0] and len(self.hand) > 1 and incoming_card[1] == "buff":
            for creature in self.hand:
                if creature != card and creature.card_type == "Creature":
                    self.buff_card_from_hand(creature, card)
        elif "hand_check" in incoming_card[0].split(":"):
            for card_in_hand in self.hand:
                if card_in_hand != card:
                    if card_in_hand.card_type == incoming_card[0].split(":")[1] or card_in_hand.category == \
                            incoming_card[0].split(":")[1]:
                        if incoming_card[1] == "buff":
                            self.buff_card_from_hand(card, card)
                            break
                        if incoming_card[1].split(":")[0] == "change":
                            if incoming_card[1].split(":")[1] == "dmg":
                                list_of_creature_that_deal_dmg_to_enemies[card.name] = incoming_card[2]
                                if list_of_creature_that_deal_dmg_to_players.get(card.name) is not None:
                                    list_of_creature_that_deal_dmg_to_players[card.name] = incoming_card[2]
                                break

    def buff_all_cards(self, card):
        for creature in self.hand:
            if list_of_creature_that_affect_all.get(card.name)[1] == "":
                if creature.card_type == list_of_creature_that_affect_all.get(card.name)[0]:
                    self.buff_card_from_hand(creature, card)
            elif creature.card_type == list_of_creature_that_affect_all.get(
                    card.name)[0] and list_of_creature_that_affect_all.get(
                card.name)[1] in creature.description.split():
                self.buff_card_from_hand(creature, card)
        for creature in self.battle_field:
            if list_of_creature_that_affect_all.get(card.name)[1] == "":
                if creature.card_type == list_of_creature_that_affect_all.get(card.name)[0]:
                    self.buff_card_from_hand(creature, card)
            elif creature.card_type == list_of_creature_that_affect_all.get(
                    card.name)[0] and list_of_creature_that_affect_all.get(card.name)[
                1] in creature.description.split():
                self.buff_card_from_hand(creature, card)
        for creature in self.deck:
            if list_of_creature_that_affect_all.get(card.name)[1] == "":
                if creature.card_type == list_of_creature_that_affect_all.get(card.name)[0]:
                    self.buff_card_from_hand(creature, card)
            elif creature.card_type == list_of_creature_that_affect_all.get(
                    card.name)[0] and list_of_creature_that_affect_all.get(
                card.name)[1] in creature.description.split():
                self.buff_card_from_hand(creature, card)

    def buff_all_in_battle(self, card):
        for creature in self.battle_field:
            if creature.card_type == "Creature":
                self.buff_card_from_hand(creature, card)

    def card_in_hand_effect(self):
        for creature in self.hand:
            if creature.name in list_of_creature_that_are_affected_in_hand:
                if list_of_creature_that_are_affected_in_hand.get(creature.name)[0] == "reduce":
                    self.reduce_mana_cost_of_card_condition(creature,
                                                            list_of_creature_that_are_affected_in_hand.get(
                                                                creature.name)[1])

    def reduce_mana_cost_of_card_condition(self, creature, condition):
        self.hand[self.hand.index(creature)].mana_cost = self.hand[
            self.hand.index(creature)].original_mana_cost
        if condition == "allies_on_battle_field":
            self.hand[self.hand.index(creature)].mana_cost -= len(self.battle_field) * \
                                                              list_of_creature_that_are_affected_in_hand.get(
                                                                  creature.name)[2]
        elif condition == "all_on_battle_field":
            if ((len(self.battle_field) + len(
                    self.enemy_player.battle_field)) * list_of_creature_that_are_affected_in_hand.get(creature.name)[
                2] > creature.mana_cost):
                creature.mana_cost = 0
            else:
                self.hand[self.hand.index(creature)].mana_cost -= (len(self.battle_field) + len(
                    self.enemy_player.battle_field)) * list_of_creature_that_are_affected_in_hand.get(creature.name)[2]
        else:
            self.hand[self.hand.index(creature)].mana_cost -= len(self.hand) * \
                                                              list_of_creature_that_are_affected_in_hand.get(
                                                                  creature.name)[2] - 1

    @staticmethod
    def card_to_draw_type(card, i):
        if "Desperate" in card.description.split():
            type_of_card = list_of_creature_that_draw_specific_cards_when_die.get(card.name)[0][i]
            type_of_description = list_of_creature_that_draw_specific_cards_when_die.get(card.name)[1][i]
            category = list_of_creature_that_draw_specific_cards_when_die.get(card.name)[2][i]
        else:
            type_of_card = list_of_creature_that_draw_specific_cards.get(card.name)[0][i]
            type_of_description = list_of_creature_that_draw_specific_cards.get(card.name)[1][i]
            category = list_of_creature_that_draw_specific_cards.get(card.name)[2][i]
        return type_of_card, type_of_description, category

    def card_discard(self, nr_of_cards, removing_card):
        for i in range(nr_of_cards):
            card_to_remove = random.randrange(len(self.hand))
            nr_try = 0
            while self.hand.index(removing_card) == card_to_remove and nr_try < len(self.hand):
                card_to_remove = random.randrange(len(self.hand))
                nr_try += 1
            if self.hand[card_to_remove].name in list_of_spells_that_have_effect_when_discarded:
                if self.hand[card_to_remove].card_type == "Spell":
                    self.incoming_spell = self.hand[card_to_remove]
            elif self.hand[card_to_remove].name in list_of_creature_that_have_effect_when_discarded:
                self.battle_field.append(self.hand[card_to_remove])
            if nr_try == len(self.hand) and self.hand.index(removing_card) == card_to_remove:
                pass
            else:
                self.hand.pop(card_to_remove)

    def buff_card_from_battle(self, card):
        condition = list_of_creature_that_are_affected_by_battle_field.get(card.name)
        if condition[0] == "buff":
            if "on field" in condition[1]:
                for creature in self.battle_field:
                    if condition[1].split()[0] == creature.category:
                        self.buff_card_from_hand(card, card)

    def check_for_creature_with_effect_on(self, action, playing_creature):
        for creature in self.battle_field:
            try:
                if creature.name in list_of_creature_that_have_other_stat_while_damaged:
                    self.action_from_condition(creature, "damaged")
                effected_cards = list_of_creature_that_are_effected_by_action.get(creature.name)
                if effected_cards[1] == action and effected_cards[0] == "self_buff":
                    self.buff_card_from_hand(creature, creature)
                elif action in effected_cards[1] and action == "summ":
                    if playing_creature.check_specific_attr(effected_cards[1].split()[1], self,
                                                            self.enemy_player) is True and \
                            effected_cards[0] == "self_buff":
                        self.buff_card_from_hand(creature, creature)
                elif action == effected_cards[1] and action == "cast spell":
                    for i in range(list_of_creature_that_draw_card_on_action.get(creature.name)):
                        self.draw_card()
                elif action == effected_cards[1] and action == "damage_taken":
                    if list_of_creature_that_add_armor_on_action.get(creature.name) is not None:
                        self.armor += list_of_creature_that_add_armor_on_action.get(creature.name)
            except Exception as e:
                print(e)

    def put_item_on(self, enemy_player, card):
        self.active_defence = list_of_creature_that_add_defence.get(card.name)[0]
        self.number_of_troops = self.active_defence.number_of_troops
        self.nr_of_assaults = self.active_defence.nr_of_assaults

    def do_damage(self, target):
        if self.guard_checking(self.enemy_player, target) == 1:
            if target == self.enemy_player and self.active_defence is not None and self.number_of_assaults >= 1:
                self.enemy_player.hp -= self.number_of_troops
                self.defences_weakened(1)
                self.number_of_assaults -= 1

            if target is not None and self.active_defence is not None and self.number_of_assaults >= 1:
                if target.armored is True:
                    target.armored = False
                else:
                    target.hp -= self.number_of_troops
                if self.immunity is False and self.armor == 0:
                    self.hp -= target.attack
                elif self.armor >= target.attack:
                    self.armor -= target.attack
                else:
                    self.hp = self.hp + self.armor - target.attack
                    self.armor = 0
                self.defences_weakened(1)
                self.number_of_assaults -= 1
            if self.nr_of_assaults == 0:
                self.number_of_troops = 0
                self.active_defence = None
        else:
            self.problem = "There are guards on the field"

    def guard_checking(self, player, current_card):
        try:
            if "Guard" in current_card.description.split():
                return 1
            else:
                for card in player.battle_field:
                    if "Guard" in card.description.split():
                        return 0
        except Exception as e:
            if current_card is None or current_card == self.enemy_player:
                for card in player.battle_field:
                    if "Guard" in card.description.split():
                        return 0
        return 1

    def defences_weakened(self, nr_of_lost):
        self.nr_of_assaults -= nr_of_lost
        self.active_defence.nr_of_assaults -= nr_of_lost

    def add_random_card_to_hand(self, card):
        if list_of_cards_that_add_cards_to_your_hand.get(card.name) is not None:
            picking_card = list_of_cards_that_add_cards_to_your_hand.get(card.name)
        else:
            picking_card = list_of_creature_that_add_cards_to_your_hand_when_die.get(card.name)
        for i in range(picking_card[0]):
            if picking_card[1] != "":
                creature = random.choice(list_of_creatures_to_pick.get(picking_card[1]))
                if len(self.hand) < 10:
                    self.hand.append(creature[0])
                    self.hand[-1].id = generate_random_int()
                    self.hand[-1].card_id = str(self.hand[-1].id)
                    if len(self.hand[-1].name.split(" ")) >= 2:
                        self.hand[-1].name_for_html = "_".join(self.hand[-1].name.split()) + self.hand[-1].card_id
                    else:
                        self.hand[-1].name_for_html = self.hand[-1].name + self.hand[-1].card_id
            elif len(self.hand) < 10:
                creature = list_of_creature_that_add_specific_card_to_your_hand.get(card.name)[0]
                self.hand.append(creature)
                del list_of_creature_that_add_specific_card_to_your_hand.get(card.name)[0]

    def check_spell(self, card):
        incoming_card = list_of_spells_that_buff_conditional.get(card.name)
        if incoming_card is not None:
            if "hand" in incoming_card[0].split(":"):
                for creature in self.hand:
                    if creature.card_type == incoming_card[0].split(":")[1] or creature.category == \
                            incoming_card[0].split(":")[1]:
                        list_of_buff_spells[card.name] = incoming_card[1]

    def action_from_condition(self, card, condition):
        if card.name in list_of_creature_that_have_other_stat_while_damaged and condition == "damaged":
            if card.hp < card.max_hp and card.attack < card.original_attack + \
                    list_of_creature_that_buff.get(card.name)[1]:
                self.buff_card_from_hand(card, card)
        if card.name in list_of_creature_that_have_other_stat_while_damaged:
            if card.hp >= card.original_hp and card.attack > card.original_attack + \
                    list_of_creature_that_buff.get(card.name)[1]:
                buff = list_of_creature_that_buff.get(card.name)
                card.hp -= buff[0]
                card.max_hp -= buff[0]
                card.attack -= buff[1]
                if buff[2] not in card.description:
                    card.description.remove(buff[2])
                card.check_creature(buff[2])
