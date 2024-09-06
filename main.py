# Import functions from the other files
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    # Input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        # Perform the operation based on the operator
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator")
            return

        # Display the result
        print(f"The result is: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
