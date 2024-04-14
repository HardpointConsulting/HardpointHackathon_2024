import os
import pytesseract as pyt
from PIL import Image
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv


def email(data):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    def accept_mail(data):
        password = "<PASSWORD>"  # Replace with your Gmail app password
        me = "<COMPANY_MAIL>"  # Replace with your email address
        email_body = f"""\
        <html>
        <body>
        <p>Dear {data[0]},<br><br>
        I hope this email finds you well. I am writing to inform you that your request for sick leave has been approved, effective from {data[3]}. The duration of your sick leave is for {data[4]} days.<br><br>
        Upon review of your medical certificate, it has been noted that you are suffering from {data[2]}. We wish you a speedy recovery and urge you to prioritize your health during this time.<br><br>
        The medical certificate provided by Dr. {data[1]} confirms your diagnosis and recommends the necessary rest period to recover from the illness.<br><br>
        Please feel free to contact me if you require any further assistance or if there are any changes to your situation that need to be addressed. We value your health and well-being and are here to support you during your recovery.<br><br>
        Take care and get well soon.<br><br>
        Warm regards,<br>
        HR<br>
        INFO TECH Solutions
        </p>
        </body>
        </html>
        """
        message = MIMEMultipart('alternative', None, [MIMEText(email_body, 'html')])
        message['Subject'] = 'Sick leave Status'
        message['From'] = me
        message['To'] = data[5]
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(me, password)
            server.sendmail(me, data[5], message.as_string())
            server.quit()
            print(f'email sent: {email_body}')
        except Exception as e:
            print(f'error in sending mail: {e}')

    def deny_mail(data, missing):
        query = ["employee name", "doctor name", "disease name", "date of issue", "days of leave", "recipient email"]
        password = "<PASSWORD>"  # Replace with your Gmail app password
        me = "<COMPANY_MAIL>"  # Replace with your email address
        email_body = f"""\
        <html>
        <body>
        <p>Dear {data[0]},<br><br>
        We regret to inform you that your request for sick leave cannot be approved at this time. Upon review, it has been noted that {query[missing]} is missing from your submission.<br><br>
        In order to process your request, we kindly ask you to provide the missing information as soon as possible.<br><br>
        Once we receive the required information, we will review your request again and notify you of the outcome.<br><br>
        Thank you for your understanding and cooperation.<br><br>
        Regards,<br>
        Warm regards,<br>
        HR<br>
        INFO TECH Solutions
        </p>
        </body>
        </html>
        """
        message = MIMEMultipart('alternative', None, [MIMEText(email_body, 'html')])
        message['Subject'] = 'Sick Leave Approved'
        message['From'] = me
        message['To'] = data[5]
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(me, password)
            server.sendmail(me, data[5], message.as_string())
            server.quit()
            print(f'email sent: {email_body}')
        except Exception as e:
            print(f'error in sending mail: {e}')

    for i in range(len(data)):
        if data[i] is None:
            deny_mail(data, i)
            break
    else:
        accept_mail(data)

def analyze_medical_record(image_path, emailid):
    load_dotenv()
    # Function to perform OCR (Optical Character Recognition) on the given image
    def perform_ocr(image_path):
        try:
            img = Image.open(image_path)
            pyt.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
            text = pyt.image_to_string(img)
            return text
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print("An error occurred:", str(e))
            return None

    # Function to create a text file with the OCR result of the given image
    def create_file(image_path):
        try:
            with open("sample.txt", "w") as file:
                file.write(perform_ocr(image_path))
            print("File created successfully.")
        except Exception as e:
            print("An error occurred:", str(e))

    
    def extract_data(doc_result,query):
        try:
            result = chain.run(input_documents=doc_result, question=query)
        except:
            result = None
        return result

    # OCR and process the image
    create_file(image_path)

    # Load text from the created file
    loader = TextLoader("sample.txt")
    document = loader.load()

    # Text Splitting
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(document)

    # Embedding
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    # Q-A
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    chain = load_qa_chain(llm, chain_type="stuff")


    # Query to extract information
    queries = ["one word answer for name of patient", "one word answer for doctor's name", " one word answer for date mentioned", "one word answer for disease", "one word answer for number of days leave applied for"]

    # Perform Q-A for each query
    results = []
    for query in queries:
        doc_result = db.similarity_search(query)
        result = extract_data(doc_result,query)
        results.append(result)

# Delete the text file
    try:
        os.remove("sample.txt")
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    results.append(emailid)
    email(results)
    return results


