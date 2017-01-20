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
