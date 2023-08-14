from bs4 import BeautifulSoup
import requests
import smtplib
import os

def send_email(email_text):
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


# getting website data
URL = "https://www.magazineluiza.com.br/console-valve-steam-deck-16gb-64gb-7-hd-60hz-bluetooth-wifi/p/cb669e660j/ga" \
      "/otga/?&seller_id=pedershop"
response = requests.get(URL)
live_page = response.text
soup = BeautifulSoup(live_page, "html.parser")

# finding the price
price_raw = soup.select_one("p.sc-kDvujY.jDmBNY.sc-hGglLj.bQqJoc")

price = int(price_raw.getText()[3:-3].replace(".", ""))

# price goal
price_goal = 2500

# send email if price is smaller

if price <= price_goal:
    text = f"Subject:SteamDeck Price Alert\nSteam deck is cheaper at Magazine Luiza! It is is currently at {price}, " \
           f"below the set price goal of {price_goal}.\nGo buy it here {URL}"
    send_email(email_text=text)


