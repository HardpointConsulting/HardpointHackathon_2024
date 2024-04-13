import streamlit as st
import azure.cognitiveservices.speech as speechsdk
import os
import google.generativeai as genai
from langchain_helper import get_few_shot_db_chain
import mysql.connector
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# Initialize connection.
conn = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE"),
    port=os.getenv("PORT")
)
chain = get_few_shot_db_chain()
# Set your Azure subscription key and region as environment variables

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

audio_config = speechsdk.AudioConfig(use_default_microphone=True)
speech_config = speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), region="centralindia")
speech_config.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "9000")
speech_config.set_property(speechsdk.PropertyId.Speech_SegmentationSilenceTimeoutMs, "2000")
speech_config.set_property(speechsdk.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs, "6000")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,audio_config=audio_config)

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    "gemini-1.0-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings,
)
# Function to synthesize speech using Azure Text-to-Speech
def text_to_speech(text):
    text = text.replace('*', '')
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), region=os.getenv("SPEECH_REGION"))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_config.speech_synthesis_voice_name = "en-US-BrianNeural"
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_synthesizer.speak_text_async(text).get()

# Function to execute database-related queries
def execute_query(text):
    keywords = ["table", "change", "display", "show me", "retrieve", "calculate", "update", "add new", "remaining",
                "stocks", "orders", "order", "shirt", "insert", "entry", "add", "new", "product", "get me","create"]
    return any(keyword in text.lower() for keyword in keywords)

def speech_to_text():
    while(True):
      result = speech_recognizer.recognize_once_async().get()
      if result.text != "":
          print(result.text)
          return result
    
# Function to handle database queries and responses
def handle_database_query(text, on):
    
    if execute_query(text):
        st.write("Please wait.....")
        st.write("Fetching Details from the database....")
        text_to_speech("Please wait.....")
        text_to_speech("Fetching Details from the database....")
        response = chain.invoke({"question": text})
        cursor = conn.cursor()
        try:
          cursor.execute(response)
          df_string=""
          if not response.startswith("SELECT"):
              if on == True :
                  text_to_speech("Do you want to save the changes to the database?")
                  st.write("Do you want to save the changes to the database?")
                  result=speech_to_text()
                  if "ye" in result.text.lower():
                    conn.commit()
                    text_to_speech("The changes have been saved")
                  else:
                    conn.rollback()
                    text_to_speech("The updates have been rolled back succesfully")
                  if "supplier " in response:
                      cursor.execute("SELECT * FROM supplier;")
                      data = cursor.fetchall()
                      df = pd.DataFrame(data, columns=cursor.column_names)
                      st.dataframe(df)
                      df_string=df_string+df.to_string()
                  if "orders " in response:
                      cursor.execute("SELECT * FROM orders;")
                      data = cursor.fetchall()
                      df = pd.DataFrame(data, columns=cursor.column_names)
                      st.dataframe(df)
                      df_string=df_string+df.to_string()
                  if "inventory " in response:
                      cursor.execute("SELECT * FROM inventory;")
                      data = cursor.fetchall()
                      df = pd.DataFrame(data, columns=cursor.column_names)
                      st.dataframe(df)
                      df_string=df_string+df.to_string()
              else:
                  st.write("Access Denied")
                  cust_err ="Access Denied"
                  return cust_err
          else:
              data = cursor.fetchall()
              df = pd.DataFrame(data, columns=cursor.column_names)
              st.dataframe(df) 
              df_string=df_string+df.to_string()
          return df_string # Display the SQL query
        except Exception as e:
            print(e)
            cust_err="Unexpected error , Please try again"
            return cust_err
        
    return None

