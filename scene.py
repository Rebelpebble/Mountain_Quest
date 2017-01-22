import os

class SceneChoice(object):
    def __init__(self, description, next_scene_name):
        self.description = description
        self.next_scene_name = next_scene_name

class Scene(object):
    def __init__(self, name, setting_description, choices):
        self.name = name
        self.setting_description = setting_description
        self.choices = choices

    def enter(self, player):
        os.system('clear')

        print self.setting_description

        selected_choices = self._prompt_choice()

        if selected_choices:
            return selected_choices.next_scene_name
        else:
            return self.name

        def _prompt_choice(self):
            for i, choice in enumerate(self.choices):
                print "(" + str(i + 1) + ") " + choice.description

            entered_choice = raw_input("> ")
            try:
                selected_choice_index = int(entered_choice)
            except ValueError:
                return None

            if not (1 <= selected_choice_index <= len(self.choices)):
                return None

            return self.choices[selected_choice_index - 1]



class TownHallScene(Scene):
    def __init__(self, name):
        self.name = name

    def enter(self, player):
        os.system('clear')

        if not player.quest_tracker.is_completed('talk to the mayor'):
            print "Oh dear. A goblin outside the city has been terrorizing the town."
            print "I know! You could slay the goblin!"
            print "Here go buy yourself a sword and come back with it's head."
            print "for an award."
            print "*The mayor hands you 10 gold coins."
            player.add_gold(10)
            player.quest_tracker.set_completed('talk to the mayor')
            return self.go_back_to_town()

        if not player.quest_tracker.is_completed('kill the goblin'):
            if not player.inventory['goblin head']:
                print "Please come back once you have slain that awful beast."
                return self.go_back_to_town()
            else:
                print "Oh thank you, thank you kind sir! Here is your award!"
                print "*The mayor gives you 30 gold coins."
                player.add_gold(30)
                player.quest_tracker.set_completed('kill the goblin')
                return self.go_back_to_town

        print "Thank you so much for saving us!"
        return self.go_back_to_town()

    def go_back_to_town(self):
        raw_input("Press ENTER to go back to town.")
        return "town"



class BuyScene(Scene):
    def __init__(self, name, item_class, price):
        self.name = name
        self.item_class = item_class
        self.price = price

    def enter(self, player):
        os.system('clear')

        print "That will be " + str(self.price) + " gold coins please.\n"

        if isinstance(player.weapon, self.item_class):
            print "But it looks like you already have a sword, bub."
            return self.go_back_to_store()

        if player.gold < self.price:
            print "Sorry but, uhh, it looks like you don't have enough."
            return self.go_back_to_store()

        print "Thank you for you business."
        print "Here's you new " + self.item_class.display_name + "."
        # ADD FUNCTIONALITY FOR ARMOR
        player.weapon = self.item_class()
        return self.go_back_to_store

    def go_back_to_store(self):
        raw_input("Press ENTER to go back to the store.")
        return "store"
