from medical_email import analyze_medical_record
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from functools import partial
def analysis(emailid):
    def upload_image_and_analyze(window, emailid):
        # Function to upload an image and call analyze_medical_record function
        # Open file dialog to select an image file
        image_path = filedialog.askopenfilename(initialdir="/", title="Select Image File", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
        if image_path:
            # Call analyze_medical_record function with the uploaded image path and email ID
            analyze_medical_record(image_path, emailid)
            # Close the window after analysis
            window.destroy()
    # Create the main window
    window = tk.Tk()
    window.title("Upload Image and Analyze")
    # Create a button to upload image and trigger analysis
    upload_button = tk.Button(window, text="Upload Image", command=lambda: upload_image_and_analyze(window, emailid))
    upload_button.pack()

    # Run the main event loop
    window.mainloop()
