import copy
from production_server.clases.game_logics import *
from production_server.decks.lists_of_cards import *

from production_server.decks.decks_to_play import *

from production_server.decks.holy_roman_empire import *

from production_server.clases.quest import *


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
        self.power = None
        self.number_of_troops = 0
        self.nr_of_assaults = 0
        self.debt = 0
        self.last_debt = 0
        self.number_of_assaults = 1
        self.choice_options = []
        self.hand_copy = []
        self.has_to_pick = False
        self.tactics = []
        self.dict_of_actions = {"Spells_casted": [], "Damage_taken": 0, "Damage_done": 0,
                                "Minions": {}, "Debt_in_game": 0,
                                "Minions_that_died": {"my_minions": [], "enemy_minions": [],
                                                      "my_minions_that_died_this_turn": [],
                                                      "enemy_minions_that_died_this_turn": []}}
        self.quest = None
        self.permanent_effect = []

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
            if self.has_to_pick is True and card_picked.get(card.name_for_html) is not None:
                self.add_card_to_hand(card)
                break
            if card_picked.get(card.name_for_html) is not None and card.mana_cost <= self.mana:
                if any(card.name == tactic.name for tactic in self.tactics):
                    break
                self.check_for_creature_with_effect_on("summ", card)
                if card.name in list_of_cards_that_change_hero_power:
                    self.empire = list_of_cards_that_change_hero_power[card.name][self.empire]
                if card.name in list_of_permanent_effect:
                    self.permanent_effect.append(card)
                if card.name in list_of_creature_that_affect_all_enemy_minions:
                    self.affect_enemy_all(card)
                if card.name in list_of_cards_that_add_cards_to_your_deck and len(self.battle_field) < 7:
                    self.add_card_to_deck(card)
                if card.name in list_of_creature_that_debuff_enemies and len(self.battle_field) < 7:
                    self.debuff_all_enemies(card)
                if card.name in list_of_creature_that_debuff_all and len(self.battle_field) < 7:
                    self.debuff_all(card)
                if card.name in list_of_creature_that_are_affected_by_hand and len(self.battle_field) < 7:
                    self.hand_check(card)
                if card.name in list_of_cards_that_add_cards_to_your_hand and len(self.battle_field) < 7:
                    self.add_random_card_to_hand(card)
                if card.name in list_of_cards_that_discover:
                    self.discover_a_card(card)
                if card.name in list_of_creature_that_damage_a_random_creature:
                    self.pick_random_enemy(card)
                if card.name in list_of_card_that_pay_debt:
                    if self.last_debt > self.mana:
                        self.mana = self.empty_mana
                    else:
                        self.mana += self.last_debt
                    self.last_debt = 0
                if card.name in list_of_cards_that_check_your_kingdom:
                    self.check_kingdom(card)
                if card.name in list_of_card_that_add_debt:
                    self.dict_of_actions["Debt_in_game"] += list_of_card_that_add_debt.get(card.name)
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
                if card.name in list_of_creature_description and len(self.battle_field) < 7:
                    self.mana_pay(card)
                    self.battle_field.append(card)
                    self.summoned_minions(card)
                    self.incoming_action = 2
                    self.active_minion = card
                    return 2
                if card.name in list_of_creature_that_add_defence:
                    self.put_item_on(self.enemy_player, card)
                elif card.name in list_of_creature_that_draw_cards and len(self.battle_field) < 7:
                    for nr_cards in range(list_of_creature_that_draw_cards.get(card.name)):
                        got_card = 0
                        if card.name in list_of_creature_that_draw_specific_cards:
                            try:
                                random_card = self.get_random_card(card, nr_cards)
                                if random_card is not None:
                                    self.hand.append(random_card)
                                    self.deck.remove(random_card)
                                    got_card = 1
                            except Exception as e:
                                print(e)
                        else:
                            self.draw_card()
                            got_card = 1
                        if card.name in list_of_creature_that_plays_a_card_from_your_deck:
                            self.play_drawn_card(got_card,
                                                 list_of_creature_that_draw_specific_cards.get(card.name))
                elif card.name in list_of_creature_that_add_mana and len(self.battle_field) < 7:
                    self.mana_increase(list_of_creature_that_add_mana.get(card.name))
                    if self.empty_mana + list_of_creature_that_add_mana.get(card.name) > 10:
                        self.empty_mana = 10
                    else:
                        self.empty_mana += list_of_creature_that_add_mana.get(card.name)
                elif card.name in list_of_creature_that_do_damage_to_all_other_creatures and len(self.battle_field) < 7:
                    self.do_damage_to_all_other_minions(card)
                elif card.name in list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms and len(
                        self.battle_field) < 7:
                    self.do_damage_to_all_other_characters(card)
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
                    self.summoned_minions(card)
                    self.mana_pay(card)
                    if len(self.battle_field) < 7:
                        for i in range(list_of_creature_that_summon.get(card.name)[0]):
                            if len(self.battle_field) < 7:
                                if card.name in list_of_creature_that_summ_random:
                                    self.battle_field.append(
                                        random.choice(list_of_creature_that_summon.get(card.name)[1]))
                                    self.battle_field[-1].card_id = str(generate_random_int())
                                else:
                                    self.battle_field.append(list_of_creature_that_summon.get(card.name)[1][i])
                                self.summoned_minions(list_of_creature_that_summon.get(card.name)[1][i])
                                list_of_creature_that_summon.get(card.name)[1].remove(
                                    list_of_creature_that_summon.get(card.name)[1][i])
                                self.check_for_creature_with_effect_on("summ", self.battle_field[-1])
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
                if card.name in list_of_creature_that_reduce_mana_cost:
                    self.reduce_mana_cost_of_card(card)
                if card.name in list_of_creature_that_are_affected_by_battle_field:
                    self.buff_card_from_battle(card)
                if self.quest is not None:
                    self.quest.check_quest_progression(self, card, "summ")
                self.battle_field.append(card)
                self.summoned_minions(card)
                self.mana_pay(card)
                return 1
        return 0

    def check_battlefield(self):
        for card in self.battle_field[:]:
            if card.hp <= 0:
                self.battle_field.remove(card)

    def mana_pay(self, card):
        if self.has_to_pick is True:
            for card_in_hand_copy in self.hand_copy:
                if card_in_hand_copy.name == card.name:
                    self.hand_copy.remove(card_in_hand_copy)
                    break
        else:
            self.hand.remove(card)
        self.mana_increase(-card.mana_cost)

    def draw_card(self):
        try:
            self.card_in_hand_effect()
            pick_card = random.choice(self.deck)
            while self.check_picked_card(pick_card) is None and len(self.deck) > 0:
                self.deck.remove(pick_card)
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
            quest_in_deck = 0
            for card in self.deck:
                if card.name in list_of_quests:
                    quest_in_deck = 1
                    self.hand.append(card)
                    self.deck.remove(card)
                    break
            if quest_in_deck == 1:
                for i in range(0, 4):
                    self.draw_card()
            else:
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
                    player.dict_of_actions["Minions_that_died"]["my_minions"].append(card)
                    player.dict_of_actions["Minions_that_died"]["my_minions_that_died_this_turn"].append(card)
                    if card.name in list_of_creature_that_do_somthing_when_die:
                        Player.action_when_die(player, card)
                    player.check_for_creature_with_effect_on("friendly_minion_dies", card)
            for card in enemy_player.battle_field[:]:
                if card.hp <= 0 and card.card_type == "Creature":
                    enemy_player.battle_field.remove(card)
                    enemy_player.dict_of_actions["Minions_that_died"]["enemy_minions"].append(card)
                    enemy_player.dict_of_actions["Minions_that_died"]["enemy_minions_that_died_this_turn"].append(card)
                    if card.name in list_of_creature_that_do_somthing_when_die:
                        Player.action_when_die(enemy_player, card)
                    enemy_player.check_for_creature_with_effect_on("friendly_minion_dies", card)
                    enemy_player.check_for_tactics("friendly_minion_dies", None, None)
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
            elif list_of_creature_that_do_somthing_when_die.get(card.name) == "resumm":
                if card.name == "Julius Caesar":
                    if player.armor >= 4:
                        player.battle_field.append(Creature(7, "Julius Caesar", 6, 7,
                                                            "Rush Gain 4 defences desperate Lose 4 defences to resummon this",
                                                            "mercenary",
                                                            7))
                        player.armor -= 4
            elif list_of_creature_that_do_somthing_when_die.get(card.name) == "put_wepon":
                player.active_defence = list_of_creature_that_add_defence_when_die.get(card.name)[0]
                player.number_of_troops = player.active_defence.number_of_troops
                player.nr_of_assaults = player.active_defence.nr_of_assaults
            elif list_of_creature_that_do_somthing_when_die.get(card.name) == "add_to_deck":
                for i in range(0, list_of_creature_that_add_cards_to_your_deck_when_die[card.name][0]):
                    player.deck.append(list_of_creature_that_add_cards_to_your_deck_when_die[card.name][1][0])
                    list_of_creature_that_add_cards_to_your_deck_when_die[card.name][1].pop(0)

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
            if card.name in list_of_creature_that_affect_in_hand_specific:
                for creature in self.hand:
                    if creature != card and creature.card_type == \
                            list_of_creature_that_affect_in_hand_specific[card.name][0]:
                        if list_of_creature_that_affect_in_hand_specific[card.name][1] in creature.description and \
                                list_of_creature_that_affect_in_hand_specific[card.name][2] == creature.category:
                            self.buff_card_from_hand(creature, card)
            else:
                for creature in self.hand:
                    if creature != card and creature.card_type == "Creature":
                        self.buff_card_from_hand(creature, card)
        elif "hand_check" in incoming_card[0].split(":"):
            if incoming_card[0].split(":")[1] == "number":
                if incoming_card[1].split(":")[0] == "change":
                    if incoming_card[1].split(":")[1] == "all":
                        if incoming_card[1].split(":")[2] == "dmg":
                            list_of_creature_that_do_damage_to_all_other_creatures[card.name] = len(self.hand) - 1
            ok = 0
            for card_in_hand in self.hand:
                if card_in_hand != card:
                    if card_in_hand.card_type == incoming_card[0].split(":")[1] or card_in_hand.category == \
                            incoming_card[0].split(":")[1]:
                        if incoming_card[1] == "buff":
                            self.buff_card_from_hand(card, card)
                            ok = 1
                            break
                        if incoming_card[1].split(":")[0] == "change":
                            if incoming_card[1].split(":")[1] == "dmg":
                                if list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms.get(
                                        card.name) is not None:
                                    list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms[card.name] = \
                                        incoming_card[2]
                                    ok = 1
                                    break
                                list_of_creature_that_deal_dmg_to_enemies[card.name] = incoming_card[2]
                                ok = 1
                                if list_of_creature_that_deal_dmg_to_players.get(card.name) is not None:
                                    list_of_creature_that_deal_dmg_to_players[card.name] = incoming_card[2]
                                    ok = 1
                                    break
                            if incoming_card[1].split(":")[1] == "armor":
                                if incoming_card[1].split(":")[2] == "gain":
                                    list_of_cards_that_give_armor[card.name] = incoming_card[2]
                                    ok = 1
                                    break
                            if incoming_card[1].split(":")[1] == "draw":
                                list_of_creature_that_draw_cards[card.name] = incoming_card[2]
                                ok = 1
                                break
                            if incoming_card[1].split(":")[1] == "discover":
                                list_of_cards_that_discover[card.name] = incoming_card[2]
                                ok = 1
                                break
            if ok == 0:
                if card.name in list_of_creature_that_draw_cards:
                    list_of_creature_that_draw_cards[card.name] = 0
                if card.name in list_of_cards_that_discover:
                    list_of_cards_that_discover[card.name] = ""
                if card.name in list_of_cards_that_give_armor:
                    list_of_cards_that_give_armor[card.name] = 0
                if card.name in list_of_creature_that_deal_dmg_to_players:
                    list_of_creature_that_deal_dmg_to_players[card.name] = 0
                if card.name in list_of_creature_that_deal_dmg_to_enemies:
                    list_of_creature_that_deal_dmg_to_enemies[card.name] = 0

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
            if self.hand[self.hand.index(creature)].mana_cost >= len(self.battle_field) * \
                    list_of_creature_that_are_affected_in_hand.get(
                        creature.name)[2]:
                self.hand[self.hand.index(creature)].mana_cost -= len(self.battle_field) * \
                                                                  list_of_creature_that_are_affected_in_hand.get(
                                                                      creature.name)[2]
            else:
                self.hand[self.hand.index(creature)].mana_cost = 0
        elif condition == "all_on_battle_field":
            if ((len(self.battle_field) + len(
                    self.enemy_player.battle_field)) * list_of_creature_that_are_affected_in_hand.get(creature.name)[
                2] > creature.mana_cost):
                creature.mana_cost = 0
            else:
                self.hand[self.hand.index(creature)].mana_cost -= (len(self.battle_field) + len(
                    self.enemy_player.battle_field)) * list_of_creature_that_are_affected_in_hand.get(creature.name)[2]
        elif condition == "armor":
            if self.hand[self.hand.index(creature)].mana_cost >= self.armor:
                self.hand[self.hand.index(creature)].mana_cost -= self.armor
            else:
                self.hand[self.hand.index(creature)].mana_cost = 0
        elif condition == "spells_casted":
            if self.hand[self.hand.index(creature)].mana_cost >= len(self.dict_of_actions["Spells_casted"]):
                self.hand[self.hand.index(creature)].mana_cost -= len(self.dict_of_actions["Spells_casted"])
            else:
                self.hand[self.hand.index(creature)].mana_cost = 0
        elif condition == "amount_of_mana_on_spells":
            amount = 0
            for spell in self.dict_of_actions["Spells_casted"]:
                amount += spell.mana_cost
            if self.hand[self.hand.index(creature)].mana_cost >= amount:
                self.hand[self.hand.index(creature)].mana_cost -= amount
            else:
                self.hand[self.hand.index(creature)].mana_cost = 0
        elif "total_summoned" in condition:
            try:
                if self.hand[self.hand.index(creature)].mana_cost >= len(
                        self.dict_of_actions['Minions'][condition.split(":")[1]]):
                    self.hand[self.hand.index(creature)].mana_cost -= len(
                        self.dict_of_actions['Minions'][condition.split(":")[1]])
                else:
                    self.hand[self.hand.index(creature)].mana_cost = 0
            except Exception as e:
                print(e)
        elif condition == "amount_of_debt_in_game":
            if self.hand[self.hand.index(creature)].mana_cost >= self.dict_of_actions["Debt_in_game"]:
                self.hand[self.hand.index(creature)].mana_cost -= self.dict_of_actions["Debt_in_game"]
            else:
                self.hand[self.hand.index(creature)].mana_cost = 0
        elif "any_dead_minion" in condition.split(":"):
            if len(self.dict_of_actions["Minions_that_died"]["my_minions"]) > 0 or len(
                    self.enemy_player.dict_of_actions["Minions_that_died"]["enemy_minions"]) > 0:
                if condition.split(":")[1] == "this_turn":
                    if len(self.enemy_player.dict_of_actions["Minions_that_died"][
                               "enemy_minions_that_died_this_turn"]) > 0 or len(
                        self.dict_of_actions["Minions_that_died"]["my_minions_that_died_this_turn"]) > 0:
                        if "cost_set" == list_of_creature_that_are_affected_in_hand[creature.name][2]:
                            creature.mana_cost = list_of_creature_that_are_affected_in_hand[creature.name][3]
        elif "tactics" in condition.split(":"):
            if "number" in condition.split(":"):
                if self.hand[self.hand.index(creature)].mana_cost >= list_of_creature_that_are_affected_in_hand.get(
                        creature.name)[2] * len(self.tactics):
                    self.hand[self.hand.index(creature)].mana_cost -= list_of_creature_that_are_affected_in_hand.get(
                        creature.name)[2] * len(self.tactics)
                else:
                    self.hand[self.hand.index(creature)].mana_cost = 0
        else:
            if self.hand[self.hand.index(creature)].mana_cost >= len(self.hand) * \
                    list_of_creature_that_are_affected_in_hand.get(
                        creature.name)[2] - 1:
                self.hand[self.hand.index(creature)].mana_cost -= len(self.hand) * \
                                                                  list_of_creature_that_are_affected_in_hand.get(
                                                                      creature.name)[2] - 1
            else:
                self.hand[self.hand.index(creature)].mana_cost = 0

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
        try:
            for creature in self.battle_field:
                try:
                    if creature.name in list_of_creature_that_have_other_stat_while_damaged:
                        self.action_from_condition(creature, "damaged")
                    effected_cards = list_of_creature_that_are_effected_by_action.get(creature.name)
                    if action in effected_cards[1].split(":") and action == "friendly_minion_dies":
                        if effected_cards[1].split(":")[1] == playing_creature.category:
                            self.buff_card_from_hand(creature, creature)
                        elif effected_cards[1].split(":")[1] == "all":
                            self.buff_card_from_hand(creature, creature)
                    elif effected_cards[1] == action and effected_cards[0] == "self_buff":
                        self.buff_card_from_hand(creature, creature)
                    elif action in effected_cards[1] and action == "summ":
                        if playing_creature.check_specific_attr(effected_cards[1].split()[1], self,
                                                                self.enemy_player) is True and \
                                effected_cards[0] == "self_buff":
                            self.buff_card_from_hand(creature, creature)
                        elif playing_creature.check_specific_attr(effected_cards[1].split()[1], self,
                                                                  self.enemy_player) is True and list_of_cards_that_add_cards_to_your_hand_by_action.get(
                            creature.name):
                            self.add_random_card_to_hand(creature)
                        elif playing_creature.check_specific_attr(effected_cards[1], self,
                                                                  self.enemy_player) is True and \
                                effected_cards[0] == "buff new summ":
                            self.buff_card_from_hand(playing_creature, creature)
                        if "all" in effected_cards[0].split(":"):
                            if "damage" in effected_cards[0].split(":"):
                                if "all" in effected_cards[0].split(":"):
                                    if "enemies" in effected_cards[0].split(":"):
                                        list_of_targets = []
                                        list_of_targets.extend(self.enemy_player.battle_field)
                                        list_of_targets.append(self.enemy_player.name)
                                        random_enemy = random.choice(list_of_targets)
                                        if isinstance(random_enemy, str):
                                            self.enemy_player.hp -= int(effected_cards[0].split(":")[4])
                                            self.dict_of_actions["Damage_done"] += int(effected_cards[0].split(":")[3])
                                        elif random_enemy.armored is True:
                                            random_enemy.armored = False
                                        else:
                                            random_enemy.hp -= int(effected_cards[0].split(":")[4])
                                        list_of_targets.clear()
                    elif action == effected_cards[1] and action == "cast spell":
                        if creature.name == "Pyrrho of Elis" and len(self.hand) < 10:
                            self.hand.append(Spell(4, "Flaming arrow", "Deal 6 damage", generate_random_int()))
                        if creature.name == "Tolui":
                            if self.enemy_player.immunity is False:
                                if self.enemy_player.armor >= playing_creature.mana_cost:
                                    self.enemy_player.armor -= playing_creature.mana_cost
                                else:
                                    self.enemy_player.hp = self.enemy_player.hp + self.enemy_player.armor - playing_creature.mana_cost
                                    self.armor = 0
                            else:
                                self.enemy_player.hp -= playing_creature.mana_cost

                        for i in range(list_of_creature_that_draw_card_on_action.get(creature.name)):
                            self.draw_card()
                    elif action == effected_cards[1] and action == "damage_taken":
                        if list_of_creature_that_add_armor_on_action.get(creature.name) is not None:
                            if playing_creature == creature:
                                if creature.name in list_of_creature_that_are_effected_by_action_once:
                                    self.do_action_once_per_trigger(creature, "add_armor")
                                else:
                                    self.armor += list_of_creature_that_add_armor_on_action.get(creature.name)
                            elif playing_creature is not None:
                                self.armor += list_of_creature_that_add_armor_on_action.get(creature.name)
                    elif action == effected_cards[1] and action == "kill_minion":
                        if list_of_creature_that_add_armor_on_action.get(creature.name) is not None:
                            self.armor += list_of_creature_that_add_armor_on_action.get(creature.name)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

    def do_action_once_per_trigger(self, card, action_to_do):
        if action_to_do == "add_armor" and list_of_creature_that_are_effected_by_action_once[card.name] == 0:
            self.armor += list_of_creature_that_add_armor_on_action.get(card.name)
            list_of_creature_that_are_effected_by_action_once[card.name] += 1

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
                self.dict_of_actions["Damage_done"] += self.number_of_troops

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
        elif list_of_creature_that_add_cards_to_your_hand_when_die.get(card.name) is not None:
            picking_card = list_of_creature_that_add_cards_to_your_hand_when_die.get(card.name)
        else:
            picking_card = list_of_cards_that_add_cards_to_your_hand_by_action.get(card.name)
        for i in range(picking_card[0]):
            if picking_card[1] != "":
                creature = copy.deepcopy(random.choice(list_of_creatures_to_pick.get(picking_card[1])))
                creature[0].id = generate_random_int()
                if len(self.hand) < 10:
                    self.hand.append(creature[0])
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
            ok = 0
            if "hand" in incoming_card[0].split(":"):
                if "knight" in incoming_card[0].split(":"):
                    for creature in self.hand:
                        if creature.card_type == incoming_card[0].split(":")[1] or creature.category == \
                                incoming_card[0].split(":")[1]:
                            list_of_buff_spells[card.name] = incoming_card[1]
                elif "empty" in incoming_card[0].split(":"):
                    if len(self.hand) == 1:
                        if "draw" == incoming_card[1]:
                            for i in range(0, incoming_card[2]):
                                self.draw_card()
            if "battle" in incoming_card[0].split(":"):
                for creature in self.battle_field:
                    if creature.category == incoming_card[0].split(":")[1]:
                        if "change" in incoming_card[1].split(":"):
                            if "damage" == incoming_card[1].split(":")[1]:
                                list_of_dmg_spells[card.name] = incoming_card[2]
                                ok = 1
                                break
                if ok == 0:
                    list_of_dmg_spells[card.name] = int(incoming_card[1].split(":")[2])

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

    def check_kingdom(self, card):
        checking_card = list_of_cards_that_check_your_kingdom.get(card.name)
        if checking_card[0] == "armor":
            if checking_card[1].split(":")[0] == "spend":
                if checking_card[1].split(":")[1] == "all":
                    if checking_card[2] == "buff":
                        if card.card_type == "Spell":
                            list_of_dmg_spells[card.name] = self.armor
                            self.armor = 0
            else:
                if checking_card[1].split(":")[1] == "all":
                    if checking_card[2] == "change:dmg":
                        list_of_creature_that_deal_dmg_to_enemies[card.name] = self.armor
                    elif checking_card[2] == "buff":
                        list_of_dmg_spells[card.name] = self.armor
                elif int(checking_card[1].split(":")[1]) <= self.armor:
                    self.buff_card_from_hand(card, card)
        if checking_card[0] == "health":
            if int(checking_card[1].split(":")[1]) >= self.hp and card.card_type == "Creature":
                self.buff_card_from_hand(card, card)
            elif int(checking_card[1].split(":")[1]) >= self.hp and card.card_type == "Spell":
                list_of_dmg_spells[card.name] = checking_card[2]
        if checking_card[0] == "defence":
            if int(checking_card[1].split(":")[1]) <= self.nr_of_assaults and card.card_type == "Creature":
                self.buff_card_from_hand(card, card)
        if checking_card[0] == "deck":
            if checking_card[1].split(":")[1] == "holy":
                ok = 1
                for creature in self.deck:
                    if not any(creature.name == obj.name for obj in cards_holy_show):
                        ok = 0
                if ok == 1:
                    if checking_card[2] == "buff":
                        self.buff_card_from_hand(card, card)
            if checking_card[1].split(":")[1] == "Resources":
                nr_resources = 0
                for creature in self.deck[:]:
                    if creature.name == "Resources":
                        nr_resources += 1
                        self.deck.remove(creature)
                        if checking_card[2] == "buff":
                            self.buff_card_from_hand(card, card)
                            nr_resources -= 1
                        elif isinstance(checking_card[2], int) is True:
                            nr_resources -= 1
                            list_of_creature_that_deal_dmg_to_enemies[card.name] = checking_card[2]
                if len(self.battle_field) < 7:
                    for i in range(nr_resources):
                        if len(self.battle_field) < 7:
                            self.battle_field.append(list_of_creature_that_summon.get(card.name)[1][i])
                            self.summoned_minions(list_of_creature_that_summon.get(card.name)[1][i])
                            list_of_creature_that_summon.get(card.name)[1].remove(
                                list_of_creature_that_summon.get(card.name)[1][i])
                            self.check_for_creature_with_effect_on("summ", self.battle_field[-1])
        if checking_card[0] == "tactic":
            if int(checking_card[1].split(":")[1]) <= len(self.tactics) and card.card_type == "Creature":
                if "draw" in checking_card[2].split(":"):
                    for i in range(int(checking_card[2].split(":")[1])):
                        self.draw_card()
                if "summ" in checking_card[2].split(":"):
                    list_of_creature_that_summon[card.name][0] = int(checking_card[2].split(":")[1])
                if "change" in checking_card[2].split(":"):
                    if "dmg" in checking_card[2].split(":"):
                        list_of_creature_that_deal_dmg_to_enemies[card.name] = int(checking_card[2].split(":")[2])
            elif list_of_creature_that_summon.get(card.name) is not None:
                list_of_creature_that_summon[card.name][0] = 0
        if checking_card[0] == "debt":
            if self.debt > 0:
                if "draw" in checking_card[2].split(":"):
                    list_of_creature_that_draw_cards[card.name] = self.debt

    def do_damage_to_all_other_minions(self, card):
        for creature in self.battle_field:
            if creature.armored is True and 0 < list_of_creature_that_do_damage_to_all_other_creatures.get(
                    card.name) < 90:
                creature.armored = False
            else:
                creature.hp -= list_of_creature_that_do_damage_to_all_other_creatures.get(card.name)
                if self.quest is not None:
                    self.quest.check_quest_progression(self, None, "damage")
                self.check_for_creature_with_effect_on("damage_taken", creature)
        for creature in self.enemy_player.battle_field:
            if creature.armored is True and 0 < list_of_creature_that_do_damage_to_all_other_creatures.get(
                    card.name) < 90:
                creature.armored = False
            else:
                creature.hp -= list_of_creature_that_do_damage_to_all_other_creatures.get(card.name)
                self.enemy_player.check_for_creature_with_effect_on("damage_taken", creature)

    def do_damage_to_all_other_characters(self, card):
        if self.immunity is False:
            self.hp -= list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms.get(
                card.name)
        if self.enemy_player.immunity is False:
            self.enemy_player.hp -= list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms.get(
                card.name)
        for creature in self.battle_field:
            if creature.armored is True and 0 < list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms.get(
                    card.name) < 90:
                creature.armored = False
            else:
                creature.hp -= list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms.get(card.name)
                if self.quest is not None:
                    self.quest.check_quest_progression(self, None, "damage")
                self.check_for_creature_with_effect_on("damage_taken", creature)
        for creature in self.enemy_player.battle_field:
            if creature.armored is True and 0 < list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms.get(
                    card.name) < 90:
                creature.armored = False
            else:
                creature.hp -= list_of_creature_that_do_damage_to_all_other_creatures_and_kingdoms.get(card.name)
                self.enemy_player.check_for_creature_with_effect_on("damage_taken", creature)
        Player.check_player(self)
        Player.check_player(self.enemy_player)

    def add_card_to_hand(self, creature):
        if len(self.hand) < 10:
            self.hand = self.hand_copy
            self.hand.append(creature)
            self.hand[-1].id = generate_random_int()
            self.hand[-1].card_id = str(self.hand[-1].id)
            if len(self.hand[-1].name.split(" ")) >= 2:
                self.hand[-1].name_for_html = "_".join(self.hand[-1].name.split()) + self.hand[-1].card_id
            else:
                self.hand[-1].name_for_html = self.hand[-1].name + self.hand[-1].card_id
        self.has_to_pick = False
        self.hand_copy = []
        self.choice_options = []
        if self.power == "Mercenary Empire" and len(self.battle_field) < 7:
            self.battle_field.append(self.hand[-1])
            self.hand.pop()
            self.power = None
            self.check_for_creature_with_effect_on("summ", self.battle_field[-1])

    def discover_a_card(self, card):
        if self.power == "Mercenary Empire":
            self.choice_options.append(Creature(1, "Shield soldier", 2, 0, "Guard", "soldier", generate_random_int()))
            self.choice_options.append(Creature(1, "Man at arms", 1, 1, "", "soldier", generate_random_int()))
            self.hand_copy = copy.deepcopy(self.hand)
            self.hand = self.choice_options
            self.has_to_pick = True
        elif list_of_cards_that_discover[card.name] != "":
            for i in range(0, 3):
                self.choice_options.append(
                    random.choice(list_of_creatures_to_pick.get(list_of_cards_that_discover[card.name]))[0])
                if card.name in list_of_spells_that_reduce_mana:
                    self.choice_options[-1].mana_cost_reduction(list_of_spells_that_reduce_mana[card.name][1])
            if card.name == "Vast Empire" and self.empty_mana == 10:
                for creature in self.choice_options:
                    if len(self.hand) < 10:
                        self.hand.append(creature)
                self.choice_options = []
            else:
                self.hand_copy = copy.deepcopy(self.hand)
                self.hand = self.choice_options
                self.has_to_pick = True

    def check_for_tactics(self, action, creature1, creature2):
        trap_triggered = False
        tactic_to_remove = None
        for tactic in self.tactics[:]:
            if action in list_of_tactics.get(tactic.name).split("=>")[0]:
                trap_triggered = True
                tactic_to_remove = tactic
                if '>' in list_of_tactics.get(tactic.name).split("=>")[0]:
                    if creature1.attack >= [int(i) for i in list_of_tactics.get(tactic.name).split("=>")[0] if
                                            i.isdigit()][0]:
                        if list_of_tactics.get(tactic.name).split("=>")[1].split(":")[0] == "deal_dmg":
                            creature1.hp -= int(list_of_tactics.get(tactic.name).split("=>")[1].split(":")[1])
                elif "debuff" in list_of_tactics.get(tactic.name).split("=>")[1]:
                    creature1.debuff_creature(list_of_spells_that_debuff.get(tactic.name), self, self.enemy_player)
                elif "buff" in list_of_tactics.get(tactic.name).split("=>")[1]:
                    random_creature = None
                    if "random" in list_of_tactics.get(tactic.name).split("=>")[1]:
                        if len(self.battle_field) > 0:
                            random_creature = random.choice(self.battle_field)
                    else:
                        random_creature = creature2
                    buff = list_of_buff_spells.get(tactic.name)
                    random_creature.hp += buff[0]
                    random_creature.max_hp += buff[0]
                    random_creature.attack += buff[1]
                    if buff[2] not in random_creature.description:
                        random_creature.description += "  " + buff[2]
                    random_creature.check_creature(buff[2])
                elif "summ" in list_of_tactics.get(tactic.name).split("=>")[1]:
                    if len(self.battle_field) < 7:
                        for i in range(int(list_of_tactics.get(tactic.name).split("=>")[1].split(":")[1])):
                            self.battle_field.append(list_of_spells_that_summon_specific_cards.get(tactic.name)[1][0])
                            list_of_spells_that_summon_specific_cards.get(tactic.name)[1].pop(0)
                elif "send_to_hand" in list_of_tactics.get(tactic.name).split("=>")[1]:
                    self.send_to_hand(creature1, self.enemy_player, "+2:mana")
                elif "deal_dmg" in list_of_tactics.get(tactic.name).split("=>")[1]:
                    if "enemies" == list_of_tactics.get(tactic.name).split("=>")[1].split(":")[2]:
                        for creature in self.enemy_player.battle_field:
                            if creature.armored is True:
                                creature.armored = False
                            else:
                                creature.hp -= int(list_of_tactics.get(tactic.name).split("=>")[1].split(":")[1])
                    elif "minion" in list_of_tactics.get(tactic.name).split("=>")[1]:
                        if creature1.armored is True:
                            creature1.armored = False
                        else:
                            creature1.hp -= int(list_of_tactics.get(tactic.name).split("=>")[1].split(":")[1])
                        if "rest_to_kingdom" in list_of_tactics.get(tactic.name).split("=>")[1]:
                            if creature1.hp < 0:
                                self.enemy_player.hp += creature1.hp
        if trap_triggered:
            self.logs += "Tactic triggered:" + tactic_to_remove.name + "\n"
            self.tactics.remove(tactic_to_remove)

    def send_to_hand(self, creature, player, negative_effect):
        if len(player.hand) < 10:
            creature.reset()
            if negative_effect is not None:
                if "mana" in negative_effect.split(":"):
                    creature.mana_cost += int(negative_effect.split(":")[0][1])
            player.battle_field.remove(creature)
            player.hand.append(creature)

    def play_drawn_card(self, got_card, what_cards_to_play):
        if got_card == 1:
            if what_cards_to_play[1][0] in self.hand[-1].description.split() and what_cards_to_play[0][0] == self.hand[
                -1].card_type and what_cards_to_play[2][0] == self.hand[-1].category:
                if what_cards_to_play[1][0] == "Tactic":
                    self.tactics.append(self.hand[-1])
                    self.hand.pop(-1)

    def create_quest(self, quest):
        self.quest = Quest(quest.mana_cost, quest.name, quest.description, quest.card_id)
        self.quest.build_criteria()

    def debuff_all(self, card):
        for creature in self.battle_field:
            if creature != card:
                creature.debuff_creature(list_of_creature_that_debuff.get(card.name), self, self.enemy_player)
        for creature in self.enemy_player.battle_field:
            creature.debuff_creature(list_of_creature_that_debuff.get(card.name), self.enemy_player, self)

    def debuff_all_enemies(self, card):
        for creature in self.enemy_player.battle_field:
            creature.debuff_creature(list_of_creature_that_debuff.get(card.name), self.enemy_player, self)

    def add_card_to_deck(self, card):
        for i in range(list_of_cards_that_add_cards_to_your_deck.get(card.name)[0]):
            self.deck.append(list_of_cards_that_add_cards_to_your_deck.get(card.name)[1][0])
            list_of_cards_that_add_cards_to_your_deck.get(card.name)[1].pop(0)

    def check_picked_card(self, card):
        if card.name in list_of_spells_that_auto_cast:
            if "heal_player" in list_of_spells_that_auto_cast.get(card.name):
                self.heal_player(list_of_spells_that_can_heal_player.get(card.name))
                self.logs += "You have drawn:" + card.name + "\n"
                return None
        return card

    def pick_random_enemy(self, card):
        for i in range(list_of_creature_that_damage_a_random_creature[card.name]):
            if len(self.enemy_player.battle_field) > 0:
                card_picked = random.choice(self.enemy_player.battle_field)
                card_picked.hp -= list_of_creature_that_deal_dmg_to_enemies[card.name]

    def affect_enemy_all(self, card):
        for creature in self.enemy_player.battle_field:
            creature.debuff_creature(list_of_creature_that_debuff.get(card.name), self.enemy_player, self)
        for creature in self.enemy_player.deck:
            if creature.card_type == "Creature":
                creature.debuff_creature(list_of_creature_that_debuff.get(card.name), self.enemy_player, self)
        for creature in self.enemy_player.hand:
            if creature.card_type == "Creature":
                creature.debuff_creature(list_of_creature_that_debuff.get(card.name), self.enemy_player, self)

    def reduce_mana_cost_of_card(self, card):
        if "deck" in list_of_creature_that_reduce_mana_cost[card.name][0].split(","):
            for creature in self.deck:
                if creature.card_type == list_of_creature_that_reduce_mana_cost[card.name][1]:
                    if creature.category == list_of_creature_that_reduce_mana_cost[card.name][2]:
                        creature.mana_cost_reduction(list_of_creature_that_reduce_mana_cost[card.name][3])
        if "hand" in list_of_creature_that_reduce_mana_cost[card.name][0].split(","):
            for creature in self.hand:
                if creature.card_type == list_of_creature_that_reduce_mana_cost[card.name][1]:
                    if creature.category == list_of_creature_that_reduce_mana_cost[card.name][2]:
                        creature.mana_cost_reduction(list_of_creature_that_reduce_mana_cost[card.name][3])
        if "last card draw" in list_of_creature_that_reduce_mana_cost[card.name][0].split(","):
            if self.hand[-1].card_type == list_of_creature_that_reduce_mana_cost[card.name][1]:
                if list_of_creature_that_reduce_mana_cost[card.name][2] == "":
                    self.hand[-1].mana_cost_reduction(list_of_creature_that_reduce_mana_cost[card.name][3])
                elif self.hand[-1].category == list_of_creature_that_reduce_mana_cost[card.name][2]:
                    self.hand[-1].mana_cost_reduction(list_of_creature_that_reduce_mana_cost[card.name][3])

    def summoned_minions(self, card):
        self.check_perma_effects(card)
        if card.category in self.dict_of_actions['Minions']:
            self.dict_of_actions['Minions'][card.category].append(card)
        else:
            self.dict_of_actions['Minions'][card.category] = [card]

    def check_perma_effects(self, card):
        for pe in self.permanent_effect:
            if card.name in list_of_permanent_effect[pe.name]:
                self.buff_card_from_hand(card, pe)

    def spell_draw_specific_card(self):
        for index_in_lists in range(len(list_of_spells_that_draw_specific_cards[self.incoming_spell.name][0])):
            for card in self.deck:
                if card.card_type == list_of_spells_that_draw_specific_cards[self.incoming_spell.name][0][
                    index_in_lists]:
                    if list_of_spells_that_draw_specific_cards[self.incoming_spell.name][1][index_in_lists] == "":
                        self.hand.append(card)
                        self.deck.remove(card)
                        if self.incoming_spell.name in list_of_spells_that_buff_drawn_cards:
                            buff_creature_with_spell(self.hand[-1], self)
                        break
                    elif list_of_spells_that_draw_specific_cards[self.incoming_spell.name][1][
                        index_in_lists] == card.category:
                        self.hand.append(card)
                        self.deck.remove(card)
                        if self.incoming_spell.name in list_of_spells_that_buff_drawn_cards:
                            buff_creature_with_spell(self.hand[-1], self)
                        break
