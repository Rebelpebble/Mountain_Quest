import random
import os
from sys import exit

### Player Information ###
class Player(object):
    starting_health = 20

    def __init__(self, my_weapon, my_armor, quests):
        self.my_health = self.starting_health
        self.my_weapon = my_weapon
        self.my_armor = my_armor
        self.quests = quests

    def reset_health(self):
        self.my_health = self.starting_health


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

    @staticmethod
    def attack():
        return random.randint(2, 5)

class Basilisk(Monster):
    display_name = "Basilisk"
    starting_health = 30

    @staticmethod
    def attack():
        return random.randint(9, 15)

class Dragon(Monster):
    display_name = "Dragon"
    starting_health = 100

    @staticmethod
    def attack():
        return random.randint(30, 50)
######


### Weapons ###
class Weapon(object):
    pass

class Hands(Weapon):

    @staticmethod
    def attack():
        return random.randint(0, 2)

class IronSword(Weapon):
    display_name = "iron sword"

    @staticmethod
    def attack():
        return random.randint(3, 8)

class SteelSword(Weapon):
    display_name = "steel sword"

    @staticmethod
    def attack():
        return random.randint(6, 12)

class DragonSword(Weapon):
    display_name = "dragon sword"

    @staticmethod
    def attack():
        return random.randint(16, 35)
######


### Armor ###
class Armor(object):
    pass

class Clothes(Armor):

    @staticmethod
    def damage_reduction():
        return 1

class IronArmor(Armor):
    display_name = "iron armor"

    @staticmethod
    def damage_reduction():
        return 1.25

class SteelArmor(Armor):
    display_name = "steel armor"

    @staticmethod
    def damage_reduction():
        return 1.75

class DragonNecklace(Armor):
    display_name = "dragon necklace"

    @staticmethod
    def damage_reduction():
        return 3
######

def clear():
    os.system('clear')

### Fighting System ###
def print_health():
    print " " * (len(monster.display_name) - 3), "My HP: ", "-" * my_health
    print "%s HP: " % monster.display_name, "-" * monster.current_health

def battle():
    clear()

    print "A %s appeared!\n" % monster.display_name.lower()
    print_health()

    while monster.is_alive():
        print "\nWill you fight (1) or flee (2)?"

        choice = raw_input("> ")
        fight_results = fight(choice)
        clear()

        print "You did %d damage." % fight_results[0]
        print "The %s did %d damage.\n" % (monster.display_name.lower(), fight_results[1])
        # TREY: Do the following two lines smell?
        print_health()

    print "You beat the %s!" % monster.display_name.lower()
    reset_health()

def fight(choice):
    global my_health

    if choice == "1":
        my_attack = my_weapon.attack()
        monster_attack = monster.attack()
        # Armor damage reduction is a float and the damage needs to be
        # converted to an integer.
        my_health -= int(monster_attack / my_armor.damage_reduction())
        monster.take_damage(my_attack)

        died()

        return my_attack, monster_attack

    else:
        exit(0)

def died():
    if my_health <= 0:
        clear()
        print "You died!"
        exit(0)

def reset_health():
    global my_health
    my_health = my_starting_health
######


### Story ###
def town():
    clear()

    print (
    "You are a traveller having arrived in the small town of Smalltown.\n"
    "Where do you go?\n"
    "(1) Store\n"
    "(2) Town Hall\n"
    "(3) Widow\'s House\n"
    "(4) Large Gate\n")

    choice = raw_input("> ")

    if choice == "1":
        store()
    elif choice == "2":
        town_hall()
    elif choice == "3":
        widows_house()
    elif choice == "4":
        gate()
    else:
        town()

def store():
    clear()

    print(
    "Hmm. You don\'t look like you are from around here.\n"
    "Anyways, how can I help you?\n"
    "(1) Buy sword.\n"
    "(2) Buy armor.\n"
    "(3) Leave the store."
    )

    choice = raw_input("> ")

    if choice == "1":
        buy_sword()
    elif choice == "2":
        buy_armor()
    elif choice == "3":
        town()
    else:
        store()

def buy_sword():
    print "\nThat will be 10 gold coins please."

    if quests[1] == True:
        print "Looks like you already have a sword, bub."
    elif quests[0] == True:
        print "Thank you for your business."
        print "Here's your new iron sword."
        print "*The store owner gives you a sword.*"
        quest[1] = True
        player.my_weapon = IronSword()
    else:
        print "Wait a minute...you don't have a dime on you!"
        print "Get outta here you penniless hobo!"

    print "\nPress enter to leave the store."
    raw_input("> ")
    town()

def buy_armor():
    print "\nThat will be 30 gold coins please."

    if quests[3] == True:
        print "Looks like you already have armor, bub."
    elif quests[2] == True:
        print "Thank you for your business."
        print "Here's your new iron armor."
        print "*The store owner gives you armor.*"
        quest[3] = True
        player.my_armor = IronArmor()
    else:
        print "Wait a minute...you don't have a dime on you!"
        print "Get outta here you penniless hobo!"

    print "\nPress enter to leave the store."
    raw_input("> ")
    town()

def town_hall():
    pass

def widows_house():
    pass

def gate():
    pass

def frontier():
    pass

def goblins_den():
    pass

def meadow():
    pass

def mountain_pass():
    pass

def fork_in_the_road():
    pass

def injured_traveler():
    pass

def maze():
    pass

def old_armory():
    pass

def rocky_pass():
    pass

def basilisks_lair():
    pass

def burnt_skeleton():
    pass

def dragon_final_battle():
    pass
######

quests = {}
for x in range(0, 11):
    quests[x] = False

player = Player(Hands(), Clothes(), quests)

town()
