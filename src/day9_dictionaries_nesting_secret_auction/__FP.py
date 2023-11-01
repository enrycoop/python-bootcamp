from replit import clear
from __art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")


# First phase
offers = {}
answer = 'yes'
while answer.lower() != 'no':
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    offers[bid] = name
    answer = input("Are there any other bidders? Type 'yes' or 'no'. ")
    clear()


# Second phase
max_bid = 0
for bid in offers:
    if bid > max_bid:
        max_bid = bid

print(f"The winner is {offers[max_bid]} with an offer of {max_bid}")
