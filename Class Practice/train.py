class Train:

    def __init__(self, current_position):
        self.current_position = current_position

    def move(self, additional_distance):
        self.current_position = self.current_position + additional_distance

    def get_position(self):
        pass


# Write a piece of coding where it starts at 10m, and it moves by 5m, and get the position after.

train = Train(10)
train.move(5)
print(train.current_position)
