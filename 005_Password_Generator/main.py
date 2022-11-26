import random
from resources import art
from resources import letters
from resources import numbers
from resources import symbols

print(art)
print("##################################################################################################################")

letters_in_password = int(input("Enter the number of letters you like to use:\n>> "))
numbers_in_password = int(input("Enter the number of numerical digits you like to use:\n>> "))
symbols_in_password = int(input("Enter the number of symbols you like to use:\n>> "))

# Letters in password
letters_list = []

for l in range(0, letters_in_password + 1):
    letter = random.choice(letters)
    letters_list.append(letter)

#print(letters_list)

# Numbers in password
numbers_list = []

for n in range(0, numbers_in_password + 1):
    number = random.choice(numbers)
    numbers_list.append(number)

#print(numbers_list)

# Symbols in password
symbols_list = []

for s in range(0, symbols_in_password + 1):
    symbol = random.choice(symbols)
    symbols_list.append(symbol)

#print(symbols_list)

# Final password list
password_list = []

for items in letters_list:
    password_list.append(items)
for items in symbols_list:
    password_list.append(items)
for items in numbers_list:
    password_list.append(items)

random.shuffle(password_list)
#print(password_list)

# Final password
final_password = ""

for item in password_list:
    final_password += item

#print(final_password)

print(f"Final password\n>> {final_password}")