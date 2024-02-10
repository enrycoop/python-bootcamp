

with open("myfile.txt") as file:
    contents = file.read()
print(contents)


# il file viene creato se non esiste e se
with open("my_file.txt", mode="a") as file:
    file.write(contents)
print(contents)
