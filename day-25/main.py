# with open("day-25/weather_data.csv") as csv_file:
#     data = csv_file.readlines()
#     print(data)

# import csv

# with open("day-25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("day-25/weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# using python
# average = sum(temp_list) / len(temp_list)
# print(int(average))

# using pandas series
# print(data["temp"].sum() / data["temp"].count())
# print(data["temp"].mean())
# print(f"The max is {data['temp'].max()}.")
# print minimum value of data temp
print(f"The min is {data['temp'].min()}")

# Get data in Columns
# print(data["day"])
# print(data["condition"])
# print(data.condition)

# Get data in Row
# print(data[data.day == "Monday"])

# getting row with max temp
# data.loc(data['temp'] == data.temp.max())
# data.loc(data["temp"] == 24)

# print(data.loc[data.temp == data.temp.max()])
# or 
# print(data[data.temp == data.temp.max()])

# getting temp of monday in fahrenheit

# monday = data[data.day == "Monday"]
# fahrenheit = monday.temp * 1.8 + 32
# print(fahrenheit)

# # creating dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("day-25/new_data.csv")