import smtplib
import os


class EmailManager:

    @staticmethod
    def send_email(text: str, receiver_email: str):
        """This functions receives a text and sends it as an email
        from 100days.day32@gmail.com to receiver_email"""
        # setting up variables
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "100days.day32@gmail.com"
        password = os.getenv("EMAIL_KEY")

        with smtplib.SMTP(smtp_server, port=port) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=receiver_email,
                msg=text.encode('utf-8')
            )
