import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SMTP_KEY = os.getenv("SMTP_KEY")


def send_email():
    sender_email = os.getenv("EMAIL_SENDER")
    receiver_email = os.getenv("EMAIL_RECEIVER")
    subject = "Motion Detected"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sendinblue_url = "https://api.sendinblue.com/v3/smtp/email"
    headers = {
        "api-key": SMTP_KEY,
        "Content-Type": "application/json",
    }

    email_content = {
        "sender": {"name": "Motion Detection App", "email": sender_email},
        "to": [{"email": receiver_email}],
        "subject": subject,
        "htmlContent": f"<p>Motion detected at: {timestamp}</p>",
    }

    try:
        response = requests.post(sendinblue_url, json=email_content, headers=headers)
        response.raise_for_status()
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", str(e))
