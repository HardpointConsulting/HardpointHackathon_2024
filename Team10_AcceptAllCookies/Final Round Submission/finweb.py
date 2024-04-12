import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration

# Load BART tokenizer and model
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def summarize_finance_docs(file_content):
    """
    Summarizes a single text document for finance documents.

    Args:
        file_content (str): Content of the text document.

    Returns:
        str: Summary of the document.
    """
    # Wrap the file content in a list
    document = [file_content]

    # Tokenize and generate summary
    inputs = tokenizer(document, max_length=1024, return_tensors='pt', truncation=True)
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, min_length=50, max_length=5048, early_stopping=False)

    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def main():
    # Set page title and background color
    st.set_page_config(page_title="Financial Document Summarizer", page_icon="💼", layout="wide", initial_sidebar_state="expanded")

    # Set sidebar title and text
    st.sidebar.title("Options")
    st.sidebar.info("Upload a text document to summarize.")

    # File uploader widget
    uploaded_file = st.sidebar.file_uploader("Upload Text document", type="txt")

    if uploaded_file is not None:
        # Read the content of the uploaded file
        file_content = uploaded_file.read().decode("utf-8")

        # Display loading message and spinner
        with st.spinner("Summarizing..."):
            # Summarize the document
            summary = summarize_finance_docs(file_content)

            # Display the summary
            st.header("Summary")
            st.info(summary)

if __name__ == "__main__":
    main()
