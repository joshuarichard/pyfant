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
        self.maxhp = self.resilience * 120
        self.hp = self.maxhp
        self.level = 0
        self.xp_to_next_level = 100
        self.xp = 0
        self.defence = 0

        self.a_piercing = 0
        self.a_slashing = 0
        self.a_blunt = 0
        self.d_piercing = 0
        self.d_slashing = 0
        self.d_blunt = 0

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

    def addXP(self, xp):
        self.xp = self.xp + xp

        if (self.xp > self.xp_to_next_level):
            levelUp()

    def levelUp(self):
        print("You leveled up!")
        print("Which skill would you like to increase?")

        while True:
            skill = raw_input("R) Resilience S) Strength D) Dexterity A) Accuracy [R/S/D/A] : ")
            if skill in ["R", "r", "S", "s", "D", "d", "A", "a"]:
                break

        if (skill == "R" or skill == "r"):
            self.resilience = self.resilience + 1
        elif (skill == "S" or skill == "s"):
            self.strength = self.strength + 1
        elif (skill == "D" or skill == "d"):
            self.dexterity = self.dexterity + 1
        elif (skill == "A" or skill == "a"):
            self.accuracy == self.accuracy + 1

        self.level = self.level + 1
        self.xp_to_next_level = self.level ** 2
        self.maxhp = self.resilience * 120
        self.hp = self.maxhp

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

    def calculate_stats(self, weapon):
        self.defence = (self.resilience * 40) + (self.strength * 25) + (self.dexterity * 10)
        try:
            self.a_piercing = self.equipped[weapon].piercing + (self.strength * 1.83 + self.dexterity * 1.32)
            self.a_slashing = self.equipped[weapon].slashing + (self.strength * 2 + self.dexterity * 1.16)
            self.a_blunt = self.equipped[weapon].blunt + (self.strength * 2 + self.dexterity * 1.07)
        except:
            print("You're not holding one of those weapons.")
            self.a_piercing = 0
            self.a_slashing = 0
            self.a_blunt = 0

        armour = ["helmet", "torso", "leggings", "boots"]
        d_piercing = 0
        d_slashing = 0
        d_blunt = 0
        for a in armour:
            if (hasattr(self.equipped[a], "piercing")):
                d_piercing = d_piercing + self.equipped[a].piercing
            if (hasattr(self.equipped[a], "slashing")):
                d_slashing = d_slashing + self.equipped[a].slashing
            if (hasattr(self.equipped[a], "blunt")):
                d_blunt = d_blunt + self.equipped[a].blunt

        self.d_piercing = .0009 * (self.defence + d_piercing)
        self.d_slashing = .0009 * (self.defence + d_slashing)
        self.d_blunt = .0009 * (self.defence + d_blunt)

    def fight(self, enemy, weapon):
        self.calculate_stats(weapon)
        total_damage_to_enemy =  (self.a_piercing  * (1 - enemy.d_piercing)) + (self.a_slashing  * (1 - enemy.d_slashing)) + (self.a_blunt  * (1 - enemy.d_blunt))
        total_damage_to_player = (enemy.a_piercing * (1 - self.d_piercing))  + (enemy.a_slashing * (1 - self.d_slashing))  + (enemy.a_blunt * (1 - self.d_blunt))

        print("You hit " + enemy.name + " with " + str(total_damage_to_enemy) + " damage.")
        print("You are hit by " + enemy.name + " for " + str(total_damage_to_player) + " damage.")

        return [total_damage_to_enemy, total_damage_to_player]

    def printStatus(self):
        print("")
        print("| Levels:")
        print("+------------------------------------------------+")
        print("| Character Name: " + self.name)
        print("| Character Class: " + self.char_class.title())
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
