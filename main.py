import streamlit as st
import pandas as pd
from PIL import Image
import base64

# Set page title and icon
st.set_page_config(
    page_title="BOILER NETWORKING",
    page_icon="🏫",
)

# Page header
st.title("Professor Survey Form")

st.subheader("A platform that automates the grueling and laborious process that Purdue students have to " 
+ "endure when sending messages to network with professors for research/internship opportunities")

# Create a form to collect professor information
with st.form("Professor Information"):
    professor_name = st.text_input("Professor's Name")
    professor_email = st.text_input("Professor's Email")
    research_paper_link = st.text_input("Link to Past Research Paper")
    student_resume = st.file_uploader("Upload Student's Resume (PDF)")

    # Submit button
    submitted = st.form_submit_button("Submit")

# Process the submitted data
if submitted:
    # Display professor information
    st.subheader("Professor Information:")
    st.write(f"Name: {professor_name}")
    st.write(f"Email: {professor_email}")
    st.write(f"Research Paper Link: {research_paper_link}")

    # Display uploaded student's resume if available
    if student_resume is not None:
        st.subheader("Student's Resume:")
        st.write("File name:", student_resume.name)
        st.write("File type:", student_resume.type)
        
        # You can choose to save the uploaded file if needed
        # with open(student_resume.name, "wb") as f:
        #     f.write(student_resume.getvalue())
        
    st.success("Survey submitted successfully!")

# Add a footer or additional information if needed
st.markdown("""
## Additional Information

You can add more text or explanations here.
""")
