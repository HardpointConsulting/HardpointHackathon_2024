!pip install pytesseract
!sudo apt install tesseract-ocr
!sudo apt-get install unrar
from google.colab import files

# Upload .rar file
uploaded = files.upload()

# Extract images from the uploaded .rar folder
!unrar x "scientific_publication.rar"

import os
import pytesseract
from PIL import Image
import pandas as pd

def extract_text_from_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Perform OCR to extract text
    text = pytesseract.image_to_string(img)

    return text

image_dir = '/content/scientific_publication/'
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
image_texts = {}

for image_file in image_files:
    text = extract_text_from_image(image_file)
    image_texts[os.path.basename(image_file)] = text
for image_file, text in image_texts.items():
    print(f"Text extracted from {image_file}:\n{text}\n")

    
!pip install datasets evaluate transformers[sentencepiece]
from transformers import pipeline
# Function to extract title and author using question answering
def extract_title_and_author(text):
    # Initialize QA pipeline
    qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

    # Define questions
    title_question = "What is the title of this document?"
    author_question = "Who are the authors of this document?"

    # Extract title
    title_result = qa_pipeline(question=title_question, context=text)
    title = title_result['answer']

    # Extract author
    author_result = qa_pipeline(question=author_question, context=text)
    author = author_result['answer']

    return title, author

  from transformers import BartTokenizer, BartForConditionalGeneration

# Load BART tokenizer and model
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

def generate_alternative_title(text):
    # Tokenize input text
    inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)

    # Generate alternative title using BART
    outputs = model.generate(
        **inputs,
        max_length=50,  # Set a maximum length for the output title
        num_beams=4,    # Use beam search for better alternatives
        length_penalty=0.6,  # Lower length penalty for shorter output
        early_stopping=True  # Stop generation when the full stop is encountered
    )

    # Decode the generated title
    generated_title = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)

    # Find the index of the first full stop
    first_fullstop_index = generated_title.find('.')
    if first_fullstop_index != -1:
        generated_title = generated_title[:first_fullstop_index+1]  # Include the full stop

    return generated_title
# Initialize lists to store extracted data
titles = []
authors = []
alternate_titles = []

# Generate alternative titles and extract titles and authors for each text
for image_file, text in image_texts.items():
    # Generate alternative title
    alternative_title = generate_alternative_title(text)
    # Extract titles and authors
    title, author = extract_title_and_author(text)
    # Append data to lists
    titles.append(title)
    authors.append(author)
    alternate_titles.append(alternative_title)
# Create DataFrame
df = pd.DataFrame({
    'Document Title': titles,
    'Author(s)': authors,
    'Generated Title': alternate_titles
}, index=image_texts.keys())
# Display DataFrame
print(df)
df.head(10)
!pip install pyspellchecker
def correct_spelling(text):
    corrected_words = []
    for word in text.split():
        corrected_word = spell.correction(word)
        if corrected_word is not None:
            corrected_words.append(corrected_word)
        else:
            corrected_words.append(word)  # Keep the original word if correction is None
    corrected_text = " ".join(corrected_words)
    return corrected_text

# Duplicate the DataFrame
df_copy = df.copy()

# Apply preprocessing and spell checking to the text columns
df_copy['Document Title'] = df_copy['Document Title'].map(lambda text: correct_spelling(text))
df_copy['Generated Title'] = df_copy['Generated Title'].map(lambda text: correct_spelling(text))

# Display the duplicated DataFrame after preprocessing and spell checking
print(df_copy)
df_copy.head(10)

from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Function to encode text using BERT
def encode_text(text):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

# Calculate BERT-based similarity for each pair of titles
doc_title_embeddings = encode_text(df['Document Title'].tolist())
gen_title_embeddings = encode_text(df['Generated Title'].tolist())
bert_similarities = cosine_similarity(doc_title_embeddings, gen_title_embeddings)


import numpy as np
!pip install matplotlib
# Print the BERT-based similarity matrix
print(np.round(bert_similarities, 2))
import matplotlib.pyplot as plt

# Plotting the similarity scores
plt.figure(figsize=(8, 6))
plt.hist(bert_similarities.flatten(), bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of BERT-based Similarity Scores')
plt.xlabel('Similarity Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
