import json
import time
import random
import hashlib
import os
import sys
import shutil
from rich.console import Console
from rich.theme import Theme
from rich.progress import track
from rich import print

# temp variables
temp = 0
temp0 = 0
temp1 = 0
temp2 = 0

# important playerVariables
steps = 0
stepBooster = 1
tempStep = 0

money = 0
level = 1

ownedItems = []
equippedItem = 0
namesOfOwnedWeapons = []


class Item:
    pass


def SAVE():
    global steps
    global money
    global level
    global ownedItems
    global equippedItem
    json.dump(steps, open('.GAMEDATA/SAVE/playerSteps.json', 'w'))
    json.dump(money, open('.GAMEDATA/SAVE/playerMoney.json', 'w'))
    json.dump(level, open('.GAMEDATA/SAVE/playerLevel.json', 'w'))
    json.dump(ownedItems, open(".GAMEDATA/USER/ownedItems.json", "w"))
    json.dump(equippedItem, open('.GAMEDATA/USER/equippedItem.json', 'w'))


def LOAD():
    global steps
    global money
    global level
    global ownedItems
    global equippedItem
    steps = json.load(open('.GAMEDATA/SAVE/playerSteps.json', 'r'))
    money = json.load(open('.GAMEDATA/SAVE/playerMoney.json', 'r'))
    level = json.load(open('.GAMEDATA/SAVE/playerLevel.json', 'r'))
    ownedItems = json.load(open(".GAMEDATA/USER/ownedItems.json", "r"))
    equippedItem = json.load(open('.GAMEDATA/USER/equippedItem.json', 'r'))


# weapon information
weapon = Item()
weapon.name = ["THE CREATOR'S MIGHT",  # 1
               "FILIP'S FIST",  # 2
               "KARA|THE SWORD THAT KNOWS",  # 3
               "SARAH'S RAINBOW SWORD OF KINDNESS",  # 4
               "PSYCHO|THE CAT GOD",  # 5
               "NEDAS' WHITE CHICKEN",  # 6
               "Taser",  # 7
               "Ancient sword",  # 8
               "Narf blaster",  # 9
               "Blinding torch",  # 10
               "Baseball bat",  # 11
               "Nerf blaster",  # 12
               ]

weapon.power = [10000,  # 1
                9000,  # 2
                9000,  # 3
                8500,  # 4
                7500,  # 5
                7000,  # 6
                15,  # 7
                50,  # 8
                20,  # 9
                70,  # 10
                75,  # 11
                100,  # 12
                ]

# when price is 0 a galaxy is shown instead of cash(In inventory)
weapon.price = [0,  # 1
                0,  # 2
                0,  # 3
                0,  # 4
                0,  # 5
                0,  # 6
                25,  # 7
                85,  # 8
                30,  # 9
                100,  # 10
                125,  # 11
                175  # 12
                ]

weapon.rarityOfItem = [8,  # 1
                       8,  # 2
                       8,  # 3
                       8,  # 4
                       8,  # 5
                       8,  # 6
                       0,  # 7
                       0,  # 8
                       0,  # 9
                       1,  # 10
                       1,  # 11
                       1,  # 12
                       ]

weapon.rarities = [0, 1, 3, 4, 5, 6, 7, 8]
rarityTypes = ["Common", "[#878787]Uncommon", "[#3c4ed6]Decent", "[#9e159a]Epic", "[#f59d31]Legendary",
               "[#b31e1e]Elite", "[#00e394]EXOTIC", "[#26e9ff]CELESTIAL", "[#edd12f]GODLY"]

firstLogin = False
jobDone = False

# creates some rich colours
colourTheme = Theme({"textscene": 'bold', "error": "bold red"})
c = Console(theme=colourTheme)

if not os.path.exists('GAMEFILES/TerminalVersion.json'):
    print("Hello person, are you using windows cmd or the microsoft store terminal?")
    time.sleep(1)
    while True:
        temp0 = input("Write which one you have, from the brackets(cmd, terminal)...").strip().lower()
        if temp0 == "cmd":
            print("The cmd will make the game experience horrible, bad colours incorrect formatting. And more...")
            time.sleep(1.5)
            print("Please go follow this link: https://www.youtube.com/watch?v=pcte_ecqoLI")
            time.sleep(0.5)
            print("It will show you how to properly download the game.")
            time.sleep(0.5)
            input("Continue...")
            exit("Incorrect terminal version!")
        if temp0 == "terminal":
            json.dump(temp0, open('GAMEFILES/TerminalVersion.json', 'w'))
            print("Ok cool, let the adventure begin...\n")
            time.sleep(0.5)
            break

        else:
            print("Invalid input!")
            time.sleep(0.5)
            continue

