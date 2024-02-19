import json
import random
import pyperclip
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
LETTERS += [letter.upper() for letter in LETTERS]
NUMBERS = [str(n) for n in range(0, 10)]
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '+', '*']


def generate_password():
    password = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    password += [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
    password += [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
    random.shuffle(password)
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(password))
    pyperclip.copy(str(password_entry.get()))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = str(website_entry.get())
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="Password file not found.")
    else:
        # Updating old data
        if website not in data.keys():
            messagebox.showerror(title="Oops!", message=f"Password not found for the given website: '{website}'")
        else:
            messagebox.showinfo(title=f"{website}",
                                message=f"Email/User: \"{data[website]['username']}\"\nPassword:   \"{data[website]['password']}\"")
            pyperclip.copy(str(data[website]['password']))
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            username_entry.insert(0, data[website]['username'])
            password_entry.insert(0, data[website]['password'])


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = str(website_entry.get())
    username = str(username_entry.get())
    password = str(password_entry.get())
    new_data = {
        website: {
            'username': username,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving new data
                json.dump(data, data_file, indent=4)
        finally:
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

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(row=1, column=1)

find_password_button = Button(text="Search", width=14, command=find_password)
find_password_button.grid(row=1, column=2)

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
