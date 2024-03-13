import os
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        question_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()


if __name__ == '__main__':
    # print(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    quiz = QuizInterface()