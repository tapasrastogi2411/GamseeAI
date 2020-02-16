import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase  # For encoding basics
from email import encoders


email_user = 'noreplygameseeai@gmail.com'
email_send = input("Enter the email you want to receive the alert on: ")

while "@" not in email_send and '.com' not in email_send:
    print("Invalid input! Please re-enter correct email address")
    email_send = input("Enter the email you want to receive the alert on: ")

subject = 'Security Alert'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = """Hello, 

We recently detected a suspicious person/movement near your registered device. If you are not near your device, please make sure you device is safe secure.

Confidential Transmissions:
This message is intended only for the use of the individual to whom it is addressed, and may contain information that is privileged and confidential.  If the reader of 
this message is not the intended recipient, you are hereby notified that any dissemination, distribution, or copying of this communication is strictly prohibited. If you have received 
this communication in error, please notify the sender immediately by reply email and confirm you have permanently delete the original transmission, including attachments, without making a copy."""
msg.attach(MIMEText(body, 'plain'))

filename = 'Person_Image.jpg'

attachment = open(filename, 'rb') # Reading by bits

part = MIMEBase('application', 'octet-stream') # Allowing you to upload the attachemnt and then sending and then closing
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= '+filename)

msg.attach(part)

text = msg.as_string()
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email_user, "fufhd&fudfhd*")

# subject = "Super Secret Message for you"

server.sendmail(email_user, email_send, text)
server.quit()


