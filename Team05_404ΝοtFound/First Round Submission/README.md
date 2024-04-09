# ScholarSlice

This Python script utilizes optical character recognition (OCR) techniques, natural language processing (NLP) models, and deep learning models to extract information from scientific publication images (PNG files), generate titles, and summarize their content. It then outputs the results to an Excel file.

## Dependencies

- *nltk:* For natural language processing tasks such as tokenization.
- *pytesseract:* Python wrapper for Google's Tesseract-OCR Engine.
- *PIL:* Python Imaging Library for opening, manipulating, and saving many different image file formats.
- *spacy:* For named entity recognition (NER) tasks.
- *transformers:* Hugging Face's Transformers library for utilizing pre-trained deep learning models.
- *pandas:* For handling tabular data efficiently.



### Usage

- Place your PNG files containing scientific publication images in a directory.
- Modify the directory_path variable in the script to point to this directory.
- Run the script.
  The script will process each PNG file, extract text, generate titles, summarize the content, and store the results in an Excel file.



### Output

The script generates an Excel file containing three columns:

- Title: Extracted title from the publication.
- Authors: Likely authors extracted using named entity recognition (NER).
- Alternative Titles: Alternative titles generated based on the summary of the publication content

### Note

- The performance of title and summary generation heavily depends on the quality and nature of the input images. Adjustments may be necessary in the code to accommodate different types of publications and image qualities.
- Fine-tuning the pre-trained models on domain-specific data could potentially improve the quality of generated titles and summaries.
- Ensure proper citation and permissions when using or distributing the generated titles and summaries.
- This script serves as a starting point and may require further customization based on specific requirements and use cases
