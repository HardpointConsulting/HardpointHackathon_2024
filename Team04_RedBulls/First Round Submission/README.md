# Problem Statement

To develop a system capable of automatically extracting the title and author information from scientific documents and generating  alternative titles based on the document content. Thesystem should analyse the text of each document printout, identify the title and author(s), and then propose alternative titles that capture the essence of the document's content.

# How does it work

Develop a project leveraging Python libraries like Pytesseract for optical character recognition (OCR), OpenCV (cv2) for image processing, and Hugging Face models for natural language processing (NLP). The project aims to extract information such as titles and authors' names from research paper images. Utilizing OCR techniques, text is extracted from the images. Then, employing NLP models, the project identifies the paper's title and authors. Additionally, it generates alternative titles for the paper to enhance discoverability and comprehensibility. Finally, the extracted information, including the original title, authors' names, and alternative titles, is stored in an Excel sheet for further analysis and reference. This project facilitates automated data extraction and organization from research paper images, streamlining the research process and aiding researchers in managing and exploring academic literature effectively.

# Tools used

* Pytesseract
* OpenCV
* Hugging Face Models - facebook/nougat-base, AryanLala/autonlp-Scientific_Title_Generator-34558227
* Excel Sheet
* openpyxl

# How to Run the Code

1. Clone the git repository using ```git clone git@github.com:HardpointConsulting/HardpointHackathon_2024.git```.
2. Go to ```Team04_RedBulls/First Round Submission```.
3. Install necessary libraries by running ```pip install -r requirements.txt```.
4. Download pytesseract from [Download Pytesseract](https://sourceforge.net/projects/tesseract-ocr.mirror/)
5. Add ```pytesseract file``` path to ```main.py```.
6. Run ```requirements.txt``` using ```pip install -r requirements.txt```
7. Paste path of required Research paper.
8. Run python ```main.py```.
