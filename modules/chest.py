from random import randint
from modules.generate import generate_item

class Chest(object):
    def __init__(self, level):
        item_types = {
            0: "sword",
            1: "dagger",
            2: "bow",
            3: "arrows",
            4: "armour",
            5: "food",
            6: "drink"
        }

        self.contents = []

        num_of_items = randint(1, 4)
        for n in range(0, num_of_items):
            self.contents.append(generate_item(randint(120, 800), item_types[randint(0,4)]))
