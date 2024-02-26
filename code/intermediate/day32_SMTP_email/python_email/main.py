import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="johnpython1987@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of the message")

