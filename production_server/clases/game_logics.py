from production_server.clases.player import *
from production_server.decks.lists_of_cards import *


def battle(card1, card2, player1, player2):
    try:
        if card1.attack > 0:
            player2.check_for_tactics("attacking", card1, card2)
            if card1 in player1.battle_field:
                player1.logs += card1.name + " is in battle with " + card2.name + "\n"
                if card1.armored is True and card2.armored is True:
                    if card2.attack > 0:
                        card1.armored = False
                    if card1.attack > 0:
                        card2.armored = False
                elif card1.armored is True:
                    card2.hp -= card1.attack
                    if card1.name in list_of_creature_that_freeze_on_attack:
                        card2.knocked_down_time = 2
                    player2.check_for_creature_with_effect_on("damage_taken", card2)
                    if card2.hp <= 0:
                        player1.check_for_creature_with_effect_on("kill_minion", None)
                    if card2.attack > 0:
                        card1.armored = False
                elif card2.armored is True:
                    card1.hp -= card2.attack
                    if card2.name in list_of_creature_that_freeze_on_attack:
                        card1.knocked_down_time = 2
                    if card1.attack > 0:
                        card2.armored = False
                    player1.check_for_creature_with_effect_on("damage_taken", card1)
                else:
                    card1.hp -= card2.attack
                    if card2.attack > 0:
                        if card2.name in list_of_creature_that_freeze_on_attack:
                            card1.knocked_down_time = 2
                        player1.check_for_creature_with_effect_on("damage_taken", card1)
                    card2.hp -= card1.attack
                    if card1.name in list_of_creature_that_freeze_on_attack and card1.attack > 0:
                        card2.knocked_down_time = 2
                    if card2.hp <= 0:
                        player1.check_for_creature_with_effect_on("kill_minion", None)
                    player2.check_for_creature_with_effect_on("damage_taken", card2)
                if "Rebuilder" in card1.description.split(" "):
                    player1.heal_player(card1.attack)
                if "Rebuilder" in card2.description.split(" "):
                    player2.heal_player(card2.attack)
                card1.exhausted = True
                card1.number_of_attacks -= 1
                player2.check_for_tactics("dmg_delt", card1, card2)
                Player.clean_board(player1, player2)
                Player.battle_fields_effects(player1, player2)
            for creature in list_of_creature_that_are_effected_by_action_once:
                list_of_creature_that_are_effected_by_action_once[creature] = 0
    except Exception as e:
        print("Error in battle")
        print(e)


def cancel_card(card, player):
    player.mana += card.mana_cost
    player.hand.append(card)
    player.incoming_spell = None
    player.active_defence = None


def reset_player(player, enemy_player):
    player.dict_of_actions["Spells_casted_this_turn"].clear()
    player.turn = 0
    player.used_power = 0
    player.number_of_assaults = 1
    try:
        if player.incoming_spell.name is not None and player.incoming_spell.name in list_of_resetting_spells:
            cancel_card(player.incoming_spell, player)
    except Exception as e:
        print("Error in reset_player")
        print(e)
    try:
        if player.incoming_spell is not None:
            player.incoming_spell = None
    except Exception as e:
        print("Error in reset_player")
        print(e)
    try:
        if player.active_defence.name is not None:
            cancel_card(player.active_defence.name, player)
    except Exception as e:
        print("Error in reset_player")
        print(e)
    for card in player.hand:
        if card.name in list_of_cards_that_reset_at_the_end_of_turn_in_hand:
            card.mana_cost = card.original_mana_cost
    for creature in player.battle_field:
        if "Can't attack" in creature.description:
            creature.exhausted = True
        else:
            creature.exhausted = False
        if creature.knocked_down_time > 0:
            creature.knocked_down_time -= 1
            creature.exhausted = True
        if creature.knocked_down_time == 0:
            creature.exhausted = False
        creature.number_of_attacks += 1
        creature.damage_taken_this_turn_from_empire = 0
    enemy_player.turn = 1
    enemy_player.empty_mana += 1
    if enemy_player.empty_mana > 10:
        enemy_player.empty_mana = 10
    enemy_player.mana = enemy_player.empty_mana
    if enemy_player.mana < enemy_player.debt:
        enemy_player.mana = 0
    else:
        enemy_player.mana -= enemy_player.debt
    enemy_player.last_debt = enemy_player.debt
    enemy_player.debt = 0
    enemy_player.draw_card()
    player.problem = ""
    enemy_player.problem = ""
    player.incoming_action = 0
    enemy_player.incoming_action = 0
    player.dict_of_actions["Minions_that_died"]["my_minions_that_died_this_turn"].clear()
    player.dict_of_actions["Damage_taken"] = 0
    player.dict_of_actions["Damage_done"] = 0
    player.enemy_player.dict_of_actions["Damage_taken"] = 0
    player.enemy_player.dict_of_actions["Damage_done"] = 0
    player.enemy_player.dict_of_actions["Minions_that_died"]["enemy_minions_that_died_this_turn"].clear()


