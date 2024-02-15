from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = str(website_entry.get())
    username = str(username_entry.get())
    password = str(password_entry.get())
    with open("data.txt", "a") as file:
        file.write(" | ".join([website, username, password]) + "\n")
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# R1
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# R2
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# R3
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=50)
username_entry.insert(END, "enricorobotic@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

# R4
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2)

# R5
add_button = Button(text="Add", width=42, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
