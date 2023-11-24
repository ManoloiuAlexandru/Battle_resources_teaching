import random

from clases.creatures import *
from clases.spells import *
from clases.Item import *
from clases.player import *
from decks.lists_of_cards import *

legendary_cards = ["Richard the Lionheart", "Frederick Barbarossa", "Basil II", "Jochi", "Joan of Arc"]


def battle(card1, card2, player1, player2):
    try:
        if card1.attack > 0:
            player1.logs += card1.name + " is in battle with " + card2.name + "\n"
            if card1.armored is True and card2.armored is True:
                if card2.attack > 0:
                    card1.armored = False
                if card1.attack > 0:
                    card2.armored = False
            elif card1.armored is True:
                card2.hp -= card1.attack
                if card2.attack > 0:
                    card1.armored = False
            elif card2.armored is True:
                card1.hp -= card2.attack
                if card1.attack > 0:
                    card2.armored = False
            else:
                card1.hp -= card2.attack
                card2.hp -= card1.attack
            card1.exhausted = True
            card1.number_of_attacks -= 1
            Player.clean_board(player1, player2)
            Player.battle_fields_effects(player1, player2)
    except Exception as e:
        print(e)


def cancel_card(card, player):
    player.mana += card.mana_cost
    player.hand.append(card)
    player.incoming_spell = None
    player.active_item = None


def reset_player(player, enemy_player):
    player.turn = 0
    player.used_power = 0
    try:
        if player.incoming_spell.name is not None and player.incoming_spell.name in list_of_resetting_spells:
            cancel_card(player.incoming_spell, player)
    except Exception as e:
        print(e)
    try:
        if player.active_item.name is not None and player.active_item.name in list_of_item:
            cancel_card(player.active_item.name, player)
    except Exception as e:
        print(e)
    for creature in player.battle_field:
        creature.exhausted = False
        creature.number_of_attacks += 1
    enemy_player.turn = 1
    enemy_player.empty_mana += 1
    if enemy_player.empty_mana > 10:
        enemy_player.empty_mana = 10
    enemy_player.mana = enemy_player.empty_mana
    enemy_player.draw_card()
    player.problem = ""
    enemy_player.problem = ""
    player.incoming_action = 0
    enemy_player.incoming_action = 0


def turn_switch(player1, player2):
    if player1.turn == 1:
        end_of_turn_action(player1, player2)
        reset_player(player1, player2)
        return 1
    else:
        end_of_turn_action(player2, player1)
        reset_player(player2, player1)
        return 2


def battle_logic(player, card_picked):
    for card in player.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            player.turn = 0
            return card


def damage_dealing(player, card_picked):
    for card in player.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            return card
    return None


def damage_to_player(player, current_card):
    player.hp -= current_card.attack
    current_card.exhausted = True
    current_card = None
    return player, current_card


def guard_checking(player, current_card):
    try:
        if "Guard" in current_card.description.split():
            return 1
        else:
            for card in player.battle_field:
                if "Guard" in card.description.split():
                    return 0
    except Exception as e:
        if current_card is None:
            for card in player.battle_field:
                if "Guard" in card.description.split():
                    return 0
    return 1


def check_target(player1, player2, card_picked):
    try:
        if player1.active_minion is not None:
            for card in player1.battle_field:
                if card_picked.get(card.name_for_html) is not None:
                    # heal_creature(card_picked, player1, list_of_creature_that_heal.get(player1.active_minion.name))
                    return 1
        for card in player2.battle_field:
            if card_picked.get(card.name_for_html) is not None:
                return 1
        if card_picked.get(
                player2.name) is not None and player1.active_minion.name in list_of_creature_that_deal_dmg_to_players:
            player2.hp -= list_of_creature_that_deal_dmg_to_players.get(player1.active_minion.name)
            return 1
    except Exception as e:
        print(e)
    try:
        if player1.incoming_spell.target == "self":
            for card in player1.battle_field:
                if card_picked.get(card.name_for_html) is not None:
                    return 1
        elif player1.incoming_spell.target == "enemy":
            for card in player1.battle_field:
                if card_picked.get(card.name_for_html) is not None:
                    return 0
            for card in player2.battle_field:
                if card_picked.get(card.name_for_html) is not None:
                    return 1
    except Exception as e:
        print(e)
    try:
        if player1.active_item is not None:
            for card in player1.battle_field:
                if card_picked.get(card.name_for_html) is not None:
                    return 1
    except Exception as e:
        print(e)
    return 0


