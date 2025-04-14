from model import Calculator


def main():

    calculator = Calculator()
    calculator.get_all_number()
    calculator.get_operator()
    all_numbers = ""
    for i in range(calculator.number_required):
        all_numbers = (
            all_numbers
            + " "
            + calculator.operator
            + " "
            + str(calculator.all_numbers[i])
        )
    all_numbers = all_numbers[3:]
    print(
        f"""------------------------------------------------
{all_numbers} = {calculator.get_result()} """
    )


if __name__ == "__main__":
    main()
