# See https://docs.python.org/3.12/library/tkinter.html#tkinter.pack for documentation
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# padding aggiunge un po di riempimento per non farli tutti attaccati
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(padx=20, pady=20)
"""
Pack è il metodo di posizionamento più rapido ma impreciso.
Place è il più preciso ma meno versatile.
Grid è il più versatile e responsivo ed è relativo agli altri componenti.
Una volta scelto uno, puoi usare solo questo.
"""
my_label.grid(row=0, column=0)
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label.config(text=input_entry.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)
new_button = Button(text="Click New", command=button_clicked)
new_button.grid(row=0, column=2)

# Entry
input_entry = Entry(width=10)
input_entry.grid(row=2, column=3)
print(input_entry.get())

window.mainloop()
