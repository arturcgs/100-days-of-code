import requests
import smtplib
from datetime import datetime
import time

MY_LAT = -23.550520
MY_LGT = -46.633308


def is_night():
    # API
    params = {
        "lat": MY_LAT,
        "lgt": MY_LGT,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    # Selecting only the sunset and sunrise hour
    data = response.json()["results"]
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])
    # checking if it is dark right now
    hour_now = datetime.now().hour
    if hour_now > sunset or hour_now < sunrise:
        return True


def iss_is_above_me():
    """This function returns the currente ISS latitude and longitude
    both as float numbers"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()["iss_position"]
    iss_lat = float(data["latitude"])
    iss_lgt = float(data["longitude"])
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LGT - 5 <= iss_lgt <= MY_LGT + 5:
        return True


def send_email(text):
    """This functions receives a text and sends it as an email
    from 100days.day32@gmail.com to arturcaminero@gmail.com"""
    # setting up variables
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "100days.day32@gmail.com"
    password = "APP PASSWORD HERE"
    receiver_email = "arturcaminero@gmail.com"

    with smtplib.SMTP(smtp_server, port=port) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=text
        )


email_text = "Subject:Look Up!\n\nLook up into the sky and wonder.\nThe ISS is right above you!"
while True:
    time.sleep(60)
    if iss_is_above_me() and is_night():
        send_email(email_text)
