# File not found
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)


# try:
#     file = open("a_file.txt")
#     a_dict: dict[str, str] = {"key": "value"}
#     value = a_dict["non_existent_key"]
#     # try:
#     #     value = a_dict["non_existent_key"]
#     # except KeyError as error_msg:
#     #     print(f"The key {error_msg} does not exist.")
# except FileNotFoundError as file_name:
#     print(f"File '{file_name.filename}' not found, creating a standard one.")
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     # raise TypeError("This is an error that I made up.")


# height = float(input("Height: "))
# weight = int(input("Weight: "))
# try:
#     if height > 3:
#         raise ValueError("Human Height should not be higher than 3m.")
# except ValueError as error:
#     print(f"Error: {error}")
# bmi = weight / height ** 2

# fruits = ["Apple", "Pear", "Orange"]
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError as idx_err:
#         fruit = "Fruit"
#     finally:
#         print(fruit + " pie")
#
# make_pie(9)


# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# def count_likes(posts):
#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except KeyError:
#             pass
#     return total_likes
#
# print(count_likes(facebook_posts))
#


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


import pandas

try:
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
except:
    print("NATO phonetic alphabet data file doesn't exist in current directory.")
else:
    #TODO 1. Create a dictionary in this format:
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    print(phonetic_dict)

    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as key_error:
        print(f"Character {key_error} doesn't belong to NATO phonetic alphabet list.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()