import os

# Function to clear the console, making each calculation start fresh on a new screen
def clear_console():
    # For Windows, use 'cls', and for Unix-based systems, use 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the menu options for the calculator
def show_menu():
    print('****************\n   BASIC CALCULATOR\n****************')
    print('Select an operation to perform:\n')
    print('+. For Addition')
    print('-. For Subtraction')
    print('*. For Multiplication')
    print('/. For Division')
    print('**. To Find the Square of a Number')
    print('%. To Find the Remainder by Dividing Two Numbers')
    print('//. To Find the Quotient Without Decimal Part')
    print('\nType "Exit" to close the app\n')

# Function to safely get a number from the user with error handling for non-numeric input
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))  # Convert input to float for decimal calculations
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Handle non-numeric input

# Main function to perform calculations based on user choice
def calculation_fun():
    while True:
        clear_console()  # Clear console for a fresh start
        show_menu()  # Display the menu to the user
        
        # Prompt user for the operation type
        key_enter_by_user = input('Enter the operation you want to perform: ')
        
        # Exit condition if user types 'Exit' or 'exit'
        if key_enter_by_user.lower() == 'exit':
            print('YOU CLOSED THE APP. SEE YOU NEXT TIME!\nTHANK YOU :)')
            break

        # Validate operation input; if invalid, prompt again
        if key_enter_by_user not in ['+', '-', '*', '/', '**', '%', '//']:
            print("Please enter a valid operation.")
            continue

        # Single-operand operation: square calculation
        if key_enter_by_user == '**':  
            first_num = get_number('Enter a number to find its square: ')
            result = first_num ** 2
            print(f'\nThe Square of {first_num} is {result}\n')
        
        else:
            # For binary operations, get both the first and second numbers from the user
            first_num = get_number('Enter First Number: ')
            second_num = get_number('Enter Second Number: ')

            # Perform addition
            if key_enter_by_user == '+':
                result = first_num + second_num
                print(f'\nThe Result of {first_num} + {second_num} is {result}\n')

            # Perform subtraction
            elif key_enter_by_user == '-':
                result = first_num - second_num
                print(f'\nThe Result of {first_num} - {second_num} is {result}\n')

            # Perform multiplication
            elif key_enter_by_user == '*':
                result = first_num * second_num
                print(f'\nThe Result of {first_num} * {second_num} is {result}\n')

            # Perform division with zero-check
            elif key_enter_by_user == '/':
                if second_num == 0:
                    print("Error: Division by zero is undefined.\n")  # Error message for zero division
                else:
                    result = first_num / second_num
                    print(f'\nThe Result of {first_num} / {second_num} is {result:.2f}\n')  # Format to 2 decimals

            # Perform modulus operation with zero-check
            elif key_enter_by_user == '%':
                if second_num == 0:
                    print("Error: Modulo by zero is undefined.\n")  # Error message for modulo by zero
                else:
                    result = first_num % second_num
                    print(f'\nThe Result of {first_num} % {second_num} is {result}\n')

            # Perform floor division with zero-check
            elif key_enter_by_user == '//':
                if second_num == 0:
                    print("Error: Floor division by zero is undefined.\n")  # Error message for floor division by zero
                else:
                    result = first_num // second_num
                    print(f'\nThe Result of {first_num} // {second_num} is {result}\n')

        # Pause to allow user to review result before continuing
        input("Press Enter to continue...")

# Run the main calculation function
calculation_fun()