def turn_switch(player1, player2):
    if player1.quest is not None:
        player1.quest.check_quest_progression(player1, None, "end_turn")
    if player2.quest is not None:
        player2.quest.check_quest_progression(player2, None, "end_turn")
    if player1.turn == 1:
        end_of_turn_action(player1, player2)
        reset_player(player1, player2)
        return 1
    else:
        end_of_turn_action(player2, player1)
        reset_player(player2, player1)
        return 2


def battle_logic(player, card_picked):
    if player.active_defence is not None:
        if card_picked.get(player.enemy_player.name) is not None:
            player.do_damage(player.enemy_player)
        for card in player.enemy_player.battle_field:
            if card_picked.get(card.name_for_html) is not None:
                player.do_damage(card)
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
    player.check_for_tactics("attacking", current_card, None)
    if current_card in player.enemy_player.battle_field:
        if player.immunity is False and player.armor == 0:
            player.hp -= current_card.attack
        elif player.armor >= current_card.attack:
            player.armor -= current_card.attack
        else:
            player.hp = player.hp + player.armor - current_card.attack
            player.armor = 0
        if "Rebuilder" in current_card.description.split(" "):
            player.enemy_player.heal_player(current_card.attack)
        player.dict_of_actions["Damage_taken"] += current_card.attack
        player.enemy_player.dict_of_actions["Damage_done"] -= current_card.attack
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
        print("Error in guard_checking")
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
                    if list_of_creature_that_can_target_yourself.get(player1.active_minion.name) is not None:
                        if card.armored is True and list_of_creature_that_can_target_yourself.get(
                                player1.active_minion.name) > 0:
                            card.armored = False
                        else:
                            card.hp -= list_of_creature_that_can_target_yourself.get(player1.active_minion.name)
                            card.damage_taken_this_turn_from_empire += list_of_creature_that_can_target_yourself.get(
                                player1.active_minion.name)
                            if player1.quest is not None:
                                player1.quest.check_quest_progression(player1, card, "damage")
                            player1.check_for_creature_with_effect_on("damage_taken", card)
                    if player1.active_minion.name in list_of_creature_that_heal:
                        heal_creature(card_picked, player1, list_of_creature_that_heal.get(player1.active_minion.name))
                    if player1.active_minion.name in list_of_creature_that_buff_specific_cards:
                        if card_picked.get(
                                card.name_for_html) is not None and list_of_creature_that_buff_specific_cards.get(
                            player1.active_minion.name) == card.category:
                            buff_creature(card_picked, player1)
                    elif player1.active_minion.name in list_of_creature_that_buff:
                        buff_creature(card_picked, player1)
                    if player1.active_minion.name in list_of_creature_that_debuff:
                        debuff_creature(player1, player2, card_picked)
                    return 1
        if player1.incoming_spell is not None:
            if player1.incoming_spell.name in list_of_spells_that_do_damage_to_your_minion_then_the_enemy:
                return check_target_for_self_cast(player1, player2, card_picked)
        for card in player1.battle_field:
            try:
                if card_picked.get(card.name_for_html) is not None:
                    return 1
            except Exception as e:
                print("Error in check_target")
                print(e)
        for card in player2.battle_field:
            try:
                if card_picked.get(card.name_for_html) is not None:
                    return 1

            except Exception as e:
                print("Error in check_target")
                print(e)
        if card_picked.get(
                player2.name) is not None and player1.active_minion.name in list_of_creature_that_deal_dmg_to_players:
            player2.hp -= list_of_creature_that_deal_dmg_to_players.get(player1.active_minion.name)
            return 1
        if card_picked.get(
                player1.name) is not None and player1.active_minion.name in list_of_creature_that_can_heal_players:
            player1.heal_player(list_of_creature_that_can_heal_players.get(player1.active_minion.name))
            return 1
    except Exception as e:
        print("Error in check_target")
        print(e)
    try:
        if card_picked.get(player1.name) is not None:
            player1.incoming_spell.target = "self"
        if player1.incoming_spell.target == "self":
            if card_picked.get(player1.name) is not None:
                player1.heal_player(list_of_spells_that_can_heal_player.get(player1.incoming_spell.name))
                return 1
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
        print("Error in check_target")
        print(e)
    try:
        if player1.active_defence is not None:
            for card in player1.battle_field:
                if card_picked.get(card.name_for_html) is not None:
                    return 1
    except Exception as e:
        print("Error in check_target")
        print(e)
    return 0


