from ITschool_projects.battle_resources.clases.creatures import Creature
from ITschool_projects.battle_resources.clases.game_logics import battle, damage_to_player
from ITschool_projects.battle_resources.clases.player import Player


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)

    def play_hand(self):
        for card in self.hand[:]:
            if card.mana_cost <= self.mana:
                self.battle_field.append(card)
                self.hand.remove(card)
                self.mana_increase(-card.mana_cost)

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
