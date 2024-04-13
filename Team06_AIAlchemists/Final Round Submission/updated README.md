# ELEVATEBIZ- ” The elevator for your business!”

Are you tired of struggling with marketing issues as a small or medium-sized business owner? We understand the challenges you face and are excited to introduce a new product that can help. Our solution provides an end-to-end approach that begins with extracting valuable customer feedback. By analyzing the strengths and weaknesses of both, we can perform a SWOT analysis for your business, using your competitors' strengths and weaknesses as opportunities and threats for you to consider. With this insight, you'll be able to optimize your marketing strategies and stay ahead of the competition.

## Technologies Used:
- Selenium
- Hugging Face
- GPT-2

## Requirements

To run this script, you will need to have the following software and libraries installed:

- Python 3.x
- Selenium
- Webdriver Manager for Chrome
- BeautifulSoup4
- Pandas
- Transformers
- PyTorch

## Code Descriptions

### 1. Script Overview:

The script consists of the following parts:

- Web Scraping: Uses Selenium and BeautifulSoup to scrape reviews from a given product page URL on Flipkart. The script navigates through the pages and extracts the text of the reviews.

- Sentiment Analysis: Uses a pretrained `distilbert-base-uncased-finetuned-sst-2-english` model from the Transformers library to analyze the sentiment of each review. The script classifies each review as either positive or negative.

- Feature Extraction: Uses the `distilbert-base-cased-distilled-squad` model from Transformers for question-answering to extract features from the reviews. Depending on the sentiment, the script asks different questions ("What are the good qualities?" for positive and "What are the areas of improvement for the product?" for negative reviews).

- Feature Classification: Uses zero-shot classification from Transformers to classify the extracted features into categories such as "quality," "worth price or money," and others.

- Analysis: Splits the reviews into separate dataframes based on sentiment and calculates the occurrence percentages of each feature within the positive and negative sentiment reviews. Determines strengths and weaknesses based on the calculated percentages.

### 2. Helper Functions:

- `initialize_driver`: Initializes a Chrome WebDriver using `webdriver_manager`.
- `scrape_reviews`: Scrapes reviews from a URL iteratively, returning a list of reviews.
- `analyze_sentiment`: Analyzes sentiment of a review using a pre-trained sentiment classification model.
- `pre_process_comment`: Preprocesses a comment (optional, like lowercasing and removing punctuation).
- `extract_features`: Uses a question-answering pipeline to extract features based on sentiment (e.g., "What are the good qualities?" for positive reviews).
- `classify_features`: Classifies features using a zero-shot classification pipeline based on predefined labels.
- `split_df_by_sentiment`: Splits a DataFrame containing reviews by sentiment (positive or negative).
- `get_feature_percentage`: Calculates feature percentages for positive, negative, and overall sentiment.
- `find_pos_neg_features`: Identifies positive and negative features based on a threshold percentage.

### 3. Main Function:

- `main`: The main function that performs the analysis. It takes an initial URL for scraping reviews as input.
    - Sets the path to the Chrome WebDriver, sentiment analysis model name, and classification labels.
    - Initializes a Chrome WebDriver and scrapes reviews from the URL.
    - Creates a DataFrame from the reviews.
    -Load sentiment analysis model and tokenizer
    -Preprocess comments(lowercase,remove punctuations etc..)
    - Analyzes sentiment for each review.
    - Extracts features based on sentiment.
    -Define questions based on each review
    - Classifies features.
    -List labels to classify each review.
    - Splits the DataFrame by sentiment.
    - Calculates feature percentages.
    - Identifies positive and negative features.
    - Generates marketing messages using GPT-2 (commented out for now).
    - Prints strengths, weaknesses, and marketing messages (if generated).

### 4. GPT-2 Marketing Message Generation :

- This section defines functions to generate marketing messages based on product description, strengths, weaknesses, brand name, and origin. It uses a GPT-2 model for text generation.

## Usage

### Installation:

