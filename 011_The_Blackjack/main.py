import random
from resources import cards

computer_cards = []
player_cards = []


for item in range(2):
    rnd_card = random.choice(cards)
    player_cards.append(rnd_card)
    rnd2_card = random.choice(cards)
    computer_cards.append(rnd2_card)

computer_total = sum(computer_cards)
player_total = sum(player_cards)

print(f"Computer Cards : {computer_cards}")
print(f"Player Cards : {player_cards}")
print(f"Computer Total : {computer_total}")
print(f"Player Total : {player_total}")

def deal_card(player_list):
    rnd3_card = random.choice(cards)
    player_list.append(rnd3_card)

def check_bust(player_list):
    if sum(player_list) > 21:
        return True

def check_blackjack(player_list):
    if sum(player_list) == 21:
        return True

def check_winner(player_list_1, player_list_2):
    if sum(player_list_1) > sum(player_list_2):
        return True

end_game = False
while not end_game:
    user_input = input("Hit or Stand:\n").lower()
    if user_input == "hit":
        deal_card(player_list=player_cards)
        print(f"Player Cards : {player_cards}")
        is_bust = check_bust(player_list=player_cards)
        if is_bust == True:
            print("You Bust")
            end_game = True
    elif user_input == "stand":
        win = check_winner(player_list_1=player_cards, player_list_2=computer_cards)
        if win == True:
            print("YOU WIN")
        else:
            print("COMPUTER WIN")
        end_game = True

