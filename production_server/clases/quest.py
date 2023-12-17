from decks.lists_of_cards import list_of_quests


class Quest:
    def __init__(self, mana_cost, name, description, id):
        self.card_id = str(id)
        self.mana_cost = mana_cost
        self.original_mana_cost = mana_cost
        self.name = name
        self.card_type = "Quest"
        self.description = description
        self.img_url = self.name + ".png"
        self.empire_belonging = ""
        self.category = ""
        self.progress = 0
        self.nr_turns = 0
        self.reward = None
        if len(self.name.split(" ")) >= 2:
            self.name_for_html = "_".join(self.name.split()) + self.card_id
        else:
            self.name_for_html = self.name + self.card_id

    def __str__(self):
        return f"MANA:{self.mana_cost} NAME:{self.name} {self.description}"

    def build_criteria(self):
        for key in list_of_quests[self.name]:
            self.nr_turns = int(key.split(":")[4])
            self.reward = list_of_quests[self.name][key]

    def check_quest_progression(self, player, card, action):
        if self.name == "We don't take it personally":
            if (player.dict_of_actions["Damage_taken"] == 0 and player.dict_of_actions["Damage_done"] == 0
                    and action == "end_turn"):
                self.progress += 1
        elif self.name == "Get back to work":
            max_damage_taken = 0
            for creature in player.battle_field:
                if creature.damage_taken_this_turn_from_empire > max_damage_taken and creature.hp > 0:
                    max_damage_taken = creature.damage_taken_this_turn_from_empire
            if max_damage_taken > self.progress:
                self.progress = max_damage_taken
            if action == "end_turn":
                self.progress = 0
        elif self.name == "Imperial Drama":
            nr_dead_minions = 0
            for creature in player.battle_field:
                if creature.hp <= 0:
                    nr_dead_minions += 1
            for creature in player.enemy_player.battle_field:
                if creature.hp <= 0:
                    nr_dead_minions = 0
            self.progress = nr_dead_minions
            if action == "end_turn":
                self.progress = 0
        if self.nr_turns <= self.progress:
            if self.name == "We don't take it personally" or self.name == "Get back to work" or self.name == "Imperial Drama":
                for key in self.reward:
                    for i in range(key):
                        if len(player.hand) < 10:
                            player.hand.append(self.reward[key])
            player.quest = None
