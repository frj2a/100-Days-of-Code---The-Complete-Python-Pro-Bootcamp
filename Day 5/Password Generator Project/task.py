import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# too easy

# passwd = ""
# for letter in letters[0:nr_letters]:
#     passwd += letter
# for symbol in symbols[0:nr_symbols]:
#     passwd += symbol
# for number in numbers[0:nr_numbers]:
#     passwd += number
# print(passwd)


# easy

passwd2 = ""
for n in range(0,nr_letters):
    # passwd2 += letters[random.randint(0,len(letters)-1)]
    passwd2 += random.choice(letters)
for n in range(0,nr_symbols):
    # passwd2 += symbols[random.randint(0,len(symbols)-1)]
    passwd2 += random.choice(symbols)
for n in range(0,nr_numbers):
    # passwd2 += numbers[random.randint(0,len(numbers)-1)]
    passwd2 += random.choice(numbers)

print(passwd2)


# hard

passwd3 = list(passwd2)
random.shuffle(passwd3)

passwd4 = ""
for pwd in passwd3:
    passwd4 += pwd
print(passwd4)
