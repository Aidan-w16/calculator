class Calculator:
    def __init__(self):
        self.number_to_collect = 0

    def get_number(self):
        self.number_to_collect += 1
        while True:
            number = input(f"Enter number {self.number_to_collect}. ")
            try:
                number = float(number)
                return number
            except ValueError:
                print("Enter Numbers ONLY.")

    def get_operator(self):
        i = 0
        while i == 0:
            operator = input("enter an operator(+,-,*,X,/):")
            if not (
                operator == "+"
                or operator == "-"
                or operator == "*"
                or operator == "X"
                or operator == "/"
            ):
                i = 0
            else:
                i = 1
        return operator

    def get_result(self, num1, num2, operator):
        num1 = int(num1)
        num2 = int(num2)
        if operator == "+":
            result = num1 + num2
        if operator == "-":
            result = num1 - num2
        if operator == "*" or operator == "X":
            result = num1 * num2
        if operator == "/":
            result = num1 / num2
        return result
