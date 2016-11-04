from item import Item, Weapon, Food
from random import randint
from modules.generate import generateItem

class Chest(object):
    def __init__(self, level, type):
        self.contents = []

        itemTypes = {
            0: "sword",
            1: "armour",
            2: "jewelry",
            3: "food",
            4: "drink"
        } # type

        numOfItems = randint(0,4)
        for n in range(0, numOfItems):
            self.contents.append(generateItem(randint(0, 400), "sword"))
