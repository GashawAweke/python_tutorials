# Modern approach:
from dotenv import load_dotenv
import os
from email.message import EmailMessage
import smtplib

message = EmailMessage()

message["From"] = "me@example.com"
message["To"] = "user@example.com"
message["Subject"] = "Welcome"

message.set_content("Hello from Python!")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login("me@example.com", "password")
    smtp.send_message(message)


# HTML Emails
message.add_alternative("""
<h1>Welcome</h1>
<p>Your account was created.</p>
""", subtype="html")


# Sending Attachments
with open("report.pdf", "rb") as file:
    data = file.read()

message.add_attachment(
    data,
    maintype="application",
    subtype="pdf",
    filename="report.pdf"
)


# Production Best Practices

# Never hardcode credentials:

# ❌ Bad:

smtp.login("user@gmail.com", "mypassword")

# ✅ Good:


email = os.getenv("EMAIL")
password = os.getenv("EMAIL_PASSWORD")

# Store secrets in :

# .env

# and load them with:

# pnpm add dotenv

# or in Python:

# pip install python-dotenv
# load_dotenv()
