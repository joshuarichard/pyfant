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
