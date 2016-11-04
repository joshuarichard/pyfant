from item import Item, Weapon, Food
from chest import Chest
from random import randint
#from enemy import Enemy

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def describe(self, description):
        print(description)

class StartingRoom(MapTile):
    def __init__(self, x, y):
        self.description = "STARTING room baby"
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

class EmptyCavePath(MapTile):
    def __init__(self, x, y):
        self.description = "cave path boring"
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

class LootRoom(MapTile):
    def __init__(self, x, y):
        self.chest = Chest(randint(0,100))
        self.description = "grab some loot"
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

class EnemyRoom(MapTile):
    def __init__(self, x, y):
        self.description = "bad guy room"
        #self.enemy = generateEnemy(randint(0,1000))
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)
