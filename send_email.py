import smtplib
from email.mime.text import MIMEText
import os

def send_email():
    msg = MIMEText("Hello Rajat, this is your daily automated email.")
    msg["Subject"] = "Daily Update"
    msg["From"] = "omkar.shinde@grayquest.com"
    msg["To"] = "rajat.singh@grayquest.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("omkar.shinde@grayquest.com", os.environ["tdao xbnx cqwd nsbb"])
        server.send_message(msg)

send_email()
