# mailmaker.py is a program that sends an email
# running from the command line:
#     mailmaker.py sender.txt password.txt receiver.txt subject.txt body.txt
# running from another python file:
#     import mailmaker
#     # sender, password, receiver, subject, and body are strings
#     mailmaker.sendEmail(sender, password, receiver, subject, body)

#         sender.txt - a single gmail address, the sender
#         password.txt - app password for the sender's gmail
#         receiver.txt - a single email address to send the email to
#         subject.txt - subject of the email
#         body.txt - main text of the email
#         NOTE: I reccommend that all text files contain only characters that can be typed on a US keyboard





import sys;
args = sys.argv[1 :]

# sender.txt password.txt receiver.txt subject.txt body.txt

from email.message import EmailMessage
import ssl
import smtplib


def sendEmail(sender, password, receiver, subject, body):

    context = ssl.create_default_context()
    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())
        print('sent')

if __name__ == '__main__':
    if len(args) != 5:
        args = 'sender.txt password.txt receiver.txt subject.txt body.txt'.split()
    sendEmail(*[open(arg).read() for arg in args])
