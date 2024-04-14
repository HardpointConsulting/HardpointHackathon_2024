import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def reject_mail(mail,name):
        password = "<PASSWORD>"  # Replace with your Gmail app password
        me = "<COMPANY_MAIL>"  # Replace with your email address
        email_body = f"""\
        <html>
        <body>
        <p>Dear {name},<br><br>
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

def accept_mail(mail,name):
        password = "<PASSWORD>"  # Replace with your Gmail app password
        me = "<COMPANY_MAIL>"  # Replace with your email address
        email_body = f"""\
        <html>
        <body>
        <p>Dear {name},<br><br>
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
 
    # Define required skills
    required_skills = {"C", "Python", "SQL", "communication", "networking"}

    # Define required qualifications
    required_qualification_pattern = re.compile(r"(?i)(bca|cs|data science|computer application|ai aiml|ml|machine learning|computer science)")

    # Extract skills mentioned in the resume
    skills_mentioned = re.findall(r'\b\w+\b', resume_text)
    skills_mentioned = set([skill.lower() for skill in skills_mentioned])

    # Extract qualifications mentioned in the resume
    qualifications_mentioned = required_qualification_pattern.findall(resume_text.lower())
    
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

def evaluate_resume(resume_path,mail,name):
   
    # Extract text from the resume PDF
    resume_text = extract_text_from_pdf(resume_path)
    if resume_text is None:
        return "Fail (Unable to extract text from the resume)"

    # Analyze the resume to determine the score
    score,eligiblity = analyze_resume(resume_text)
    
    # Determine pass or fail based on the score
    if eligiblity and score > 6:
        accept_mail(mail,name)
        print("Pass")
    else:
        reject_mail(mail,name)
        print("Fail")
