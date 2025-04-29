import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_number_0_to_10 = random.random() * 10
# print(random_number_0_to_10)
#
# random_number = random.uniform(1, 10)
# print(random_number)

random_integer_is_odd = random.randint(1, 10) % 2 == 0

if random_integer_is_odd:
    print("Heads")
else:
    print("Tails")