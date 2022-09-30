import smtplib
import datetime as dt
import random


def send_email(text):
    """This functions receives a text and sends it as an email
    from 100days.day32@gmail.com to arturcaminero@gmail.com"""
    # setting up variables
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "100days.day32@gmail.com"
    password = "tlfwgxoljllupscj"
    receiver_email = "arturcaminero@gmail.com"

    print("sending email")
    with smtplib.SMTP(smtp_server, port=port) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=text
        )
    print("email sent")


# reading quotes file
with open("quotes.txt", "r") as f:
    quotes = f.readlines()

# checking if it is monday
weekday = dt.datetime.now().weekday()
if weekday == 1:
    # creating email text
    email_text = f"Subject:Monday Motivation!\n\n{random.choice(quotes)}"
    # send email
    send_email(email_text)
