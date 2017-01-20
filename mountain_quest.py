# My Files
from monsters import *
from armor import *
from weapons import *
from player import *

import random
import os
from sys import exit

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
def back_to_town():
    raw_input("Press ENTER")
    town()

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
    "(3) Leave the store.\n"
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
    print player.weapon

    #Broken
    if player.weapon != XXXXX:
        print "But it looks like you already have a sword, bub."
    elif quests[0] == True:
        print "Thank you for your business."
        print "Here's your new iron sword."
        print "*The store owner gives you a sword.*"
        player.weapon = IronSword()
    else:
        print "Sorry but, uhhh, it looks like you don't have enough."

    back_to_town()

def buy_armor():

    print "\nThat will be 30 gold coins please."

    #Broken
    if player.armor != XXXXX:
        print "But it looks like you already have armor, bub."
    elif player.gold == 10:
        print "Thank you for your business."
        print "Here's your new iron armor."
        print "*The store owner gives you armor.*"
        quest[3] = True
        player.my_armor = IronArmor()
    else:
        print "Sorry but, uhhh, it looks like you don't have enough."

    back_to_town()

def town_hall():
    clear()

    if player.quests[1] == True:
        print "Thank you so much for saving us!"
    elif player.quests[0] == True and player.inventory['goblin head'] == True:
        print "Oh thank you, thank you kind sir! Here is your reward!"
        print "*The mayor gives you 30 gold coins.*"
        player.add_gold(30)
    elif player.quests[0] == True and player.inventory['goblin head'] == False:
        print "Please come back once you have slain that awful beast."
    else:
        print "Oh dear. A goblin outside the city has been terrorizing the town."
        print "I know! You could slay the goblin!"
        print "Here go buy yourself a sword and come back with it\'s head"
        print "for and award."
        print "*The mayor hands you 10 gold coins."
        player.add_gold(10)
        player.quests[0] = True

    back_to_town()

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

player = Player(Hands(), Clothes())

town()
