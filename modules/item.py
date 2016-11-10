class Item(object):
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def print_item(self):
        print("| " + self.name)
        print("| Value: " + str(self.value) + " Weight: " + str(self.weight))

class Weapon(Item):
    def __init__(self, name, weight, value, piercing, slashing, blunt):
        self.piercing = piercing
        self.slashing = slashing
        self.blunt = blunt
        Item.__init__(self, name, weight, value)

    def print_item(self):
        Item.print_item(self)
        print("| Piercing: " + str(self.piercing) + " Slashing: " + str(self.slashing) + " Blunt: " + str(self.blunt))

class Armour(Item):
    def __init__(self, name, weight, value, piercing, slashing, blunt):
        self.piercing = piercing
        self.slashing = slashing
        self.blunt = blunt
        Item.__init__(self, name, weight, value)

    def print_item(self):
        Item.print_item(self)
        print("| Piercing: " + str(self.piercing) + " Slashing: " + str(self.slashing) + " Blunt: " + str(self.blunt))

class Food(Item):
    def __init__(self, name, weight, value, healing):
        self.healing = healing
        Item.__init__(self, name, weight, value)

    def print_item(self):
        Item.print_item(self)
        print("| Healing: " + str(self.healing))

class Drink(Item):
    def __init__(self, name, weight, value, healing, drunk):
        self.healing = healing
        self.drunk = drunk
        Item.__init__(self, name, weight, value)

    def print_item(self):
        Item.print_item(self)
        print("| Healing: " + str(self.healing) + " Drunk: " + str(self.drunk))
