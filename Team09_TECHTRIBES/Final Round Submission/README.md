# RockyBot: News Research Tool 📈

RockyBot is a Streamlit web application designed to help users conduct research on news articles. It utilizes natural language processing (NLP) techniques to extract relevant information and answer questions based on the processed data.

## Features

- Process multiple news article URLs simultaneously.
- Extract key information and generate answers to user queries using the OpenAI API.
- Display sources for the provided answers.

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/rockybot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd rockybot
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

5. Run the Streamlit app:

    ```bash
    streamlit run main.py
    ```

6. Access the app in your web browser at the provided URL.

## Usage

1. In the sidebar, input up to three news article URLs.
2. Click the "Process URLs" button to extract information from the provided articles.
3. Once the processing is complete, input your question in the text box labeled "Question."
4. Press Enter to submit your question and view the generated answer along with relevant sources.

## Technologies Used

- Python
- Streamlit
- langchain (for NLP tasks)
- OpenAI API
- FAISS (Facebook AI Similarity Search)

