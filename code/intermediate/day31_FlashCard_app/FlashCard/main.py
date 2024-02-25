from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = read_csv("data/data_to_learn.csv")
except FileNotFoundError:
    data = read_csv("data/data.csv")
actual_word = None
dictionary = data.to_dict(orient="records")


# Functions
def set_flashcard(orientation="front", language="Deutch", word="word"):
    global canvas
    global bgimage
    canvas.delete("Language")
    canvas.delete("Word")
    canvas.itemconfig(bgimage, image=CARD_IMAGES[orientation])
    canvas.create_text(400, 158, text=f"{language}", font=("Ariel", 40, "italic"), tags="Language")
    canvas.create_text(400, 263, text=f"{word}", font=("Ariel", 60, "bold"), tags="Word")
    canvas.grid(row=0, column=0, columnspan=2)


def pick_word():
    global timer, actual_word
    window.after_cancel(timer)
    actual_word = random.choice(dictionary)
    # window.after_cancel(timer)
    set_flashcard(orientation="front", language="deutch", word=actual_word['Deutch'])
    timer = window.after(3000, set_flashcard, "back", "Italian", actual_word['Italian'])


def know_word():
    global data, actual_word
    if actual_word is not None:
        data = data.loc[data['Deutch'] != str(actual_word['Deutch'])]

    data.to_csv("data/data_to_learn.csv", index=False)
    pick_word()



# UI setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
CARD_IMAGES = {
    "front": PhotoImage(file=f"images/card_front.png"),
    "back": PhotoImage(file=f"images/card_back.png")
}

# R1
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bgimage = canvas.create_image(400, 263, image=CARD_IMAGES['front'])
timer = window.after(1, set_flashcard)
pick_word()

# R2
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=know_word)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_word)
wrong_button.grid(row=1, column=0)

window.mainloop()
