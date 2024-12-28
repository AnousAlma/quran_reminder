import os
from dotenv import load_dotenv
from email.message import EmailMessage
from email.utils import formataddr
import ssl
import smtplib

load_dotenv()

SENDER = "quranreminderbot@gmail.com"
try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    print("Password not found in environment variables")

CONTEXT = ssl.create_default_context()
PORT = 465


def send_email(receiver_email, urgent_surah, days, body):
    msg = EmailMessage()
    msg["From"] = formataddr(("Quaran Reminder", "quranreminderbot@gmail.com"))
    msg["To"] = receiver_email

    if days >= 4:
        subject = f"🟢 Reminder: {urgent_surah} in {days} days"
    elif days >=1:
        subject = f"🟡 Reminder: {urgent_surah} in {days} days"
    else:
        subject = f"🚨🚨🚨 Reminder: {urgent_surah.upper()} HAS TO BE DONE BY TODAY 🚨🚨🚨"

    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', PORT, context=CONTEXT) as smtp:
        smtp.login(SENDER, PASSWORD)
        smtp.sendmail(SENDER, receiver_email, msg.as_string())

# def send_email(receiver_email, surah, days):
#     msg = EmailMessage()
#     msg["From"] = formataddr(("Quaran Reminder", "quranreminderbot@gmail.com"))
#     msg["To"] = receiver_email

#     if days >= 4:
#         subject = f"🟢 Reminder: {surah} in {days} days"
#     elif days >=1:
#         subject = f"🟡 Reminder: {surah} in {days} days"
#     else:
#         subject = f"🚨🚨🚨 Reminder: {surah.upper()} HAS TO BE DONE BY TODAY 🚨🚨🚨"

#     msg["Subject"] = subject
#     msg.set_content(f"You have {days} days left to recite {surah}.")

#     with smtplib.SMTP_SSL('smtp.gmail.com', PORT, context=CONTEXT) as smtp:
#         smtp.login(SENDER, PASSWORD)
#         smtp.sendmail(SENDER, receiver_email, msg.as_string())

if __name__ == "__main__":
    send_email("anaskhaldoun2@gmail.com", "Al-Fatiha", 7)