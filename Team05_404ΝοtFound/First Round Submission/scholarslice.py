import nltk
import pytesseract
from PIL import Image
import os
import re
import spacy
from transformers import T5Tokenizer, T5ForConditionalGeneration
import pandas as pd

# Download NLTK resources
nltk.download('punkt')

# Load English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Load the pre-trained T5 model and tokenizer for summary generation
tokenizer_summary = T5Tokenizer.from_pretrained("t5-small")
model_summary = T5ForConditionalGeneration.from_pretrained("t5-small")

# Load the pre-trained T5 model and tokenizer for title generation
tokenizer_title = T5Tokenizer.from_pretrained("t5-small")
model_title = T5ForConditionalGeneration.from_pretrained("t5-small")

# Function to clean extracted text
def clean_text(text):
    cleaned_text = text.replace("\n", " ").strip()
    return cleaned_text

# Function to check if text contains alphabetic characters
def contains_alphabetic(text):
    return any(char.isalpha() for char in text)

# Function to extract title from text blocks
def extract_title_from_text_blocks(text_blocks):
    # Initialize variables for title extraction
    title = ""
    max_font_size = 0
    max_text_length = 0

    # Keywords commonly found in headers
    header_keywords = ['abstract', 'introduction', 'method', 'results', 'discussion', 'conclusion','journal','revised','copyright','vol']

    # Iterate through each text block
    for block_text in text_blocks:
        # Default font size and position for now
        font_size = 12  # You may need to adjust this based on your data
        text_length = len(block_text)

        # Check if the text block contains alphabetic characters
        if contains_alphabetic(block_text):
            # Check if the block contains any header keywords
            contains_header_keyword = any(keyword in block_text.lower() for keyword in header_keywords)

            # Update title if font size is the largest seen so far and the block does not contain header keywords
            if font_size > max_font_size and text_length > max_text_length and not contains_header_keyword:
                title = block_text
                max_font_size = font_size
                max_text_length = text_length

    return title

# Function to generate alternative titles
def generate_alternative_titles(summary):
    # Generate the alternative titles
    inputs = tokenizer_title("summarize: " + summary, return_tensors="pt", max_length=512, truncation=True)
    outputs = model_title.generate(inputs.input_ids, max_length=50, num_beams=4, early_stopping=True)
    alternative_titles = [tokenizer_title.decode(output, skip_special_tokens=True) for output in outputs]

    # Post-processing: Truncate and capitalize the first letter of each title
    alternative_titles = [title[:50].capitalize() for title in alternative_titles]

    return alternative_titles

# Path to the directory containing PNG files
directory_path = 'C:\\Users\\amalg\\OneDrive\\Documents\\hackathon\\scientific_publication'

# List all PNG files in the directory
png_files_list = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith('.png')]

# Initialize lists to store data
titles = []
authors = []
alternative_titles_list = []

# Loop through each PNG file
for png_file_path in png_files_list:
    # Open the PNG file
    image = Image.open(png_file_path)

    # Use Tesseract OCR to extract text
    extracted_text = pytesseract.image_to_string(image)

    # Clean the extracted text
    cleaned_text = clean_text(extracted_text)

    # Apply NER
    doc = nlp(cleaned_text)

    # Extract person entities (likely authors)
    extracted_authors = [ent.text for ent in doc.ents if ent.label_ == "PERSON"][:3]
    authors.append(", ".join(extracted_authors))

    

    # Split the cleaned text into blocks based on punctuation or line breaks
    text_blocks = re.split(r'[.!?]', cleaned_text)
    text_blocks = [block.strip() for block in text_blocks if block.strip()]

    # Extract title from text blocks
    title = extract_title_from_text_blocks(text_blocks)

    titles.append(title)

    # Tokenize the input text for summary generation
    input_text_summary = "summarize: " + cleaned_text
    inputs_summary = tokenizer_summary(input_text_summary, return_tensors="pt", max_length=512, truncation=True)

    # Generate the summary
    summary_ids = model_summary.generate(inputs_summary.input_ids, max_length=150, num_beams=4, early_stopping=True)
    summary = tokenizer_summary.decode(summary_ids[0], skip_special_tokens=True)

    # Print the generated summary
    print("Generated Summary:", summary)

    # Generate alternative titles based on the summary
    alternative_titles = generate_alternative_titles(summary)
    alternative_titles_list.append(", ".join(alternative_titles))

# Create a DataFrame to store the data
data = {
    'Title': titles,
    'Authors': authors,
    'Alternative Titles': alternative_titles_list
}    

df = pd.DataFrame(data)

excel_file_path = 'C:\\Users\\amalg\\OneDrive\\Documents\\hackathon\\output.ods'
df.to_excel(excel_file_path, index=False)

print(f"Data written to {excel_file_path}")