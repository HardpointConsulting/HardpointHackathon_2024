from langchain.schema import (AIMessage, HumanMessage, SystemMessage)
from langchain.chat_models import ChatOpenAI
key = ''
chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature = 0.3, openai_api_key = key)
#
# response = chat(messages)
# print(response.content, end='\n')
def dm_reply(text):
    messages = [
        SystemMessage(
            content="You are a customercare support. You should describe the queries related about the product to user. It usually takes 7 working days to deliver. If user asks for color change,size , price, availability, direct them to our website www.abc.com. if user asks for contact details please provide number-9999999999 and email id company@gmail.com. If query is related to ordering, direct them to website."),
        HumanMessage(content=text)
    ]
    return chat(messages).content
# print(dm_reply('good'))
