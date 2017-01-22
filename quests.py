class QuestTracker(object):

    def __init__(self):
        self.quests = {
            'talk to the mayor': False,
            'kill the goblin': False
        }

    # sets a quest to true
    def set_completed(self, quest_name):
        self._check_quest_name(quest_name)
        self.quests[quest_name] = True

    # checks if the quest has been completed. It will return a boolean
    def is_completed(self, quest_name):
        self._check_quest_name(quest_name)
        return self.quests[quest_name]

    # checks if the quest name that is being passed into the QuestTracker
    # is available in the dictionary of quests
    def _check_quest_name(self, quest_name):
        if not quest_name in self.quests.keys():
            raise KeyError
