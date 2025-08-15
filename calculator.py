# A simple command-line calculator script.

def calculator():
    """
    Main function for the calculator.
    It takes user input for two numbers and then a number to select
    an operator. It performs the calculation and prints the result.
    The loop continues until the user types 'exit'.
    """
    print("Welcome to the Simple Python Calculator!")
    print("Enter 'exit' to quit.\n")

    while True:
        # Prompt user for the first number
        num1_input = input("Enter the first number: ")
        # Check if the user wants to exit
        if num1_input.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        # Prompt user for the second number
        num2_input = input("Enter the second number: ")
        # Check if the user wants to exit
        if num2_input.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        # Prompt user to select an operator by number
        print("Select an operator:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        operator_choice = input("Enter your choice (1-4): ")

        # Map the numeric choice to an operator symbol
        operator = ''
        if operator_choice == '1':
            operator = '+'
        elif operator_choice == '2':
            operator = '-'
        elif operator_choice == '3':
            operator = '*'
        elif operator_choice == '4':
            operator = '/'
        else:
            # Handle invalid operator choice and restart the loop
            print("Error: Invalid operator choice. Please enter a number from 1 to 4.\n")
            continue

        try:
            # Convert string inputs to floats for calculation
            num1 = float(num1_input)
            num2 = float(num2_input)

            # Perform the calculation based on the operator
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                # Handle division by zero error
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue  # Skip to the next iteration of the loop
                result = num1 / num2
            
            # Print the final result
            print(f"Result: {result}\n")

        except ValueError:
            # Handle cases where the user enters non-numeric values
            print("Error: Invalid number input. Please enter valid numbers.\n")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    calculator()
