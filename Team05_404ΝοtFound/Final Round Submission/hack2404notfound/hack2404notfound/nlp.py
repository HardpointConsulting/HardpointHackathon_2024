import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

from collections import Counter

from transformers import pipeline

from datetime import datetime

generator = pipeline("text-generation", model="distilgpt2")


# Download VADER lexicon
nltk.download('vader_lexicon')

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}





def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove HTML tags
    text = re.sub(r'<[^>]*>', '', text)
    
    # Remove special characters, punctuation, and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    
    # Join tokens back into text
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text
# Define a function to get sentiment score
def get_sentiment_score(text):
    if pd.isnull(text):
        return 0.0  # Assigning a neutral sentiment score for NaN values
    else:
        return sid.polarity_scores(str(text))['compound']


# Classify sentiment based on the sentiment score
def classify_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'


review_page_links = []

url = "https://www.amazon.in/BLUE-TYGA-SUNSCREEN-Trekking-Sunscreen/dp/B0C7MS9L7M/ref=sr_1_1_sspa?crid=29FQRILPXA9TR&dib=eyJ2IjoiMSJ9.67T0zawINt8J6yQKg1DDKnhuu4MruJDlPDQva7d5xOF63-EIhQo7YIuQ9ODkss59ehoWHY7og9ZqBF8OY1zhbLaE_16Ybzm06O-rnf4hCKsMzVabmSNyzR7I5zn-mvI2wXTCoSj-NgiAvUmqBT64W5Ch3T3Y6VkvtU2OK_amxuwruclcUVkIVS5vswxpbN9PWr94yR26pY4wcR71E8V4CkXNUR9oOtHg8C8y3W71V6fO0ChR9gCgOpmxv2ePM7RMKyeCh9K3s7RCK8kNU4Lat2zFkrgYWBH290MddNUW0Cw.uLrjKOouz16g9wPulqZiICEWEsfN2UFRd2-uFW6JJkg&dib_tag=se&keywords=clothes&qid=1712609118&sprefix=clothes%2Caps%2C222&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"


response = requests.get(url, headers=headers)
parsedHtml = BeautifulSoup(response.text, 'html.parser')
next_review = parsedHtml.find('a', attrs={'data-hook': 'see-all-reviews-link-foot'})
if not next_review:
    print("All review Link Not Found")

page_number = 16

#int(input("Enter number of page reviews you wish to scrape: "))

all_reviews = []
product_name = parsedHtml.find("span", class_="product-title-word-break").get_text(strip=True)

print(product_name)

for i in range(page_number):
    if next_review:
        next_page = 'https://www.amazon.in{0}'.format(next_review['href'])
        review_page_links.append(next_page)
        response = requests.get(next_page, headers=headers)
        parsedHtml = BeautifulSoup(response.text, 'html.parser')

        # Find all review elements
        reviews = parsedHtml.find_all("div", class_="a-section review aok-relative")
        
        # Extract information from each review element
        for review in reviews:
            review_text = review.find("span", class_="review-text-content").get_text(strip=True)
            review_date = review.find("span", class_="review-date").get_text(strip=True)
            
            all_reviews.append({'review': review_text, 'date': review_date})
        
        next_review = parsedHtml.find('li', class_='a-last').find('a')
    else:
        print("Page finished at:", i)
        break

# Write reviews to CSV file
df = pd.DataFrame(all_reviews)

# Replace "Reviewed in India on" with an empty string in the date column
df['date'] = df['date'].str.replace('Reviewed in India on', '')

df.to_csv('amazon_review.csv', index=False)



# Read the dataset from CSV file
df = pd.read_csv('C:\\Users\\haran\\hack2404notfound\\amazon_review.csv')



# Preprocess the text data in the 'review' column
df['cleaned_review'] = df['review'].apply(preprocess_text)

# Display the cleaned dataset
print(df.head())

# Save the output. 
df.to_csv('cleaned_text.csv', index=False)

