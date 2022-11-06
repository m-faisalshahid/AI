from email.message import EmailMessage
import smtplib 
import ssl

# def send_email(email, height, average_height, count):
from_email ="techgoingcrazy@gmail.com"
from_password = "ggsevpgxukphggmy"
to_email = "mfaisalshahid789@gmail.com"

subject="Height data"
message = """Hey there, your height is  Average height of all is  and that is calculated out of people. Thanks! """

msg = EmailMessage()
msg['subject']=subject
msg['To']=to_email
msg['From']=from_email
msg.set_content(message)

context = ssl.create_default_context() 

with smtplib.SMTP_SSL('smtp.gmail.com',465, context= context ) as smtp:
    smtp.login(from_email,from_password)
    smtp.sendmail(from_email,to_email, msg.as_string())
