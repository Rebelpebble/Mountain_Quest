import random
import os
from sys import exit

### Monsters ###
class Monster(object):

    def __init__(self):
        # TREY: Why is it necessary to do this? Is this to give each instance a current health?
        self.current_health = self.starting_health

    def is_alive(self):
        return self.current_health > 0

    def take_damage(self, damage):
        self.current_health -= damage

class Goblin(Monster):
    display_name = "Goblin"
    starting_health = 10

    def attack(self):
        return random.randint(0, 2)

class Troll(Monster):
    display_name = "Troll"
    starting_health = 20

    def attack(self):
        return random.randint(2, 5)

class Basilisk(Monster):
    display_name = "Basilisk"
    starting_health = 30

    def attack(self):
        return random.randint(9, 15)

class Dragon(Monster):
    display_name = "Grand Dragon"
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



def clear():
    os.system('clear')

def battle():
    clear()

    print "A %s appeared!\n" % monster.display_name.lower()
    print " " * (len(monster.display_name) - 3), "My HP: ", "-" * my_health
    print "%s HP: " % monster.display_name, "-" * monster.current_health

    while monster.is_alive():
        print "\nWill you fight (1) or flee (2)?"

        choice = raw_input("> ")
        fight_results = fight(choice)
        clear()

        print "You did %d damage." % fight_results[0]
        print "The %s did %d damage.\n" % (monster.display_name, fight_results[1])
        # TREY: Do the following two lines smell?
        print " " * (len(monster.display_name) - 3), "My HP: ", "-" * my_health
        print "%s HP: " % monster.display_name, "-" * monster.current_health

def fight(choice):
    global my_health

    if choice == "1":
        my_attack = my_weapon.attack()
        monster_attack = monster.attack()
        # Armor damage reduction is a float and the damage needs to be
        # converted to an integer.
        my_health -= int(monster_attack / my_armor.damage_reduction())
        monster.take_damage(my_attack)

        return my_attack, monster_attack

    else:
        exit(0)

my_health = 20
my_weapon = SteelSword()
my_armor = IronArmor()
monster = Troll()

battle()
print my_health
