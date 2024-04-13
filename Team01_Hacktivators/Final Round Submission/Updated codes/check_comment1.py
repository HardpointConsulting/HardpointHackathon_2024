from langchain.schema import (AIMessage, HumanMessage, SystemMessage)
from langchain.chat_models import ChatOpenAI
key = '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' #add openai secret key
chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature = 0.3, openai_api_key = key)
#
# response = chat(messages)
# print(response.content, end='\n')
def reply_comment(text):
    messages = [
        SystemMessage(
            content="Act as a human commenter in instagram. Reply to the query of the users. If it is related to price, availability, color answer them to dm us. If they want product ask them to dm. If they are giving good feedback, say thank you. For bad feedback say sorry"),
        HumanMessage(content=text)
    ]
    return chat(messages).content
