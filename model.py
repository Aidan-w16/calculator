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
                or operator == "/"):
                pass
            else:
                self.operator = operator
                break

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
