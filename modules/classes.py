from config import config

class Item(object):
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

class Weapon(Item):
    def __init__(self, name, weight, value, piercing, slashing, blunt):
        self.piercing = piercing
        self.slashing = slashing
        self.blunt = blunt
        Item.__init__(self, name, weight, value)

class Food(Item):
    def __init__(self, name, weight, value, healing):
        self.healing = healing
        Item.__init__(self, name, weight, value)

class Character(object):
    def __init__(self, name, char_class):
        self.name = name
        self.inventory = []
        self.weightCap = 30
        self.weightCur = 0
        self.resilience = config["class_starting_levels"][char_class][0]
        self.strength = config["class_starting_levels"][char_class][1]
        self.dexterity = config["class_starting_levels"][char_class][2]
        self.accuracy = config["class_starting_levels"][char_class][3]
        self.equipped = {
            "sword": None,
            "dagger1": None,
            "dagger2": None,
            "shield": None,
            "bow": None,
            "arrows": None
        }

    def levelUp(self, skill):
        if (skill == "resilience"):
            self.resilience = self.resilience + 1
        elif (skill == "strength"):
            self.strength = self.strength + 1
        elif (skill == "dexterity"):
            self.dexterity = self.dexterity + 1
        elif (skill == "accuracy"):
            self.accuracy == self.accuracy + 1

    def updateWeight(self, bagWeight):
        self.weightCap = bagWeight

    def addItemToInventory(self, item):
        if(item.weight + self.weightCur <= self.weightCap):
            self.inventory.append(item)
            self.weightCur = self.weightCur + item.weight
        else:
            print(item.name + " too heavy to be added to inventory.")

    def dropItemFromInventory(self, item):
        foundItem = False
        for itemInInventory in self.inventory:
            if(item == itemInInventory.name):
                del self.inventory[self.inventory.index(itemInInventory)]
                self.weightCur = self.weightCur - itemInInventory.weight
                foundItem = True
                break
        if(foundItem is False):
            print(item + " is not in your inventory.")

    def printStatus(self):
        print("Character Name: " + self.name)
        print("---------------")
        print("Levels")
        print("Resilience: " + str(self.resilience) + "  Strength: " + str(self.strength))
        print("Dexterity: " + str(self.dexterity) + "  Accuracy: " + str(self.accuracy))
        print("---------------")
        print("Inventory")
        print("Bag Capacity: " + str(self.weightCap) + "  Current Weight: " + str(self.weightCur))
        print("Equipped: " + str(self.equipped))
        for item in self.inventory:
            print("Name: " + item.name + "  Weight: " + str(item.weight) + "  Value: " + str(item.value))
