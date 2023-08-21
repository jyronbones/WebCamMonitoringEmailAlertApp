import datetime
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
PASSWORD = os.getenv("PASSWORD")


def getDateTime():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime


def get_image_extension(image_path):
    try:
        with Image.open(image_path) as img:
            return img.format.lower()
    except Exception as e:
        print("Error:", e)
        return None


def send_email(image_path):
    image_extension = get_image_extension(image_path)
    if image_extension:
        email_message = EmailMessage()
        email_message["Subject"] = "Motion detected"
        email_message.set_content(f"Motion detected at: {getDateTime()}")

        with open(image_path, "rb") as file:
            content = file.read()

        email_message.add_attachment(content, maintype="image", subtype=image_extension)

        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(EMAIL_SENDER, PASSWORD)
        gmail.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message.as_string())
        gmail.quit()
    else:
        print("Failed to determine image extension.")
