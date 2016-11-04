from resources.maps import Maps
from tiles import StartingRoom, EmptyCavePath, LootRoom
from config import config

CurrentMap = config["CurrentMap"]

class World:
    def __init__(self, map):
        self.map = map

    def getStartingRoomLocation(self):
        for indexX, row in enumerate(self.map):
            for indexY, entry in enumerate(row):
                if (entry is not None):
                    if (entry.__class__.__name__ == "StartingRoom"):
                        return [indexX, indexY]

    def canGo(self, goingX, goingY):
        try:
            if (self.map[goingX][goingY] is not None):
                return True
            else:
                return False
        except:
            return False

    def getTile(self, x, y):
        return self.map[x][y]

    def lookAtAdjacentTiles(self, x, y):
        # N S W E
        directions = {
            0: "Up: ",
            1: "Down: ",
            2: "Left: ",
            3: "Right: "
        }

        adjacentTiles = []

        # top row
        # left, middle, right
        if (self.canGo(x - 1, y)):
            adjacentTiles.append([None, self.map[x - 1][y].__class__.__name__, None])
        else:
            adjacentTiles.append([None, None, None])

        # middle row
        middleRow = []

        # left
        if (self.canGo(x, y - 1)):
            middleRow.append(self.map[x][y - 1].__class__.__name__)
        else:
            middleRow.append(None)

        # middle (current location)
        middleRow.append(self.map[x][y].__class__.__name__)

        # right
        if (self.canGo(x, y + 1)):
            middleRow.append(self.map[x][y + 1].__class__.__name__)
        else:
            middleRow.append(None)

        adjacentTiles.append(middleRow)

        # bottom row
        # left, middle, right
        if (self.canGo(x + 1, y)):
            adjacentTiles.append([None, self.map[x + 1][y].__class__.__name__, None])
        else:
            adjacentTiles.append([None, None, None])

        for row in adjacentTiles:
            print(str(row))

def getWorld():
    worldList = []
    for indexX, row in enumerate(Maps[CurrentMap]):
        rowList = []
        for indexY, entry in enumerate(row):
            if (Maps[CurrentMap][indexX][indexY] is not None):
                if (Maps[CurrentMap][indexX][indexY] == "StartingRoom"):
                    rowList.append(StartingRoom(indexX, indexY))
                elif (Maps[CurrentMap][indexX][indexY] == "EmptyCavePath"):
                    rowList.append(EmptyCavePath(indexX, indexY))
                elif (Maps[CurrentMap][indexX][indexY] == "LootRoom"):
                    rowList.append(LootRoom(indexX, indexY))
            else:
                rowList.append(None)
        worldList.append(rowList)
    return World(worldList)
