import random
import resources

cases = ["Rock", "Paper", "Scissors"]
arts = [resources.rock, resources.paper, resources.scissors]
play_again = True
while play_again:
    print("THE ROCK PAPER AND SCISSORS GAME")
    print("################################")

    user_choice = int(input("Enter your choice:\n0: Rock\n1: Paper\n2: Scissors\n>> "))

    print("YOU CHOSE:\n")
    print(cases[user_choice])
    print(arts[user_choice])

    computer_choice = random.randint(0,2)

    print("COMPUTER CHOSE:\n")
    print(cases[computer_choice])
    print(arts[computer_choice])

    # Logic
    #Draw case
    if computer_choice == user_choice:
        print("YOU HAVE A DRAW.")
    # User winning case
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        print("YOU LOST.")
    else:
        print("YOU WON.")
    
    continue_game = input("Do you wanna play again ? 'Y' or 'N'\n").lower()
    if continue_game == "n":
        play_again = False
        print("BYE !!!")