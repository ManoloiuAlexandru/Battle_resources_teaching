def battle(card1, card2, player1, player2):
    try:
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


def turn_switch(player1, player2):
    if player1.turn == 1:
        player2.turn = 1
        player1.turn = 0
        player2.mana_increase(1)
        reset(player1, player2)
        for creature in player1.battle_field:
            creature.exhausted = False
        return 1
    else:
        player2.turn = 0
        player1.turn = 1
        player1.mana_increase(1)
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
        if current_card.description == "Guard":
            return 1
        else:
            for card in player.battle_field:
                if card.description == "Guard":
                    return 0
    except Exception as e:
        if current_card is None:
            for card in player.battle_field:
                if card.description == "Guard":
                    return 0
    return 1


def check_target(player1, player2, card_picked):
    for card in player1.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            return 0
    for card in player2.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            return 1
    return 0


def destroy_creature(card_picked, player):
    for card in player.battle_field:
        if card_picked.get(card.name_for_html) is not None:
            player.battle_field.remove(card)
            break
