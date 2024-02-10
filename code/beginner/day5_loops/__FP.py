import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
letters += [letter.upper() for letter in letters]
numbers = [str(n) for n in range(0, 10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '+', '*']

print("Welcome to the PyPassword generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
'''
password = ''

for n in range(0, nr_letters):
    password += letters[random.randint(0,len(letters)-1)]
for n in range(0, nr_symbols):
    password += symbols[random.randint(0,len(symbols)-1)]
for n in range(0, nr_numbers):
    password += numbers[random.randint(0,len(numbers)-1)]
password = list(password)
for n in range(0, len(password)):
    i = random.randint(0,len(password)-1)
    j = random.randint(0,len(password)-1)
    temp = password[i]
    password[i] = password[j]
    password[j] = temp
password = ''.join(password)
'''
password = []
for n in range(0, nr_letters):
    password.append(random.choice(letters))
for n in range(0, nr_symbols):
    password.append(random.choice(symbols))
for n in range(0, nr_numbers):
    password.append(random.choice(numbers))
print(password)
random.shuffle(password)
print(password)
final = ''
for p in password:
    final += p
print(final)
