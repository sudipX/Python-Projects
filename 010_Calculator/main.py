from resources import logo
import os


def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division
}

def calculator():
    print(logo)
    first_num = int(input("Enter the number:\n>> "))
    continue_calculation = True
    while continue_calculation:
        for items in operations:
            print(f"{items} : {operations[items]}")
        operator = input("Choose your operator:\n>> ")
        second_num = int(input("Enter next number:\n>> "))

        calculation = operations[operator]
        output = calculation(num1=first_num, num2=second_num)

        print(f"Your Output:\n{first_num} {operator} {second_num}  = {output}\n------------------------------------------------------------------")
        user_input = input(f"Type 'Y' to continue calculation with {output} or 'N' to start new calculation & 'E' to exit:\n>> ").lower()
        if user_input == "y":
            first_num = output
        elif user_input == "n":
            os.system("clear")
            calculator()
        elif user_input == "e":
            print("GOODBYE !!!")
            break

calculator()