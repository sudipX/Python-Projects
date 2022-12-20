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
    if any_other_bidder == "n":
        remaining_bidder = False

# finding the highest bidder from the bidders information list
print(bidders_information)