# Load the cleaned reviews
df = pd.read_csv('cleaned_text.csv')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()


# Apply sentiment analysis to each review
df['sentiment_score'] = df['cleaned_review'].apply(get_sentiment_score)

# Apply sentiment classification
df['sentiment'] = df['sentiment_score'].apply(classify_sentiment)

# Display the results
print(df.head())

# Save the output
df.to_csv('sentiment_analysis_results.csv', index=False)

# Load the sentiment analysis results
df = pd.read_csv('sentiment_analysis_results.csv')

# Filter out only the reviews with negative sentiment
negative_reviews = df[df['sentiment'] == 'Negative'].copy()  # Make a copy to avoid chained indexing






def classify_product_category(product_name):
    # Define patterns or rules to match against product names
    clothing_keywords = ['shirt', 'dress', 'pants', 'jeans', 'jacket', 'sweater', 't-shirt', 'blouse', 'skirt', 'shorts', 'coat', 'suit', 'tie', 'scarf', 'gloves', 'hat', 'socks', 'underwear', 'lingerie']
    earphones_keywords = ['earphones', 'earbuds', 'headphones', 'earplugs']
    shoes_keywords = ['shoes', 'sneakers', 'boots', 'sandals', 'slippers', 'heels', 'flats', 'loafers', 'oxfords']
    air_conditioner_keywords = ['air conditioner', 'AC', 'cooling unit', 'portable air conditioner', 'window air conditioner', 'split air conditioner']
    fan_keywords = ['fan', 'ceiling fan', 'tower fan', 'desk fan', 'box fan', 'pedestal fan']
    phone_keywords = ['phone', 'smartphone', 'cellphone', 'mobile', 'iPhone', 'Samsung', 'Google Pixel', 'OnePlus', 'Xiaomi']
    laptop_keywords = ['laptop', 'notebook', 'chromebook', 'macbook', 'ultrabook', 'gaming laptop', '2-in-1 laptop']
    tablet_keywords = ['tablet', 'ipad', 'android tablet', 'Windows tablet']
    camera_keywords = ['camera', 'dslr', 'mirrorless camera', 'point-and-shoot camera', 'action camera', 'instant camera']
    tv_keywords = ['television', 'tv', 'smart tv', 'led tv', '4k tv', 'OLED tv', 'QLED tv']
    watch_keywords = ['watch', 'smartwatch', 'fitness tracker', 'analog watch', 'digital watch', 'sport watch']
    speaker_keywords = ['speaker', 'bluetooth speaker', 'portable speaker', 'bookshelf speaker', 'floorstanding speaker', 'soundbar', 'subwoofer']
    router_keywords = ['router', 'wifi router', 'wireless router', 'mesh router', 'gigabit router', 'gaming router']
    printer_keywords = ['printer', 'inkjet printer', 'laser printer', 'all-in-one printer', 'photo printer', 'color printer']
    monitor_keywords = ['monitor', 'computer monitor', 'lcd monitor', 'led monitor', 'gaming monitor', 'ultrawide monitor']
    keyboard_keywords = ['keyboard', 'wireless keyboard', 'mechanical keyboard', 'gaming keyboard', 'ergonomic keyboard']
    mouse_keywords = ['mouse', 'wireless mouse', 'gaming mouse', 'ergonomic mouse', 'trackball mouse']
    refrigerator_keywords = ['refrigerator', 'fridge', 'freezer', 'mini fridge', 'compact refrigerator', 'wine cooler']
    microwave_keywords = ['microwave', 'microwave oven', 'countertop microwave', 'over-the-range microwave']
    blender_keywords = ['blender', 'food processor', 'juicer', 'hand blender', 'immersion blender', 'smoothie maker']
    vacuum_keywords = ['vacuum cleaner', 'robot vacuum', 'cordless vacuum', 'canister vacuum', 'upright vacuum', 'handheld vacuum']
    toaster_keywords = ['toaster', 'toaster oven', 'convection toaster oven', '4-slice toaster', '2-slice toaster']
    coffee_maker_keywords = ['coffee maker', 'espresso machine', 'drip coffee maker', 'french press', 'single-serve coffee maker', 'pour-over coffee maker']
    iron_keywords = ['iron', 'clothes iron', 'steam iron', 'travel iron', 'garment steamer']
    hair_dryer_keywords = ['hair dryer', 'blow dryer', 'hair straightener', 'hair curler', 'hair clipper', 'hair trimmer']
    scale_keywords = ['scale', 'bathroom scale', 'digital scale', 'analog scale', 'body fat scale']
    pendrive_keywords = ['pendrive', 'usb drive', 'flash drive', 'thumb drive', 'USB stick']
    hard_disk_keywords = ['hard disk', 'external hard drive', 'portable hard drive', 'SSD', 'NAS drive', 'network attached storage']
    power_bank_keywords = ['power bank', 'portable charger', 'battery pack', 'power pack', 'charging bank']
    printer_paper_keywords = ['printer paper', 'copy paper', 'inkjet paper', 'laser paper', 'multipurpose paper']
    webcam_keywords = ['webcam', 'web camera', 'usb camera', 'PC camera', 'video camera', 'conference camera']
    gps_keywords = ['gps', 'global positioning system', 'GPS device', 'navigation system', 'GPS tracker']
    calculator_keywords = ['calculator', 'scientific calculator', 'graphing calculator', 'financial calculator', 'basic calculator']

    # Check for matches with each category and return the corresponding category
    if any(keyword in product_name.lower() for keyword in clothing_keywords):
        return 'Clothing'
    elif any(keyword in product_name.lower() for keyword in earphones_keywords):
        return 'Earphones'
    elif any(keyword in product_name.lower() for keyword in shoes_keywords):
        return 'Shoes'
    elif any(keyword in product_name.lower() for keyword in air_conditioner_keywords):
        return 'Air Conditioner'
    elif any(keyword in product_name.lower() for keyword in fan_keywords):
        return 'Fan'
    elif any(keyword in product_name.lower() for keyword in phone_keywords):
        return 'Phone'
    elif any(keyword in product_name.lower() for keyword in laptop_keywords):
        return 'Laptop'
    elif any(keyword in product_name.lower() for keyword in tablet_keywords):
        return 'Tablet'
    elif any(keyword in product_name.lower() for keyword in camera_keywords):
        return 'Camera'
    elif any(keyword in product_name.lower() for keyword in tv_keywords):
        return 'TV'
    elif any(keyword in product_name.lower() for keyword in watch_keywords):
        return 'Watch'
    elif any(keyword in product_name.lower() for keyword in speaker_keywords):
        return 'Speaker'
    elif any(keyword in product_name.lower() for keyword in router_keywords):
        return 'Router'
    elif any(keyword in product_name.lower() for keyword in printer_keywords):
        return 'Printer'
    elif any(keyword in product_name.lower() for keyword in monitor_keywords):
        return 'Monitor'
    elif any(keyword in product_name.lower() for keyword in keyboard_keywords):
        return 'Keyboard'
    elif any(keyword in product_name.lower() for keyword in mouse_keywords):
        return 'Mouse'
    elif any(keyword in product_name.lower() for keyword in refrigerator_keywords):
        return 'Refrigerator'
    elif any(keyword in product_name.lower() for keyword in microwave_keywords):
        return 'Microwave'
    elif any(keyword in product_name.lower() for keyword in blender_keywords):
        return 'Blender'
    elif any(keyword in product_name.lower() for keyword in vacuum_keywords):
        return 'Vacuum Cleaner'
    elif any(keyword in product_name.lower() for keyword in toaster_keywords):
        return 'Toaster'
    elif any(keyword in product_name.lower() for keyword in coffee_maker_keywords):
        return 'Coffee Maker'
    elif any(keyword in product_name.lower() for keyword in iron_keywords):
        return 'Iron'
    elif any(keyword in product_name.lower() for keyword in hair_dryer_keywords):
        return 'Hair Dryer'
    elif any(keyword in product_name.lower() for keyword in scale_keywords):
        return 'Scale'
    elif any(keyword in product_name.lower() for keyword in pendrive_keywords):
        return 'Pendrive'
    elif any(keyword in product_name.lower() for keyword in hard_disk_keywords):
        return 'Hard Disk'
    elif any(keyword in product_name.lower() for keyword in power_bank_keywords):
        return 'Power Bank'
    elif any(keyword in product_name.lower() for keyword in printer_paper_keywords):
        return 'Printer Paper'
    elif any(keyword in product_name.lower() for keyword in webcam_keywords):
        return 'Webcam'
    elif any(keyword in product_name.lower() for keyword in gps_keywords):
        return 'GPS'
    elif any(keyword in product_name.lower() for keyword in calculator_keywords):
        return 'Calculator'
    else:
        return 'Other'  # If the product doesn't match any predefined category