def cast_spell(player1, player2, card_picked):
    destroy_minion = 0
    dmg_to_enemy_minions = 0
    if player1.incoming_spell.name in list_of_spells_that_draw_cards:
        for nr_cards in range(list_of_spells_that_draw_cards.get(player1.incoming_spell.name)):
            player1.draw_card()
    if player1.incoming_spell.name in list_of_healing_spells:
        heal_creature(card_picked, player1, int(player1.incoming_spell.heal_to_target()))
    if player1.incoming_spell.name == "Kill":
        destroy_minion = 1
    if player1.incoming_spell.name == "Volley":
        dmg_to_enemy_minions = 1
    if player1.incoming_spell.name in list_of_self_target:
        for card in player1.battle_field:
            if card_picked.get(card.name_for_html) is not None:
                buff_creature_with_spell(card, player1)
                break
    for card in player2.battle_field:
        if dmg_to_enemy_minions == 1:
            card.hp -= int(player1.incoming_spell.deal_dmg_to_target())
        elif card_picked.get(card.name_for_html) is not None and destroy_minion == 0:
            if card.armored is True:
                card.armored = False
                break
            else:
                card.hp -= int(player1.incoming_spell.deal_dmg_to_target())
                break
        elif card_picked.get(card.name_for_html) is not None:
            card.hp = 0
            break
    player1.check_player()
    player2.check_player()


def buff_creature_with_spell(card, player1):
    if player1.incoming_spell.name in list_of_spells_that_buff_specific_targets:
        if list_of_spells_that_buff_specific_targets.get(player1.incoming_spell.name)[0] in card.description.split():
            if "draw" == list_of_spells_that_buff_specific_targets.get(player1.incoming_spell.name)[1]:
                for nr_cards in range(list_of_spells_that_draw_cards_conditional.get(player1.incoming_spell.name)):
                    player1.draw_card()
        elif list_of_spells_that_buff_specific_targets.get(player1.incoming_spell.name)[0] == "":
            for i in range(list_of_spells_that_draw_cards_conditional.get(player1.incoming_spell.name)):
                random_card = player1.get_random_card(card, i)
                if random_card is not None:
                    player1.hand.append(random_card)
                    player1.deck.remove(random_card)
    card.hp += list_of_buff_spells.get(player1.incoming_spell.name)[0]
    card.max_hp += list_of_buff_spells.get(player1.incoming_spell.name)[0]
    card.attack += list_of_buff_spells.get(player1.incoming_spell.name)[1]
    if list_of_buff_spells.get(player1.incoming_spell.name)[2] not in card.description:
        card.description += " " + list_of_buff_spells.get(player1.incoming_spell.name)[2]
    card.check_creature(list_of_buff_spells.get(player1.incoming_spell.name)[2])


