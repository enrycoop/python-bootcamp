import pandas

data = pandas.read_csv("./NATO.csv")
dict_data = {str(row.letter): str(row.code) for (index, row) in data.iterrows()}

correct = False
while not correct:
    try:
        token = input("Write a name: ")
        print([dict_data[str(t).upper()] for t in token])
    except KeyError:
        print("Please enter a letter string!")
    else:
        correct = True
