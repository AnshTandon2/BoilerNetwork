import streamlit as st
from streamlit.logger import get_logger
from streamlit_card import card
from datetime import datetime
import sqlite3
import time
import pickle
import openai

st.set_page_config(
        page_title="Dashboard",
        page_icon="👋",
    )

class projectCard:
    def __init__(self, professorName, professorEmail, projectTitle, College, Department, researchArea, projectDescription, Qualifications, toApply):
        self.professorName = professorName
        self.professorEmail = professorEmail
        self.projectTitle = projectTitle
        self.College = College
        self.Department = Department
        self.researchArea = researchArea
        self.projectDescription = projectDescription
        self.Qualifications = Qualifications
        self.toApply = toApply

    def makeCard(self):
        project = card(
            title = self.projectTitle,
            text=[self.Department, self.professorName],
            image="https://t4.ftcdn.net/jpg/04/37/53/59/360_F_437535966_BeqAubSzmrhlniUjsJ5NQGj7l7r7yk20.jpg",
            styles={
                "card": {
                    "width": "500px",
                    "height": "200px",
                    "border-radius": "30px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                },
                "text": {
                    "font-family": "serif",
                }
            },
            on_click=self.nextpage
        )
    
    def nextpage(self):
        data = {
            "professorName" : self.professorName,
            "professorEmail": self.professorEmail,
            "projectTitle": self.projectTitle,
            "college": self.College,
            "department": self.Department,
            "researchArea": self.researchArea,
            "projectDescription": self.projectDescription,
            "qualifications": self.Qualifications,
            "toApply": self.toApply
        }
            # f"{self.professorName}\n{self.professorEmail}\n{self.projectTitle}\n{self.College}\n{self.Department}\n{self.researchArea}\n{self.projectDescription}\n{self.Qualifications}\n{self.toApply}"
        file_name = "streamlitEmbed/data/temp.txt"
        with open(file_name, 'wb') as file:
            pickle.dump(data, file)
        st.session_state.page += 1

project = projectCard("", "", "", "", "", "", "", "", "")

class User:
    def __init__(self, Name, Email, Resume, additionalInformation):
        self.Name = Name
        self.Email = Email
        self.Resume = Resume
        self.additionalInformation = additionalInformation
    def nextpage(self):
        data = {
            "userName": self.Name,
            "userEmail": self.Email,
            "resume": self.Resume,
            "additionalInformation": self.additionalInformation
        }
        # data = f"\n\n{self.Name}\n{self.Email}\n{self.Resume}\n{self.additionalInformation}"
        file_name = "streamlitEmbed/data/temp.txt"
        with open(file_name, 'rb') as file:
            existing_data = pickle.load(file)

        existing_data.update(data)

        with open(file_name, 'wb') as file:
            pickle.dump(existing_data, file)

        st.session_state.page += 1

user = User("", "", "", "")

def model():

    openai.api_key = "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"

    with open('streamlitEmbed/data/temp.txt', 'rb') as pickle_file:
        data = pickle.load(pickle_file)

    professorContext = (
        data["professorName"], 
        data["professorEmail"],
        data["projectTitle"],
        data["college"],
        data["department"],
        data["researchArea"],
        data["projectDescription"],
        data["qualifications"],
        data["toApply"]
        )

    userContext = (
        data["userName"],
        data["userEmail"],
        data["resume"],
        data["additionalInformation"]
        )

    prompt = f'''Write a descriptive email to a researcher about why you as an individual would be interested in working with them and learning from their experience. Explain why you think their project is interesting in the context of the problem description and your own background. Please be formal, use professional language, and reference the information in the documents to make a strong case for why you are a good candidate. Always say Best Regards, and your name at the end, and the beginning always include an introduction to yourself and why you are so passionate about the subject, please be heartfelt, cringey, and use varying sentence structure throughout. Be cordial as well! Be extremely descriptive and use complex vocabulary.
    Professor Research Project Context: {professorContext}
    Your Own Personal Context: {userContext}
    '''

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )

    answer = response.choices[0].text

    return answer

def nextpage(): st.session_state.page += 1

def backpage(): st.session_state.page -= 1

def back2page(): st.session_state.page -= 2

def restart(): st.session_state.page = 0

def dashboard():
    global project
    LOGGER = get_logger(__name__)

    dbPATH = "streamlitEmbed/data/opportunityDatabase.db"

    conn = sqlite3.connect(dbPATH)
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM opportunityDatabase')

    rows = cursor.fetchall()

    for row in rows:
        project = projectCard(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        project.makeCard()

    cursor.close()
    conn.close()

def user_info():
    global user
    st.title("Your Information")
    name = st.text_input("First & Last Name:")
    email = st.text_input("Email:")
    resume = st.file_uploader("Resume:")
    addInfo = st.text_area("Additional Info:")
    backButton = st.button("Back", on_click=backpage)
    user = User(name, email, resume, addInfo)
    if name and email and resume and ("@gmail.com" in email or "@purdue.edu" in email):
        generateButton = st.button("Generate", type="primary", on_click=user.nextpage)

def generating():

    answer = model()

    data = {
        "emailBody" : answer
    }

    file_name = "streamlitEmbed/data/temp.txt"
    with open(file_name, 'rb') as file:
        existing_data = pickle.load(file)

    existing_data.update(data)

    with open(file_name, 'wb') as file:
        pickle.dump(existing_data, file)

    progress_text = "Generating..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

    st.success('Email Generated!')
    st.button("Next", on_click=nextpage)

def emailForm(userEmail, profEmail, subject, body, resumePath):
    form = st.form('sdkalfjdslajld form')
    #your email
    usEmail = form.text_input("Your Email", value=userEmail)
    # email address
    profEmail = form.text_input("Professor's email address", value = profEmail, help = 'This is the address that the email will be sent to.\nIf you\'re sending this to multiple addresses, please separate emails with spaces.')
    # subject
    subject = form.text_input("Subject", value = subject, help = 'This is the subject of the email that will be sent to the professor.')
    # body
    body = form.text_area("Content of the email", value = body, help = 'This is the content of the email that will be sent to the professor', height = 56 + 24 * body.count('\n'))
    submitted = form.form_submit_button('Send email')
    backButton = st.button("Back", on_click=back2page)

    if submitted:
        'Please wait as we send your email...'
        mailmakerComplex.sendEmail(subject, body, to = profEmail, bcc = userEmail, pdf = resumePath)
        'The email has been sent, and you have received a copy in your inbox.'
        st.balloons()
        nextButton = st.button("RESTART", on_click=restart)

if "page" not in st.session_state:
    st.session_state.page = 0

placeholder = st.empty()

if st.session_state.page == 0:
    dashboard()

elif st.session_state.page == 1:
    user_info()

elif st.session_state.page == 2:
    generating()

elif st.session_state.page == 3:
    file_name = "streamlitEmbed/data/temp.txt"
    with open(file_name, 'rb') as file:
        loaded_data = pickle.load(file)

    emailForm(loaded_data["userEmail"], loaded_data["professorEmail"], "SUBJECT", loaded_data["emailBody"], loaded_data["resume"])

else:
    with placeholder:
        st.button("Restart", on_click=restart) 
        placeholder = st.empty()