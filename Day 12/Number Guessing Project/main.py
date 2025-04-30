import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

correct = False
number = random.randint(1,100)

while not correct and attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if number == guess:
        print(f"You got it! The answer was {number}.")
        correct = True
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")

    attempts -= 1
    if attempts > 0 and not correct:
        print("Guess again.")
    elif attempts == 0:
        print(f"You've run out of guesses, you lose. The answer was {number}.")
