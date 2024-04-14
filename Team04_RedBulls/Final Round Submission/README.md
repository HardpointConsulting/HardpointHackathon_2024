# Problem Statement
Lack of appointing HR staffs in medium sized enterprises always raises the question of authenticity,as there exists no communication channels for the company staffs to enquire about their queries or others to know about the details on new recruitments.
To get rid of this prevailing challenge,we have developed a smart HR-gpt that can automate the tasks done by an HR personnel such as responding to employee queries on leave requests,salary,incentives and other allowances. It also does the work of verifying CVs, shortlisting candidates and scheduling their interviews.

# What does the HR Bot do?
The HR bot streamlines employee inquiries and automates routine HR tasks, enhancing efficiency and responsiveness within the workplace. The HR bot manages leave requests and responds to them via email, while also handling job applications by receiving details and resumes, and subsequently sending acceptance or rejection emails to candidates. Through natural language processing and machine learning algorithms, it provides personalized assistance and fosters a smoother employee experience.

![Working diagram of HR-bot](https://github.com/HardpointConsulting/HardpointHackathon_2024/assets/97967333/950d346a-31f3-4ca5-8033-61ffe411e60e)


# How does it work
   
   ![Flowchart of HR-bot](https://github.com/HardpointConsulting/HardpointHackathon_2024/assets/97967333/504f3290-d854-428c-bfc7-072803f17193)
   
The HR bot operates in two main sections: "Apply for Job" and "Employee."

Within the "Employee" section, users can log in to pose queries. These are addressed using pre-trained knowledge sourced from the company's terms and policies, which are stored as vectors on Chroma. FAISS matches similar queries, and ChatOpenAI reconstructs matched queries. Employees can also request leave by uploading a medical certificate. The certificate's text is extracted using pytesseract, and essential details such as the patient's name, illness, and leave duration are verified to determine whether to approve or reject the request. A return email confirms the decision.

![IMG_20240413_162527](https://github.com/HardpointConsulting/HardpointHackathon_2024/assets/97967333/0f298291-45ee-4a6e-b52e-6adfeec2d6bf)

In the "Apply for Job" section, new candidates submit their details and resume. The system analyzes this information through an ATS like system and sends either an acceptance or rejection email. Additionally, the entered details are stored for future reference.

   
# Tools Used
* Langchain
* PIL
* PyPDF2
* Pytesseract
* smtplib
* Streamlit
* Chroma
* Openai
* Pandas
* FAISS


# How to Run the Code
Note : The code was written using ```Python 3.10``` version.
1. Clone the git repository using
```javascript
git clone git@github.com:HardpointConsulting/HardpointHackathon_2024.git
```
2. Go to directory
```javascript
cd Team04_RedBulls/Final Round Submission/UPDATED CODE 14-04-24
```
3. Install necessary libraries by running
```javascript
pip install -r requirements.txt
```
4. Add pytesseract to your path in ```medical_email.py```.
5. Add ```Email``` and ```Email APP Password``` in ```medical_email.py``` and ```resume_email.py```
6. Insert the neccessary ```API_KEY``` in ```.env``` file for HuggingFace and OpenAI.
7. Run home.py using
```javascript
streamlit run home.py
```
8. The default ```username``` and ```password``` are "admin" and "admin123".

# Future Scope
* The HR-bot could expand its functionality to include the assessment and rating of employee performance, along with the ability to track their ongoing work and progress.
* Enhance its capabilities by integrating voice search functionality, enabling users to access HR services and information through spoken commands and queries.
* Training new Employees.
* Including on boarding of new employees.

# Demo
### Login Interface for Employee
<img width="960" alt="login" src="https://github.com/HardpointConsulting/HardpointHackathon_2024/assets/97967333/e9fa8c62-9621-40bf-9628-56adf3980123">


### Chatbot Interface
<img width="960" alt="salary query" src="https://github.com/HardpointConsulting/HardpointHackathon_2024/assets/97967333/5a80e8bc-9c6a-4e6f-abaf-35bfdefbe3bd">

<img width="960" alt="leave" src="https://github.com/HardpointConsulting/HardpointHackathon_2024/assets/97967333/c77dda2c-de60-4224-ab77-43ef0bac292c">



### Job Application Interface
<img width="960" alt="candidate" src="https://github.com/HardpointConsulting/HardpointHackathon_2024/assets/97967333/0d0b4b0d-999a-428d-82db-17b1f4f43048">


### Response Email Examples for both Leave application & Job Application

![image](https://github.com/HardpointConsulting/HardpointHackathon_2024/assets/97967333/48cde803-9990-4928-bb18-326513227064)


![image](https://github.com/HardpointConsulting/HardpointHackathon_2024/assets/97967333/9f591ae1-d400-4bce-8e62-5b7da25c7879)



