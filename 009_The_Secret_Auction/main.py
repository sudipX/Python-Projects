from resources import logo, text
import os
print(logo)
print(text)

bidders_information = []
remaining_bidder = True
while remaining_bidder:
    temp = {}
    bidder_name = input("Enter the name of the bidder: \n>> ").capitalize()
    temp["Name"] = bidder_name
    bid_amount = float(input("Enter your bid amount: \n>> $"))
    temp["Amount"] = bid_amount

    bidders_information.append(temp)

    any_other_bidder = input("Are there any other bidder ? Y / N\n>> ").lower()
    if any_other_bidder == "y":
        os.system("cls")
        print(logo)
        print(text)
    elif any_other_bidder == "n":
        remaining_bidder = False

highest_bid_amount = 0
highest_bidder_name = ""
for items in bidders_information:
    amount = items["Amount"]
    if amount > highest_bid_amount:
        highest_bid_amount = amount
        highest_bidder_name = items["Name"]

print("Analyzing results...............................")
print(f"Highest bidder : {highest_bidder_name}\nBid Amount : ${int(highest_bid_amount)}")