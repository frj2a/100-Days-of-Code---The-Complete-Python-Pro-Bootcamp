import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

computer_choice = random.randint(0,2)

human_wins = True

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if 2 >= human_choice >= 0:
    print(game_images[human_choice])
    print(f"Computer chose:\n{game_images[computer_choice]}")
    if human_choice == computer_choice:
        print("Draw!\n")
    else:
        if human_choice > computer_choice:
            if human_choice == 2 and computer_choice == 0:
                human_wins = False
        else:
            if not(human_choice == 0 and computer_choice == 2):
                human_wins = False

        if human_wins:
            print("You win!\n")
        else:
            print("You lose.\n")
else:
    print("Wrong choice, please next time enter an integer from 0 to 2.\n")