print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ") == "Y"
extra_cheese = input("Do you want extra cheese? Y or N: ") == "Y"

bill = 0

if size == "S":
    bill = 15
    if pepperoni:
        bill +=2
elif size == "M":
    bill = 20
    if pepperoni:
        bill +=3
else:
    bill = 25
    if pepperoni:
        bill +=3

if extra_cheese:
    bill += 1

print(f"Your final bill is: ${bill}.")
