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
        self.description = "Looking around you realize this is where you started your journey."
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

class EmptyCavePath(MapTile):
    def __init__(self, x, y):
        self.description = "An empty cave path. There's nothing to see here and no enemies to kill you."
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

class LootRoom(MapTile):
    def __init__(self, x, y):
        self.chest = Chest(randint(0,100))
        self.description = "You're in a grand room with a chest at the center. Open it?"
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)

class EnemyRoom(MapTile):
    def __init__(self, x, y):
        self.description = "BAD GUY ROOM FUCK HIM"
        #self.enemy = generateEnemy(randint(0,1000))
        MapTile.__init__(self, x, y)

    def describe(self):
        MapTile.describe(self.description)
