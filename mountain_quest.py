import random

### Monsters ###
class Monster(object):

    def __init__(self):
        # TREY: Why is it necessary to do this?
        self.current_health = self.starting_health

    def is_alive(self):
        return current_health > 0

    def take_damage(self, damage):
        self.current_health = self.current_health - damage

class Goblin(Monster):
    display_name = "goblin"
    starting_health = 10

    def attack(self):
        return random.randint(0, 5)

class Troll(Monster):
    display_name = "troll"
    starting_health = 20

    def attack(self):
        return random.randint(2, 10)

class Basilisk(Monster):
    display_name = "basilisk"
    starting_health = 30

    def attack(self):
        return random.randint(9, 15)

class Dragon(Monster):
    display_name = "grand dragon"
    starting_health = 100

    def attack(self):
        return random.randint(30, 50)
######

### Weapons ###
class Weapon(object):
    pass

class Hands(Weapon):
    pass

class IronSword(Weapon):
    pass

class SteelSword(Weapon):
    pass

class DragonSword(Weapon):
    pass
######

### Armor ###
class Armor(object):
    pass

class Clothes(Armor):
    pass

class IronArmor(Armor):
    pass

class SteelArmor(Armor):
    pass
######
