import streamlit as st
from datetime import datetime
import mailmakerComplex


def emailForm(userEmail, profEmail, subject, body, resumePath):
    form = st.form('sdkalfjdslajld form')
    # email address
    profEmail = form.text_input("Professor's email address", value = profEmail, help = 'This is the address that the email will be sent to.\nIf you\'re sending this to multiple addresses, please separate emails with spaces.')
    # subject
    subject = form.text_input("Subject", value = subject, help = 'This is the subject of the email that will be sent to the professor.')
    # body
    body = form.text_area("Content of the email", value = body, help = 'This is the content of the email that will be sent to the professor', height = 56 + 24 * body.count('\n'))
    submitted = form.form_submit_button('Send email')

    if submitted:

        # TODO: hide the form
        'Please wait as we send your email...'
        mailmakerComplex.sendEmail(subject, body, to = profEmail, bcc = userEmail, pdf = resumePath)
        'The email has been sent, and you have received a copy in your inbox.'
        st.balloons()



if __name__ == '__main__':
    userEmail = 'arnavgrover@gmail.com'
    profEmail = 'stooshievangooglie@gmail.com'
    subject = 'Filler subject at ' + datetime.now().strftime("%H:%M:%S")
    body = f'''Good day,
I am a student. I want to research with you at {datetime.now().strftime("%H:%M:%S")}.
I hope you accept my request.
I have my resume attatched.

Best regards,
Students McStudentson'''
    emailForm(userEmail, profEmail, subject, body, 'resume.pdf')
