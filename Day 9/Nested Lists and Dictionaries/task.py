capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# print "Lille"

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print "D"

print(nested_list[2][1])

print(type(nested_list[2]))

travel_log_2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon", ],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart", ],
        "total_visits": 5,
    },
}

print(travel_log_2["Germany"]["cities_visited"][2])

starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary)