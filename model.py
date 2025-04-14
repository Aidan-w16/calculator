class Calculator:

    def get_first_number(self):
        while True:
            first_number = input("Enter the first number. ")
            try:
                first_number = int(first_number)
                return first_number
            except ValueError:
                print("Enter Numbers ONLY.")


    def get_second_number(self):
        while True:
            second_number = input("Enter the second number")
            try:
                second_number = int(second_number)
                return second_number
            except ValueError:
                print("Enter Numbers ONLY")


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
