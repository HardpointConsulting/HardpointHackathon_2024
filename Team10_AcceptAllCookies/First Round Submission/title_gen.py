import os
from rake_nltk import Rake
from transformers import BertTokenizerFast, EncoderDecoderModel
import torch
import nltk
nltk.download('stopwords')
nltk.download('punkt')
def generate_title(text):
    # Initialize Rake to extract keywords
    rake = Rake()

    # Extract keywords from the text
    rake.extract_keywords_from_text(text)

    # Get the ranked keywords
    ranked_keywords = rake.get_ranked_phrases()

    # Select the top keyword as the title
    title = ranked_keywords[0] if ranked_keywords else "Untitled"

    return title

def generate_title_from_files(folder_path):
    # Get a list of all text files in the folder
    text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    titles = []

    # Iterate through each text file
    for file in text_files:
        file_path = os.path.join(folder_path, file)
        
        # Read the content of the text file
        with open(file_path, 'r') as f:
            text = f.read()
        
        # Generate title for the text
        title = generate_title(text)
        titles.append(title)

    return titles

# Call the function to generate titles for text files in the folder
folder_path = 'E:/Hackathon/pics' # Update with your folder path
titles = generate_title_from_files(folder_path)

# Print the titles
for i, title in enumerate(titles):
  print(f"Title {i+1}: {title}")
