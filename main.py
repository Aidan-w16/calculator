from model import Calculator

def main():

    calculator = Calculator()
    calculator.get_number()
    calculator.get_number()
    calculator.get_operator()

    print(
        f"""------------------------------------------------
{calculator.number1} {calculator.operator} {calculator.number2} = {calculator.get_result(calculator.number1,calculator.number2,calculator.operator)} """
    )

if __name__ == "__main__":
    main()