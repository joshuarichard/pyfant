from classes import Item, Weapon
from random import randint

def generateSword(level):
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
