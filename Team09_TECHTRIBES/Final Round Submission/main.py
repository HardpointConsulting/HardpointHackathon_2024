import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500, openai_api_key=os.getenv("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"))

if process_url_clicked:
    if all(urls):  # Check if all URLs are provided
        # Load data
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("Data Loading...Started...✅✅✅")
        data = loader.load()

        # Split data
        main_placeholder.text("Text Splitter...Started...✅✅✅")
        embeddings = OpenAIEmbeddings()
        vectorstore_openai = FAISS.from_documents(data, embeddings, chunk_size=1000)
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
        time.sleep(2)

        # Save the FAISS index to a pickle file
        with open(file_path, "wb") as f:
            pickle.dump(vectorstore_openai, f)
    else:
        st.error("Please provide all URLs before processing.")

query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.write(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                for source in sources:
                    st.write(source)
