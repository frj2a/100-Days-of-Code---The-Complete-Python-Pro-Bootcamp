# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it now in {location}?\n")

def calculate_love_score(name1, name2):
    keyword1 = "TRUE"
    keyword2 = "LOVE"
    true_count = 0
    love_count = 0
    for letter in name1.lower():
        if letter in keyword1.lower():
            true_count += 1
        if letter in keyword2.lower():
            love_count += 1
    for letter in name2.lower():
        if letter in keyword1.lower():
            true_count += 1
        if letter in keyword2.lower():
            love_count += 1
    print(true_count * 10 + love_count)

greet_with("Jack Bauer", "London")
greet_with(location="London", name="Jack Bauer")

calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")
