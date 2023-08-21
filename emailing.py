import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your SendinBlue API key here
SMTP_KEY = os.getenv("SMTP_KEY")


def send_email():
    sender_email = os.getenv("EMAIL_SENDER")
    receiver_email = os.getenv("EMAIL_RECEIVER")
    subject = "Motion Detected"

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sendinblue_url = "https://api.sendinblue.com/v3/smtp/email"
    headers = {
        "api-key": SMTP_KEY,
        "Content-Type": "application/json",
    }

    # Create the email content
    email_content = {
        "sender": {"name": "Motion Detection App", "email": sender_email},
        "to": [{"email": receiver_email}],
        "subject": subject,
        "htmlContent": f"<p>Motion detected at: {timestamp}</p>",
    }

    # Send the email using SendinBlue API
    try:
        response = requests.post(sendinblue_url, json=email_content, headers=headers)
        response.raise_for_status()
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", str(e))