def cast_spell(player1, player2, card_picked):
    destroy_minion = 0
    if player1.incoming_spell.name in list_of_spells_that_freeze:
        freeze_target(player1, player2, card_picked)
    if player1.incoming_spell.name in list_of_spells_that_summon:
        spell_that_summon(player1, player2, player1.incoming_spell.name)
    if player1.incoming_spell.name in list_of_spells_that_draw_cards:
        for nr_cards in range(list_of_spells_that_draw_cards.get(player1.incoming_spell.name)):
            player1.draw_card()
    if player1.incoming_spell.name in list_of_healing_spells:
        heal_creature(card_picked, player1, list_of_healing_spells.get(player1.incoming_spell.name))
    if player1.incoming_spell.name in list_of_spells_that_kill_the_target:
        destroy_minion = 1
    if player1.incoming_spell.name in list_of_self_target:
        for card in player1.battle_field:
            if card_picked.get(card.name_for_html) is not None:
                if player1.incoming_spell.name in list_of_spells_that_do_something_conditional:
                    if cast_conditional_spell(card, player1.incoming_spell) == 0:
                        player1.hand.append(player1.incoming_spell)
                        player1.mana += player1.incoming_spell.mana_cost
                    else:
                        buff_creature_with_spell(card, player1)
                if player1.incoming_spell.name in list_of_spells_that_do_damage_to_your_minion_then_the_enemy:
                    break
                else:
                    buff_creature_with_spell(card, player1)
                break
    if player1.incoming_spell.name in list_of_dmg_spells:
        for card in player1.battle_field:
            if card_picked.get(card.name_for_html) is not None:
                if player1.incoming_spell.name in list_of_spells_that_do_something_conditional:
                    if cast_conditional_spell(card, player1.incoming_spell) == 0:
                        player1.hand.append(player1.incoming_spell)
                        player1.mana += player1.incoming_spell.mana_cost
                    else:
                        card.hp -= list_of_dmg_spells[player1.incoming_spell.name]
                else:
                    card.hp -= list_of_dmg_spells[player1.incoming_spell.name]
                break
    for card in player2.battle_field:
        if card_picked.get(
                card.name_for_html) is not None and player1.incoming_spell.name in list_of_spells_that_debuff:
            card.debuff_creature(list_of_spells_that_debuff.get(player1.incoming_spell.name), player1, player2)
            Player.clean_board(player1, player2)
            Player.battle_fields_effects(player1, player2)
        elif card_picked.get(card.name_for_html) is not None and destroy_minion == 0:
            if card.armored is True and list_of_dmg_spells[player1.incoming_spell.name] > 0:
                card.armored = False
                break
            else:
                if player1.incoming_spell.name in list_of_spells_that_do_something_conditional:
                    if cast_conditional_spell(card, player1.incoming_spell) == 0:
                        player1.hand.append(player1.incoming_spell)
                        player1.mana += player1.incoming_spell.mana_cost
                    else:
                        card.hp -= list_of_dmg_spells[player1.incoming_spell.name]
                else:
                    card.hp -= list_of_dmg_spells[player1.incoming_spell.name]
                    break
                if player1.incoming_spell.name in list_of_buff_spells:
                    if player1.incoming_spell.name in list_of_spells_that_do_something_conditional:
                        if cast_conditional_spell(card, player1.incoming_spell) == 0:
                            player1.hand.append(player1.incoming_spell)
                            player1.mana += player1.incoming_spell.mana_cost
                        else:
                            buff_creature_with_spell(card, player1)
                    else:
                        buff_creature_with_spell(card, player1)
                    break
                player1.check_for_creature_with_effect_on("damage_taken", card)
                player2.check_for_creature_with_effect_on("damage_taken", card)
                break
        elif card_picked.get(card.name_for_html) is not None:
            card.hp = 0
            break
    if player1.incoming_spell.name in list_of_spells_that_affect_one_target_and_then_the_rest:
        general_spells(player1, player2, player1.incoming_spell.name)
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
        card.description += "  " + list_of_buff_spells.get(player1.incoming_spell.name)[2]
    card.check_creature(list_of_buff_spells.get(player1.incoming_spell.name)[2])
    player1.check_for_creature_with_effect_on("cast spell:", card)


