class Train:

    def __init__(self, current_position):
        self.current_position = current_position
        print(self.current_position)

    def move(self, additional_distance):
        pass

    def get_position(self):
        pass

    position = 10

#Write a piece of coding where it starts at 10m, and it moves by 5m, and get the position after.

train = Train(10)