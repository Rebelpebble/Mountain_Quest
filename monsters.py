class Monster(object):

    def __init__(self):
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
