import os
import re
import textwrap
from datetime import datetime

import pytesseract as pyt
from PIL import Image
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
from langchain.chat_models import ChatOpenAI



def analyze_medical_record(image_path):
    """
    Analyze a medical record image.

    Args:
    - image_path (str): The path to the image file containing the medical record.

    Returns:
    - dict: A dictionary containing extracted information from the medical record.
    """
    # Function to perform OCR (Optical Character Recognition) on the given image
    def perform_ocr(image_path):
        try:
            img = Image.open(image_path)
            pyt.pytesseract.tesseract_cmd = "Tesseract-OCR\\tesseract.exe"
            text = pyt.image_to_string(img)
            return text
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print("An error occurred:", str(e))
            return None

    # Function to create a text file with the OCR result of the given image
    def create_file(image_path):
        try:
            with open("sample.txt", "w") as file:
                file.write(perform_ocr(image_path))
            print("File created successfully.")
        except Exception as e:
            print("An error occurred:", str(e))

    # Function to extract the first number found in the input string
    def extract_number(input_string):
        match = re.search(r'\b(\d+)\b', input_string)
        if match:
            return int(match.group(1))
        else:
            return None

    # Function to standardize the input date string into "dd-mm-yyyy" format
    def standardize_date(input_date):
        try:
            date_formats = ["%d-%m-%Y", "%m-%d-%Y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%d %b %Y", "%B %d, %Y"]
            for date_format in date_formats:
                try:
                    parsed_date = datetime.strptime(input_date, date_format)
                    return parsed_date.strftime("%d-%m-%Y")
                except ValueError:
                    pass
            return None
        except Exception as e:
            print("Error:", e)
            return None
    def extract_data(doc_result,query):
        try:
            result = chain.run(input_documents=doc_result, question=query)
        except:
            result = "NA"
        return result
    
    # Set Hugging Face Hub API token
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

    # OCR and process the image
    create_file(image_path)

    # Load text from the created file
    loader = TextLoader("sample.txt")
    document = loader.load()

    # Text Splitting
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(document)

    # Embedding
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    # Q-A
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="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")
    chain = load_qa_chain(llm, chain_type="stuff")


    # Query to extract information
    queries = ["patient's name in one word", "doctor's name in one word", "medical examination date in one word", "name of the disease in one word", "days of leave just give number"]

    # Perform Q-A for each query
    results = {}
    for query in queries:
        doc_result = db.similarity_search(query)
        result = extract_data(doc_result,query)
        # if query == "number of days leave applied for":
        #     result = extract_number(result)
        # if query == "date mentioned":
        #     result = standardize_date(result)
        results[query] = result

# Delete the text file
    # try:
    #     os.remove("sample.txt")
    #     print("File deleted successfully.")
    # except FileNotFoundError:
    #     print("File not found.")

    return results
image_path = 'medical2.jpg'
extracted_info = analyze_medical_record(image_path)
print(extracted_info)