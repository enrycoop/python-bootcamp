import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FREQUENCY = 3

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

# Widgets
player = Player()


# Listeners
screen.onkey(player.up, "Up")
screen.listen()
car_manager = CarManager()

game_is_on = True

delay = 0
while game_is_on:
    time.sleep(0.1)
    car_manager.move_on()
    if delay == FREQUENCY:
        delay = 0
        car_manager.create_car()
    else:
        delay += 1
    screen.update()


