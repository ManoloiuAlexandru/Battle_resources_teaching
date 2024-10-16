from flask import Flask, render_template, request, redirect, url_for

from clases.modes import modes_alteration
from decks.roman_empire import *
from decks.all_cards_in_the_game import all_cards_in_game, cards_that_are_in_the_game_for_all
from decks.holy_roman_empire import *
from decks.mesopotamia_empire import *
from decks.mongols_empire import *
from decks.byzantine_empire import *
from decks.greek_empire import *
from clases.server_logics import *
from clases.Defence import Defence
from clases.spells import Spell
from clases.creatures import Creature
from clases.bot import Bot
from clases.game_logics import *
from clases.player import Player
from decks.decks_to_play import *

app = Flask(__name__)
global player1
global player2
global current_card
global attacked_player
global your_deck
global index
global show_deck
global empire
global mode


def game_difficulty(player1_name, player2_name, play1_deck, player2_deck, difficulty, player1_empire, player2_empire):
    global player1
    global player2
    global attacked_player
    global your_deck
    global mode
    try:
        if player1 is None:
            player1 = Player(player1_name)
    except Exception as e:
        player1 = Player(player1_name)
    player1.empire = " ".join(player1_empire.split("_"))
    player1.hand = []
    player1.playing_deck_name = play1_deck
    if play1_deck == "personal_deck":
        try:
            if len(your_deck) == 0:
                your_deck = get_old_deck()[0]
        except Exception as e:
            player1.make_deck(get_old_deck()[0])
        player1.make_deck(your_deck)
    else:
        player1.make_deck(dict_of_decks.get(play1_deck))
    if player2_name == "Bot":
        player2 = Bot("Bot")
        player2.difficulty = difficulty
    else:
        player2 = Player("Andras")
    player2.empire = " ".join(player2_empire.split("_"))
    player2.hand = []
    player2.playing_deck_name = player2_deck
    try:
        if mode:
            player2.make_deck(modes_alteration(mode, player1, player2, dict_of_decks))
        else:
            player2.make_deck(dict_of_decks.get(player2_deck))
            modes_alteration(mode, player1, player2, dict_of_decks)
    except Exception as e:
        mode = ""
        print(e)
        player2.make_deck(dict_of_decks.get(player2_deck))
        modes_alteration(mode, player1, player2, dict_of_decks)
    if difficulty == "easy" and player1.mana == 0:
        attacked_player = 2
        player1.turn = 1
        player1.mana = 1
        player1.hp = 9999
        player2.hp = 30
        player2.mana = 1
    if difficulty == "normal" and player1.mana == 0:
        attacked_player = 2
        player1.turn = 1
        player1.mana = 1
        player2.mana = 1
    if difficulty == "hard" and player1.mana == 0:
        attacked_player = 2
        player1.turn = 1
        player1.mana = 1
        player2.mana = 1
        for card in player2.deck:
            card.mana_cost -= 1
            if card.mana_cost < 0:
                card.mana_cost = 0
    if difficulty == "insane" and player1.mana == 0:
        player1.hp = 30
        attacked_player = 2
        player1.turn = 1
        player1.mana = 1
        player2.mana = 1
        for card in player2.deck:
            card.mana_cost -= 1
            if card.mana_cost < 0:
                card.mana_cost = 0
            if card.card_type == "Creature":
                card.attack += 1
                card.hp += 1
                card.check_creature("")
    player1.start_game()
    player2.start_game()
    player1.enemy_player = player2
    player2.enemy_player = player1
    return player1, player2


def game_start(player1_name, player2_name, play1_deck, player2_deck, difficulty, player1_empire, player2_empire):
    global player1
    global player2
    try:
        if player1 is None:
            player1, player2 = game_difficulty(player1_name, player2_name, play1_deck, player2_deck, difficulty,
                                               player1_empire, player2_empire)
    except Exception as e:
        player1, player2 = game_difficulty(player1_name, player2_name, play1_deck, player2_deck, difficulty,
                                           player1_empire, player2_empire)


@app.route("/")
def game_options():
    global index
    index = 0
    global your_deck
    try:
        if your_deck is None:
            your_deck = []
    except Exception as e:
        your_deck = []
    global show_deck
    show_deck = {}
    return render_template("game_option.html")


@app.route("/reset", methods=["POST", "GET"])
def reset():
    global player1
    global player2
    game_difficulty(player1.name, player2.name, player1.playing_deck_name, player2.playing_deck_name,
                    player2.difficulty, player1.empire, player2.empire)
    return redirect(url_for('show_battle', players=[player2, player1], attacking_card=None))


