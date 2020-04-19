import json
import random

PLAYER_DATA = "playerData.json"
ENEMIES_DATA = "enemies.json"

def getPlayerData():
    with open("playerData.json", 'r') as f:
        data = json.load(f)
    return data


def setPlayerData(data):
    with open("playerData.json", 'w') as f:
        f.write(json.dumps(data, indent=4))


def getOppData():
    with open("enemies.json", 'r') as f:
        data = json.load(f)
    return data

def randVar():
    odds = random.randrange(0, 101)
    return int(odds)


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
    oppData = Enemy[enemy]
    print(oppData)
    # while (player == alive) or (enemy == alive):


def attackGuide():
    print("\nAttack Skill Guide:")
    print('\nThe Attack skill controls the probability that you will land an attack on an enemy. It also allows you '
          'to wield better weapons as your level increases.')


def strengthGuide():
    print("\nStrength Skill Guide:")
    print('\nThe Strength skill controls both your max possible damage, and also the likelihood '
          'that you will deal more damage with your successful hits.')


def defenceGuide():
    print("Defence Skill Guide:")


def magicGuide():
    print("Magic Skill Guide:")


def archeryGuide():
    print("Archery Skill Guide:")


def healthGuide():
    print("Health Skill Guide:")


def brewingGuide():
    print("Brewing Skill Guide:")


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
    input(">> Press >enter< to continue.")


def main():
    data = getPlayerData()
    print("\nWelcome to the game.")

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


main()
