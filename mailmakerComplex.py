import sys;
args = sys.argv[1 :]

# sender, password, subject, body, (to), (cc), (bcc), (pdf)

from email.message import EmailMessage
import ssl
import smtplib

def sendEmail(sender, password, subject, body, to = None, cc = None, bcc = None, pdf = None):
    sender, password, subject, body = [open(arg).read() for arg in (sender, password, subject, body)]
    to, cc, bcc = [[] if not path else open(path).read().split() for path in (to, cc, bcc)]

    context = ssl.create_default_context()
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    smtp.login(sender, password)

    for receiver in to + cc + bcc:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = ', '.join(to)
        em['Cc'] = ', '.join(cc)
        em['Subject'] = subject
        em.set_content(body)
        # em['Subject'] = subject + ' ' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        # em.set_content(body) + '\n' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))

        if pdf:
            content = open(pdf, 'rb').read()
            em.add_attachment(content, maintype = 'application', subtype = 'pdf', filename = pdf)
        
        if receiver in bcc:
            em['Bcc'] = receiver
        
        smtp.sendmail(sender, receiver, em.as_string())
        print(f'sent to {receiver}')
    
if __name__ == '__main__':
    if not len(args):
        args = 'sender.txt password.txt subject.txt body.txt to.txt cc.txt bcc.txt resume.pdf'.split()
    sendEmail(*args)
