import random
from art import logo, stages
from wordlists import words
import os

def hangman():
    print(logo)
    random_word = random.choice(words)
    print(random_word)
    lives = 6
    blanks = []
    for letters in random_word:
        blanks.append("_")
    print("\n")
    print(" ".join(blanks))
    print("\n")
    end_of_game = False
    while not end_of_game:
        user_input = input("Guess Any Letter:\n>> ").lower()
        print("------------------------------------------------")
        n = 0
        for letters in random_word:
            if user_input == letters:
                blanks[n] = user_input
                if "_" not in blanks:
                    print("CONGRATULATIONS !!!")
                    end_of_game = True

            n += 1
        print(" ".join(blanks))
        print("------------------------------------------------")
        if user_input not in random_word:
            print("########################################")
            print("WRONG GUESS!!!\nYOU LOSE A LIFE.\n")
            print(stages[lives])
            print("########################################")
            lives -= 1
            if lives == 1:
                print("ALERT !!! YOU HAVE ONLY 1 LIFE LEFT.")
            if lives == 0:
                print("#####################################")
                print("YOU HANGED YOUR HANGMAN!!!")
                print(stages[0])
                print("GAME OVER!!!!")
                print("#####################################")
                end_of_game = True

        
    
play_again = True
while play_again:
    os.system("clear")
    hangman()
    user = input("Play Again(Y / N):\n>> ").lower()
    if user == "n":
        play_again = False
        print("BYE")


