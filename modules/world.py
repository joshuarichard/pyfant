from resources.maps import Maps
from tiles import Start, Path, BanditLoot, Enemies
from config import config

CurrentMap = config["CurrentMap"]

class World:
    def __init__(self, map):
        self.map = map

    def getStartingRoomLocation(self):
        for indexX, row in enumerate(self.map):
            for indexY, entry in enumerate(row):
                if (entry is not None):
                    if (entry.__class__.__name__ == "Start"):
                        return [indexX, indexY]

    def canGo(self, goingX, goingY):
        if (goingX < 0 or goingY < 0 or goingX > len(self.map[0]) - 1 or goingY > len(self.map) - 1):
            return False

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
        adjacentTiles = []

        # top row
        topRow = []

        # left
        if (self.canGo(x - 1, y - 1)): #  and x - 1 >= 0 and y - 1 >= 0
            topRow.append(self.map[x - 1][y - 1].__class__.__name__)
        else:
            topRow.append(None)

        # middle (current location)
        if (self.canGo(x - 1, y)): # and x - 1 >= 0
            topRow.append(self.map[x - 1][y].__class__.__name__)
        else:
            topRow.append(None)

        # right
        if (self.canGo(x - 1, y + 1)): # and x - 1 >= 0 and y + 1 <= len(self.map) - 1
            topRow.append(self.map[x - 1][y + 1].__class__.__name__)
        else:
            topRow.append(None)

        adjacentTiles.append(topRow)

        # middle row
        middleRow = []

        # left
        if (self.canGo(x, y - 1)): # and y - 1 >= 0
            middleRow.append(self.map[x][y - 1].__class__.__name__)
        else:
            middleRow.append(None)

        # middle (current location)
        middleRow.append(self.map[x][y].__class__.__name__)

        # right
        if (self.canGo(x, y + 1)): # and y + 1 <= len(self.map) - 1
            middleRow.append(self.map[x][y + 1].__class__.__name__)
        else:
            middleRow.append(None)

        adjacentTiles.append(middleRow)

        # bottom row
        bottomRow = []

        # left
        if (self.canGo(x + 1, y - 1)): # and x + 1 <= len(self.map[0]) - 1 and y - 1 >= 0
            bottomRow.append(self.map[x + 1][y - 1].__class__.__name__)
        else:
            bottomRow.append(None)

        # middle (current location)
        if (self.canGo(x + 1, y)): # and (x + 1 <= len(self.map[0]) - 1)
            bottomRow.append(self.map[x + 1][y].__class__.__name__)
        else:
            bottomRow.append(None)

        # right
        if (self.canGo(x + 1, y + 1)): # and x + 1 <= len(self.map[0]) - 1 and y + 1 <= len(self.map[0]) - 1
            bottomRow.append(self.map[x + 1][y + 1].__class__.__name__)
        else:
            bottomRow.append(None)

        adjacentTiles.append(bottomRow)

        # get longest string of all the strings and pad the smaller ones
        for indexR, row in enumerate(adjacentTiles):
            for indexC, col in enumerate(row):
                if (col is None):
                    adjacentTiles[indexR][indexC] = "Forest"

        longest = 0
        for row in adjacentTiles:
            for col in row:
                if (len(str(col)) > longest):
                    longest = len(str(col))

        for indexR, row in enumerate(adjacentTiles):
            for indexC, col in enumerate(row):
                if (longest > len(str(col))):
                    difference = longest - len(str(col))
                    newCol = str(col)
                    for d in range(difference):
                        newCol = newCol + " "
                    adjacentTiles[indexR][indexC] = newCol

        for row in adjacentTiles:
            print(str(row))

def getWorld():
    worldList = []
    for indexX, row in enumerate(Maps[CurrentMap]):
        rowList = []
        for indexY, entry in enumerate(row):
            if (Maps[CurrentMap][indexX][indexY] is not None):
                if (Maps[CurrentMap][indexX][indexY] == "Start"):
                    rowList.append(Start(indexX, indexY))
                elif (Maps[CurrentMap][indexX][indexY] == "Path"):
                    rowList.append(Path(indexX, indexY))
                elif (Maps[CurrentMap][indexX][indexY] == "BanditLoot"):
                    rowList.append(BanditLoot(indexX, indexY))
                elif (Maps[CurrentMap][indexX][indexY] == "Enemies"):
                    rowList.append(Enemies(indexX, indexY))
            else:
                rowList.append(None)
        worldList.append(rowList)
    return World(worldList)