def general_spells(player, enemy_player, spell_name):
    if spell_name in list_of_spells_that_summon:
        if spell_name in list_of_spells_that_summon_specific_cards:
            for creature in range(list_of_spells_that_summon_specific_cards.get(spell_name)[0]):
                if len(player.battle_field) < 7:
                    list_of_animals_to_summon = list_of_spells_that_summon_specific_cards.get(spell_name)[1]
                    if type(list_of_animals_to_summon[0]) is list:
                        player.battle_field.append(
                            list_of_animals_to_summon[0][0])
                        list_of_animals_to_summon[0].remove(
                            list_of_animals_to_summon[0][0])
                        if not list_of_animals_to_summon[0]:
                            del (list_of_animals_to_summon[0])
                    else:
                        player.battle_field.append(
                            list_of_animals_to_summon[creature])
                        list_of_animals_to_summon.remove(
                            list_of_animals_to_summon[creature])
                    if player.battle_field[-1].name in list_of_creature_with_on_going_effect:
                        player.ongoing_effects.append(player.battle_field[-1])
        for i in range(0, list_of_spells_that_summon.get(spell_name)[1]):
            for card in player.deck:
                if list_of_spells_that_summon.get(spell_name)[0] == "":
                    card_picked = random.choice(player.deck)
                    if any(obj.card_type == "Creature" for obj in player.deck):
                        while card_picked.card_type != "Creature":
                            card_picked = random.choice(player.deck)
                        player.battle_field.append(card_picked)
                        player.deck.remove(card_picked)
                    break
                elif (list_of_spells_that_summon.get(spell_name)[0] in card.description.split()
                      and card.card_type == "Creature"):
                    player.battle_field.append(card)
                    player.deck.remove(card)
                    break
    elif spell_name == "Peace Treaty":
        for creature in player.battle_field[:]:
            return_to_hand(creature, player)
        for creature in enemy_player.battle_field[:]:
            return_to_hand(creature, enemy_player)
    elif player.incoming_spell.name in list_of_spells_that_affect_the_battlefield:
        affect_battle_field(player.incoming_spell, player, enemy_player)
    elif player.incoming_spell.name in list_of_spells_that_draw_cards:
        for nr_cards in range(list_of_spells_that_draw_cards.get(player.incoming_spell.name)):
            player.draw_card()
            if player.incoming_spell.name in list_of_spells_that_reduce_mana:
                if list_of_spells_that_reduce_mana.get(player.incoming_spell.name)[0] in player.hand[-1].description:
                    player.hand[-1].mana_cost_reduction(
                        list_of_spells_that_reduce_mana.get(player.incoming_spell.name)[1])
    elif player.incoming_spell.name in list_of_spells_with_specific_targets:
        creature_to_avoid = list_of_spells_with_specific_targets.get(player.incoming_spell.name)[0].split()[1]
        if list_of_spells_with_specific_targets.get(player.incoming_spell.name)[1] == "ALL":
            for creature in player.battle_field:
                if creature.check_creature_for_dmg(creature_to_avoid):
                    creature.hp -= list_of_dmg_spells.get(player.incoming_spell.name)
            for creature in enemy_player.battle_field:
                if creature.check_creature_for_dmg(creature_to_avoid):
                    creature.hp -= list_of_dmg_spells.get(player.incoming_spell.name)
    elif player.incoming_spell.name in list_of_dmg_spells:
        if "ALL" in player.incoming_spell.description:
            for creature in player.battle_field:
                creature.hp -= list_of_dmg_spells.get(player.incoming_spell.name)
            for creature in enemy_player.battle_field:
                creature.hp -= list_of_dmg_spells.get(player.incoming_spell.name)
        elif "enemies" in player.incoming_spell.description:
            for creature in enemy_player.battle_field:
                if creature.armored is True and list_of_dmg_spells.get(player.incoming_spell.name) < 98:
                    creature.armored = False
                else:
                    creature.hp -= list_of_dmg_spells.get(player.incoming_spell.name)
    Player.clean_board(player, enemy_player)


def destroy_creature(card_picked, player):
    for card in player.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            player.battle_field.remove(card)
            break


def put_item_on_creature(player1, player2, card_picked):
    if check_target(player1, player2, card_picked) == 0:
        player1.problem = "You need to select a card"
    else:
        put_item(player1, player2, card_picked)


