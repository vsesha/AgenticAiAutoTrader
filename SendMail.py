import os
from dotenv import load_dotenv

import smtplib
from email.message import EmailMessage
from agents import function_tool


# Load environment variables to get OPENAI API key
load_dotenv()

SENDER_EMAIL_ID = os.getenv("SENDER_EMAIL_ID")
SENDER_EMAIL_PWD = os.getenv("SENDER_EMAIL_PWD")

@function_tool
def send_email(subject:str, body:str, receiver:str):
    """Sends an email using Gmail SMTP."""
    sender_email=SENDER_EMAIL_ID
    sender_password=SENDER_EMAIL_PWD  # Use an App Password for security
    #receiver_email=RECEIVER_EMAIL_ID
    receiver_email=receiver
    print("Receiver = ",receiver_email)
    
    # Create the email message
    msg = EmailMessage()

    msg.set_content(body)
    msg["Subject"]  = subject
    msg["From"]     = sender_email
    msg["To"]       = receiver_email

    # Connect to Gmail SMTP server
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f" Error sending email: {e}")

