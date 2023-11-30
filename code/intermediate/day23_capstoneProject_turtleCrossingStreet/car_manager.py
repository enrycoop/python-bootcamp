import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.frequency = 6
        self.cars = []

    def create_car(self):
        car = Turtle("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=2)
        car.goto(320, random.randint(-250, 250))
        self.cars.append(car)

    def move_on(self):
        for car in self.cars:
            car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())
