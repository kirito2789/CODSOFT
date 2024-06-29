"""This a Basic Calculator designed for my Internship """

def run_calculator():
    print("Welcome to my basic calculator!")
    print("You can use this tool to perform addition, subtraction, multiplication, or division.")


    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter the number of the operation you want to perform: ")

    if choice == '1':
        result = number1 + number2
        operation = "addition"
    elif choice == '2':
        result = number1 - number2
        operation = "subtraction"
    elif choice == '3':
        result = number1 * number2
        operation = "multiplication"
    elif choice == '4':
        if number2 != 0:
            result = number1 / number2
            operation = "division"
        else:
            print("Error: Division by zero is not possible.")
            return
    else:
        print("Invalid selection. Please run the program again and select a valid operation.")
        return

    print(f"The result is: {result}")


run_calculator()
