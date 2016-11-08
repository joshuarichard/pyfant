from item import Item, Weapon, Armour, Food, Drink
from enemy import Enemy
from random import randint

def generateItem(level, itemType):
    if (itemType == "sword"):
        swordMaterial = ""
        if (level > 150):
            swordMaterial = "Steel"
        else:
            swordMaterial = "Iron"

        swordTypes = {
            0: ["Shortsword", randint(4, 7), .80, .49, .28],
            1: ["Longsword", randint(6, 10), .48, .71, .49],
            2: ["Greatsword", randint(8, 14), .12, .52, .76],
            3: ["Dagger", randint(1, 3), .91, .23, .07]
        }
        swordType = swordTypes[randint(0,2)]

        return Weapon(swordMaterial + " " + swordType[0], # name
               swordType[1],                              # weight
               level * .5,                               # value
               level * swordType[2],                      # pierce
               level * swordType[3],                      # slash
               level * swordType[4]                       # blunt
        )

    elif (itemType == "bow"):
        bowTypes = {
            0: ["Shortbow", randint(2, 5), .99, .02, .28],
            1: ["Longbow", randint(4, 8), 1.05, .06, .31]
        }
        bowType = bowTypes[randint(0,1)]

        return Weapon(bowType[0],
                      bowType[1],
                      level * .5,
                      level * bowType[2],
                      level * bowType[3],
                      level * bowType[4]
        )

    elif (itemType == "armour"):
        armourMaterial = ""
        if (level > 200):
            armourMaterial = "Steel"
        elif (200 > level and level > 50):
            armourMaterial = "Iron"
        elif (50 > level):
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

    elif (itemType == "food"):
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

    elif (itemType == "drink"):
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

def generateEnemy(char_level):
    enemies = {
        0: ["Bandit Archer",  [.91, .08, .34], [.21, .16, .42], "A bandit archer who fires piercing arrows, while weak to sharp weapons."],
        1: ["Bandit Warrior", [.46, .73, .58], [.32, .27, .59], "Common bandit warrior. Drunk with a powerful swing. It's best to pierce or slash this warrior's armour."],
        2: ["Bandit Leader",  [.61, .65, .43], [.49, .37, .72], "Not your average bandit who is strong all around. No clear weakness."],
        3: ["Pack of Wolves", [.99, .32, .27], [.91, .11, .19], "A pack of wolves that pierces with it's teeth with enormous success. Weak to slashing."]
    }
    enemy = enemies[randint(0,3)]

    if (char_level >= 30):
        enemyRangeEnd = char_level + 7
        enemyRangeStart = char_level - 1
    elif (char_level >= 20):
        enemyRangeEnd = char_level + 5
        enemyRangeStart = char_level - 2
    elif (char_level >= 10):
        enemyRangeEnd = char_level + 3
        enemyRangeStart = char_level - 3
    elif (char_level >= 5):
        enemyRangeEnd = char_level + 2
        enemyRangeStart = char_level - 4
    else:
        enemyRangeEnd = char_level + 1
        enemyRangeStart = 1

    enemyLevel = randint(enemyRangeStart, enemyRangeEnd)

    attack = [enemy[1][0] * enemyLevel,   # piercing attack
              enemy[1][1] * enemyLevel,   # slashing attack
              enemy[1][2] * enemyLevel]   # blunt attack

    defence = [enemy[2][0] * enemyLevel,  # piercing defence
               enemy[2][1] * enemyLevel,  # slashing defence
               enemy[2][2] * enemyLevel]  # blunt defence

    return Enemy(enemy[0],   # name
                 enemyLevel, # level
                 attack,     # attack
                 defence,    # defence
                 enemy[3]    # description
    )
