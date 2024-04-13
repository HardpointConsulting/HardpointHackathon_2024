import pytesseract as pyt
import cv2
from transformers import pipeline
from PIL import Image
from openpyxl import Workbook

# path of document image
path = "sample-image\\doc_000016.png"

# loading image
img = cv2.imread(path)

#converting to gray scale to improve text visibility
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# increasing sharpness of text
ret, thresholded_image = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)
sharpened = cv2.convertScaleAbs(thresholded_image, alpha=8, beta=8)

# extracting text
pyt.pytesseract.tesseract_cmd = "Tesseract-OCR\\tesseract.exe"
text = pyt.image_to_string(sharpened)[:300]


# Authors Names Extraction using NER model
ner = pipeline("ner", grouped_entities=True)
t = ner(text)
auth = []
for i in range(len(t)):
    if t[i]['entity_group'] == 'PER':
        if(len(t[i]['word'])<=1):
            auth.append(t[i]['word'].replace(",","").replace("\'","").replace(" ","").replace("  ","") + ".")  #removing unwanted characters and white-spaces
        else:
            auth.append(t[i]['word'] + ",")
auth_name = " ".join(auth)


#Extract Title of the document
title_extract = pipeline("image-to-text", model="facebook/nougat-base")
title=""

# load the image
img = Image.open(path)
title = title_extract(img)[0]['generated_text'].replace("#","").replace("\n"," ")
# print(title)

# Alternate Title Generation
alt = pipeline("text2text-generation", model="AryanLala/autonlp-Scientific_Title_Generator-34558227")
alt_title = alt(text,max_length=10,min_length=3)[0]['generated_text']
# print(alt_title)

result = []
result.append(title)
result.append(auth_name)
result.append(alt_title)
# print(result)


# Exporting extracted data to Excel

# create a new Excel workbook if it doesn't exist
workbook = Workbook()

# select the active worksheet
sheet = workbook.active


# write each element of the array into a separate column
for index, value in enumerate(result, start=1):
    sheet.cell(row=2, column=index, value=value)
  
# save the workbook to a file
workbook.save('Output_format.xlsx')
