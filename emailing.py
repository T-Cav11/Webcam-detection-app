import smtplib
from email.message import EmailMessage
import filetype
import os

password = os.getenv("WEBCAM")
sender = "pythonprojectstc@gmail.com"
receiver = "pythonprojectstc@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()

    kind = filetype.guess(content)
    if kind is None:
        raise ValueError("Unsupported or unrecognized file type.")
    maintype, subtype = kind.mime.split('/')
    email_message.add_attachment(content, maintype=maintype, subtype=subtype, filename=image_path)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender,password=password)
    gmail.sendmail(sender,receiver,email_message.as_string())
    gmail.quit()


