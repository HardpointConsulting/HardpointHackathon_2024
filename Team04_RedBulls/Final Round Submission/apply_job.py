import streamlit as st
import pandas as pd
from resume_email import evaluate_resume
from res_doc import analysis

def app():
    st.title("Job Application")
    st.header("Welcome Candidate 👋")
    st.subheader("Enter your details and upload your reusme")

    name = st.text_input("Full Name:")
    mob = st.text_input("Contact No.:")
    email_id = st.text_input("Email:")
    
    # analysis(email)
    st.write("Upload your Resume as PDF :")
    if st.button("Upload Resume"):
        analysis(email_id)
    if st.button("Submit"):
    # Create a DataFrame from the collected data
        data = {
            "Name": [name],
            "Contact": [mob],
            "Email ID": [email_id]
        }
        df = pd.DataFrame(data)
    
    # Export DataFrame to Excel
        file_path = "user_data.xlsx"
        df.to_excel(file_path, index=False)
        st.success(f"Application submitted successfully ✔ \n Note : Please check your email for futher proceedings...")
