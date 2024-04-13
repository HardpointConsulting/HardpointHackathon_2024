import os
import streamlit as st
import pickle
import time
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

import pandas as pd
from sentence_transformers import SentenceTransformer
st.title("Research Your Equity..📄📄")
st.sidebar.title("Enter Article Urls...")
i=0
urls=[]    
while True:
    url_input = st.sidebar.text_input(f"URL {i+1}", key=f"url_input_{i+1}")
    if url_input:
        urls.append(url_input)
        i += 1
    else:
        break
process_url_clicked=st.sidebar.button("Process URLs..")
main_placefolder=st.empty()
Google_api_key="AIzaSyCwnN-9SnCfkl-ncRJY1mreo9qG-U_L9XM" #Api key
llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro",temperature=0.9,google_api_key=Google_api_key)#LLM initilizing
if process_url_clicked:

    loader=UnstructuredURLLoader(urls=urls)#Urls loading
    main_placefolder.text("Data Loading Started.......✅✅✅")
    data=loader.load()
    splitter=RecursiveCharacterTextSplitter( #Split the texts
    chunk_size=1000,
    chunk_overlap=200,
    )
    main_placefolder.text("Text Splitter Started.......✅✅✅")
    chunk=splitter.split_documents(data)
    # for i in chunk:
    #     print(i)
    embeddings=HuggingFaceEmbeddings()#Call Embeddings
    vectorindex=FAISS.from_documents(documents=chunk,embedding=embeddings)#Create indexes and store in faiss database
    main_placefolder.text("Embedding Vector Started Building.......✅✅✅")

    f=open("pickled.txt","wb")#Serialization
    pickle.dump(vectorindex,f)
    f.close()
question=main_placefolder.text_input("Question: ")
if question:
    f=open("pickled.txt","rb")#Deserialization
    vector=pickle.load(f)


    chain=RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vector.as_retriever())#Ancwer retrival
    print(chain)
    result=chain({"question":question})
    print(result)
    st.header("Answer")
    st.subheader(result["answer"])#Print Answer
