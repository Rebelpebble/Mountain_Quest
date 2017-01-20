class Player(object):
    starting_health = 20

    def __init__(self, weapon, armor):
        self.health = self.starting_health
        self.weapon = weapon
        self.armor = armor
        self.quests = self.generate_quests()
        self.inventory = {'goblin head': False}
        self.gold = 0

    def reset_health(self):
        self.health = self.starting_health

    def add_gold(self, gold_gained):
        self.gold += gold_gained

    def subtract_gold(self, gold_removed):
        self.gold += gold_removed

    @staticmethod
    def generate_quests():
        quests = {}
        for x in range(0, 11):
            quests[x] = False
        return quests
