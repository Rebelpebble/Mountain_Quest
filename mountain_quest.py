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
        return random.randint(0, 2)

class Troll(Monster):
    display_name = "troll"
    starting_health = 20

    def attack(self):
        return random.randint(2, 5)

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

    def attack(self):
        return random.randint(0, 2)

class IronSword(Weapon):

    def attack(self):
        return random.randint(3, 8)

class SteelSword(Weapon):

    def attack(self):
        return random.randint(6, 12)

class DragonSword(Weapon):

    def attack(self):
        return random.randint(6, 12)

    def dragon_attack(self):
        return random.randint(16, 35)
######

### Armor ###
class Armor(object):
    pass

class Clothes(Armor):

    def damage_reduction(self):
        return 1

class IronArmor(Armor):

    def damage_reduction(self):
        return 1.25

class SteelArmor(Armor):

    def damage_reduction(self):
        return 1.75

class DragonNecklace(Armor):

    def damage_reduction(self):
        return 3
######
