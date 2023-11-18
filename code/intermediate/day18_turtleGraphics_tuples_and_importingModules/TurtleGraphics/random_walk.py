from turtle import Turtle, Screen
import random

from prettytable import SINGLE_BORDER

COLORS = ["aquamarine4", "brown4", "burlywood4", "DarkSlateGrey",
          "DarkOrchid4", "LightCyan4", "gray40", "SeaGreen4", "SpringGreen4",
          "SteelBlue4"]
SPEED = 11
DIRECTIONS = [1, 3]
SINGLE_STEP = 2
MIN_STEP = 30
MAX_STEP = 100
PENSIZE = 20
DEEP = 0
frequency = 5
MAX_FREQUENCY = 3

DEEP_STATUSES = [
    {
        "name": "plane",
        "pensize": 10
    },
    {
        "name": "distant",
        "pensize": 5
    },
    {   
        "name": "closer",
        "pensize": 20
    }
]

def z_move():
    global DEEP
    global frequency
    old = DEEP
    
    a = DEEP_STATUSES[old]['pensize']
    if frequency > MAX_FREQUENCY:
        frequency = 0
        DEEP = random.randint(0,2)
        b = DEEP_STATUSES[DEEP]['pensize']
    else:
        frequency += 1
        b = a
    return a, b


def move(turtle):
    step = random.randint(MIN_STEP, MAX_STEP)

    deep_a, deep_b = z_move()
    if deep_a == deep_b:
        turtle.pensize(deep_a)
        for i in range(1, step):
            turtle.forward(SINGLE_STEP)
    elif deep_a > deep_b:
        deep_step = abs(deep_b - deep_a)/step 
        deep = deep_a
        for i in range(1, step):
            turtle.pensize(deep)
            deep -= deep_step
            turtle.forward(SINGLE_STEP)
    else:
        deep_step = abs(deep_b - deep_a)/step 
        deep = deep_a
        for i in range(1, step):
            turtle.pensize(deep)
            deep += deep_step
            turtle.forward(SINGLE_STEP)

def change_direction(turtle):
    turtle.right(90 * random.choice(DIRECTIONS))


screen = Screen()
screen.bgcolor("black")

tim = Turtle()
tim.color("bisque4")
tim.speed(10)


for _ in range(20):
    tim.color(random.choice(COLORS))
    for _ in range(20):
        change_direction(tim)
        move(tim)
    

screen.exitonclick()

        
