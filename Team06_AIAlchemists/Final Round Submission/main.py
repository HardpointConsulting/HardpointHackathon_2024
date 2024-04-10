# Import necessary libraries
from scraper_module import *
import transformers
from transformers import pipeline
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

# Main function to perform analysis
def main(initial_url):
    # Path to Chrome WebDriver
    webdriver_path = r'C:\Users\user\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    labels = ["trend or style", "worth price or money", "comfortable", "broken or defective", "advertisement", "delivery time", "customer or staff support"]

    driver = initialize_driver(webdriver_path)
    all_reviews = scrape_reviews(driver, initial_url)

    # Create DataFrame from reviews
    df = pd.DataFrame({'Review': all_reviews})
    driver.quit()

    sentiments = [analyze_sentiment(review, model_name) for review in df['Review']]
    df['Sentiment'] = sentiments

    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", tokenizer="distilbert-base-cased")

    df = extract_features(df, qa_pipeline)

    zero_shot_classifier = pipeline("zero-shot-classification")

    df = classify_features(df, zero_shot_classifier, labels)

    df_positive, df_negative = split_df_by_sentiment(df, 'Sentiment')

    feature_percentages = get_feature_percentage(df_positive, df_negative, df, 'Classified')

    positive_features, negative_features = find_pos_neg_features(feature_percentages, threshold=10)

    # Prepare outputs
    strengths_output = []
    strengths_output.append("Positive reviews " + str(len(df_positive) / len(df) * 100))
    for feature, info in positive_features.items():
        strengths_output.append(f"Feature: {feature}, Percentage: {info['Percentage']}")

    weaknesses_output = []
    weaknesses_output.append("Negative reviews " + str(len(df_negative) / len(df) * 100))
    for feature, info in negative_features.items():
        weaknesses_output.append(f"Feature: {feature}, Percentage: {info['Percentage']}")

    return positive_features, negative_features, strengths_output, weaknesses_output

if __name__ == "__main__":
    print("TARGET SME- BLUE PEARL:\n")
    initial_url = 'https://www.flipkart.com/blue-pearl-new-latest-designer-combo-2-analog-watch-men/product-reviews/itm0206349890c12?pid=WATFHNZSZ3A6VYHZ&lid=LSTWATFHNZSZ3A6VYHZFP4WZW&marketplace=FLIPKART&page={}'
    positive_features, negative_features, strengths_output, weaknesses_output = main(initial_url)
    
    print("\n\nCOMPETITOR- FASTRACK:\n")
    initial_url = 'https://www.flipkart.com/fastrack-minimalists-analog-watch-men-women/product-reviews/itmf3zhmzku4r7pv?pid=WATF2VTYEQ6H3H5U&lid=LSTWATF2VTYEQ6H3H5UNXO3FU&aid=overall&certifiedBuyer=false&sortOrder=MOST_RECENT&page={}'
    pos_comp, neg_comp, threats_output, opportunities_output = main(initial_url)

    print("STRENGTH")
    print('\n'.join(strengths_output))

    print("\n\nWEAKNESS")
    print('\n'.join(weaknesses_output))

    print("\nOPPORTUNITIES")
    print('\n'.join(opportunities_output))

    print("\nTHREATS")
    print('\n'.join(threats_output))

    webdriver_path = r'C:\Users\user\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Set up ChromeOptions (if any)
options = webdriver.ChromeOptions()  # Add any desired options here

# Create a Service object to manage the WebDriver
service = Service(webdriver_path)

# Initialize Chrome WebDriver using the Service object
driver = webdriver.Chrome(service=service, options=options)

# URL of the product page
url = 'https://bluepearlwatches.in/Brown---Black-New-Latest-Designer-Combo-Of-Analog/catalogue/Y3BNPr11/GsiYt5Rq'

# Navigate to the product page
driver.get(url)

# Get the page source
page_source = driver.page_source


# Close the browser
driver.quit()

# Parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Extract review elements (adjust selector based on website structure)
desc = soup.find('div', class_='css-zk1q6z').text.strip()  # Replace with appropriate class name

# Assuming you have a GPT-2 model loaded from transformers (or other source)
model_name = "gpt2"  # Adjust model name as needed
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
generator = pipeline("text-generation", model=model_name)

def generate_watch_marketing_messages(context, strengths, weaknesses, brand_name, origin, contact=None):
    """
    Generates marketing messages for a watch brand using GPT-2 based on provided context, strengths, weaknesses, brand name, origin, and optionally contact information.

    Args:
        context: String representing the context or features of the watch (e.g., "This Analog Watches comes with a Designer Look dial and stainless steel back...").
        strengths: List of strings representing key strengths of the watch brand (e.g., "quality").
        weaknesses: List of strings representing key weaknesses of the watch brand (e.g., "costly").
        brand_name: String representing the brand name (e.g., "Blue Pearl").
        origin: String representing the origin of the company (e.g., "India").
        contact: Optional string representing the contact information of the brand.

    Returns:
        A list of strings containing the generated marketing messages.
    """
    messages = []

    # Craft prompt focusing on highlighting strengths and addressing perceived weakness
    prompt = f"{context} Discover the {' and '.join(strengths)} of {brand_name} watches. Although some may perceive our watches as {' and '.join(weaknesses)}, our dedication to {' and '.join(strengths)} ensures that every {brand_name} timepiece is meticulously crafted with precision. Proudly made in {origin}."
    if contact:
        prompt += f" For inquiries, contact us at {contact}."

    # Generate marketing messages using GPT-2
    try:
        response = generator(prompt, max_length=200, num_return_sequences=5, truncation=True, no_repeat_ngram_size=2)  # Adjust parameters as needed
        messages = [message['generated_text'].strip() for message in response]
    except Exception as e:
        print("WARNING: GPT-2 generation failed. Error:", e)

    return messages


context = desc
strengths = positive_features.keys()
brand_name = "Blue Pearl"
origin = "India"
contact = "Praizyenterprises2018@gmail.com"

watch_marketing_messages = generate_watch_marketing_messages(context, strengths, brand_name, origin, contact)

if watch_marketing_messages:
    print("Watch Marketing Messages:")
    for i, message in enumerate(watch_marketing_messages, 1):
        print(f"{i}. {message}\n")
else:
    print("No marketing messages generated.")

