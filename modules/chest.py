from random import randint
from modules.generate import generateItem

class Chest(object):
    def __init__(self, level):
        itemTypes = {
            0: "sword",
            1: "bow",
            2: "armour",
            3: "food",
            4: "drink"
        }

        self.contents = []

        numOfItems = randint(10,20)
        for n in range(0, numOfItems):
            self.contents.append(generateItem(randint(0, 400), itemTypes[randint(0,4)]))
