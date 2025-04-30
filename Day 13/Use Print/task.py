word_per_page = 0
pages = int(input("Number of pages: "))
# fixing
print(pages) # results as expected
# /fixing

# word_per_page == int(input("Number of words per page: ")) # wrong
word_per_page = int(input("Number of words per page: ")) # fixed

# fixing
print(word_per_page) # resulted a boolean
# /fixing

total_words = pages * word_per_page
print(total_words)
