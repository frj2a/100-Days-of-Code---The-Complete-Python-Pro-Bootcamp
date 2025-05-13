# list_n = [1, 2, 3]
# new_list = [ n + 1 for n in list_n]
# print(new_list)
#
# range_list = [ n * 2 for n in range(1,5)]
# print(range_list)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) == 4]
# print(short_names)
# long_names =  [name.upper() for name in names if len(name) >= 5]
# print(long_names)



# with open("file1.txt") as file1:
#     file1_contents = file1.readlines()
#
# with open("file2.txt") as file2:
#     file2_contents = file2.readlines()
#
# file1_list = [int(n.strip()) for n in file1_contents ]
# file2_list = [int(n.strip()) for n in file2_contents ]
# result = [ n for n in file1_list if n in file2_list]
# print(result)



# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = { name : random.randint(1,100) for name in names }
# print(students_scores)
# print(students_scores.items())
# passed_students = { student : score for (student, score) in students_scores.items() if score >= 70}
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = { word.strip() : len(word) for word in sentence.split(" ") }
# print(result)


# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = { day : temperature * 9 / 5 + 32 for (day,temperature) in weather_c.items() }
# print(weather_f)



import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score" : [56, 76, 98]
# }
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

NATO_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# NATO_alphabet_dict = NATO_alphabet.to_dict("records")
NATO_alphabet_dict = { row.letter : row.code for (index,row) in NATO_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
processed_word = [ NATO_alphabet_dict[letter] for letter in word]
print(processed_word)
