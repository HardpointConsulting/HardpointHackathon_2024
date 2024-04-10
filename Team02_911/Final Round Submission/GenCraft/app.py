import streamlit as st
from src import main
import json
import numpy as np
import base64
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
import pinecone
from transformers import pipeline
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
from datetime import datetime
from streamlit_card import card
from dotenv import load_dotenv
import os

st.set_page_config(page_title="AdWiseInsights", page_icon="🧊", layout="wide")

load_dotenv()
PINECONE_API_KEY = "a703538c-4839-4a6d-8c5d-6f00e0e1face"
PINECONE_ENV = "gcp-starter"
OPENAI_API = "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"

df = pd.read_parquet("data/product_reviews.parquet")
df["date"] = pd.to_datetime(df["date"]).dt.date
docs = list(df["content"])
with open("data/product_details.json", "r") as file:
    product_details = json.load(file)

num_of_reviews = df.shape[0]
average_rating = df["rating"].mean()
num_of_unique_ecommerce_sites = (
    df["source"].astype(str).str.split("provided by").str[-1].nunique()
)


@st.cache_resource
def get_sentiment_model():
    # Create a database session object that points to the URL.
    classifier = pipeline(
        "text-classification", model="distilbert-base-uncased-finetuned-sst-2-english"
    )
    return classifier


classifier = get_sentiment_model()



def display_product_data():
    with open("data/product_details.json", "r") as file:
        product_details = json.load(file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            product_details["media"][0],
            # Manually Adjust the width of the image as per requirement
            width=200,
        )
    with col2:
        product_details = {key: product_details[key] for key in {"title", "prices"}}

        st.json(product_details)


with st.sidebar:
    choose = option_menu(
        "App Gallery",
        [
            "About",
            "Customer modeling",
            "Review Analytics",
            "Track Churn/Repeat",
            "Contact",
        ],
        icons=[
            "house",
            "people-fill",
            "messenger",
            "file-earmark-code",
            "person lines fill",
        ],
        menu_icon="app-indicator",
        default_index=0,
    )

#    if choose != "About" and choose != "Contact":
#        OPENAI_API = st.text_input(
#            "Enter **OpenAI API Key**", key="chatbot_api_key", type="password"
#        )


if choose == "About":
    st.title(
        ":speech_balloon: ReviewSense \n\n *Customer Insights to aid marketing campaigns at your Fingertips*"
    )
    #    with open("news.md", "r") as f:
    #        st.success(f.read())

    with open("docs/main.md", "r") as f:
        st.info(f.read())
    st.success(
        """
                **Tech Stack** : Python, Pinecone, Langchain, Streamlit, Hugging Face, OpenAI \n
                The entire project is open-source and hosted on [GitHub](https://github.com/pjeena/Customer_insights_to_aid_marketing).
        
        """
    )


elif choose == "Customer modeling":
    with st.form("form_1", clear_on_submit=True):
        url = st.text_input(
            "**:violet[Enter the URL of a product from [Google Shopping](https://shopping.google.com/)]**",
            "",
        )
        query = st.text_input(
            "**:violet[Enter relevant query representing product reviews]** *(Example : The shoes/speakers are fantastic)*",
            "",
        )
        num_reviews = st.slider("**:violet[No of reviews to analyse]**", 0, 100, 20)
        st.write(
            "<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>",
            unsafe_allow_html=True,
        )
        st.write(
            "<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>",
            unsafe_allow_html=True,
        )
        rating = st.radio("**:violet[Rating]**", [1.0, 2.0, 3.0, 4.0, 5.0], 4)
        submitted = st.form_submit_button("**Submit**")
        if submitted:
            with st.spinner('**Fetching product details and scraping reviews...**'):
                main.get_product_details_and_reviews(url)

    if url != "":
        display_product_data()

    if "clicked" not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    if st.button(
        "**:violet[Click here to get a summary of reviews and an advertisement copy for personalized marketing]**",
        on_click=click_button,
        use_container_width=True,
    ):
        if url != "" and query != "":
            with st.spinner('**Generating embeddings, uploading to vector database and generating summary...**'):
#            summary, advertisement = "text", "text"
                summary, advertisement = main.main(query, num_reviews, rating)
    
                #            st.markdown("**:green[Summary]** : *{}*".format(summary))
                #            st.markdown("**:green[Advertisement]** : *{}*".format(advertisement))
    
                if "summary" not in st.session_state:
                    st.session_state["summary"] = summary
                if "advertisement" not in st.session_state:
                    st.session_state["advertisement"] = advertisement

        else:
            st.warning(
                "Enter OPENAI API key correctly or URL/query regarding a product from Google Shopping",
                icon="⚠️",
            )

#    if OPENAI_API.startswith('sk-'):
    if st.session_state.clicked:
            st.markdown("**:green[Summary]** : *{}*".format(st.session_state["summary"]))
            st.markdown(
                "**:green[Advertisement]** : *{}*".format(st.session_state["advertisement"])
            )


