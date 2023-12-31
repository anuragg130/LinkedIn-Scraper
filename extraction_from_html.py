# -*- coding: utf-8 -*-
"""extraction-from-html.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15j92-cV3MwmowMpuhtHx6y3WrNMj5AsF
"""

from bs4 import BeautifulSoup

import pandas as pd

# Read the HTML file
file_path = r'D:\EY\LinkedIn-Job-Scraper\LinkedIn Job (4).html'  # Replace with the path to your HTML file
with open(file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table element in the HTML
table = soup.find('table')

# Extract the table headers (column names)
headers = [header.text for header in table.find_all('th')]

# Extract the table rows and their values
rows = []
for row in table.find_all('tr'):
    row_data = [cell.text for cell in row.find_all('td')]
    rows.append(row_data)

# Create a Pandas DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save the DataFrame to an Excel file
excel_file_path = 'D:\EY\LinkedIn-Job-Scraper/output100.xlsx'  # Replace with the desired output file path
df.to_excel(excel_file_path, index=False)

print("Table saved to Excel successfully!")

