print('Welcome to the tip calculator.')
dollars = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to givw? 10, 20, or 15? "))
people = int(input("How many people to split the bill? "))

percent = (1 + (percent/100))
total = round(dollars * percent, 2) / people

print(f'Each person should pay: ${round(total,2)}')