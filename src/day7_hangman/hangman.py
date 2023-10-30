import random
from ascii import stages, logo
from words import word_list

print(logo)


word = random.choice(word_list)
lives = len(stages) - 1
print(f"Pssss, the  solution is {word}")

display = []
word_length = len(word)
for _ in range(word_length):
    display += "_"
history = []
end_of_game = False
while not end_of_game:
    guess = input("choose a letter: ").lower()
    if guess in history:
        print(f"You've already insert {guess}!")
    else:
        history.append(guess)

    for i in range(word_length):
        if word[i] == guess:
            display[i] = word[i]

    print(f"{' '.join(display)}")
    print(stages[lives])

    if guess not in word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loose")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

