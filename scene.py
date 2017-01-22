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