@app.route("/rules")
def rules():
    return render_template("Rules.html")


@app.route("/make_your_own_deck", methods=["POST", "GET"])
def make_your_own_deck():
    global show_deck
    try:
        return render_template("make_your_deck.html", your_deck=show_deck,
                               library=empire_decks[empire])
    except Exception as e:
        show_deck = {}
        return render_template("make_your_deck.html", your_deck=show_deck,
                               library=cards_that_are_in_the_game_for_all)


@app.route("/make_your_own_deck_pick_empire", methods=["POST", "GET"])
def make_your_own_deck_pick_empire():
    return render_template("empires_choice.html",
                           library=[cards_byzantine_show, cards_holy_show, cards_for_mongol, mesopotamia_show,
                                    roman_empire_show, cards_greek_show])


@app.route("/update_deck", methods=["POST", "GET"])
def update_deck():
    global your_deck
    global empire
    global show_deck
    try:
        your_deck = get_old_deck()[0]
        empire = get_old_deck()[1]
        show_deck = make_html_deck(your_deck, show_deck)
        return render_template("update_deck.html", your_deck=show_deck, library=empire_decks[empire])
    except Exception as e:
        return render_template("game_option.html")


@app.route("/chaotic_history", methods=["POST", "GET"])
def chaotic_history():
    global show_deck
    global mode
    mode = "chaotic_history"
    return render_template("chaotic_history.html", your_deck=show_deck,
                           library=all_cards_in_game)


@app.route("/i_hate_myself", methods=["POST", "GET"])
def i_hate_myself():
    global show_deck
    global mode
    mode = "i_hate_myself"
    return redirect(url_for('make_your_own_deck_pick_empire'))


@app.route("/there_can_be_only_one", methods=["POST", "GET"])
def there_can_be_only_one():
    global show_deck
    global mode
    mode = "there_can_be_only_one"
    return redirect(url_for('make_your_own_deck_pick_empire'))


@app.route("/that_is_not_what_i_payed_for", methods=["POST", "GET"])
def that_is_not_what_i_payed_for():
    global show_deck
    global mode
    mode = "that_is_not_what_i_payed_for"
    return redirect(url_for('make_your_own_deck_pick_empire'))


@app.route("/personal_troops", methods=["POST", "GET"])
def personal_troops():
    global show_deck
    global mode
    mode = "personal_troops"
    return redirect(url_for('make_your_own_deck_pick_empire'))


@app.route("/send_empire", methods=["POST", "GET"])
def send_empire():
    global empire
    empire = request.form.get("your_empire")
    return redirect(url_for('make_your_own_deck', empire=empire))


@app.route("/deck_cards", methods=["POST", "GET"])
def make_deck():
    global your_deck
    global show_deck
    global index
    global empire
    global mode
    try:
        if empire == "":
            deck_to_pick = all_cards_in_game
        elif empire == "Byzantine_Empire":
            deck_to_pick = cards_for_byzantine_empire
        elif empire == "Holy_Roman_Empire":
            deck_to_pick = cards_for_holy_roman_empire
        elif empire == "Mongol_Empire":
            deck_to_pick = cards_for_mongol_empire
        elif empire == "Mesopotamia_Empire":
            deck_to_pick = mesopotamia_empire
        elif empire == "Roman_Empire":
            deck_to_pick = roman_empire
        elif empire == "Greek_Empire":
            deck_to_pick = cards_for_greek_empire
        else:
            deck_to_pick = cards_that_are_in_the_game_for_all
    except Exception as e:
        empire = ""
        deck_to_pick = all_cards_in_game
    try:
        if mode:
            pass
    except Exception as e:
        mode = ""
    cards_name = request.form
    for card in deck_to_pick:
        if cards_name.get(card.name_for_html) is not None and check_if_card_in_deck(card, your_deck, mode) < 2 and len(
                your_deck) < 30:
            if card.card_type == "Creature":
                your_deck.append(
                    Creature(card.mana_cost, card.name, card.hp, card.attack, card.description, card.category, index))
                index += 1
            if card.card_type == "Spell":
                your_deck.append(Spell(card.mana_cost, card.name, card.description, index))
                index += 1
            if card.card_type == "Defence":
                your_deck.append(
                    Defence(card.mana_cost, card.name, card.number_of_troops, card.nr_of_assaults, card.description,
                            index))
                index += 1
    show_deck = make_html_deck(your_deck, show_deck)
    if empire == "":
        return redirect(url_for('chaotic_history', show_deck=show_deck))
    else:
        return redirect(url_for('make_your_own_deck', show_deck=show_deck))