def spell_that_summon(player, enemy_player, spell_name):
    if spell_name in list_of_spells_that_summon_specific_cards:
        for creature in range(list_of_spells_that_summon_specific_cards.get(spell_name)[0]):
            if len(player.battle_field) < 7:
                list_of_animals_to_summon = list_of_spells_that_summon_specific_cards.get(spell_name)[1]
                if type(list_of_animals_to_summon[0]) is list:
                    player.battle_field.append(
                        list_of_animals_to_summon[0][0])
                    player.summoned_minions(list_of_animals_to_summon[0][0])
                    list_of_animals_to_summon[0].remove(
                        list_of_animals_to_summon[0][0])
                    if not list_of_animals_to_summon[0]:
                        del (list_of_animals_to_summon[0])
                else:
                    player.battle_field.append(
                        list_of_animals_to_summon[creature])
                    player.summoned_minions(list_of_animals_to_summon[creature])
                    list_of_animals_to_summon.remove(
                        list_of_animals_to_summon[creature])
                if player.battle_field[-1].name in list_of_creature_with_on_going_effect:
                    player.ongoing_effects.append(player.battle_field[-1])
            player.check_for_creature_with_effect_on("summ", player.battle_field[-1])
    for i in range(0, list_of_spells_that_summon.get(spell_name)[1]):
        for card in player.deck:
            if list_of_spells_that_summon.get(spell_name)[0] == "":
                card_picked = random.choice(player.deck)
                if any(obj.card_type == "Creature" for obj in player.deck):
                    while card_picked.card_type != "Creature":
                        card_picked = random.choice(player.deck)
                    player.battle_field.append(card_picked)
                    player.summoned_minions(card_picked)
                    player.deck.remove(card_picked)
                    player.check_for_creature_with_effect_on("summ", player.battle_field[-1])
                break
            elif (list_of_spells_that_summon.get(spell_name)[0] in card.description.split()
                  and card.card_type == "Creature"):
                player.battle_field.append(card)
                player.summoned_minions(card)
                player.deck.remove(card)
                player.check_for_creature_with_effect_on("summ", player.battle_field[-1])
                break
    if spell_name in list_of_spells_that_resummon:
        list_of_creature_to_resumm = []
        if "died" in list_of_spells_that_resummon[spell_name][0].split(":")[0]:
            for i in range(0, list_of_spells_that_resummon[spell_name][2]):
                try:
                    creature_to_resumm = random.choice(player.dict_of_actions["Minions_that_died"]["my_minions"])
                    if creature_to_resumm.category == list_of_spells_that_resummon[spell_name][1]:
                        list_of_creature_to_resumm.append(creature_to_resumm)
                        player.dict_of_actions["Minions_that_died"]["my_minions"].remove(list_of_creature_to_resumm[-1])
                except Exception as e:
                    print("Error in spell_that_summon")
                    print(e)
        resummon_creatures(player, list_of_creature_to_resumm)


def resummon_creatures(player, list_of_creature_to_resumm):
    for card in list_of_creature_to_resumm:
        card.hp = card.original_hp
        card.attack = card.original_attack
        card.description = card.original_description
        if "Charge" in card.description.split() or "Rush" in card.description.split():
            card.number_of_attacks = 1
            card.exhausted = card.check_creature("")
        if len(player.battle_field) < 7:
            player.battle_field.append(card)
            player.check_for_creature_with_effect_on("summ", card)


