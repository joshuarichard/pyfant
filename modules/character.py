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
        self.maxhp = self.resilience * 12
        self.hp = self.maxhp
        self.defence = (self.resilience * .40) + (self.strength * .25) + (self.dexterity * .10)
        self.armour = 0
        self.equipped = {
            "sword": None,
            "dagger": None,
            "shield": None,
            "bow": None,
            "arrows": None,
            "helmet": None,
            "torso": None,
            "leggings": None,
            "boots": None
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
        if (item.weight + self.weight_cur <= self.weight_cap):
            self.inventory.append(item)
            self.weight_cur = self.weight_cur + item.weight
            return True
        else:
            print(item.name + " too heavy to be added to inventory.")
            return False

    def dropItemFromInventory(self, index):
        index = index
        inIventory = False
        try:
            item = self.inventory[index]
            inInventory = True
        except:
            inInventory = False
            print("There is no item in the inventory at that index.")

        if (inInventory is True):
            self.weight_cur = self.weight_cur - self.inventory[index].weight
            del self.inventory[index]

    def equipItem(self, index):
        isItem = False
        try:
            item = self.inventory[index]
            isItem = True
        except:
            isItem = False

        if (isItem is True):
            if (self.inventory[index].__class__.__name__ == "Weapon"):
                if ("sword" in self.inventory[index].name):
                    if (self.equipped["sword"] is None):
                        self.equipped["sword"] = self.inventory[index]
                        self.dropItemFromInventory(index)
                        print(self.equipped["sword"].name + " equipped.")
                    else:
                        print("There is already an item equipped in the slot for that item.")
                elif ("Dagger" in self.inventory[index].name):
                    if (self.equipped["dagger"] is None):
                        self.equipped["dagger"] = self.inventory[index]
                        self.dropItemFromInventory(index)
                        print(self.equipped["dagger"].name + " equipped.")
                    else:
                        print("There is already an item equipped in the slot for that item.")
            elif (self.inventory[index].__class__.__name__ == "Armour"):
                if ("Helmet" in self.inventory[index].name):
                    if (self.equipped["helmet"] is None):
                        self.equipped["helmet"] = self.inventory[index]
                        self.dropItemFromInventory(index)
                        print(self.equipped["helmet"].name + " equipped.")
                    else:
                        print("There is already an item equipped in the slot for that item.")
                elif ("Chainmail" in self.inventory[index].name or "Platemail" in self.inventory[index].name):
                    if (self.equipped["torso"] is None):
                        self.equipped["torso"] = self.inventory[index]
                        self.dropItemFromInventory(index)
                        print(self.equipped["torso"].name + " equipped.")
                    else:
                        print("There is already an item equipped in the slot for that item.")
                elif ("Leggings" in self.inventory[index].name):
                    if (self.equipped["leggings"] is None):
                        self.equipped["leggings"] = self.inventory[index]
                        self.dropItemFromInventory(index)
                        print(self.equipped["leggings"].name + " equipped.")
                    else:
                        print("There is already an item equipped in the slot for that item.")
                elif ("Boots" in self.inventory[index].name):
                    if (self.equipped["boots"] is None):
                        self.equipped["boots"] = self.inventory[index]
                        self.dropItemFromInventory(index)
                        print(self.equipped["boots"].name + " equipped.")
                    else:
                        print("There is already an item equipped in the slot for that item.")
            else:
                print("You cannot equip that item.")
        else:
            print("There is no item at that index.")

    def unequipItem(self, slot):
        if (self.equipped[slot] is not None):
            if (self.addItemToInventory(self.equipped[slot]) is True):
                dropped = self.equipped[slot]
                self.equipped[slot] = None
                print(dropped.name + " unequipped.")
            else:
                print(self.equipped[slot].name + " too heavy to be added to inventory.")
        else:
            print("There is nothing equipped in that slot.")

    def heal(self, index):
        if ("Food" in self.inventory[index].__class__.__name__):
            if (self.hp + self.inventory[index].healing <= self.maxhp):
                healing = self.inventory[index].healing
                self.hp = self.hp + self.inventory[index].healing
                self.dropItemFromInventory(index)
                print("Healed " + str(healing) + " hp.")
            else:
                difference = self.maxhp - self.hp
                self.hp = self.maxhp
                self.dropItemFromInventory(index)
                print("Healed " + str(difference) + " hp.")
        else:
            print("That item is not consumable.")

    def printStatus(self):
        print("")
        print("| Levels:")
        print("+------------------------------------------------+")
        print("| Character Name: " + self.name)
        print("| Character Class: " + self.char_class)
        print("| HP: " + str(self.hp) + "/" + str(self.maxhp))
        print("| Resilience: " + str(self.resilience))
        print("| Strength: " + str(self.strength))
        print("| Dexterity: " + str(self.dexterity))
        print("| Accuracy: " + str(self.accuracy))
        print("+------------------------------------------------+")
        print("")

    def printInventory(self):
        print("")
        print("| Equipped:")
        print("+------------------------------------------------+")
        i = 0 # i used to only print the "======" for all but the first one
        for key, item in self.equipped.iteritems():
            if(hasattr(item, "name")):
                if (i > 0):
                    print("| ===================")
                print("| " + str(key).title())
                item.printItem()
                #print("| -------------")
            else:
                if (i > 0):
                    print("| ===================")
                print("| " + str(key).title())
                print("| None")
                #print("| -------------")
            i = i + 1
        print("+------------------------------------------------+")
        print("")
        print("| Inventory:")
        print("+------------------------------------------------+")
        print("| Bag Capacity: " + str(self.weight_cap) + "  Current Weight: " + str(self.weight_cur))
        if(len(self.inventory) == 0):
            print("| Nothing in your inventory.")
        for index, item in enumerate(self.inventory):
            print("| ======== " + str(index + 1) + " ========")
            item.printItem()
        print("+------------------------------------------------+")
        print("")
