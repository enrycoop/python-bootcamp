target = 1000
for n in range(1, target + 1):
    number = ''
    if n % 3 == 0:
        number += 'Fizz'
    if n % 5 == 0:
        number += 'Buzz'
    if number == '':
        number = str(n)
    print(number)
