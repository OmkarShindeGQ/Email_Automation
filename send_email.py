import smtplib
from email.mime.text import MIMEText
import os

def send_email():
    msg = MIMEText("Hello! This is your daily automated email.")
    msg["Subject"] = "Daily Update"
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = os.environ["EMAIL_TO"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
        server.send_message(msg)

send_email()