def put_item(player1, player2, card_picked):
    for card in player1.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            if player1.active_item.name in list_of_items_that_draw_cards:
                for i in range(0, list_of_items_that_draw_cards.get(player1.active_item.name)):
                    player1.draw_card()
            card.items.append(player1.active_item)
            player1.active_item.status_update(card)
            player1.active_item = None
            break


def heal_creature(card_picked, player, amount):
    try:
        for card in player.battle_field:
            if card_picked.get(card.name_for_html) is not None:
                if card.hp + amount > card.max_hp:
                    card.hp = card.max_hp
                    player.logs += " on this card:" + card.name
                    break
                else:
                    card.hp += amount
                    player.logs += " on this card:" + card.name
                    break
        check_for_creature_with_effect_on(player, "heal")
    except Exception as e:
        print(e)
    player.incoming_action = 0


def check_for_creature_with_effect_on(player, action):
    for creature in player.battle_field:
        if creature.name in list_of_creature_that_are_effected_by_action and \
                list_of_creature_that_are_effected_by_action.get(creature.name)[3] == action:
            creature.hp += list_of_creature_that_are_effected_by_action.get(creature.name)[0]
            creature.max_hp += list_of_creature_that_are_effected_by_action.get(creature.name)[0]
            creature.attack += list_of_creature_that_are_effected_by_action.get(creature.name)[1]
            creature.description += list_of_creature_that_are_effected_by_action.get(creature.name)[2]
            creature.check_creature(list_of_creature_that_are_effected_by_action.get(creature.name)[2])


def deal_dmg_to_creature(card_picked, player, dmg):
    for card in player.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            card.hp -= dmg
            player.logs += " on this card:" + card.name


def destroy_creature_from_player(player1, player2, card_picked):
    if check_target(player1, player2, card_picked) == 0:
        player1.problem = "You need to select a card"
    else:
        if player1.active_minion.name in list_of_creature_that_deal_dmg_to_enemies:
            deal_dmg_to_creature(card_picked, player2,
                                 list_of_creature_that_deal_dmg_to_enemies.get(player1.active_minion.name))
            player1.active_minion = None
            player2.check_battlefield()
        elif player1.active_minion.name in list_of_creature_that_heal:
            heal_creature(card_picked, player1, list_of_creature_that_heal.get(player1.active_minion.name))
            if player1.active_minion.name in list_of_creature_that_buff:
                buff_creature(card_picked, player1)
            player1.active_minion = None
        elif player1.active_minion.name in list_of_creature_that_buff_specific_cards:
            for card in player1.battle_field:
                if card_picked.get(card.name_for_html) is not None and list_of_creature_that_buff_specific_cards.get(
                        player1.active_minion.name) == card.category:
                    buff_creature(card_picked, player1)
        elif player1.active_minion.name in list_of_creature_that_buff:
            buff_creature(card_picked, player1)
            player1.active_minion = None
        player1.incoming_action = 0


def buff_creature(card_picked, player1):
    try:
        if player1.active_minion is not None:
            for card in player1.battle_field:
                if card_picked.get(card.name_for_html) is not None:
                    card.hp += list_of_creature_that_buff.get(player1.active_minion.name)[0]
                    card.max_hp += list_of_creature_that_buff.get(player1.active_minion.name)[0]
                    card.attack += list_of_creature_that_buff.get(player1.active_minion.name)[1]
                    if list_of_creature_that_buff.get(player1.active_minion.name)[2] not in card.description:
                        card.description += " " + list_of_creature_that_buff.get(player1.active_minion.name)[2]
                    card.check_creature(list_of_creature_that_buff.get(player1.active_minion.name)[2])
    except Exception as e:
        print(e)


