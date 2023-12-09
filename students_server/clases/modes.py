import copy
import random

from decks.lists_of_cards import generate_random_int


def modes_alteration(mode, player, bot, dict_of_decks):
    if mode == "i_hate_myself":
        return i_hate_myself(player)
    if mode == "that_is_not_what_i_payed_for":
        return that_is_not_what_i_pay_for(player, bot, dict_of_decks)
    if mode == "personal_troops":
        return personal_troops(player, bot, dict_of_decks)


def i_hate_myself(player):
    bot_deck = []
    for card in player.deck:
        bot_card = copy.deepcopy(card)
        bot_card.id = generate_random_int()
        bot_card.card_id = str(bot_card.id)
        if len(bot_card.name.split(" ")) >= 2:
            bot_card.name_for_html = "_".join(bot_card.name.split()) + bot_card.card_id
        else:
            bot_card.name_for_html = bot_card.name + bot_card.card_id
        bot_deck.append(bot_card)
    return bot_deck


def that_is_not_what_i_pay_for(player, bot, dict_of_decks):
    for card in player.deck:
        card.mana_cost = random.randrange(0, 11)
        card.original_mana_cost = card.mana_cost

    deck_for_bot = dict_of_decks.get(bot.playing_deck_name)
    for card in deck_for_bot:
        card.mana_cost = random.randrange(0, 11)
        card.original_mana_cost = card.mana_cost
    return deck_for_bot


def personal_troops(player, bot, dict_of_decks):
    for card in player.deck:
        card.mana_cost = card.attack
        card.original_mana_cost = card.mana_cost

    deck_for_bot = dict_of_decks.get(bot.playing_deck_name)
    for card in deck_for_bot:
        card.mana_cost = card.attack
        card.original_mana_cost = card.mana_cost
    return deck_for_bot
