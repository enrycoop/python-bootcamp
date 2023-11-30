from turtle import Turtle
POSITION = (-200, 250)
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(POSITION)
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)
