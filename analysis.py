# Iris Data Set
# Author : Joanna Mnich

# 1: Source the Data Set

# The Iris dataset was loaded using url from UC Irvine Machine Learning Repository archive.
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# uploaded data is stored in zip file in library
# function return with iris data

import pandas as pd
import zipfile
from io import BytesIO

# Define the local path to the ZIP file
zip_file_path = 'iris_data.txt'  # Update with the correct path to your local ZIP file

# Define column names based on the dataset description
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Open the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # List the contents of the ZIP file to check if the expected file exists
    zip_ref.printdir()
    
    # Extract the CSV file from the ZIP archive
    # Assuming the CSV file is named 'iris.data'
    csv_file = 'iris.data'  # Adjust this if the file name is different inside the ZIP
    
    # Read the extracted CSV file into a DataFrame
    with zip_ref.open(csv_file) as my_file:
        df = pd.read_csv(my_file, names=column_names)

# Print the first few rows of the DataFrame
print(df.head())

