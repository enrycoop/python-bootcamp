# Declaration -> {Key: Value}

dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving item from dictionary
print(dictionary["Bug"])

# Adding new items to dictionary
dictionary["Loop"] = "The action of doing something over and over again."
print(dictionary)

# Empty dictionary
empty = {}

# wipe an existing dictionary
# dictionary = {}
# print(dictionary)

# Edit an item in a dictionary
dictionary["Bug"] = "A moth in your computer."
print(dictionary)

# Loop through a dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])