def cast_spell_from_player(player1, player2, card_picked):
    if player1.incoming_spell.name in list_of_spells_with_no_target:
        general_spells(player1, player2, player1.incoming_spell.name)
        player1.incoming_action = 0
        player1.incoming_spell = None
    elif card_picked.get(player2.name) is not None:
        player2.hp -= int(player1.incoming_spell.deal_dmg_to_target())
        cast_spell(player1, player2, card_picked)
        player1.incoming_action = 0
        player1.incoming_spell = None
    elif check_target(player1, player2, card_picked) == 0:
        player1.problem = "You need to select a card"
    else:
        cast_spell(player1, player2, card_picked)
        player2.check_battlefield()
        Player.battle_fields_effects(player1, player2)
        player1.incoming_action = 0
        player1.incoming_spell = None


def check_if_card_in_deck(card, deck):
    nr_app = 0
    for card_in_deck in deck:
        if card_in_deck.name in legendary_cards and card_in_deck.name == card.name:
            return 3
        elif card_in_deck.name == card.name and card.name not in legendary_cards:
            nr_app += 1
    return nr_app


def make_html_deck(deck, html_deck):
    for i in range(0, len(deck)):
        nr_ap = 0
        for j in range(0, len(deck)):
            if deck[i].name == deck[j].name:
                nr_ap += 1
        html_deck[deck[i].name] = [deck[i].mana_cost, nr_ap]
    return html_deck


def check_hero_power(player, enemy_player):
    if player.mana < 2:
        player.problem = "Not enough mana"
    else:
        if player.empire == "Byzantine Empire":
            list_of_auxiliary_soldiers = [
                Creature(1, "Shield soldier", 2, 0, "Guard", "soldier", len(player.deck) + 934),
                Creature(1, "Man at arms", 1, 1, "", "soldier", len(player.deck) + 944)]
            if len(player.battle_field) < 7:
                player.battle_field.append(random.choice(list_of_auxiliary_soldiers))
                player.used_power = 1
                player.mana_increase(-2)
            else:
                player.problem = "You don't have enough space"
        elif player.empire == "Holy Roman Empire":
            if len(player.battle_field) < 7:
                player.battle_field.append(Creature(1, "Kaiserliche", 1, 1, "", "soldier", len(player.deck) + 3112))
                player.used_power = 1
                player.mana_increase(-2)
            else:
                player.problem = "You don't have enough space"
        elif player.empire == "Mongol Empire":
            if len(player.battle_field) < 7:
                enemy_player.hp -= 2
                player.used_power = 1
                player.mana_increase(-2)
        elif player.empire == "Mesopotamia Empire":
            if len(player.battle_field) < 7:
                player.hp -= 2
                player.draw_card()
                player.used_power = 1
                player.mana_increase(-2)
            else:
                player.problem = "You don't have enough space"
    player.check_player()
    enemy_player.check_player()


def return_to_hand(card, player):
    card.hp = card.original_hp
    card.attack = card.original_attack
    card.description = card.original_description
    if len(player.hand) < 10:
        player.hand.append(card)
    player.battle_field.remove(card)


def end_of_turn_action(player, enemy_player):
    for card in player.battle_field:
        if card.name in list_of_creature_that_do_something_at_the_end_of_your_turn:
            if list_of_creature_that_do_something_at_the_end_of_your_turn.get(card.name)[0] == "draw":
                for nr_cards in range(list_of_creature_that_do_something_at_the_end_of_your_turn.get(card.name)[1]):
                    player.draw_card()
            elif list_of_creature_that_do_something_at_the_end_of_your_turn.get(card.name)[0] == "buff":
                card.hp += list_of_creature_that_do_something_at_the_end_of_your_turn.get(card.name)[1]
                card.max_hp += list_of_creature_that_do_something_at_the_end_of_your_turn.get(card.name)[1]
                card.attack += list_of_creature_that_do_something_at_the_end_of_your_turn.get(card.name)[2]


def affect_battle_field(card, player, enemy_player):
    if list_of_spells_that_affect_the_battlefield.get(card.name) == "self":
        for creature in player.battle_field:
            buff_creature_with_spell(creature, player)
