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
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.card_id
        else:
            self.name_for_html = self.name + self.card_id

    def __str__(self):
        return f"MANA:{self.mana_cost} {self.name} HP:{self.hp} ATTACK:{self.attack} {self.description} "

    def charge_check(self):
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
        if buff_attr == "Armored":
            self.armored = self.check_armored()
        if buff_attr == "Charge" and self.number_of_attacks >= 1:
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
            if creature.name in effects:
                nr_buff += 1
        while len(self.active_effects) < nr_buff:
            for buffing_creature in player.ongoing_effects:
                if buffing_creature.name not in self.active_effects:
                    self.attack_before_on_effects = self.attack
                    self.hp_before_on_effects = self.hp
                    self.active_effects.append(buffing_creature.name)
                    self.attack += effects.get(buffing_creature.name)[1]
                    self.hp += effects.get(buffing_creature.name)[0]
                elif buffing_creature.name in self.active_effects:
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
