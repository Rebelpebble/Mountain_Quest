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
