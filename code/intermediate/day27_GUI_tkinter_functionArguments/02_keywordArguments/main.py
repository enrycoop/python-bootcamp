def add(*args):
    sum = 0
    for arg in args:
        sum += int(arg)
    return sum


print(add(1, 2, 3, 4, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, multiply=4, add=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs["model"]


my_car = Car(model="Nissan")
print(my_car.make)
