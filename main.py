from model import Calculator


def main():

    calculator = Calculator()
    calculator.get_all_number()
    calculator.get_operator()
    print(calculator.all_numbers)
    print(calculator.operator)
    print(
        f"""------------------------------------------------
        {calculator.get_result()} """
    )


if __name__ == "__main__":
    main()
