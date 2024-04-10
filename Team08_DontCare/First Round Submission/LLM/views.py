from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os
import pytesseract as pyt
from PIL import Image
import google.generativeai as genai
from .models import *
import time
from dotenv import load_dotenv
from openpyxl import Workbook

load_dotenv()

def home(request):
    #Home page of the website
    return render(request,'upload.html')

def upload(request):
    files=[]
    
    #Remove previous dataset
    folder_path='media/dataset'
    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Get a list of all files in the folder
        files=os.listdir(folder_path)
        
        # Check if the folder is not empty
        if files:
            # Iterate over each file and delete it
            for file_name in files:
                file_path=os.path.join(folder_path, file_name)
                os.remove(file_path)
    
    if request.method == 'POST':
        # Access uploaded files
        uploaded_files = request.FILES.getlist('file')  # Access all uploaded files as a list

        # Loop through each uploaded file
        for uploaded_file in uploaded_files:
            # Check if file type is png
            if uploaded_file.content_type.startswith('image/png'):  # Adjust for desired file types
                # Construct the file path
                file_path = os.path.join(settings.MEDIA_ROOT, 'dataset', uploaded_file.name)
                files.append(file_path)

                # Save the uploaded file
                with open(file_path, 'wb') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

        #Configure tesseract ocr
        pyt.pytesseract.tesseract_cmd='Tesseract-OCR/tesseract.exe'
        
        #Configure Google Gemini api for prompting
        genai.configure(api_key=os.getenv('API_KEY'))
        generation_config={"temperature": 0.9,"top_p": 1,"top_k": 1,"max_output_tokens": 2048}
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]
        model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config,safety_settings=safety_settings)
        convo = model.start_chat(history=[])
        
        #Clear all previous entries in the database table
        if Output.objects.exists():
            Output.objects.all().delete()

        #passing pngs one by one to the llm for prompting
        i=1
        for path in files:
            content=pyt.image_to_string(Image.open(path))
            try:
                convo.send_message(f'Get the title of the text provided in {content}. Return the output as a string of the exact name as the title of the content. Do not add any other content of your own in the output.')
                title=convo.last.text
                convo.send_message(f'Get the names of the authors in {content}. Return the output as a string of all the names of authors separated by commas. Do not add any other content of your own in the output.')
                authors=convo.last.text
                convo.send_message(f'Generate an alternate title for the text provided in {content}. Return the output as a string of an alternate title. Do not make the title too long.')
                alt=convo.last.text
            except Exception as e:
                continue

            #Stores the title,authorand alternate title in the database
            output=Output(id=i,title=title,authors=authors,alt=alt)
            output.save()
            i+=1
            os.remove(path) #Remove page from folder once information is extracted
        
        #passing object of table to frontend
        response=Output.objects.all()
        return render(request,'view.html',{'response':response})
    else:
        error = "Upload PDF"
        return render(request,'error.html',{'error':error})

def create(request):
    data=Output.objects.all()
    
    wb=Workbook()
    ws=wb.active

    ws.append(['S No.','Document Title','Author(s)','Generated Title'])
    for i in data:
        ws.append([i.id,i.title,i.authors,i.alt])

    file_path = os.path.join(settings.MEDIA_ROOT,'excel','titlr.xlsx')

    wb.save(file_path)
    return render(request,'download.html')
