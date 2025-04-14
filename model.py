class Calculator:
    def __init__(self):
        self.number_to_collect = 0

    def get_number(self):
        self.number_to_collect += 1
        while True:
            number = input(f"Enter number {self.number_to_collect}: ")
            try:
                number = float(number)
                if self.number_to_collect == 1:
                    self.number1 = number
                elif self.number_to_collect == 2:
                    self.number2 = number
                break
            except ValueError:
                print("Enter Numbers ONLY.")

    def get_operator(self):

        while True:
            operator = input("enter an operator(+,-,*,X,/):")
            if not (
                operator == "+"
                or operator == "-"
                or operator == "*"
                or operator == "X"
                or operator == "/"
            ):
                pass
            else:
                self.operator = operator
                break

    def get_result(self, number1, number2, operator):
        number1 = int(number1)
        number2 = int(number2)
        if operator == "+":
            result = number1 + number2
        if operator == "-":
            result = number1 - number2
        if operator == "*" or operator == "X":
            result = number1 * number2
        if operator == "/":
            result = number1 / number2
        return result
