class Player(object):
    starting_health = 20

    def __init__(self, my_weapon, my_armor, quests):
        self.my_health = self.starting_health
        self.my_weapon = my_weapon
        self.my_armor = my_armor
        self.quests = quests

    def reset_health(self):
        self.my_health = self.starting_health