# checks if login files exist
if not os.path.exists('GAMEFILES'):
    c.print("Oops, your game files are deleted. Go onto my github and download them.", style="error")
    time.sleep(3)
    exit()
    # starts first login process
if not os.path.exists('.GAMEDATA'):

    firstLogin = True
    os.makedirs('.GAMEDATA')
    if not os.path.exists('.GAMEDATA/SAVE'):
        os.makedirs('.GAMEDATA/SAVE')
    if not os.path.exists('.GAMEDATA/USER'):
        os.makedirs('.GAMEDATA/USER')

    # all save files are created
    SAVE()
    LOAD()

    c.print("Once upon a time, there was a developer.", style="textscene")
    time.sleep(1)
    c.print("He was bored.", style="textscene")
    time.sleep(0.7)
    c.print("So he decided to create a world, in which there were animals and life.", style="textscene")
    time.sleep(2.5)
    c.print("And you!", style="textscene")
    time.sleep(0.5)
    username = input("Enter a username:").strip()

    # checks username formatting
    while username == "":
        c.print("Please enter a username...", style="error")
        username = input("Enter a username...")
    while len(username) > 20:
        username = input("Please enter a shorter username...")

    line_number = 0
    # opens the file in read only mode
    with open('GAMEFILES/Names.txt', 'r') as read:
        # reads all lines in the file one by one
        for line in read.readlines():
            # for each line, check if line contains the string
            line_number += 1
            if username.strip().capitalize() in line:
                c.print("Are you sure you want to use your real name?", style="error")
                temp = input("(y, n)...")
                if temp == "y":
                    break
                else:
                    username = input("Enter your username again...")

    username = username.strip()

    # welcomes user and dumps username
    json.dump(username, open('.GAMEDATA/USER/username.json', 'w'))
    print(f"Welcome to PyMMo [bold]{username}[/], you are very lucky to be here!")
    time.sleep(1)

    # password
    while True:
        password = input("Enter your password(remember it!)...")
        temp1 = input("Do you want this password?(y, n)...")
        if temp1 == "y":
            break
        else:
            continue
    string = hashlib.sha256(password.encode())
    string_hex = string.hexdigest()
    json.dump(string_hex, open('.GAMEDATA/USER/pass.json', 'w'))

    string_hex = json.load(open('.GAMEDATA/USER/pass.json', 'r'))

    passCheck = input("Enter again:")

    string2 = hashlib.sha256(passCheck.encode())
    temp_hex = string2.hexdigest()

    while temp_hex != string_hex:
        passCheck = input("Try again(Check password from older inputs)!..")
        temp = hashlib.sha256(passCheck.encode())
        temp_hex = temp.hexdigest()
    else:
        print("\nPassword created!\nYou have been logged in.\n")
        print(f"Your account hex is [red]{temp_hex}[/].")

