# <span style="font-size:larger;">TEAM 10: ACCEPTALLCOOKIES</span>

# <span style="font-size:larger;">Document Summarization in Various Fields</span>

---

## <span style="font-size:larger;">Contents</span>

1. [Introduction](#introduction)
2. [Features](#features)
3. [Setup](#setup)
5. [Dataset](#dataset)
6. [Usage](#usage)
7. [UI/UX](#ui/ux)
8. [Technologies Used](#technologies-used)
9. [Screen Recording](#Screen-Recording)
10. [Team Members](#Team-Members)

---

## <span id="introduction">Introduction</span>

We , AcceptAllCookies made this Document Summzarization so as to tackle the time wastage one has to read the wntire documents and try to gather informations.
This helps in saving time and resources and, we can use this time productively in our environment.
We tried to implement summarization in many fields  but due to the time constraint , we have only done it on Legal,Finance and Research.

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
   
## <span id="ui/ux">UI/UX</span>

Therees a front end which was initially designed, but had to be dropped down, as we didn't have the coding skills required to connect it using the frameworks(flask/django).
The UI/UX designed , if implemented becomes a very promising one.But due to knowledge/time constraints , we had to use the streamlit as our backup plan


[Click here to view the Figma prototype](https://www.figma.com/proto/Ri7WaYfC3V2CP2fvgtgAZ3/team-14?page-id=0%3A1&type=design&node-id=202-1545&viewport=-26%2C980%2C0.31&t=SApTnsVenbevqAI9-1&scaling=scale-down-width)

[This is the screen recording demo of the UI/UX design](https://vimeo.com/932845614?share=copy)

[Click here to view the Figma design](https://www.figma.com/file/Ri7WaYfC3V2CP2fvgtgAZ3/team-14?type=design&node-id=199-229&mode=design&t=LJRZHvKahQgsajia-0)

Flochart of the working
[Flowchart](https://drive.google.com/file/d/1vHhlnJYs2uZ9qao8cUkKvaR_idv8Rl6c/view?usp=sharing)


## <span id="Technologies-used">Technologies Used</span>

The technologies used here are
1. Python
2. Streamlit
3. Pretrained Models from HuggingFace
4. Pytorh


## <span id="Screen-Recording">Screen Recording</span>
[Click here to watch the screen recording of the project](https://drive.google.com/file/d/1x6Vhd33IKsg5sr2Zgi6EgrFHctod8pCY/view?usp=sharing)

## <span id="Team-Members">Team-Members</span>
1. Fatimahziya AT (Team Lead)
2. Aswin MM (Documentation)
3. SarathKumar K(Data/ML Engineer)
4. Jeeva Vinod(Data/ML Engineer)
5. Arfan BT(Software Enginner)



