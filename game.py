import sys
import os
import cPickle as pickle
import getopt
from random import randint
from time import sleep

from modules.character import Character
from modules.item import Item, Weapon, Food
from modules.generate import generate_enemy
from modules.world import get_world

# pylint: disable=C0301

# todo = bigger picture
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

def usage():
    print "usage: game.py --autoload"
    sys.exit(2)

def print_help():
    print "Help"

def startup():
    global world

    world = get_world()

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'a:h', ['autoload', 'help'])
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ('-a', '--autoload'):
            print "==================================================================="
            print "Welcome to your new great adventure in the land of Pyfant!!!!!!"
            print "Type in \"clear\" or \"help\" at any time."
            print "Autoloading character..."
            load_game(False)
        else:
            usage()

    print "==================================================================="
    print "Welcome to your new great adventure in the land of Pyfant!!!!!!"
    print "Type in \"clear\" or \"help\" at any time."

    while True:
        choice = raw_input("Would you like to start a new game (N) or load an old game? (L) [N/L]? : ")
        choice = choice.lower()
        if choice in ("n", "l", "help", "clear"):
            break

    if choice in "n":
        new_game()
    elif choice in "l":
        load_game(True)
    elif choice in "help":
        print_help()
        startup()
    elif choice in "clear":
        os.system("clear")
        startup()

def new_game():
    global character
    character_name = raw_input("What's your character's name? : ")

    while True:
        character_class = raw_input("Would you like to be a fighter (F) or an archer? (A) [F/A]? : ")
        character_class = character_class.lower()
        if character_class in ("f", "a"):
            break

    if character_class in "f":
        character_class = "fighter"
    elif character_class in "a":
        character_class = "archer"

    character = Character(character_name, character_class, world.get_starting_room_location())

    print "Your new character has been created!"
    character.print_status()
    character.print_inventory()
    prompt()

def load_game(ask):
    global character

    load_path = ""

    if ask is True:
        load_path = raw_input("Where is your game saved? (just press enter to look for a save.pkl file in the current directory, or press C to cancel) : ")

    if load_path in ("C", "c"):
        startup()

    if load_path == "":
        load_path = os.getcwd()

    if "/save.pkl" not in load_path:
        load_path = load_path + "/save.pkl"

    try:
        with open(load_path, "rb") as character_input:
            character = pickle.load(character_input)
    except:
        print "Error accessing your save file. Is the file there?"
        sys.exit(2)

    character_input.close()

    print "Character " + character.name + " (" + character.char_class +  ") loaded."
    prompt()


def save_game():
    save_path = raw_input("Where would you like to save the file? (just press enter to save in the current directory) : ")

    if save_path == "":
        save_path = os.getcwd()

    save_path = save_path + "/save.pkl"

    print "Character saved at " + save_path
    with open(save_path, "wb") as output:
        pickle.dump(character, output)

    output.close()

    sys.exit(2)

def prompt():
    print "==================================================================="
    print "Main Menu:"
    print "What would you like to do?"

    while True:
        choice = raw_input("G) Go somewhere D) Do something L) Look around C) Check Character Q) Save and quit [G/D/L/C/Q] : ")
        choice = choice.lower()
        if choice in ["g", "d", "l", "c", "q", "help", "clear"]:
            break

    if choice in "g":
        move_character()
    elif choice in "d":
        do_something()
    elif choice in "l":
        print ""
        print "Current room: " + world.get_tile(character.currentLocation[0], character.currentLocation[1]).description
        print ""
        print "Around you:"
        world.look_at_adjacent_tiles(character.currentLocation[0], character.currentLocation[1])
        print ""
        prompt()
    elif choice in "c":
        check_character()
    elif choice in "q":
        save_game()
        print "Game saved."
        sys.exit(2)
    elif choice in "clear":
        os.system("clear")
        prompt()

def move_character():
    print "==================================================================="
    print "Which direction would you like to travel?"

    while True:
        choice = raw_input("U) Up D) Down L) Left R) Right C) Cancel [U/D/L/R/C] : ")
        choice = choice.lower()
        if choice in ("u", "d", "l", "r", "c", "help", "clear"):
            break

    if choice in "u":
        if world.can_go(character.currentLocation[0] - 1, character.currentLocation[1]):
            character.move(character.currentLocation[0] - 1, character.currentLocation[1])
            print world.get_tile(character.currentLocation[0], character.currentLocation[1]).description
            prompt()
        else:
            print "It doesn't seem like you can go that way."
            move_character()
    elif choice in "d":
        if world.can_go(character.currentLocation[0] + 1, character.currentLocation[1]):
            character.move(character.currentLocation[0] + 1, character.currentLocation[1])
            print world.get_tile(character.currentLocation[0], character.currentLocation[1]).description
            prompt()
        else:
            print "It doesn't seem like you can go that way."
            move_character()
    elif choice in "l":
        if world.can_go(character.currentLocation[0], character.currentLocation[1] - 1):
            character.move(character.currentLocation[0], character.currentLocation[1] - 1)
            print world.get_tile(character.currentLocation[0], character.currentLocation[1]).description
            prompt()
        else:
            print "It doesn't seem like you can go that way."
            move_character()
    elif choice in "r":
        if world.can_go(character.currentLocation[0], character.currentLocation[1] + 1):
            character.move(character.currentLocation[0], character.currentLocation[1] + 1)
            print world.get_tile(character.currentLocation[0], character.currentLocation[1]).description
            prompt()
        else:
            print "It doesn't seem like you can go that way."
            move_character()
    elif choice in "c":
        prompt()
    elif choice in "clear":
        os.system("clear")
        move_character()

