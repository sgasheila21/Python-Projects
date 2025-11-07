def input_number(param):
    while True:
        try:
            return float(input(param))
        except ValueError:
            print("Invalid number. Please try again!")


def input_operator(param):
    while True:
        operator = input(param)
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Invalid operator. Please try again!")


while True:
    result = None
    first_number = input_number("Enter first number: ")
    operator = input_operator("Enter operator (+, -, *, /): ")

    while True:
        second_number = input_number("Enter second number: ")
        if operator == "/" and second_number == 0:
            print("Division by zero is not allowed. Please enter a different number.")
        else:
            break

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number

    if result.is_integer():
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")

    while True:
        again = input(
            "Do you want to perform another calculation? (y/n): ").strip().lower()
        if again in ['y', 'n']:
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

    if again == 'n':
        print("Goodbye")
        break
