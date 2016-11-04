from item import Item, Weapon, Armour, Food, Drink
from random import randint

def generateItem(level, itemType):
    if(itemType == "sword"):
        swordMaterial = ""
        if(level > 150):
            swordMaterial = "Steel"
        else:
            swordMaterial = "Iron"

        swordTypes = {
            0: ["Shortsword", randint(4,7), .80, .49, .28],
            1: ["Longsword", randint(6, 10), .48, .71, .49],
            2: ["Greatsword", randint(8, 14), .12, .52, .76]
        }
        swordType = swordTypes[randint(0,2)]

        return Weapon(swordMaterial + " " + swordType[0], # name
               swordType[1],                              # weight
               level * .50,                               # value
               level * swordType[2],                      # pierce
               level * swordType[3],                      # slash
               level * swordType[4]                       # blunt
        )

    elif(itemType == "armour"):
        armourMaterial = ""
        if(level > 200):
            armourMaterial = "Steel"
        elif(200 > level and level > 50):
            armourMaterial = "Iron"
        elif(50 > level):
            armourMaterial = "Leather"

        armourType = {
            0: ["Helmet", randint(1, 3), .69, .75, .17],
            1: ["Chainmail", randint(7, 10), .87, .63, .37],
            2: ["Platemail", randint(10, 18), .84, .96, .24],
            3: ["Leggings", randint(5, 13), .53, .29, .43],
            4: ["Boots", randint(3, 7), .34, .19, .13]
        }
        armourType = armourType[randint(0,4)]

        return Armour(armourMaterial + " " + armourType[0], # name
               armourType[1],                              # weight
               level * .50,                                # value
               level * armourType[2],                      # pierce
               level * armourType[3],                      # slash
               level * armourType[4]                       # blunt
        )

    elif(itemType == "food"):
        foodType = {
            0: ["Bread", 1, 3, 20],
            1: ["Soup", .5, 5, 25],
            2: ["Cheese", .25, 5, 10],
            3: ["Tomato", .2, 1, 3],
            4: ["Lettuce", .3, 2, 5]
        }
        foodType = foodType[randint(0,4)]

        return Food(foodType[0],  # name
               foodType[1],       # weight
               foodType[2],       # value
               foodType[3]        # healing
        )

    elif(itemType == "drink"):
        drinkType = {
            0: ["Beer", 1, 5, 12, 20],
            1: ["Wine", .75, 8, 25, 40],
            2: ["Mead", 1.5, 6, 15, 32]
        }
        drinkType = drinkType[randint(0,2)]

        return Drink(drinkType[0],  # name
               drinkType[1],        # weight
               drinkType[2],        # value
               drinkType[3],        # healing
               drinkType[4]         # drunkLevel
        )
