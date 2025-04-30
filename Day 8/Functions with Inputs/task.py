def greet():
    print("Hello Francisco")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice?\n")


def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?\n")

def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left.")

greet()
greet_with_name("Chico")
life_in_weeks(56)