# Apply the classification function to the product name
product_category = classify_product_category(product_name)



# Define common problems or issues and their associated keywords
common_problems_keywords = {
    'sound_quality': ['sound', 'audio', 'bass', 'treble', 'muffled', 'distorted'],
    'connectivity_issues': ['connect', 'pair', 'connection', 'disconnect', 'sync', 'pairing', 'bluetooth'],
    'battery_life': ['battery', 'charge', 'power', 'life', 'drain', 'lasting', 'runtime', 'charging'],
    'fit_comfort': ['fit', 'comfort', 'ear', 'wear', 'size', 'tight', 'loose', 'comfortable', 'adjustable'],
    'durability': ['durable', 'build', 'quality', 'long-lasting', 'sturdy', 'fragile', 'break', 'breakable', 'damage'],
    'customer_service': ['customer', 'service', 'support', 'response', 'help', 'assist', 'assistance', 'contact', 'resolve'],
    'price_value': ['price', 'value', 'expensive', 'cheap', 'worth', 'overpriced', 'affordable', 'cost-effective'],
    'design_appearance': ['design', 'appearance', 'look', 'aesthetic', 'stylish', 'plain', 'fashionable', 'color'],
    'user_interface': ['interface', 'UI', 'navigation', 'menu', 'control', 'buttons', 'interface', 'operation'],
    'compatibility_issues': ['compatibility', 'compatible', 'incompatible', 'work', 'device', 'system', 'software'],
    'shipping_delivery': ['shipping', 'delivery', 'ship', 'arrive', 'arrival', 'packaging', 'package', 'shipment'],
    'performance_issues': ['performance', 'speed', 'lag', 'response', 'efficiency', 'crash', 'freeze', 'hang'],
    'software_bugs': ['bug', 'issue', 'error', 'glitch', 'crash', 'software', 'firmware', 'update'],
    'warranty_coverage': ['warranty', 'guarantee', 'coverage', 'claim', 'repair', 'replace', 'refund'],
    'instruction_manual': ['manual', 'instructions', 'guide', 'documentation', 'user manual'],
    'accessory_quality': ['accessory', 'quality', 'case', 'bag', 'charger', 'adapter', 'cable', 'ear tips'],
    'performance_consistency': ['consistent', 'reliable', 'reliability', 'stable', 'fluctuate'],
    'size_weight': ['size', 'weight', 'portable', 'compact', 'lightweight', 'bulky', 'heavy'],
    'brand_reputation': ['brand', 'reputation', 'trustworthy', 'reliable', 'reputation', 'reputed', 'unknown'],
    'environmental_impact': ['environment', 'impact', 'sustainable', 'eco-friendly', 'recyclable', 'carbon footprint'],
    'security_privacy': ['security', 'privacy', 'secure', 'private', 'protection', 'data', 'hack', 'breach'],
    'customer_reviews': ['review', 'rating', 'feedback', 'opinion', 'testimonial', 'rating', 'stars'],
    'packaging_waste': ['packaging', 'waste', 'excessive', 'reduce', 'recyclable', 'environmentally friendly'],
    'returns_exchange_policy': ['return', 'exchange', 'policy', 'refund', 'exchange', 'returnable', 'non-returnable'],
    'health_safety_concerns': ['health', 'safety', 'concern', 'hazard', 'danger', 'risk', 'toxic', 'flammable'],
    'product_recall': ['recall', 'recall notice', 'defect', 'fault', 'recall', 'safety issue'],
    'network_coverage': ['network', 'coverage', 'signal', 'reception', 'strength', 'service', 'area'],
    'component_failure': ['component', 'failure', 'malfunction', 'defect', 'breakdown', 'component', 'part'],
    'instruction_clarity': ['clarity', 'clear', 'understand', 'confusing', 'ambiguous', 'vague', 'instruction']}

