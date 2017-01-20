class Player(object):
    starting_health = 20

    def __init__(self, weapon, armor, quests, inventory, gold):
        self.health = self.starting_health
        self.weapon = my_weapon
        self.armor = my_armor
        self.quests = quests
        self.inventory = inventory
        self.gold = gold

    def reset_health(self):
        self.my_health = self.starting_health

    def add_gold(self, gold_gained):
        self.gold += gold_gained

    def subtract_gold(self, gold_removed):
        self.gold += gold_removed
