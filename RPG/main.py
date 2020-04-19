
import yaml
import random
from enemy import Enemy
from player import Player

PLAYER_DATA = "player_data.yaml"
ENEMIES_DATA = "enemies.yaml"


def get_data(filename):
    with open(filename, "r") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
    return data


def set_data(filename,data):
    with open(filename, "w") as f:
        yaml.dump(data,f,sort_keys=False)


def getPlayerData():
    return get_data(filename=PLAYER_DATA)


def setPlayerData(data):
    set_data(filename=PLAYER_DATA, data=data)


def getOppData():
    return get_data(ENEMIES_DATA)


def randVar():
    return random.randint(101)


def playerAtk(attack, oppDef):
    hitChance = ((int(attack) - (int(oppDef) // 2)) + 65)
    randHit = randVar()
    if randHit < hitChance:
        hit = 'hit'
    else:
        hit = 'miss'
    return hit


def viewStats():
    data = getPlayerData()
    # Data
    name = data["name"]
    race = data["race"]
    sex = data["sex"]
    # Combat
    health = int(data["health"])
    attack = data["attack"]
    strength = data["strength"]
    defence = data["defence"]
    magic = data["magic"]
    archery = data["archery"]
    # Crafting
    brewing = data["brewing"]

    print("\n" + name + "'s Combat Skills:")
    print("Health:", health)
    print("Attack:", attack)
    print("Strength:", strength)
    print("Defence:", defence)
    print("Magic:", magic)
    print("Archery:", archery)
    print()
    print(name + "'s Crafting Skills:")
    print("Brewing:", brewing)
    print()
    print("What would you like to do?")
    print("1) View Skill Guide"
          "\n2) Return to Menu")
    ans = input(">> ")
    if (ans == '1') or (ans.lower() == "view skill guide"):
        skillGuide()
    if (ans == '2') or (ans.lower() == "return to menu"):
        mainMenu()


def skillGuide():
    print("\nWhich skill would you like to read about?")
    print("Attack, Strength, Defence, Magic, Archery, Health, Brewing")
    ans = input(">> ")
    if ans.lower() == 'attack':
        attackGuide()
    elif ans.lower() == 'strength':
        strengthGuide()
    elif ans.lower() == 'defence':
        defenceGuide()
    elif ans.lower() == 'magic':
        magicGuide()
    elif ans.lower() == 'archery':
        archeryGuide()
    elif ans.lower() == 'health':
        healthGuide()
    elif ans.lower() == 'brewing':
        brewingGuide()

    else:
        print("ERROR: Type a correct input.")
        skillGuide()


def fight(enemy):
    oppData = getOppData()
    the_dude = Enemy(**oppData[enemy])
    print(the_dude)





def load_guide(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents


def attackGuide():
    contents = load_guide("guides/attack_guide.txt")
    print(contents)


def strengthGuide():
    contents = load_guide("guides/strength_guide.txt")
    print(contents)


def defenceGuide():
    contents = load_guide("guides/defence_guide.txt")
    print(contents)


def magicGuide():
    contents = load_guide("guides/magic_guide.txt")
    print(contents)


def archeryGuide():
    contents = load_guide("guides/archery_guide.txt")
    print(contents)


def healthGuide():
    contents = load_guide("guides/health_guide.txt")
    print(contents)


def brewingGuide():
    contents = load_guide("guides/brewing_guide.txt")
    print(contents)


def mainMenu():
    print("\nWhat would you like to do?")
    print("1) View Inventory"
          "\n2) View Armour"
          "\n3) View Stats"
          "\n4) Resume Game")
    ans = input(">> ")
    # if (ans == '1') or (ans.lower() == 'view inventory'):
    # viewInv()
    # elif (ans == '2') or (ans.lower() == 'view armour'):
    # viewArmour()
    if (ans == '3') or (ans.lower() == 'view stats'):
        viewStats()


def continueDialogue():
    input("Press >enter< to continue. ")


def main():
    import subprocess as sp
    sp.call("clear", shell=True)

    data = getPlayerData()
    print("Welcome to the game.")

    print("\nGUARD: Greetings, traveller! You must have come a long way to reach this place. How my I assist you?")
    continueDialogue()
    print("\n1) Prepare to die!"
          "\n2) What is this place?")
    ans = input(">> ")
    if (ans == '1') or (ans.lower() == "prepare to die!"):
        fight("guard")
    elif (ans == '2') or (ans.lower() == "what is this place?"):
        print()
        continueDialogue()
    elif ans == 'menu':
        mainMenu()


if __name__ == "__main__":
    main()
