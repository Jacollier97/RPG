import yaml

class Gen_Enemy():
    """this class is used to more easily generate enemy data, and then save it into the
    enemies.json file"""

    ENEMIES_DATA = "RPG/enemies.yaml"
    def __init__(self):
        self.data = self.get_data()
        self.main()

    def main(self):
        # check if you actually want to create an enemy
        self.begin_check()

        while True:
            # collect recent copy of the enemies.yaml data
            self.data = self.get_data()
            # get the enemy
            title, enemy = self.get_new_enemy()

            # tell you what data it got from you
            print(yaml.dump({title: enemy}, sort_keys=False))
            if self.get_y_n("do you like it? (y/n): "):
                # add new data to old and write it to enemies.yaml
                self.data[title] = enemy
                self.set_data(self.data)
            else:
                # ask you if you want to try again else, exit program
                if self.get_y_n("do you want to try again? (y/n): "):
                    print("ok lets try again.")
                    continue
                else:
                    self.end()
            # ask you if you want to make another or exit the program
            if self.get_y_n("do you want to make another? (y/n): "):
                continue
            else:
                self.end()


    def begin_check(self):
        message = "do you want to create a new enemy?"
        return self.get_y_n(message)

    def get_new_enemy(self):
        """ collect all data values need to create an enemy,
        and check to make sure they are within bounds.
        return data values and enemy title."""

        string_values_needed = ["name",
                                "race"]

        num_values_needed = ["health",
                             "attack",
                             "strength",
                             "defence",
                             "magic",
                             "archery"]

        while True:
            enemy_title = input("What should be the enemy's title?: ").lower()

            # check if that title already exists in the data
            if enemy_title in self.data:
                print("that title is already in the data. pick a new one")
            else:
                print("good choice")
                break

        enemy = {}
        for value in string_values_needed:
            enemy[value] = input(f"what should the enemy's {value} be?: ")

        # get integer values and check if within bounds
        for value in num_values_needed:
            enemy[value] = self.get_num_input(value)

        return enemy_title, enemy

    def set_data(self, data):
        with open(self.ENEMIES_DATA, "w") as f:
            yaml.dump(data, f, sort_keys=False)

    def get_data(self):
        with open(self.ENEMIES_DATA, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    @staticmethod
    def get_num_input(value):
        while True:
            try:
                answer = int(input(f"What should the enemies {value} be? (1-200): "))
            except ValueError as e:
                print("That's not an integer.")
                continue
            else:
                if 0 < answer <= 200:
                    return answer
                elif answer <= 0:
                    print("Your answer is too small.")
                else:
                    print("Your answer is too big.")

    def get_y_n(self, message):
        options = ["y", "n"]
        while True:
            answer = input(message)
            if answer in options:
                return answer == "y"
            else:
                print("invalid input")
                continue


if __name__ == "__main__":
    ge = Gen_Enemy()

