import time

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FREQUENCY = 6
MOVE_INCREMENT = 0.9
FINISH_LINE_Y = 280


screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

# Widgets
player = Player()
scoreboard = Scoreboard()


# Listeners
screen.onkey(player.up, "Up")
screen.listen()
car_manager = CarManager()

game_is_on = True
time_delay = 0.05
delay = 0
while game_is_on:
    time.sleep(time_delay)
    car_manager.move_on()
    screen.update()

    # create new turtle evey FREQUENCY time
    if delay == FREQUENCY:
        delay = 0
        car_manager.create_car()
    else:
        delay += 1

    # detect car collision
    for car in car_manager.cars:
        if player.distance(car) < 28:
            # detected collision
            game_is_on = False

    # detect if reach the other side
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_player()
        time_delay *= MOVE_INCREMENT
        scoreboard.level_up()

scoreboard.game_over()
screen.exitonclick()

