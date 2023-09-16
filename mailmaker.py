# mailmaker.py is a program that sends an email

# example of running from the command line:
#     mailmaker.py sender.txt password.txt receiver.txt subject.txt body.txt

# example of running from another python file:
#     import mailmaker
#     mailmaker.sendEmail('sender.txt', 'password.txt', 'receiver.txt', 'subject.txt', 'body.txt')

#     arguments
#     mailmaker.sendEmail(sender, password, receiver, subject, body)
#         sender - a single gmail address, the sender
#         password - app password for the sender's gmail
#         receiver - a single email address to send the email to
#         subject - subject of the email
#         body - main text of the email
#         NOTE: I reccommend that all text files contain only characters that can be typed on a US keyboard




import sys;
args = sys.argv[1 :]

# sender password receiver subject body

from email.message import EmailMessage
import ssl
import smtplib

def sendEmail(sender, password, receiver, subject, body):
    sender, password, receiver, subject, body = [open(arg).read() for arg in (sender, password, receiver, subject, body)]

    context = ssl.create_default_context()
    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        print(em.as_string())
        smtp.sendmail(sender, receiver, em.as_string())
        print('sent')

if __name__ == '__main__':
    if len(args) != 5:
        args = 'sender.txt password.txt receiver.txt subject.txt body.txt'.split()
    sendEmail(*args)