elif choose == "Review Analytics":
    #   dash_1 = st.container()

    #   with dash_1:
    #       st.markdown(
    #           "<h2 style='text-align: center;'>Superstore Sales Dashboard</h2>",
    #           unsafe_allow_html=True,
    #       )
    #        st.write("")

    dash_2 = st.container()
    with dash_2:
        col1, col2, col3 = st.columns(3)

        col1.metric(label="No of relevant Reviews", value=num_of_reviews)
        col2.metric(label="Average Rating", value=np.round(average_rating, 2))
        col3.metric(
            label="No of e-commerce outlets registered",
            value=num_of_unique_ecommerce_sites,
        )

        style_metric_cards(border_left_color="#d472bc")

    dash_6 = st.container()
    with dash_6:
        if "clicked_1" not in st.session_state:
            st.session_state.clicked_1 = False

        def click_button():
            st.session_state.clicked_1 = True

        if st.button(
            "**:violet[Click here to generate overall textual impression and provide suggestions for improvement]**",
            on_click=click_button,
            use_container_width=True,
        ):
            with st.spinner('**Generating overall summary and ideas for improvement...**'):
                overall_review = main.generate_review_analytics(
                    product=product_details["title"]
                )
                # overall_review = "fgfg"
                if "overall_review" not in st.session_state:
                    st.session_state["overall_review"] = overall_review
            #           st.markdown(overall_review)

        if st.session_state.clicked_1:
            st.markdown("{}".format(st.session_state["overall_review"]))


 
elif choose == "Track Churn/Repeat":
    #    dash_1 = st.container()

    #    with dash_1:
    #        st.markdown(
    #            "<h2 style='text-align: center;'>Churn Analytics</h2>",
    #            unsafe_allow_html=True,
    #        )

    dash_2 = st.container()
    with dash_2:
        with st.form("form_1"):
            query = st.text_input(
                "**:violet[Enter relevant query associated with churn or repeat purchases]** *(Example : Churn/Repeat : disappointed with the purchase/will purchase again)*",
                value="will purchase again",
            )
            st.write(
                "<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>",
                unsafe_allow_html=True,
            )
            st.write(
                "<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>",
                unsafe_allow_html=True,
            )
            rating = st.radio("**:violet[Rating]**", [1.0, 2.0, 3.0, 4.0, 5.0], 4)
            submitted = st.form_submit_button(
                "**Submit**",
                use_container_width=True,
            )

        st.markdown("##")

        if "clicked_2" not in st.session_state:
            st.session_state.clicked_2 = False

        def click_button():
            st.session_state.clicked_2 = True

        if st.button(
            "**:violet[Click here to generate list of customers who are likely to churn/repeat]**",
            use_container_width=True,
            on_click=click_button,
        ):
            if query != "":
                with st.spinner('**Generating list of churned/repeat customers...**'):
                    df_customer_list = main.generate_churn_and_repeat_customers(
                        query, rating
                    )
    
                    # style
                    th_props = [
                        ("font-size", "14px"),
                        ("text-align", "center"),
                        ("font-weight", "bold"),
                        ("color", "#6d6d6d"),
                        ("background-color", "#f7ffff"),
                    ]
    
                    td_props = [("font-size", "12px")]
    
                    styles = [
                        dict(selector="th", props=th_props),
                        dict(selector="td", props=td_props),
                    ]
    
                    # table
                    df_customer_list_table = (
                        df_customer_list.style.set_properties(**{"text-align": "left"})
                        .set_table_styles(styles)
                        .hide(axis="index")
                    )
    
                    if "df_customer_list_table" not in st.session_state:
                        st.session_state["df_customer_list_table"] = df_customer_list_table
    
                    if "df_customer_list" not in st.session_state:
                        st.session_state["df_customer_list"] = df_customer_list

            else:
                st.warning("Enter a query relevant to the product", icon="⚠️")

        if st.session_state.clicked_2:
            df_customer_list_table = st.session_state["df_customer_list_table"]
            df_customer_list = st.session_state["df_customer_list"]
            st.table(df_customer_list_table)

            csv_file = df_customer_list.to_csv(index=False).encode("utf-8")

            st.download_button(
                ":red[Press to Download as excel file]",
                csv_file,
                "customers_list_churn_or_repeat.csv",
                "data/xslx",
                key="download-csv",
            )


elif choose == "Contact":
    with open("docs/intro.md", "r") as f:
        st.info(f.read())

# if __name__ == "__main__":
#    import time

#    start = time.time()

#    URL = "https://www.google.com/shopping/product/r/FR/10131092341654226490?prds=oid:7150038858920687208,eto:7150038858920687208_0,epd:7150038858920687208,prmr:1,rsk:PC_2718491079951339247&rss=ChZQQ18yNzE4NDkxMDc5OTUxMzM5MjQ3&hl=en&sa=X&ved=2ahUKEwidgKLRmqmCAxWWUkECHaXFAooQkLoIegQIAhBW"
#    query = "easy to read font and good battery life"
#    summary, advertisement = main.main(URL, query, num_reviews=20, rating_num=5)
#    summary, advertisement = "text", "text"
#    print(summary)
#    print(
#       "-------------------------------------------------------------------------------------------------------"
#    )
#    print(advertisement)

#    end = time.time()
#    print(end - start)
