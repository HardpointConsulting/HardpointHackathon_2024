import os
import json
import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration, BertTokenizerFast, EncoderDecoderModel

# Load the BART model and tokenizer
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# Function to summarize a legal document
def summarize_legal_document(file):
    document_content = json.load(file)

    # Extract relevant keys
    date = document_content.get("DATE", "")
    title = document_content.get("DOCNAME", "")
    text = document_content.get("TEXT", "")
    conclusion = document_content.get("CONCLUSION", "")
    judges = document_content.get("JUDGES", "")

    # Combine information for summarization
    summary_content = f"{title}: Dated {date} {text} (Conclusion: {conclusion}, Judges: {judges})"

    # Tokenize and generate summary
    inputs = tokenizer([summary_content], max_length=1024, return_tensors='pt', truncation=True)
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, min_length=50, max_length=5048, early_stopping=False)

    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Function to summarize a financial document
def summarize_financial_document(file):
    text = file.read()

    # Generate summary for the text
    summary = summarize_text(text)
    return summary

# Function to summarize a research paper
def summarize_research_paper(file):
    text = file.read()

    # Generate summary for the text
    summary = generate_summary(text)
    return summary

# Streamlit app
def main():
    st.title("Document Summarization")

    # Add radio buttons for document types
    document_type = st.radio("Select Document Type", ("Legal", "Finance", "Research Paper"))

    # Add input documents button
    uploaded_file = st.file_uploader("Upload your document", type=["txt", "json"])

    # Add submit button
    if st.button("Submit"):
        if uploaded_file:
            if document_type == "Legal":
                summary = summarize_legal_document(uploaded_file)
            elif document_type == "Finance":
                summary = summarize_financial_document(uploaded_file)
            elif document_type == "Research Paper":
                summary = summarize_research_paper(uploaded_file)

            # Display the summary
            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please upload a file before submitting.")

if __name__ == "__main__":
    main()
