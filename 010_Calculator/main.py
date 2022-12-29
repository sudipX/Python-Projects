from resources import logo
import os


operations = {
    "+" : "Addition",
    "-" : "Subtraction",
    "*" : "Multiplication",
    "/" : "Division"
}

def addtion(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2


continue_calculation = True

while continue_calculation:
    print(logo)
    first_num = int(input("Enter the number:\n>> "))
    for items in operations:
        print(f"{items} : {operations[items]}")
    operator = input("Choose your operator:\n>> ")
    second_num = int(input("Enter the number:\n>> "))

    def calculation(num1, operator_input, num2):
        if operator_input == "+":
            output = addtion(num1, num2)
            return output
        elif operator_input == "-":
            output = subtraction(num1, num2)
            return output
        elif operator_input == "*":
            output = multiplication(num1, num2)
            return output
        elif operator_input == "/":
            output = division(num1, num2)
            return output

    output = calculation(num1=first_num, operator_input=operator, num2=second_num)
    print(f"Your Output:\n{first_num} {operator} {second_num}  = {output}\n------------------------------------------------------------------")

    user_option = input("a. Continue Calculation\nb. New Calculation\n>> ")
    if user_option == "b":
        os.system("clear")

