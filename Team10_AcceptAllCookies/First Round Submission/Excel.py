import pandas as pd

titles_str = generate_title_from_files(folder_path)
authors_str = #add func calls
generated_titles_str = #here too
# Split the input strings into lists
titles = titles_str.split(', ')
authors = authors_str.split(', ')
generated_titles = generated_titles_str.split(', ')

# Create a DataFrame
data = {
    'Title': titles,
    'Authors': authors,
    'Generated Title': generated_titles
}
df = pd.DataFrame(data)

# Specify the file path for the Excel file
file_path = "E:/Hackathon//test.xlsx"

# Write the DataFrame to an Excel file
df.to_excel(file_path, index=False)

print("Excel sheet generated successfully!")
