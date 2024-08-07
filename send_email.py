import smtplib, ssl
import os

def send_email(message):
    host = "smpt.gmail.com"
    port = 465

    username = "app@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "app@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)