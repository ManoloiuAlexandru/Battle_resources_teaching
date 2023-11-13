from clases.creatures import *
from clases.game_logics import battle, damage_to_player
from clases.player import Player

from clases.spells import *

from clases.Item import *

from clases.game_logics import *


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)
        self.difficulty = ""

    def play_hand(self, player):
        for card in self.hand[:]:
            if card.name in list_of_self_target:
                aux_card = self.hand[-1]
                self.hand[-1] = self.hand[self.hand.index(card)]
                self.hand[self.hand.index(card)] = aux_card
            if card.mana_cost <= self.mana and len(self.battle_field) < 7:
                if self.check_summed_card(card, player) == 1:
                    self.logs += "Playing:" + card.name + "\n"
                    if card.card_type == "Creature":
                        self.battle_field.append(card)
                    self.hand.remove(card)
                    self.mana_increase(-card.mana_cost)
                    Player.battle_fields_effects(self, player)

    def check_summed_card(self, card, player):
        if card.card_type == "Creature":
            target_creature = Creature(1, 'DEMO', 0, 0, "", 999)
            if card.name in list_of_creature_that_deal_dmg_to_enemies:
                for creature in player.battle_field:
                    if target_creature.hp <= creature.hp <= list_of_creature_that_deal_dmg_to_enemies.get(card.name):
                        target_creature = creature
                self.dmg_to_player_creature(target_creature, player,
                                            list_of_creature_that_deal_dmg_to_enemies.get(card.name))
            elif card.name in list_of_creature_that_heal:
                try:
                    for creature in self.battle_field:
                        if creature.hp < creature.max_hp:
                            if creature.hp + list_of_creature_that_heal.get(card.name) > card.max_hp:
                                creature.hp = card.max_hp
                                self.logs += "Playing:" + creature.name + "\n"
                                break
                            else:
                                creature.hp += list_of_creature_that_heal.get(card.name)
                                self.logs += "Playing:" + creature.name + "\n"
                                break
                    check_for_creature_with_effect_on(self)
                except Exception as e:
                    print(e)
            if card.name in list_of_creature_that_buff:
                try:
                    for creature in self.battle_field:
                        creature.hp += list_of_creature_that_buff.get(card.name)[0]
                        creature.attack += list_of_creature_that_buff.get(card.name)[1]
                        creature.description += " " + list_of_creature_that_buff.get(card.name)[2]
                        break
                except Exception as e:
                    print(e)
            elif card.name in list_of_creature_that_draw_cards:
                for nr_cards in range(list_of_creature_that_draw_cards.get(card.name)):
                    self.draw_card()
            elif card.name in list_of_creature_that_add_mana:
                self.mana_increase(list_of_creature_that_add_mana.get(card.name))
                if self.empty_mana + list_of_creature_that_add_mana.get(card.name) > 10:
                    self.empty_mana = 10
                else:
                    self.empty_mana += list_of_creature_that_add_mana.get(card.name)
            elif card.name in list_of_creature_with_on_going_effect:
                self.ongoing_effects.append(card)
        elif card.card_type == "Spell":
            if card.name in list_of_self_target and len(self.battle_field) > 0:
                try:
                    if card.name == "Personal Guard":
                        self.battle_field.sort(key=lambda x: x.max_hp)
                        for creature in self.battle_field[::-1]:
                            if "Guard" not in creature.description:
                                creature.description += " Guard"
                                self.logs += " on this card:" + creature.name + "\n"
                                self.draw_card()
                                break
                    if card.name == "Horse riding lessons":
                        self.battle_field.sort(key=lambda x: x.attack)
                        for creature in self.battle_field[::-1]:
                            if "Charge" not in creature.description:
                                creature.description += " Charge"
                                creature.exhausted = False
                                self.logs += " on this card:" + creature.name + "\n"
                                break
                    elif card.name in list_of_healing_spells:
                        self.battle_field.sort(key=lambda x: x.max_hp - x.hp)
                        for creature in self.battle_field:
                            if creature.hp + list_of_healing_spells.get(card.name) > creature.max_hp > creature.hp:
                                creature.hp = creature.max_hp
                                self.logs += " on this card:" + creature.name + "\n"
                                return 1
                            elif creature.hp < creature.max_hp:
                                creature.hp += list_of_healing_spells.get(card.name)
                                self.logs += " on this card:" + creature.name + "\n"
                                return 1
                        return 0
                except Exception as e:
                    print(e)
            elif card.name == "Bodyguards":
                for i in range(0, 2):
                    for card in self.deck:
                        if "Guard" in card.description.split() and card.card_type == "Creature":
                            self.battle_field.append(card)
                            self.deck.remove(card)
                            break
            elif card.name == "Feudal Obligations":
                for nr_cards in range(list_of_spells_that_draw_cards.get(card.name)):
                    self.draw_card()
            elif card.name in list_of_enemy_target or card.name in list_of_dmg_spells:
                self.target_creature_with_spell(card, player)
            else:
                return 0
        elif card.card_type == "Item":
            if card.name in list_of_good_items and len(self.battle_field) > 0:
                try:
                    target_creature = Creature(1, 'DEMO', 0, 0, "", 0)
                    for creature in self.battle_field:
                        if creature.hp > target_creature.hp:
                            target_creature = creature
                    if card.name in list_of_items_that_draw_cards:
                        for i in range(0, list_of_items_that_draw_cards.get(card.name)):
                            self.draw_card()
                    target_creature.items.append(card)
                    card.status_update(target_creature)
                except Exception as e:
                    print(e)
                    return 0
            else:
                return 0
        return 1

    def dmg_to_player_creature(self, target_card, player, dmg):
        for card in player.battle_field:
            if card == target_card:
                card.hp -= dmg
                self.logs += " on this card:" + card.name
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

    def target_creature_with_spell(self, card, player):
        if self.check_for_guards(player) == 1:
            target_creature = Creature(1, 'DEMO', 999, 999, "", 999)
            for creature in player.battle_field:
                if "Guard" in creature.description and target_creature.hp >= creature.hp:
                    target_creature = creature
            if card.name == "Kill":
                for creature in player.battle_field:
                    if creature == target_creature:
                        creature.hp -= 999
                        self.logs += " on this card:" + creature.name + "\n"
            elif card.name == "Arrow shot":
                for creature in player.battle_field:
                    if creature == target_creature:
                        creature.hp -= 1
                        self.logs += " on this card:" + creature.name + "\n"
            else:
                if "ALL" in card.description:
                    for creature in player.battle_field:
                        creature.hp -= list_of_dmg_spells.get(card.name)
                    for creature in self.battle_field:
                        creature.hp -= list_of_dmg_spells.get(card.name)
                else:
                    for creature in player.battle_field:
                        creature.hp -= list_of_dmg_spells.get(card.name)
        else:
            target_creature = Creature(1, 'DEMO', 999, 999, "", 999)
            for creature in player.battle_field:
                if target_creature.attack >= creature.attack:
                    target_creature = creature
            if card.name == "Kill":
                for creature in player.battle_field:
                    if creature == target_creature:
                        creature.hp -= 99
                        self.logs += " on this card:" + creature.name + "\n"
            elif card.name == "Arrow shot":
                for creature in player.battle_field:
                    if creature == target_creature:
                        creature.hp -= 1
                        self.logs += " on this card:" + creature.name + "\n"
            else:
                if "ALL" in card.description:
                    for creature in player.battle_field:
                        creature.hp -= list_of_dmg_spells.get(card.name)
                    for creature in self.battle_field:
                        creature.hp -= list_of_dmg_spells.get(card.name)
                else:
                    for creature in player.battle_field:
                        creature.hp -= list_of_dmg_spells.get(card.name)

    def target_priority(self, card, player):
        if self.check_for_guards(player) == 1:
            target_creature = Creature(1, 'DEMO', 999, 999, "", 999)
            for creature in player.battle_field:
                if "Guard" in creature.description and target_creature.hp >= creature.hp:
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
            if "Guard" in creature.description.split():
                return 1
        return 0
