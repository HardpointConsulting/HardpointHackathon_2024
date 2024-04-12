import json
import streamlit as st
from transformers import BertTokenizerFast, EncoderDecoderModel
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = BertTokenizerFast.from_pretrained('mrm8488/bert-mini2bert-mini-finetuned-cnn_daily_mail-summarization')
model = EncoderDecoderModel.from_pretrained('mrm8488/bert-mini2bert-mini-finetuned-cnn_daily_mail-summarization').to(device)
def summarize_legal_docs(file_content):
    """
    Summarizes a single JSON document for legal documents.

    Args:
        file_content (str): Content of the JSON document.

    Returns:
        str: Summary of the document.
    """
    document_content = json.loads(file_content)

    # to extract needed keys only 
    date = document_content.get("DATE", "")
    title = document_content.get("DOCNAME", "")
    text = document_content.get("TEXT", "")
    conclusion = document_content.get("CONCLUSION", "")
    judges = document_content.get("JUDGES", "")

    # Combine information from key
    summary_content = f"{title}: Dated {date} {text} (Conclusion: {conclusion}, Judges: {judges})"

    # Tokenize and generate summary
    inputs = tokenizer([summary_content], max_length=1024, return_tensors='pt', truncation=True)
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, min_length=50, max_length=2048, early_stopping=False)

    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def main():
    st.title("Legal Document Summarizer")

    # Sidebar with file uploader and information message
    st.sidebar.markdown("ℹ️ Please upload a JSON document:")
    uploaded_file = st.sidebar.file_uploader("", type="json")

    # Radio buttons for document type selection
    document_type = st.sidebar.radio("Select Document Type", ("Legal", "Finance", "Research"))

    if uploaded_file is not None:
        # Read the content of the uploaded file
        file_content = uploaded_file.read().decode("utf-8")

        # Display loading message and spinner
        with st.spinner("Summarizing..."):
            # Summarize the document based on the selected document type
            if document_type == "Legal":
                summary = summarize_legal_docs(file_content)
                
        # Display the summary
        st.subheader("Summary:")
        st.write(summary)

if __name__ == "__main__":
    main()
