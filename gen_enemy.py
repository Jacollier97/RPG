import yaml

class Gen_Enemy():
    """this class is used to more easily generate enemy data, and then save it into the
    enemies.json file"""

    ENEMIES_DATA = "RPG/enemies.yaml"
    def __init__(self):
        self.data = self.get_data()
        self.main()

    def main(self):
        self.begin_check()

        new_enemy = self.get_new_enemy()


    def begin_check(self):
        message = "do you want to create a new enemy?"
        return self.get_y_n(message)


    def get_new_enemy(self):
    def set_data(self):
        pass

    def get_data(self):
        with open(self.ENEMIES_DATA, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def get_num_input(self, value):
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

