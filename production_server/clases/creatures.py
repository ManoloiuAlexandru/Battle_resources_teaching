class Creature:
    def __init__(self, mana_cost, name, hp, attack, description, category, id):
        self.card_id = str(id)
        self.mana_cost = mana_cost
        self.original_mana_cost = mana_cost
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.original_hp = hp
        self.attack = attack
        self.category = category
        self.attack_before_on_effects = 0
        self.hp_before_on_effects = 0
        self.original_attack = attack
        self.active_effects = []
        self.knocked_down_time = 0
        self.description = description
        self.original_description = description
        self.card_type = "Creature"
        self.exhausted = self.charge_check()
        self.armored = self.check_armored()
        self.can_be_target = True
        self.img_url = self.name + ".png"
        self.items = []
        self.number_of_attacks = 1
        self.empire_belonging = ""
        self.damage_taken_this_turn_from_empire = 0
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.card_id
        else:
            self.name_for_html = self.name + self.card_id

    def __str__(self):
        return f"MANA:{self.mana_cost} {self.name} HP:{self.hp} ATTACK:{self.attack} {self.description} "

    def charge_check(self):
        if self.knocked_down_time > 0:
            return True
        if "Can't attack" in self.description:
            return True
        if "Charge" in self.description.split():
            return False
        return True

    def check_creature(self, buff_attr):
        if self.mana_cost < 0:
            self.mana_cost = 0
        elif self.mana_cost >= 10:
            self.mana_cost = 10
        if self.attack < 0:
            self.attack = 0
        if self.hp <= 0:
            self.hp = 1
        if "Armored" in buff_attr.split():
            self.armored = self.check_armored()
        if "Charge" in buff_attr.split() and self.number_of_attacks >= 1:
            self.exhausted = self.charge_check()
        # if buff_attr == "":
        #     self.armored = self.check_armored()
        #     self.exhausted = self.charge_check()

    def negative_effects_from_creatures(self, card, effects, player):
        nr_buff = 0
        for creature in player.ongoing_effects:
            if creature.name == card.name:
                nr_buff += 1
        while len(self.active_effects) < nr_buff:
            self.active_effects.append(card.name)
            if self.attack >= effects[1]:
                self.attack -= effects[1]
            else:
                self.attack_before_on_effects -= effects[1]
                self.attack = 0
            if self.hp >= effects[0]:
                self.hp -= effects[0]
            else:
                self.hp_before_on_effects -= effects[1]
                self.hp = 0

    def positive_effects_from_creatures(self, card, effects, player):
        nr_buff = 0
        for creature in player.ongoing_effects:
            if creature.name in effects and creature.original_description in creature.description.split("  "):
                nr_buff += 1
        while len(self.active_effects) < nr_buff:
            for buffing_creature in player.ongoing_effects:
                if buffing_creature.name not in self.active_effects and effects.get(buffing_creature.name)[2] == "":
                    self.attack_before_on_effects = self.attack
                    self.hp_before_on_effects = self.hp
                    self.active_effects.append(buffing_creature.name)
                    self.attack += effects.get(buffing_creature.name)[1]
                    self.hp += effects.get(buffing_creature.name)[0]

                elif buffing_creature.name not in self.active_effects and self.category == \
                        effects.get(buffing_creature.name)[2]:
                    self.attack_before_on_effects = self.attack
                    self.hp_before_on_effects = self.hp
                    self.active_effects.append(buffing_creature.name)
                    self.attack += effects.get(buffing_creature.name)[1]
                    self.hp += effects.get(buffing_creature.name)[0]
                else:
                    nr_buff -= 1

    def reverse_effect_creature(self, card, effects, effect, player):
        try:
            nr_buff = 0
            for creature in player.ongoing_effects:
                if creature.name in effects:
                    nr_buff += 1
            while len(self.active_effects) > nr_buff:
                for buffing_creature in self.active_effects[:]:
                    on_field = 0
                    for ongoing_effect in player.ongoing_effects:
                        if buffing_creature == ongoing_effect.name:
                            on_field = 1
                    if on_field == 0:
                        self.attack += effect * effects.get(buffing_creature)[1]
                        if self.attack < 0:
                            self.attack = 0
                        self.hp += effect * effects.get(buffing_creature)[0]
                        self.hp_before_on_effects += effect * effects.get(buffing_creature)[0]
                        if self.hp < 0:
                            self.hp = 0
                        self.active_effects.remove(card.name)
        except Exception as e:
            print("Error in reverse_effect_creature")
            print(e)

    def check_armored(self):
        if "Armored" in self.description.split():
            return True
        return False

    def mana_cost_reduction(self, amount):
        if self.mana_cost - amount < 0:
            self.mana_cost = 0
        else:
            self.mana_cost -= amount

    def check_creature_for_dmg(self, effect_to_look):
        if effect_to_look == "Armored":
            if self.armored is True:
                return False
        return True

    def check_specific_attr(self, attr, player, enemy_player):
        if attr in self.description.split():
            return True
        elif attr == self.category:
            return True
        elif attr == self.card_type:
            return True
        else:
            if "summ" in attr.split():
                if "hp" in attr.split():
                    if self.hp <= int(attr.split()[1]):
                        return True
        return False

    def debuff_creature(self, debuffing_effect, player, enemy_player):
        if debuffing_effect[0] == 0:
            if self.hp > self.original_hp:
                self.hp = self.original_hp
        elif debuffing_effect[0] == -1:
            self.hp = self.hp
        else:
            self.hp = debuffing_effect[0]
        if debuffing_effect[1] == 0:
            self.attack = self.original_attack
        elif debuffing_effect[1] == -1:
            self.attack = self.attack
        else:
            self.attack = debuffing_effect[1]
        if debuffing_effect[2] == "":
            self.description = ""
            self.armored = False
            self.active_effects.clear()
        else:
            self.description += " " + debuffing_effect[2]

    def reset(self):
        self.mana_cost = self.original_mana_cost
        self.hp = self.original_hp
        self.attack = self.original_attack
        self.description = self.original_description
