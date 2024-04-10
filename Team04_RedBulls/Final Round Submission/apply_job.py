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
    email = st.text_input("Email:")
    
    # analysis(email)
    if st.button("Submit"):
    # Create a DataFrame from the collected data
        data = {
            "Name": [name],
            "Contact": [mob],
            "Email ID": [email]
        }
        df = pd.DataFrame(data)
    
    # Export DataFrame to Excel
        file_path = "user_data.xlsx"
        df.to_excel(file_path, index=False)
        st.success(f"Details Entered Successfully ✔")