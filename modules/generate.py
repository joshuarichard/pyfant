from modules.item import Item, Weapon, Armour, Food, Drink
from modules.enemy import Enemy
from random import randint

def generate_item(level, item_type):
    if (item_type == "sword"):
        sword_material = ""
        if (level > 200):
            sword_material = "Steel"
        else:
            sword_material = "Iron"

        sword_types = {
            0: ["Shortsword", randint(4, 7), .80, .49, .28],
            1: ["Longsword", randint(6, 10), .48, .71, .49],
            2: ["Greatsword", randint(8, 14), .12, .52, .76]
        }
        sword_type = sword_types[randint(0,2)]

        return Weapon(sword_material + " " + sword_type[0], # name
               sword_type[1],                              # weight
               level * .5,                                # value
               level * sword_type[2],                      # pierce
               level * sword_type[3],                      # slash
               level * sword_type[4]                       # blunt
        )

    elif (item_type == "dagger"):
        sword_material = ""
        if (level > 200):
            sword_material = "Steel"
        else:
            sword_material = "Iron"

        sword_types = {
            0: ["Dagger", randint(1, 3), .91, .23, .07]
        }
        sword_type = sword_types[0]

        return Weapon(sword_material + " " + sword_type[0], # name
               sword_type[1],                              # weight
               level * .5,                                # value
               level * sword_type[2],                      # pierce
               level * sword_type[3],                      # slash
               level * sword_type[4]                       # blunt
        )

    elif (item_type == "bow"):
        bow_types = {
            0: ["Shortbow", randint(2, 5), .99, .02, .28],
            1: ["Longbow", randint(4, 8), 1.05, .06, .31]
        }
        bow_type = bow_types[randint(0,1)]

        return Weapon(bow_type[0],
                      bow_type[1],
                      level * .5,
                      level * bow_type[2],
                      level * bow_type[3],
                      level * bow_type[4]
        )

    elif (item_type == "arrows"):
        return Weapon("Arrows",
                      1,
                      level * .5,
                      level * 1.43,
                      level * .02,
                      level * .1
        )

    elif (item_type == "armour"):
        armour_material = ""
        if (level > 600):
            armour_material = "Steel"
        elif (400 > level and level > 50):
            armour_material = "Iron"
        elif (200 > level):
            armour_material = "Leather"

        armour_type = {
            0: ["Helmet", randint(1, 3), .69, .75, .17],
            1: ["Chainmail", randint(7, 10), .87, .63, .37],
            2: ["Platemail", randint(10, 18), .84, .96, .24],
            3: ["Gloves", randint(2, 5), .35, .58, .42],
            4: ["Leggings", randint(5, 13), .53, .29, .43],
            5: ["Boots", randint(3, 7), .34, .19, .13]
        }
        armour_type = armour_type[randint(0,5)]

        return Armour(armour_material + " " + armour_type[0], # name
               armour_type[1],                              # weight
               level * .50,                                # value
               level * armour_type[2],                      # pierce
               level * armour_type[3],                      # slash
               level * armour_type[4]                       # blunt
        )

    elif (item_type == "food"):
        food_types = {
            0: ["Bread", 1, 3, 20],
            1: ["Soup", .5, 5, 25],
            2: ["Cheese", .25, 5, 10],
            3: ["Tomato", .2, 1, 3],
            4: ["Lettuce", .3, 2, 5]
        }
        food_type = food_types[randint(0,4)]

        return Food(food_type[0],  # name
               food_type[1],       # weight
               food_type[2],       # value
               food_type[3]        # healing
        )

    elif (item_type == "drink"):
        drink_types = {
            0: ["Beer", 1, 5, 12, 20],
            1: ["Wine", .75, 8, 25, 40],
            2: ["Mead", 1.5, 6, 15, 32]
        }
        drink_type = drink_types[randint(0,2)]

        return Drink(drink_type[0],  # name
               drink_type[1],        # weight
               drink_type[2],        # value
               drink_type[3],        # healing
               drink_type[4]         # drunkLevel
        )

def generate_enemy(char_level):
    enemies = {
        0: ["Bandit Archer",  [.91, .08, .34], [.21, .16, .42], "A bandit archer who fires piercing arrows, while weak to sharp weapons."],
        1: ["Bandit Warrior", [.46, .73, .58], [.32, .27, .59], "Common bandit warrior. Drunk with a powerful swing. It's best to pierce or slash this warrior's armour."],
        2: ["Bandit Leader",  [.61, .65, .43], [.49, .37, .72], "Not your average bandit who is strong all around. No clear weakness."],
        3: ["Pack of Wolves", [.99, .32, .27], [.91, .11, .19], "A pack of wolves that pierces with it's teeth with enormous success. Weak to slashing."]
    }
    enemy = enemies[randint(0,3)]

    if (char_level >= 30):
        enemy_range_end = char_level + 6
        enemy_range_start = char_level - 1
    elif (char_level >= 20):
        enemy_range_end = char_level + 5
        enemy_range_start = char_level - 2
    elif (char_level >= 10):
        enemy_range_end = char_level + 3
        enemy_range_start = char_level - 3
    elif (char_level >= 5):
        enemy_range_end = char_level + 2
        enemy_range_start = char_level - 4
    else:
        enemy_range_end = char_level + 1
        enemy_range_start = 1

    enemy_level = randint(enemy_range_start, enemy_range_end)

    attack = [enemy[1][0] * (enemy_level * .2),   # piercing attack
              enemy[1][1] * (enemy_level * .2),   # slashing attack
              enemy[1][2] * (enemy_level * .2)]   # blunt attack

    defence = [enemy[2][0] * (enemy_level * .2),  # piercing defence
               enemy[2][1] * (enemy_level * .2),  # slashing defence
               enemy[2][2] * (enemy_level * .2)]  # blunt defence

    return Enemy(enemy[0],   # name
                 enemy_level, # level
                 attack,     # attack
                 defence,    # defence
                 enemy[3]    # description
    )
