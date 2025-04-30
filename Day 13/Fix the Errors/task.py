# age = int(input("How old are you?"))

# fixing
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical value.")
    age = int(input("How old are you?"))
# fixed


#if age > 18:
if age >= 18: # fixed
# print("You can drive at age {age}.")
    print(f"You can drive at age {age}.") # fixed