if not firstLogin:

    money = 0
    level = 1

    # checks if login files exist
    try:
        json.load(open('.GAMEDATA/USER/username.json', 'r'))
        json.load(open('.GAMEDATA/USER/pass.json', 'r'))
    except FileNotFoundError:
        c.print("CRITICAL ERROR... Login files have been deleted!", style="red")
        time.sleep(2)
        exit()

    # loads all other files
    try:
        steps = json.load(open('.GAMEDATA/SAVE/playerSteps.json', 'r'))
        money = json.load(open('.GAMEDATA/SAVE/playerMoney.json', 'r'))
        level = json.load(open('.GAMEDATA/SAVE/playerLevel.json', 'r'))
        ownedItems = json.load(open(".GAMEDATA/USER/ownedItems.json", "r"))
    except FileNotFoundError:
        c.print("One or more of your save files have been deleted! New ones were created."
                "\nCheck your recycle bin and drag them back to .GAMEDATA/SAVE", style="error")
        # creates new game files and loads them
        SAVE()
        LOAD()

        # imports username and pass hex
    username = json.load(open('.GAMEDATA/USER/username.json', 'r'))
    string_hex = json.load(open('.GAMEDATA/USER/pass.json', 'r'))

    passCheck = input("Enter your password...")
    string2 = hashlib.sha256(passCheck.encode())
    temp_hex = string2.hexdigest()

    while temp_hex != string_hex:
        passCheck = input("Try again!:")
        temp = hashlib.sha256(passCheck.encode())
        temp_hex = temp.hexdigest()
    else:
        print(f"\nCorrect password!\nWelcome back to PyMMo, [bold]{username}[/]!\n")
        print(f"Your account hex is [red]{temp_hex}[/].\n\n")
        time.sleep(0.2)

    print(f"Hi, [bold]{username}[/]. What will you do today?")

    # game loop
    while True:
        print(f"\nYou are currently level {level} and have [green]${money}[/].")
        print(f"You have took {steps} steps.")
        print("-----------------------------\n")
        print("[bold blue]-Step(s)      [dim white]Stats(st)[/]\n"
              "[bold blue]-Pvp(p)       [dim white]Settings(/s)[/]\n"
              "[bold green]-Town(t)[/]\n"
              "[white]-Inventory(i)\n"
              "\n"
              "[dim red]-Or exit game(/)")

        temp1 = input("...").strip().lower()
        if temp1 == "":
            c.print("\nplease enter something...\n", style="error")
            time.sleep(0.2)

        # stepping
        elif temp1 == "s":
            c.print("\nNot done yet!\n", style="error")
            print("Press enter to take a step...")

            temp2 = 0  # number of steps to next level
            temp3 = 0  # number of times user pressed enter key
            toNextLevel = 100  # amount of steps to get to the next level
            while True:
                temp0 = input("...")
                tempNumStep = random.randint(1, 10)
                if temp0 == "":
                    temp3 += 1
                    if temp3 >= tempNumStep:
                        # checks if amount of steps increase level
                        if temp2 == toNextLevel:
                            level += 1
                            temp2 = 0
                            print(f"You are now on level {level}!")
                            SAVE()
                        else:
                            temp2 += 1
                        # adds one step and saves it, resets variables
                        tempNumStep = 0
                        temp3 = 0
                        steps += 1 * stepBooster
                        SAVE()
                        print(f"You have taken {steps} steps.")

                else:
                    if temp0 == "/":
                        break

        # pvp
        elif temp1 == "p":
            c.print("\nNot done yet!\n", style="error")
            time.sleep(0.2)

        # town
        elif temp1 == "t":
            while True:
                print("-----------------------------")
                c.print("\nBeware that the town is still under construction, some things have not been built yet.\n",
                        style="error")
                print("[bold blue]-Casino(c)[/]\n"
                      "[bold green]-Job(j)\n"
                      "-Shrine(s)[/]\n"
                      "\n"
                      "[dim red]-Or leave(/)")

                temp2 = input("...").strip().lower()
                if temp2 == "":
                    c.print("\nplease enter something...\n", style="error")
                    time.sleep(0.1)

                elif temp2 == "/":
                    break

                elif temp2 == "j":
                    print(f"\nYou currently have [green]${money}[/].")

                    while True:
                        LOAD()
                        if jobDone:
                            jobDone = "Another job?"
                        else:
                            jobDone = "Do job?"

                        if input(f"{jobDone}(y, n)...") == "y":
                            temp1 = input("\nHow long will the job be?(1min, 3min, 5min)...").strip()
                            if temp1 == "1min":
                                temp0 = 60  # money
                                temp2 = 1  # level
                                jobDone = True
                            elif temp1 == "3min":
                                temp0 = 180
                                temp2 = 3
                                jobDone = True
                            elif temp1 == "5min":
                                temp0 = 300
                                temp2 = 5
                            elif temp1 == "/":
                                break
                                jobDone = "Do job?"
                            else:
                                c.print("\nInvalid selection! You can also exit with / .\n", style="error")
                                jobDone = False
                                continue
                            print()

                            for step in track(range(temp0)):
                                time.sleep(1)
                            money = money + (temp0 * 2)
                            level = level + temp2
                            SAVE()
                            print(f"You now have [green]${money}[/].")
                            print()
                        else:
                            jobDone = False
                            break

                elif temp2 == "c":
                    print(f"Hello, [bold]{username}[/] welcome to the casino.")

                    while True:
                        print(f"\nYou have [green]${money}[/] to spend.\n")
                        print(f"There are some games you could play:"
                              f"\n[white]-Double or nothing(1)[/]"
                              f"\n[white]-777 slot machine(2)[/]"
                              f"\n"
                              f"\n[dim red]-Or exit(/)")
                        choice = input("...")
                        if choice == "1":  # casino choose game
                            # Money half game
                            if money > 5:
                                print("You are now playing double or nothing.")
                                moneyFromGame = input("Enter amount of money to bet...")
                                while True:
                                    rand = random.randint(0, 1)
                                    if rand == 0:
                                        money = money + int(moneyFromGame) * 2
                                        print(f"You won! You now have [green]${money}[/].\n")
                                        SAVE()
                                        break

                                    elif rand == 1:
                                        c.print("You lost your money!", style="error")
                                        money = money - int(moneyFromGame)
                                        print(f"You now have [green]${money}[/].\n")
                                        SAVE()
                                        break

                            else:
                                print("Sorry you do not have enough money for this game.\n")
                                time.sleep(2)

                        elif choice == "2":
                            print("Game not finished! Sowy!")
                            slot1 = "$ $ $"
                            slot2 = "$ X $"
                            slot3 = "X X $"
                            slot4 = "$ X X"
                            slot5 = "X X X"
                            break

                        elif choice == "/":
                            break

                        else:
                            c.print("Invalid input!", style="error")
                            time.sleep(0.5)

        # inventory
        elif temp1 == "i":
            c.print("\nNot done yet!\n", style="error")

            while True:
                if len(ownedItems) == 0:  # Checks if there is anything to print
                    print("\nYou have no weapons.")
                    break

                num = 0
                try:
                    for weapons in ownedItems:
                        temp0 = [str(weapon.price[weapons]), "🌌"]
                        if weapon.price[weapons] == 0:  # infinite price checker
                            temp1 = 1
                        else:
                            temp1 = 0
                        print(f"{weapon.name[weapons]}: [red]{str(weapon.power[weapons])}[/]"
                              f"\n[green]${temp0[temp1]}[/]"
                              f"\n{rarityTypes[weapon.rarityOfItem[weapons]]}\n")
                        namesOfOwnedWeapons.append(weapon.name[num])
                        num += 1

                except IndexError:  # Just in case the file is corrupt
                    exit(".GAMEDATA/USER/ownedItems.json is out of range! Consider deleting the file.")

                itemSelected = ""
                temp2 = input("Select an item(Or exit /)...").strip()
                if temp2 in namesOfOwnedWeapons:
                    print("Exists.")
                    itemSelected = namesOfOwnedWeapons.index(temp2)
                    while True:
                        print(f"\nYou have selected {weapon.name[itemSelected]}.\n")
                        print("-Equip(e)"
                              "\n-Sell(s)"
                              "\n-Discard(d)"
                              "\n"
                              "\n-Or nothing(/)")
                        temp2 = input("...").strip().lower()
                        if temp2 == "":
                            print("\nEnter something!")
                        elif temp2 == "/":
                            break

                        elif temp2 == "e":
                            if equippedItem == itemSelected:
                                print("\nYou have already equipped this item!\n")
                                break
                            equippedItem = itemSelected
                            print(f"\n{weapon.name[itemSelected]} has been equipped.\n")
                            SAVE()
                            break

                        elif temp2 == "s":
                            if input(f"Are you sure you want to sell {weapon.name[itemSelected]}(y, n)?..") == "y":
                                print(
                                    f"{weapon.name[itemSelected]} has been sold for "
                                    f"[green]${weapon.price[itemSelected]}[/].")
                                money += weapon.price[itemSelected]
                                ownedItems.remove(itemSelected)
                                SAVE()
                                break

                        elif temp2 == "d":
                            if input(f"Are you sure you want to discard {weapon.name[itemSelected]}(y, n)?..") == "y":
                                print(f"{weapon.name[itemSelected]} has been discarded.")
                                ownedItems.remove(itemSelected)
                                SAVE()
                                break

                elif temp2 == "/":
                    break

                elif temp2 == "/dev":
                    c.print(f"Do not enter value higher than [bold red]{len(weapon.name) - 1}[/].\n", style="error")

                    while True:
                        if input("Add more numbers to list(y, n)?") == "y":
                            try:
                                tempNum1 = int(input("Enter number..."))
                                if len(weapon.name) - 1 >= tempNum1:  # Checks if number inputted is in range of list
                                    if input("More(y, n)?") == "y":
                                        ownedItems.append(tempNum1)
                                        with open(".GAMEDATA/USER/ownedItems.json", "w") as f:
                                            json.dump(ownedItems, f)
                                        continue

                                    else:
                                        ownedItems.append(tempNum1)
                                        with open(".GAMEDATA/USER/ownedItems.json", "w") as f:
                                            json.dump(ownedItems, f)
                                            print(f"\n")
                                            print(json.load(open('.GAMEDATA/USER/ownedItems.json', 'r')))
                                        break
                                else:
                                    c.print("Enter a number that is in range!\n", style="error")

                            except ValueError:
                                print("Enter a number!")
                                continue
                        else:
                            break

                    print(f"\n")

                    if len(ownedItems) == 0:  # Checks if there is anything to print
                        print("\nThere was nothing to print.")
                    try:
                        for num in ownedItems:
                            temp0 = [str(weapon.price[num]), "🌌"]
                            if weapon.price[num] == 0:
                                temp1 = 1
                            else:
                                temp1 = 0
                            print(f"{weapon.name[num]}: [red]{str(weapon.power[num])}[/]"
                                  f"\n[green]${temp0[temp1]}[/]"
                                  f"\n{rarityTypes[weapon.rarityOfItem[num]]}\n")

                    except IndexError:  # Just in case the file is corrupt
                        exit(".GAMEDATA/USER/ownedItems.json is out of range! Consider deleting the file.")

                else:
                    print("Does not exist!")

        # settings
        elif temp1 == "/s":
            while True:
                print("\n[white]-Change username(1)\n"
                      "[blink red]-Delete account(2)\n"
                      "\n"
                      "[dim red]-Or leave(/)")
                temp2 = input("...")
                if temp2 == "":
                    c.print("Please enter something...", style="error")

                elif temp2 == "1":
                    while True:
                        username = input("Enter a new username...")

                        while username == "":
                            username = input('Please enter "a" username...')
                        while len(username) > 20:
                            username = input("Please enter a shorter username...")

                        username = username.strip()

                        # welcomes user and dumps username
                        if username == json.load(open('.GAMEDATA/USER/username.json')):
                            json.dump(username, open('.GAMEDATA/USER/username.json', 'w'))
                            print("\nThat was already your username, anyway...")
                            time.sleep(1)
                            print(f"Your username is now {username}. Ok???")
                            time.sleep(0.5)
                            break
                        else:
                            json.dump(username, open('.GAMEDATA/USER/username.json', 'w'))
                            print(f"\nCool! [bold]{username}[/] is now your new username.")
                            break

                elif temp2 == "2":
                    c.print("This action is irreversible!", style="error")
                    time.sleep(0.5)
                    c.print("Type the words: [red]'DELETE ACCOUNT'[/] to confirm deletion. Caps sensitive!",
                            style="error")
                    time.sleep(0.5)
                    print("[white]Press / to exit if you changed your mind.")
                    temp = input("...").strip()
                    if temp == "DELETE ACCOUNT":
                        shutil.rmtree(".GAMEDATA")
                        c.print("Account deleted!", style="error")
                        print("Game will now close.")
                        input("Continue...")
                        exit("GAMEDATA deleted by user!")
                    else:
                        print("\nPussyo!\n")
                        time.sleep(0.5)
                        break

                elif temp2 == "/":
                    break

                else:
                    c.print("Invalid input!", style="error")

        # exits game and saves stuff
        elif temp1 == "/":
            while True:
                temp0 = 0
                temp0 = input("Are you sure(y, n)?..").lower()
                if temp0 == "y":
                    print(f"Ok bye, {username}!")
                    time.sleep(0.5)
                    exit("Player exited!")
                else:
                    print("Good that you decided to stay.\n")
                    time.sleep(1)
                    break

        else:
            c.print("\nInvalid selection!...\n", style="error")
            time.sleep(0.2)

