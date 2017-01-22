class World(object):
    def __init__(self, player):
        self.player = player
        self.scene = {}

    def add_scene(self, name):
        self.scenes[scene.name] = scene
        if len(self.scenes) == 1:
            self.starting_scene = scene

    def start(self):
        scene = self.starting_scene
        while True:
            next_scene_name = scene.enter(self.player)
            scene self.scenes[next_scene_name]