def general_spells(player, enemy_player, spell_name):
    if spell_name in list_of_quests:
        player.create_quest(player.incoming_spell)
    if spell_name in list_of_tactics:
        player.tactics.append(player.incoming_spell)
    if spell_name in list_of_spells_that_add_defences:
        player.active_defence = list_of_spells_that_add_defences.get(spell_name)
        put_item_on(player, enemy_player, None)
    if spell_name in list_of_spells_that_add_traps:
        player.number_of_troops += list_of_spells_that_add_traps.get(spell_name)
    if spell_name in list_of_spells_that_summon:
        spell_that_summon(player, enemy_player, spell_name)
    if spell_name in list_of_spells_that_freeze and spell_name not in list_of_spells_that_freeze_all_enemies:
        for creature in player.battle_field:
            freeze_target(player, enemy_player, {creature.name_for_html: ""})
        for creature in enemy_player.battle_field:
            freeze_target(enemy_player, player, {creature.name_for_html: ""})
    elif spell_name in list_of_spells_that_freeze_all_enemies:
        for creature in enemy_player.battle_field:
            freeze_target(enemy_player, player, {creature.name_for_html: ""})
    if spell_name == "Peace Treaty":
        for creature in player.battle_field[:]:
            return_to_hand(creature, player)
        for creature in enemy_player.battle_field[:]:
            return_to_hand(creature, enemy_player)
    elif player.incoming_spell.name in list_of_spells_that_affect_the_battlefield:
        affect_battle_field(player.incoming_spell, player, enemy_player)
    elif player.incoming_spell.name in list_of_spells_that_draw_cards:
        if player.incoming_spell.name in list_of_spells_that_draw_specific_cards:
            player.spell_draw_specific_card()
        else:
            for nr_cards in range(list_of_spells_that_draw_cards.get(player.incoming_spell.name)):
                player.draw_card()
                if player.incoming_spell.name in list_of_spells_that_reduce_mana:
                    if list_of_spells_that_reduce_mana.get(player.incoming_spell.name)[0] in player.hand[
                        -1].description:
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
        if player.incoming_spell.name in list_of_spells_that_target_random_creatures:
            if list_of_spells_that_target_random_creatures.get(player.incoming_spell.name) == 13:
                pick_random_creature(player, enemy_player)
            elif list_of_spells_that_target_random_enemy_creature.get(player.incoming_spell.name) == 1:
                pick_random_enemy_creature(enemy_player, player.incoming_spell, "dmg")
            elif 1 < list_of_spells_that_target_random_enemy_creature.get(player.incoming_spell.name) < 13:
                pick_random_enemy_creatures(enemy_player, player.incoming_spell, "dmg",
                                            list_of_spells_that_target_random_enemy_creature.get(
                                                player.incoming_spell.name))
                player.incoming_spell.description = ""
        if "ALL" in player.incoming_spell.description:
            damage_to_all_minions(player, enemy_player)
        elif "enemies" in player.incoming_spell.description:
            for creature in enemy_player.battle_field:
                if creature.armored is True and 0 < list_of_dmg_spells.get(player.incoming_spell.name) < 98:
                    creature.armored = False
                else:
                    creature.hp -= list_of_dmg_spells.get(player.incoming_spell.name)
                    enemy_player.check_for_creature_with_effect_on("damage_taken", creature)
        elif "all characters" in player.incoming_spell.description:
            damage_to_all_minions(player, enemy_player)
            player.hp -= list_of_dmg_spells.get(player.incoming_spell.name)
            enemy_player.hp -= list_of_dmg_spells.get(player.incoming_spell.name)

    Player.clean_board(player, enemy_player)


def destroy_creature(card_picked, player):
    for card in player.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            player.battle_field.remove(card)
            break


def damage_to_all_minions(player, enemy_player):
    for creature in player.battle_field:
        if creature.armored is True and 0 < list_of_dmg_spells.get(player.incoming_spell.name) < 90:
            creature.armored = False
        else:
            creature.hp -= list_of_dmg_spells.get(player.incoming_spell.name)
            creature.damage_taken_this_turn_from_empire += list_of_dmg_spells.get(player.incoming_spell.name)
            if player.quest is not None:
                player.quest.check_quest_progression(player, None, "damage")
            player.check_for_creature_with_effect_on("damage_taken", creature)
    for creature in list_of_creature_that_are_effected_by_action_once:
        list_of_creature_that_are_effected_by_action_once[creature] = 0
    for creature in enemy_player.battle_field:
        if creature.armored is True and 0 < list_of_dmg_spells.get(player.incoming_spell.name) < 90:
            creature.armored = False
        else:
            creature.hp -= list_of_dmg_spells.get(player.incoming_spell.name)
            enemy_player.check_for_creature_with_effect_on("damage_taken", creature)
    for creature in list_of_creature_that_are_effected_by_action_once:
        list_of_creature_that_are_effected_by_action_once[creature] = 0


def put_item_on(player1, player2, card_picked):
    player1.number_of_troops = player1.active_defence.number_of_troops
    player1.nr_of_assaults = player1.active_defence.nr_of_assaults


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
        player.check_for_creature_with_effect_on("heal", None)
    except Exception as e:
        print("Error in heal_creature")
        print(e)
    player.incoming_action = 0


def deal_dmg_to_creature(card_picked, player, dmg):
    for card in player.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            if player.enemy_player.active_minion.name in list_of_creature_that_buff_specific_cards:
                if card_picked.get(
                        card.name_for_html) is not None and list_of_creature_that_buff_specific_cards.get(
                    player.enemy_player.active_minion.name) == card.category:
                    buff_creature(card_picked, player.enemy_player)
            elif player.enemy_player.active_minion.name in list_of_creature_that_buff:
                buff_creature(card_picked, player.enemy_player)
            if dmg < 90 and card.armored is True:
                card.armored = False
            else:
                card.hp -= dmg
            player.logs += " on this card:" + card.name


