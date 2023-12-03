# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    template = letter_file.readlines()
print(template)

for name in names:
    stripped_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", "w") as output_file:
        for line in template:
            if PLACEHOLDER in line:
                output_file.write(line.replace(PLACEHOLDER, stripped_name))
            else:
                output_file.write(line)


