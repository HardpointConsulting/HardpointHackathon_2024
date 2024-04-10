# call evaluate_resume(resume_path,mail)


import re
import PyPDF2

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def reject_mail(mail):
        password = "zkffesjsnywjlupp"  # Replace with your Gmail app password
        me = "harithatony17@gmail.com"  # Replace with your email address
        email_body = f"""\
        <html>
        <body>
        <p>Dear Applicant,<br><br>
        We regret to inform you that your application has been rejected at this time.<br><br>
        We appreciate your interest in the position and wish you the best of luck in your future endeavors.<br><br>
        Regards,<br>
        HR<br>
        INFO TECH Solutions
        </p>
        </body>
        </html>
        """
        message = MIMEMultipart('alternative', None, [MIMEText(email_body, 'html')])
        message['Subject'] = 'INFO TECH Recruitment Process'
        message['From'] = me
        message['To'] = mail
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(me, password)
            server.sendmail(me, mail, message.as_string())
            server.quit()
            print(f'email sent: {email_body}')
        except Exception as e:
            print(f'error in sending mail: {e}')

def accept_mail(mail):
        password = "zkffesjsnywjlupp"  # Replace with your Gmail app password
        me = "harithatony17@gmail.com"  # Replace with your email address
        email_body = f"""\
        <html>
        <body>
        <p>Dear Applicant,<br><br>
        We are pleased to inform you that your application has been selected for further consideration.<br><br>
        We will contact you shortly with more information.<br><br>
        Regards,<br>
        HR,<br>
        INFO TECH Solutions
        </p>
        </body>
        </html>
        """
        message = MIMEMultipart('alternative', None, [MIMEText(email_body, 'html')])
        message['Subject'] = 'INFO TECH Recruitment Process'
        message['From'] = me
        message['To'] = mail
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(me, password)
            server.sendmail(me, mail, message.as_string())
            server.quit()
            print(f'email sent: {email_body}')
        except Exception as e:
            print(f'error in sending mail: {e}')

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.

    Args:
    - pdf_path (str): The path to the PDF file.

    Returns:
    - str: The extracted text from the PDF.
    """
    try:
        import fitz  # PyMuPDF
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print("An error occurred while extracting text from PDF:", e)
        return None

def analyze_resume(resume_text):
    """
    Analyze a resume to determine the score.

    Args:
    - resume_text (str): The text content of the resume.

    Returns:
    - int: The score of the resume (out of 10).
    """
    # Define required skills
    required_skills = {"C", "Python", "SQL", "communication", "networking"}

    # Define required qualifications
    required_qualification_pattern = re.compile(r"(?i)(bca|cs|data science|computer application|ai aiml|ml|machine learning|computer science)")

    # Extract skills mentioned in the resume
    skills_mentioned = re.findall(r'\b\w+\b', resume_text)
    skills_mentioned = set([skill.lower() for skill in skills_mentioned])

    # Extract qualifications mentioned in the resume
    qualifications_mentioned = required_qualification_pattern.findall(resume_text.lower())
    # print(qualifications_mentioned)
    # print(skills_mentioned)
    # Calculate score based on skills and qualifications
    score = 0
    for skill in required_skills:
        if skill.lower() in skills_mentioned:
            score += 2  # Each required skill contributes 2 points to the score
    if len(qualifications_mentioned) > 0:
        # score += 4  # Meeting the qualification criteria contributes 4 points to the score
        eligibility = True
    else:
        eligibility =  False
    return score,eligibility

def evaluate_resume(resume_path,mail):
    """
    Evaluate a resume and determine pass or fail based on the score.

    Args:
    - resume_path (str): The path to the resume PDF file.

    Returns:
    - str: "Pass" if the resume score is above 6, otherwise "Fail".
    """
    # Extract text from the resume PDF
    resume_text = extract_text_from_pdf(resume_path)
    if resume_text is None:
        return "Fail (Unable to extract text from the resume)"

    # Analyze the resume to determine the score
    score,eligiblity = analyze_resume(resume_text)
    
    # Determine pass or fail based on the score
    if eligiblity and score > 6:
        accept_mail(mail)
        print("Pass")
    else:
        reject_mail(mail)
        print("Fail")

# Example usage:
# resume_path = "resume.pdf"
# mail =  "csnobel2001@gmail.com"
# evaluate_resume(resume_path,mail)
# print("Result:", result)