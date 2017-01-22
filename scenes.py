import os

from scene import Scene, SceneChoice, TownHallScene, BuyScene
from weapons import IronSword
from armor import IronArmor

scenes = [
    Scene(
        "town",
        "You are a traveller having arrived in the small town of Smalltown.\n" + \
        "Where do you go?",
        [
            SceneChoice("Store", "store"),
            SceneChoice("Town Hall", "town_hall")
        ]
    ),

    Scene(
        "store",
        "Hmm. You don't look like you are from around here.\n" + \
        "Anyways, how can I help you?",
        [
            SceneChoice("Buy sword", "buy_sword"),
            SceneChoice("Buy armor", "buy_armor"),
            SceneChoice("Leave the store", "town")
        ]
    )

    TownHallScene("town_hall")
    BuyScene("buy_sword", IronSword, 10)
    BuyScene("buy_armor", IronArmor, 30)

]
