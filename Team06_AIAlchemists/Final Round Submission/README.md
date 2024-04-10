FRONTEND

FrontEnd - React App 

The front end is a React-based application designed for conducting a SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis. 
The Strengths, Weaknesses, Opportunities, Threats are displayed in 4 boxes and a general inference is also displayed.

The main components of the application are: 
App.js & App.css
SwotAnalysis.js & SwotAnalysis.css

Requirements 
Node.js must be installed
npm (Node Package Manager) must be installed
Create React App : Toolchain to make the base components of react app 

Installation 
Install Node.js from the official site - https://nodejs.org/en
Install npm using the command  npm install  
Create a new app using the command  npx create-react-app swot-analysis
 Create a new file SwotAnalysi.css and other file called SwotAnalysis.js  in the src folder and copy paste the code as given below
Also update the  App.js and App.css as given below

App.js
	
import React from 'react';
import './App.css';
import SwotAnalysis from './SwotAnalysis';

function App() {
  return (
    <div className="App">
      <h2 className="product-name">ElevateBiz</h2>
      <SwotAnalysis />
      <footer className="footer">
        by AI Alchemists
      </footer>
    </div>
  );
}
export default App;
App.css
	
.App {
    text-align: left; /* Align text to the left */
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    min-height: 100vh; /* Ensure the container fills the viewport height */
    justify-content: space-between; /* Push footer to the bottom */
  }

  .footer {
    width: 100%;
    background-color: #f0f0f0;
    color: #2D2D2D;
    text-align: center;
    padding: 20px 0;
    font-size: 1em;
    font-weight: bold;
    border-top: 1px solid #e6e6e6;
    position: fixed; /* Fixed to the bottom of the viewport */
    bottom: 0;
    left: 0;
    right: 0; /* Ensure it spans the full width */
  }


SwotAnalysis.js	

import React from 'react';
import './SwotAnalysis.css';

const SwotAnalysis = () => {
  return (
    <div className="swot-container">
      <div className="swot-boxes">
        <div className="box">
          <h3>Strength</h3>
          <textarea placeholder="Enter strengths..."></textarea>
        </div>
        <div className="box">
          <h3>Weakness</h3>
          <textarea placeholder="Enter weaknesses..."></textarea>
        </div>
        <div className="box">
          <h3>Opportunities</h3>
          <textarea placeholder="Enter opportunities..."></textarea>
        </div>
        <div className="box">
          <h3>Threats</h3>
          <textarea placeholder="Enter threats..."></textarea>
        </div>
      </div>
      <div className="general-inference">
        <h2>General Inference</h2>
        <textarea placeholder="Enter general inference here..."></textarea>
      </div>
    </div>
  );
};

export default SwotAnalysis;


SwotAnalysis.css	

body {
  background: linear-gradient(135deg, #e2efff 0%, #ffddf0 100%);
  font-family: 'Arial', sans-serif;
}

.product-name {
  font-size: 32px; /* Relatively big font size */
  font-weight: bold; /* Bold font weight */
  text-align: left; /* Align text to the left */
  margin: 20px 0 -60px 0; /* Add some space above and below the heading */
  padding-left: 50px; /* Align with the content, assuming the same padding as the container */
}

.App {
  min-height: 100vh;
  position: relative; /* Needed for absolute positioning of the footer */
  padding-bottom: 60px; /* Space for the footer */
  box-sizing: border-box; /* Include padding in the height calculation */
}

.app-container {
  min-height: 100vh; /* Ensure the container fills the viewport height */
  display: flex;
  flex-direction: column; /* Stack children vertically */
  justify-content: space-between; 
}

.swot-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 0 50px;
}

.swot-boxes {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  width: calc(100% - 100px);
  margin: auto;
}

.box {
  padding: 40px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 200px;
  background: rgba(255, 255, 255, 0.25);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(8.5px);
  -webkit-backdrop-filter: blur(8.5px);
  border-radius: 10px;
  color: #2D2D2D; /* Dark text color for readability */
  font-size: 1.2em;
  flex-direction: column; /* Ensure items are stacked vertically */
  align-items: center; /* Center align items horizontally */
  text-align: center;
}

.box h3 {
  margin-top: 0; /* Decrease the top space of the headings */
  margin-bottom: 10px; /* Adjust space between the heading and the textarea */
  color: #2D2D2D; /* Dark text color for readability */
  font-size: 1.4em; /* Adjust if you want to change the size of the heading */
}

.box textarea {
  width: 100%; /* Make the textarea take up the full width of the box */
  height: 150px; /* Increase the height of the textarea */
  margin-top: 0; /* Decrease the top space above the textarea if needed */
  background: #FFFFFF; /* Solid white background for the textarea */
  border: 1px solid rgba(255, 255, 255, 0.5); /* Adjust border as needed */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  border-radius: 10px; /* Rounded corners for the textarea */
  padding: 15px; /* Increase padding for larger text area */
  color: #2D2D2D; /* Dark text color for readability */
  font-size: 1em; /* Maintain font size */
  resize: vertical; /* Allow only vertical resizing */
}

.box textarea {
  /* Apply the same styles to both general inference and box textareas */
  background: rgba(255, 255, 255, 0.25);
  border: none;
  backdrop-filter: blur(8.5px);
  -webkit-backdrop-filter: blur(8.5px);
  border-radius: 10px;
  padding: 20px;
  color: #2D2D2D;
  font-size: 1em;
}

.general-inference {
  width: calc(100% - 100px);
  margin: 20px 50px;
}

