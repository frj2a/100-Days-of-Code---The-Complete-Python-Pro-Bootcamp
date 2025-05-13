
# First approach
# with open("weather_data.csv") as weather_file:
#     weather_days = weather_file.readlines()
#     for weather_day in weather_days:
#         day = weather_day.strip().split(',')
#         print(day)


# Second approach
# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:    # excluding column label
#         if row[1] != "temp":
#             print(int(row[1]))
#             temperatures.append(int(row[1]))
#     print (temperatures)


# Third approach
import pandas
# https://pandas.pydata.org/docs/reference/index.html
# https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/getting_started/index.html#getting-started

# Tests #1
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data["temp"].to_list()
# print(data_list)
# print(f"Average temperature: {sum(data_list) / len(data_list):.1f}")
# print(f"Average temperature: {data['temp'].mean() :.1f}")
# print(f"Maximum temperature: {data['temp'].max() :.1f}\n")
# print(data[data['day'] == "Monday"])
# print(data[data.day == "Monday"])   # Pandas creates attributes for the table column labels
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(type(monday.temp))
# print(f"{monday.temp[0] / 5 * 9 + 32:.1f} ºF")

# Tests #2 - Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")