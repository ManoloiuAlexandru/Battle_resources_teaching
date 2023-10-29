from flask import Flask, render_template, request, redirect, url_for, flash

from ITschool_projects.battle_resources.clases.creatures import Creature
from ITschool_projects.battle_resources.clases.game_logics import battle, turn_switch, battle_logic, damage_dealing, \
    damage_to_player
from ITschool_projects.battle_resources.clases.player import Player

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
            player1.hand = [Creature(1, "Peasant", 1, 1, None, 1),
                            Creature(1, "Peasant", 1, 1, None, 2)]
            player1.mana = 1
            player2 = Player("Andras")
            player2.hand = [Creature(1, "Peasant", 1, 1, None, 3),
                            Creature(1, "Knight", 3, 3, None, 4)]
            player2.mana = -100
    except Exception as e:
        attacked_player = 2
        player1 = Player("Alex")
        player1.hand = [Creature(1, "Peasant", 1, 1, None, 1),
                        Creature(1, "Peasant", 1, 1, None, 2)]
        player1.turn = 1
        player1.mana = 100
        player2 = Player("Andras")
        player2.hand = [Creature(1, "Peasant", 1, 1, None, 3),
                        Creature(1, "Knight", 3, 3, None, 4)]
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
        if player1.put_card_on_field(card_picked) == 0:
            player1.problem = "Not enough mana"
    else:
        card_picked = request.form
        if player2.put_card_on_field(card_picked) == 0:
            player2.problem = "No enough mana"
    return redirect(url_for('show_battle', players=[player2, player1], attacking_card=None))


@app.route("/battlefield_action", methods=["POST"])
def battlefield_fight():
    card_picked = request.form
    global current_card
    global player2
    global player1
    if player1.turn == 1:
        current_card = battle_logic(player1, card_picked)
    elif attacked_player == 2:
        card = damage_dealing(player2, card_picked)
        if card is not None:
            battle(current_card, card, player1, player2)
        elif card_picked.get(player2.name) is not None:
            current_card.exhausted = True
            player2, current_card = damage_to_player(player2, current_card)
            player1.turn = 1
            if player2.check_player() == 0:
                return render_template("END.html", player=player2)
    if player2.turn == 1:
        current_card = battle_logic(player2, card_picked)
    elif attacked_player == 1:
        card = damage_dealing(player1, card_picked)
        if card is not None:
            battle(current_card, card, player2, player1)
            player2.turn = 1
        elif card_picked.get(player1.name) is not None:
            player1, current_card = damage_to_player(player1, current_card)
            player2.turn = 1
            if player1.check_player() == 0:
                return render_template("END.html", player=player1)
    return redirect(url_for('show_battle', players=[player2, player1]))


@app.route("/end_turn", methods=["POST"])
def end_turn():
    global attacked_player
    attacked_player = turn_switch(player1, player2)
    return redirect(url_for('show_battle', players=[player2, player1]))


if __name__ == '__main__':
    app.run(debug=True)
