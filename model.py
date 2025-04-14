
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

    def get_number(self):
        self.number_required = self.get_number("How many numbers do you need to calculate?")
        # self.first_number = self._get_number("Ënter the first number.")
        # self.second_number = self._get_number("Ënter the second number.")

    def get_operator(self):

        

        while True:
            concat_string = ', '.join(self.accepted_operators)
            operator = input(f"enter an operator({concat_string}):")
            if operator in self.accepted_operators:
                self.operator = operator
                break
            else:
                print(f"Please enter one of the following '{concat_string}'.")

    def get_result(self):
        number1 = int(self.first_number)
        number2 = int(self.second_number)

        operator_map = {
            '+': number1 + number2,
            '-': number1 - number2,
            "*": number1 * number2,
            "X": number1 * number2,
            "/": number1 / number2
        }

        result = operator_map[self.operator]
        return result
