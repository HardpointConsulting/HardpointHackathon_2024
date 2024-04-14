import streamlit as st
from langchain.document_loaders import DirectoryLoader,CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from PIL import Image
from dotenv import load_dotenv
from medical_email import analyze_medical_record
load_dotenv()
from streamlit_chat import message
import pandas as pd
import os


def save_image():
    uploaded_image = st.file_uploader("Upload your Medical Certificate", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        save_path = os.path.join("", uploaded_image.name)
        image.save(save_path)
        st.success(f"File {save_path} uploaded successfully...")
        uploaded_image = None
        return save_path
        
    

# To find the email of the employee
def find_mail(name):
    # Read the Excel file into a DataFrame
    excel_file = 'employeedata.xlsx'  # Provide the path to your Excel file
    df = pd.read_excel(excel_file)

    # Access the columns containing employee names and email addresses
    employee_names = df['username']  
    employee_emails = df['email']  

    # Iterate through the DataFrame to find the email corresponding to the given name
    for n, email in zip(employee_names, employee_emails):
        if n == name:
            return email

# Function to load documents
def load_docs(directory):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    return documents

# Function to split documents
def split_docs(documents, chunk_size=500, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

# Load documents

#contains HR Policy of the Company
directory = 'data/' 

documents = load_docs(directory)
docs = split_docs(documents)


# Embeddings
embeddings = OpenAIEmbeddings()

# Vector store
persist_directory = 'docs/chroma/'
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=persist_directory
)

#Load csv file
loader = CSVLoader('./data/employeedata.csv',encoding="windows-1252")
csv_doc = loader.load()

vectordb = Chroma.from_documents(
    documents=csv_doc,
    embedding=embeddings,
    persist_directory=persist_directory
)

# Language model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


# Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
username = "nobel"


# Build prompt

policy_template = """You are a virtual HR bot. You are taking to user named "admin". Answer "admin" quries precisely .Try to provide answers in maximum two sentences. Be polite and gentle. If you dont know the answer, say I don't know don't make up answers.
{context}

Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(policy_template)


# Run chains
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

def chatbot(username):
    # Streamlit app
    st.title("HR Bot")
    st.subheader(f"Welcome {username} 👋")


    if 'responses' not in st.session_state:
        st.session_state['responses'] = ["How can I assist you?"]

    if 'requests' not in st.session_state:
        st.session_state['requests'] = []


    # container for chat history
    response_container = st.container()
    # container for text box
    textcontainer = st.container()



    with textcontainer:
        # User input
        question = st.text_input("Enter your query:",value="",key='input')
        if question:
            if question == "apply for leave":
                p = save_image()
                if p:
                    print(p)
                    analyze_medical_record(p,find_mail(username))
                    st.session_state.requests.append(question)
                    response = "Check your email for leave status."
                    st.session_state.responses.append(response)
                    os.remove(p)
            else:   
                st.session_state.requests.append(question)
                result = qa_chain({"query": question})
                st.session_state.responses.append(result['result'])
            
        
        

    with response_container:
        if st.session_state['responses']:
            for i in range(len(st.session_state['responses'])):
                    message(st.session_state['responses'][i],key=str(i))
                    if i < len(st.session_state['requests']):
                        message(st.session_state["requests"][i], is_user=True,key=str(i)+ '_user')
