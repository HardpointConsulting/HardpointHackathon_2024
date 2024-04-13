import streamlit as st
import sqlite3
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
import streamlit as st
from streamlit_chat import message
from utils import *
from main import work


# Function to create a database connection
def create_connection():
    conn = sqlite3.connect('users.db')
    return conn

# Function to create a table for users
def create_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY NOT NULL,
             password TEXT NOT NULL);''')

# Function to add a default admin user
def add_default_user(conn):
    conn.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123')")

# Function to check if username and password match
def check_credentials(conn, username, password):
    cursor = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cursor.fetchone() is not None

# Main function for login page
def login_page(conn):
    st.title("Employee Login")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    # Login button
    if st.button("Login"):
        if check_credentials(conn, username, password):
            st.experimental_set_query_params(logged_in=True)
            work(username)
        else:
            st.error("Invalid Username or Password")
        

# Main function for home page

def main():
    # Create database connection
    conn = create_connection()
    # Create table for users if not exists
    create_table(conn)
    # Add default admin user if not exists
    add_default_user(conn)
    # Check if logged in based on query parameters
    if st.experimental_get_query_params().get("logged_in"):
        work(st.experimental_get_query_params().get("username"))
    else:
        login_page(conn)  # Pass the connection to the login page function

# Run the main function
if __name__ == "__main__":
    main()
