from PIL import Image
import os
import pytesseract

# Path to the folder containing images
folder_path = 'E:/Hackathon/pics'

# Custom Tesseract OCR configuration
custom_config = r"--psm 6 --oem 3"

# Function to extract text from images using Tesseract OCR
def extract_text_with_tesseract(folder_path):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Configure Tesseract OCR
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Iterate through each image file in the folder
    for file in image_files:
        image_path = os.path.join(folder_path, file)
        
        # Open the image using Pillow
        img = Image.open(image_path)
        
        # Convert the image to grayscale
        gray_img = img.convert('L')
        
        # Perform OCR on the image
        data= pytesseract.image_to_data(img, output_type='dict')
        text = pytesseract.image_to_string(img, config=custom_config)
        
        # Extract confidence levels for each word
        confidences = [int(conf) for conf in data['conf'] if str(conf).isdigit()]  # Check if conf is digit before conversion

    
        if confidences:
            accuracy = sum(confidences) / len(confidences)
        else:
            accuracy = 0

    
        # Use Tesseract OCR to extract text from the grayscale image with custom configuration
        extracted_text = pytesseract.image_to_string(gray_img, config=custom_config)

        
        # Save the extracted text to a text file
        text_file_path = os.path.splitext(image_path)[0] + '.txt'
        with open(text_file_path, 'w') as text_file:
            text_file.write(extracted_text)
        
        # Extract title and author from the text
        lines = extracted_text.split('\n')
        potential_lines = lines[:10]
        title = potential_lines[0]
        authors = []

        for line in potential_lines:
            if "by" in line.lower() or "and" in line.lower():
                authors.extend(line.split("by" if "by" in line.lower() else "and"))

         #Clean up author names
        authors = [author.strip() for author in authors if author.strip()]

        # Print title and authors
        print("Title:", title)
        print("Authors:", authors)
        # Call the function to extract text from images in the folder using Tesseract OCR
extract_text_with_tesseract(folder_path)
