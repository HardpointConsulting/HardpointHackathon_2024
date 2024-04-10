# DragonSense AI: AI Powered Database Assistant for SMEs
**DragonSense AI** is an open-source project which utilises generative AI to address real-world challeneges faced by Small and Medium Enterprises(SMEs) with a user-friendly database assistant. Our goal is to help SMEs monitor their database and gaining valuable insights into their products in a manner that is both straightforward and time-saving.

## Problem Statement:
Many small and medium-sized enterprises (SMEs) struggle to efficiently leverage their databases to gain meaningful insights about their products.This results in SMEs facing challenges in optimizing their product strategies and decision-making processes.

## Solution:
**DragoneSense AI** is an generative AI tool which is specifically designed to address the problem statement mentioned.This tool would:
* Seamlessly integrate with SME's existing database.
* Utilize generative AI algorithms to analyze data within the database and provide valuable insights about the products and market trends.
* Provide a user-friendly interface for SMEs

## Technology:
This DragonSense AI is implemented using different technologies and alogirthms.
* **LangChain:** Langchain provides two key components for natural language-powered database interactions:\
      * SQLDatabase:Establishes a connection to your database.\
      * SQL DatabaseChain: Combines the SQLDatabase instance with a large language model(LLM) for text-to-SQL conversion.
* **Google Generative-AI:Text Bison:** For text-to-SQL conversion within the SQLDatabaseChain.
* **Machine Learning:** For text to speech and speech to text conversions.
## Getting Started:
1. **Create a virtual environment**
```
pip install virtualenv
virtualenv v_env
cd v_env/Scripts
activate
```
2. **Install `requirements.txt`**
```
pip install -r requirements.txt
```
3. **Create your own MySql Database and configure your variables in `database_config.py`**
```
username = "root"
password = "root"
host = "localhost"
database =  "atliq_tshirts"
```
4. **Get your Google API key from (https://aistudio.google.com/app/apikey) and create secret.py in the root folder. Enter your secret key**
```
secret_key="Your API key"
```
5. **Run the application**
```
python app.py
```
This will launch Dragonsense AI on your local machine. You can then access the user interface (usually at `http://localhost:5000`) and gain valuable insights about your products.

## Task Identification and Allocation:
* Gokul P : LLM Model
* Anurag Chandra : Web Devolopment
* Athul Menon: Voice to Text Module
* Gopika Babu : Text to Voice Module,Documentation
* Divya Devaraj : Documentation,Presentation

## Contribute:
We welcome contributions from the community! Feel free to:

* Fork the repository and propose changes through pull requests.
* Report bugs or suggest new features through GitHub issues.
* Share your ideas and experiences with DragonSense AI!

## For more details, check the original repository https://github.com/Anuragchandra221/LLM-AI-Tool
  


