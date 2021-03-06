from player import Player
from world import World
from scenes import scenes

def main():
    player = Player()
    world = World(player)

    for scene in scenes:
        world.add_scene(scene)

    world.start()

main()
