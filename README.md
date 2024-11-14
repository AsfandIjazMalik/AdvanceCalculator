# NumWorks
Python Programming 

# Basic Calculator 🧮

A simple, interactive command-line calculator built with Python. This calculator allows users to perform basic arithmetic operations, as well as other mathematical calculations, in a clear and user-friendly way. It also includes input validation and error handling to prevent issues such as division by zero and non-numeric input errors.

## Features

- **Addition** (+)
- **Subtraction** (-)
- **Multiplication** (*)
- **Division** (/)
- **Square Calculation** (**)
- **Modulo Calculation** (%)
- **Floor Division** (//)
- **Exit Option**: Type "Exit" to close the application

Each calculation operation is followed by an interactive prompt that guides the user through entering numbers and obtaining results.

## How It Works

1. The calculator displays a menu of available operations.
2. The user selects an operation by typing the corresponding symbol (e.g., `+` for addition).
3. The program prompts the user for input numbers as needed (either one or two numbers depending on the operation).
4. Results are displayed, formatted for readability.
5. The user can continue performing calculations or type "Exit" to close the application.

## Project Structure

The calculator consists of three primary functions:
- `show_menu()`: Displays the available operations.
- `get_number(prompt)`: Prompts for and validates numeric input from the user.
- `calculation_fun()`: The main function that handles operation selection, calculation logic, and user interaction flow. <br>
## Error Handling
Division by Zero: If the user attempts to divide by zero, the program alerts them that this operation is undefined.
Non-numeric Input: The program validates that inputs are numeric, prompting the user to re-enter values if non-numeric input is detected. <br>
<br> 
## Example 
Select an operation to perform:<br>

+. For Addition<br>
-. For Subtraction<br>
*. For Multiplication<br>
/. For Division<br>
**. To Find the Square of a Number<br>
%. To Find the Remainder by Dividing Two Numbers<br>
//. To Find the Quotient Without Decimal Part<br>

Type "Exit" to close the app<br>

Enter the operation you want to perform: +<br>
Enter First Number for Addition: 10<br>
Enter Second Number for Addition: 5<br>

The Result of 10 + 5 is 15<br>
Press Enter to continue...<br>


