from tkinter import *


def action():
    miles = float(entry.get())
    km = miles * 1.689
    result.config(text=str(km))


# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# 1st Row
# Entry
entry = Entry(width=7)
entry.insert(END, string="88")
entry.grid(row=0, column=1)

# Label
label = Label(text="Miles")
label.grid(row=0, column=2)

# 2nd Row
label = Label(text="Is Equal To")
label.grid(row=1, column=0)
result = Label(text="0")
result.grid(row=1, column=1)
label = Label(text="Km")
label.grid(row=1, column=2)


# 3rd Row
# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)

window.mainloop()
