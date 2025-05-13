import pandas

# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250512.csv")

black_squirrels = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()

new_data = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count":[gray_squirrels, cinnamon_squirrels, black_squirrels]
}

pandas.DataFrame(new_data).to_csv("squirrels_count.txt")
