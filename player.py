from weapons import Hands
from armor import Clothes
from quests import QuestTracker

class Player(object):
    starting_health = 20

    def __init__(self):
        self.health = self.starting_health
        self.weapon = Hands()
        self.armor = Clothes()
        self.quest_tracker = QuestTracker()
        self.inventory = {
            'goblin head': False
        }
        self.gold = 0

    def reset_health(self):
        self.health = self.starting_health

    def add_gold(self, gold_gained):
        self.gold += gold_gained

    def subtract_gold(self, gold_removed):
        self.gold -= gold_removed
