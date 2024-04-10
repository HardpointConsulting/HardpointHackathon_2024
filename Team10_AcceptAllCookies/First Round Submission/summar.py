import os
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

def generate_summary_from_files(folder_path):
    # Get a list of all text files in the folder
    text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    summaries = []

    # Iterate through each text file
    for file in text_files:
        file_path = os.path.join(folder_path, file)
        
        # Read the content of the text file
        with open(file_path, 'r') as f:
            text = f.read()
        
        # Generate summary for the text
        summary = generate_summary(text)
        summaries.append(summary)

    return summaries

# Call the function to generate summaries for text files in the folder
folder_path ='E:/Hackathon/pics'  # Update with your folder path
summaries = generate_summary_from_files(folder_path)

# Print the summaries
for i, summary in enumerate(summaries):
    print(f"Summary {i+1}:\n{summary}\n{'-'*50}")
