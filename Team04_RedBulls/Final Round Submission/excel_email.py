import pandas as pd

def find_mail(name):
    # Read the Excel file into a DataFrame
    excel_file = 'employeedata.xlsx'  # Provide the path to your Excel file
    df = pd.read_excel(excel_file)

    # Access the columns containing employee names and email addresses
    employee_names = df['name']  
    employee_emails = df['email']  

    # Iterate through the DataFrame to find the email corresponding to the given name
    for n, email in zip(employee_names, employee_emails):
        if n == name:
            return email
