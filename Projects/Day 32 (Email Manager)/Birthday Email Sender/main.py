import smtplib
import datetime as dt
import random
import pandas as pd


def send_email(text, receiver_email):
    """This functions receives a text and sends it as an email
    from 100days.day32@gmail.com to receiver_email"""
    # setting up variables
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "100days.day32@gmail.com"
    password = "tlfwgxoljllupscj"

    with smtplib.SMTP(smtp_server, port=port) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=text
        )


def get_birthday_message(birthday_line):
    # getting birthday message from file
    letter = f"letter_templates/letter{random.randint(1, 2)}.txt"
    with open(letter, "r") as f:
        message = f.read()
    # adding subject and changing name and age in message
    message = "Subject:Happy Birthday!\n\n" + message
    message = message.replace("[NAME]", birthday_line.name)
    message = message.replace("[AGE]", f"{year - birthday_line.year}")
    return message


# getting today's date
today = dt.datetime.today()
year = today.year
month = today.month
day = today.day

# importing birthdays csv
birthdays = pd.read_csv("birthdays.csv")

# getting only today's birthdays
today_birthdays = birthdays[(birthdays.month == month) & (birthdays.day == day)]
for birthday_person in today_birthdays.itertuples():
    birthday_message = get_birthday_message(birthday_person)
    send_email(text=birthday_message.encode('utf-8'), receiver_email=birthday_person.email)
