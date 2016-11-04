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
# more Maps
# more items
# monsters (and combat...)
#   - critical hits (combat...)
# chest traps
# fix running off the map
# put items in bag from chests
# equip item ability
# unequip item
# eat food to heal
#   - drink alchohol to get stronger but more vulnerable to critical attacks
# big city
#   - buy/sell in big city

character = None
world = None

def startup():
    global world
    print("===================================================================")
    print("Welcome to your new great adventure in the land of Pyfant!!!!!!")

    world = getWorld()

    while True:
        choice = raw_input("Would you like to start a new game (N) or load an old game? (L) [N/L]? : ")
        if choice in ["N", "L", "n", "l"]:
            break

    if(choice == "N" or choice == "n"):
        print ("Starting a new game...")
        newGame()
    elif (choice == "L" or choice == "l"):
        loadGame()

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
    print("You are at location: " + str(character.currentLocation))
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

def prompt():
    print("===================================================================")
    print("Main Menu:")
    print("What would you like to do?")

    while True:
        choice = raw_input("G) Go Somewhere D) Do something L) Look around C) Check Character Q) Save and Quit [C/Q] : ")
        if choice in ["G", "D", "L", "C", "Q", "g", "d", "l", "c", "q"]:
            break

    if(choice == "G" or choice == "g"):
        moveCharacter()
    elif(choice == "D" or choice == "d"):
        doSomething()
    elif(choice == "L" or choice == "l"):
        print(world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
        prompt()
    elif(choice == "C" or choice == "c"):
        checkCharacter()
    elif(choice == "Q" or choice == "q"):
        print("Hold on - saving the game...")
        saveGame()
        print("Game saved.")
        sys.exit()

def moveCharacter():
    # TODO NEED TO FIX - GOING OFF THE MAP (catch if off map and say can't go there)
    print("===================================================================")
    print("Which direction would you like to travel?")

    while True:
        choice = raw_input("N) North S) South W) West E) East C) Cancel [N/S/W/E/C] : ")
        if choice in ["N", "S", "W", "E", "C", "n", "s", "w", "e", "c"]:
            break

    if(choice == "N" or choice == "n"):
        if(world.canGo(character.currentLocation[0] - 1, character.currentLocation[1])):
            character.currentLocation[0] = character.currentLocation[0] - 1
            print(world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
            prompt()
        else:
            noGo()
            moveCharacter()
    elif(choice == "S" or choice == "s"):
        if(world.canGo(character.currentLocation[0] + 1, character.currentLocation[1])):
            character.currentLocation[0] = character.currentLocation[0] + 1
            print(world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
            prompt()
        else:
            noGo()
            moveCharacter()
    elif(choice == "W" or choice == "w"):
        if(world.canGo(character.currentLocation[0], character.currentLocation[1] - 1)):
            character.currentLocation[1] = character.currentLocation[1] - 1
            print(world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
            prompt()
        else:
            noGo()
            moveCharacter()
    elif(choice == "E" or choice == "e"):
        if(world.canGo(character.currentLocation[0], character.currentLocation[1] + 1)):
            character.currentLocation[1] = character.currentLocation[1] - 1
            print(world.getTile(character.currentLocation[0], character.currentLocation[1]).description)
            prompt()
        else:
            noGo()
            moveCharacter()
    elif(choice == "C" or choice == "c"):
        prompt()

def noGo():
    print("It doesn't seem like you can go that way.")

def doSomething():
    print("===================================================================")
    print("What would you like to do?")

    while True:
        choice = raw_input("C) Check for a chest [C] : ")
        if choice in ["C", "c"]:
            break

    if(choice == "C" or choice == "c"):
        if(hasattr(world.getTile(character.currentLocation[0], character.currentLocation[1]), "chest")):
            print("You're in luck, there is a chest in the room!")
            print("In the chest: ")
            chest = world.getTile(character.currentLocation[0], character.currentLocation[1]).chest
            for index, item in enumerate(chest.contents):
                print("======== " + str(index) + " ========")
                item.printItem()
                # TODO Can list items but now need to put them in your bag
            prompt()
            # continue process here....
        else:
            print("There's no chest in the room.")
            prompt()

def checkCharacter():
    print("===================================================================")
    print("Would you like to check your characters inventory or their levels?")

    while True:
        choice = raw_input("I) Inventory L) Levels C) Cancel [I/L/C] : ")
        if choice in ["I", "L", "C", "i", "l", "c"]:
            break

    if(choice == "I" or choice == "i"):
        character.printInventory()
        prompt()
    elif(choice == "L" or choice == "l"):
        character.printStatus()
        prompt()
    elif(choice == "C" or choice == "c"):
        prompt()

if __name__ == "__main__":
    startup()
