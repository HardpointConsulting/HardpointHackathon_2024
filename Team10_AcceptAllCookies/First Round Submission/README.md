First order of viewing the python files is  Title_Auth.py

This Python script utilizes the Tesseract OCR engine to extract text from images in a specified folder.
It configures Tesseract OCR, processes each image by converting it to grayscale, and performs Optical Character Recognition to extract text.
The script then saves the extracted text to text files corresponding to each image and attempts to identify the title and author information from the text.
Finally, it prints the extracted title and author details. This script provides a streamlined solution for extracting text, including title and author information, from images using Tesseract OCR.


Then , the next one is  summar.py


This code leverages a pre-trained BERT-based encoder-decoder model to generate summaries from text files. 
It first checks for GPU availability and initializes the necessary tokenizer and model.
The generate_summary function processes text inputs, tokenizes them, and generates summaries using the BERT model, limited to 512 tokens. 
The generate_summary_from_files function iterates through text files in a specified folder, generates summaries for each, and stores them. 
Finally, the code prints the summaries, offering a convenient way to summarize multiple text files efficiently.


Then we have the title_gen.py

This Python script automates the process of generating titles for text documents stored in a specified folder.
It begins by importing essential libraries such as os for file handling, rake_nltk for keyword extraction, nltk for natural language processing utilities, and transformers for leveraging a BERT-based model.
After downloading necessary NLTK resources, the script defines two functions: generate_title(text) and generate_title_from_files(folder_path). The former extracts keywords from input text using Rake, ranks them, and selects the top keyword as the title. 
The latter iterates through all text files in the designated folder, reads their content, invokes the generate_title function to create titles, and aggregates them in a list. 
Subsequently, it prints the generated titles for each text file in the folder. Overall, this script offers a straightforward yet effective solution for automatically generating titles for batches of text documents based on their content.


Atlast, we have the Excel.py

This code snippet utilizes pandas to create a DataFrame from lists of titles, authors, and generated titles extracted from text files. 
It first splits the input strings into lists and then constructs the DataFrame using these lists. The DataFrame is then written to an Excel file specified by the file path. 
Finally, a success message is printed upon successful generation of the Excel sheet. 
Overall, this code efficiently organizes and exports textual data into a structured Excel format for further analysis or sharing.
