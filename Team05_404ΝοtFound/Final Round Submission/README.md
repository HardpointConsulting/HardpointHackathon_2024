# Amazon Product Review Analysis

This Python script analyzes product reviews from an Amazon product page, performs sentiment analysis, identifies common problems mentioned in negative reviews, and generates potential solutions using a language model. It also visualizes the distribution of sentiments and trends in review scores over time.

## Dependencies

- [requests](https://pypi.org/project/requests/): For making HTTP requests
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/): For parsing HTML
- [pandas](https://pypi.org/project/pandas/): For data manipulation and analysis
- [nltk](https://pypi.org/project/nltk/): For natural language processing tasks
- [matplotlib](https://pypi.org/project/matplotlib/): For data visualization
- [transformers](https://huggingface.co/transformers/): For using pre-trained language models
- [datetime](https://docs.python.org/3/library/datetime.html): For handling date and time

## Setup

1. Install the required dependencies using pip:

   ```bash
   pip install requests beautifulsoup4 pandas nltk matplotlib transformers
   ```

2. Ensure NLTK data is downloaded:

   ```python
   import nltk
   nltk.download('vader_lexicon')
   nltk.download('stopwords')
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

## Usage

1. Run the script `amazon_product_review_analysis.py`.
2. Provide the URL of the Amazon product page to analyze.
3. The script will perform sentiment analysis, identify common problems, and generate potential solutions.
4. Results will be saved in CSV files (`amazon_review.csv`, `cleaned_text.csv`, `sentiment_analysis_results.csv`) and visualization plots (`review_count.png`, `trent_analysis_plot.png`).

## Additional Information

- The script utilizes the VADER sentiment analyzer for sentiment analysis.
- Preprocessing steps include text cleaning, tokenization, stop word removal, and lemmatization.
- Identified problems are based on predefined keywords associated with common issues mentioned in product reviews.
- Solutions are generated using a pre-trained language model (DistilGPT-2).
- Results are saved in CSV files for further analysis, and visualization plots are generated for easy interpretation.