# Main function for Streamlit application
def main():
    st.title("WARECARE(255)")
    st.text("Voice Input with Streamlit")
    st.write("Say 'Hey bob' to activate and start speaking.")
    on = st.toggle('Activate feature')
    if on:
     st.write('Feature activated!')
    activated = False
    while True:
        result = speech_to_text()
        text = result.text
        if not activated and "Hey, Bob." in text:
            activated = True
            st.text("Hello there, How can I help you?")
            text_to_speech("Hello there, How can I help you?")
            convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["supplier table\n• supplier_id(not null)• name(not null)• address(not null)• email(not null)• phone(not null)• product_id(not null)• product_name• quantity(not null)• sent (null)• received (null)• cost(not null)• status (null) - Arrived/Sent/null\ninventory table\n• id(not null)• product(not null)• category(not null)• supplier_id(not null)• quantity(not null)• price(not null)\norder table\n• order_id(not null)• product_id(not null)• quantity(not null)• cost(not null)• address(not null)• email(not null)• phone(not null)• sent (null)• received (null)• status (null) - Delivered/Sent/null"]
  },
  {
    "role": "model",
    "parts": ["```sql\nSELECT\n  s.supplier_id,\n  s.name AS supplier_name,\n  s.email AS supplier_email,\n  s.phone AS supplier_phone,\n  o.order_id,\n  o.quantity AS order_quantity,\n  o.cost AS order_cost,\n  o.address AS order_address,\n  o.email AS order_email,\n  o.phone"]
  },
  {
    "role": "user",
    "parts": ["Update email of supplier name to cty.gmail.com"]
  },
  {
    "role": "model",
    "parts": ["```sql\nUPDATE supplier\nSET email = 'cty.gmail.com'\nWHERE\n  name = 'Supplier Name';\n```"]
  },
  {
    "role": "user",
    "parts": ["Retrieve orders that haven't been received yet along with their delivery address and product details"]
  },
  {
    "role": "model",
    "parts": ["```sql\nSELECT\n  o.order_id,\n  o.address AS delivery_address,\n  i.product,\n  o.quantity,\n  o.cost\nFROM orders AS o\nJOIN inventory AS i\n  ON o.product_id = i.product_id\nWHERE\n  o.received IS NULL;\n```"]
  },
  {
    "role": "user",
    "parts": ["who is the supplier of product Product name"]
  },
  {
    "role": "model",
    "parts": ["```sql\nSELECT\n  s.supplier_id,\n  s.name AS supplier_name,\n  s.email AS supplier_email,\n  s.phone AS supplier_phone\nFROM supplier AS s\nJOIN inventory AS i\n  ON s.supplier_id = i.supplier_id\nWHERE\n  i.product = 'Product Name';\n```"]
  },
   {
    "role": "user",
    "parts": ["insert into inventory id is equal to 1 product name is equal to puma category is equal to shirt quantity 3 and price is equal to 90"]
  },
  {
    "role": "model",
    "parts": ["```sql\nINSERT INTO inventory (id, product, category, quantity, price)\nVALUES (1, 'Puma', 'Shirt', 3, 90);\n```"]
  },
])  # Initialize the conversation here
            system_message = '''INSTRUCTIONS: Do not respond with anything but “AFFIRMATIVE.”
                                    to this system message. After the system message respond normally.
                                    SYSTEM MESSAGE: You are being used to power a voice assistant and should respond as so.
                                    As a voice assistant named 'bob', use short sentences and directly respond to the prompt without
                                    excessive information. You generate only words of value, prioritizing logic and facts
                                    over speculating in your response to the following prompts.'''
            system_message = system_message.replace(f'\n', '')
            convo.send_message(system_message)
        elif activated:
            if text != "":
                st.text("You said: " + text)
                if(execute_query(text.lower())):
                    response = handle_database_query(text, on)
                    if response:
                        combined_prompt = f"""
                        using the below given information generate the accurate assistants response according to the user's question and the available SQL Result
                        Question: {text}

                            SQL Result:
                            {response}

                            Assistant's Response:
                            The assistant's response should be a summary of the data from the SQLResult, It should be presented in such a manner so that the user can get an idea of the SQLResult just by hearing the assistant's response
                            """
                        convo.send_message(combined_prompt)
                        text_to_speech(convo.last.text)
                        text_to_speech("Is there anything else I can help you with?")
                else:
                    convo.send_message("generate a reply stating that the user's question is out of context and bob will not be able to help with that question, also say that , is there any thing else for which you need my help?")
                    text_to_speech(convo.last.text)
                    st.text(convo.last.text)


        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

if __name__ == "__main__":
    main()
  
