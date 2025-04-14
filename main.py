from model import Calculator

def main():

    calculator = Calculator()
    number1 = calculator.get_number()
    number2 = calculator.get_number()
    operator = calculator.get_operator()

    print(
        f"""------------------------------------------------
{number1} {operator} {number2} = {calculator.get_result(number1,number2,operator)} """
    )

if __name__ == "__main__":
    main()