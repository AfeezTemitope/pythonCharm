import sys


class Calculator:
    def add(self, x, y):
       if isinstance(int)(x,(int,float)) and isinstance(int)(y,(int,float)):
            return int(x) + int(y)
       raise 'both input must be numeric'


    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def exit(self, exit_button):
        if exit_button == '5':
            sys.exit(0)

    def display_menu(self):
        operator = """Select operation:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Exit App"""
        print(f'-------------------\n{operator}')

    def calculate(self, choice, num1, num2):
        match choice:
            case '1':
                return self.add(num1, num2)
            case '2':
                return self.subtract(num1, num2)
            case '3':
                return self.multiply(num1, num2)
            case '4':
                return self.divide(num1, num2)
            case _:
                print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
                return None



