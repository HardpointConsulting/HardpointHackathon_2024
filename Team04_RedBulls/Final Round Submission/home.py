import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu

import login,apply_job

st.set_page_config(
    page_title="HR-Assistant",
    page_icon="🤖"
)

class MultiApp:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            "title" : title,
            "function" : function,
        })
    def run():
        with st.sidebar:
            selected = option_menu(
            menu_title="HR-Assistant",
            options = ["Employee Login","Apply Job"],
            menu_icon="🤖"
            )
        if selected == "Employee Login":
            login.main()
        if selected == "Apply Job":
            apply_job.app()

# Run the main function
    run()
