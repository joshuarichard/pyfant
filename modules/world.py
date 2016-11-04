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
                if(entry is not None):
                    if(entry.__class__.__name__ == "StartingRoom"):
                        return [indexX, indexY]

    def canGo(self, goingX, goingY):
        if(self.map[goingX][goingY] is not None):
            return True
        else:
            return False

    def getTile(self, x, y):
        return self.map[x][y]

def getWorld():
    worldList = []
    for indexX, row in enumerate(Maps[CurrentMap]):
        rowList = []
        for indexY, entry in enumerate(row):
            if(Maps[CurrentMap][indexX][indexY] is not None):
                if(Maps[CurrentMap][indexX][indexY] == "StartingRoom"):
                    rowList.append(StartingRoom(indexX, indexY))
                elif(Maps[CurrentMap][indexX][indexY] == "EmptyCavePath"):
                    rowList.append(EmptyCavePath(indexX, indexY))
                elif(Maps[CurrentMap][indexX][indexY] == "LootRoom"):
                    rowList.append(LootRoom(indexX, indexY))
            else:
                rowList.append(None)
        worldList.append(rowList)
    return World(worldList)