.general-inference textarea {
  width: 100%; /* Maintain full width within its container */
  height: 200px; /* Revert to original height */
  background: rgba(255, 255, 255, 0.25); /* Keep the updated background style */
  border: none;
  backdrop-filter: blur(8.5px);
  -webkit-backdrop-filter: blur(8.5px);
  border-radius: 10px;
  padding: 20px; /* Maintain the padding */
  color: #2D2D2D; /* Keep the text color */
  font-size: 1em; /* Maintain the font size */
  resize: none; /* Prevent resizing */
}

.footer {
  width: 100%;
  background-color: #f0f0f0;
  color: #2D2D2D;
  text-align: center;
  padding: 20px 0;
  font-size: 1em;
  font-weight: bold;
  border-top: 1px solid #e6e6e6;
  position: fixed; /* Fixed to the bottom of the viewport */
  bottom: 0;
  left: 0;
  right: 0;
}

body {
  margin-bottom: 60px; /* Adjust this value based on the footer's height */
}





Understanding Each Component

App.css
This CSS file defines the styling for the main application container (.App) and the footer (.footer). The .App class styles ensure that the app content is displayed using a flexbox layout, with text aligned to the left and the content stretching to fill the viewport height. The footer is styled to be fixed at the bottom of the viewport, with a specific background color, text color, and border.

App.js
This JavaScript file defines the main React component for the application. It imports the React library, the App component's CSS file, and a SwotAnalysis component. The App function returns a JSX structure that includes a heading for the product name, the SwotAnalysis component, and a footer crediting "AI Alchemists". The App component is then exported for use in other parts of the application.







SwotAnalysis.js
This file defines a React component for conducting a SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis. It imports React and a CSS file specific to the SWOT analysis. The component renders a container with four boxes for entering strengths, weaknesses, opportunities, and threats, as well as a section for general inference. Each box and the general inference section contain a textarea for input.


SwotAnalysis.css
This CSS file provides the styling for the SWOT analysis component. It includes styles for the body, product name, SWOT analysis container, boxes, and text areas. The styling creates a visually appealing layout with a background gradient, rounded corners, shadows, and specific fonts. The .box class styles are applied to the individual SWOT categories, and the .general-inference class styles the general inference section.



Together, these files create a web application that allows users to perform a SWOT analysis. The application is styled to be user-friendly and visually appealing, with a responsive layout that adapts to different screen sizes






BACKEND

The provided code creates a comprehensive README file for a Python script that analyzes reviews, extracts features, classifies features, and generates marketing messages. Here's a breakdown of the code sections:

**1. Libraries:**

- Imports necessary libraries like `selenium` for web scraping, `transformers` for sentiment analysis and text generation, `pandas` for data manipulation, and `BeautifulSoup` for HTML parsing.

**2. Helper Functions:**

- `initialize_driver`: Initializes a Chrome WebDriver using `webdriver_manager`.
- `scrape_reviews`: Scrapes reviews from a URL iteratively, returning a list of reviews.
- `analyze_sentiment`: Analyzes sentiment of a review using a pre-trained sentiment classification model.
- `pre_process_comment`: Preprocesses a comment (optional, like lowercasing and removing punctuation).
- `extract_features`: Uses a question-answering pipeline to extract features based on sentiment (e.g., "What are the good qualities?" for positive reviews).
- `classify_features`: Classifies features using a zero-shot classification pipeline based on predefined labels.
- `split_df_by_sentiment`: Splits a DataFrame containing reviews by sentiment (positive or negative).
- `get_feature_percentage`: Calculates feature percentages for positive, negative, and overall sentiment.
- `find_pos_neg_features`: Identifies positive and negative features based on a threshold percentage.

**3. Main Function:**

- `main`: The main function that performs the analysis. It takes an initial URL for scraping reviews as input.
    - Sets the path to the Chrome WebDriver, sentiment analysis model name, and classification labels.
    - Initializes a Chrome WebDriver and scrapes reviews from the URL.
    - Creates a DataFrame from the reviews.
    - Analyzes sentiment for each review.
    - Extracts features based on sentiment.
    - Classifies features.
    - Splits the DataFrame by sentiment.
    - Calculates feature percentages.
    - Identifies positive and negative features.
    - Generates marketing messages using GPT-2 (commented out for now).
    - Prints strengths, weaknesses, and marketing messages (if generated).

**4. GPT-2 Marketing Message Generation (Commented Out):**

- This section defines functions to generate marketing messages based on product description, strengths, weaknesses, brand name, and origin. It uses a GPT-2 model for text generation (commented out as it might require additional setup).

**5. Script Execution:**

- The script executes the `main` function for a Blue Pearl watch URL and a competitor (Fastrack) URL.
- It prints the strengths, weaknesses, and marketing messages (if generated) for both brands.

**Overall, this code provides a well-structured framework for analyzing reviews, extracting features, and generating marketing messages. Note that the GPT-2 marketing message generation is currently commented out.**


Here's how you can run the script assuming you have Python and the required libraries installed:

**1. Dependencies:**

Before running the script, make sure you have the necessary libraries installed. You can install them using the following command:

```bash
pip install requirements.txt
```

**2. Script Execution:**

- Save the script as `main.py`.
- Open your terminal and navigate to the directory where you saved the script.
- Run the script using the following command:

```bash
python main.py
```

This will execute the `main` function and analyze reviews from the URLs specified in the script (Blue Pearl watch and Fastrack). It will then print the strengths, weaknesses, and marketing messages (if the GPT-2 section is uncommented).

**Additional Notes:**

- Make sure you have a compatible version of ChromeDriver installed for `selenium` to work. You can download it from [URLchromedriver chrome version ON Google sites.google.com].
- The script uses pre-trained models for sentiment analysis and classification. You might need to download these models depending on the script's configuration. Refer to the documentation of the specific libraries used for model download instructions if necessary.
- The GPT-2 marketing message generation is currently commented out. Uncomment the relevant sections and potentially install additional libraries for text generation with GPT-2 if you want to use that functionality.
