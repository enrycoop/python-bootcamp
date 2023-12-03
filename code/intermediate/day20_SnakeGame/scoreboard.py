from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Liberation Mono', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.speed("fastest")
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.refresh()
        self.hideturtle()

    def read_high_score(self):
        with open("data.txt") as file:
            score = int(file.read())
        return score

    def write_high_score(self, score):
        with open("data.txt", "w") as file:
            file.write(str(score))

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} Hih Score: {self.high_score}",
                   align=ALIGNMENT,
                   font=FONT)

    def increase(self):
        self.score += 1
        self.refresh()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(self.high_score)
        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.home()
    #     self.write(f"GAME OVER",
    #                align=ALIGNMENT,
    #                font=FONT)
