##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
from pandas import *

from account import *

now = dt.datetime.now()

data = read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")
for birthday in birthdays:
    if now.month == birthday["month"] and now.day == birthday["day"]:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as template_file:
            template = [temp.replace("[NAME]", birthday['name']) for temp in template_file.readlines()]

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday['email'],
                    msg="Subject:Happy Birthday!!!!\n\n"+"".join(template))


#
# if dt.datetime.now().weekday() != 0:
#     exit()
#
# with open("quotes.txt", "r") as file:
#     quotes = [line.replace(" -", "\n -") for line in file.readlines()]
#     quote = random.choice(quotes)
#

#


