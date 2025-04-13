class Calculator:

    def get_first_number(self):
        i = 0
        while i == 0:
            first_num = input("Enter the first number")
            try:
                first_num = int(first_num)
                i = 2
            except ValueError:
                print("Enter Numbers ONLY")

                i = 0
        return first_num

    def get_second_number(self):
        i = 0
        while i == 0:
            second_num = input("Enter the second number")
            try:
                second_num = int(second_num)
                i = 2
            except ValueError:
                print("Enter Numbers ONLY")

                i = 0
        return second_num

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
