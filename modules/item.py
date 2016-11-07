class Item(object):
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def printItem(self):
        print("| " + self.name)
        print("| Value: " + str(self.value) + " Weight: " + str(self.weight))

class Weapon(Item):
    def __init__(self, name, weight, value, piercing, slashing, blunt):
        self.piercing = piercing
        self.slashing = slashing
        self.blunt = blunt
        Item.__init__(self, name, weight, value)

    def printItem(self):
        Item.printItem(self)
        #print("| Damage:")
        print("| Piercing: " + str(self.piercing) + " Slashing: " + str(self.slashing) + " Blunt: " + str(self.blunt))

class Armour(Item):
    def __init__(self, name, weight, value, piercing, slashing, blunt):
        self.piercing = piercing
        self.slashing = slashing
        self.blunt = blunt
        Item.__init__(self, name, weight, value)

    def printItem(self):
        Item.printItem(self)
        #print("| Defence:")
        print("| Piercing: " + str(self.piercing) + " Slashing: " + str(self.slashing) + " Blunt: " + str(self.blunt))

class Food(Item):
    def __init__(self, name, weight, value, healing):
        self.healing = healing
        Item.__init__(self, name, weight, value)

    def printItem(self):
        Item.printItem(self)
        print("| Healing: " + str(self.healing))

class Drink(Item):
    def __init__(self, name, weight, value, healing, drunkLevel):
        self.healing = healing
        self.drunkLevel = drunkLevel
        Item.__init__(self, name, weight, value)

    def printItem(self):
        Item.printItem(self)
        print("| Healing: " + str(self.healing) + " Drunk: " + str(self.drunkLevel))
