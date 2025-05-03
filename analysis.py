# Iris Data Set
# Author : Joanna Mnich

# 1: Source the Data Set

import pandas as pd
import math
import os

# Define column names based on the dataset structure
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Read the .data file with no header row
df = pd.read_csv('iris_data/iris.data', names=column_names)

# Check the shape of the dataset
print("Shape of the dataset: ", df.shape)


# Preview the data
print(df.head())



''''
# Calculate the mean of each feature

variable_means = df.mean(numeric_only=True)
print("Mean of each variable:")
print(variable_means)

# Calculate the minimum of each feature

variable_minimum = df.min()
print("Minimum of each variable:")
print(variable_minimum)

# Calculate the maximum of each feature

variable_maximum = df.max()
print("Maximum of each variable:")
print(variable_maximum)

# Calculate the standard deviation of each feature

variable_stdev = df.std()
print("Standard Deviation of each variable:")
print(variable_stdev)

# Calculate the median of each feature

variable_median = df.median()
print("Median of each variable:")
print(variable_median)
'''