def destroy_creature_from_player(player1, player2, card_picked):
    if player1.power is not None:
        use_hero_power_on_target(player1, player2, card_picked)
    elif check_target(player1, player2, card_picked) == 0:
        player1.problem = "You need to select a card"
    else:
        if list_of_creature_that_deal_dmg_to_enemies.get(player1.active_minion.name) is not None:
            deal_dmg_to_creature(card_picked, player2,
                                 list_of_creature_that_deal_dmg_to_enemies.get(player1.active_minion.name))
        if list_of_creature_that_debuff.get(player1.active_minion.name) is not None:
            debuff_creature(player1, player2, card_picked)
        player1.active_minion = None
        player1.incoming_action = 0
        Player.clean_board(player1, player2)


def use_hero_power_on_target(player1, player2, card_picked):
    power_dict = {"Greek": 1, "Macedonian Empire": 2}
    if player1.power is not None:
        for card in player1.battle_field:
            if card_picked.get(card.name_for_html) is not None:
                if player1.power in power_dict:
                    if card.armored is not True:
                        card.hp -= power_dict[player1.power]
                    else:
                        card.armored = False
                    player1.power = None
        for card in player2.battle_field:
            if card_picked.get(card.name_for_html) is not None:
                if player1.power in power_dict:
                    if card.armored is not True:
                        card.hp -= power_dict[player1.power]
                    else:
                        card.armored = False
                    player1.power = None
        if card_picked.get(player2.name) is not None:
            if player2.armor == 0:
                player2.hp -= power_dict[player1.power]
            else:
                player2.armor -= power_dict[player1.power]
            player1.power = None

        if card_picked.get(player1.name) is not None:
            if player1.armor == 0:
                player1.hp -= power_dict[player1.power]
            else:
                player1.armor -= power_dict[player1.power]
            player1.power = None


def debuff_creature(player1, player2, card_picked):
    for card in player1.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            card.debuff_creature(list_of_creature_that_debuff.get(player1.active_minion.name), player1, player2)
    for card in player2.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            card.debuff_creature(list_of_creature_that_debuff.get(player1.active_minion.name), player1, player2)
    Player.clean_board(player1, player2)
    Player.battle_fields_effects(player1, player2)


def buff_creature(card_picked, player1):
    try:
        if player1.active_minion is not None:
            for card in player1.battle_field:
                if card_picked.get(card.name_for_html) is not None:
                    player1.buff_card_from_hand(card, player1.active_minion)

            for card in player1.enemy_player.battle_field:
                if card_picked.get(card.name_for_html) is not None:
                    player1.enemy_player.buff_card_from_hand(card, player1.active_minion)
    except Exception as e:
        print("Error in buff_creature")
        print(e)


def cast_spell_from_player(player1, player2, card_picked):
    if player1.incoming_spell.name in list_of_spells_with_no_target:
        general_spells(player1, player2, player1.incoming_spell.name)
        player1.dict_of_actions["Spells_casted"].append(player1.incoming_spell)
        player1.dict_of_actions["Spells_casted_this_turn"].append(player1.incoming_spell)
        if player1.incoming_spell.name in list_of_cards_that_discard_after_effect:
            player1.card_discard(list_of_cards_that_discard.get(player1.incoming_spell.name), player1.incoming_spell)
        player1.incoming_action = 0
        check_for_spell_reset(player1)
        player1.incoming_spell = None
    elif card_picked.get(
            player2.name) is not None and player1.incoming_spell.name not in list_of_dmg_spells_but_not_to_player:
        player2.hp -= list_of_dmg_spells.get(player1.incoming_spell.name)
        cast_spell(player1, player2, card_picked)
        player1.dict_of_actions["Spells_casted"].append(player1.incoming_spell)
        player1.dict_of_actions["Spells_casted_this_turn"].append(player1.incoming_spell)
        player1.incoming_action = 0
        check_for_spell_reset(player1)
        player1.incoming_spell = None
    elif check_target(player1, player2, card_picked) == 0:
        player1.problem = "You need to select a card"
    else:
        cast_spell(player1, player2, card_picked)
        Player.battle_fields_effects(player1, player2)
        player1.dict_of_actions["Spells_casted"].append(player1.incoming_spell)
        player1.dict_of_actions["Spells_casted_this_turn"].append(player1.incoming_spell)
        if player1.incoming_spell.name in list_of_spells_that_target_multiple_targets and \
                list_of_spells_that_target_multiple_targets[player1.incoming_spell.name] > 0:
            player1.incoming_action = 3
            list_of_spells_that_target_multiple_targets[player1.incoming_spell.name] -= 1
            if list_of_spells_that_target_multiple_targets[player1.incoming_spell.name] == 0:
                player1.incoming_action = 0
                check_for_spell_reset(player1)
                player1.incoming_spell = None
        else:
            player1.incoming_action = 0
            check_for_spell_reset(player1)
            player1.incoming_spell = None
    Player.clean_board(player1, player2)


