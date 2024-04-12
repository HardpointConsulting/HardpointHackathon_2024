import streamlit as st
from transformers import BertTokenizerFast, EncoderDecoderModel
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = BertTokenizerFast.from_pretrained('mrm8488/bert-mini2bert-mini-finetuned-cnn_daily_mail-summarization')
model = EncoderDecoderModel.from_pretrained('mrm8488/bert-mini2bert-mini-finetuned-cnn_daily_mail-summarization').to(device)

def generate_summary(text):
    # cut off at BERT max length 512
    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    output = model.generate(input_ids, attention_mask=attention_mask)

    return tokenizer.decode(output[0], skip_special_tokens=True)

def summarize_document(file_content):
    """
    Summarizes a single text document.

    Args:
        file_content (str): Content of the text document.

    Returns:
        str: Summary of the document.
    """
    # Generate summary for the text
    summary = generate_summary(file_content)
    return summary

def main():
    st.title("Research Document Summarizer")

    # Sidebar with file uploader and information message
    st.sidebar.markdown("ℹ️ Please upload a text document:")
    uploaded_file = st.sidebar.file_uploader("", type="txt")

    if uploaded_file is not None:
        # Read the content of the uploaded file
        file_content = uploaded_file.read().decode("utf-8")

        # Display loading message and spinner
        with st.spinner("Summarizing..."):
            # Summarize the document
            summary = summarize_document(file_content)

        # Display the summary
        st.subheader("Summary:")
        st.write(summary)

if __name__ == "__main__":
    main()
