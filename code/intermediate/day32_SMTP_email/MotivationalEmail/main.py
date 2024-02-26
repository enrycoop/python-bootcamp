import smtplib
import datetime as dt
import random

from account import *

if dt.datetime.now().weekday() != 0:
    exit()

with open("quotes.txt", "r") as file:
    quotes = [line.replace(" -", "\n -") for line in file.readlines()]
    quote = random.choice(quotes)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="johnpython1987@yahoo.com",
        msg="Subject:Monday Motivation\n\n"+quote)
