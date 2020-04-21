from combatant import Combatant

class Enemy(Combatant):

    def __init__(self, name=None, race=None, health=None, attack=None, strength=None, defence=None, magic=None,
                 archery=None):
        self.name = name
        self.race = race
        self.health = int(health)
        self.attack = int(attack)
        self.strength = int(strength)
        self.defence = int(defence)
        self.magic = int(magic)
        self.archery = int(archery)


    def die(self):
        self._produce_loot()
        pass

    def _produce_loot(self):
        pass

    def speak(self):
        pass

    def __str__(self):
        return f"{self.name} im working"
