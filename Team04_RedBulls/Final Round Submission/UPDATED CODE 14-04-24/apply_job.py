import streamlit as st
import pandas as pd
from resume_email import evaluate_resume
import os

def upload_pdf():
    # Display file uploader widget
    uploaded_file = st.file_uploader("Upload your Resume", type=["pdf"])

    if uploaded_file is not None:
        # Save the uploaded file to a specified directory
        save_path = ""
        file_path = os.path.join(save_path, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        # Calculate the relative file path
        relative_path = os.path.relpath(file_path, os.getcwd())
        print(relative_path)
        
        # Return the relative file path
        return relative_path


def app():
    st.title("Job Application")
    st.header("Welcome Candidate 👋")
    st.subheader("Enter your details and upload your reusme")

    name = st.text_input("Full Name:")
    mob = st.text_input("Contact No.:")
    email_id = st.text_input("Email:")
    
    uploaded_file_path = upload_pdf()
  
    # Create a DataFrame from the collected data
    data = {
        "Name": [name],
        "Contact": [mob],
        "Email ID": [email_id]
    }
    df = pd.DataFrame(data)
    
    # Export DataFrame to Excel
    file_path = "user_data.xlsx"
    
    if st.button("Submit"):
        if uploaded_file_path:
            df.to_excel(file_path, index=False)
            st.success(f"File {uploaded_file_path} uploaded succesfully....")
            evaluate_resume(uploaded_file_path,email_id,name)
            os.remove(uploaded_file_path)
        st.success(f"Application submitted successfully ✔ \n Note : Please check your email for futher proceedings...")