# Iris Data Set
# Author : Joanna Mnich

# 1: Source the Data Set

import pandas as pd

# Define column names based on the dataset structure
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Read the .data file with no header row
df = pd.read_csv('iris_data/iris.data', names=column_names)

# Preview the data
print(df.head())


