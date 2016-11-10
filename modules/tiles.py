from item import Item, Weapon, Food
from chest import Chest
from random import randint

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def describe(self, description):
        print(description)

class Start(MapTile):
    def __init__(self, x, y):
        self.description = "Looking around you realize this is where you started your journey."
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

class Path(MapTile):
    def __init__(self, x, y):
        self.description = "A dirt path running through a thickly covered forest."
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

class BanditLoot(MapTile):
    def __init__(self, x, y):
        self.chest = Chest(randint(0,100))
        self.description = "Off to the side of the path there's a chest that some bandits left behind."
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

class Enemies(MapTile):
    def __init__(self, x, y):
        self.enemies = []
        self.killed_all_enemies = False
        self.description = "Bandits were hiding along the path... stop them from hurting anyone else!"
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def print_enemies(self):
        print("")
        print("| Enemies:")
        print("+------------------------------------------------+")
        for index, enemy in enumerate(self.enemies):
            print("| ======== " + str(index + 1) + " ========")
            print("| " + enemy.name + " Level: " + str(enemy.level))
            print("| " + str(enemy.hp) + "/" + str(enemy.maxhp))
            print("| Description: " + enemy.description)
        print("+------------------------------------------------+")
        print("")
