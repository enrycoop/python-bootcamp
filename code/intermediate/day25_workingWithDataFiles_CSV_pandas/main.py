# Open the weather_data.csv, read lines and create a list named data that contains the values from the .csv file.


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

"""
In pandas abbiamo due tipi di struture dati 
1D series
2D dataframe
"""

data = pandas.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)







