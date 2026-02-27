##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import datetime as dt
import  pandas as pd
import smtplib

name_constant = "[NAME]"
letters_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
my_email = "mysticman004@gmail.com"
my_password = "eznqnsfxvejuwwnm"


now = dt.datetime.now()
current_day = now.day
current_month = now.month

birthday_df = pd.read_csv("birthdays.csv")
birthdays = birthday_df.to_dict(orient = "records")

for birthday in birthdays:
    if birthday["day"] == current_day and birthday["month"] == current_month:
        birthday_today = birthday
        with open(random.choice(letters_list)) as birthday_letter_file:
            letter = birthday_letter_file.read()
        updated_letter = letter.replace(name_constant, birthday["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= my_email, password= my_password)
            connection.sendmail(from_addr= my_email,
                                to_addrs= birthday["email"],
                                msg= f"Subject:Birthday Wishes\n\n{updated_letter}")
