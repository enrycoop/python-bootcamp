import pandas

data = pandas.read_csv("./NATO.csv")

dict_data = {str(row.letter): str(row.code) for (index, row) in data.iterrows()}

token = input("Write a name: ")

print([dict_data[str(t).upper()] for t in token])

