print (10 % 3)

number = int(input("What is the number you want to check? "))

is_even = number %2 == 0

if is_even:
    print (f"Your number {number} is even.")
else:
    print (f"Your number {number} is odd.")