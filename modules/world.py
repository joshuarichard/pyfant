from resources.maps import Maps
from tiles import Start, Path, BanditLoot, Enemies
from config import config

current_map = config["current_map"]

class World:
    def __init__(self, map):
        self.map = map

    def get_starting_room_location(self):
        for indexX, row in enumerate(self.map):
            for indexY, entry in enumerate(row):
                if (entry is not None):
                    if (entry.__class__.__name__ == "Start"):
                        return [indexX, indexY]

    def can_go(self, goingX, goingY):
        if (goingX < 0 or goingY < 0 or goingX > len(self.map[0]) - 1 or goingY > len(self.map) - 1):
            return False

        try:
            if (self.map[goingX][goingY] is not None):
                return True
            else:
                return False
        except:
            return False

    def get_tile(self, x, y):
        return self.map[x][y]

    def look_at_adjacent_tiles(self, x, y):
        adjacentTiles = []

        # top row
        topRow = []

        # left
        if (self.can_go(x - 1, y - 1)): #  and x - 1 >= 0 and y - 1 >= 0
            topRow.append(self.map[x - 1][y - 1].__class__.__name__)
        else:
            topRow.append(None)

        # middle (current location)
        if (self.can_go(x - 1, y)): # and x - 1 >= 0
            topRow.append(self.map[x - 1][y].__class__.__name__)
        else:
            topRow.append(None)

        # right
        if (self.can_go(x - 1, y + 1)): # and x - 1 >= 0 and y + 1 <= len(self.map) - 1
            topRow.append(self.map[x - 1][y + 1].__class__.__name__)
        else:
            topRow.append(None)

        adjacentTiles.append(topRow)

        # middle row
        middleRow = []

        # left
        if (self.can_go(x, y - 1)): # and y - 1 >= 0
            middleRow.append(self.map[x][y - 1].__class__.__name__)
        else:
            middleRow.append(None)

        # middle (current location)
        middleRow.append(self.map[x][y].__class__.__name__)

        # right
        if (self.can_go(x, y + 1)): # and y + 1 <= len(self.map) - 1
            middleRow.append(self.map[x][y + 1].__class__.__name__)
        else:
            middleRow.append(None)

        adjacentTiles.append(middleRow)

        # bottom row
        bottomRow = []

        # left
        if (self.can_go(x + 1, y - 1)): # and x + 1 <= len(self.map[0]) - 1 and y - 1 >= 0
            bottomRow.append(self.map[x + 1][y - 1].__class__.__name__)
        else:
            bottomRow.append(None)

        # middle (current location)
        if (self.can_go(x + 1, y)): # and (x + 1 <= len(self.map[0]) - 1)
            bottomRow.append(self.map[x + 1][y].__class__.__name__)
        else:
            bottomRow.append(None)

        # right
        if (self.can_go(x + 1, y + 1)): # and x + 1 <= len(self.map[0]) - 1 and y + 1 <= len(self.map[0]) - 1
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

def get_world():
    world_list = []
    for indexX, row in enumerate(Maps[current_map]):
        row_list = []
        for indexY, entry in enumerate(row):
            if (Maps[current_map][indexX][indexY] is not None):
                if (Maps[current_map][indexX][indexY] == "Start"):
                    row_list.append(Start(indexX, indexY))
                elif (Maps[current_map][indexX][indexY] == "Path"):
                    row_list.append(Path(indexX, indexY))
                elif (Maps[current_map][indexX][indexY] == "BanditLoot"):
                    row_list.append(BanditLoot(indexX, indexY))
                elif (Maps[current_map][indexX][indexY] == "Enemies"):
                    row_list.append(Enemies(indexX, indexY))
            else:
                row_list.append(None)
        world_list.append(row_list)
    return World(world_list)
