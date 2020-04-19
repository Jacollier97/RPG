
class Combatant:

    def do_attack(self,attack_move="basic"):
        print(self.name, " attacking")
        # place holder
        # named do_attack because of conflict with attack variable
        return self.attack

    def do_defence(self, opponents_attack, defence_move="basic"):
        # named do_defence because of conflict with defence variable
        print(self.name, " Defending!")

        print(f"defense: {self.defence}, opponents attack:{opponents_attack}, Defense move{defence_move}")
        # the player attack logic from main.py, I'm taking a break.
        # hitChance = ((int(attack) - (int(oppDef) // 2)) + 65)
        # randHit = randVar()
        # if randHit < hitChance:
        #     hit = 'hit'
        # else:
        #     hit = 'miss'
        # return hit

    def alive(self):
        return self.health > 0