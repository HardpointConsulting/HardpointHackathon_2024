from sentence_transformers import SentenceTransformer
import pinecone
import openai
import streamlit as st
openai.api_key = "<OPENAI_API_KEY>"
model = SentenceTransformer('all-MiniLM-L6-v2')

pinecone.init(api_key='<PINECONE_APIKEY>', environment='<PINECONE_ENVIRONEMENT>')  #enter pinecone api key and environment
index = pinecone.Index('<PINECONE_INDEX_NAME>') #enter pinecone index name

def find_match(input):
    input_em = model.encode(input).tolist()
    result = index.query(input_em, top_k=2, includeMetadata=True)
    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']

def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):
        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
    return conversation_string
