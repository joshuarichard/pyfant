import sys
import os
import cPickle as pickle
from modules.character import Character
from modules.item import Item, Weapon, Food
from modules.generate import generateItem
from modules.world import getWorld
from random import randint
from time import sleep

# TODO bigger picture
# ===================
# more Maps (bigger maps)
# more items
# monsters (and combat...)
#   - critical hits (combat...)
# chest traps
#   - drink alchohol to get stronger but more vulnerable to critical attacks
# big city
#   - buy/sell in big city

character = None
world = None

def startup():
    global world
    print("===================================================================")
    print("Welcome to your new great adventure in the land of Pyfant!!!!!!")
    print("Type in \"clear\" or \"help\" at any time.")

    world = getWorld()

    while True:
        choice = raw_input("Would you like to start a new game (N) or load an old game? (L) [N/L]? : ")
        if choice in ["N", "L", "n", "l", "help", "clear"]:
            break

    if(choice == "N" or choice == "n"):
        newGame()
    elif (choice == "L" or choice == "l"):
        loadGame()
    elif (choice == "clear"):
        os.system("clear")
        startup()

def newGame():
    global character
    character_name = raw_input("What's your character's name? : ")

    while True:
        character_class = raw_input("Would you like to be a fighter (F) or an archer? (A) [F/A]? : ")
        if character_class in ["F", "A", "f", "a"]:
            break

    if(character_class == "F" or character_class == "f"):
        character_class = "fighter"
    elif(character_class == "A" or character_class == "a"):
        character_class = "archer"

    character = Character(character_name, character_class, world.getStartingRoomLocation())

    print("Your new character has been created!")
    character.printStatus()
    character.printInventory()
    prompt()

def loadGame():
    global character
    load_path = raw_input("Where is your game saved? (just press enter to look for a save.pkl file in the current directory, or press C to cancel) : ")

    if(load_path == "C" or load_path == "c"):
        startup()

    if(load_path == ""):
        load_path = os.getcwd()

    if("/save.pkl" not in load_path):
        load_path = load_path + "/save.pkl"

    with open(load_path, "rb") as character_input:
        character = pickle.load(character_input)

    character_input.close()

    print("Character " + character.name + " (" + character.char_class +  ") loaded.")
    prompt()


def saveGame():
    save_path = raw_input("Where would you like to save the file? (just press enter to save in the current directory) : ")

    if(save_path == ""):
        save_path = os.getcwd()

    save_path = save_path + "/save.pkl"

    print("Character saved at " + save_path)
    with open(save_path, "wb") as output:
        pickle.dump(character, output)

    output.close()

    sys.exit()

