import random
from __art import art

print(art)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Type 'easy' or 'hard': ")

if difficulty == "easy":
    trials = 10
else:
    trials = 5

number = random.randint(0,100)
while True:
    print(f"You have {trials} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if number == guess:
        break
    elif guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    if trials > 1:
        print("Guess again.")
    else:
        break
    trials -= 1

if number == guess:
    print(f"You got it! The answer was {number}")
else:
    print("You've run out of guesses, you loose.")

    