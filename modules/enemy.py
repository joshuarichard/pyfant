from random import randint

class Enemy(object):
    def __init__(self, name, level, attack, defence, description):
        self.name = name
        self.level = level
        self.maxhp = level * 120
        self.hp = self.maxhp
        self.description = description
        self.a_piercing = attack[0] * 110
        self.a_slashing = attack[1] * 110
        self.a_blunt = attack[2] * 110
        self.d_piercing = defence[0]
        self.d_slashing = defence[1]
        self.d_blunt = defence[2]

#bossTypes: {
#    0: "Dragon",
#    1: "Cave Giant",
#    2: "Goblin Leader",
#    3: "Basilisk"
#}

#monsterTypes = {
#    0: "Skeleton Warrior",
#    1: "Skeleton Archer",
#    2: "Skeleton Chief",
#    3: "Werewolf",
#    4: "Goblin Warrior",
#    5: "Goblin Archer",
#    6: "Goblin Chief",
#    7: "Ghoul",
#    8: "Manticore",
#    9: "Orc Warrior",
#    10: "Orc Chief",
#    11: "Troll",
#    12: "",
#    13: ""
#}
