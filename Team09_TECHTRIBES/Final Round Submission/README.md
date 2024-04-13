# Research Your Equity..📄📄

## Introduction
This Streamlit application enables users to input URLs of articles they wish to analyze and ask questions related to the content of those articles. It utilizes various natural language processing tools and models to process the data and provide answers to user questions.

## Setup
Before running the application, make sure you have the necessary dependencies installed. You can install them using pip:

bash
pip install -r requirements.txt


## Usage
1. Run the application using the following command:

bash
streamlit run your_file_name.py
```

2. In the sidebar, enter the URLs of the articles you want to analyze. You can input multiple URLs.
3. Click the "Process URLs" button to initiate the analysis.
4. Once the data loading and processing are completed, you can input your question in the provided text box.
5. After entering your question, the application will generate an answer based on the content of the articles.

## Components
### Libraries Used:
- *os*: For interacting with the operating system.
- *streamlit*: For building interactive web applications.
- *pickle*: For serializing and deserializing Python objects.
- *time*: For time-related functions.
- *langchain*: A library for working with language models and natural language processing tasks.
- *langchain_google_genai*: A module providing access to Google's Generative AI models.
- *pandas*: For data manipulation and analysis.
- *sentence_transformers*: For computing embeddings of text sentences.

### Other Components:
- *Google API Key*: Replace "AIzaSyCwnN-9SnCfkl-ncRJY1mreo9qG-U_L9XM" with your own Google API key.
- *Model*: Uses the gemini-1.0-pro model from Google's Generative AI for generating responses.
- *Data Loading*: Articles' text is loaded from the provided URLs.
- *Text Splitting*: Splits the text into smaller chunks for processing.
- *Embedding Vector Building*: Constructs embedding vectors for the text chunks using Hugging Face's embeddings and FAISS for indexing.
- *Question Answering*: After processing, users can input questions, and the application provides answers based on the analyzed content.
