import random
import art
import game_data

score = 0
person_2 = random.choice(game_data.data)

def format_person(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"

def get_persons():
    global person_2
    person_1 = person_2
    print(f"Compare A: {format_person(person_1)}")
    print(art.vs)
    person_2 = random.choice(game_data.data)
    name = person_2['name']
    while name == person_1['name']:
        person_2 = random.choice(game_data.data)
        name = person_2['name']
    print(f"Against B: {format_person(person_2)}")
    return [person_1['follower_count'], person_2['follower_count'],]

def check_answer(guess, a_count, b_count):
    if a_count == b_count:
        return True
    elif a_count > b_count:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    global score
    keep_going = True
    while keep_going:
        print(art.logo)
        if score !=0:
            print (f"You're right! Current score: {score}")
        a_follower_count, b_follower_count = get_persons()
        print(f"A: {a_follower_count} - B: {b_follower_count}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        if is_correct:
            score += 1
            print("\n" * 50)
        else:
            keep_going = False
            print(f"Sorry, that's wrong.  Final score: {score}")

game()
