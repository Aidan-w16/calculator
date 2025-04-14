from number_to_word import number_to_word

num_to_word = number_to_word()


class Calculator:

    def __init__(self):
        self.number_required = None
        self.all_numbers = []
        self.operator = None
        self.accepted_operators = ["+", "-", "*", "X", "/"]

    def _get_number(self, display_text):
        while True:
            number = input(display_text)
            try:
                number = float(number)
                return number
            except ValueError:
                print("Enter Numbers ONLY.")

    def get_all_number(self):
        self.number_required = int(
            self._get_number("How many numbers do you need to calculate?")
        )
        for i in range(self.number_required):
            number_word = num_to_word.number_to_word[i + 1]
            self.all_numbers.append(
                self._get_number(f"Enter the {number_word} number: ")
            )

    def get_operator(self):

        while True:
            concat_string = ", ".join(self.accepted_operators)
            operator = input(f"Enter an operator({concat_string}): ")
            if operator in self.accepted_operators:
                self.operator = operator
                break
            else:
                print(f"Please enter one of the following '{concat_string}'.")

    def get_result(self):
        result = self.all_numbers[0]
        numberindex = 0

        for numberindex in range(1, self.number_required):

            operator_map = {
                "+": result + self.all_numbers[numberindex],
                "-": result - self.all_numbers[numberindex],
                "*": result * self.all_numbers[numberindex],
                "X": result * self.all_numbers[numberindex],
                "/": result / self.all_numbers[numberindex],
            }

            result = operator_map[self.operator]

        return result
