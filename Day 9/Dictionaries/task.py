programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    123: "Test",
}

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"])
print(programming_dictionary[123])

empty_list = []
empty_dictionary = {}

programming_dictionary["Bug"] = "A moth in the valves of your computer."

print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(type(key))
    print(programming_dictionary[key])