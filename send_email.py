from email.mime.text import MIMEText
import smtplib

def send_email(email, height):
    from_email="ry6899@gmail.com"
    from_password="mohityadav6899"
    to_email=email

    subject="height data"
    message="hey here's your height :- %s" %height

    msg =MIMEText(message)
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
