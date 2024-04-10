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
from medical_email import analyze_medical_record
from excel_email import find_mail




def work():

    # st.subheader("Chatbot with Langchain, ChatGPT, Pinecone, and Streamlit")
    st.title("HR Assistant")
    name = st.chat_input("Your name?")
    st.subheader(f"Welcome👋")
    

    if 'responses' not in st.session_state:
        st.session_state['responses'] = ["How can I assist you?"]

    if 'requests' not in st.session_state:
        st.session_state['requests'] = []

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="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")

    if 'buffer_memory' not in st.session_state:
                st.session_state.buffer_memory=ConversationBufferWindowMemory(k=3,return_messages=True)


    system_msg_template = SystemMessagePromptTemplate.from_template(template="""Answer the question as truthfully as possible using the provided context, 
    and if the answer is not contained within the text below, say 'I don't know'""")


    human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

    prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

    conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)




    # container for chat history
    response_container = st.container()
    # container for text box
    textcontainer = st.container()


    with textcontainer:
        query = st.text_input("Ask your quries: ", key="input")
        if query:
            with st.spinner("typing..."):
                conversation_string = get_conversation_string()
                if "apply for leave" in query:
                    from med_doc import analysis
                    email = find_mail(name)
                    analysis(email)
                    response = "Check your email for confirmation mail..."
                    st.session_state.responses.append(response) 
        
                    
                # st.code(conversation_string)
                # refined_query = query_refiner(conversation_string, query)
                # st.subheader("Refined Query:")
                # st.write(refined_query)
                # context = find_match(conversation_string)
                # print(context)  
                else:
                    response = conversation.predict(input=f"Context:\n {conversation_string} \n\n Query:\n{query}")
                    st.session_state.requests.append(query)
                    st.session_state.responses.append(response) 
    with response_container:
        if st.session_state['responses']:

            for i in range(len(st.session_state['responses'])):
                message(st.session_state['responses'][i],key=str(i))
                if i < len(st.session_state['requests']):
                    message(st.session_state["requests"][i], is_user=True,key=str(i)+ '_user')

            