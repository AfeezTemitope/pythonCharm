from calculator_functions import Calculator


def main():
    calculator = Calculator()
    main_app(calculator)


def main_app(calculator):
    calculator.display_menu()
    choice = input("Enter choice (1/2/3/4/5): ")
    calculator.exit(choice)

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    result = calculator.calculate(choice, num1, num2)
    if result is not None:
        print(f"Result: {result}")
        print('-----------------')
        with open("CalculatorResult.txt", "w") as file:
            file.write(f"Result: {result}\n")

    main_app(calculator)


if __name__ == "__main__":
    main()
