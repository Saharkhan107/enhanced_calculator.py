# CIS 103: Introduction to Programming
#Lab 02: "Building a Enhanced Calculator"
#Instructor: Md Ali
#Student Name: Sahar Iqbal
#Date: 09/02/2024

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square_root(x):
    if x < 0:
        return "Error: Cannot compute the square root of a negative number."
    return math.sqrt(x)

def main():
    while True:
        # Display menu options
        print("\nPlease select an operation -")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation")
        print("6. Modulus")
        print("7. Square root")
        print("8. Exit")

        try:
            # Get user's choice
            operation = int(input("Select an operation (1, 2, 3, 4, 5, 6, 7, 8): "))

            if operation == 8:
                print("Exiting the calculator. Goodbye!")
                break

            if operation == 7:
                # Get number for square root
                number = float(input("Enter the number to find the square root of: "))
                result = square_root(number)
                print(f"Square root of {number} = {result}")
            elif operation in [1, 2, 3, 4, 5, 6]:
                # Get numbers for other operations
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))

                if operation == 1:
                    result = add(first_number, second_number)
                elif operation == 2:
                    result = subtract(first_number, second_number)
                elif operation == 3:
                    result = multiply(first_number, second_number)
                elif operation == 4:
                    result = divide(first_number, second_number)
                elif operation == 5:
                    result = exponentiate(first_number, second_number)
                elif operation == 6:
                    result = modulus(first_number, second_number)

                print(f"Result: {result}")
            else:
                print("Invalid input. Please select a valid operation (1, 2, 3, 4, 5, 6, 7, 8).")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
