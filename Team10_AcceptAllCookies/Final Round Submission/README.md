# <span style="font-size:larger;">TEAM 10: ACCEPTALLCOOKIES</span>

# <span style="font-size:larger;">Document Summarization in Various Fields</span>

---

## <span style="font-size:larger;">Contents</span>

1. [Introduction](#introduction)
2. [Features](#features)
3. [Setup](#setup)
4. [Dataset](#dataset)
5. [Usage](#usage)
6. [Technologies Used](#technologies-used)

---

## <span id="introduction">Introduction</span>

We , AcceptAllCookies made this Document Summzarization so as to tackle the time wastage one has to read the wntire documents and try to gather informations.
This helps in saving time and resources and, we can use this time productively in our environment.
We tried to impllement summarization in many fields  but due to the time constraint , we have only done it on Legal,Finance and Research.

## <span id="features">Features</span>

We have used pretrained models from hugging face  such as BART and BERT.
The key to finding the right model is to find one, where the resources/computational time are not much and accuracy is upto the mark.
Now, we couldhave used OPENAI etc keys and done it , but some of the reasons i felt are that, firstly we could do customization on models to adapt to the style/language of the documents we are summarizing.We could also adjust parameters, training procedures to optimize the model's performance for use case.
There's an flexibility which comes along with this
And basically since we didnt use these models in projects , we were curious on how theese models worked.
## <span id="setup">Setup</span>
Running through the setup we have to
1. Make sure to have Python installed.
2. Have Streamlit installed.
   2.<sup>1</sup> Use `pip install streamlit` to install it.
3. Have Transformers installed.
   3.<sup>1</sup> Use `pip install transformers` to install it.
4. Have PyTorch installed.
   4.<sup>1</sup> Use `pip install torch` to install it.


## <span id="dataset">Dataset</span>

We got one dataset from actual sources, ie for legal documents summarization.
For the others , we created a dummy dataset and we went along with it.
This was done as we were not doing any training of the pre-trained model usinng sickit (keras).
## <span id="usage">Usage</span>

1. Run the code file , whether be it legal,research or finance using streamlit.
2. Once ran, it wil direct you to web browser.
3. Add the input documents from the sidebar
4. It wil summarise the document once we add the documents automatically
5. The summarised document text will be displayed on the screen.
   

## <span id="technologies-used">Technologies Used</span>

The technologies used here are
1. Python
2. Streamlit
3. Pretrained Models from HuggingFace



https://vimeo.com/932845614?share=copy
