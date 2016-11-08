from random import randint
from modules.generate import generateItem

class Chest(object):
    def __init__(self, level):
        itemTypes = {
            0: "sword",
            1: "dagger",
            2: "bow",
            3: "arrows",
            4: "armour",
            5: "food",
            6: "drink"
        }

        self.contents = []

        numOfItems = randint(1, 4)
        for n in range(0, numOfItems):
            self.contents.append(generateItem(randint(120, 800), itemTypes[randint(0,4)]))