def prompt():
    print("===================================================================")
    print("Main Menu:")
    print("What would you like to do?")

    while True:
        choice = raw_input("G) Go somewhere D) Do something L) Look around C) Check Character Q) Save and quit [G/D/L/C/Q] : ")
        if choice in ["G", "D", "L", "C", "Q", "g", "d", "l", "c", "q", "help", "clear"]:
            break

    if (choice == "G" or choice == "g"):
        moveCharacter()
    elif (choice == "D" or choice == "d"):
        doSomething()
    elif (choice == "L" or choice == "l"):
        print("")
        print("Current room: " + world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
        print("")
        print("Around you:")
        world.lookAtAdjacentTiles(character.currentLocation[0], character.currentLocation[1])
        print("")
        prompt()
    elif (choice == "C" or choice == "c"):
        checkCharacter()
    elif (choice == "Q" or choice == "q"):
        saveGame()
        print("Game saved.")
        sys.exit()
    elif (choice == "clear"):
        os.system("clear")
        prompt()

def moveCharacter():
    print("===================================================================")
    print("Which direction would you like to travel?")

    while True:
        choice = raw_input("U) Up D) Down L) Left R) Right C) Cancel [U/D/L/R/C] : ")
        if choice in ["U", "D", "L", "R", "C", "u", "d", "l", "r", "c", "help", "clear"]:
            break

    if (choice == "U" or choice == "u"):
        if (world.canGo(character.currentLocation[0] - 1, character.currentLocation[1])):
            character.currentLocation[0] = character.currentLocation[0] - 1
            print(world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
            prompt()
        else:
            noGo()
            moveCharacter()
    elif (choice == "D" or choice == "d"):
        if (world.canGo(character.currentLocation[0] + 1, character.currentLocation[1])):
            character.currentLocation[0] = character.currentLocation[0] + 1
            print(world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
            prompt()
        else:
            noGo()
            moveCharacter()
    elif (choice == "L" or choice == "l"):
        if (world.canGo(character.currentLocation[0], character.currentLocation[1] - 1)):
            character.currentLocation[1] = character.currentLocation[1] - 1
            print(world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
            prompt()
        else:
            noGo()
            moveCharacter()
    elif (choice == "R" or choice == "r"):
        if (world.canGo(character.currentLocation[0], character.currentLocation[1] + 1)):
            character.currentLocation[1] = character.currentLocation[1] + 1
            print(world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
            prompt()
        else:
            noGo()
            moveCharacter()
    elif (choice == "C" or choice == "c"):
        prompt()
    elif (choice == "clear"):
        os.system("clear")
        moveCharacter()

def noGo():
    print("It doesn't seem like you can go that way.")

def doSomething():
    print("===================================================================")
    print("What would you like to do?")

    while True:
        choice = raw_input("L) Look for a chest C) Cancel [L/C] : ")
        if choice in ["L", "C", "l", "c", "help", "clear"]:
            break

    if (choice == "L" or choice == "l"):
        if (hasattr(world.getTile(character.currentLocation[0], character.currentLocation[1]), "chest")):
            print("You're in luck, there is a chest in the room!")
            print("In the chest: ")
            chest = world.getTile(character.currentLocation[0], character.currentLocation[1]).chest
            for index, item in enumerate(chest.contents):
                print("======== " + str(index + 1) + " ========")
                item.printItem()

            print("Would you like to take any of the items?")

            while True:
                choice = raw_input("Item Index: [int] (press C to cancel) : ")
                if choice in ["C", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
                    break

            notThere = True
            try:
                item = chest.contents[int(choice) - 1]
                notThere = False
            except:
                notThere = True

            if (choice == "C" or choice == "c"):
                prompt()
            elif (notThere is False):
                if (chest.contents[int(choice) - 1] is not None):
                    result = character.addItemToInventory(chest.contents[int(choice) - 1])
                    if (result is True):
                        del chest.contents[int(choice) - 1]
                    doSomething()
            else:
                print("There is no item in the chest at that index.")
                doSomething()

        else:
            print("There's no chest in the room.")
            prompt()
    elif (choice == "C" or choice == "c"):
        prompt()
    elif (choice == "clear"):
        os.system("clear")
        doSomething()

def checkCharacter():
    print("===================================================================")
    print("Would you like to check your characters inventory or their levels?")

    while True:
        choice = raw_input("I) Inventory L) Levels E) Equip Item U) Unequip Item D) Drop Item H) Heal C) Cancel [I/L/E/U/D/H/C] : ")
        if choice in ["I", "L", "C", "E", "U", "D", "H", "i", "l", "e", "u", "d", "h", "c", "help", "clear"]:
            break

    # List inventory
    if (choice == "I" or choice == "i"):
        character.printInventory()
        checkCharacter()

    # List character levels
    elif (choice == "L" or choice == "l"):
        character.printStatus()
        checkCharacter()

    # Equip item
    elif (choice == "E" or choice == "e"):
        character.printInventory()
        print("Which item would you like to equip?")

        while True:
            choice = raw_input("Item Index [int] (press C to cancel) : ")
            if choice in ["C", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
                break

        notThere = True
        try:
            item = character.inventory[int(choice) - 1]
            notThere = False
        except:
            notThere = True

        if (choice == "C" or choice == "c"):
            prompt()
        elif (notThere is False):
            character.equipItem(int(choice) - 1)
            checkCharacter()
        else:
            print("There is no item at that index.")
            checkCharacter()

    # Unequip item
    elif (choice == "U" or choice == "u"):
        character.printInventory()
        print("Which slot would you like to unequip?")

        while True:
            choice = raw_input("Slot [sword/dagger/shield/bow/arrows/helmet/torso/leggings/boots] (press C to cancel) : ")
            if choice in ["sword", "dagger", "shield", "bow", "arrows", "helmet", "torso", "leggings", "boots", "C", "c"]:
                break

        if (choice == "C" or choice == "c"):
            prompt()
        else:
            character.unequipItem(choice)
            checkCharacter()

    # Cancel
    elif (choice == "C" or choice == "c"):
        prompt()

    # Drop item
    elif (choice == "D" or choice == "d"):
        character.printInventory()
        print("Which item would you like to drop?")

        while True:
            choice = raw_input("Item Index [int] (press C to cancel) : ")
            if choice in ["C", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
                break

        notThere = True
        try:
            item = chest.contents[int(choice) - 1]
            notThere = False
        except:
            notThere = True

        if (choice == "C" or choice == "c"):
            prompt()
        elif (notThere is False):
            if (character.inventory[int(choice) - 1] is not None):
                character.dropItemFromInventory(int(choice) - 1)
                checkCharacter()
        else:
            print("There is no item at that index.")
            checkCharacter()

    # Heal
    elif (choice == "H" or choice == "h"):
        character.printInventory()
        print("Which item would you like to consume?")

        while True:
            choice = raw_input("Item Index [int] (press C to cancel) : ")
            if choice in ["C", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
                break

        if (choice == "C" or choice == "c"):
            prompt()
        elif (character.inventory[int(choice) - 1] is not None):
            character.heal(int(choice) - 1)
            checkCharacter()
        else:
            print("There is no item at that index.")
            checkCharacter()

    # Clear
    elif (choice == "clear"):
        os.system("clear")
        checkCharacter()

if __name__ == "__main__":
    startup()
