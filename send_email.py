import os
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(user, pwd, recipient, subject, body, fileName, filePath):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd

    msg = MIMEMultipart()
    msg['From'] = user
    TO = recipient if type(recipient) is list else [recipient]
    msg['To'] = recipient[0] +','+ recipient[1] +',' + recipient[2]
    msg['Subject'] = subject

    body = body
    
    msg.attach(MIMEText(body,'plain'))

    filename = fileName
    attachment = open(filePath, "r")

    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename = %s" % filename)

    msg.attach(part)
    text = msg.as_string()
    #print "======================================file name:%r" % filename
    #print "======================================attach name:%r" % attachment

    try:
        # connection to GMAIL
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        # send emails
        server.sendmail(user, TO, text)
        server.close()
        print 'successfully sent the mail'
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "failed to send mail"
