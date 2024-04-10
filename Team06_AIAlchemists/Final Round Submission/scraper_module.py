# Import necessary libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

# Function to initialize the Chrome WebDriver
def initialize_driver(webdriver_path):
    options = webdriver.ChromeOptions()  # No specific options in this example
    service = Service(webdriver_path)
    return webdriver.Chrome(service=service, options=options)

# Function to scrape reviews from a URLs iteratively
def scrape_reviews(driver, initial_url, num_pages=10):
    all_reviews = []
    for page_num in range(1, num_pages + 1):
        current_url = initial_url.format(page_num)
        driver.get(current_url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        parent_divs = soup.find_all('div', class_='t-ZTKy _1QgsS5')
        for parent_div in parent_divs:
            review = parent_div.find('div', class_='_6K-7Co').text.strip()
            all_reviews.append(review)
    return all_reviews

# Function to analyze sentiment of a review using a pre-trained model
def analyze_sentiment(review, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    cleaned_comment = pre_process_comment(review)
    inputs = tokenizer(cleaned_comment, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    sentiment_labels = {0: "Negative", 1: "Positive"}
    return sentiment_labels[predictions.item()]

def pre_process_comment(comment):
    # Preprocessing code here (lowercasing, removing punctuation, etc.)
    return comment

# Function to extract features from reviews using a question-answering pipeline
def extract_features(df, qa_pipeline):
    features = []
    for index, row in df.iterrows():
        review = row['Review']
        sentiment = row['Sentiment']
        question = "What are the good qualities?" if sentiment == 'Positive' else "What are the areas of improvement for the product?"
        review_encoding = qa_pipeline({"question": question, "context": review})
        extracted_feature = review_encoding["answer"]
        features.append(extracted_feature)
    df['Features'] = features
    return df

# Function to classify features using a zero-shot classification pipeline
def classify_features(df, zero_shot_classifier, labels):
    classified = []
    for feature in df['Features']:
        classification_result = zero_shot_classifier(feature, labels)
        classifieds = classification_result['labels'][0]
        classified.append(classifieds)
    df['Classified'] = classified
    print(df)
    return df

# Function to split DataFrame by sentiment
def split_df_by_sentiment(df, sentiment_col):
    df_positive = df[df[sentiment_col] == 'Positive']
    df_negative = df[df[sentiment_col] == 'Negative']
    return df_positive, df_negative

# Function to calculate feature percentages
def get_feature_percentage(df_positive, df_negative, df_combined, feature_column):
    positive_counts = df_positive[feature_column].value_counts()
    negative_counts = df_negative[feature_column].value_counts()
    total_entries = len(df_combined)
    max_positive_entries = max(1, len(df_positive))  # Ensure there are no divisions by zero
    max_negative_entries = max(1, len(df_negative))  # Ensure there are no divisions by zero
    feature_percentages = {}

    # Calculate percentages for positive sentiment entries
    for feature, count in positive_counts.items():
        feature_percentages[feature] = {
            'Positive': count / total_entries * 100,
            'Within_Positive': count / max_positive_entries * 100
        }

    # Calculate percentages for negative sentiment entries
    for feature, count in negative_counts.items():
        if feature in feature_percentages:
            feature_percentages[feature]['Negative'] = count / total_entries * 100
            feature_percentages[feature]['Within_Negative'] = count / max_negative_entries * 100
        else:
            feature_percentages[feature] = {
                'Negative': count / total_entries * 100,
                'Within_Negative': count / max_negative_entries * 100
            }
    print(feature_percentages)

    return feature_percentages

# Function to find positive and negative features based on a threshold
def find_pos_neg_features(feature_percentage, threshold=10):
    positive_features = {}
    negative_features = {}
    for feature, percentages in feature_percentage.items():
        if 'Positive' in percentages and percentages['Within_Positive'] >= threshold:
            positive_features[feature] = {'Percentage': percentages['Within_Positive']}
        if 'Negative' in percentages and percentages['Within_Negative'] >= threshold:
            negative_features[feature] = {'Percentage': percentages['Within_Negative']}
    return positive_features, negative_features
