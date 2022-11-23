print("##### TIP CALCULATOR #####")

total_bill = float(input("Enter the total amount of bill: \n$ ")) 
tip_percentage = float(input("Enter the percentage of tip you would like to give: \n% "))
persons = float(input("Enter the number of people to split the bill :\n> "))

tip_amount = ( tip_percentage * total_bill ) / 100
total_amount_to_pay = total_bill + tip_amount
individual_amount = round(total_amount_to_pay / persons, 2)

print(f"Each person should pay ${individual_amount}.")