import random
# import my_module
# print(my_module.pi)

random_integer = random.randint(1, 9)
print(random_integer)

random_float = random.random() # genera tra 0 e 1
random_float += random_integer # genera tra 1 e 9 float
print(random_float)