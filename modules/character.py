from config import config

class Character:
    def __init__(self, name, char_class, startingLocation):
        self.name = name
        self.char_class = char_class
        self.inventory = []
        self.weight_cap = 30
        self.weight_cur = 0
        self.currentLocation = startingLocation
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

    def setLocation(self, location):
        self.currentLocation = location

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
        self.weight_cap = bagWeight

    def addItemToInventory(self, item):
        if(item.weight + self.weight_cur <= self.weight_cap):
            self.inventory.append(item)
            self.weight_cur = self.weight_cur + item.weight
            return True
        else:
            print(item.name + " too heavy to be added to inventory.")
            return False

    def dropItemFromInventory(self, index):
        index = index - 1
        self.weight_cur = self.weight_cur - self.inventory[index].weight
        del self.inventory[index]

    def equipItem(self, index):
        index = index - 1
        if("sword" in self.inventory[index].name):
            self.equipped["sword"] = self.inventory[index]
            self.dropItemFromInventory(index + 1)

    def printStatus(self):
        print("Character Name: " + self.name)
        print("Character Class: " + self.char_class)
        print("-------- Levels --------")
        print("Resilience: " + str(self.resilience))
        print("Strength: " + str(self.strength))
        print("Dexterity: " + str(self.dexterity))
        print("Accuracy: " + str(self.accuracy))

    def printInventory(self):
        print("-------- Items ---------")
        print("Equipped: ")
        print("=========")
        for key, value in self.equipped.iteritems():
            if(hasattr(value, "name")):
                print(key + " - ")
                item.printItem()
            else:
                print(key + " - " + str(value))
        print("Inventory:")
        print("==========")
        print("Bag Capacity: " + str(self.weight_cap) + "  Current Weight: " + str(self.weight_cur))
        if(len(self.inventory) == 0):
            print("Nothing in your inventory.")
        for index, item in enumerate(self.inventory):
            print("==")
            item.printItem()
