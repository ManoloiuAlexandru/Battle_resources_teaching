import copy

from decks.lists_of_cards import generate_random_int


def modes_alteration(mode, player, bot):
    if mode == "i_hate_myself":
        return i_hate_myself(player)


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