def check_if_card_in_deck(card, deck, mode):
    nr_app = 0
    for card_in_deck in deck:
        if (card_in_deck.name in legendary_cards and card_in_deck.name == card.name) or (
                mode == "there_can_be_only_one" and card_in_deck.name == card.name):
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
    summoned_creature = None
    if player.mana < 2:
        player.problem = "Not enough mana"
    else:
        if player.empire == "Byzantine Empire":
            list_of_auxiliary_soldiers = [
                Creature(1, "Shield soldier", 2, 0, "Guard", "soldier", generate_random_int()),
                Creature(1, "Man at arms", 1, 1, "", "soldier", generate_random_int())]
            if len(player.battle_field) < 7:
                summoned_creature = random.choice(list_of_auxiliary_soldiers)
                player.battle_field.append(summoned_creature)
                player.summoned_minions(summoned_creature)
                player.used_power = 1
                player.mana_increase(-2)
            else:
                player.problem = "You don't have enough space"
        elif player.empire == "Mercenary Empire":
            player.power = "Mercenary Empire"
            player.discover_a_card("Mercenary Empire")
            player.used_power = 1
            player.mana_increase(-2)
        elif player.empire == "Holy Roman Empire":
            if len(player.battle_field) < 7:
                summoned_creature = Creature(1, "Kaiserliche", 1, 1, "", "soldier", generate_random_int())
                player.battle_field.append(summoned_creature)
                player.summoned_minions(summoned_creature)
                player.used_power = 1
                player.mana_increase(-2)
            else:
                player.problem = "You don't have enough space"
        elif player.empire == "Mongol Empire":
            if enemy_player.immunity is False:
                if enemy_player.armor < 2:
                    enemy_player.hp = enemy_player.hp + enemy_player.armor - 2
                    enemy_player.armor = 0
                else:
                    enemy_player.armor -= 2
                player.used_power = 1
                player.mana_increase(-2)
        elif player.empire == "Mongol Hordes":
            if enemy_player.immunity is False:
                if enemy_player.armor < 3:
                    enemy_player.hp = enemy_player.hp + enemy_player.armor - 3
                    enemy_player.armor = 0
                else:
                    enemy_player.armor -= 3
                player.used_power = 1
                player.mana_increase(-2)
        elif player.empire == "Mesopotamia Empire":
            if player.immunity is False:
                if player.armor < 2:
                    player.hp = player.hp + player.armor - 2
                    player.armor = 0
                else:
                    player.armor -= 2
            player.draw_card()
            player.used_power = 1
            player.mana_increase(-2)
        elif player.empire == "Test of Time":
            player.draw_card()
            player.used_power = 1
            player.mana_increase(-2)
        elif player.empire == "Roman empire":
            player.armor += 2
            player.used_power = 1
            player.mana_increase(-2)
        elif player.empire == "Fortifications!":
            player.armor += 4
            player.used_power = 1
            player.mana_increase(-2)
        elif player.empire == "Greek empire":
            player.power = "Greek"
            player.used_power = 1
            player.mana_increase(-2)
        elif player.empire == "Macedonian Empire":
            player.power = "Macedonian Empire"
            player.used_power = 1
            player.mana_increase(-2)
        elif player.empire == "Order of the Church":
            for i in range(0, 2):
                summoned_creature = Creature(1, "Kaiserliche", 1, 1, "", "soldier", generate_random_int())
                player.battle_field.append(summoned_creature)
                player.summoned_minions(summoned_creature)
            player.used_power = 1
            player.mana_increase(-2)
    player.check_player()
    enemy_player.check_player()
    player.check_for_creature_with_effect_on("summ", summoned_creature)


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
            end_of_turn_card = list_of_creature_that_do_something_at_the_end_of_your_turn.get(card.name)
            if end_of_turn_card[0] == "draw":
                for nr_cards in range(end_of_turn_card[1]):
                    player.draw_card()
            elif "damage" in end_of_turn_card[0].split():
                if "all" in end_of_turn_card[0].split():
                    if "enemies" in end_of_turn_card[0].split():
                        list_of_targets = []
                        list_of_targets.extend(enemy_player.battle_field)
                        list_of_targets.append(enemy_player.name)
                        random_enemy = random.choice(list_of_targets)
                        if isinstance(random_enemy, str):
                            enemy_player.hp -= end_of_turn_card[1]
                            player.dict_of_actions["Damage_done"] += end_of_turn_card[1]
                        elif random_enemy.armored is True:
                            random_enemy.armored = False
                        else:
                            random_enemy.hp -= end_of_turn_card[1]
                        list_of_targets.clear()
    Player.clean_board(player, enemy_player)


