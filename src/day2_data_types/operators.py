3 + 5
7 - 4
3 * 2
print(6 / 3)  # hai sempre un float con una divisione
print(2 ** 3)  # 2 alla potenza di 3

# priorità operatori
# PEMDAS
# () Parenthesis
# ** Exp
# * / Mult division
# + - add subtract
print(3 * 3 + 3 / 3 - 3)

print(round(8 / 3, 2))  # 2.666666666666

print(8 // 3) # equivale a int(8 / 3)

result = 4 / 2
# result /= 2
# result += 1
# result -= 1
result *= 1
print(result)


# F Strings

score = 0
height = 1.8
isWinning = True
# f-string servono a combinare diversi tipi di dati in una stringa
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