1. **Python:** Ensure you have Python 3.x installed. You can download Python from [the official website](https://www.python.org/).

2. **Selenium:** Install the Selenium package using the following command:

    ```shell
    pip install selenium
    ```

3. **Webdriver Manager for Chrome:** Install the Webdriver Manager package using the following command:

    ```shell
    pip install webdriver-manager
    ```

4. **BeautifulSoup4:** Install the BeautifulSoup4 package using the following command:

    ```shell
    pip install beautifulsoup4
    ```

5. **Pandas:** Install the Pandas package using the following command:

    ```shell
    pip install pandas
    ```

6. **Transformers:** Install the Transformers package using the following command:

    ```shell
    pip install transformers
    ```

7. **PyTorch:** Install the PyTorch package using the following command:

    ```shell
    pip install torch
    ```
### Setup

1. Download the Chrome WebDriver from the [official website](https://chromedriver.chromium.org/downloads). Choose the version that matches your Chrome browser.
2. Add the path to the Chrome WebDriver executable file to the `webdriver_path` variable in the script.
3. **GPT-2 Setup**

    1. **Loading GPT-2 Model and Tokenizer:**
        - The code loads a pre-trained GPT-2 model and tokenizer using the transformers library.
        - The model name is specified as "gpt2", and the appropriate model and tokenizer are loaded.

    2. **Initializing Text Generation Pipeline:**
        - A text generation pipeline is initialized using the loaded GPT-2 model and tokenizer with the pipeline function from the transformers library.
        - The pipeline is set up for the "text-generation" task.

    3. **Function for Generating Marketing Messages:**
        - *generate_watch_marketing_messages function*:
            - Takes context, strengths, weaknesses, brand name, origin, and optional contact information as input parameters.
            - Constructs a prompt based on the provided context, strengths, weaknesses, brand name, and origin. If contact information is available, it is also included in the prompt.
            - Uses the GPT-2 model to generate marketing messages based on the crafted prompt.
            - The function specifies parameters for text generation such as max_length for the length of generated text, num_return_sequences for the number of text outputs to generate, and truncation and no_repeat_ngram_size to control generation behavior and reduce repetition.
            - The function handles potential exceptions during GPT-2 generation and outputs a list of marketing messages.

### Running the script

1. Open the script and update the `initial_url` variable with the URL of the product reviews page you want to scrape.
2. Adjust the loop in the script to scrape the desired number of pages (in the range provided) from the reviews.
3. Run the script using the following command:

    ```shell
    python main.py
    ```
## Percentages and Thresholds:

### Positive:
Represents the percentage of all reviews with a positive sentiment mentioning a particular feature.

### Within Positive:
Indicates the percentage of positive reviews that mention the specific feature.

### Negative:
Denotes the percentage of all reviews with a negative sentiment mentioning the feature as a downside.

### Within Negative:
Represents the percentage of negative reviews that specifically mention the feature.

## Threshold for Feature Selection:

Features with a percentage below the threshold, such as 10%, are not considered significant enough to influence the SWOT analysis. For example, if a feature like "trend or style" has a percentage of only 1%, it indicates that it is mentioned infrequently in the reviews and may not significantly impact the overall sentiment. Therefore, features with percentages below the threshold are excluded from being categorized as strengths, weaknesses, opportunities, or threats. The threshold ensures that only features with a more substantial presence in the reviews are considered for analysis, providing more meaningful insights.

## Explanation of Output:

The output consists of four sections: "Strengths," "Weaknesses," "Opportunities," and "Threats." Each section provides insights into different aspects of the collected data, such as positive and negative reviews, as well as the percentages of various features within these categories. Additionally, the output includes overall percentages of positive and negative reviews.

### Strengths:
Derived from the positive sentiment reviews of the target SME product. Represents the percentage of positive reviews, indicating aspects of the product that customers perceive as strong points. The "Within_Positive" percentage indicates the proportion of positive reviews mentioning a particular feature compared to all positive reviews.

### Weaknesses:
Extracted from the negative sentiment reviews of the target SME product. Reflects the percentage of negative reviews, highlighting areas where the product falls short or faces challenges. Similar to strengths, the "Within_Negative" percentage indicates the proportion of negative reviews mentioning a particular feature compared to all negative reviews.

### Opportunities:
Derived from the negative sentiment reviews of the competitor product. Represents the percentage of negative reviews for the competitor's product, indicating potential areas for improvement or expansion for the target SME. Calculated similarly to weakness but based on the competitor's negative sentiment reviews.

### Threats:
Extracted from the positive sentiment reviews of the competitor product. Reflects the percentage of positive reviews for the competitor's product, highlighting potential risks that the target SME may face. Calculated similarly to strengths but based on the competitor's positive sentiment reviews.

## Notes

- Ensure your environment has access to GPU resources if you are running the model locally for faster inference times.
- The script uses transformers, which may download models the first time you run the script. Make sure you have an active internet connection for the initial run.
- This script may require modification if the structure of the Flipkart website changes.


# ELEVATEBIZ SWOT Analysis Web Application

This project is a React-based web application designed for conducting and displaying SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis. The application is part of the ELITBIZ product and focuses on presenting the SWOT analysis results in a user-friendly and visually appealing manner.

## Features

- **SWOT Analysis Visualization:** Displays the Strengths, Weaknesses, Opportunities, and Threats in four distinct boxes.
- **General Inference:** Provides a section for displaying general inferences drawn from the SWOT analysis.
- **Responsive Design:** Ensures the application is accessible and functional across various devices and screen sizes.

## Requirements

Before you begin the installation process, ensure you have the following prerequisites installed on your system:

- **Node.js:** The runtime environment required to run the application.
- **npm (Node Package Manager):** The package manager for JavaScript, used to install dependencies.

## Installation

Follow these steps to set up the project on your local machine:

1. **Install Node.js:** Download and install Node.js from the [official website](https://nodejs.org/).
2. **Install npm:** Run the following command in your terminal:
   ```
   npm install
   ```
3. **Create React App:** Initialize a new React application using the Create React App toolchain:
   ```
   npx create-react-app swot-analysis
   ```
4. **Add SWOT Analysis Component:** Navigate to the `src` folder of your new React app, and create two new files: `SwotAnalysis.js` and `SwotAnalysis.css`. Copy and paste the provided code into these files.
5. **Update App Component:** Replace the content of `App.js` and `App.css` with the provided code to include the SWOT Analysis component in your application.
6. **Start the Application:** Launch your React app by running:
   ```
   npm start
   ```

Your application should now be running on [http://localhost:3000](http://localhost:3000).

## Understanding Each Component

- **App.js:** Defines the main React component for the application, importing the necessary CSS file and the SwotAnalysis component. It renders the application's structure, including the header, SWOT Analysis component, and footer.
- **App.css:** Contains styling for the main application container and footer, ensuring a responsive and visually appealing layout.
- **SwotAnalysis.js:** A React component for inputting and displaying the SWOT analysis. It renders a container with text areas for each SWOT category and a section for general inferences.
- **SwotAnalysis.css:** Provides the styling for the SWOT analysis component, including the layout for the SWOT categories and the general inference section, ensuring a cohesive and attractive design.