def affect_battle_field(card, player, enemy_player):
    if list_of_spells_that_affect_the_battlefield.get(card.name) == "self":
        for creature in player.battle_field:
            buff_creature_with_spell(creature, player)


def pick_random_creature(player, enemy_player):
    all_creatures = []
    all_creatures.extend(player.battle_field)
    all_creatures.extend(enemy_player.battle_field)
    last_on_standing = random.choice(all_creatures)
    for creature in player.battle_field[:]:
        if last_on_standing != creature:
            creature.hp -= 99
    for creature in enemy_player.battle_field[:]:
        if last_on_standing != creature:
            creature.hp -= 99


def cast_conditional_spell(card, spell):
    if list_of_spells_that_do_something_conditional.get(spell.name) == "damaged":
        if card.hp < card.max_hp:
            return 1
    return 0


def pick_random_enemy_creature(player, card, effect):
    try:
        card_picked = random.choice(player.battle_field)
        if effect == "dmg":
            card_picked.hp -= list_of_dmg_spells[card.name]
    except Exception as e:
        print("Error in pick_random_enemy_creature")
        print(e)


def pick_random_enemy_creatures(player, card, effect, nr_targets):
    for i in range(nr_targets):
        try:
            card_picked = random.choice(player.battle_field)
            if effect == "dmg":
                card_picked.hp -= list_of_dmg_spells[card.name]
        except Exception as e:
            print("Error in pick_random_enemy_creatures")
            print(e)


def freeze_target(player, enemy_player, card):
    for creature in player.battle_field:
        if card.get(creature.name_for_html) is not None:
            creature.knocked_down_time = 1
            creature.exhausted = creature.charge_check()
    for creature in enemy_player.battle_field:
        if card.get(creature.name_for_html) is not None:
            creature.knocked_down_time = 1
            creature.exhausted = creature.charge_check()


def check_target_for_self_cast(player1, player2, card_picked):
    if player1.incoming_spell is not None:
        if player1.incoming_spell.name in list_of_spells_that_do_damage_to_your_minion_then_the_enemy:
            for creature in player1.battle_field:
                if card_picked.get(creature.name_for_html) is not None:
                    if list_of_spells_that_do_damage_to_your_minion_then_the_enemy[player1.incoming_spell.name][
                        'own_minion_picked'] is False:
                        list_of_spells_that_do_damage_to_your_minion_then_the_enemy[player1.incoming_spell.name][
                            'own_minion_picked'] = True
                        return 1
            for creature in player2.battle_field:
                if card_picked.get(creature.name_for_html) is not None:
                    if list_of_spells_that_do_damage_to_your_minion_then_the_enemy[player1.incoming_spell.name][
                        'enemy_minion_picked'] is False and \
                            list_of_spells_that_do_damage_to_your_minion_then_the_enemy[player1.incoming_spell.name][
                                'own_minion_picked'] is True:
                        list_of_spells_that_do_damage_to_your_minion_then_the_enemy[player1.incoming_spell.name][
                            'enemy_minion_picked'] = True
                        return 1
    return 0


def check_for_spell_reset(player1):
    if player1.incoming_spell.name in list_of_spells_that_do_damage_to_your_minion_then_the_enemy:
        if list_of_spells_that_do_damage_to_your_minion_then_the_enemy[player1.incoming_spell.name][
            "own_minion_picked"] is True and \
                list_of_spells_that_do_damage_to_your_minion_then_the_enemy[player1.incoming_spell.name][
                    "enemy_minion_picked"] is True:
            list_of_spells_that_target_multiple_targets[player1.incoming_spell.name] = 2
            list_of_spells_that_do_damage_to_your_minion_then_the_enemy[player1.incoming_spell.name][
                "own_minion_picked"] = False
            list_of_spells_that_do_damage_to_your_minion_then_the_enemy[player1.incoming_spell.name][
                "enemy_minion_picked"] = False
