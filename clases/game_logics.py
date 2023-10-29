def battle(card1, card2, player1, player2):
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


def turn_switch(player1, player2):
    if player1.turn == 1:
        player2.turn = 1
        player1.turn = 0
        player2.mana_increase(1)
        player1.problem = ""
        player2.problem = ""
        for creature in player1.battle_field:
            creature.exhausted = False
        return 1
    else:
        player2.turn = 0
        player1.turn = 1
        player1.mana_increase(1)
        player1.problem = ""
        player2.problem = ""
        for creature in player2.battle_field:
            creature.exhausted = False
        return 2


def battle_logic(player, card_picked):
    for card in player.battle_field:
        if card_picked.get(card.name + card.id) is not None:
            player.turn = 0
            return card


def damage_dealing(player, card_picked):
    for card in player.battle_field:
        if card_picked.get(card.name + card.id) is not None:
            return card
    return None


def damage_to_player(player, current_card):
    player.hp -= current_card.attack
    current_card.exhausted = True
    current_card = None
    return player, current_card
