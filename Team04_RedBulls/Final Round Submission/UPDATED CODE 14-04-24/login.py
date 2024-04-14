import streamlit as st
from employee_bot import chatbot
from utils import *
import pandas as pd

# Load the Excel database
def load_database():
    return pd.read_excel("employeedata.xlsx")

# Check user credentials
def authenticate_user(username, password, database):
    user = database[(database['username'] == username) & (database['password'] == password)]
    return not user.empty

# Main function for login page
def login_page(database):
    st.title("Employee Login 🔑")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password, database):
            st.session_state.logged_in = True
            st.session_state.username = username
            if st.session_state.logged_in:
                st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.username = None


# Main function for the app
def main():
    st.title("INFO TECH SOLUTIONS 💻")
    st.subheader("Welcome to our HR Bot")

    database = load_database()

    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None

    if st.session_state.logged_in:
        chatbot(st.session_state.username)
        if st.button("Logout"):
                logout()
    else:
        login_page(database)

if __name__ == "__main__":
    main()