else:
    c.print("\nNow the developer or you can call him the creator,", style="textscene")
    time.sleep(2)
    c.print("will take you through a tutorial.", style="textscene")
    time.sleep(1)
    while True:
        temp1 = input("Type w to start to go for a walk...")
        time.sleep(1)
        if temp1 == "w":
            break
        else:
            c.print("Please follow the tutorial.", style="error")
            time.sleep(1)
    c.print("\nOk nice, I did not think you had those capabilities!"
            "\nNow press enter to take steps...", style="textscene")

    while True:
        temp0 = input("...")
        tempNumStep = random.randint(1, 10)
        if temp0 == "":
            tempStep += 1
            if tempStep >= tempNumStep:
                tempNumStep = 0
                tempStep = 0
                steps += 1 * stepBooster
                print(f"You have taken {steps} steps.")
                SAVE()

                if steps == 50:
                    break

    json.dump(steps, open('.GAMEDATA/SAVE/playerSteps.json', 'w'))
    c.print("\nOk nice, you have now arrived in the +1 braincell universe!", style="textscene")
    time.sleep(2)
    c.print("JK but now,", style="textscene")
    time.sleep(0.5)
    c.print("you have finished the tutorial.", style="textscene")
    exit("Now type: .PyMMo.py to begin your adventure!")
