import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = "example@gmail.com"
PASSWORD = "iwm9xTqSzsS6zUM"


def birthday_msg(name):
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        text = letter.read().replace("[NAME]", name)
    return text


def send_wisher(to_who):
    for idx, row in to_who.iterrows():
        name = row["name"]
        text = birthday_msg(name)
        email = row.email

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(to_addrs=email, from_addr=MY_EMAIL, msg=text)


now = dt.datetime.now()
month = now.month
day = now.day
birthdays_df = pd.read_csv("./birthdays.csv")
birthday_people = birthdays_df[(birthdays_df.month == month) & (birthdays_df.day == day)]
send_wisher(birthday_people)