# Function to identify common problems in text
def identify_common_problems(text):
    problems = []
    for problem, keywords in common_problems_keywords.items():
        for keyword in keywords:
            if keyword in text:
                problems.append(problem)
                break  # Once a problem is identified, no need to check further keywords
    return problems

# Apply function to identify common problems in each negative review
negative_reviews['negative_problems'] = negative_reviews['cleaned_review'].apply(identify_common_problems)

# Collect all identified problems in a single list
all_problems = []
for problems_list in negative_reviews['negative_problems']:
    all_problems.extend(problems_list)



print("Product Name:", product_name)

# Print unique set of problems
unique_problems = set(all_problems)

# Convert the set of unique_problems to a list
unique_problems_list = list(unique_problems)

# Limit the number of problems to 5
limited_problems = unique_problems_list[:5]

print("Identified Problems:")
for problem in limited_problems:
    print("- {}".format(problem.replace('_', ' ')))


    





solution=[]
for problem in limited_problems:
    text= "the developer of "+product_category+" should solve "+problem+" by"
    value = generator(text,max_length=100,num_return_sequences=2,)

    solution.append(value)

print(solution)


# Define the file path where you want to save the solutions
file_path = 'C:\\Users\\haran\\hack2404notfound\\solution.txt.txt'

# Open the file in write mode
with open(file_path, 'w', encoding='utf-8') as file:
    file.write('PRODUCT NAME:'+product_name)
    file.write('\n\n')
    file.write('IDENTIFIED PROBLEMS:')
    file.write('\n')
    for problem in limited_problems:
      file.write('-' + problem + '\n')

    file.write('\n\n')
    file.write('SOLUTIONS:')
    file.write('\n')
    # Iterate over each solution
    for solutions_per_problem in solution:
        # Write each solution to the file
        for solution_text in solutions_per_problem:
            file.write(solution_text['generated_text'] + '\n')
        # Add a separator between solutions for different problems
        file.write('-' * 50 + '\n\n')
        file.write('\n\n')

print("Solutions have been written to", file_path)


# Calculate the frequency of each sentiment category
sentiment_counts = df['sentiment'].value_counts()

# Reorder the index to match the desired order
sentiment_counts = sentiment_counts.reindex(['Positive', 'Neutral', 'Negative'])

# Plot a bar plot
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title('Distribution of Sentiments')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.xticks(rotation=0)  # Rotate x-axis labels if needed

plt.savefig('review_count')





# Function to parse date string into datetime object
def parse_date(date_str):
    # Strip leading and trailing whitespace, then parse the date
    date_str = date_str.strip()
    return datetime.strptime(date_str, "%d %B %Y")


# Convert 'date' column to datetime using the parse_date function
df['date'] = df['date'].apply(parse_date)

# Group by date and calculate average sentiment score
daily_sentiment = df.groupby('date')['sentiment_score'].mean()

# Plot the line graph
plt.figure(figsize=(10, 6))
plt.plot(daily_sentiment.index, daily_sentiment.values, marker='o', linestyle='-')
plt.title('Trend Analysis')
plt.xlabel('Date')
plt.ylabel('Reviews')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()


plt.savefig('trent_analysis_plot.png')