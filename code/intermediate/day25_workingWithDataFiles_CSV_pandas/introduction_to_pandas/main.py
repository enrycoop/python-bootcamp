# Open the weather_data.csv, read lines and create a list named data that contains the values from the .csv file.
# from statistics import mean

# with open("./weather_data.csv") as file:
#     lines = file.readlines()
#
# data = []
# for line in lines:
#     data.append(line.strip().split(','))
# print(data)

# import csv
#
# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in Columns
# print(data["condition"]) # case sensitive
# print(data.condition)

# get Data in row
# Questo e' possibile grazie al fatto che c'e un operatore
#  ==(list,obj) -> list[bool] e restituisce una lista di booleani
# del confronto tra ogni valore della lista e il valore obj che stiamo confrontando.
#
# Inoltre se applichiamo tale output ad un operatore[] ad una lista ci filtrera'
# i valori della lista solo agli indici dove e' true


# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp_fahrenheit = (monday.temp * 9/5) + 32
# print(monday_temp_fahrenheit)

#
# Create datafram from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")





