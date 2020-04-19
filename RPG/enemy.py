

class Enemy:
    def __init__(self, name=None, race=None, health=None, attack=None, strength=None, defence=None, magic=None,
                 archery=None):
        self.name = name
        self.race = race
        self.health = health
        self.attack = attack
        self.strength = strength
        self.defence = defence
        self.magic = magic
        self.archery = archery

    def do_attack(self,attack_move="basic"):
        # place holder
        # named do_attack because of conflict with attack variable
        pass

    def do_defence(self,defence_move="basic"):
        # named do_defence because of conflict with defence variable
        pass

    def die(self):
        self._produce_loot()
        pass

    def _produce_loot(self):
        pass

    def speak(self):
        pass
