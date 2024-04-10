#call analysis(email)
from excel_email import find_mail
from resume_email import evaluate_resume
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from functools import partial
def analysis(emailid):
    def upload_pdf_and_analyze(window, emailid):
    # Function to upload a PDF file and call analyze_medical_record function
    # Open file dialog to select a PDF file
        pdf_path = filedialog.askopenfilename(initialdir="/", title="Select PDF File", filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
        if pdf_path:
            # Call analyze_medical_record function with the uploaded PDF path and email ID
            evaluate_resume(pdf_path, emailid)
            # Close the window after analysis
            window.destroy()

    # Create the main window
    window = tk.Tk()
    window.title("Upload Image and Analyze")
    # Create a button to upload image and trigger analysis
    upload_button = tk.Button(window, text="Upload PDF", command=lambda: upload_pdf_and_analyze(window, emailid))
    upload_button.pack()


    # Run the main event loop
    window.mainloop()
# example
username = "Mark Delos Santos"
email = find_mail(username)
analysis(email)