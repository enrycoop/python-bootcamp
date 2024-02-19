# Struttura Gestione degli errori
# try:
#   blocco di codice che puo' causare un eccezione
# except:
#   fai questo se c'e' un eccezione
# else:
#   fai questo se non c'e' un eccezione
# finally:
#   non importa cosa succede, fai questo

# FileNotFoundError
try:
    data_file = open('a_file.txt')
    a_dictionary = {"key1": "value1", "key2": "value2"}
    value = a_dictionary["key1"]
except FileNotFoundError:
    data_file = open("a_file.txt", "w")
    data_file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exists.")
else:
    content = data_file.read()
    print(content)
finally:
    data_file.close()
    print("file closed.")
    # raise TypeError("This is not an error!")


# KeyError
# a_dictionary = {"key1": "value1", "key2": "value2"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["apple", "banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)
print(bmi)