@app.route("/play", methods=["POST", "GET"])
def show_battle():
    global player1
    global player2
    player1_empire = request.form.get("your_empire")
    player2_empire = request.form.get("enemy_empire")
    player1_name = request.form.get("player1")
    player2_name = request.form.get("player2")
    player1_deck = request.form.get("deck_player1")
    player2_deck = request.form.get("deck_player2")
    difficulty = request.form.get("difficulty")
    game_start(player1_name, player2_name, player1_deck, player2_deck, difficulty, player1_empire, player2_empire)
    player1.card_in_hand_effect()
    player2.card_in_hand_effect()
    Player.battle_fields_effects(player1, player2)
    return render_template("home.html", players=[player2, player1])


@app.route("/send_deck", methods=["POST", "GET"])
def personal_deck():
    save_your_deck(your_deck, empire)
    try:
        if mode != "":
            return redirect(url_for('modes'))
    except Exception as e:
        print(e)
    return redirect(url_for('game_options'))


@app.route("/modes", methods=["POST", "GET"])
def modes():
    global index
    index = 0
    global your_deck
    try:
        if your_deck is None:
            your_deck = []
    except Exception as e:
        your_deck = []
    global show_deck
    show_deck = {}
    return render_template("Modes.html")


@app.route("/remove_card", methods=["POST", "GET"])
def remove_card_from_deck():
    global show_deck
    cards_name = request.form
    for card in your_deck[:]:
        if cards_name.get("_".join(card.name.split())) is not None:
            your_deck.remove(card)
            if show_deck[card.name][1] == 2:
                show_deck[card.name][1] -= 1
                break
            else:
                show_deck.pop(card.name)
    show_deck = make_html_deck(your_deck, show_deck)
    if empire != "":
        return redirect(url_for('make_your_own_deck', show_deck=show_deck))
    else:
        return redirect(url_for('chaotic_history', show_deck=show_deck))


@app.route("/library")
def show_library():
    return render_template("library.html", library=all_cards_in_game)


@app.route("/update_battle_field", methods=["POST", "GET"])
def update_battle():
    global player1
    global player2
    if attacked_player == 2:
        card_picked = request.form
        if player1.put_card_on_field(card_picked) != 0:
            Player.battle_fields_effects(player1, player2)
            return redirect(url_for('battlefield_fight'))
        elif player1.put_card_on_field(card_picked) == 0:
            if len(player1.battle_field) == 7:
                player1.problem = "You don't have enough space"
            else:
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
    if card_picked.get("hero_power") is not None:
        check_hero_power(player1, player2)
    if player1.power is not None:
        destroy_creature_from_player(player1, player2, card_picked)
    Player.battle_fields_effects(player1, player2)
    if player1.incoming_action == 2:
        destroy_creature_from_player(player1, player2, card_picked)
    if player1.incoming_action == 3:
        cast_spell_from_player(player1, player2, card_picked)
    if player1.incoming_action == 4:
        put_item_on(player1, player2, card_picked)
    if player2.incoming_action == 4:
        put_item_on(player2, player1, card_picked)
    if player2.incoming_action == 3:
        cast_spell_from_player(player2, player1, card_picked)
    if player2.incoming_action == 2:
        destroy_creature_from_player(player2, player1, card_picked)
    if player1.turn == 1:
        current_card = battle_logic(player1, card_picked)
    elif attacked_player == 2:
        card = damage_dealing(player2, card_picked)
        if card is not None and "Rush" in current_card.description.split() and guard_checking(player2, card) == 1:
            if current_card.number_of_attacks >= 1:
                battle(current_card, card, player1, player2)
            player1.turn = 1
            current_card = None
        elif (card is not None or card_picked.get(player2.name) is not None) and current_card.exhausted is True:
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
        Player.battle_fields_effects(player1, player2)
        if player2.check_move(player1) == 0:
            attacked_player = turn_switch(player1, player2)
        Player.clean_board(player1, player2)
        if player1.check_player() == 0:
            return render_template("END.html", player=player1)
        elif player2.check_player() == 0:
            return render_template("END.html", player=player2)
    return redirect(url_for('show_battle', players=[player2, player1]))


if __name__ == '__main__':
    app.run()
