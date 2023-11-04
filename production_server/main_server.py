from flask import Flask, render_template, request, redirect, url_for

from clases.creatures import Creature
from clases.bot import Bot
from clases.game_logics import battle, turn_switch, battle_logic, damage_dealing, \
    damage_to_player, guard_checking, destroy_creature, check_target, cast_spell, destroy_creature_from_player, \
    cast_spell_from_player, put_item_on_creature
from clases.player import Player
from decks.decks_to_play import starter_deck, demo_deck, test_deck, \
    knight_deck_official, bot_deck, integration_deck, integration_deck_opponent, cards_that_are_in_the_game, \
    dict_of_decks

app = Flask(__name__)
global player1
global player2
global current_card
global attacked_player


def game_difficulty(player1_name, player2_name, play1_deck, player2_deck, difficulty):
    global player1
    global player2
    global attacked_player
    if difficulty == "easy":
        attacked_player = 2
        player1 = Player(player1_name)
        player1.hand = []
        player1.deck = dict_of_decks.get(play1_deck)
        player1.turn = 1
        player1.mana = 10
        player1.start_game()
        player1.battle_field.append(Creature(0, "Dummy", 98, 0, "", 99999))
        player1.battle_field.append(Creature(0, "Dummy", 98, 0, "", 99))
        player1.battle_field.append(Creature(0, "Dummy", 98, 0, "", 999))
        player1.hp = 999999999
        if player2_name == "Bot":
            player2 = Bot("Bot")
        else:
            player2 = Player("Andras")
        player2.hand = []
        player2.deck = dict_of_decks.get(player2_deck)
        player2.mana = 10
        player2.start_game()
    return player1, player2


def game_start(player1_name, player2_name, play1_deck, player2_deck, difficulty):
    global player1
    global player2
    try:
        if player1 is None:
            player1, player2 = game_difficulty(player1_name, player2_name, play1_deck, player2_deck, difficulty)
    except Exception as e:
        player1, player2 = game_difficulty(player1_name, player2_name, play1_deck, player2_deck, difficulty)


@app.route("/")
def game_options():
    return render_template("game_option.html")


@app.route("/rules")
def rules():
    return render_template("Rules.html")


@app.route("/play", methods=["POST", "GET"])
def show_battle():
    global player1
    global player2
    player1_name = request.form.get("player1")
    player2_name = request.form.get("player2")
    player1_deck = request.form.get("deck_player1")
    player2_deck = request.form.get("deck_player2")
    difficulty = request.form.get("difficulty")
    game_start(player1_name, player2_name, player1_deck, player2_deck, difficulty)
    return render_template("home.html", players=[player2, player1])


@app.route("/library")
def show_library():
    return render_template("library.html", library=cards_that_are_in_the_game)


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
    if player1.incoming_action == 4:
        put_item_on_creature(player1, player2, card_picked)
    if player2.incoming_action == 4:
        put_item_on_creature(player2, player1, card_picked)
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
        player2.play_hand(player1)
        if player2.check_move(player1) == 0:
            attacked_player = turn_switch(player1, player2)
        if player1.check_player() == 0:
            return render_template("END.html", player=player1)
        elif player2.check_player() == 0:
            return render_template("END.html", player=player2)
    return redirect(url_for('show_battle', players=[player2, player1]))


if __name__ == '__main__':
    app.run(debug=True)
