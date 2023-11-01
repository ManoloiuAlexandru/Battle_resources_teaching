from clases.creatures import Creature
from clases.game_logics import battle, damage_to_player
from clases.player import Player

from resource_game.clases.creatures import list_of_creature_that_deal_dmg_to_enemies
from resource_game.clases.spells import list_of_self_target


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)

    def play_hand(self, player):
        for card in self.hand[:]:
            if card.mana_cost <= self.mana:
                self.check_summed_card(card, player)
                if card.card_type == "Creature":
                    self.battle_field.append(card)
                self.hand.remove(card)
                self.mana_increase(-card.mana_cost)

    def check_summed_card(self, card, player):
        if card.card_type == "Creature":
            target_creature = Creature(1, 'DEMO', 0, 0, "", 999)
            if card.name in list_of_creature_that_deal_dmg_to_enemies:
                for creature in player.battle_field:
                    if target_creature.hp <= creature.hp <= list_of_creature_that_deal_dmg_to_enemies.get(card.name):
                        target_creature = creature
                self.dmg_to_player_creature(target_creature, player,
                                            list_of_creature_that_deal_dmg_to_enemies.get(card.name))
        elif card.card_type == "Spell":
            if card.name in list_of_self_target:
                if card.name == "Personal Guard":
                    max_hp_creature = max(self.battle_field, key=lambda x: x.hp and "Guard" not in card.description.split())
                    max_hp_creature.description += " Guard"

    def dmg_to_player_creature(self, target_card, player, dmg):
        for card in player.battle_field:
            if card == target_card:
                card.hp -= dmg
        player.check_battlefield()

    def check_move(self, player):
        you_can_do = 1
        while you_can_do == 1:
            you_can_do = 0
            for card in self.battle_field[:]:
                if card.exhausted is not True:
                    you_can_do = 1
                    self.target_priority(card, player)
        return you_can_do

    def attack_creature(self, card, player):
        min_hp_creature = min(player.battle_field, key=lambda x: x.hp)
        battle(card, min_hp_creature, self, player)

    def attack_player(self, card, player):
        damage_to_player(player, card)

    def target_priority(self, card, player):
        if self.check_for_guards(player) == 1:
            target_creature = Creature(1, 'DEMO', 99, 99, "", 999)
            for creature in player.battle_field:
                if creature.description == "Guard" and target_creature.hp >= creature.hp:
                    target_creature = creature
            battle(card, target_creature, self, player)
        else:
            if len(player.battle_field) == 0:
                self.attack_player(card, player)
            for creature in player.battle_field:
                if creature.hp <= card.attack <= creature.attack:
                    self.attack_creature(card, player)
                    break
                else:
                    self.attack_player(card, player)
                    break

    def check_for_guards(self, player):
        for creature in player.battle_field:
            if creature.description == "Guard":
                return 1
        return 0
