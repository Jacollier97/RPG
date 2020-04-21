from combatant import Combatant

class Player(Combatant):

    def __init__(self, name=None, race=None, sex=None, health=None, attack=None, strength=None, defence=None, magic=None,
                 archery=None, brewing=None):
        self.name = name
        self.race = race
        self.sex = sex
        self.health = int(health)
        self.attack = int(attack)
        self.strength = int(strength)
        self.defence = int(defence)
        self.magic = int(magic)
        self.archery = int(archery)
        self.brewing = int(brewing)