def do_something():
    print "==================================================================="
    print "What would you like to do?"

    while True:
        choice = raw_input("L) Look for a chest F) Fight an Enemy C) Cancel [L/F/C] : ")
        choice = choice.lower()
        if choice in ("l", "c", "f", "help", "clear"):
            break

    are_enemies = True

    if choice in "l":
        if hasattr(world.get_tile(character.currentLocation[0], character.currentLocation[1]), "enemies"):
            if world.get_tile(character.currentLocation[0], character.currentLocation[1]).killed_all_enemies is True:
                room = world.get_tile(character.currentLocation[0], character.currentLocation[1])
                are_enemies = False
        else:
            are_enemies = False

        if are_enemies is False:
            if hasattr(world.get_tile(character.currentLocation[0], character.currentLocation[1]), "chest"):
                print "You're in luck, there is a chest in the room!"
                print "In the chest: "
                chest = world.get_tile(character.currentLocation[0], character.currentLocation[1]).chest
                for index, item in enumerate(chest.contents):
                    print "======== " + str(index + 1) + " ========"
                    item.print_item()

                print "Would you like to take any of the items?"

                while True:
                    choice = raw_input("Item Index: [int] (press C to cancel) : ")
                    if choice in ("C", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"):
                        break

                not_there = True
                try:
                    item = chest.contents[int(choice) - 1]
                    not_there = False
                except:
                    not_there = True

                if choice in ("C", "c"):
                    prompt()
                elif not_there is False:
                    if chest.contents[int(choice) - 1] is not None:
                        result = character.add_item_to_inventory(chest.contents[int(choice) - 1])
                        if result is True:
                            del chest.contents[int(choice) - 1]
                        do_something()
                else:
                    print "There is no item in the chest at that index."
                    do_something()
            else:
                print "There's no chest in the room."
                prompt()
        else:
            print "You must clear out the enemies in the room before you look for a chest."
            do_something()
    elif choice in "f":
        if hasattr(world.get_tile(character.currentLocation[0], character.currentLocation[1]), "enemies"):
            room = world.get_tile(character.currentLocation[0], character.currentLocation[1])

            if room.killed_all_enemies is False and not room.enemies:
                num_of_enemies = randint(1, 1)

                for n in range(0, num_of_enemies):
                    room.add_enemy(generate_enemy(character.level))

            character.print_status()
            room.print_enemies()

            print "Which enemy do you want to attack?"
            while True:
                choice = raw_input("Enemy Index [int] (press C to cancel) : ")
                if choice in ("C", "c", "1", "2", "3", "4"):
                    break

            not_there = True
            try:
                item = room.enemies[int(choice) - 1]
                not_there = False
            except:
                not_there = True

            if choice in ("C", "c"):
                prompt()
            elif not_there is False:
                while True:
                    weapon = raw_input("Slot [sword/dagger/bow] (press C to cancel) : ")
                    weapon = weapon.lower()
                    if weapon in ("sword", "dagger", "bow", "c"):
                        break

                if weapon in "sword":
                    hits = character.fight(room.enemies[int(choice) - 1], "sword")
                    room.enemies[int(choice) - 1].hp = room.enemies[int(choice) - 1].hp - hits[0]
                    character.hp = character.hp - hits[1]
                    check_if_dead()
                    if room.enemies[int(choice) - 1].hp <= 0:
                        print "You killed " + room.enemies[int(choice) - 1].name + "!"
                        del room.enemies[int(choice) - 1]
                        character.add_xp(2)
                        if not room.enemies:
                            room.killed_all_enemies = True

                elif weapon in "dagger":
                    hits = character.fight(room.enemies[int(choice) - 1], "dagger")
                    room.enemies[int(choice) - 1].hp = room.enemies[int(choice) - 1].hp - hits[0]
                    character.hp = character.hp - hits[1]
                    check_if_dead()
                    if room.enemies[int(choice) - 1].hp <= 0:
                        print "You killed " + room.enemies[int(choice) - 1].name + "!"
                        del room.enemies[int(choice) - 1]
                        character.add_xp(2)
                        if not room.enemies:
                            room.killed_all_enemies = True

                elif weapon in "bow":
                    hits = character.fight(room.enemies[int(choice) - 1], "bow")
                    room.enemies[int(choice) - 1].hp = room.enemies[int(choice) - 1].hp - hits[0]
                    character.hp = character.hp - hits[1]
                    check_if_dead()
                    if room.enemies[int(choice) - 1].hp <= 0:
                        print "You killed " + room.enemies[int(choice) - 1].name + "!"
                        del room.enemies[int(choice) - 1]
                        character.add_xp(2)
                        if not room.enemies:
                            room.killed_all_enemies = True

                elif weapon in "c":
                    do_something()

                do_something()
            else:
                print "There is no enemy at that index."
                do_something()

        else:
            print "There are no enemies in the room."
            prompt()
    elif choice in ("C", "c"):
        prompt()
    elif choice in "help":
        print_help()
    elif choice in "clear":
        os.system("clear")
        do_something()

def check_character():
    print "==================================================================="
    print "Would you like to check your characters inventory or their levels?"

    while True:
        choice = raw_input("I) Inventory L) Levels E) Equip Item U) Unequip Item D) Drop Item H) Heal C) Cancel [I/L/E/U/D/H/C] : ")
        choice = choice.lower()
        if choice in ("i", "l", "e", "u", "d", "h", "c", "help", "clear"):
            break

    # List inventory
    if choice in "i":
        character.print_inventory()
        check_character()

    # List character levels
    elif choice in "l":
        character.print_status()
        check_character()

    # Equip item
    elif choice in "e":
        character.print_inventory()
        print "Which item would you like to equip?"

        while True:
            choice = raw_input("Item Index [int] (press C to cancel) : ")
            if choice in ("C", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"):
                break

        not_there = True
        try:
            item = character.inventory[int(choice) - 1]
            not_there = False
        except:
            not_there = True

        if choice in ("C", "c"):
            prompt()
        elif not_there is False:
            character.equip_item(int(choice) - 1)
            check_character()
        else:
            print "There is no item at that index."
            check_character()

    # Unequip item
    elif choice in "u":
        character.print_inventory()
        print "Which slot would you like to unequip?"

        while True:
            choice = raw_input("Slot [sword/dagger/shield/bow/arrows/helmet/torso/leggings/boots] (press C to cancel) : ")
            if choice in ("sword", "dagger", "shield", "bow", "arrows", "helmet", "torso", "leggings", "boots", "C", "c"):
                break

        if choice in ("C", "c"):
            prompt()
        else:
            character.un_equip_item(choice)
            check_character()

    # Drop item
    elif choice in "d":
        character.print_inventory()
        print "Which item would you like to drop?"

        while True:
            choice = raw_input("Item Index [int] (press C to cancel) : ")
            if choice in ["C", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
                break

        not_there = True
        try:
            item = character.inventory[int(choice) - 1]
            not_there = False
        except:
            not_there = True

        if choice in ("C", "c"):
            prompt()
        elif not_there is False:
            if character.inventory[int(choice) - 1] is not None:
                character.drop_item_from_inventory(int(choice) - 1)
                check_character()
        else:
            print "There is no item at that index."
            check_character()

    # Heal
    elif choice in "h":
        character.print_inventory()
        print "Which item would you like to consume?"

        while True:
            choice = raw_input("Item Index [int] (press C to cancel) : ")
            if choice in ["C", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
                break

        if choice in ("C", "c"):
            prompt()
        elif character.inventory[int(choice) - 1] is not None:
            character.heal(int(choice) - 1)
            check_character()
        else:
            print "There is no item at that index."
            check_character()

    # Cancel
    elif choice in "c":
        prompt()

    # Help
    elif choice in "help":
        print_help()

    # Clear
    elif choice in "clear":
        os.system("clear")
        check_character()

# checks to see if the character is dead. if they are then calls dead()
def check_if_dead():
    if character.hp <= 0:
        dead()

# called if character dies. resets HP, deletes inventory and equipped and saves game.
def dead():
    print "You died!"
    print "Your game will be saved with full health."
    print "Everything you were holding has been deleted, and you have nothing equipped."
    print "But all your levels are the same. So that's great! You've been resurrected!"
    character.hp = character.maxhp
    character.inventory = []
    character.equipped = {
        "sword": None,
        "dagger": None,
        "shield": None,
        "bow": None,
        "arrows": None,
        "helmet": None,
        "torso": None,
        "leggings": None,
        "boots": None
    }
    save_game()

if __name__ == "__main__":
    startup()
