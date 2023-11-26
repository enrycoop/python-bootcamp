import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

# setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

# game widgets
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

# setup command listeners
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# start game logic
while True:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # detect collision with wall and bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330\
            or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detect R paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.r_point()

    # detect L paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.l_point()
