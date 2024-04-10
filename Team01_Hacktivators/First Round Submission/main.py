import pytesseract
from transformers import BartForConditionalGeneration, BartTokenizer
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import openpyxl

# Initialize OCR engine
try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
except Exception as e:
    print("Error while configuring Tesseract OCR:", e)

# Initialize BART for title generation
try:
    bart_model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    bart_tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
except Exception as e:
    print("Error while initializing BART model:", e)

# Initialize spaCy NLP pipeline
try:
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    print("Error while initializing spaCy NLP pipeline:", e)

# Function to extract text from printed documents using OCR
def extract_text_from_document(image_path):
    try:
        text = pytesseract.image_to_string(image_path)
        return text
    except Exception as e:
        print("Error during text extraction from document:", e)
        return None

# Function to extract title from text
def extract_title(text):
    try:
        lines = text.split('\n')
        title = lines[0] if lines else "Untitled Document"
        return title
    except Exception as e:
        print("Error during title extraction:", e)
        return "Untitled Document"

# Function to extract authors from the initial sentence using spaCy NER
def extract_authors(text):
    try:
        # Split the text into sentences
        sentences = nlp(text).sents
        # Iterate through sentences until a sentence with a PERSON entity is found
        for sentence in sentences:
            # Extract PERSON entities from the sentence
            authors = [ent.text for ent in sentence.ents if ent.label_ == "PERSON"]
            if authors:
                return authors  # Return the authors found in the first sentence
        return []  # Return an empty list if no authors are found
    except Exception as e:
        print("Error during author extraction:", e)
        return []

# Function for content analysis and alternative title generation
def generate_alternative_titles(text):
    try:
        summarizer = LexRankSummarizer()
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summary = summarizer(parser.document, 2)  # Generate a 2-sentence summary

        # Truncate text if it's too long for BART
        max_input_length = 1024  # Maximum input length for BART model
        if len(text) > max_input_length:
            text = text[:max_input_length]

        input_text = "summarize: " + text  # Prefix for BART summarization
        input_ids = bart_tokenizer.encode(input_text, max_length=1024, truncation=True, return_tensors='pt')
        output = bart_model.generate(input_ids, max_length=100, num_beams=4, early_stopping=True)
        alternative_titles = [bart_tokenizer.decode(title, skip_special_tokens=True) for title in output]

        return summary, alternative_titles
    except Exception as e:
        print("Error during alternative title generation:", e)
        return [], []

# Example usage
try:
    import os
    # Create a new workbook
    workbook = openpyxl.Workbook()

    # Select the active sheet
    sheet = workbook.active

    # Define headings for each column
    headings = ["Document Title", "Author(s)", "Generated Title"]

    # Add headings to the Excel sheet
    for col, heading in enumerate(headings, start=1):
        sheet.cell(row=1, column=col, value=heading)
# Directory containing document images
    dataset_dir = "scientific_publication/scientific_publication"

# Iterate over each image in the dataset
    for filename in os.listdir(dataset_dir):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(dataset_dir, filename)
            text_from_document = extract_text_from_document(image_path)
            if text_from_document:
                title = extract_title(text_from_document)
                authors = extract_authors(text_from_document)
                summary, alternative_titles = generate_alternative_titles(text_from_document)

                # print("Document:", filename)
                # print("Title:", title)
                # print("Authors:", authors)
                # print("Alternative Titles:", alternative_titles)
                # print()
                title = title
                author = authors
                author = ', '.join(author)
                alternative = alternative_titles
                alternative = ', '.join(alternative)
                data = [title, author, alternative]
                sheet.append(data)

                # Save the workbook
                workbook.save("output.xlsx")

except Exception as e:
    print("Error during example usage:", e)
