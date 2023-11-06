from clases.creatures import list_of_creature_that_deal_dmg_to_enemies, list_of_creature_that_heal
from clases.spells import list_of_healing_spells

from clases.spells import list_of_resetting_spells

from clases.Item import list_of_item

from ITschool_projects.battle_resources.production_server.clases.spells import list_of_self_target


def battle(card1, card2, player1, player2):
    try:
        if card1.exhausted is False:
            if card1.attack >= card2.hp and card1.hp <= card2.attack:
                player2.battle_field.remove(card2)
                player1.battle_field.remove(card1)
            elif card1.attack < card2.hp and card2.attack >= card1.hp:
                player1.battle_field.remove(card1)
                card2.hp -= card1.attack
            elif card1.attack >= card2.hp and card1.hp > card2.attack:
                player2.battle_field.remove(card2)
                card1.hp -= card2.attack
                card1.exhausted = True
            else:
                card1.hp -= card2.attack
                card2.hp -= card1.attack
                card1.exhausted = True

    except Exception as e:
        print(e)


def cancel_card(card, player):
    player.mana += card.mana_cost
    player.hand.append(card)
    player.incoming_spell = None
    player.active_item = None


def turn_switch(player1, player2):
    if player1.turn == 1:
        try:
            if player1.incoming_spell.name is not None and player1.incoming_spell.name in list_of_resetting_spells:
                cancel_card(player1.incoming_spell, player1)
        except Exception as e:
            print(e)
        try:
            if player1.active_item.name is not None and player1.active_item.name in list_of_item:
                cancel_card(player1.active_item.name, player1)
        except Exception as e:
            print(e)
        player2.turn = 1
        player1.turn = 0
        player2.empty_mana += 1
        if player2.empty_mana > 10:
            player2.empty_mana = 10
        player2.mana = player2.empty_mana
        reset(player1, player2)
        player2.draw_card()
        for creature in player1.battle_field:
            creature.exhausted = False
        return 1
    else:
        try:
            if player2.incoming_spell.name is not None and player2.incoming_spell.name in list_of_resetting_spells:
                cancel_card(player2.incoming_spell, player2)
        except Exception as e:
            print(e)
        try:
            if player2.active_item.name is not None and player2.active_item.name in list_of_item:
                cancel_card(player2.active_item.name, player2)
        except Exception as e:
            print(e)
        player2.turn = 0
        player1.turn = 1
        player1.empty_mana += 1
        if player1.empty_mana > 10:
            player1.empty_mana = 10
        player1.mana = player1.empty_mana
        player1.draw_card()
        reset(player1, player2)
        for creature in player2.battle_field:
            creature.exhausted = False
        return 2


def reset(player1, player2):
    player1.problem = ""
    player2.problem = ""
    player1.incoming_action = 0
    player2.incoming_action = 0


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
                    heal_creature(card_picked, player1, list_of_creature_that_heal.get(player1.active_minion.name))
                    return 0
        for card in player2.battle_field:
            if card_picked.get(card.name_for_html) is not None:
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
    if player1.incoming_spell.name in list_of_healing_spells:
        heal_creature(card_picked, player1, int(player1.incoming_spell.heal_to_target()))
    if player1.incoming_spell.name == "Kill":
        destroy_minion = 1
    if player1.incoming_spell.name == "Volley":
        dmg_to_enemy_minions = 1
    if player1.incoming_spell.name in list_of_self_target:
        for card in player1.battle_field:
            if card_picked.get(card.name_for_html) is not None and list_of_self_target.get(
                    player1.incoming_spell.name) not in card.description.split():
                card.description += " " + list_of_self_target.get(player1.incoming_spell.name)
                break
    # elif player1.incoming_spell.name == "Horse riding lessons":
    #     for card in player1.battle_field:
    #         if card_picked.get(card.name_for_html) is not None and "Charge" not in card.description.split():
    #             card.description += " Charge"
    #             card.exhausted = False
    #             break
    for card in player2.battle_field:
        if dmg_to_enemy_minions == 1:
            card.hp -= int(player1.incoming_spell.deal_dmg_to_target())
        elif card_picked.get(card.name_for_html) is not None and destroy_minion == 0:
            card.hp -= int(player1.incoming_spell.deal_dmg_to_target())
            break
        elif card_picked.get(card.name_for_html) is not None:
            card.hp = 0
            break


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
    except Exception as e:
        print(e)
    player.incoming_action = 0
    player.active_minion = None


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
            player1.active_minion = None
        player1.incoming_action = 0


def cast_spell_from_player(player1, player2, card_picked):
    if card_picked.get(player2.name) is not None:
        player2.hp -= int(player1.incoming_spell.deal_dmg_to_target())
        player1.incoming_action = 0
    elif check_target(player1, player2, card_picked) == 0:
        player1.problem = "You need to select a card"
    else:
        cast_spell(player1, player2, card_picked)
        player2.check_battlefield()
        player1.incoming_action = 0
        player1.incoming_spell = None
