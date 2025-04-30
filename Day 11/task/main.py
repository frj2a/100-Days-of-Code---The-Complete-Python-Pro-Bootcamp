import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal(hand):
    """ Only on the first deal, distribute 2 cards"""
    if len(hand) == 0: # first deal
        hand.append(random.choice(cards))
    hand.append(random.choice(cards))
    return hand

def show_player_hand(hand):
    output = ""
    amount1 = 0
    amount2 = 0
    for card in hand:
        if card == 11:
            output += " Ace"
            amount1 += 1
            amount2 += 11
        else:
            output += f" {card}"
            amount1 += card
            amount2 += card
    if amount1 == amount2:
        print(f"You have: {output} that counts as {amount1}")
    else:
        print(f"You have: {output} that counts as {amount1} or {amount2}")
    return [amount1, amount2]

def show_hidden_computer_hand(hand):
    output = ""
    amount1 = 0
    amount2 = 0
    if hand[0] == 11:
        output += "Ace"
        amount1 += 1
        amount2 += 11
    else:
        output += f"{hand[0]}"
        amount1 += hand[0]
        amount2 += hand[0]
    for i in range(len(hand) - 1):
        output += " _"
        if hand[i+1] == 11:
            amount1 += 1
            amount2 += 11
        else:
            amount1 += hand[i+1]
            amount2 += hand[i+1]

    print(f"Computer has: {output}\n")
    return [amount1, amount2]

def show_opened_computer_hand(hand):
    output = ""
    amount1 = 0
    amount2 = 0
    for card in hand:
        if card == 11:
            output += " Ace"
            amount1 += 1
            amount2 += 11
        else:
            output += f" {card}"
            amount1 += card
            amount2 += card
    if amount1 == amount2:
        print(f"Computer has: {output} that counts as {amount1}")
    else:
        print(f"Computer has: {output} that counts as {amount1} or {amount2}")

def best_player_option(values):
    best_option = -1
    if values[0] == values[1]:
        best_option = values[0]
    else:
        if values[0] > 21 and values[1] > 21:
            best_option = min(values)
        elif values[0] <= 21 and values[1] > 21:
            best_option = values[0]
        elif values[0] > 21 and values[1] <= 21:
            best_option = values[1]
        else:
            best_option = max(values)
    return best_option

keep_playing = True
keep_going = True

player_hand = []
computer_hand = []

best_player_value = 0
best_computer_value = 0

print (art.logo)
while keep_playing:
    while keep_going:
        player_hand = deal(player_hand)
        if best_computer_value < 17:
            computer_hand = deal(computer_hand)
        player_values = show_player_hand(player_hand)
        computer_values = show_hidden_computer_hand(computer_hand)
        # print(player_values)
        # print(computer_values)
        best_player_value = best_player_option(player_values)
        best_computer_value = best_player_option(computer_values)
        # print(f"Computer: {computer_hand} = {best_computer_value}  -  Player: {best_player_value}")
        if (best_player_value == 21 and best_computer_value == 21) or best_player_value > 21:
            print ("You loose!")
            break
        else:
            if best_computer_value == 21:
                print("You loose!")
                break
            elif best_player_value == 21:
                print("You win!")
                break
            else:
                keep_going = "y" == input("Do you want to another card (y/n)? ").lower()
                if not keep_going:
                    if best_player_value == best_computer_value or (best_player_value > 21 and best_computer_value> 21):
                        print("Draw!")
                    else:
                        if (best_player_value > 21 or (best_player_value < best_computer_value)) and best_computer_value <= 21:
                            print("You lose!")
                        else:
                            print("You win!")
    show_opened_computer_hand(computer_hand)
    keep_going = True
    player_hand = []
    computer_hand = []
    keep_playing = "y" == input("Do you want to play again (y/n)? ").lower()
