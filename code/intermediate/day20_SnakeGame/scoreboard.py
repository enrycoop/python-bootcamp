from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Liberation Mono', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.refresh()
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   align=ALIGNMENT,
                   font=FONT)

    def increase(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write(f"GAME OVER",
                   align=ALIGNMENT,
                   font=FONT)