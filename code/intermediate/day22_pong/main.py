import time
from turtle import Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


while True:
    screen.update()
    ball.go_forward()
    time.sleep(0.003)

    # detect collision with wall and bounce
    if ball.ycor() > 350:
        if ball.heading() < 90:
            ball.setheading(ball.heading() - 90)
        else:
            ball.setheading(ball.heading() + 90)

    if ball.ycor() < -350:
        if ball.heading() > 270:
            ball.setheading(ball.heading() + 90)
        else:
            ball.setheading(ball.heading() - 90)

    # detect collision with wall and bounce
    if ball.distance(r_paddle) < 10:
        if 90 > ball.heading() > 0:
            ball.setheading(ball.heading() + 90)
        else:
            ball.setheading(ball.heading() - 90)

    if ball.distance(l_paddle) < 10:
        if 180 > ball.heading() > 90:
            ball.setheading(ball.heading() - 90)
        else:
            ball.setheading(ball.heading() + 90)

    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.home()




screen.exitonclick()
