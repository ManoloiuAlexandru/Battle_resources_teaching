from flask import Flask, render_template, request, redirect, url_for

from ITschool_projects.battle_resources.clases.bot import Bot
from ITschool_projects.battle_resources.clases.game_logics import battle, turn_switch, battle_logic, damage_dealing, \
    damage_to_player, guard_checking, destroy_creature, check_target, cast_spell, destroy_creature_from_player, \
    cast_spell_from_player
from ITschool_projects.battle_resources.clases.player import Player
from ITschool_projects.battle_resources.decks.decks_to_play import starter_deck, demo_deck, test_deck, knight_deck, \
    knight_deck_official, bot_deck

app = Flask(__name__)
global player1
global player2
global current_card
global attacked_player


def game_start():
    global player1
    global player2
    global attacked_player
    try:
        if player1 is None:
            attacked_player = 2
            player1 = Player("Alex")
            player1.turn = 1
            player1.hand = demo_deck
            player1.mana = 1
            # player2 = Player("Andras")
            # player2.hand = starter_deck
            # player2.mana = -100
    except Exception as e:
        attacked_player = 2
        player1 = Player("Alex")
        player1.hand = test_deck
        player1.turn = 1
        player1.mana = 10
        # player2 = Player("Andras")
        # player2.hand = test_deck
        # player2.mana = 10
        player2 = Bot("Bot")
        player2.hand = bot_deck
        player2.mana = 10


@app.route("/")
def show_battle():
    game_start()
    return render_template("home.html", players=[player2, player1])


@app.route("/update_battle_field", methods=["POST", "GET"])
def update_battle():
    global player1
    global player2
    if attacked_player == 2:
        card_picked = request.form
        if player1.put_card_on_field(card_picked) != 0:
            return redirect(url_for('battlefield_fight'))
        elif player1.put_card_on_field(card_picked) == 0:
            player1.problem = "Not enough mana"
    elif type(player2) == Player:
        card_picked = request.form
        if player2.put_card_on_field(card_picked) != 0:
            return redirect(url_for('battlefield_fight'))
        elif player2.put_card_on_field(card_picked) == 0:
            player2.problem = "No enough mana"
    return redirect(url_for('show_battle', players=[player2, player1], attacking_card=None))


@app.route("/battlefield_action", methods=["POST", "GET"])
def battlefield_fight():
    card_picked = request.form
    global current_card
    global player2
    global player1
    player_selected = False
    if player1.incoming_action == 2:
        destroy_creature_from_player(player1, player2, card_picked)
    if player1.incoming_action == 3:
        cast_spell_from_player(player1, player2, card_picked)
    if player2.incoming_action == 3:
        cast_spell_from_player(player2, player1, card_picked)
    if player2.incoming_action == 2:
        destroy_creature_from_player(player2, player1, card_picked)
    if player1.turn == 1:
        current_card = battle_logic(player1, card_picked)
    elif attacked_player == 2:
        card = damage_dealing(player2, card_picked)
        if (card is not None or card_picked.get(player2.name) is not None) and current_card.exhausted is True:
            player1.turn = 1
        elif card is not None and guard_checking(player2, card) == 1:
            battle(current_card, card, player1, player2)
            player1.turn = 1
            current_card = None
        elif card_picked.get(player2.name) is not None and guard_checking(player2,
                                                                          card) == 1:
            current_card.exhausted = True
            player2, current_card = damage_to_player(player2, current_card)
            player_selected = True
            player1.turn = 1
            current_card = None
            if player2.check_player() == 0:
                return render_template("END.html", player=player2)
        elif guard_checking(player2, card) == 0:
            player1.problem = "There are guards in battle"
            return redirect(url_for('show_battle', players=[player2, player1]))
    if player2.turn == 1:
        current_card = battle_logic(player2, card_picked)
    elif attacked_player == 1:
        card = damage_dealing(player1, card_picked)
        if (card is not None or card_picked.get(player1.name) is not None) and current_card.exhausted is True:
            player2.turn = 1
        elif card is not None and guard_checking(player1, card) == 1:
            battle(current_card, card, player2, player1)
            player2.turn = 1
        elif card_picked.get(player1.name) is not None and guard_checking(player1, card) == 1:
            player1, current_card = damage_to_player(player1, current_card)
            player2.turn = 1
            player_selected = True
            if player1.check_player() == 0:
                return render_template("END.html", player=player1)
        elif guard_checking(player1, card) == 0:
            player2.problem = "There are guards in battle"
            return redirect(url_for('show_battle', players=[player2, player1]))
    if card_picked is None or player_selected is not True:
        if attacked_player == 1:
            player2.problem = "You need to select a card"
        else:
            player1.problem = "You need to select a card"
    else:
        player1.problem = ""
        player2.problem = ""
    return redirect(url_for('show_battle', players=[player2, player1]))


@app.route("/end_turn", methods=["POST"])
def end_turn():
    global attacked_player
    attacked_player = turn_switch(player1, player2)
    if type(player2) == Bot:
        player2.play_hand()
        if player2.check_move(player1) == 0:
            attacked_player = turn_switch(player1, player2)
        if player1.check_player() == 0:
            return render_template("END.html", player=player1)
    return redirect(url_for('show_battle', players=[player2, player1]))


if __name__ == '__main__':
    app.run(debug=True)
